# CoinsDataBaseMarketDataMarketCap

coin market cap in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data_market_cap import CoinsDataBaseMarketDataMarketCap

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataMarketCap from a JSON string
coins_data_base_market_data_market_cap_instance = CoinsDataBaseMarketDataMarketCap.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataMarketCap.to_json())

# convert the object into a dict
coins_data_base_market_data_market_cap_dict = coins_data_base_market_data_market_cap_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataMarketCap from a dict
coins_data_base_market_data_market_cap_from_dict = CoinsDataBaseMarketDataMarketCap.from_dict(coins_data_base_market_data_market_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


