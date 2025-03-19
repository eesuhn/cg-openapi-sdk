# CoinsTickersTickersInnerMarket

coin ticker exchange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | exchange name | 
**identifier** | **str** | exchange identifier | 
**has_trading_incentive** | **bool** | exchange trading incentive | 
**logo** | **str** | exchange image url | [optional] 

## Example

```python
from coingecko_python.models.coins_tickers_tickers_inner_market import CoinsTickersTickersInnerMarket

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsTickersTickersInnerMarket from a JSON string
coins_tickers_tickers_inner_market_instance = CoinsTickersTickersInnerMarket.from_json(json)
# print the JSON string representation of the object
print(CoinsTickersTickersInnerMarket.to_json())

# convert the object into a dict
coins_tickers_tickers_inner_market_dict = coins_tickers_tickers_inner_market_instance.to_dict()
# create an instance of CoinsTickersTickersInnerMarket from a dict
coins_tickers_tickers_inner_market_from_dict = CoinsTickersTickersInnerMarket.from_dict(coins_tickers_tickers_inner_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


