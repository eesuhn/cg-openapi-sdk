# NFTDataAthChangePercentage

NFT collection all time highs change percentage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **float** |  | [optional] 
**usd** | **float** |  | [optional] 

## Example

```python
from coingecko_python.models.nft_data_ath_change_percentage import NFTDataAthChangePercentage

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataAthChangePercentage from a JSON string
nft_data_ath_change_percentage_instance = NFTDataAthChangePercentage.from_json(json)
# print the JSON string representation of the object
print(NFTDataAthChangePercentage.to_json())

# convert the object into a dict
nft_data_ath_change_percentage_dict = nft_data_ath_change_percentage_instance.to_dict()
# create an instance of NFTDataAthChangePercentage from a dict
nft_data_ath_change_percentage_from_dict = NFTDataAthChangePercentage.from_dict(nft_data_ath_change_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


