# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import eleven_tts
from eleven_tts.tts.text_to_speech_api import TextToSpeechApi  # noqa: E501
from eleven_tts.rest import ApiException


class TestTextToSpeechApi(unittest.TestCase):
    """TextToSpeechApi unit test stubs"""

    def setUp(self):
        self.api = TextToSpeechApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_text_to_speech_v1_text_to_speech_voice_id_post(self):
        """Test case for text_to_speech_v1_text_to_speech_voice_id_post

        Text To Speech  # noqa: E501
        """
        pass

    def test_text_to_speech_v1_text_to_speech_voice_id_stream_post(self):
        """Test case for text_to_speech_v1_text_to_speech_voice_id_stream_post

        Text To Speech  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
