# TradesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**TradesDataInnerAttributes**](TradesDataInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.trades_data_inner import TradesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TradesDataInner from a JSON string
trades_data_inner_instance = TradesDataInner.from_json(json)
# print the JSON string representation of the object
print(TradesDataInner.to_json())

# convert the object into a dict
trades_data_inner_dict = trades_data_inner_instance.to_dict()
# create an instance of TradesDataInner from a dict
trades_data_inner_from_dict = TradesDataInner.from_dict(trades_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


