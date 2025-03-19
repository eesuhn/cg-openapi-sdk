# Categories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | category ID | [optional] 
**name** | **str** | category name | [optional] 
**market_cap** | **float** | category market cap | [optional] 
**market_cap_change_24h** | **float** | category market cap change in 24 hours | [optional] 
**content** | **str** | category description | [optional] 
**top_3_coins_id** | **List[str]** | IDs of top 3 coins in the category | [optional] 
**top_3_coins** | **List[str]** | images of top 3 coins in the category | [optional] 
**volume_24h** | **float** | category volume in 24 hours | [optional] 
**updated_at** | **str** | category last updated time | [optional] 

## Example

```python
from coingecko_python.models.categories import Categories

# TODO update the JSON string below
json = "{}"
# create an instance of Categories from a JSON string
categories_instance = Categories.from_json(json)
# print the JSON string representation of the object
print(Categories.to_json())

# convert the object into a dict
categories_dict = categories_instance.to_dict()
# create an instance of Categories from a dict
categories_from_dict = Categories.from_dict(categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


