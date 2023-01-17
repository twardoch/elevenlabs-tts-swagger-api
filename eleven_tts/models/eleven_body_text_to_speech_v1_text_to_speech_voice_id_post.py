# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str'
    }

    attribute_map = {
        'text': 'text'
    }

    def __init__(self, text=None):  # noqa: E501
        """ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self.discriminator = None
        self.text = text

    @property
    def text(self):
        """Gets the text of this ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost.  # noqa: E501

        The text that will get converted into speech. Currently only English text is supported.  # noqa: E501

        :return: The text of this ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost.

        The text that will get converted into speech. Currently only English text is supported.  # noqa: E501

        :param text: The text of this ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ElevenBodyTextToSpeechV1TextToSpeechVoiceIdPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
