# NFTDataImage

NFT collection image url

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**small** | **str** |  | [optional] 
**small_2x** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.nft_data_image import NFTDataImage

# TODO update the JSON string below
json = "{}"
# create an instance of NFTDataImage from a JSON string
nft_data_image_instance = NFTDataImage.from_json(json)
# print the JSON string representation of the object
print(NFTDataImage.to_json())

# convert the object into a dict
nft_data_image_dict = nft_data_image_instance.to_dict()
# create an instance of NFTDataImage from a dict
nft_data_image_from_dict = NFTDataImage.from_dict(nft_data_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


