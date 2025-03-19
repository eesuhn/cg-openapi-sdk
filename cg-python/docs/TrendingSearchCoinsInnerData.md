# TrendingSearchCoinsInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | coin price in usd | [optional] 
**price_btc** | **str** | coin price in btc | [optional] 
**price_change_percentage_24h** | [**TrendingSearchCoinsInnerDataPriceChangePercentage24h**](TrendingSearchCoinsInnerDataPriceChangePercentage24h.md) |  | [optional] 
**market_cap** | **str** | coin market cap in usd | [optional] 
**market_cap_btc** | **str** | coin market cap in btc | [optional] 
**total_volume** | **str** | coin total volume in usd | [optional] 
**total_volume_btc** | **str** | coin total volume in btc | [optional] 
**sparkline** | **str** | coin sparkline image url | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from coingecko_python.models.trending_search_coins_inner_data import TrendingSearchCoinsInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchCoinsInnerData from a JSON string
trending_search_coins_inner_data_instance = TrendingSearchCoinsInnerData.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchCoinsInnerData.to_json())

# convert the object into a dict
trending_search_coins_inner_data_dict = trending_search_coins_inner_data_instance.to_dict()
# create an instance of TrendingSearchCoinsInnerData from a dict
trending_search_coins_inner_data_from_dict = TrendingSearchCoinsInnerData.from_dict(trending_search_coins_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


