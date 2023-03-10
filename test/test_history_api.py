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
from eleven_tts.tts.history_api import HistoryApi  # noqa: E501
from eleven_tts.rest import ApiException


class TestHistoryApi(unittest.TestCase):
    """HistoryApi unit test stubs"""

    def setUp(self):
        self.api = HistoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_history_item_v1_history_history_item_id_delete(self):
        """Test case for delete_history_item_v1_history_history_item_id_delete

        Delete History Item  # noqa: E501
        """
        pass

    def test_delete_history_items_v1_history_delete_post(self):
        """Test case for delete_history_items_v1_history_delete_post

        Delete History Items  # noqa: E501
        """
        pass

    def test_download_history_items_v1_history_download_post(self):
        """Test case for download_history_items_v1_history_download_post

        Download History Items  # noqa: E501
        """
        pass

    def test_get_audio_from_history_item_v1_history_history_item_id_audio_get(self):
        """Test case for get_audio_from_history_item_v1_history_history_item_id_audio_get

        Get Audio From History Item  # noqa: E501
        """
        pass

    def test_get_generated_items_v1_history_get(self):
        """Test case for get_generated_items_v1_history_get

        Get Generated Items  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
