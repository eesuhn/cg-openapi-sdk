# CoinsHistoricalDataMarketData

coin market data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_price** | [**CoinsHistoricalDataMarketDataCurrentPrice**](CoinsHistoricalDataMarketDataCurrentPrice.md) |  | [optional] 
**market_cap** | [**CoinsHistoricalDataMarketDataMarketCap**](CoinsHistoricalDataMarketDataMarketCap.md) |  | [optional] 
**total_volume** | [**CoinsHistoricalDataMarketDataTotalVolume**](CoinsHistoricalDataMarketDataTotalVolume.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_historical_data_market_data import CoinsHistoricalDataMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataMarketData from a JSON string
coins_historical_data_market_data_instance = CoinsHistoricalDataMarketData.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataMarketData.to_json())

# convert the object into a dict
coins_historical_data_market_data_dict = coins_historical_data_market_data_instance.to_dict()
# create an instance of CoinsHistoricalDataMarketData from a dict
coins_historical_data_market_data_from_dict = CoinsHistoricalDataMarketData.from_dict(coins_historical_data_market_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


