# OnchainSimplePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OnchainSimplePriceData**](OnchainSimplePriceData.md) |  | [optional] 

## Example

```python
from coingecko_python.models.onchain_simple_price import OnchainSimplePrice

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainSimplePrice from a JSON string
onchain_simple_price_instance = OnchainSimplePrice.from_json(json)
# print the JSON string representation of the object
print(OnchainSimplePrice.to_json())

# convert the object into a dict
onchain_simple_price_dict = onchain_simple_price_instance.to_dict()
# create an instance of OnchainSimplePrice from a dict
onchain_simple_price_from_dict = OnchainSimplePrice.from_dict(onchain_simple_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


