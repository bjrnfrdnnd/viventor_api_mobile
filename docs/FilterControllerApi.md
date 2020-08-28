# swagger_client.FilterControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post5**](FilterControllerApi.md#create_using_post5) | **POST** /api/app/v1/filters | create
[**delete_using_post1**](FilterControllerApi.md#delete_using_post1) | **POST** /api/app/v1/filters/{id}/delete | delete
[**read_using_get4**](FilterControllerApi.md#read_using_get4) | **GET** /api/app/v1/filters/{id} | read
[**read_using_get5**](FilterControllerApi.md#read_using_get5) | **GET** /api/app/v1/filters | read
[**update_using_post1**](FilterControllerApi.md#update_using_post1) | **POST** /api/app/v1/filters/{id} | update


# **create_using_post5**
> FilterModel create_using_post5(model)

create

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
api_instance = viventor_api_mobile.FilterControllerApi(api_mobile.ApiClient(configuration))
model = viventor_api_mobile.FilterModel() # FilterModel | model

try:
    # create
    api_response = api_instance.create_using_post5(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterControllerApi->create_using_post5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**FilterModel**](FilterModel.md)| model | 

### Return type

[**FilterModel**](FilterModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_post1**
> delete_using_post1(id)

delete

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
api_instance = viventor_api_mobile.FilterControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # delete
    api_instance.delete_using_post1(id)
except ApiException as e:
    print("Exception when calling FilterControllerApi->delete_using_post1: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_using_get4**
> FilterModel read_using_get4(id)

read

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
api_instance = viventor_api_mobile.FilterControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # read
    api_response = api_instance.read_using_get4(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterControllerApi->read_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**FilterModel**](FilterModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_using_get5**
> list[FilterListModel] read_using_get5()

read

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
api_instance = viventor_api_mobile.FilterControllerApi(api_mobile.ApiClient(configuration))

try:
    # read
    api_response = api_instance.read_using_get5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterControllerApi->read_using_get5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FilterListModel]**](FilterListModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_post1**
> FilterModel update_using_post1(id, model)

update

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
api_instance = viventor_api_mobile.FilterControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id
model = viventor_api_mobile.FilterModel() # FilterModel | model

try:
    # update
    api_response = api_instance.update_using_post1(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterControllerApi->update_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **model** | [**FilterModel**](FilterModel.md)| model | 

### Return type

[**FilterModel**](FilterModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

