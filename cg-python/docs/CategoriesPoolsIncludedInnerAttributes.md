# CategoriesPoolsIncludedInnerAttributes


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
from coingecko-sdk.models.categories_pools_included_inner_attributes import CategoriesPoolsIncludedInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPoolsIncludedInnerAttributes from a JSON string
categories_pools_included_inner_attributes_instance = CategoriesPoolsIncludedInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(CategoriesPoolsIncludedInnerAttributes.to_json())

# convert the object into a dict
categories_pools_included_inner_attributes_dict = categories_pools_included_inner_attributes_instance.to_dict()
# create an instance of CategoriesPoolsIncludedInnerAttributes from a dict
categories_pools_included_inner_attributes_from_dict = CategoriesPoolsIncludedInnerAttributes.from_dict(categories_pools_included_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


