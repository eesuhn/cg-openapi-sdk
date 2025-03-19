# CategoriesPools


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CategoriesPoolsDataInner]**](CategoriesPoolsDataInner.md) |  | [optional] 
**included** | [**List[CategoriesPoolsIncludedInner]**](CategoriesPoolsIncludedInner.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.categories_pools import CategoriesPools

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPools from a JSON string
categories_pools_instance = CategoriesPools.from_json(json)
# print the JSON string representation of the object
print(CategoriesPools.to_json())

# convert the object into a dict
categories_pools_dict = categories_pools_instance.to_dict()
# create an instance of CategoriesPools from a dict
categories_pools_from_dict = CategoriesPools.from_dict(categories_pools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


