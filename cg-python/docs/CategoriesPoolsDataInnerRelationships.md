# CategoriesPoolsDataInnerRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**dex** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**base_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**quote_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 

## Example

```python
from coingecko_python.models.categories_pools_data_inner_relationships import CategoriesPoolsDataInnerRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPoolsDataInnerRelationships from a JSON string
categories_pools_data_inner_relationships_instance = CategoriesPoolsDataInnerRelationships.from_json(json)
# print the JSON string representation of the object
print(CategoriesPoolsDataInnerRelationships.to_json())

# convert the object into a dict
categories_pools_data_inner_relationships_dict = categories_pools_data_inner_relationships_instance.to_dict()
# create an instance of CategoriesPoolsDataInnerRelationships from a dict
categories_pools_data_inner_relationships_from_dict = CategoriesPoolsDataInnerRelationships.from_dict(categories_pools_data_inner_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


