# TokenIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**TokenIncludedInnerAttributes**](TokenIncludedInnerAttributes.md) |  | [optional] 
**relationships** | [**TokenIncludedInnerRelationships**](TokenIncludedInnerRelationships.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.token_included_inner import TokenIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIncludedInner from a JSON string
token_included_inner_instance = TokenIncludedInner.from_json(json)
# print the JSON string representation of the object
print(TokenIncludedInner.to_json())

# convert the object into a dict
token_included_inner_dict = token_included_inner_instance.to_dict()
# create an instance of TokenIncludedInner from a dict
token_included_inner_from_dict = TokenIncludedInner.from_dict(token_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


