# CoinsHistoricalDataMarketDataTotalVolume

coin total volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.coins_historical_data_market_data_total_volume import CoinsHistoricalDataMarketDataTotalVolume

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataMarketDataTotalVolume from a JSON string
coins_historical_data_market_data_total_volume_instance = CoinsHistoricalDataMarketDataTotalVolume.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataMarketDataTotalVolume.to_json())

# convert the object into a dict
coins_historical_data_market_data_total_volume_dict = coins_historical_data_market_data_total_volume_instance.to_dict()
# create an instance of CoinsHistoricalDataMarketDataTotalVolume from a dict
coins_historical_data_market_data_total_volume_from_dict = CoinsHistoricalDataMarketDataTotalVolume.from_dict(coins_historical_data_market_data_total_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


