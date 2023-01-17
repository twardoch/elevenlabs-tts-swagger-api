# eleven_tts.VoicesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_voice_v1_voices_add_post**](VoicesApi.md#add_voice_v1_voices_add_post) | **POST** /v1/voices/add | Add Voice
[**delete_voice_v1_voices_voice_id_delete**](VoicesApi.md#delete_voice_v1_voices_voice_id_delete) | **DELETE** /v1/voices/{voice_id} | Delete Voice
[**edit_voice_settings_v1_voices_voice_id_settings_edit_post**](VoicesApi.md#edit_voice_settings_v1_voices_voice_id_settings_edit_post) | **POST** /v1/voices/{voice_id}/settings/edit | Edit Voice Settings
[**edit_voice_v1_voices_voice_id_edit_post**](VoicesApi.md#edit_voice_v1_voices_voice_id_edit_post) | **POST** /v1/voices/{voice_id}/edit | Edit Voice
[**get_default_voice_settings_v1_voices_settings_default_get**](VoicesApi.md#get_default_voice_settings_v1_voices_settings_default_get) | **GET** /v1/voices/settings/default | Get Default Voice Settings
[**get_voice_settings_v1_voices_voice_id_settings_get**](VoicesApi.md#get_voice_settings_v1_voices_voice_id_settings_get) | **GET** /v1/voices/{voice_id}/settings | Get Voice Settings
[**get_voice_v1_voices_voice_id_get**](VoicesApi.md#get_voice_v1_voices_voice_id_get) | **GET** /v1/voices/{voice_id} | Get Voice
[**get_voices_v1_voices_get**](VoicesApi.md#get_voices_v1_voices_get) | **GET** /v1/voices | Get Voices

# **add_voice_v1_voices_add_post**
> ElevenAddVoiceResponseModel add_voice_v1_voices_add_post(name, files, xi_api_key=xi_api_key)

Add Voice

Add a new voice to your collection of voices in VoiceLab.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
name = 'name_example' # str | 
files = ['files_example'] # list[str] | 
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Add Voice
    api_response = api_instance.add_voice_v1_voices_add_post(name, files, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->add_voice_v1_voices_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenAddVoiceResponseModel**](ElevenAddVoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_v1_voices_voice_id_delete**
> object delete_voice_v1_voices_voice_id_delete(voice_id, xi_api_key=xi_api_key)

Delete Voice

Deletes a voice by its ID.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Delete Voice
    api_response = api_instance.delete_voice_v1_voices_voice_id_delete(voice_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->delete_voice_v1_voices_voice_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_voice_settings_v1_voices_voice_id_settings_edit_post**
> object edit_voice_settings_v1_voices_voice_id_settings_edit_post(body, voice_id, xi_api_key=xi_api_key)

Edit Voice Settings

Edit your settings for a specific voice.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
body = eleven_tts.ElevenSettings() # ElevenSettings | 
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Edit Voice Settings
    api_response = api_instance.edit_voice_settings_v1_voices_voice_id_settings_edit_post(body, voice_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->edit_voice_settings_v1_voices_voice_id_settings_edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElevenSettings**](ElevenSettings.md)|  | 
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_voice_v1_voices_voice_id_edit_post**
> object edit_voice_v1_voices_voice_id_edit_post(name, files, voice_id, xi_api_key=xi_api_key)

Edit Voice

Edit a voice created by you.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
name = 'name_example' # str | 
files = ['files_example'] # list[str] | 
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Edit Voice
    api_response = api_instance.edit_voice_v1_voices_voice_id_edit_post(name, files, voice_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->edit_voice_v1_voices_voice_id_edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | 
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_voice_settings_v1_voices_settings_default_get**
> ElevenVoiceSettingsResponseModel get_default_voice_settings_v1_voices_settings_default_get()

Get Default Voice Settings

Gets the default settings for voices.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()

try:
    # Get Default Voice Settings
    api_response = api_instance.get_default_voice_settings_v1_voices_settings_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->get_default_voice_settings_v1_voices_settings_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ElevenVoiceSettingsResponseModel**](ElevenVoiceSettingsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_settings_v1_voices_voice_id_settings_get**
> ElevenVoiceSettingsResponseModel get_voice_settings_v1_voices_voice_id_settings_get(voice_id, xi_api_key=xi_api_key)

Get Voice Settings

Returns the settings for a specific voice.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Voice Settings
    api_response = api_instance.get_voice_settings_v1_voices_voice_id_settings_get(voice_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->get_voice_settings_v1_voices_voice_id_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenVoiceSettingsResponseModel**](ElevenVoiceSettingsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_v1_voices_voice_id_get**
> ElevenVoiceResponseModel get_voice_v1_voices_voice_id_get(voice_id, with_settings=with_settings, xi_api_key=xi_api_key)

Get Voice

Returns metadata about a specific voice.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
with_settings = false # bool | If set will return settings information corresponding to the voice, requires authorization. (optional) (default to false)
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Voice
    api_response = api_instance.get_voice_v1_voices_voice_id_get(voice_id, with_settings=with_settings, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->get_voice_v1_voices_voice_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **with_settings** | **bool**| If set will return settings information corresponding to the voice, requires authorization. | [optional] [default to false]
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenVoiceResponseModel**](ElevenVoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voices_v1_voices_get**
> ElevenGetVoicesResponseModel get_voices_v1_voices_get(xi_api_key=xi_api_key)

Get Voices

Gets a list of all available voices for a user.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.VoicesApi()
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Voices
    api_response = api_instance.get_voices_v1_voices_get(xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicesApi->get_voices_v1_voices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenGetVoicesResponseModel**](ElevenGetVoicesResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

