# GlobalMarketCapChartMarketCapChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_cap** | **List[List[float]]** |  | [optional] 
**volume** | **List[List[float]]** |  | [optional] 

## Example

```python
from coingecko_sdk.models.global_market_cap_chart_market_cap_chart import GlobalMarketCapChartMarketCapChart

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalMarketCapChartMarketCapChart from a JSON string
global_market_cap_chart_market_cap_chart_instance = GlobalMarketCapChartMarketCapChart.from_json(json)
# print the JSON string representation of the object
print(GlobalMarketCapChartMarketCapChart.to_json())

# convert the object into a dict
global_market_cap_chart_market_cap_chart_dict = global_market_cap_chart_market_cap_chart_instance.to_dict()
# create an instance of GlobalMarketCapChartMarketCapChart from a dict
global_market_cap_chart_market_cap_chart_from_dict = GlobalMarketCapChartMarketCapChart.from_dict(global_market_cap_chart_market_cap_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


