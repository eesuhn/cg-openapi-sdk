# OHLCVMetaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**coingecko_coin_id** | **str** |  | [optional] 

## Example

```python
from coingecko-sdk.models.ohlcv_meta_base import OHLCVMetaBase

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVMetaBase from a JSON string
ohlcv_meta_base_instance = OHLCVMetaBase.from_json(json)
# print the JSON string representation of the object
print(OHLCVMetaBase.to_json())

# convert the object into a dict
ohlcv_meta_base_dict = ohlcv_meta_base_instance.to_dict()
# create an instance of OHLCVMetaBase from a dict
ohlcv_meta_base_from_dict = OHLCVMetaBase.from_dict(ohlcv_meta_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


