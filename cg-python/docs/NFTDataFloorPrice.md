# NFTDataFloorPrice

NFT collection floor price

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.nft_data_floor_price import NFTDataFloorPrice

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataFloorPrice from a JSON string
nft_data_floor_price_instance = NFTDataFloorPrice.from_json(json)
# print the JSON string representation of the object
print(NFTDataFloorPrice.to_json())

# convert the object into a dict
nft_data_floor_price_dict = nft_data_floor_price_instance.to_dict()
# create an instance of NFTDataFloorPrice from a dict
nft_data_floor_price_from_dict = NFTDataFloorPrice.from_dict(nft_data_floor_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


