# GetOneTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**method_of_payment** | [**List[Wallet]**](Wallet.md) |  | 
**amount** | **int** |  | 
**amount_to_pay** | **int** |  | 
**currency** | **str** |  | 
**created_at** | **str** |  | 
**transaction_status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | 
**products** | [**List[ProductModel]**](ProductModel.md) |  | 
**is_done** | **bool** |  | 
**is_escrow** | **bool** |  | 
**is_merchant** | **bool** |  | 
**checkout_url** | **str** |  | 

## Example

```python
from naboo.models.get_one_transaction import GetOneTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of GetOneTransaction from a JSON string
get_one_transaction_instance = GetOneTransaction.from_json(json)
# print the JSON string representation of the object
print(GetOneTransaction.to_json())

# convert the object into a dict
get_one_transaction_dict = get_one_transaction_instance.to_dict()
# create an instance of GetOneTransaction from a dict
get_one_transaction_from_dict = GetOneTransaction.from_dict(get_one_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


