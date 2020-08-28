# swagger_client.AccountControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_and_download_statement_as_json_using_post**](AccountControllerApi.md#export_and_download_statement_as_json_using_post) | **POST** /api/app/v1/myaccounts/statement/export.json | exportAndDownloadStatementAsJson
[**export_and_download_statement_ios_using_post**](AccountControllerApi.md#export_and_download_statement_ios_using_post) | **POST** /api/app/v1/myaccounts/export.json | exportAndDownloadStatementIOS
[**export_and_download_statement_using_post**](AccountControllerApi.md#export_and_download_statement_using_post) | **POST** /api/app/v1/myaccounts/export.xlsx | exportAndDownloadStatement
[**generate_tax_report_in_html_using_post**](AccountControllerApi.md#generate_tax_report_in_html_using_post) | **POST** /api/app/v1/myaccounts/tax-report.html | generateTaxReportInHtml
[**generate_tax_report_in_pdf_using_post**](AccountControllerApi.md#generate_tax_report_in_pdf_using_post) | **POST** /api/app/v1/myaccounts/tax-report.pdf | generateTaxReportInPdf
[**get_account_balance_using_get**](AccountControllerApi.md#get_account_balance_using_get) | **GET** /api/app/v1/mybalance.json | getAccountBalance
[**get_account_statement_using_get**](AccountControllerApi.md#get_account_statement_using_get) | **GET** /api/app/v1/myaccount.json | getAccountStatement
[**get_account_statement_using_post**](AccountControllerApi.md#get_account_statement_using_post) | **POST** /api/app/v1/myaccounts.json | getAccountStatement


# **export_and_download_statement_as_json_using_post**
> export_and_download_statement_as_json_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)

exportAndDownloadStatementAsJson

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
payment_type = 56 # int |  (optional)

try:
    # exportAndDownloadStatementAsJson
    api_instance.export_and_download_statement_as_json_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)
except ApiException as e:
    print("Exception when calling AccountControllerApi->export_and_download_statement_as_json_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **payment_type** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_and_download_statement_ios_using_post**
> export_and_download_statement_ios_using_post(query)

exportAndDownloadStatementIOS

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
query = viventor_api_mobile.StatementQuery() # StatementQuery | query

try:
    # exportAndDownloadStatementIOS
    api_instance.export_and_download_statement_ios_using_post(query)
except ApiException as e:
    print("Exception when calling AccountControllerApi->export_and_download_statement_ios_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**StatementQuery**](StatementQuery.md)| query | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_and_download_statement_using_post**
> export_and_download_statement_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)

exportAndDownloadStatement

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
payment_type = 56 # int |  (optional)

try:
    # exportAndDownloadStatement
    api_instance.export_and_download_statement_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)
except ApiException as e:
    print("Exception when calling AccountControllerApi->export_and_download_statement_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **payment_type** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_tax_report_in_html_using_post**
> str generate_tax_report_in_html_using_post(start_date=start_date, end_date=end_date)

generateTaxReportInHtml

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)

try:
    # generateTaxReportInHtml
    api_response = api_instance.generate_tax_report_in_html_using_post(start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->generate_tax_report_in_html_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_tax_report_in_pdf_using_post**
> generate_tax_report_in_pdf_using_post(start_date=start_date, end_date=end_date)

generateTaxReportInPdf

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)

try:
    # generateTaxReportInPdf
    api_instance.generate_tax_report_in_pdf_using_post(start_date=start_date, end_date=end_date)
except ApiException as e:
    print("Exception when calling AccountControllerApi->generate_tax_report_in_pdf_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balance_using_get**
> AccountBalance get_account_balance_using_get()

getAccountBalance

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))

try:
    # getAccountBalance
    api_response = api_instance.get_account_balance_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->get_account_balance_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statement_using_get**
> AccountStatement get_account_statement_using_get()

getAccountStatement

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))

try:
    # getAccountStatement
    api_response = api_instance.get_account_statement_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->get_account_statement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statement_using_post**
> AccountStatement get_account_statement_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)

getAccountStatement

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
api_instance = viventor_api_mobile.AccountControllerApi(api_mobile.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
payment_type = 56 # int |  (optional)

try:
    # getAccountStatement
    api_response = api_instance.get_account_statement_using_post(start_date=start_date, end_date=end_date, payment_type=payment_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->get_account_statement_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **payment_type** | **int**|  | [optional] 

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

