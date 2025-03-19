# CoinsDataBaseMarketDataTotalVolume

coin total trading volume in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data_total_volume import CoinsDataBaseMarketDataTotalVolume

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataTotalVolume from a JSON string
coins_data_base_market_data_total_volume_instance = CoinsDataBaseMarketDataTotalVolume.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataTotalVolume.to_json())

# convert the object into a dict
coins_data_base_market_data_total_volume_dict = coins_data_base_market_data_total_volume_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataTotalVolume from a dict
coins_data_base_market_data_total_volume_from_dict = CoinsDataBaseMarketDataTotalVolume.from_dict(coins_data_base_market_data_total_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


