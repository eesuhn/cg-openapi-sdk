# TrendingSearchCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** | category name | [optional] 
**market_cap_1h_change** | **float** | category market cap 1 hour change | [optional] 
**slug** | **str** | category web slug | [optional] 
**coins_count** | **float** | category number of coins | [optional] 
**data** | [**TrendingSearchCategoriesInnerData**](TrendingSearchCategoriesInnerData.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.trending_search_categories_inner import TrendingSearchCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchCategoriesInner from a JSON string
trending_search_categories_inner_instance = TrendingSearchCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchCategoriesInner.to_json())

# convert the object into a dict
trending_search_categories_inner_dict = trending_search_categories_inner_instance.to_dict()
# create an instance of TrendingSearchCategoriesInner from a dict
trending_search_categories_inner_from_dict = TrendingSearchCategoriesInner.from_dict(trending_search_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


