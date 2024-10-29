# GetAllTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[GetOneTransaction]**](GetOneTransaction.md) |  | 

## Example

```python
from naboo.models.get_all_transaction import GetAllTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTransaction from a JSON string
get_all_transaction_instance = GetAllTransaction.from_json(json)
# print the JSON string representation of the object
print(GetAllTransaction.to_json())

# convert the object into a dict
get_all_transaction_dict = get_all_transaction_instance.to_dict()
# create an instance of GetAllTransaction from a dict
get_all_transaction_from_dict = GetAllTransaction.from_dict(get_all_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


