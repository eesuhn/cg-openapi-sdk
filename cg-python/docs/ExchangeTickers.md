# ExchangeTickers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | coin name | [optional] 
**tickers** | [**List[CoinsTickersTickersInner]**](CoinsTickersTickersInner.md) | list of tickers | [optional] 

## Example

```python
from coingecko-sdk.models.exchange_tickers import ExchangeTickers

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTickers from a JSON string
exchange_tickers_instance = ExchangeTickers.from_json(json)
# print the JSON string representation of the object
print(ExchangeTickers.to_json())

# convert the object into a dict
exchange_tickers_dict = exchange_tickers_instance.to_dict()
# create an instance of ExchangeTickers from a dict
exchange_tickers_from_dict = ExchangeTickers.from_dict(exchange_tickers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


