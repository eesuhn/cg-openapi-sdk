# Exchanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | exchange ID | [optional] 
**name** | **str** | exchange name | [optional] 
**year_established** | **float** | exchange established year | [optional] 
**country** | **str** | exchange country | [optional] 
**description** | **str** | exchange description | [optional] 
**url** | **str** | exchange website url | [optional] 
**image** | **str** | exchange image url | [optional] 
**has_trading_incentive** | **bool** | exchange trading incentive | [optional] 
**trust_score** | **float** | exchange trust score | [optional] 
**trust_score_rank** | **float** | exchange trust score rank | [optional] 
**trade_volume_24h_btc** | **float** | exchange trade volume in BTC in 24 hours | [optional] 
**trade_volume_24h_btc_normalized** | **float** | normalized trading volume by traffic in BTC in 24 hours &lt;br&gt; *refers to [&#x60;this blog&#x60;](https://blog.coingecko.com/trust-score/). | [optional] 

## Example

```python
from coingecko_python.models.exchanges import Exchanges

# TODO update the JSON string below
json = "{}"
# create an instance of Exchanges from a JSON string
exchanges_instance = Exchanges.from_json(json)
# print the JSON string representation of the object
print(Exchanges.to_json())

# convert the object into a dict
exchanges_dict = exchanges_instance.to_dict()
# create an instance of Exchanges from a dict
exchanges_from_dict = Exchanges.from_dict(exchanges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


