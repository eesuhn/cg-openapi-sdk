# TrendingSearchNftsInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor_price** | **str** | NFT collection floor price | [optional] 
**floor_price_in_usd_24h_percentage_change** | **str** | NFT collection floor price in usd 24 hours percentage change | [optional] 
**h24_volume** | **str** | NFT collection volume in 24 hours | [optional] 
**h24_average_sale_price** | **str** | NFT collection 24 hours average sale price | [optional] 
**sparkline** | **str** | NFT collection sparkline image url | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from coingecko_python.models.trending_search_nfts_inner_data import TrendingSearchNftsInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchNftsInnerData from a JSON string
trending_search_nfts_inner_data_instance = TrendingSearchNftsInnerData.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchNftsInnerData.to_json())

# convert the object into a dict
trending_search_nfts_inner_data_dict = trending_search_nfts_inner_data_instance.to_dict()
# create an instance of TrendingSearchNftsInnerData from a dict
trending_search_nfts_inner_data_from_dict = TrendingSearchNftsInnerData.from_dict(trending_search_nfts_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


