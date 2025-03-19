# OHLCVData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OHLCVDataAttributes**](OHLCVDataAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.ohlcv_data import OHLCVData

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVData from a JSON string
ohlcv_data_instance = OHLCVData.from_json(json)
# print the JSON string representation of the object
print(OHLCVData.to_json())

# convert the object into a dict
ohlcv_data_dict = ohlcv_data_instance.to_dict()
# create an instance of OHLCVData from a dict
ohlcv_data_from_dict = OHLCVData.from_dict(ohlcv_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


