# CategoriesPoolsIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CategoriesPoolsIncludedInnerAttributes**](CategoriesPoolsIncludedInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.categories_pools_included_inner import CategoriesPoolsIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPoolsIncludedInner from a JSON string
categories_pools_included_inner_instance = CategoriesPoolsIncludedInner.from_json(json)
# print the JSON string representation of the object
print(CategoriesPoolsIncludedInner.to_json())

# convert the object into a dict
categories_pools_included_inner_dict = categories_pools_included_inner_instance.to_dict()
# create an instance of CategoriesPoolsIncludedInner from a dict
categories_pools_included_inner_from_dict = CategoriesPoolsIncludedInner.from_dict(categories_pools_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


