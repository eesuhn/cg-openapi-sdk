# OHLCV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OHLCVData**](OHLCVData.md) |  | [optional] 
**meta** | [**OHLCVMeta**](OHLCVMeta.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.ohlcv import OHLCV

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCV from a JSON string
ohlcv_instance = OHLCV.from_json(json)
# print the JSON string representation of the object
print(OHLCV.to_json())

# convert the object into a dict
ohlcv_dict = ohlcv_instance.to_dict()
# create an instance of OHLCV from a dict
ohlcv_from_dict = OHLCV.from_dict(ohlcv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


