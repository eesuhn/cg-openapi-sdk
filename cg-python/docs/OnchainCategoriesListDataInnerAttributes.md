# OnchainCategoriesListDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**volume_change_percentage** | [**OnchainCategoriesListDataInnerAttributesVolumeChangePercentage**](OnchainCategoriesListDataInnerAttributesVolumeChangePercentage.md) |  | [optional] 
**reserve_in_usd** | **str** |  | [optional] 
**fdv_usd** | **str** |  | [optional] 
**h24_volume_usd** | **str** |  | [optional] 
**h24_tx_count** | **int** |  | [optional] 

## Example

```python
from coingecko_sdk.models.onchain_categories_list_data_inner_attributes import OnchainCategoriesListDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainCategoriesListDataInnerAttributes from a JSON string
onchain_categories_list_data_inner_attributes_instance = OnchainCategoriesListDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(OnchainCategoriesListDataInnerAttributes.to_json())

# convert the object into a dict
onchain_categories_list_data_inner_attributes_dict = onchain_categories_list_data_inner_attributes_instance.to_dict()
# create an instance of OnchainCategoriesListDataInnerAttributes from a dict
onchain_categories_list_data_inner_attributes_from_dict = OnchainCategoriesListDataInnerAttributes.from_dict(onchain_categories_list_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


