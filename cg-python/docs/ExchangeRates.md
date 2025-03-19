# ExchangeRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**Dict[str, ExchangeRatesRatesValue]**](ExchangeRatesRatesValue.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.exchange_rates import ExchangeRates

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRates from a JSON string
exchange_rates_instance = ExchangeRates.from_json(json)
# print the JSON string representation of the object
print(ExchangeRates.to_json())

# convert the object into a dict
exchange_rates_dict = exchange_rates_instance.to_dict()
# create an instance of ExchangeRates from a dict
exchange_rates_from_dict = ExchangeRates.from_dict(exchange_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


