# PoolDataInnerRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**quote_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**network** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**dex** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_data_inner_relationships import PoolDataInnerRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PoolDataInnerRelationships from a JSON string
pool_data_inner_relationships_instance = PoolDataInnerRelationships.from_json(json)
# print the JSON string representation of the object
print(PoolDataInnerRelationships.to_json())

# convert the object into a dict
pool_data_inner_relationships_dict = pool_data_inner_relationships_instance.to_dict()
# create an instance of PoolDataInnerRelationships from a dict
pool_data_inner_relationships_from_dict = PoolDataInnerRelationships.from_dict(pool_data_inner_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


