# OnchainSimplePriceDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_prices** | **Dict[str, str]** |  | [optional] 

## Example

```python
from coingecko-sdk.models.onchain_simple_price_data_attributes import OnchainSimplePriceDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainSimplePriceDataAttributes from a JSON string
onchain_simple_price_data_attributes_instance = OnchainSimplePriceDataAttributes.from_json(json)
# print the JSON string representation of the object
print(OnchainSimplePriceDataAttributes.to_json())

# convert the object into a dict
onchain_simple_price_data_attributes_dict = onchain_simple_price_data_attributes_instance.to_dict()
# create an instance of OnchainSimplePriceDataAttributes from a dict
onchain_simple_price_data_attributes_from_dict = OnchainSimplePriceDataAttributes.from_dict(onchain_simple_price_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


