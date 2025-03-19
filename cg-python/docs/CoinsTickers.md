# CoinsTickers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | coin name | [optional] 
**tickers** | [**List[CoinsTickersTickersInner]**](CoinsTickersTickersInner.md) | list of tickers | [optional] 

## Example

```python
from coingecko_sdk.models.coins_tickers import CoinsTickers

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsTickers from a JSON string
coins_tickers_instance = CoinsTickers.from_json(json)
# print the JSON string representation of the object
print(CoinsTickers.to_json())

# convert the object into a dict
coins_tickers_dict = coins_tickers_instance.to_dict()
# create an instance of CoinsTickers from a dict
coins_tickers_from_dict = CoinsTickers.from_dict(coins_tickers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


