# CashOutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 
**amount** | **int** |  | 
**full_name** | **str** |  | 
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | 

## Example

```python
from naboo.models.cash_out_response import CashOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashOutResponse from a JSON string
cash_out_response_instance = CashOutResponse.from_json(json)
# print the JSON string representation of the object
print(CashOutResponse.to_json())

# convert the object into a dict
cash_out_response_dict = cash_out_response_instance.to_dict()
# create an instance of CashOutResponse from a dict
cash_out_response_from_dict = CashOutResponse.from_dict(cash_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


