# ExchangesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | exchange ID | [optional] 
**name** | **str** | exchange name | [optional] 

## Example

```python
from coingecko_python.models.exchanges_list import ExchangesList

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangesList from a JSON string
exchanges_list_instance = ExchangesList.from_json(json)
# print the JSON string representation of the object
print(ExchangesList.to_json())

# convert the object into a dict
exchanges_list_dict = exchanges_list_instance.to_dict()
# create an instance of ExchangesList from a dict
exchanges_list_from_dict = ExchangesList.from_dict(exchanges_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


