# OnchainCategoriesListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OnchainCategoriesListDataInnerAttributes**](OnchainCategoriesListDataInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.onchain_categories_list_data_inner import OnchainCategoriesListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainCategoriesListDataInner from a JSON string
onchain_categories_list_data_inner_instance = OnchainCategoriesListDataInner.from_json(json)
# print the JSON string representation of the object
print(OnchainCategoriesListDataInner.to_json())

# convert the object into a dict
onchain_categories_list_data_inner_dict = onchain_categories_list_data_inner_instance.to_dict()
# create an instance of OnchainCategoriesListDataInner from a dict
onchain_categories_list_data_inner_from_dict = OnchainCategoriesListDataInner.from_dict(onchain_categories_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


