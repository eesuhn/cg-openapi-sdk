# CoinsHistoricalDataMarketDataMarketCap

coin market cap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_historical_data_market_data_market_cap import CoinsHistoricalDataMarketDataMarketCap

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataMarketDataMarketCap from a JSON string
coins_historical_data_market_data_market_cap_instance = CoinsHistoricalDataMarketDataMarketCap.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataMarketDataMarketCap.to_json())

# convert the object into a dict
coins_historical_data_market_data_market_cap_dict = coins_historical_data_market_data_market_cap_instance.to_dict()
# create an instance of CoinsHistoricalDataMarketDataMarketCap from a dict
coins_historical_data_market_data_market_cap_from_dict = CoinsHistoricalDataMarketDataMarketCap.from_dict(coins_historical_data_market_data_market_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


