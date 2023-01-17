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

class ElevenBodyAddVoiceV1VoicesAddPost(object):
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
        'name': 'str',
        'files': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'files': 'files'
    }

    def __init__(self, name=None, files=None):  # noqa: E501
        """ElevenBodyAddVoiceV1VoicesAddPost - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._files = None
        self.discriminator = None
        self.name = name
        self.files = files

    @property
    def name(self):
        """Gets the name of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501

        The name that identifies this voice. This will be displayed in the dropdown of the website.  # noqa: E501

        :return: The name of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElevenBodyAddVoiceV1VoicesAddPost.

        The name that identifies this voice. This will be displayed in the dropdown of the website.  # noqa: E501

        :param name: The name of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def files(self):
        """Gets the files of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501

        One or more audio files to clone the voice from  # noqa: E501

        :return: The files of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ElevenBodyAddVoiceV1VoicesAddPost.

        One or more audio files to clone the voice from  # noqa: E501

        :param files: The files of this ElevenBodyAddVoiceV1VoicesAddPost.  # noqa: E501
        :type: list[str]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

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
        if issubclass(ElevenBodyAddVoiceV1VoicesAddPost, dict):
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
        if not isinstance(other, ElevenBodyAddVoiceV1VoicesAddPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
