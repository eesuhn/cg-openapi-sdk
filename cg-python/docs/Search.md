# Search


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coins** | [**List[SearchCoinsInner]**](SearchCoinsInner.md) |  | [optional] 
**exchanges** | [**List[SearchExchangesInner]**](SearchExchangesInner.md) |  | [optional] 
**icos** | **List[str]** |  | [optional] 
**categories** | [**List[SearchCategoriesInner]**](SearchCategoriesInner.md) |  | [optional] 
**nfts** | [**List[SearchNftsInner]**](SearchNftsInner.md) |  | [optional] 

## Example

```python
from coingecko_python.models.search import Search

# TODO update the JSON string below
json = "{}"
# create an instance of Search from a JSON string
search_instance = Search.from_json(json)
# print the JSON string representation of the object
print(Search.to_json())

# convert the object into a dict
search_dict = search_instance.to_dict()
# create an instance of Search from a dict
search_from_dict = Search.from_dict(search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


