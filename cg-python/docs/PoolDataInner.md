# PoolDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PoolDataInnerAttributes**](PoolDataInnerAttributes.md) |  | [optional] 
**relationships** | [**PoolDataInnerRelationships**](PoolDataInnerRelationships.md) |  | [optional] 

## Example

```python
from coingecko_python.models.pool_data_inner import PoolDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PoolDataInner from a JSON string
pool_data_inner_instance = PoolDataInner.from_json(json)
# print the JSON string representation of the object
print(PoolDataInner.to_json())

# convert the object into a dict
pool_data_inner_dict = pool_data_inner_instance.to_dict()
# create an instance of PoolDataInner from a dict
pool_data_inner_from_dict = PoolDataInner.from_dict(pool_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


