# naboo.CashoutService

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cash_out_orange_money_cashout_orange_money_post**](CashoutService.md#cash_out_orange_money_cashout_orange_money_post) | **POST** /cashout/orange-money | Cash Out Orange Money
[**cash_out_wave_cashout_wave_post**](CashoutService.md#cash_out_wave_cashout_wave_post) | **POST** /cashout/wave | Cash Out Wave


# **cash_out_orange_money_cashout_orange_money_post**
> CashOutResponse cash_out_orange_money_cashout_orange_money_post(cash_out_orange_request)

Cash Out Orange Money

This endpoint enables a user to withdraw funds from their NabooPay account to their Orange Money account. Authentication is required, and users with the 'dev' role are not permitted to perform this operation. The amount to be withdrawn must be positive and within the user's available balance. The user's account must be active and registered in the system. After validation, the user's account balance is adjusted accordingly, and the transaction is logged for record-keeping.

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.cash_out_orange_request import CashOutOrangeRequest
from naboo.models.cash_out_response import CashOutResponse
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
    api_instance = naboo.CashoutService(api_client)
    cash_out_orange_request = naboo.CashOutOrangeRequest() # CashOutOrangeRequest | 

    try:
        # Cash Out Orange Money
        api_response = api_instance.cash_out_orange_money_cashout_orange_money_post(cash_out_orange_request)
        print("The response of CashoutService->cash_out_orange_money_cashout_orange_money_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashoutService->cash_out_orange_money_cashout_orange_money_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_out_orange_request** | [**CashOutOrangeRequest**](CashOutOrangeRequest.md)|  | 

### Return type

[**CashOutResponse**](CashOutResponse.md)

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

# **cash_out_wave_cashout_wave_post**
> CashOutResponse cash_out_wave_cashout_wave_post(cash_out_wave_request)

Cash Out Wave

This endpoint allows a user to withdraw funds from their NabooPay account to their Wave account. The user must be authenticated and not possess the 'dev' role. The withdrawal amount must be greater than 10 and not exceed the user's account balance. The user's account must exist and be active. Upon successful validation, the system updates the user's account balance and records the transaction for tracking purposes.

### Example

* Bearer Authentication (HTTPBearer):

```python
import naboo
from naboo.models.cash_out_response import CashOutResponse
from naboo.models.cash_out_wave_request import CashOutWaveRequest
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
    api_instance = naboo.CashoutService(api_client)
    cash_out_wave_request = naboo.CashOutWaveRequest() # CashOutWaveRequest | 

    try:
        # Cash Out Wave
        api_response = api_instance.cash_out_wave_cashout_wave_post(cash_out_wave_request)
        print("The response of CashoutService->cash_out_wave_cashout_wave_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashoutService->cash_out_wave_cashout_wave_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_out_wave_request** | [**CashOutWaveRequest**](CashOutWaveRequest.md)|  | 

### Return type

[**CashOutResponse**](CashOutResponse.md)

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

