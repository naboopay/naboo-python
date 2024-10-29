# CashOutWaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**amount** | **int** |  | 
**phone_number** | **str** |  | 

## Example

```python
from naboo.models.cash_out_wave_request import CashOutWaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashOutWaveRequest from a JSON string
cash_out_wave_request_instance = CashOutWaveRequest.from_json(json)
# print the JSON string representation of the object
print(CashOutWaveRequest.to_json())

# convert the object into a dict
cash_out_wave_request_dict = cash_out_wave_request_instance.to_dict()
# create an instance of CashOutWaveRequest from a dict
cash_out_wave_request_from_dict = CashOutWaveRequest.from_dict(cash_out_wave_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


