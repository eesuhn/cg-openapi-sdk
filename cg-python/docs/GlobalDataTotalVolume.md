# GlobalDataTotalVolume

cryptocurrencies total volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **float** |  | [optional] 
**eth** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.global_data_total_volume import GlobalDataTotalVolume

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalDataTotalVolume from a JSON string
global_data_total_volume_instance = GlobalDataTotalVolume.from_json(json)
# print the JSON string representation of the object
print(GlobalDataTotalVolume.to_json())

# convert the object into a dict
global_data_total_volume_dict = global_data_total_volume_instance.to_dict()
# create an instance of GlobalDataTotalVolume from a dict
global_data_total_volume_from_dict = GlobalDataTotalVolume.from_dict(global_data_total_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


