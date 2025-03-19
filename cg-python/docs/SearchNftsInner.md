# SearchNftsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NFT collection ID | [optional] 
**name** | **str** | NFT name | [optional] 
**symbol** | **str** | NFT collection symbol | [optional] 
**thumb** | **str** | NFT collection thumb image url | [optional] 

## Example

```python
from coingecko_python.models.search_nfts_inner import SearchNftsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchNftsInner from a JSON string
search_nfts_inner_instance = SearchNftsInner.from_json(json)
# print the JSON string representation of the object
print(SearchNftsInner.to_json())

# convert the object into a dict
search_nfts_inner_dict = search_nfts_inner_instance.to_dict()
# create an instance of SearchNftsInner from a dict
search_nfts_inner_from_dict = SearchNftsInner.from_dict(search_nfts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


