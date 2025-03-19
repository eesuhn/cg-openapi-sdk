# CoinsDataBaseLinks

links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homepage** | **List[str]** | coin website url | [optional] 
**whitepaper** | **List[str]** | coin whitepaper url | [optional] 
**blockchain_site** | **List[str]** | coin block explorer url | [optional] 
**official_forum_url** | **List[str]** | coin official forum url | [optional] 
**chat_url** | **List[str]** | coin chat url | [optional] 
**announcement_url** | **List[str]** | coin announcement url | [optional] 
**snapshot_url** | **str** | coin snapshot url | [optional] 
**twitter_screen_name** | **str** | coin twitter handle | [optional] 
**facebook_username** | **str** | coin facebook username | [optional] 
**bitcointalk_thread_identifier** | **str** | coin bitcointalk thread identifier | [optional] 
**telegram_channel_identifier** | **str** | coin telegram channel identifier | [optional] 
**subreddit_url** | **str** | coin subreddit url | [optional] 
**repos_url** | [**CoinsDataBaseLinksReposUrl**](CoinsDataBaseLinksReposUrl.md) |  | [optional] 

## Example

```python
from coingecko_python.models.coins_data_base_links import CoinsDataBaseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseLinks from a JSON string
coins_data_base_links_instance = CoinsDataBaseLinks.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseLinks.to_json())

# convert the object into a dict
coins_data_base_links_dict = coins_data_base_links_instance.to_dict()
# create an instance of CoinsDataBaseLinks from a dict
coins_data_base_links_from_dict = CoinsDataBaseLinks.from_dict(coins_data_base_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


