# OHLCVMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**OHLCVMetaBase**](OHLCVMetaBase.md) |  | [optional] 
**quote** | [**OHLCVMetaBase**](OHLCVMetaBase.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.ohlcv_meta import OHLCVMeta

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVMeta from a JSON string
ohlcv_meta_instance = OHLCVMeta.from_json(json)
# print the JSON string representation of the object
print(OHLCVMeta.to_json())

# convert the object into a dict
ohlcv_meta_dict = ohlcv_meta_instance.to_dict()
# create an instance of OHLCVMeta from a dict
ohlcv_meta_from_dict = OHLCVMeta.from_dict(ohlcv_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


