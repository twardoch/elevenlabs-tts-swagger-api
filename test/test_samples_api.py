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
from eleven_tts.tts.samples_api import SamplesApi  # noqa: E501
from eleven_tts.rest import ApiException


class TestSamplesApi(unittest.TestCase):
    """SamplesApi unit test stubs"""

    def setUp(self):
        self.api = SamplesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_sample_v1_voices_voice_id_samples_sample_id_delete(self):
        """Test case for delete_sample_v1_voices_voice_id_samples_sample_id_delete

        Delete Sample  # noqa: E501
        """
        pass

    def test_get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get(self):
        """Test case for get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get

        Get Audio From Sample  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
