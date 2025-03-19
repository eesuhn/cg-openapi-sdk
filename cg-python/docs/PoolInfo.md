# PoolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PoolInfoDataInner]**](PoolInfoDataInner.md) |  | [optional] 
**included** | [**List[PoolIncludedInner]**](PoolIncludedInner.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_info import PoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfo from a JSON string
pool_info_instance = PoolInfo.from_json(json)
# print the JSON string representation of the object
print(PoolInfo.to_json())

# convert the object into a dict
pool_info_dict = pool_info_instance.to_dict()
# create an instance of PoolInfo from a dict
pool_info_from_dict = PoolInfo.from_dict(pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


