# NFTDataVolume24h

NFT collection volume in 24 hours

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.nft_data_volume24h import NFTDataVolume24h

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataVolume24h from a JSON string
nft_data_volume24h_instance = NFTDataVolume24h.from_json(json)
# print the JSON string representation of the object
print(NFTDataVolume24h.to_json())

# convert the object into a dict
nft_data_volume24h_dict = nft_data_volume24h_instance.to_dict()
# create an instance of NFTDataVolume24h from a dict
nft_data_volume24h_from_dict = NFTDataVolume24h.from_dict(nft_data_volume24h_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


