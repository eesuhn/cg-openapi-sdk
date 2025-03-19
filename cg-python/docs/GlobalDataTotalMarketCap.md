# GlobalDataTotalMarketCap

cryptocurrencies total market cap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eth** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.global_data_total_market_cap import GlobalDataTotalMarketCap

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalDataTotalMarketCap from a JSON string
global_data_total_market_cap_instance = GlobalDataTotalMarketCap.from_json(json)
# print the JSON string representation of the object
print(GlobalDataTotalMarketCap.to_json())

# convert the object into a dict
global_data_total_market_cap_dict = global_data_total_market_cap_instance.to_dict()
# create an instance of GlobalDataTotalMarketCap from a dict
global_data_total_market_cap_from_dict = GlobalDataTotalMarketCap.from_dict(global_data_total_market_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


