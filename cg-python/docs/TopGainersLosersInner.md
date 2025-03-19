# TopGainersLosersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**image** | **str** | coin image url | [optional] 
**market_cap_rank** | **float** | coin rank by market cap | [optional] 
**usd** | **float** | coin price in USD | [optional] 
**usd_24h_vol** | **float** | coin 24hr volume in USD | [optional] 
**usd_1y_change** | **float** | coin 1 year change in USD | [optional] 

## Example

```python
from coingecko-sdk.models.top_gainers_losers_inner import TopGainersLosersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TopGainersLosersInner from a JSON string
top_gainers_losers_inner_instance = TopGainersLosersInner.from_json(json)
# print the JSON string representation of the object
print(TopGainersLosersInner.to_json())

# convert the object into a dict
top_gainers_losers_inner_dict = top_gainers_losers_inner_instance.to_dict()
# create an instance of TopGainersLosersInner from a dict
top_gainers_losers_inner_from_dict = TopGainersLosersInner.from_dict(top_gainers_losers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


