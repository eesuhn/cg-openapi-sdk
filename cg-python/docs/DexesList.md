# DexesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DexesListDataInner]**](DexesListDataInner.md) |  | [optional] 

## Example

```python
from coingecko_python.models.dexes_list import DexesList

# TODO update the JSON string below
json = "{}"
# create an instance of DexesList from a JSON string
dexes_list_instance = DexesList.from_json(json)
# print the JSON string representation of the object
print(DexesList.to_json())

# convert the object into a dict
dexes_list_dict = dexes_list_instance.to_dict()
# create an instance of DexesList from a dict
dexes_list_from_dict = DexesList.from_dict(dexes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


