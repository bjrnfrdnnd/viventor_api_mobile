# swagger_client.DocumentsControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_settings_document_using_get**](DocumentsControllerApi.md#download_settings_document_using_get) | **GET** /api/app/v1/user/settings/document/{id}.pdf | downloadSettingsDocument
[**upload_document_using_post**](DocumentsControllerApi.md#upload_document_using_post) | **POST** /api/app/v1/user/settings/uploaddocument.json | uploadDocument


# **download_settings_document_using_get**
> download_settings_document_using_get(id)

downloadSettingsDocument

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
api_instance = api_mobile.DocumentsControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # downloadSettingsDocument
    api_instance.download_settings_document_using_get(id)
except ApiException as e:
    print("Exception when calling DocumentsControllerApi->download_settings_document_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_using_post**
> CommonOperationResponse upload_document_using_post(document_file)

uploadDocument

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
api_instance = api_mobile.DocumentsControllerApi(api_mobile.ApiClient(configuration))
document_file = '/path/to/file.txt' # file | document[file]

try:
    # uploadDocument
    api_response = api_instance.upload_document_using_post(document_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsControllerApi->upload_document_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_file** | **file**| document[file] | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

