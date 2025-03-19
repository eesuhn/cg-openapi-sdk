# CoinsTickersTickersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | coin ticker base currency | [optional] 
**target** | **str** | coin ticker target currency | [optional] 
**market** | [**CoinsTickersTickersInnerMarket**](CoinsTickersTickersInnerMarket.md) |  | [optional] 
**last** | **float** | coin ticker last price | [optional] 
**volume** | **float** | coin ticker volume | [optional] 
**cost_to_move_up_usd** | **float** | coin ticker cost to move up in usd | [optional] 
**cost_to_move_down_usd** | **float** | coin ticker cost to move down in usd | [optional] 
**converted_last** | [**CoinsDataBaseTickersInnerConvertedLast**](CoinsDataBaseTickersInnerConvertedLast.md) |  | [optional] 
**converted_volume** | [**CoinsDataBaseTickersInnerConvertedVolume**](CoinsDataBaseTickersInnerConvertedVolume.md) |  | [optional] 
**trust_score** | **str** | coin ticker trust score | [optional] 
**bid_ask_spread_percentage** | **float** | coin ticker bid ask spread percentage | [optional] 
**timestamp** | **str** | coin ticker timestamp | [optional] 
**last_traded_at** | **str** | coin ticker last traded timestamp | [optional] 
**last_fetch_at** | **str** | coin ticker last fetch timestamp | [optional] 
**is_anomaly** | **bool** | coin ticker anomaly | [optional] 
**is_stale** | **bool** | coin ticker stale | [optional] 
**trade_url** | **str** | coin ticker trade url | [optional] 
**token_info_url** | **str** | coin ticker token info url | [optional] 
**coin_id** | **str** | coin ticker base currency coin ID | [optional] 
**target_coin_id** | **str** | coin ticker target currency coin ID | [optional] 

## Example

```python
from coingecko_python.models.coins_tickers_tickers_inner import CoinsTickersTickersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsTickersTickersInner from a JSON string
coins_tickers_tickers_inner_instance = CoinsTickersTickersInner.from_json(json)
# print the JSON string representation of the object
print(CoinsTickersTickersInner.to_json())

# convert the object into a dict
coins_tickers_tickers_inner_dict = coins_tickers_tickers_inner_instance.to_dict()
# create an instance of CoinsTickersTickersInner from a dict
coins_tickers_tickers_inner_from_dict = CoinsTickersTickersInner.from_dict(coins_tickers_tickers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


