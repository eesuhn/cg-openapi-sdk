# DexesListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**DexesListDataInnerAttributes**](DexesListDataInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko_python.models.dexes_list_data_inner import DexesListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DexesListDataInner from a JSON string
dexes_list_data_inner_instance = DexesListDataInner.from_json(json)
# print the JSON string representation of the object
print(DexesListDataInner.to_json())

# convert the object into a dict
dexes_list_data_inner_dict = dexes_list_data_inner_instance.to_dict()
# create an instance of DexesListDataInner from a dict
dexes_list_data_inner_from_dict = DexesListDataInner.from_dict(dexes_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


