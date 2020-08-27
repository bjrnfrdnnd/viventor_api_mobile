# swagger_client.LegacyPasswordControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_using_post1**](LegacyPasswordControllerApi.md#change_password_using_post1) | **POST** /api/app/v1/user/settings/change-password.json | changePassword
[**confirm_password_reset_using_post**](LegacyPasswordControllerApi.md#confirm_password_reset_using_post) | **POST** /api/app/v1/user/recover/second.json | confirmPasswordReset
[**request_password_reset_using_post**](LegacyPasswordControllerApi.md#request_password_reset_using_post) | **POST** /api/app/v1/user/recover/first.json | requestPasswordReset


# **change_password_using_post1**
> CommonOperationResponse change_password_using_post1(change_password_info)

changePassword

### Example
```python
from __future__ import print_function
import time
import viventor_api_mobile
from viventor_api_mobile.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = viventor_api_mobile.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viventor_api_mobile.LegacyPasswordControllerApi(viventor_api_mobile.ApiClient(configuration))
change_password_info = viventor_api_mobile.ChangePasswordInfo() # ChangePasswordInfo | changePasswordInfo

try:
    # changePassword
    api_response = api_instance.change_password_using_post1(change_password_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyPasswordControllerApi->change_password_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_info** | [**ChangePasswordInfo**](ChangePasswordInfo.md)| changePasswordInfo | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_password_reset_using_post**
> CommonOperationResponse confirm_password_reset_using_post(reset_password_info)

confirmPasswordReset

### Example
```python
from __future__ import print_function
import time
import viventor_api_mobile
from viventor_api_mobile.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = viventor_api_mobile.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viventor_api_mobile.LegacyPasswordControllerApi(viventor_api_mobile.ApiClient(configuration))
reset_password_info = viventor_api_mobile.ResetPasswordInfo() # ResetPasswordInfo | resetPasswordInfo

try:
    # confirmPasswordReset
    api_response = api_instance.confirm_password_reset_using_post(reset_password_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyPasswordControllerApi->confirm_password_reset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_info** | [**ResetPasswordInfo**](ResetPasswordInfo.md)| resetPasswordInfo | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset_using_post**
> CommonOperationResponse request_password_reset_using_post(email)

requestPasswordReset

### Example
```python
from __future__ import print_function
import time
import viventor_api_mobile
from viventor_api_mobile.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = viventor_api_mobile.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viventor_api_mobile.LegacyPasswordControllerApi(viventor_api_mobile.ApiClient(configuration))
email = 'email_example' # str | email

try:
    # requestPasswordReset
    api_response = api_instance.request_password_reset_using_post(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyPasswordControllerApi->request_password_reset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

