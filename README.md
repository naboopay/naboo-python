# naboo
Here you have the first version of the naboo api to create checkout automatically

- API version: 0.1.0

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import naboo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import naboo
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import naboo
from naboo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = naboo.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = naboo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with naboo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = naboo.AccountService(api_client)

    try:
        # Get Account Information
        api_response = api_instance.get_account_information_account_get()
        print("The response of AccountService->get_account_information_account_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountService->get_account_information_account_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountService* | [**get_account_information_account_get**](docs/AccountService.md#get_account_information_account_get) | **GET** /account/ | Get Account Information
*CashoutService* | [**cash_out_orange_money_cashout_orange_money_post**](docs/CashoutService.md#cash_out_orange_money_cashout_orange_money_post) | **POST** /cashout/orange-money | Cash Out Orange Money
*CashoutService* | [**cash_out_wave_cashout_wave_post**](docs/CashoutService.md#cash_out_wave_cashout_wave_post) | **POST** /cashout/wave | Cash Out Wave
*TransactionService* | [**create_transaction_transaction_create_transaction_post**](docs/TransactionService.md#create_transaction_transaction_create_transaction_post) | **PUT** /transaction/create-transaction | Create Transaction
*TransactionService* | [**delete_transaction_transaction_delete_transaction_delete**](docs/TransactionService.md#delete_transaction_transaction_delete_transaction_delete) | **DELETE** /transaction/delete-transaction | Delete Transaction
*TransactionService* | [**get_one_transaction_transaction_get_one_transaction_get**](docs/TransactionService.md#get_one_transaction_transaction_get_one_transaction_get) | **GET** /transaction/get-one-transaction | Get One Transaction
*TransactionService* | [**get_transactions_transaction_get_transactions_get**](docs/TransactionService.md#get_transactions_transaction_get_transactions_get) | **GET** /transaction/get-transactions | Get Transactions


## Documentation For Models

 - [CashOutOrangeRequest](docs/CashOutOrangeRequest.md)
 - [CashOutResponse](docs/CashOutResponse.md)
 - [CashOutWaveRequest](docs/CashOutWaveRequest.md)
 - [DeleteTransactionRequest](docs/DeleteTransactionRequest.md)
 - [DeleteTransactionResponse](docs/DeleteTransactionResponse.md)
 - [GetAccountResponse](docs/GetAccountResponse.md)
 - [GetAllTransaction](docs/GetAllTransaction.md)
 - [GetOneTransaction](docs/GetOneTransaction.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ProductModel](docs/ProductModel.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionStatusEnum](docs/TransactionStatusEnum.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Wallet](docs/Wallet.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication


## Author




