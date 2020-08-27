# swagger_client.LegacyAuthenticationControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_using_post**](LegacyAuthenticationControllerApi.md#get_token_using_post) | **POST** /api/token | getToken
[**refresh_token_using_get**](LegacyAuthenticationControllerApi.md#refresh_token_using_get) | **GET** /api/refreshtoken | refreshToken


# **get_token_using_post**
> AccessToken get_token_using_post(email, password, web)

getToken

### Example
```python
from __future__ import print_function
import time
import api_mobile
from api_mobile.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = api_mobile.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = api_mobile.LegacyAuthenticationControllerApi(api_mobile.ApiClient(configuration))
email = 'email_example' # str | email
password = 'password_example' # str | password
web = true # bool | web

try:
    # getToken
    api_response = api_instance.get_token_using_post(email, password, web)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAuthenticationControllerApi->get_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
 **password** | **str**| password | 
 **web** | **bool**| web | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token_using_get**
> AccessToken refresh_token_using_get()

refreshToken

### Example
```python
from __future__ import print_function
import time
import api_mobile
from api_mobile.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = api_mobile.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = api_mobile.LegacyAuthenticationControllerApi(api_mobile.ApiClient(configuration))

try:
    # refreshToken
    api_response = api_instance.refresh_token_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAuthenticationControllerApi->refresh_token_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

