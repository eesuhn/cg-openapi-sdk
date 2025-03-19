# AssetPlatformsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | asset platform ID | [optional] 
**chain_identifier** | **float** | chainlist&#39;s chain ID | [optional] 
**name** | **str** | chain name | [optional] 
**shortname** | **str** | chain shortname | [optional] 
**native_coin_id** | **str** | chain native coin ID | [optional] 
**image** | [**AssetPlatformsInnerImage**](AssetPlatformsInnerImage.md) |  | [optional] 

## Example

```python
from coingecko_python.models.asset_platforms_inner import AssetPlatformsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPlatformsInner from a JSON string
asset_platforms_inner_instance = AssetPlatformsInner.from_json(json)
# print the JSON string representation of the object
print(AssetPlatformsInner.to_json())

# convert the object into a dict
asset_platforms_inner_dict = asset_platforms_inner_instance.to_dict()
# create an instance of AssetPlatformsInner from a dict
asset_platforms_inner_from_dict = AssetPlatformsInner.from_dict(asset_platforms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


