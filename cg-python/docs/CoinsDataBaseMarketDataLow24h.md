# CoinsDataBaseMarketDataLow24h

coin 24hr price low in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_data_base_market_data_low24h import CoinsDataBaseMarketDataLow24h

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataLow24h from a JSON string
coins_data_base_market_data_low24h_instance = CoinsDataBaseMarketDataLow24h.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataLow24h.to_json())

# convert the object into a dict
coins_data_base_market_data_low24h_dict = coins_data_base_market_data_low24h_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataLow24h from a dict
coins_data_base_market_data_low24h_from_dict = CoinsDataBaseMarketDataLow24h.from_dict(coins_data_base_market_data_low24h_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


