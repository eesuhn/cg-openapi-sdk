# Trades


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TradesDataInner]**](TradesDataInner.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.trades import Trades

# TODO update the JSON string below
json = "{}"
# create an instance of Trades from a JSON string
trades_instance = Trades.from_json(json)
# print the JSON string representation of the object
print(Trades.to_json())

# convert the object into a dict
trades_dict = trades_instance.to_dict()
# create an instance of Trades from a dict
trades_from_dict = Trades.from_dict(trades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


