# swagger_client.UserControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_user_settings_using_get**](UserControllerApi.md#get_account_user_settings_using_get) | **GET** /api/app/v1/user/settings.json | getAccountUserSettings
[**get_bank_accounts_using_get**](UserControllerApi.md#get_bank_accounts_using_get) | **GET** /api/app/v1/user/bank-accounts.json | getBankAccounts
[**save_account_user_settings_using_post**](UserControllerApi.md#save_account_user_settings_using_post) | **POST** /api/app/v1/user/settings.json | saveAccountUserSettings


# **get_account_user_settings_using_get**
> UserSettings get_account_user_settings_using_get()

getAccountUserSettings

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
api_instance = api_mobile.UserControllerApi(api_mobile.ApiClient(configuration))

try:
    # getAccountUserSettings
    api_response = api_instance.get_account_user_settings_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_account_user_settings_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSettings**](UserSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_accounts_using_get**
> BankAccountsModel get_bank_accounts_using_get()

getBankAccounts

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
api_instance = api_mobile.UserControllerApi(api_mobile.ApiClient(configuration))

try:
    # getBankAccounts
    api_response = api_instance.get_bank_accounts_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_bank_accounts_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BankAccountsModel**](BankAccountsModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_account_user_settings_using_post**
> UserSettings save_account_user_settings_using_post(settings)

saveAccountUserSettings

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
api_instance = api_mobile.UserControllerApi(api_mobile.ApiClient(configuration))
settings = api_mobile.UserSettings() # UserSettings | settings

try:
    # saveAccountUserSettings
    api_response = api_instance.save_account_user_settings_using_post(settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->save_account_user_settings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**UserSettings**](UserSettings.md)| settings | 

### Return type

[**UserSettings**](UserSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

