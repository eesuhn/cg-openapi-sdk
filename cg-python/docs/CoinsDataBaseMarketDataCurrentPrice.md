# CoinsDataBaseMarketDataCurrentPrice

coin current price in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data_current_price import CoinsDataBaseMarketDataCurrentPrice

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataCurrentPrice from a JSON string
coins_data_base_market_data_current_price_instance = CoinsDataBaseMarketDataCurrentPrice.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataCurrentPrice.to_json())

# convert the object into a dict
coins_data_base_market_data_current_price_dict = coins_data_base_market_data_current_price_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataCurrentPrice from a dict
coins_data_base_market_data_current_price_from_dict = CoinsDataBaseMarketDataCurrentPrice.from_dict(coins_data_base_market_data_current_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


