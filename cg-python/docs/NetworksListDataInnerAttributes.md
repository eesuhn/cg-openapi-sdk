# NetworksListDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**coingecko_asset_platform_id** | **str** |  | [optional] 

## Example

```python
from coingecko-sdk.models.networks_list_data_inner_attributes import NetworksListDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksListDataInnerAttributes from a JSON string
networks_list_data_inner_attributes_instance = NetworksListDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(NetworksListDataInnerAttributes.to_json())

# convert the object into a dict
networks_list_data_inner_attributes_dict = networks_list_data_inner_attributes_instance.to_dict()
# create an instance of NetworksListDataInnerAttributes from a dict
networks_list_data_inner_attributes_from_dict = NetworksListDataInnerAttributes.from_dict(networks_list_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


