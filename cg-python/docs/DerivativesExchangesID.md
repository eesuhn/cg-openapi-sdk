# DerivativesExchangesID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | derivatives exchange name | [optional] 
**open_interest_btc** | **float** | derivatives exchange open interest in BTC | [optional] 
**trade_volume_24h_btc** | **str** | derivatives exchange trade volume in BTC in 24 hours | [optional] 
**number_of_perpetual_pairs** | **float** | number of perpetual pairs in the derivatives exchange | [optional] 
**number_of_futures_pairs** | **float** | number of futures pairs in the derivatives exchange | [optional] 
**image** | **str** | derivatives exchange image url | [optional] 
**year_established** | **float** | derivatives exchange established year | [optional] 
**country** | **str** | derivatives exchange incorporated country | [optional] 
**description** | **str** | derivatives exchange description | [optional] 
**url** | **str** | derivatives exchange website url | [optional] 
**tickers** | [**List[DerivativesTickersList]**](DerivativesTickersList.md) |  | [optional] 

## Example

```python
from coingecko_python.models.derivatives_exchanges_id import DerivativesExchangesID

# TODO update the JSON string below
json = "{}"
# create an instance of DerivativesExchangesID from a JSON string
derivatives_exchanges_id_instance = DerivativesExchangesID.from_json(json)
# print the JSON string representation of the object
print(DerivativesExchangesID.to_json())

# convert the object into a dict
derivatives_exchanges_id_dict = derivatives_exchanges_id_instance.to_dict()
# create an instance of DerivativesExchangesID from a dict
derivatives_exchanges_id_from_dict = DerivativesExchangesID.from_dict(derivatives_exchanges_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


