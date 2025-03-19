# CoinsMarketChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prices** | **List[List[float]]** |  | [optional] 
**market_caps** | **List[List[float]]** |  | [optional] 
**total_volumes** | **List[List[float]]** |  | [optional] 

## Example

```python
from coingecko_python.models.coins_market_chart import CoinsMarketChart

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsMarketChart from a JSON string
coins_market_chart_instance = CoinsMarketChart.from_json(json)
# print the JSON string representation of the object
print(CoinsMarketChart.to_json())

# convert the object into a dict
coins_market_chart_dict = coins_market_chart_instance.to_dict()
# create an instance of CoinsMarketChart from a dict
coins_market_chart_from_dict = CoinsMarketChart.from_dict(coins_market_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


