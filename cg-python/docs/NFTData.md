# NFTData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NFT collection ID | [optional] 
**contract_address** | **str** | NFT collection contract address | [optional] 
**asset_platform_id** | **str** | NFT collection asset platform ID | [optional] 
**name** | **str** | NFT collection name | [optional] 
**symbol** | **str** | NFT collection symbol | [optional] 
**image** | [**NFTDataImage**](NFTDataImage.md) |  | [optional] 
**banner_image** | [**NFTDataBannerImage**](NFTDataBannerImage.md) |  | [optional] 
**description** | **str** | NFT collection description | [optional] 
**native_currency** | **str** | NFT collection native currency | [optional] 
**native_currency_symbol** | **str** | NFT collection native currency symbol | [optional] 
**market_cap_rank** | **float** | coin market cap rank | [optional] 
**floor_price** | [**NFTDataFloorPrice**](NFTDataFloorPrice.md) |  | [optional] 
**market_cap** | [**NFTDataMarketCap**](NFTDataMarketCap.md) |  | [optional] 
**volume_24h** | [**NFTDataVolume24h**](NFTDataVolume24h.md) |  | [optional] 
**floor_price_in_usd_24h_percentage_change** | **float** | NFT collection floor price in usd 24 hours percentage change | [optional] 
**floor_price_24h_percentage_change** | [**NFTDataFloorPrice24hPercentageChange**](NFTDataFloorPrice24hPercentageChange.md) |  | [optional] 
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
**links** | [**NFTDataLinks**](NFTDataLinks.md) |  | [optional] 
**floor_price_7d_percentage_change** | [**NFTDataFloorPrice7dPercentageChange**](NFTDataFloorPrice7dPercentageChange.md) |  | [optional] 
**floor_price_14d_percentage_change** | [**NFTDataFloorPrice14dPercentageChange**](NFTDataFloorPrice14dPercentageChange.md) |  | [optional] 
**floor_price_30d_percentage_change** | [**NFTDataFloorPrice30dPercentageChange**](NFTDataFloorPrice30dPercentageChange.md) |  | [optional] 
**floor_price_60d_percentage_change** | [**NFTDataFloorPrice60dPercentageChange**](NFTDataFloorPrice60dPercentageChange.md) |  | [optional] 
**floor_price_1y_percentage_change** | [**NFTDataFloorPrice1yPercentageChange**](NFTDataFloorPrice1yPercentageChange.md) |  | [optional] 
**explorers** | [**List[NFTDataExplorersInner]**](NFTDataExplorersInner.md) | NFT collection block explorers links | [optional] 
**user_favorites_count** | **float** | NFT collection user favorites count | [optional] 
**ath** | [**NFTDataAth**](NFTDataAth.md) |  | [optional] 
**ath_change_percentage** | [**NFTDataAthChangePercentage**](NFTDataAthChangePercentage.md) |  | [optional] 
**ath_date** | [**NFTDataAthDate**](NFTDataAthDate.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.nft_data import NFTData

# TODO update the JSON string below
json = "{}"
# create an instance of NFTData from a JSON string
nft_data_instance = NFTData.from_json(json)
# print the JSON string representation of the object
print(NFTData.to_json())

# convert the object into a dict
nft_data_dict = nft_data_instance.to_dict()
# create an instance of NFTData from a dict
nft_data_from_dict = NFTData.from_dict(nft_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


