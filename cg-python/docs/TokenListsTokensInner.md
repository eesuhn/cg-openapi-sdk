# TokenListsTokensInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **float** | chainlist&#39;s chain ID | [optional] 
**address** | **str** | token contract address | [optional] 
**name** | **str** | token name | [optional] 
**symbol** | **str** | token symbol | [optional] 
**decimals** | **float** | token decimals | [optional] 
**logo_uri** | **str** | token image url | [optional] 

## Example

```python
from coingecko_sdk.models.token_lists_tokens_inner import TokenListsTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenListsTokensInner from a JSON string
token_lists_tokens_inner_instance = TokenListsTokensInner.from_json(json)
# print the JSON string representation of the object
print(TokenListsTokensInner.to_json())

# convert the object into a dict
token_lists_tokens_inner_dict = token_lists_tokens_inner_instance.to_dict()
# create an instance of TokenListsTokensInner from a dict
token_lists_tokens_inner_from_dict = TokenListsTokensInner.from_dict(token_lists_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


