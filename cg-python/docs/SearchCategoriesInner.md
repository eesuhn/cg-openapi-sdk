# SearchCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | category ID | [optional] 
**name** | **str** | category name | [optional] 

## Example

```python
from coingecko_python.models.search_categories_inner import SearchCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCategoriesInner from a JSON string
search_categories_inner_instance = SearchCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(SearchCategoriesInner.to_json())

# convert the object into a dict
search_categories_inner_dict = search_categories_inner_instance.to_dict()
# create an instance of SearchCategoriesInner from a dict
search_categories_inner_from_dict = SearchCategoriesInner.from_dict(search_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


