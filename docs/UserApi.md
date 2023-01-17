# eleven_tts.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info_v1_user_get**](UserApi.md#get_user_info_v1_user_get) | **GET** /v1/user | Get User Info

# **get_user_info_v1_user_get**
> ElevenUserResponseModel get_user_info_v1_user_get(xi_api_key=xi_api_key)

Get User Info

Gets information about the logged in user.

### Example
```python
from __future__ import print_function
import time
import eleven_tts
from eleven_tts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eleven_tts.UserApi()
xi_api_key = 'xi_api_key_example' # str | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website. (optional)

try:
    # Get User Info
    api_response = api_instance.get_user_info_v1_user_get(xi_api_key=xi_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_info_v1_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xi_api_key** | **str**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#x27;Profile&#x27; tab on the website. | [optional] 

### Return type

[**ElevenUserResponseModel**](ElevenUserResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

