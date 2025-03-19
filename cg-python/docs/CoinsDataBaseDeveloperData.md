# CoinsDataBaseDeveloperData

coin developer data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forks** | **float** | coin repository forks | [optional] 
**stars** | **float** | coin repository stars | [optional] 
**subscribers** | **float** | coin repository subscribers | [optional] 
**total_issues** | **float** | coin repository total issues | [optional] 
**closed_issues** | **float** | coin repository closed issues | [optional] 
**pull_requests_merged** | **float** | coin repository pull requests merged | [optional] 
**pull_request_contributors** | **float** | coin repository pull request contributors | [optional] 
**code_additions_deletions_4_weeks** | [**CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks**](CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks.md) |  | [optional] 
**commit_count_4_weeks** | **float** | coin repository commit count in 4 weeks | [optional] 
**last_4_weeks_commit_activity_series** | **List[float]** | coin repository last 4 weeks commit activity series | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_developer_data import CoinsDataBaseDeveloperData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseDeveloperData from a JSON string
coins_data_base_developer_data_instance = CoinsDataBaseDeveloperData.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseDeveloperData.to_json())

# convert the object into a dict
coins_data_base_developer_data_dict = coins_data_base_developer_data_instance.to_dict()
# create an instance of CoinsDataBaseDeveloperData from a dict
coins_data_base_developer_data_from_dict = CoinsDataBaseDeveloperData.from_dict(coins_data_base_developer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


