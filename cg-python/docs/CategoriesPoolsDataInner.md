# CategoriesPoolsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CategoriesPoolsDataInnerAttributes**](CategoriesPoolsDataInnerAttributes.md) |  | [optional] 
**relationships** | [**CategoriesPoolsDataInnerRelationships**](CategoriesPoolsDataInnerRelationships.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.categories_pools_data_inner import CategoriesPoolsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPoolsDataInner from a JSON string
categories_pools_data_inner_instance = CategoriesPoolsDataInner.from_json(json)
# print the JSON string representation of the object
print(CategoriesPoolsDataInner.to_json())

# convert the object into a dict
categories_pools_data_inner_dict = categories_pools_data_inner_instance.to_dict()
# create an instance of CategoriesPoolsDataInner from a dict
categories_pools_data_inner_from_dict = CategoriesPoolsDataInner.from_dict(categories_pools_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


