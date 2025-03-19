# TokenIncludedInnerAttributes


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
**token_price_usd** | **str** |  | [optional] 
**fdv_usd** | **str** |  | [optional] 
**market_cap_usd** | **str** |  | [optional] 
**price_change_percentage** | [**PoolDataInnerAttributesPriceChangePercentage**](PoolDataInnerAttributesPriceChangePercentage.md) |  | [optional] 
**transactions** | [**PoolDataInnerAttributesTransactions**](PoolDataInnerAttributesTransactions.md) |  | [optional] 
**volume_usd** | [**PoolDataInnerAttributesPriceChangePercentage**](PoolDataInnerAttributesPriceChangePercentage.md) |  | [optional] 
**reserve_in_usd** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_included_inner_attributes import TokenIncludedInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIncludedInnerAttributes from a JSON string
token_included_inner_attributes_instance = TokenIncludedInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(TokenIncludedInnerAttributes.to_json())

# convert the object into a dict
token_included_inner_attributes_dict = token_included_inner_attributes_instance.to_dict()
# create an instance of TokenIncludedInnerAttributes from a dict
token_included_inner_attributes_from_dict = TokenIncludedInnerAttributes.from_dict(token_included_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


