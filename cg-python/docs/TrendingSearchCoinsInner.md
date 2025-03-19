# TrendingSearchCoinsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**coin_id** | **float** |  | [optional] 
**name** | **str** | coin name | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**market_cap_rank** | **float** | coin market cap rank | [optional] 
**thumb** | **str** | coin thumb image url | [optional] 
**small** | **str** | coin small image url | [optional] 
**large** | **str** | coin large image url | [optional] 
**slug** | **str** | coin web slug | [optional] 
**price_btc** | **float** | coin price in btc | [optional] 
**score** | **float** | coin sequence in the list | [optional] 
**data** | [**TrendingSearchCoinsInnerData**](TrendingSearchCoinsInnerData.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.trending_search_coins_inner import TrendingSearchCoinsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchCoinsInner from a JSON string
trending_search_coins_inner_instance = TrendingSearchCoinsInner.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchCoinsInner.to_json())

# convert the object into a dict
trending_search_coins_inner_dict = trending_search_coins_inner_instance.to_dict()
# create an instance of TrendingSearchCoinsInner from a dict
trending_search_coins_inner_from_dict = TrendingSearchCoinsInner.from_dict(trending_search_coins_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


