# PoolInfoDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PoolInfoDataInnerAttributes**](PoolInfoDataInnerAttributes.md) |  | [optional] 
**relationships** | [**PoolDataInnerRelationships**](PoolDataInnerRelationships.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.pool_info_data_inner import PoolInfoDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfoDataInner from a JSON string
pool_info_data_inner_instance = PoolInfoDataInner.from_json(json)
# print the JSON string representation of the object
print(PoolInfoDataInner.to_json())

# convert the object into a dict
pool_info_data_inner_dict = pool_info_data_inner_instance.to_dict()
# create an instance of PoolInfoDataInner from a dict
pool_info_data_inner_from_dict = PoolInfoDataInner.from_dict(pool_info_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


