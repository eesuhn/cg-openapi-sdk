# CoinsMarkets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**image** | **str** | coin image url | [optional] 
**current_price** | **float** | coin current price in currency | [optional] 
**market_cap** | **float** | coin market cap in currency | [optional] 
**market_cap_rank** | **float** | coin rank by market cap | [optional] 
**fully_diluted_valuation** | **float** | coin fully diluted valuation (fdv) in currency | [optional] 
**total_volume** | **float** | coin total trading volume in currency | [optional] 
**high_24h** | **float** | coin 24hr price high in currency | [optional] 
**low_24h** | **float** | coin 24hr price low in currency | [optional] 
**price_change_24h** | **float** | coin 24hr price change in currency | [optional] 
**price_change_percentage_24h** | **float** | coin 24hr price change in percentage | [optional] 
**market_cap_change_24h** | **float** | coin 24hr market cap change in currency | [optional] 
**market_cap_change_percentage_24h** | **float** | coin 24hr market cap change in percentage | [optional] 
**circulating_supply** | **float** | coin circulating supply | [optional] 
**total_supply** | **float** | coin total supply | [optional] 
**max_supply** | **float** | coin max supply | [optional] 
**ath** | **float** | coin all time high (ath) in currency | [optional] 
**ath_change_percentage** | **float** | coin all time high (ath) change in percentage | [optional] 
**ath_date** | **datetime** | coin all time high (ath) date | [optional] 
**atl** | **float** | coin all time low (atl) in currency | [optional] 
**atl_change_percentage** | **float** | coin all time low (atl) change in percentage | [optional] 
**atl_date** | **datetime** | coin all time low (atl) date | [optional] 
**roi** | **str** |  | [optional] 
**last_updated** | **datetime** | coin last updated timestamp | [optional] 
**price_change_percentage_1h** | **float** | coin 1h price change in percentage | [optional] 
**sparkline_in_7d** | [**CoinsMarketsSparklineIn7d**](CoinsMarketsSparklineIn7d.md) |  | [optional] 

## Example

```python
from coingecko_python.models.coins_markets import CoinsMarkets

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsMarkets from a JSON string
coins_markets_instance = CoinsMarkets.from_json(json)
# print the JSON string representation of the object
print(CoinsMarkets.to_json())

# convert the object into a dict
coins_markets_dict = coins_markets_instance.to_dict()
# create an instance of CoinsMarkets from a dict
coins_markets_from_dict = CoinsMarkets.from_dict(coins_markets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


