# ExchangeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | exchange name | [optional] 
**year_established** | **float** | exchange established year | [optional] 
**country** | **str** | exchange incorporated country | [optional] 
**description** | **str** | exchange description | [optional] 
**url** | **str** | exchange website url | [optional] 
**image** | **str** | exchange image url | [optional] 
**facebook_url** | **str** | exchange facebook url | [optional] 
**reddit_url** | **str** | exchange reddit url | [optional] 
**telegram_url** | **str** | exchange telegram url | [optional] 
**slack_url** | **str** | exchange slack url | [optional] 
**other_url_1** | **str** |  | [optional] 
**other_url_2** | **str** |  | [optional] 
**twitter_handle** | **str** | exchange twitter handle | [optional] 
**has_trading_incentive** | **bool** | exchange trading incentive | [optional] 
**centralized** | **bool** | exchange type (true for centralized, false for decentralized) | [optional] 
**public_notice** | **str** | public notice for exchange | [optional] 
**alert_notice** | **str** | alert notice for exchange | [optional] 
**trust_score** | **float** | exchange trust score | [optional] 
**trust_score_rank** | **float** | exchange trust score rank | [optional] 
**trade_volume_24h_btc** | **float** |  | [optional] 
**trade_volume_24h_btc_normalized** | **float** | normalized trading volume by traffic in BTC in 24 hours &lt;br&gt; *refers to [&#x60;this blog&#x60;](https://blog.coingecko.com/trust-score/). | [optional] 
**coins** | **float** | number of coins listed on the exchange | [optional] 
**pairs** | **float** | number of trading pairs on the exchange | [optional] 
**tickers** | [**List[CoinsTickers]**](CoinsTickers.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.exchange_data import ExchangeData

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeData from a JSON string
exchange_data_instance = ExchangeData.from_json(json)
# print the JSON string representation of the object
print(ExchangeData.to_json())

# convert the object into a dict
exchange_data_dict = exchange_data_instance.to_dict()
# create an instance of ExchangeData from a dict
exchange_data_from_dict = ExchangeData.from_dict(exchange_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


