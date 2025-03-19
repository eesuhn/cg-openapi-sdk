# NFTList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NFT collection ID | [optional] 
**contract_address** | **str** | NFT collection contract address | [optional] 
**name** | **str** | NFT collection name | [optional] 
**asset_platform_id** | **str** | NFT collection asset platform ID | [optional] 
**symbol** | **str** | NFT collection symbol | [optional] 

## Example

```python
from coingecko-sdk.models.nft_list import NFTList

# TODO update the JSON string below
json = "{}"
# create an instance of NFTList from a JSON string
nft_list_instance = NFTList.from_json(json)
# print the JSON string representation of the object
print(NFTList.to_json())

# convert the object into a dict
nft_list_dict = nft_list_instance.to_dict()
# create an instance of NFTList from a dict
nft_list_from_dict = NFTList.from_dict(nft_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


