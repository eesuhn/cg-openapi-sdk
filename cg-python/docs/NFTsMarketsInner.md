# NFTsMarketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NFT collection ID | [optional] 
**contract_address** | **str** | NFT collection contract address | [optional] 
**asset_platform_id** | **str** | NFT collection asset platform ID | [optional] 
**name** | **str** | NFT collection name | [optional] 
**symbol** | **str** | NFT collection symbol | [optional] 
**image** | [**NFTDataImage**](NFTDataImage.md) |  | [optional] 
**description** | **str** | NFT collection description | [optional] 
**native_currency** | **str** | NFT collection native currency | [optional] 
**native_currency_symbol** | **str** | NFT collection native currency symbol | [optional] 
**market_cap_rank** | **float** | coin market cap rank | [optional] 
**floor_price** | [**NFTDataFloorPrice**](NFTDataFloorPrice.md) |  | [optional] 
**market_cap** | [**NFTDataMarketCap**](NFTDataMarketCap.md) |  | [optional] 
**volume_24h** | [**NFTDataVolume24h**](NFTDataVolume24h.md) |  | [optional] 
**floor_price_in_usd_24h_percentage_change** | **float** | NFT collection floor price in usd 24 hours percentage change | [optional] 
**floor_price_24h_percentage_change** | [**NFTsMarketsInnerFloorPrice24hPercentageChange**](NFTsMarketsInnerFloorPrice24hPercentageChange.md) |  | [optional] 
**market_cap_24h_percentage_change** | [**NFTDataMarketCap24hPercentageChange**](NFTDataMarketCap24hPercentageChange.md) |  | [optional] 
**volume_24h_percentage_change** | [**NFTDataVolume24hPercentageChange**](NFTDataVolume24hPercentageChange.md) |  | [optional] 
**number_of_unique_addresses** | **float** | number of unique address owning the NFTs | [optional] 
**number_of_unique_addresses_24h_percentage_change** | **float** | number of unique address owning the NFTs 24 hours percentage change | [optional] 
**volume_in_usd_24h_percentage_change** | **float** | NFT collection volume in usd 24 hours percentage change | [optional] 
**total_supply** | **float** | NFT collection total supply | [optional] 
**one_day_sales** | **float** | NFT collection one day sales | [optional] 
**one_day_sales_24h_percentage_change** | **float** | NFT collection one day sales 24 hours percentage change | [optional] 
**one_day_average_sale_price** | **float** | NFT collection one day average sale price | [optional] 
**one_day_average_sale_price_24h_percentage_change** | **float** | NFT collection one day average sale price 24 hours percentage change | [optional] 

## Example

```python
from coingecko-sdk.models.nfts_markets_inner import NFTsMarketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFTsMarketsInner from a JSON string
nfts_markets_inner_instance = NFTsMarketsInner.from_json(json)
# print the JSON string representation of the object
print(NFTsMarketsInner.to_json())

# convert the object into a dict
nfts_markets_inner_dict = nfts_markets_inner_instance.to_dict()
# create an instance of NFTsMarketsInner from a dict
nfts_markets_inner_from_dict = NFTsMarketsInner.from_dict(nfts_markets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


