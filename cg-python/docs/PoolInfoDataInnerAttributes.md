# PoolInfoDataInnerAttributes


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
**pool_created_at** | **str** |  | [optional] 
**fdv_usd** | **str** |  | [optional] 
**market_cap_usd** | **str** |  | [optional] 
**price_change_percentage** | [**PoolDataInnerAttributesPriceChangePercentage**](PoolDataInnerAttributesPriceChangePercentage.md) |  | [optional] 
**transactions** | [**PoolInfoDataInnerAttributesTransactions**](PoolInfoDataInnerAttributesTransactions.md) |  | [optional] 
**volume_usd** | [**PoolInfoDataInnerAttributesVolumeUsd**](PoolInfoDataInnerAttributesVolumeUsd.md) |  | [optional] 
**reserve_in_usd** | **str** |  | [optional] 
**locked_liquidity_percentage** | **str** |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_info_data_inner_attributes import PoolInfoDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfoDataInnerAttributes from a JSON string
pool_info_data_inner_attributes_instance = PoolInfoDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(PoolInfoDataInnerAttributes.to_json())

# convert the object into a dict
pool_info_data_inner_attributes_dict = pool_info_data_inner_attributes_instance.to_dict()
# create an instance of PoolInfoDataInnerAttributes from a dict
pool_info_data_inner_attributes_from_dict = PoolInfoDataInnerAttributes.from_dict(pool_info_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


