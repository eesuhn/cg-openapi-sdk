# NFTDataAth

NFT collection all time highs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko-sdk.models.nft_data_ath import NFTDataAth

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataAth from a JSON string
nft_data_ath_instance = NFTDataAth.from_json(json)
# print the JSON string representation of the object
print(NFTDataAth.to_json())

# convert the object into a dict
nft_data_ath_dict = nft_data_ath_instance.to_dict()
# create an instance of NFTDataAth from a dict
nft_data_ath_from_dict = NFTDataAth.from_dict(nft_data_ath_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


