# CoinsDataBaseTickersInnerConvertedVolume

coin ticker converted volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eth** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_data_base_tickers_inner_converted_volume import CoinsDataBaseTickersInnerConvertedVolume

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseTickersInnerConvertedVolume from a JSON string
coins_data_base_tickers_inner_converted_volume_instance = CoinsDataBaseTickersInnerConvertedVolume.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseTickersInnerConvertedVolume.to_json())

# convert the object into a dict
coins_data_base_tickers_inner_converted_volume_dict = coins_data_base_tickers_inner_converted_volume_instance.to_dict()
# create an instance of CoinsDataBaseTickersInnerConvertedVolume from a dict
coins_data_base_tickers_inner_converted_volume_from_dict = CoinsDataBaseTickersInnerConvertedVolume.from_dict(coins_data_base_tickers_inner_converted_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


