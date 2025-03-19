# CoinsDataBaseCommunityData

coin community data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facebook_likes** | **float** | coin facebook likes | [optional] 
**twitter_followers** | **float** | coin twitter followers | [optional] 
**reddit_average_posts_48h** | **float** | coin reddit average posts in 48 hours | [optional] 
**reddit_average_comments_48h** | **float** | coin reddit average comments in 48 hours | [optional] 
**reddit_subscribers** | **float** | coin reddit subscribers | [optional] 
**reddit_accounts_active_48h** | **float** | coin reddit active accounts in 48 hours | [optional] 
**telegram_channel_user_count** | **float** | coin telegram channel user count | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_community_data import CoinsDataBaseCommunityData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseCommunityData from a JSON string
coins_data_base_community_data_instance = CoinsDataBaseCommunityData.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseCommunityData.to_json())

# convert the object into a dict
coins_data_base_community_data_dict = coins_data_base_community_data_instance.to_dict()
# create an instance of CoinsDataBaseCommunityData from a dict
coins_data_base_community_data_from_dict = CoinsDataBaseCommunityData.from_dict(coins_data_base_community_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


