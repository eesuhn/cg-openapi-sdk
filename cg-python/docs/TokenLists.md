# TokenLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo_uri** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tokens** | [**List[TokenListsTokensInner]**](TokenListsTokensInner.md) |  | [optional] 

## Example

```python
from coingecko_python.models.token_lists import TokenLists

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLists from a JSON string
token_lists_instance = TokenLists.from_json(json)
# print the JSON string representation of the object
print(TokenLists.to_json())

# convert the object into a dict
token_lists_dict = token_lists_instance.to_dict()
# create an instance of TokenLists from a dict
token_lists_from_dict = TokenLists.from_dict(token_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


