# TokenDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_pools** | [**TokenDataRelationshipsTopPools**](TokenDataRelationshipsTopPools.md) |  | [optional] 

## Example

```python
from coingecko_python.models.token_data_relationships import TokenDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDataRelationships from a JSON string
token_data_relationships_instance = TokenDataRelationships.from_json(json)
# print the JSON string representation of the object
print(TokenDataRelationships.to_json())

# convert the object into a dict
token_data_relationships_dict = token_data_relationships_instance.to_dict()
# create an instance of TokenDataRelationships from a dict
token_data_relationships_from_dict = TokenDataRelationships.from_dict(token_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


