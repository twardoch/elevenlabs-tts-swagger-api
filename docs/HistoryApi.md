# eleven_tts.HistoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_history_item_v1_history_history_item_id_delete**](HistoryApi.md#delete_history_item_v1_history_history_item_id_delete) | **DELETE** /v1/history/{history_item_id} | Delete History Item
[**delete_history_items_v1_history_delete_post**](HistoryApi.md#delete_history_items_v1_history_delete_post) | **POST** /v1/history/delete | Delete History Items
[**download_history_items_v1_history_download_post**](HistoryApi.md#download_history_items_v1_history_download_post) | **POST** /v1/history/download | Download History Items
[**get_audio_from_history_item_v1_history_history_item_id_audio_get**](HistoryApi.md#get_audio_from_history_item_v1_history_history_item_id_audio_get) | **GET** /v1/history/{history_item_id}/audio | Get Audio From History Item
[**get_generated_items_v1_history_get**](HistoryApi.md#get_generated_items_v1_history_get) | **GET** /v1/history | Get Generated Items

# **delete_history_item_v1_history_history_item_id_delete**
> object delete_history_item_v1_history_history_item_id_delete(history_item_id, xi_api_key=xi_api_key)

Delete History Item

Delete a history item by its ID

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.HistoryApi()
history_item_id = 'history_item_id_example' # str | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Delete History Item
    api_response = api_instance.delete_history_item_v1_history_history_item_id_delete(history_item_id, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->delete_history_item_v1_history_history_item_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_item_id** | **str**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_history_items_v1_history_delete_post**
> object delete_history_items_v1_history_delete_post(body, xi_api_key=xi_api_key)

Delete History Items

Delete a number of history items by their IDs.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.HistoryApi()
body = eleven_tts.ElevenBodyDeleteHistoryItemsV1HistoryDeletePost() # ElevenBodyDeleteHistoryItemsV1HistoryDeletePost | 
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Delete History Items
    api_response = api_instance.delete_history_items_v1_history_delete_post(body, xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->delete_history_items_v1_history_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElevenBodyDeleteHistoryItemsV1HistoryDeletePost**](ElevenBodyDeleteHistoryItemsV1HistoryDeletePost.md)|  | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_history_items_v1_history_download_post**
> download_history_items_v1_history_download_post(body, xi_api_key=xi_api_key)

Download History Items

Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.HistoryApi()
body = eleven_tts.ElevenBodyDownloadHistoryItemsV1HistoryDownloadPost() # ElevenBodyDownloadHistoryItemsV1HistoryDownloadPost | 
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Download History Items
    api_instance.download_history_items_v1_history_download_post(body, xi_api_key=xi_api_key)
except ApiException as e:
    print("Exception when calling HistoryApi->download_history_items_v1_history_download_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElevenBodyDownloadHistoryItemsV1HistoryDownloadPost**](ElevenBodyDownloadHistoryItemsV1HistoryDownloadPost.md)|  | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_from_history_item_v1_history_history_item_id_audio_get**
> get_audio_from_history_item_v1_history_history_item_id_audio_get(history_item_id, xi_api_key=xi_api_key)

Get Audio From History Item

Returns the audio of an history item.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.HistoryApi()
history_item_id = 'history_item_id_example' # str | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Audio From History Item
    api_instance.get_audio_from_history_item_v1_history_history_item_id_audio_get(history_item_id, xi_api_key=xi_api_key)
except ApiException as e:
    print("Exception when calling HistoryApi->get_audio_from_history_item_v1_history_history_item_id_audio_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_item_id** | **str**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | 
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/mpeg, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generated_items_v1_history_get**
> ElevenGetHistoryResponseModel get_generated_items_v1_history_get(xi_api_key=xi_api_key)

Get Generated Items

Returns metadata about all your generated audio.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.HistoryApi()
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get Generated Items
    api_response = api_instance.get_generated_items_v1_history_get(xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->get_generated_items_v1_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenGetHistoryResponseModel**](ElevenGetHistoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

