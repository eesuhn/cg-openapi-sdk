# TokenIncludedInnerRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**quote_token** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 
**dex** | [**PoolDataInnerRelationshipsBaseToken**](PoolDataInnerRelationshipsBaseToken.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_included_inner_relationships import TokenIncludedInnerRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIncludedInnerRelationships from a JSON string
token_included_inner_relationships_instance = TokenIncludedInnerRelationships.from_json(json)
# print the JSON string representation of the object
print(TokenIncludedInnerRelationships.to_json())

# convert the object into a dict
token_included_inner_relationships_dict = token_included_inner_relationships_instance.to_dict()
# create an instance of TokenIncludedInnerRelationships from a dict
token_included_inner_relationships_from_dict = TokenIncludedInnerRelationships.from_dict(token_included_inner_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


