# CoinsListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**platforms** | **Dict[str, str]** | coin asset platform and contract address | [optional] 

## Example

```python
from coingecko_sdk.models.coins_list_inner import CoinsListInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsListInner from a JSON string
coins_list_inner_instance = CoinsListInner.from_json(json)
# print the JSON string representation of the object
print(CoinsListInner.to_json())

# convert the object into a dict
coins_list_inner_dict = coins_list_inner_instance.to_dict()
# create an instance of CoinsListInner from a dict
coins_list_inner_from_dict = CoinsListInner.from_dict(coins_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


