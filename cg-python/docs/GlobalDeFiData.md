# GlobalDeFiData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defi_market_cap** | **str** | defi market cap | [optional] 
**eth_market_cap** | **str** | eth market cap | [optional] 
**defi_to_eth_ratio** | **str** | defi to eth ratio | [optional] 
**trading_volume_24h** | **str** | defi trading volume in 24 hours | [optional] 
**defi_dominance** | **str** | defi dominance | [optional] 
**top_coin_name** | **str** | defi top coin name | [optional] 
**top_coin_defi_dominance** | **float** | defi top coin dominance | [optional] 

## Example

```python
from coingecko_python.models.global_de_fi_data import GlobalDeFiData

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalDeFiData from a JSON string
global_de_fi_data_instance = GlobalDeFiData.from_json(json)
# print the JSON string representation of the object
print(GlobalDeFiData.to_json())

# convert the object into a dict
global_de_fi_data_dict = global_de_fi_data_instance.to_dict()
# create an instance of GlobalDeFiData from a dict
global_de_fi_data_from_dict = GlobalDeFiData.from_dict(global_de_fi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


