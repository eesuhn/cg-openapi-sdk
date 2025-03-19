# OnchainCategoriesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OnchainCategoriesListDataInner]**](OnchainCategoriesListDataInner.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.onchain_categories_list import OnchainCategoriesList

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainCategoriesList from a JSON string
onchain_categories_list_instance = OnchainCategoriesList.from_json(json)
# print the JSON string representation of the object
print(OnchainCategoriesList.to_json())

# convert the object into a dict
onchain_categories_list_dict = onchain_categories_list_instance.to_dict()
# create an instance of OnchainCategoriesList from a dict
onchain_categories_list_from_dict = OnchainCategoriesList.from_dict(onchain_categories_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


