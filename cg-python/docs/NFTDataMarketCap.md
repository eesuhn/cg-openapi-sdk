# NFTDataMarketCap

NFT collection market cap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.nft_data_market_cap import NFTDataMarketCap

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataMarketCap from a JSON string
nft_data_market_cap_instance = NFTDataMarketCap.from_json(json)
# print the JSON string representation of the object
print(NFTDataMarketCap.to_json())

# convert the object into a dict
nft_data_market_cap_dict = nft_data_market_cap_instance.to_dict()
# create an instance of NFTDataMarketCap from a dict
nft_data_market_cap_from_dict = NFTDataMarketCap.from_dict(nft_data_market_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


