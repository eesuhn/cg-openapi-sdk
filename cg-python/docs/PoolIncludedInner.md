# PoolIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PoolIncludedInnerAttributes**](PoolIncludedInnerAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_included_inner import PoolIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PoolIncludedInner from a JSON string
pool_included_inner_instance = PoolIncludedInner.from_json(json)
# print the JSON string representation of the object
print(PoolIncludedInner.to_json())

# convert the object into a dict
pool_included_inner_dict = pool_included_inner_instance.to_dict()
# create an instance of PoolIncludedInner from a dict
pool_included_inner_from_dict = PoolIncludedInner.from_dict(pool_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


