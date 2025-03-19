# NetworksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworksListDataInner]**](NetworksListDataInner.md) |  | [optional] 

## Example

```python
from coingecko_python.models.networks_list import NetworksList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksList from a JSON string
networks_list_instance = NetworksList.from_json(json)
# print the JSON string representation of the object
print(NetworksList.to_json())

# convert the object into a dict
networks_list_dict = networks_list_instance.to_dict()
# create an instance of NetworksList from a dict
networks_list_from_dict = NetworksList.from_dict(networks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


