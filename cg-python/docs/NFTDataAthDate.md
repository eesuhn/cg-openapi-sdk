# NFTDataAthDate

NFT collection all time highs date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency** | **datetime** |  | [optional] 
**usd** | **datetime** |  | [optional] 

## Example

```python
from coingecko_python.models.nft_data_ath_date import NFTDataAthDate

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataAthDate from a JSON string
nft_data_ath_date_instance = NFTDataAthDate.from_json(json)
# print the JSON string representation of the object
print(NFTDataAthDate.to_json())

# convert the object into a dict
nft_data_ath_date_dict = nft_data_ath_date_instance.to_dict()
# create an instance of NFTDataAthDate from a dict
nft_data_ath_date_from_dict = NFTDataAthDate.from_dict(nft_data_ath_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


