# NFTDataLinks

NFT collection links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homepage** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**discord** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.nft_data_links import NFTDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataLinks from a JSON string
nft_data_links_instance = NFTDataLinks.from_json(json)
# print the JSON string representation of the object
print(NFTDataLinks.to_json())

# convert the object into a dict
nft_data_links_dict = nft_data_links_instance.to_dict()
# create an instance of NFTDataLinks from a dict
nft_data_links_from_dict = NFTDataLinks.from_dict(nft_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


