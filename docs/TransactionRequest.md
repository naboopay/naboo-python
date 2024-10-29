# TransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_of_payment** | [**List[Wallet]**](Wallet.md) |  | 
**products** | [**List[ProductModel]**](ProductModel.md) |  | 
**success_url** | **str** |  | [optional] 
**error_url** | **str** |  | [optional] 
**is_escrow** | **bool** |  | [optional] [default to False]
**is_merchant** | **bool** |  | [optional] [default to False]

## Example

```python
from naboo.models.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionRequest.to_json())

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_from_dict = TransactionRequest.from_dict(transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


