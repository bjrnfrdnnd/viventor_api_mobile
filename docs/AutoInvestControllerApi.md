# swagger_client.AutoInvestControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_using_get**](AutoInvestControllerApi.md#activate_using_get) | **GET** /api/app/v1/autoinvest/active/{id}.json | activate
[**add_auto_investment_using_post**](AutoInvestControllerApi.md#add_auto_investment_using_post) | **POST** /api/app/v1/autoinvest/add.json | addAutoInvestment
[**delete_using_get**](AutoInvestControllerApi.md#delete_using_get) | **GET** /api/app/v1/autoinvest/delete/{id}.json | delete
[**edit_auto_investment_using_post**](AutoInvestControllerApi.md#edit_auto_investment_using_post) | **POST** /api/app/v1/autoinvest/edit/{id}.json | editAutoInvestment
[**get_auto_investment_list_using_get**](AutoInvestControllerApi.md#get_auto_investment_list_using_get) | **GET** /api/app/v1/autoinvest.json | getAutoInvestmentList
[**get_auto_investment_view_using_get**](AutoInvestControllerApi.md#get_auto_investment_view_using_get) | **GET** /api/app/v1/autoinvest/view/{id}.json | getAutoInvestmentView
[**stop_using_get**](AutoInvestControllerApi.md#stop_using_get) | **GET** /api/app/v1/autoinvest/cancel/{id}.json | stop


# **activate_using_get**
> CommonOperationResponse activate_using_get(id)

activate

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # activate
    api_response = api_instance.activate_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->activate_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_auto_investment_using_post**
> CommonOperationResponse add_auto_investment_using_post(auto_investment_view)

addAutoInvestment

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
auto_investment_view = viventor_api_mobile.AutoInvestmentView() # AutoInvestmentView | autoInvestmentView

try:
    # addAutoInvestment
    api_response = api_instance.add_auto_investment_using_post(auto_investment_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->add_auto_investment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_investment_view** | [**AutoInvestmentView**](AutoInvestmentView.md)| autoInvestmentView | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_get**
> CommonOperationResponse delete_using_get(id)

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # delete
    api_response = api_instance.delete_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->delete_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_auto_investment_using_post**
> CommonOperationResponse edit_auto_investment_using_post(id, auto_investment_view)

editAutoInvestment

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id
auto_investment_view = viventor_api_mobile.AutoInvestmentView() # AutoInvestmentView | autoInvestmentView

try:
    # editAutoInvestment
    api_response = api_instance.edit_auto_investment_using_post(id, auto_investment_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->edit_auto_investment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **auto_investment_view** | [**AutoInvestmentView**](AutoInvestmentView.md)| autoInvestmentView | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_investment_list_using_get**
> list[AutoInvestment] get_auto_investment_list_using_get()

getAutoInvestmentList

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))

try:
    # getAutoInvestmentList
    api_response = api_instance.get_auto_investment_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->get_auto_investment_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AutoInvestment]**](AutoInvestment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_investment_view_using_get**
> AutoInvestmentView get_auto_investment_view_using_get(id)

getAutoInvestmentView

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # getAutoInvestmentView
    api_response = api_instance.get_auto_investment_view_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->get_auto_investment_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**AutoInvestmentView**](AutoInvestmentView.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_using_get**
> CommonOperationResponse stop_using_get(id)

stop

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
api_instance = viventor_api_mobile.AutoInvestControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # stop
    api_response = api_instance.stop_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestControllerApi->stop_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

