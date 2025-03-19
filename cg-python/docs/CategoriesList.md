# CategoriesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | category ID | [optional] 
**name** | **str** | category name | [optional] 

## Example

```python
from coingecko_python.models.categories_list import CategoriesList

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesList from a JSON string
categories_list_instance = CategoriesList.from_json(json)
# print the JSON string representation of the object
print(CategoriesList.to_json())

# convert the object into a dict
categories_list_dict = categories_list_instance.to_dict()
# create an instance of CategoriesList from a dict
categories_list_from_dict = CategoriesList.from_dict(categories_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


