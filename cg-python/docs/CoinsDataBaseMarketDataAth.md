# CoinsDataBaseMarketDataAth

coin all time high (ath) in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data_ath import CoinsDataBaseMarketDataAth

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataAth from a JSON string
coins_data_base_market_data_ath_instance = CoinsDataBaseMarketDataAth.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataAth.to_json())

# convert the object into a dict
coins_data_base_market_data_ath_dict = coins_data_base_market_data_ath_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataAth from a dict
coins_data_base_market_data_ath_from_dict = CoinsDataBaseMarketDataAth.from_dict(coins_data_base_market_data_ath_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


