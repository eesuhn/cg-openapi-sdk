# CoinsDataBaseMarketDataAtl

coin all time low (atl) in currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eur** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data_atl import CoinsDataBaseMarketDataAtl

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketDataAtl from a JSON string
coins_data_base_market_data_atl_instance = CoinsDataBaseMarketDataAtl.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketDataAtl.to_json())

# convert the object into a dict
coins_data_base_market_data_atl_dict = coins_data_base_market_data_atl_instance.to_dict()
# create an instance of CoinsDataBaseMarketDataAtl from a dict
coins_data_base_market_data_atl_from_dict = CoinsDataBaseMarketDataAtl.from_dict(coins_data_base_market_data_atl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


