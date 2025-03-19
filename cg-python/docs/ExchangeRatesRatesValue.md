# ExchangeRatesRatesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the currency | [optional] 
**unit** | **str** | unit of the currency | [optional] 
**value** | **float** | value of the currency | [optional] 
**type** | **str** | type of the currency | [optional] 

## Example

```python
from coingecko-sdk.models.exchange_rates_rates_value import ExchangeRatesRatesValue

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRatesRatesValue from a JSON string
exchange_rates_rates_value_instance = ExchangeRatesRatesValue.from_json(json)
# print the JSON string representation of the object
print(ExchangeRatesRatesValue.to_json())

# convert the object into a dict
exchange_rates_rates_value_dict = exchange_rates_rates_value_instance.to_dict()
# create an instance of ExchangeRatesRatesValue from a dict
exchange_rates_rates_value_from_dict = ExchangeRatesRatesValue.from_dict(exchange_rates_rates_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


