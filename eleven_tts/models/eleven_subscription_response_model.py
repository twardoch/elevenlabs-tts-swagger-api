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

class ElevenSubscriptionResponseModel(object):
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
        'tier': 'str',
        'character_count': 'int',
        'character_limit': 'int',
        'can_extend_character_limit': 'bool',
        'next_character_count_reset_unix': 'int',
        'voice_limit': 'int',
        'can_extend_voice_limit': 'bool'
    }

    attribute_map = {
        'tier': 'tier',
        'character_count': 'character_count',
        'character_limit': 'character_limit',
        'can_extend_character_limit': 'can_extend_character_limit',
        'next_character_count_reset_unix': 'next_character_count_reset_unix',
        'voice_limit': 'voice_limit',
        'can_extend_voice_limit': 'can_extend_voice_limit'
    }

    def __init__(self, tier=None, character_count=None, character_limit=None, can_extend_character_limit=None, next_character_count_reset_unix=None, voice_limit=None, can_extend_voice_limit=None):  # noqa: E501
        """ElevenSubscriptionResponseModel - a model defined in Swagger"""  # noqa: E501
        self._tier = None
        self._character_count = None
        self._character_limit = None
        self._can_extend_character_limit = None
        self._next_character_count_reset_unix = None
        self._voice_limit = None
        self._can_extend_voice_limit = None
        self.discriminator = None
        self.tier = tier
        self.character_count = character_count
        self.character_limit = character_limit
        self.can_extend_character_limit = can_extend_character_limit
        self.next_character_count_reset_unix = next_character_count_reset_unix
        self.voice_limit = voice_limit
        self.can_extend_voice_limit = can_extend_voice_limit

    @property
    def tier(self):
        """Gets the tier of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The tier of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this ElevenSubscriptionResponseModel.


        :param tier: The tier of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: str
        """
        if tier is None:
            raise ValueError("Invalid value for `tier`, must not be `None`")  # noqa: E501

        self._tier = tier

    @property
    def character_count(self):
        """Gets the character_count of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The character_count of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._character_count

    @character_count.setter
    def character_count(self, character_count):
        """Sets the character_count of this ElevenSubscriptionResponseModel.


        :param character_count: The character_count of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: int
        """
        if character_count is None:
            raise ValueError("Invalid value for `character_count`, must not be `None`")  # noqa: E501

        self._character_count = character_count

    @property
    def character_limit(self):
        """Gets the character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._character_limit

    @character_limit.setter
    def character_limit(self, character_limit):
        """Sets the character_limit of this ElevenSubscriptionResponseModel.


        :param character_limit: The character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: int
        """
        if character_limit is None:
            raise ValueError("Invalid value for `character_limit`, must not be `None`")  # noqa: E501

        self._character_limit = character_limit

    @property
    def can_extend_character_limit(self):
        """Gets the can_extend_character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The can_extend_character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._can_extend_character_limit

    @can_extend_character_limit.setter
    def can_extend_character_limit(self, can_extend_character_limit):
        """Sets the can_extend_character_limit of this ElevenSubscriptionResponseModel.


        :param can_extend_character_limit: The can_extend_character_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: bool
        """
        if can_extend_character_limit is None:
            raise ValueError("Invalid value for `can_extend_character_limit`, must not be `None`")  # noqa: E501

        self._can_extend_character_limit = can_extend_character_limit

    @property
    def next_character_count_reset_unix(self):
        """Gets the next_character_count_reset_unix of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The next_character_count_reset_unix of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._next_character_count_reset_unix

    @next_character_count_reset_unix.setter
    def next_character_count_reset_unix(self, next_character_count_reset_unix):
        """Sets the next_character_count_reset_unix of this ElevenSubscriptionResponseModel.


        :param next_character_count_reset_unix: The next_character_count_reset_unix of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: int
        """
        if next_character_count_reset_unix is None:
            raise ValueError("Invalid value for `next_character_count_reset_unix`, must not be `None`")  # noqa: E501

        self._next_character_count_reset_unix = next_character_count_reset_unix

    @property
    def voice_limit(self):
        """Gets the voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._voice_limit

    @voice_limit.setter
    def voice_limit(self, voice_limit):
        """Sets the voice_limit of this ElevenSubscriptionResponseModel.


        :param voice_limit: The voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: int
        """
        if voice_limit is None:
            raise ValueError("Invalid value for `voice_limit`, must not be `None`")  # noqa: E501

        self._voice_limit = voice_limit

    @property
    def can_extend_voice_limit(self):
        """Gets the can_extend_voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501


        :return: The can_extend_voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._can_extend_voice_limit

    @can_extend_voice_limit.setter
    def can_extend_voice_limit(self, can_extend_voice_limit):
        """Sets the can_extend_voice_limit of this ElevenSubscriptionResponseModel.


        :param can_extend_voice_limit: The can_extend_voice_limit of this ElevenSubscriptionResponseModel.  # noqa: E501
        :type: bool
        """
        if can_extend_voice_limit is None:
            raise ValueError("Invalid value for `can_extend_voice_limit`, must not be `None`")  # noqa: E501

        self._can_extend_voice_limit = can_extend_voice_limit

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
        if issubclass(ElevenSubscriptionResponseModel, dict):
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
        if not isinstance(other, ElevenSubscriptionResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
