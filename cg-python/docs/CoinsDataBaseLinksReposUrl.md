# CoinsDataBaseLinksReposUrl

coin repository url

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github** | **List[str]** | coin github repository url | [optional] 
**bitbucket** | **List[str]** | coin bitbucket repository url | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_links_repos_url import CoinsDataBaseLinksReposUrl

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseLinksReposUrl from a JSON string
coins_data_base_links_repos_url_instance = CoinsDataBaseLinksReposUrl.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseLinksReposUrl.to_json())

# convert the object into a dict
coins_data_base_links_repos_url_dict = coins_data_base_links_repos_url_instance.to_dict()
# create an instance of CoinsDataBaseLinksReposUrl from a dict
coins_data_base_links_repos_url_from_dict = CoinsDataBaseLinksReposUrl.from_dict(coins_data_base_links_repos_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


