# GlobalDataMarketCapPercentage

cryptocurrencies market cap percentage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eth** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.global_data_market_cap_percentage import GlobalDataMarketCapPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalDataMarketCapPercentage from a JSON string
global_data_market_cap_percentage_instance = GlobalDataMarketCapPercentage.from_json(json)
# print the JSON string representation of the object
print(GlobalDataMarketCapPercentage.to_json())

# convert the object into a dict
global_data_market_cap_percentage_dict = global_data_market_cap_percentage_instance.to_dict()
# create an instance of GlobalDataMarketCapPercentage from a dict
global_data_market_cap_percentage_from_dict = GlobalDataMarketCapPercentage.from_dict(global_data_market_cap_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


