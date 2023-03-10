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

class VoiceResponseModel(object):
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
        'voice_id': 'str',
        'name': 'str',
        'samples': 'list[SampleResponseModel]',
        'category': 'str',
        'available_for_tiers': 'list[str]',
        'settings': 'VoiceSettingsResponseModel'
    }

    attribute_map = {
        'voice_id': 'voice_id',
        'name': 'name',
        'samples': 'samples',
        'category': 'category',
        'available_for_tiers': 'available_for_tiers',
        'settings': 'settings'
    }

    def __init__(self, voice_id=None, name=None, samples=None, category=None, available_for_tiers=None, settings=None):  # noqa: E501
        """VoiceResponseModel - a model defined in Swagger"""  # noqa: E501
        self._voice_id = None
        self._name = None
        self._samples = None
        self._category = None
        self._available_for_tiers = None
        self._settings = None
        self.discriminator = None
        self.voice_id = voice_id
        self.name = name
        self.samples = samples
        self.category = category
        self.available_for_tiers = available_for_tiers
        self.settings = settings

    @property
    def voice_id(self):
        """Gets the voice_id of this VoiceResponseModel.  # noqa: E501


        :return: The voice_id of this VoiceResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._voice_id

    @voice_id.setter
    def voice_id(self, voice_id):
        """Sets the voice_id of this VoiceResponseModel.


        :param voice_id: The voice_id of this VoiceResponseModel.  # noqa: E501
        :type: str
        """
        if voice_id is None:
            raise ValueError("Invalid value for `voice_id`, must not be `None`")  # noqa: E501

        self._voice_id = voice_id

    @property
    def name(self):
        """Gets the name of this VoiceResponseModel.  # noqa: E501


        :return: The name of this VoiceResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VoiceResponseModel.


        :param name: The name of this VoiceResponseModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def samples(self):
        """Gets the samples of this VoiceResponseModel.  # noqa: E501


        :return: The samples of this VoiceResponseModel.  # noqa: E501
        :rtype: list[SampleResponseModel]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this VoiceResponseModel.


        :param samples: The samples of this VoiceResponseModel.  # noqa: E501
        :type: list[SampleResponseModel]
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")  # noqa: E501

        self._samples = samples

    @property
    def category(self):
        """Gets the category of this VoiceResponseModel.  # noqa: E501


        :return: The category of this VoiceResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VoiceResponseModel.


        :param category: The category of this VoiceResponseModel.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def available_for_tiers(self):
        """Gets the available_for_tiers of this VoiceResponseModel.  # noqa: E501


        :return: The available_for_tiers of this VoiceResponseModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_for_tiers

    @available_for_tiers.setter
    def available_for_tiers(self, available_for_tiers):
        """Sets the available_for_tiers of this VoiceResponseModel.


        :param available_for_tiers: The available_for_tiers of this VoiceResponseModel.  # noqa: E501
        :type: list[str]
        """
        if available_for_tiers is None:
            raise ValueError("Invalid value for `available_for_tiers`, must not be `None`")  # noqa: E501

        self._available_for_tiers = available_for_tiers

    @property
    def settings(self):
        """Gets the settings of this VoiceResponseModel.  # noqa: E501


        :return: The settings of this VoiceResponseModel.  # noqa: E501
        :rtype: VoiceSettingsResponseModel
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this VoiceResponseModel.


        :param settings: The settings of this VoiceResponseModel.  # noqa: E501
        :type: VoiceSettingsResponseModel
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

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
        if issubclass(VoiceResponseModel, dict):
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
        if not isinstance(other, VoiceResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
