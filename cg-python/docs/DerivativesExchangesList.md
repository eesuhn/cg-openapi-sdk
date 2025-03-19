# DerivativesExchangesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | derivatives exchange ID | [optional] 
**name** | **str** | derivatives exchange name | [optional] 

## Example

```python
from coingecko-sdk.models.derivatives_exchanges_list import DerivativesExchangesList

# TODO update the JSON string below
json = "{}"
# create an instance of DerivativesExchangesList from a JSON string
derivatives_exchanges_list_instance = DerivativesExchangesList.from_json(json)
# print the JSON string representation of the object
print(DerivativesExchangesList.to_json())

# convert the object into a dict
derivatives_exchanges_list_dict = derivatives_exchanges_list_instance.to_dict()
# create an instance of DerivativesExchangesList from a dict
derivatives_exchanges_list_from_dict = DerivativesExchangesList.from_dict(derivatives_exchanges_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


