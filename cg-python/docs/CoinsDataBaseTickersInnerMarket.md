# CoinsDataBaseTickersInnerMarket

coin ticker exchange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | coin ticker exchange name | [optional] 
**identifier** | **str** | coin ticker exchange identifier | [optional] 
**has_trading_incentive** | **bool** | coin ticker exchange trading incentive | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_tickers_inner_market import CoinsDataBaseTickersInnerMarket

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseTickersInnerMarket from a JSON string
coins_data_base_tickers_inner_market_instance = CoinsDataBaseTickersInnerMarket.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseTickersInnerMarket.to_json())

# convert the object into a dict
coins_data_base_tickers_inner_market_dict = coins_data_base_tickers_inner_market_instance.to_dict()
# create an instance of CoinsDataBaseTickersInnerMarket from a dict
coins_data_base_tickers_inner_market_from_dict = CoinsDataBaseTickersInnerMarket.from_dict(coins_data_base_tickers_inner_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


