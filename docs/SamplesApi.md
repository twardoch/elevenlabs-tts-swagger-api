# eleven_tts.SamplesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sample_v1_voices_voice_id_samples_sample_id_delete**](SamplesApi.md#delete_sample_v1_voices_voice_id_samples_sample_id_delete) | **DELETE** /v1/voices/{voice_id}/samples/{sample_id} | Delete Sample
[**get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get**](SamplesApi.md#get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get) | **GET** /v1/voices/{voice_id}/samples/{sample_id}/audio | Get Audio From Sample

# **delete_sample_v1_voices_voice_id_samples_sample_id_delete**
> object delete_sample_v1_voices_voice_id_samples_sample_id_delete(voice_id, sample_id, xi_api_key=xi_api_key)

Delete Sample

Removes a sample by its ID.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.SamplesApi()
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
sample_id = 'sample_id_example' # str | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Delete Sample
    api_response = api_instance.delete_sample_v1_voices_voice_id_samples_sample_id_delete(voice_id, sample_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->delete_sample_v1_voices_voice_id_samples_sample_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **sample_id** | **str**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get**
> get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get(voice_id, sample_id, xi_api_key=xi_api_key)

Get Audio From Sample

Returns the audio corresponding to a sample attached to a voice.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.SamplesApi()
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
sample_id = 'sample_id_example' # str | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Audio From Sample
    api_instance.get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get(voice_id, sample_id, xi_api_key=xi_api_key)
except ApiException as e:
    print("Exception when calling SamplesApi->get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **sample_id** | **str**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

