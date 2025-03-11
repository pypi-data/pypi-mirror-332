# audio_sdk/transcriber.py

import json
import os
import requests
from http import HTTPStatus
import dashscope.audio
import logging
import uuid
from typing import List, Dict
from docx import Document
from .video_utils import get_cc_video_url
from .save_to_word_srt import  save_to_word,save_to_srt

class AudioTranscriber:
    def __init__(self, api_key: str = None, userid: str = None, salt: str = None,model: str = 'paraformer-v2', log_level: int = logging.INFO):
        """
        初始化转录器，设置 API Key 和模型类型。
        如果未提供 API Key，则尝试从环境变量中获取。
        """

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.api_key = api_key
        if not self.api_key:
            self.logger.error("API Key 未提供。请设置环境变量 DASHSCOPE_API_KEY 或在初始化时提供。")
            raise ValueError("API Key 未提供。")
        dashscope.api_key = self.api_key
        self.model = model
        self.userid = userid
        self.salt = salt


    def transcribe_urls(self, file_urls: List[str], language_hints: List[str] = ['zh', 'en']) :
        """
        开始异步转录任务并等待完成。
        返回转录结果。
        """
        try:
            task_response = dashscope.audio.asr.Transcription.async_call(
                model=self.model,
                file_urls=file_urls,
                language_hints=language_hints
            )
            self.logger.info("成功启动异步转录任务。")
        except Exception as e:
            self.logger.error(f"启动异步转录任务失败: {e}")
            raise RuntimeError("启动异步转录任务失败") from e

        transcription_response = dashscope.audio.asr.Transcription.wait(task=task_response.output.task_id)

        if transcription_response.status_code == HTTPStatus.OK:
            self.logger.info("转录任务完成。")
            return transcription_response.output
        else:
            error_message = transcription_response.output.get('message', '未知错误')
            self.logger.error(f"转录任务失败: {error_message}")
            raise RuntimeError(f"转录任务失败: {error_message}")



    def _save_combined_json(self, results: List[Dict], output_path: str):
        """
        将所有转录结果保存为一个合并的 JSON 文件。
        """
        combined_json = {"transcripts": results}
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(combined_json, f, indent=4, ensure_ascii=False)


    def get_video_urls_by_ids(self, videoids: List[str]) :
        """
        根据视频ID列表获取视频URL列表。
        """
        file_urls = []
        for videoid in videoids:
            video_url = get_cc_video_url(videoid,self.userid,self.salt)
            if video_url:
                file_urls.append(video_url)
                self.logger.info(f"成功获取视频URL: {video_url}")
            else:
                self.logger.warning(f"未能获取视频ID {videoid} 的URL")
        return file_urls

    def parse_transcription_urls(self, transcription_result):
        """
        解析 transcription_url 并下载其内容。
        返回解析后的转录数据列表。
        """
        results = []
        if 'results' not in transcription_result:
            self.logger.error("转录结果缺少 'results' 字段。")
            return results

        for index, item in enumerate(transcription_result['results']):
            transcription_url = item.get('transcription_url')
            if not transcription_url:
                self.logger.warning(f"第 {index} 个转录结果缺少 transcription_url，跳过。")
                continue

            try:
                transcription_data = self._download_and_parse_url(transcription_url, index)
                if transcription_data:
                    results.append(transcription_data)
            except requests.RequestException as e:
                self.logger.error(f"下载第 {index} 个 transcription_url 失败: {e}")
            except json.JSONDecodeError as e:
                self.logger.error(f"解析第 {index} 个 transcription_url 的 JSON 失败: {e}")


        return results

    def _download_and_parse_url(self, url, index):
        """
        下载并解析单个 transcription_url
        """
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        transcription_data = response.json()
        self.logger.info(f"成功下载并解析第 {index} 个 transcription_url 的内容。")
        return transcription_data
    def transcribe_videos_by_ids(self, videoids: List[str], language_hints: List[str] = ['zh', 'en']) -> List[Dict]:
        """
        根据视频ID列表获取视频URL并进行转录。
        返回转录结果。
        """
        file_urls = self.get_video_urls_by_ids(videoids)
        if not file_urls:
            self.logger.error("没有可用的视频URL进行转录。")
            raise ValueError("没有有效的视频URL进行转录。")

        return self.transcribe_urls(file_urls, language_hints)


    def transcribe_and_save_all_by_ids(self, videoids: List[str], output_dir: str = "output") :
        """
        根据视频ID列表完成转录并保存结果为多种格式（TXT, Word, SRT）。
        """
        self.logger.info("开始转录和保存所有视频的结果。")

        # 获取转录结果
        transcription_result = self.transcribe_videos_by_ids(videoids)


        # 解析 transcription_url 并下载其内容
        transcription_data = self.parse_transcription_urls(transcription_result)

        self.logger.info(f"解析后得到 {len(transcription_data)} 个转录结果。")

        saved_files = []
        for idx, transcription in enumerate(transcription_data):

            # 为每个转录结果创建单独的文件
            base_filename = f"transcription_result_{idx + 1}"
            word_output_path = os.path.join(output_dir, f"{base_filename}.docx")
            srt_output_path = os.path.join(output_dir, f"{base_filename}.srt")

            save_to_word(transcription, word_output_path)
            save_to_srt(transcription, srt_output_path)
            saved_files.extend([word_output_path, srt_output_path])

        # 合并所有转录结果到一个文件（可选）
        combined_json_path = os.path.join(output_dir, "transcription_results.json")
        self._save_combined_json(transcription_data, combined_json_path)
        self.logger.info(f"合并的 JSON 文件已保存到 {combined_json_path}")

        self.logger.info("所有转录结果已保存为多种格式。")
        return saved_files + [combined_json_path]