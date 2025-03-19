# DerivativesExchanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | derivatives exchange name | [optional] 
**id** | **str** | derivatives exchange ID | [optional] 
**open_interest_btc** | **float** | derivatives exchange open interest in BTC | [optional] 
**trade_volume_24h_btc** | **str** | derivatives exchange trade volume in BTC in 24 hours | [optional] 
**number_of_perpetual_pairs** | **float** | number of perpetual pairs in the derivatives exchange | [optional] 
**number_of_futures_pairs** | **float** | number of futures pairs in the derivatives exchange | [optional] 
**image** | **str** | derivatives exchange image url | [optional] 
**year_established** | **float** | derivatives exchange established year | [optional] 
**country** | **str** | derivatives exchange incorporated country | [optional] 
**description** | **str** | derivatives exchange description | [optional] 
**url** | **str** | derivatives exchange website url | [optional] 

## Example

```python
from coingecko-sdk.models.derivatives_exchanges import DerivativesExchanges

# TODO update the JSON string below
json = "{}"
# create an instance of DerivativesExchanges from a JSON string
derivatives_exchanges_instance = DerivativesExchanges.from_json(json)
# print the JSON string representation of the object
print(DerivativesExchanges.to_json())

# convert the object into a dict
derivatives_exchanges_dict = derivatives_exchanges_instance.to_dict()
# create an instance of DerivativesExchanges from a dict
derivatives_exchanges_from_dict = DerivativesExchanges.from_dict(derivatives_exchanges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


