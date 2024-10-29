# TransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**method_of_payment** | **List[str]** |  | 
**amount** | **int** |  | [optional] [default to 0]
**amount_to_pay** | **int** |  | [optional] [default to 0]
**currency** | **str** |  | 
**created_at** | **str** |  | 
**transaction_status** | **str** |  | [optional] [default to 'pending']
**is_escrow** | **bool** |  | [optional] [default to False]
**is_merchant** | **bool** |  | [optional] [default to False]
**checkout_url** | **str** |  | 

## Example

```python
from naboo.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionResponse.to_json())

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_from_dict = TransactionResponse.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


