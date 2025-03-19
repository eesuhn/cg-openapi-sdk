# CoinsListNewInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**activated_at** | **float** | timestamp when coin was activated on CoinGecko | [optional] 

## Example

```python
from coingecko_sdk.models.coins_list_new_inner import CoinsListNewInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsListNewInner from a JSON string
coins_list_new_inner_instance = CoinsListNewInner.from_json(json)
# print the JSON string representation of the object
print(CoinsListNewInner.to_json())

# convert the object into a dict
coins_list_new_inner_dict = coins_list_new_inner_instance.to_dict()
# create an instance of CoinsListNewInner from a dict
coins_list_new_inner_from_dict = CoinsListNewInner.from_dict(coins_list_new_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


