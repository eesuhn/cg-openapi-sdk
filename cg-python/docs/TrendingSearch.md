# TrendingSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coins** | [**List[TrendingSearchCoinsInner]**](TrendingSearchCoinsInner.md) |  | [optional] 
**nfts** | [**List[TrendingSearchNftsInner]**](TrendingSearchNftsInner.md) |  | [optional] 
**categories** | [**List[TrendingSearchCategoriesInner]**](TrendingSearchCategoriesInner.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.trending_search import TrendingSearch

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearch from a JSON string
trending_search_instance = TrendingSearch.from_json(json)
# print the JSON string representation of the object
print(TrendingSearch.to_json())

# convert the object into a dict
trending_search_dict = trending_search_instance.to_dict()
# create an instance of TrendingSearch from a dict
trending_search_from_dict = TrendingSearch.from_dict(trending_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


