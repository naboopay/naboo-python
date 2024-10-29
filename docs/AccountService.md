# naboo.AccountService

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_information_account_get**](AccountService.md#get_account_information_account_get) | **GET** /account/ | Get Account Information


# **get_account_information_account_get**
> GetAccountResponse get_account_information_account_get()

Get Account Information

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.get_account_response import GetAccountResponse
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
    except Exception as e:
        print("Exception when calling AccountService->get_account_information_account_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

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

