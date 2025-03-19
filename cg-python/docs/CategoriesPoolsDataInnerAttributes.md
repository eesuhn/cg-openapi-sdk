# CategoriesPoolsDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_token_price_usd** | **str** |  | [optional] 
**base_token_price_native_currency** | **str** |  | [optional] 
**quote_token_price_usd** | **str** |  | [optional] 
**quote_token_price_native_currency** | **str** |  | [optional] 
**base_token_price_quote_token** | **str** |  | [optional] 
**quote_token_price_base_token** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**pool_created_at** | **datetime** |  | [optional] 
**fdv_usd** | **str** |  | [optional] 
**market_cap_usd** | **str** |  | [optional] 
**price_change_percentage** | [**PoolDataInnerAttributesPriceChangePercentage**](PoolDataInnerAttributesPriceChangePercentage.md) |  | [optional] 
**reserve_in_usd** | **str** |  | [optional] 
**h24_volume_usd** | **str** |  | [optional] 
**h24_tx_count** | **int** |  | [optional] 

## Example

```python
from coingecko_python.models.categories_pools_data_inner_attributes import CategoriesPoolsDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesPoolsDataInnerAttributes from a JSON string
categories_pools_data_inner_attributes_instance = CategoriesPoolsDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(CategoriesPoolsDataInnerAttributes.to_json())

# convert the object into a dict
categories_pools_data_inner_attributes_dict = categories_pools_data_inner_attributes_instance.to_dict()
# create an instance of CategoriesPoolsDataInnerAttributes from a dict
categories_pools_data_inner_attributes_from_dict = CategoriesPoolsDataInnerAttributes.from_dict(categories_pools_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


