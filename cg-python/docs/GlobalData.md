# GlobalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_cryptocurrencies** | **float** | number of active cryptocurrencies | [optional] 
**upcoming_icos** | **float** | number of upcoming icos | [optional] 
**ongoing_icos** | **float** | number of ongoing icos | [optional] 
**ended_icos** | **float** | number of ended icos | [optional] 
**markets** | **float** | number of exchanges | [optional] 
**total_market_cap** | [**GlobalDataTotalMarketCap**](GlobalDataTotalMarketCap.md) |  | [optional] 
**total_volume** | [**GlobalDataTotalVolume**](GlobalDataTotalVolume.md) |  | [optional] 
**market_cap_percentage** | [**GlobalDataMarketCapPercentage**](GlobalDataMarketCapPercentage.md) |  | [optional] 

## Example

```python
from coingecko_python.models.global_data import GlobalData

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalData from a JSON string
global_data_instance = GlobalData.from_json(json)
# print the JSON string representation of the object
print(GlobalData.to_json())

# convert the object into a dict
global_data_dict = global_data_instance.to_dict()
# create an instance of GlobalData from a dict
global_data_from_dict = GlobalData.from_dict(global_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


