# NFTMarketChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor_price_usd** | **List[List[float]]** | NFT collection floor price in usd | [optional] 
**floor_price_native** | **List[List[float]]** | NFT collection floor price in native currency | [optional] 
**h24_volume_usd** | **List[List[float]]** | NFT collection volume in 24 hours in usd | [optional] 
**h24_volume_native** | **List[List[float]]** | NFT collection volume in 24 hours in native currency | [optional] 
**market_cap_usd** | **List[List[float]]** | NFT collection market cap in usd | [optional] 
**market_cap_native** | **List[List[float]]** | NFT collection market cap in native currency | [optional] 

## Example

```python
from coingecko-sdk.models.nft_market_chart import NFTMarketChart

# TODO update the JSON string below
json = "{}"
# create an instance of NFTMarketChart from a JSON string
nft_market_chart_instance = NFTMarketChart.from_json(json)
# print the JSON string representation of the object
print(NFTMarketChart.to_json())

# convert the object into a dict
nft_market_chart_dict = nft_market_chart_instance.to_dict()
# create an instance of NFTMarketChart from a dict
nft_market_chart_from_dict = NFTMarketChart.from_dict(nft_market_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


