# NFTTickersTickersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor_price_in_native_currency** | **float** | NFT collection floor price in native currency | [optional] 
**h24_volume_in_native_currency** | **float** | NFT collection volume in 24 hours in native currency | [optional] 
**native_currency** | **str** | NFT collection native currency | [optional] 
**native_currency_symbol** | **str** | NFT collection native currency symbol | [optional] 
**updated_at** | **str** | last updated time | [optional] 
**nft_marketplace_id** | **str** | NFT marketplace ID | [optional] 
**name** | **str** | NFT marketplace name | [optional] 
**image** | **str** | NFT marketplace image url | [optional] 
**nft_collection_url** | **str** | NFT collection url in the NFT marketplace | [optional] 

## Example

```python
from coingecko-sdk.models.nft_tickers_tickers_inner import NFTTickersTickersInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFTTickersTickersInner from a JSON string
nft_tickers_tickers_inner_instance = NFTTickersTickersInner.from_json(json)
# print the JSON string representation of the object
print(NFTTickersTickersInner.to_json())

# convert the object into a dict
nft_tickers_tickers_inner_dict = nft_tickers_tickers_inner_instance.to_dict()
# create an instance of NFTTickersTickersInner from a dict
nft_tickers_tickers_inner_from_dict = NFTTickersTickersInner.from_dict(nft_tickers_tickers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


