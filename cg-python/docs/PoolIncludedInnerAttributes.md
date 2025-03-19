# PoolIncludedInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**decimals** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**coingecko_coin_id** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.pool_included_inner_attributes import PoolIncludedInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PoolIncludedInnerAttributes from a JSON string
pool_included_inner_attributes_instance = PoolIncludedInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(PoolIncludedInnerAttributes.to_json())

# convert the object into a dict
pool_included_inner_attributes_dict = pool_included_inner_attributes_instance.to_dict()
# create an instance of PoolIncludedInnerAttributes from a dict
pool_included_inner_attributes_from_dict = PoolIncludedInnerAttributes.from_dict(pool_included_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


