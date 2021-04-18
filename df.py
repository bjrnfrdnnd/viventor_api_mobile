from __future__ import print_function

import shutil
import pandas as pd

import viventor_api_mobile
from viventor_api_mobile import LegacyAuthenticationControllerApi, AccessToken, AccountControllerApi, \
    InvestmentControllerApi
from viventor_api_mobile.rest import ApiException

# Configure API key authorization: apiKey
configuration = viventor_api_mobile.Configuration()
configuration.username = 'bjrnfrdnnd@gmail.com'
# the following is a deprecated password
configuration.password = '7TGBUGfRWRX@x4h'
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_client = viventor_api_mobile.ApiClient(configuration=configuration)
laca = LegacyAuthenticationControllerApi(api_client=api_client)
aca = AccountControllerApi(api_client=api_client)
ica = InvestmentControllerApi(api_client=api_client)

a: AccessToken = laca.get_token_using_post(email=configuration.username, password=configuration.password, web=True)
configuration.api_key['Authorization'] = a.token



try:
    # create an instance of the API class
    api_instance = viventor_api_mobile.AccountControllerApi(api_client=api_client)
    a = api_instance.get_account_balance_using_get()
    print(a)
except ApiException as e:
    print("Exception when calling AccountControllerApi->get_account_balance_using_get: %s\n" % e)

try:
    start_date = '2020-08-01'
    api_instance = AccountControllerApi(api_client=api_client)
    a = api_instance.export_and_download_statement_using_post(start_date=start_date)
    print(a)
    df = pd.read_excel(io=a, skiprows=18, engine='xlrd')
    print(df)
except ApiException as e:
    print("Exception when calling AccountControllerApi->export_and_download_statement_using_post: %s\n" % e)

try:
    filter = {
        "pages": 100000,
    }
    api_instance = InvestmentControllerApi(api_client=api_client)
    a = api_instance.export_and_download_loan_book_using_post()
    print(a)
    df = pd.read_excel(io=a, skiprows=0, engine='xlrd')
    print(df)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->export_and_download_loan_book_using_post: %s\n" % e)

try:
    filter = {
        "pages": 100000,
    }
    api_instance = InvestmentControllerApi(api_client=api_client)
    a = api_instance.my_investments_using_post(filter=filter)
    b = a.items_my_investments_filtered
    c = [a.to_dict() for a in b]
    df = pd.DataFrame(c)
except ApiException as e:
    print("Exception when calling InvestmentControllerApi->my_investments_using_post: %s\n" % e)