# PoolTokensInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TokenInfoData**](TokenInfoData.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_tokens_info import PoolTokensInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PoolTokensInfo from a JSON string
pool_tokens_info_instance = PoolTokensInfo.from_json(json)
# print the JSON string representation of the object
print(PoolTokensInfo.to_json())

# convert the object into a dict
pool_tokens_info_dict = pool_tokens_info_instance.to_dict()
# create an instance of PoolTokensInfo from a dict
pool_tokens_info_from_dict = PoolTokensInfo.from_dict(pool_tokens_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


