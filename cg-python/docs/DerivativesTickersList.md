# DerivativesTickersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market** | **str** | derivative market name | [optional] 
**symbol** | **str** | derivative ticker symbol | [optional] 
**index_id** | **str** | derivative underlying asset | [optional] 
**price** | **str** | derivative ticker price | [optional] 
**price_percentage_change_24h** | **float** | derivative ticker price percentage change in 24 hours | [optional] 
**contract_type** | **str** | derivative contract type | [optional] 
**index** | **float** | derivative underlying asset price | [optional] 
**basis** | **float** | difference of derivative price and index price | [optional] 
**spread** | **float** | derivative bid ask spread | [optional] 
**funding_rate** | **float** | derivative funding rate | [optional] 
**open_interest** | **float** | derivative open interest | [optional] 
**volume_24h** | **float** | derivative volume in 24 hours | [optional] 
**last_traded_at** | **float** | derivative last updated time | [optional] 
**expired_at** | **str** |  | [optional] 

## Example

```python
from coingecko_python.models.derivatives_tickers_list import DerivativesTickersList

# TODO update the JSON string below
json = "{}"
# create an instance of DerivativesTickersList from a JSON string
derivatives_tickers_list_instance = DerivativesTickersList.from_json(json)
# print the JSON string representation of the object
print(DerivativesTickersList.to_json())

# convert the object into a dict
derivatives_tickers_list_dict = derivatives_tickers_list_instance.to_dict()
# create an instance of DerivativesTickersList from a dict
derivatives_tickers_list_from_dict = DerivativesTickersList.from_dict(derivatives_tickers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


