# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eleven_tts.api_client import ApiClient


class VoicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_voice_v1_voices_add_post(self, name, files, **kwargs):  # noqa: E501
        """Add Voice  # noqa: E501

        Add a new voice to your collection of voices in VoiceLab.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_voice_v1_voices_add_post(name, files, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param list[str] files: (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenAddVoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_voice_v1_voices_add_post_with_http_info(name, files, **kwargs)  # noqa: E501
        else:
            (data) = self.add_voice_v1_voices_add_post_with_http_info(name, files, **kwargs)  # noqa: E501
            return data

    def add_voice_v1_voices_add_post_with_http_info(self, name, files, **kwargs):  # noqa: E501
        """Add Voice  # noqa: E501

        Add a new voice to your collection of voices in VoiceLab.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_voice_v1_voices_add_post_with_http_info(name, files, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param list[str] files: (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenAddVoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'files', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_voice_v1_voices_add_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `add_voice_v1_voices_add_post`")  # noqa: E501
        # verify the required parameter 'files' is set
        if ('files' not in params or
                params['files'] is None):
            raise ValueError("Missing the required parameter `files` when calling `add_voice_v1_voices_add_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'files' in params:
            form_params.append(('files', params['files']))  # noqa: E501
            collection_formats['files'] = 'multi'  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElevenAddVoiceResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_voice_v1_voices_voice_id_delete(self, voice_id, **kwargs):  # noqa: E501
        """Delete Voice  # noqa: E501

        Deletes a voice by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_voice_v1_voices_voice_id_delete(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_voice_v1_voices_voice_id_delete_with_http_info(voice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_voice_v1_voices_voice_id_delete_with_http_info(voice_id, **kwargs)  # noqa: E501
            return data

    def delete_voice_v1_voices_voice_id_delete_with_http_info(self, voice_id, **kwargs):  # noqa: E501
        """Delete Voice  # noqa: E501

        Deletes a voice by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_voice_v1_voices_voice_id_delete_with_http_info(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voice_id', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_voice_v1_voices_voice_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voice_id' is set
        if ('voice_id' not in params or
                params['voice_id'] is None):
            raise ValueError("Missing the required parameter `voice_id` when calling `delete_voice_v1_voices_voice_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voice_id' in params:
            path_params['voice_id'] = params['voice_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/{voice_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_voice_settings_v1_voices_voice_id_settings_edit_post(self, body, voice_id, **kwargs):  # noqa: E501
        """Edit Voice Settings  # noqa: E501

        Edit your settings for a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_voice_settings_v1_voices_voice_id_settings_edit_post(body, voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ElevenSettings body: (required)
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_voice_settings_v1_voices_voice_id_settings_edit_post_with_http_info(body, voice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_voice_settings_v1_voices_voice_id_settings_edit_post_with_http_info(body, voice_id, **kwargs)  # noqa: E501
            return data

    def edit_voice_settings_v1_voices_voice_id_settings_edit_post_with_http_info(self, body, voice_id, **kwargs):  # noqa: E501
        """Edit Voice Settings  # noqa: E501

        Edit your settings for a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_voice_settings_v1_voices_voice_id_settings_edit_post_with_http_info(body, voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ElevenSettings body: (required)
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'voice_id', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_voice_settings_v1_voices_voice_id_settings_edit_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `edit_voice_settings_v1_voices_voice_id_settings_edit_post`")  # noqa: E501
        # verify the required parameter 'voice_id' is set
        if ('voice_id' not in params or
                params['voice_id'] is None):
            raise ValueError("Missing the required parameter `voice_id` when calling `edit_voice_settings_v1_voices_voice_id_settings_edit_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voice_id' in params:
            path_params['voice_id'] = params['voice_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/{voice_id}/settings/edit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_voice_v1_voices_voice_id_edit_post(self, name, files, voice_id, **kwargs):  # noqa: E501
        """Edit Voice  # noqa: E501

        Edit a voice created by you.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_voice_v1_voices_voice_id_edit_post(name, files, voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param list[str] files: (required)
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_voice_v1_voices_voice_id_edit_post_with_http_info(name, files, voice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_voice_v1_voices_voice_id_edit_post_with_http_info(name, files, voice_id, **kwargs)  # noqa: E501
            return data

    def edit_voice_v1_voices_voice_id_edit_post_with_http_info(self, name, files, voice_id, **kwargs):  # noqa: E501
        """Edit Voice  # noqa: E501

        Edit a voice created by you.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_voice_v1_voices_voice_id_edit_post_with_http_info(name, files, voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param list[str] files: (required)
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'files', 'voice_id', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_voice_v1_voices_voice_id_edit_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `edit_voice_v1_voices_voice_id_edit_post`")  # noqa: E501
        # verify the required parameter 'files' is set
        if ('files' not in params or
                params['files'] is None):
            raise ValueError("Missing the required parameter `files` when calling `edit_voice_v1_voices_voice_id_edit_post`")  # noqa: E501
        # verify the required parameter 'voice_id' is set
        if ('voice_id' not in params or
                params['voice_id'] is None):
            raise ValueError("Missing the required parameter `voice_id` when calling `edit_voice_v1_voices_voice_id_edit_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voice_id' in params:
            path_params['voice_id'] = params['voice_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'files' in params:
            form_params.append(('files', params['files']))  # noqa: E501
            collection_formats['files'] = 'multi'  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/{voice_id}/edit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_default_voice_settings_v1_voices_settings_default_get(self, **kwargs):  # noqa: E501
        """Get Default Voice Settings  # noqa: E501

        Gets the default settings for voices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_default_voice_settings_v1_voices_settings_default_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ElevenVoiceSettingsResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_default_voice_settings_v1_voices_settings_default_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_default_voice_settings_v1_voices_settings_default_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_default_voice_settings_v1_voices_settings_default_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Default Voice Settings  # noqa: E501

        Gets the default settings for voices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_default_voice_settings_v1_voices_settings_default_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ElevenVoiceSettingsResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_default_voice_settings_v1_voices_settings_default_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/settings/default', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElevenVoiceSettingsResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_voice_settings_v1_voices_voice_id_settings_get(self, voice_id, **kwargs):  # noqa: E501
        """Get Voice Settings  # noqa: E501

        Returns the settings for a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_settings_v1_voices_voice_id_settings_get(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenVoiceSettingsResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_voice_settings_v1_voices_voice_id_settings_get_with_http_info(voice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_voice_settings_v1_voices_voice_id_settings_get_with_http_info(voice_id, **kwargs)  # noqa: E501
            return data

    def get_voice_settings_v1_voices_voice_id_settings_get_with_http_info(self, voice_id, **kwargs):  # noqa: E501
        """Get Voice Settings  # noqa: E501

        Returns the settings for a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_settings_v1_voices_voice_id_settings_get_with_http_info(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenVoiceSettingsResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voice_id', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_voice_settings_v1_voices_voice_id_settings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voice_id' is set
        if ('voice_id' not in params or
                params['voice_id'] is None):
            raise ValueError("Missing the required parameter `voice_id` when calling `get_voice_settings_v1_voices_voice_id_settings_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voice_id' in params:
            path_params['voice_id'] = params['voice_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/{voice_id}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElevenVoiceSettingsResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_voice_v1_voices_voice_id_get(self, voice_id, **kwargs):  # noqa: E501
        """Get Voice  # noqa: E501

        Returns metadata about a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_v1_voices_voice_id_get(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param bool with_settings: If set will return settings information corresponding to the voice, requires authorization.
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenVoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_voice_v1_voices_voice_id_get_with_http_info(voice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_voice_v1_voices_voice_id_get_with_http_info(voice_id, **kwargs)  # noqa: E501
            return data

    def get_voice_v1_voices_voice_id_get_with_http_info(self, voice_id, **kwargs):  # noqa: E501
        """Get Voice  # noqa: E501

        Returns metadata about a specific voice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_v1_voices_voice_id_get_with_http_info(voice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. (required)
        :param bool with_settings: If set will return settings information corresponding to the voice, requires authorization.
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenVoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voice_id', 'with_settings', 'xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_voice_v1_voices_voice_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voice_id' is set
        if ('voice_id' not in params or
                params['voice_id'] is None):
            raise ValueError("Missing the required parameter `voice_id` when calling `get_voice_v1_voices_voice_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voice_id' in params:
            path_params['voice_id'] = params['voice_id']  # noqa: E501

        query_params = []
        if 'with_settings' in params:
            query_params.append(('with_settings', params['with_settings']))  # noqa: E501

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices/{voice_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElevenVoiceResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_voices_v1_voices_get(self, **kwargs):  # noqa: E501
        """Get Voices  # noqa: E501

        Gets a list of all available voices for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voices_v1_voices_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenGetVoicesResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_voices_v1_voices_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_voices_v1_voices_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_voices_v1_voices_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Voices  # noqa: E501

        Gets a list of all available voices for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voices_v1_voices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
        :return: ElevenGetVoicesResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['xi_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_voices_v1_voices_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'xi_api_key' in params:
            header_params['xi-api-key'] = params['xi_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/voices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElevenGetVoicesResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
