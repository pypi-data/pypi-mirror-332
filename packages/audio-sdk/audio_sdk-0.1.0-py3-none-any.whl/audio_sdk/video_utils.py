# audio_sdk/video_utils.py

import requests
import hashlib
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_cc_video_url(videoid, userid, salt):
    """
    获取 CC 视频的播放 URL。

    :param videoid: 视频的唯一标识符。
    :param userid: 用户 ID，默认为 "45BBAA286764DB35"。
    :param salt: 固定的盐值，默认为 "tdYRayZIr5ZGIByzOeanRvnUHLMP1I07"。
    :return: 返回视频的播放 URL 或 None 如果请求失败。
    """
    # 基础URL
    base_url = "https://spark.bokecc.com/api/video/original"
    print(userid, salt)

    # 定义初始参数
    params = {
        "userid": userid,
        "videoid": videoid
    }

    # 获取当前时间戳（毫秒）
    time_stamp = int(time.time() * 1000)

    # 参数排序和拼接
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{key}={value}" for key, value in sorted_params])
    pre_hash_string = f"{query_string}&time={time_stamp}&salt={salt}"

    # MD5 加密
    md5 = hashlib.md5()
    md5.update(pre_hash_string.encode("utf-8"))
    hash_value = md5.hexdigest().upper()

    # 最终查询字符串
    final_query_string = f"{query_string}&time={time_stamp}&hash={hash_value}"
    full_url = f"{base_url}?{final_query_string}"

    try:
        logger.info(f"发送GET请求到: {full_url}")
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()

        response_data = response.json()
        logger.debug(f"响应JSON数据: {response_data}")

        if "video" in response_data and "url" in response_data["video"]:
            video_url = response_data["video"]["url"]
            logger.info(f"成功获取视频URL: {video_url}")
            return video_url
        else:
            logger.warning("响应中没有找到视频URL字段")
            return None

    except requests.RequestException as e:
        logger.error(f"请求发生错误: {e}")
    except ValueError:
        logger.error("响应内容不是有效的JSON")
    except Exception as e:
        logger.error(f"发生未知错误: {e}")

    return None