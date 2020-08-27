# swagger_client.InvestmentControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_investment_using_post**](InvestmentControllerApi.md#cancel_investment_using_post) | **POST** /api/app/v1/loan-investor/myInvestments/cancel/{noteId}.json | cancelInvestment
[**download_assignment_agreement_using_get**](InvestmentControllerApi.md#download_assignment_agreement_using_get) | **GET** /api/app/v1/assignment-agreements.pdf | downloadAssignmentAgreement
[**download_contract_file_using_get**](InvestmentControllerApi.md#download_contract_file_using_get) | **GET** /api/app/v1/loan-investor/myInvestments/contract/{noteId}.pdf | downloadContractFile
[**download_data_processing_agreement_using_get**](InvestmentControllerApi.md#download_data_processing_agreement_using_get) | **GET** /api/app/v1/data-processing.pdf | downloadDataProcessingAgreement
[**download_loan_attachment_using_get2**](InvestmentControllerApi.md#download_loan_attachment_using_get2) | **GET** /api/app/v1/loan-investor/attachment/{id} | downloadLoanAttachment
[**download_primary_market_contract_preview_file_using_get**](InvestmentControllerApi.md#download_primary_market_contract_preview_file_using_get) | **GET** /api/app/v1/loan-investor/primary/contract/{loanId}.pdf | downloadPrimaryMarketContractPreviewFile
[**download_privacy_policy_agreement_using_get**](InvestmentControllerApi.md#download_privacy_policy_agreement_using_get) | **GET** /api/app/v1/privacy-policy.pdf | downloadPrivacyPolicyAgreement
[**download_secondary_market_contract_preview_file_using_get**](InvestmentControllerApi.md#download_secondary_market_contract_preview_file_using_get) | **GET** /api/app/v1/loan-investor/secondary/contract/{noteId}.pdf | downloadSecondaryMarketContractPreviewFile
[**download_user_agreement_using_get**](InvestmentControllerApi.md#download_user_agreement_using_get) | **GET** /api/app/v1/user-agreements.pdf | downloadUserAgreement
[**export_and_download_loan_book_using_post**](InvestmentControllerApi.md#export_and_download_loan_book_using_post) | **POST** /api/app/v1/loan-investor/loan-book.xlsx | exportAndDownloadLoanBook
[**export_and_download_report_using_post**](InvestmentControllerApi.md#export_and_download_report_using_post) | **POST** /api/app/v1/loan-investor/myInvestment/export.xlsx | exportAndDownloadReport
[**get_add_funds_credentials_using_get**](InvestmentControllerApi.md#get_add_funds_credentials_using_get) | **GET** /api/app/v1/invest-fund/add.json | getAddFundsCredentials
[**get_view_loan_primary_market_using_get**](InvestmentControllerApi.md#get_view_loan_primary_market_using_get) | **GET** /api/app/v1/loan-investor/primary/{loanId}.json | getViewLoanPrimaryMarket
[**get_view_loan_secondary_market_using_get**](InvestmentControllerApi.md#get_view_loan_secondary_market_using_get) | **GET** /api/app/v1/loan-investor/secondary/{noteId}.json | getViewLoanSecondaryMarket
[**get_view_my_investment_using_get**](InvestmentControllerApi.md#get_view_my_investment_using_get) | **GET** /api/app/v1/loan-investor/myInvestment/{noteId}.json | getViewMyInvestment
[**invest_primary_market_with_request_body_using_post**](InvestmentControllerApi.md#invest_primary_market_with_request_body_using_post) | **POST** /api/app/v1/loan-investor/primary/invest/{loanId}.json | investPrimaryMarketWithRequestBody
[**invest_secondary_market_using_get**](InvestmentControllerApi.md#invest_secondary_market_using_get) | **GET** /api/app/v1/loan-investor/secondary/invest/{noteId}.json | investSecondaryMarket
[**list_loan_attachments_using_get1**](InvestmentControllerApi.md#list_loan_attachments_using_get1) | **GET** /api/app/v1/loan-investor/attachments/{loanId} | listLoanAttachments
[**my_investments_using_get**](InvestmentControllerApi.md#my_investments_using_get) | **GET** /api/app/v1/loan-investor/myInvestments.json | myInvestments
[**my_investments_using_post**](InvestmentControllerApi.md#my_investments_using_post) | **POST** /api/app/v1/loan-investor/myInvestments.json | myInvestments
[**primary_public_info_using_get**](InvestmentControllerApi.md#primary_public_info_using_get) | **GET** /api/app/v1/loan-investor/primary-public.json | primaryPublicInfo
[**primary_public_info_using_post**](InvestmentControllerApi.md#primary_public_info_using_post) | **POST** /api/app/v1/loan-investor/primary-public.json | primaryPublicInfo
[**primary_using_get**](InvestmentControllerApi.md#primary_using_get) | **GET** /api/app/v1/loan-investor/primary.json | primary
[**primary_using_post**](InvestmentControllerApi.md#primary_using_post) | **POST** /api/app/v1/loan-investor/primary.json | primary
[**render_assignment_agreement_using_get**](InvestmentControllerApi.md#render_assignment_agreement_using_get) | **GET** /api/app/v1/assignment-agreements.html | renderAssignmentAgreement
[**render_contract_html_using_get**](InvestmentControllerApi.md#render_contract_html_using_get) | **GET** /api/app/v1/loan-investor/myInvestments/contract/{noteId}.html | renderContractHtml
[**render_primary_market_contract_preview_html_using_get**](InvestmentControllerApi.md#render_primary_market_contract_preview_html_using_get) | **GET** /api/app/v1/loan-investor/primary/contract/{loanId}.html | renderPrimaryMarketContractPreviewHtml
[**render_secondary_market_contract_preview_html_using_get**](InvestmentControllerApi.md#render_secondary_market_contract_preview_html_using_get) | **GET** /api/app/v1/loan-investor/secondary/contract/{noteId}.html | renderSecondaryMarketContractPreviewHtml
[**render_user_agreement_using_get**](InvestmentControllerApi.md#render_user_agreement_using_get) | **GET** /api/app/v1/user-agreements.html | renderUserAgreement
[**secondary_public_info_using_get**](InvestmentControllerApi.md#secondary_public_info_using_get) | **GET** /api/app/v1/loan-investor/secondary-public.json | secondaryPublicInfo
[**secondary_using_get**](InvestmentControllerApi.md#secondary_using_get) | **GET** /api/app/v1/loan-investor/secondary.json | secondary
[**secondary_using_post**](InvestmentControllerApi.md#secondary_using_post) | **POST** /api/app/v1/loan-investor/secondary.json | secondary
[**sell_investment_using_post**](InvestmentControllerApi.md#sell_investment_using_post) | **POST** /api/app/v1/loan-investor/myInvestments/sell/{noteId}.json | sellInvestment
[**withdraw_funds_with_request_body_using_post**](InvestmentControllerApi.md#withdraw_funds_with_request_body_using_post) | **POST** /api/app/v1/invest-fund/withdraw.json | withdrawFundsWithRequestBody
[**withdrawal_using_get**](InvestmentControllerApi.md#withdrawal_using_get) | **GET** /api/app/v1/invest-fund/withdraw.json | withdrawal


# **cancel_investment_using_post**
> SellResponse cancel_investment_using_post(note_id)

cancelInvestment

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # cancelInvestment
    api_response = api_instance.cancel_investment_using_post(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->cancel_investment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

[**SellResponse**](SellResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_assignment_agreement_using_get**
> download_assignment_agreement_using_get()

downloadAssignmentAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # downloadAssignmentAgreement
    api_instance.download_assignment_agreement_using_get()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_assignment_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_contract_file_using_get**
> download_contract_file_using_get(note_id)

downloadContractFile

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # downloadContractFile
    api_instance.download_contract_file_using_get(note_id)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_contract_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_data_processing_agreement_using_get**
> download_data_processing_agreement_using_get()

downloadDataProcessingAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # downloadDataProcessingAgreement
    api_instance.download_data_processing_agreement_using_get()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_data_processing_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_loan_attachment_using_get2**
> download_loan_attachment_using_get2(id)

downloadLoanAttachment

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
id = 789 # int | id

try:
    # downloadLoanAttachment
    api_instance.download_loan_attachment_using_get2(id)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_loan_attachment_using_get2: %s\n" % e)
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

# **download_primary_market_contract_preview_file_using_get**
> download_primary_market_contract_preview_file_using_get(loan_id)

downloadPrimaryMarketContractPreviewFile

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # downloadPrimaryMarketContractPreviewFile
    api_instance.download_primary_market_contract_preview_file_using_get(loan_id)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_primary_market_contract_preview_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_privacy_policy_agreement_using_get**
> download_privacy_policy_agreement_using_get()

downloadPrivacyPolicyAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # downloadPrivacyPolicyAgreement
    api_instance.download_privacy_policy_agreement_using_get()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_privacy_policy_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_secondary_market_contract_preview_file_using_get**
> download_secondary_market_contract_preview_file_using_get(note_id)

downloadSecondaryMarketContractPreviewFile

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # downloadSecondaryMarketContractPreviewFile
    api_instance.download_secondary_market_contract_preview_file_using_get(note_id)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_secondary_market_contract_preview_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_user_agreement_using_get**
> download_user_agreement_using_get()

downloadUserAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # downloadUserAgreement
    api_instance.download_user_agreement_using_get()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->download_user_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_and_download_loan_book_using_post**
> export_and_download_loan_book_using_post()

exportAndDownloadLoanBook

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # exportAndDownloadLoanBook
    api_instance.export_and_download_loan_book_using_post()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->export_and_download_loan_book_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_and_download_report_using_post**
> export_and_download_report_using_post()

exportAndDownloadReport

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # exportAndDownloadReport
    api_instance.export_and_download_report_using_post()
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->export_and_download_report_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_add_funds_credentials_using_get**
> AddFundsCredentials get_add_funds_credentials_using_get()

getAddFundsCredentials

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # getAddFundsCredentials
    api_response = api_instance.get_add_funds_credentials_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->get_add_funds_credentials_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AddFundsCredentials**](AddFundsCredentials.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_loan_primary_market_using_get**
> LoanViewPrimary get_view_loan_primary_market_using_get(loan_id)

getViewLoanPrimaryMarket

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # getViewLoanPrimaryMarket
    api_response = api_instance.get_view_loan_primary_market_using_get(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->get_view_loan_primary_market_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**LoanViewPrimary**](LoanViewPrimary.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_loan_secondary_market_using_get**
> LoanViewSecondary get_view_loan_secondary_market_using_get(note_id)

getViewLoanSecondaryMarket

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # getViewLoanSecondaryMarket
    api_response = api_instance.get_view_loan_secondary_market_using_get(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->get_view_loan_secondary_market_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

[**LoanViewSecondary**](LoanViewSecondary.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_my_investment_using_get**
> MyInvestmentView get_view_my_investment_using_get(note_id)

getViewMyInvestment

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # getViewMyInvestment
    api_response = api_instance.get_view_my_investment_using_get(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->get_view_my_investment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

[**MyInvestmentView**](MyInvestmentView.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invest_primary_market_with_request_body_using_post**
> InvestResponse invest_primary_market_with_request_body_using_post(loan_id, request_body_with_amount)

investPrimaryMarketWithRequestBody

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
loan_id = 789 # int | loanId
request_body_with_amount = api_mobile.RequestBodyWithAmount() # RequestBodyWithAmount | requestBodyWithAmount

try:
    # investPrimaryMarketWithRequestBody
    api_response = api_instance.invest_primary_market_with_request_body_using_post(loan_id, request_body_with_amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->invest_primary_market_with_request_body_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **request_body_with_amount** | [**RequestBodyWithAmount**](RequestBodyWithAmount.md)| requestBodyWithAmount | 

### Return type

[**InvestResponse**](InvestResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invest_secondary_market_using_get**
> InvestResponse invest_secondary_market_using_get(note_id, extension_opt_in=extension_opt_in)

investSecondaryMarket

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId
extension_opt_in = true # bool | extensionOptIn (optional)

try:
    # investSecondaryMarket
    api_response = api_instance.invest_secondary_market_using_get(note_id, extension_opt_in=extension_opt_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->invest_secondary_market_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 
 **extension_opt_in** | **bool**| extensionOptIn | [optional] 

### Return type

[**InvestResponse**](InvestResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_attachments_using_get1**
> list[LoanAttachment] list_loan_attachments_using_get1(loan_id)

listLoanAttachments

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # listLoanAttachments
    api_response = api_instance.list_loan_attachments_using_get1(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->list_loan_attachments_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[LoanAttachment]**](LoanAttachment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_investments_using_get**
> MarketInfo my_investments_using_get()

myInvestments

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # myInvestments
    api_response = api_instance.my_investments_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->my_investments_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_investments_using_post**
> MarketInfo my_investments_using_post(filter)

myInvestments

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
filter = api_mobile.FilterOptions() # FilterOptions | filter

try:
    # myInvestments
    api_response = api_instance.my_investments_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->my_investments_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**FilterOptions**](FilterOptions.md)| filter | 

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_public_info_using_get**
> LoansPrimaryModel primary_public_info_using_get()

primaryPublicInfo

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # primaryPublicInfo
    api_response = api_instance.primary_public_info_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->primary_public_info_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoansPrimaryModel**](LoansPrimaryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_public_info_using_post**
> LoansPrimaryModel primary_public_info_using_post(filter_options)

primaryPublicInfo

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
filter_options = api_mobile.FilterOptions() # FilterOptions | filterOptions

try:
    # primaryPublicInfo
    api_response = api_instance.primary_public_info_using_post(filter_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->primary_public_info_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_options** | [**FilterOptions**](FilterOptions.md)| filterOptions | 

### Return type

[**LoansPrimaryModel**](LoansPrimaryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_using_get**
> MarketInfo primary_using_get()

primary

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # primary
    api_response = api_instance.primary_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->primary_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_using_post**
> MarketInfo primary_using_post(filter)

primary

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
filter = api_mobile.FilterOptions() # FilterOptions | filter

try:
    # primary
    api_response = api_instance.primary_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->primary_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**FilterOptions**](FilterOptions.md)| filter | 

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_assignment_agreement_using_get**
> str render_assignment_agreement_using_get()

renderAssignmentAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # renderAssignmentAgreement
    api_response = api_instance.render_assignment_agreement_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->render_assignment_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_contract_html_using_get**
> str render_contract_html_using_get(note_id)

renderContractHtml

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # renderContractHtml
    api_response = api_instance.render_contract_html_using_get(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->render_contract_html_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_primary_market_contract_preview_html_using_get**
> str render_primary_market_contract_preview_html_using_get(loan_id)

renderPrimaryMarketContractPreviewHtml

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # renderPrimaryMarketContractPreviewHtml
    api_response = api_instance.render_primary_market_contract_preview_html_using_get(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->render_primary_market_contract_preview_html_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_secondary_market_contract_preview_html_using_get**
> str render_secondary_market_contract_preview_html_using_get(note_id)

renderSecondaryMarketContractPreviewHtml

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId

try:
    # renderSecondaryMarketContractPreviewHtml
    api_response = api_instance.render_secondary_market_contract_preview_html_using_get(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->render_secondary_market_contract_preview_html_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_user_agreement_using_get**
> str render_user_agreement_using_get()

renderUserAgreement

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # renderUserAgreement
    api_response = api_instance.render_user_agreement_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->render_user_agreement_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secondary_public_info_using_get**
> LoansSecondaryModel secondary_public_info_using_get()

secondaryPublicInfo

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # secondaryPublicInfo
    api_response = api_instance.secondary_public_info_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->secondary_public_info_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoansSecondaryModel**](LoansSecondaryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secondary_using_get**
> MarketInfo secondary_using_get()

secondary

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # secondary
    api_response = api_instance.secondary_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->secondary_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secondary_using_post**
> MarketInfo secondary_using_post(filter)

secondary

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
filter = api_mobile.FilterOptions() # FilterOptions | filter

try:
    # secondary
    api_response = api_instance.secondary_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->secondary_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**FilterOptions**](FilterOptions.md)| filter | 

### Return type

[**MarketInfo**](MarketInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sell_investment_using_post**
> SellResponse sell_investment_using_post(note_id, sell_interest)

sellInvestment

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
note_id = 789 # int | noteId
sell_interest = 56 # int | sell_interest

try:
    # sellInvestment
    api_response = api_instance.sell_investment_using_post(note_id, sell_interest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->sell_investment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| noteId | 
 **sell_interest** | **int**| sell_interest | 

### Return type

[**SellResponse**](SellResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_funds_with_request_body_using_post**
> CommonOperationResponse withdraw_funds_with_request_body_using_post(withdrawal_model)

withdrawFundsWithRequestBody

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))
withdrawal_model = api_mobile.WithdrawalModel() # WithdrawalModel | withdrawalModel

try:
    # withdrawFundsWithRequestBody
    api_response = api_instance.withdraw_funds_with_request_body_using_post(withdrawal_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->withdraw_funds_with_request_body_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_model** | [**WithdrawalModel**](WithdrawalModel.md)| withdrawalModel | 

### Return type

[**CommonOperationResponse**](CommonOperationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdrawal_using_get**
> WithdrawalThreshold withdrawal_using_get()

withdrawal

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
api_instance = api_mobile.InvestmentControllerApi(api_mobile.ApiClient(configuration))

try:
    # withdrawal
    api_response = api_instance.withdrawal_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->withdrawal_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WithdrawalThreshold**](WithdrawalThreshold.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

