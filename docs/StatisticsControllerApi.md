# swagger_client.StatisticsControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistic_xirr_using_get**](StatisticsControllerApi.md#statistic_xirr_using_get) | **GET** /api/app/v1/statistic-xirr.json | statisticXirr
[**statistics_using_get**](StatisticsControllerApi.md#statistics_using_get) | **GET** /api/app/v1/statistics.json | statistics


# **statistic_xirr_using_get**
> StatisticXirrModel statistic_xirr_using_get()

statisticXirr

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
api_instance = viventor_api_mobile.StatisticsControllerApi(viventor_api_mobile.ApiClient(configuration))

try:
    # statisticXirr
    api_response = api_instance.statistic_xirr_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsControllerApi->statistic_xirr_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticXirrModel**](StatisticXirrModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_using_get**
> StatisticsModel statistics_using_get(_from, to)

statistics

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
api_instance = viventor_api_mobile.StatisticsControllerApi(viventor_api_mobile.ApiClient(configuration))
_from = '_from_example' # str | from
to = 'to_example' # str | to

try:
    # statistics
    api_response = api_instance.statistics_using_get(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsControllerApi->statistics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| from | 
 **to** | **str**| to | 

### Return type

[**StatisticsModel**](StatisticsModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

