# TrendingSearchNftsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NFT collection ID | [optional] 
**name** | **str** | NFT collection name | [optional] 
**symbol** | **str** | NFT collection symbol | [optional] 
**thumb** | **str** | NFT collection thumb image url | [optional] 
**nft_contract_id** | **float** |  | [optional] 
**native_currency_symbol** | **str** | NFT collection native currency symbol | [optional] 
**floor_price_in_native_currency** | **float** | NFT collection floor price in native currency | [optional] 
**floor_price_24h_percentage_change** | **float** | NFT collection floor price 24 hours percentage change | [optional] 
**data** | [**TrendingSearchNftsInnerData**](TrendingSearchNftsInnerData.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.trending_search_nfts_inner import TrendingSearchNftsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchNftsInner from a JSON string
trending_search_nfts_inner_instance = TrendingSearchNftsInner.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchNftsInner.to_json())

# convert the object into a dict
trending_search_nfts_inner_dict = trending_search_nfts_inner_instance.to_dict()
# create an instance of TrendingSearchNftsInner from a dict
trending_search_nfts_inner_from_dict = TrendingSearchNftsInner.from_dict(trending_search_nfts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


