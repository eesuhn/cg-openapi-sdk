# CoinsHistoricalDataCommunityData

coin community data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facebook_likes** | **float** | coin facebook likes | [optional] 
**twitter_followers** | **float** | coin twitter followers | [optional] 
**reddit_average_posts_48h** | **float** | coin reddit average posts 48h | [optional] 
**reddit_average_comments_48h** | **float** | coin reddit average comments 48h | [optional] 
**reddit_subscribers** | **float** | coin reddit subscribers | [optional] 
**reddit_accounts_active_48h** | **float** | coin reddit accounts active 48h | [optional] 

## Example

```python
from coingecko_python.models.coins_historical_data_community_data import CoinsHistoricalDataCommunityData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataCommunityData from a JSON string
coins_historical_data_community_data_instance = CoinsHistoricalDataCommunityData.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataCommunityData.to_json())

# convert the object into a dict
coins_historical_data_community_data_dict = coins_historical_data_community_data_instance.to_dict()
# create an instance of CoinsHistoricalDataCommunityData from a dict
coins_historical_data_community_data_from_dict = CoinsHistoricalDataCommunityData.from_dict(coins_historical_data_community_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


