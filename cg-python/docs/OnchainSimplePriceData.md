# OnchainSimplePriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OnchainSimplePriceDataAttributes**](OnchainSimplePriceDataAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.onchain_simple_price_data import OnchainSimplePriceData

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainSimplePriceData from a JSON string
onchain_simple_price_data_instance = OnchainSimplePriceData.from_json(json)
# print the JSON string representation of the object
print(OnchainSimplePriceData.to_json())

# convert the object into a dict
onchain_simple_price_data_dict = onchain_simple_price_data_instance.to_dict()
# create an instance of OnchainSimplePriceData from a dict
onchain_simple_price_data_from_dict = OnchainSimplePriceData.from_dict(onchain_simple_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


