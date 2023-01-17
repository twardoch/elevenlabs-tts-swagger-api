# eleven_tts.TextToSpeechApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_to_speech_v1_text_to_speech_voice_id_post**](TextToSpeechApi.md#text_to_speech_v1_text_to_speech_voice_id_post) | **POST** /v1/text-to-speech/{voice_id} | Text To Speech
[**text_to_speech_v1_text_to_speech_voice_id_stream_post**](TextToSpeechApi.md#text_to_speech_v1_text_to_speech_voice_id_stream_post) | **POST** /v1/text-to-speech/{voice_id}/stream | Text To Speech

# **text_to_speech_v1_text_to_speech_voice_id_post**
> text_to_speech_v1_text_to_speech_voice_id_post(body, voice_id, xi_api_key=xi_api_key)

Text To Speech

Converts text into speech using a voice of your choice and returns audio.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.TextToSpeechApi()
body = eleven_tts.BodyTextToSpeechV1TextToSpeechVoiceIdPost() # BodyTextToSpeechV1TextToSpeechVoiceIdPost | 
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Text To Speech
    api_instance.text_to_speech_v1_text_to_speech_voice_id_post(body, voice_id, xi_api_key=xi_api_key)
except ApiException as e:
    print("Exception when calling TextToSpeechApi->text_to_speech_v1_text_to_speech_voice_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyTextToSpeechV1TextToSpeechVoiceIdPost**](BodyTextToSpeechV1TextToSpeechVoiceIdPost.md)|  | 
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: audio/mpeg, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_to_speech_v1_text_to_speech_voice_id_stream_post**
> text_to_speech_v1_text_to_speech_voice_id_stream_post(body, voice_id, xi_api_key=xi_api_key)

Text To Speech

Converts text into speech using a voice of your choice and returns audio as an audio stream.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.TextToSpeechApi()
body = eleven_tts.BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost() # BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost | 
voice_id = 'voice_id_example' # str | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Text To Speech
    api_instance.text_to_speech_v1_text_to_speech_voice_id_stream_post(body, voice_id, xi_api_key=xi_api_key)
except ApiException as e:
    print("Exception when calling TextToSpeechApi->text_to_speech_v1_text_to_speech_voice_id_stream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost**](BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost.md)|  | 
 **voice_id** | **str**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

