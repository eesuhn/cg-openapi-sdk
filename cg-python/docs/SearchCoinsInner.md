# SearchCoinsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**name** | **str** | coin name | [optional] 
**api_symbol** | **str** | coin api symbol | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**market_cap_rank** | **float** | coin market cap rank | [optional] 
**thumb** | **str** | coin thumb image url | [optional] 
**large** | **str** | coin large image url | [optional] 

## Example

```python
from coingecko_sdk.models.search_coins_inner import SearchCoinsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCoinsInner from a JSON string
search_coins_inner_instance = SearchCoinsInner.from_json(json)
# print the JSON string representation of the object
print(SearchCoinsInner.to_json())

# convert the object into a dict
search_coins_inner_dict = search_coins_inner_instance.to_dict()
# create an instance of SearchCoinsInner from a dict
search_coins_inner_from_dict = SearchCoinsInner.from_dict(search_coins_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


