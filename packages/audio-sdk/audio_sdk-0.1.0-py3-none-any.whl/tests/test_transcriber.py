# tests/test_transcriber.py

import unittest
from unittest.mock import patch, MagicMock
from audio_sdk import AudioTranscriber

class TestAudioTranscriber(unittest.TestCase):

    @patch('audio_sdk.transcriber.requests.get')
    @patch('dashscope.audio.asr.Transcription.async_call')
    @patch('dashscope.audio.asr.Transcription.wait')
    def test_transcribe_and_save(self, mock_wait, mock_async_call, mock_requests_get):
        # 设置模拟返回值
        mock_async_call.return_value.output.task_id = 'task_123'
        mock_wait.return_value.status_code = 200
        mock_wait.return_value.output.results = [
            {'transcription_url': 'http://example.com/result1.json'},
            {'transcription_url': 'http://example.com/result2.json'}
        ]
        mock_requests_get.side_effect = [
            unittest.mock.Mock(text=json.dumps({'text': '测试结果1'}), status_code=200),
            unittest.mock.Mock(text=json.dumps({'text': '测试结果2'}), status_code=200)
        ]

        transcriber = AudioTranscriber(api_key='test_api_key')
        saved_files = transcriber.transcribe_and_save(['http://example.com/audio1.mp4'], output_dir='tests/output')

        self.assertEqual(len(saved_files), 2)
        self.assertTrue(any('transcription_result_1_' in file for file in saved_files))
        self.assertTrue(any('transcription_result_2_' in file for file in saved_files))

if __name__ == '__main__':
    unittest.main()