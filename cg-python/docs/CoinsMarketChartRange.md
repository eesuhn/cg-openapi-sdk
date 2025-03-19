# CoinsMarketChartRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prices** | **List[List[float]]** |  | [optional] 
**market_caps** | **List[List[float]]** |  | [optional] 
**total_volumes** | **List[List[float]]** |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_market_chart_range import CoinsMarketChartRange

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsMarketChartRange from a JSON string
coins_market_chart_range_instance = CoinsMarketChartRange.from_json(json)
# print the JSON string representation of the object
print(CoinsMarketChartRange.to_json())

# convert the object into a dict
coins_market_chart_range_dict = coins_market_chart_range_instance.to_dict()
# create an instance of CoinsMarketChartRange from a dict
coins_market_chart_range_from_dict = CoinsMarketChartRange.from_dict(coins_market_chart_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


