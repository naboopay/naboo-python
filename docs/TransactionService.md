# naboo.TransactionService

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_transaction_create_transaction_post**](TransactionService.md#create_transaction_transaction_create_transaction_post) | **PUT** /transaction/create-transaction | Create Transaction
[**delete_transaction_transaction_delete_transaction_delete**](TransactionService.md#delete_transaction_transaction_delete_transaction_delete) | **DELETE** /transaction/delete-transaction | Delete Transaction
[**get_one_transaction_transaction_get_one_transaction_get**](TransactionService.md#get_one_transaction_transaction_get_one_transaction_get) | **GET** /transaction/get-one-transaction | Get One Transaction
[**get_transactions_transaction_get_transactions_get**](TransactionService.md#get_transactions_transaction_get_transactions_get) | **GET** /transaction/get-transactions | Get Transactions


# **create_transaction_transaction_create_transaction_post**
> TransactionResponse create_transaction_transaction_create_transaction_post(transaction_request)

Create Transaction

This endpoint allows authenticated users to create a transaction by submitting a request with the necessary details. The endpoint ensures that the user's access level permits transaction creation and enforces a rate limit of 30 requests. It checks that the number of products is within the allowed range (1-20) and calculates the total transaction amount, applying a 20% charge for escrow transactions. It also verifies that the total amount does not exceed a specific threshold (2,000,000). The user's IP address and browser information are logged, and the transaction details are saved with relevant metadata, including a unique order ID and the associated account state. If any conditions are not met, appropriate error messages are returned.

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.transaction_request import TransactionRequest
from naboo.models.transaction_response import TransactionResponse
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
    api_instance = naboo.TransactionService(api_client)
    transaction_request = naboo.TransactionRequest() # TransactionRequest | 

    try:
        # Create Transaction
        api_response = api_instance.create_transaction_transaction_create_transaction_post(transaction_request)
        print("The response of TransactionService->create_transaction_transaction_create_transaction_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionService->create_transaction_transaction_create_transaction_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | The request was invalid or malformed. |  -  |
**401** | The user is not authorized to make this request. |  -  |
**403** | The user does not have permission to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_transaction_delete_transaction_delete**
> DeleteTransactionResponse delete_transaction_transaction_delete_transaction_delete(delete_transaction_request)

Delete Transaction

This endpoint allows authenticated users to delete a transaction by submitting a request with the necessary details. The endpoint checks the user's access level to ensure they have permission to delete transactions and enforces a rate limit of 30 requests. It verifies that the transaction belongs to the user and has not already been deleted or withdrawn. If the transaction is paid and has a payment reference, it processes refunds and updates the user's account balance accordingly.

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.delete_transaction_request import DeleteTransactionRequest
from naboo.models.delete_transaction_response import DeleteTransactionResponse
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
    api_instance = naboo.TransactionService(api_client)
    delete_transaction_request = naboo.DeleteTransactionRequest() # DeleteTransactionRequest | 

    try:
        # Delete Transaction
        api_response = api_instance.delete_transaction_transaction_delete_transaction_delete(delete_transaction_request)
        print("The response of TransactionService->delete_transaction_transaction_delete_transaction_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionService->delete_transaction_transaction_delete_transaction_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_transaction_request** | [**DeleteTransactionRequest**](DeleteTransactionRequest.md)|  | 

### Return type

[**DeleteTransactionResponse**](DeleteTransactionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | The request was invalid or malformed. |  -  |
**401** | The user is not authorized to make this request. |  -  |
**403** | The user does not have permission to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_transaction_transaction_get_one_transaction_get**
> GetOneTransaction get_one_transaction_transaction_get_one_transaction_get(order_id)

Get One Transaction

This endpoint allows authenticated users to retrieve the details of a specific transaction using the order ID. The endpoint ensures the user has read access and enforces a rate limit of 30 requests. It checks if the transaction exists in the database and if the user has the appropriate access rights,then provides a checkout URL for the transaction and others informations

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.get_one_transaction import GetOneTransaction
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
    api_instance = naboo.TransactionService(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # Get One Transaction
        api_response = api_instance.get_one_transaction_transaction_get_one_transaction_get(order_id)
        print("The response of TransactionService->get_one_transaction_transaction_get_one_transaction_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionService->get_one_transaction_transaction_get_one_transaction_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**GetOneTransaction**](GetOneTransaction.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | The request was invalid or malformed. |  -  |
**401** | The user is not authorized to make this request. |  -  |
**403** | The user does not have permission to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | An unexpected internal server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_transaction_get_transactions_get**
> GetAllTransaction get_transactions_transaction_get_transactions_get()

Get Transactions

This endpoint allows authenticated users to retrieve a list of their visible transactions, up to a maximum of 50. The endpoint enforces a rate limit of 30 requests and ensures the user has read access.

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.get_all_transaction import GetAllTransaction
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
    api_instance = naboo.TransactionService(api_client)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions_transaction_get_transactions_get()
        print("The response of TransactionService->get_transactions_transaction_get_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionService->get_transactions_transaction_get_transactions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllTransaction**](GetAllTransaction.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | The request was invalid or malformed. |  -  |
**401** | The user is not authorized to make this request. |  -  |
**403** | The user does not have permission to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | An unexpected internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

