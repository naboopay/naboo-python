# GetAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**balance** | **float** |  | 
**account_is_activate** | **bool** |  | 
**method_of_payment** | [**Wallet**](Wallet.md) |  | 
**loyalty_credit** | **int** |  | 

## Example

```python
from naboo.models.get_account_response import GetAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountResponse from a JSON string
get_account_response_instance = GetAccountResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountResponse.to_json())

# convert the object into a dict
get_account_response_dict = get_account_response_instance.to_dict()
# create an instance of GetAccountResponse from a dict
get_account_response_from_dict = GetAccountResponse.from_dict(get_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


