# TrendingSearchCategoriesInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_cap** | **float** | category market cap | [optional] 
**market_cap_btc** | **float** | category market cap in btc | [optional] 
**total_volume** | **float** | category total volume | [optional] 
**total_volume_btc** | **float** | category total volume in btc | [optional] 
**market_cap_change_percentage_24h** | [**TrendingSearchCategoriesInnerDataMarketCapChangePercentage24h**](TrendingSearchCategoriesInnerDataMarketCapChangePercentage24h.md) |  | [optional] 
**sparkline** | **str** | category sparkline image url | [optional] 

## Example

```python
from coingecko_python.models.trending_search_categories_inner_data import TrendingSearchCategoriesInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingSearchCategoriesInnerData from a JSON string
trending_search_categories_inner_data_instance = TrendingSearchCategoriesInnerData.from_json(json)
# print the JSON string representation of the object
print(TrendingSearchCategoriesInnerData.to_json())

# convert the object into a dict
trending_search_categories_inner_data_dict = trending_search_categories_inner_data_instance.to_dict()
# create an instance of TrendingSearchCategoriesInnerData from a dict
trending_search_categories_inner_data_from_dict = TrendingSearchCategoriesInnerData.from_dict(trending_search_categories_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


