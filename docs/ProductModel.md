# ProductModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**category** | **str** |  | 
**amount** | **int** |  | 
**quantity** | **int** |  | 
**description** | **str** |  | 

## Example

```python
from naboo.models.product_model import ProductModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModel from a JSON string
product_model_instance = ProductModel.from_json(json)
# print the JSON string representation of the object
print(ProductModel.to_json())

# convert the object into a dict
product_model_dict = product_model_instance.to_dict()
# create an instance of ProductModel from a dict
product_model_from_dict = ProductModel.from_dict(product_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


