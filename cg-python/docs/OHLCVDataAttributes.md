# OHLCVDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ohlcv_list** | **List[List[float]]** |  | [optional] 

## Example

```python
from coingecko-sdk.models.ohlcv_data_attributes import OHLCVDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVDataAttributes from a JSON string
ohlcv_data_attributes_instance = OHLCVDataAttributes.from_json(json)
# print the JSON string representation of the object
print(OHLCVDataAttributes.to_json())

# convert the object into a dict
ohlcv_data_attributes_dict = ohlcv_data_attributes_instance.to_dict()
# create an instance of OHLCVDataAttributes from a dict
ohlcv_data_attributes_from_dict = OHLCVDataAttributes.from_dict(ohlcv_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


