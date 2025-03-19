# TokenDataRelationshipsTopPools


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PoolDataInnerRelationshipsBaseTokenData]**](PoolDataInnerRelationshipsBaseTokenData.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.token_data_relationships_top_pools import TokenDataRelationshipsTopPools

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDataRelationshipsTopPools from a JSON string
token_data_relationships_top_pools_instance = TokenDataRelationshipsTopPools.from_json(json)
# print the JSON string representation of the object
print(TokenDataRelationshipsTopPools.to_json())

# convert the object into a dict
token_data_relationships_top_pools_dict = token_data_relationships_top_pools_instance.to_dict()
# create an instance of TokenDataRelationshipsTopPools from a dict
token_data_relationships_top_pools_from_dict = TokenDataRelationshipsTopPools.from_dict(token_data_relationships_top_pools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


