# NetworksListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**NetworksListDataInnerAttributes**](NetworksListDataInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko_python.models.networks_list_data_inner import NetworksListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksListDataInner from a JSON string
networks_list_data_inner_instance = NetworksListDataInner.from_json(json)
# print the JSON string representation of the object
print(NetworksListDataInner.to_json())

# convert the object into a dict
networks_list_data_inner_dict = networks_list_data_inner_instance.to_dict()
# create an instance of NetworksListDataInner from a dict
networks_list_data_inner_from_dict = NetworksListDataInner.from_dict(networks_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


