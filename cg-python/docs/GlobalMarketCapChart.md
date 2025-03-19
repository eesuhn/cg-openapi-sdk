# GlobalMarketCapChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_cap_chart** | [**GlobalMarketCapChartMarketCapChart**](GlobalMarketCapChartMarketCapChart.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.global_market_cap_chart import GlobalMarketCapChart

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalMarketCapChart from a JSON string
global_market_cap_chart_instance = GlobalMarketCapChart.from_json(json)
# print the JSON string representation of the object
print(GlobalMarketCapChart.to_json())

# convert the object into a dict
global_market_cap_chart_dict = global_market_cap_chart_instance.to_dict()
# create an instance of GlobalMarketCapChart from a dict
global_market_cap_chart_from_dict = GlobalMarketCapChart.from_dict(global_market_cap_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


