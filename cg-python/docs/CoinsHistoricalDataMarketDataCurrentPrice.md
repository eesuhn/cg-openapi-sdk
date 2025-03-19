# CoinsHistoricalDataMarketDataCurrentPrice

coin current price

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.coins_historical_data_market_data_current_price import CoinsHistoricalDataMarketDataCurrentPrice

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataMarketDataCurrentPrice from a JSON string
coins_historical_data_market_data_current_price_instance = CoinsHistoricalDataMarketDataCurrentPrice.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataMarketDataCurrentPrice.to_json())

# convert the object into a dict
coins_historical_data_market_data_current_price_dict = coins_historical_data_market_data_current_price_instance.to_dict()
# create an instance of CoinsHistoricalDataMarketDataCurrentPrice from a dict
coins_historical_data_market_data_current_price_from_dict = CoinsHistoricalDataMarketDataCurrentPrice.from_dict(coins_historical_data_market_data_current_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


