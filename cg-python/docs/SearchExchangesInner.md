# SearchExchangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | exchange ID | [optional] 
**name** | **str** | exchange name | [optional] 
**market_type** | **str** | exchange market type | [optional] 
**thumb** | **str** | exchange thumb image url | [optional] 
**large** | **str** | exchange large image url | [optional] 

## Example

```python
from coingecko_sdk.models.search_exchanges_inner import SearchExchangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExchangesInner from a JSON string
search_exchanges_inner_instance = SearchExchangesInner.from_json(json)
# print the JSON string representation of the object
print(SearchExchangesInner.to_json())

# convert the object into a dict
search_exchanges_inner_dict = search_exchanges_inner_instance.to_dict()
# create an instance of SearchExchangesInner from a dict
search_exchanges_inner_from_dict = SearchExchangesInner.from_dict(search_exchanges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


