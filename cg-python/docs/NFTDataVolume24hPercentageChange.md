# NFTDataVolume24hPercentageChange

NFT collection volume in 24 hours percentage change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usd** | **float** |  | [optional] 
**native_currency** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.nft_data_volume24h_percentage_change import NFTDataVolume24hPercentageChange

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataVolume24hPercentageChange from a JSON string
nft_data_volume24h_percentage_change_instance = NFTDataVolume24hPercentageChange.from_json(json)
# print the JSON string representation of the object
print(NFTDataVolume24hPercentageChange.to_json())

# convert the object into a dict
nft_data_volume24h_percentage_change_dict = nft_data_volume24h_percentage_change_instance.to_dict()
# create an instance of NFTDataVolume24hPercentageChange from a dict
nft_data_volume24h_percentage_change_from_dict = NFTDataVolume24hPercentageChange.from_dict(nft_data_volume24h_percentage_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


