# CoinsHistoricalDataDeveloperData

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
**code_additions_deletions_4_weeks** | [**CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks**](CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks.md) |  | [optional] 
**commit_count_4_weeks** | **float** | coin commit count 4 weeks | [optional] 

## Example

```python
from coingecko-sdk.models.coins_historical_data_developer_data import CoinsHistoricalDataDeveloperData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataDeveloperData from a JSON string
coins_historical_data_developer_data_instance = CoinsHistoricalDataDeveloperData.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataDeveloperData.to_json())

# convert the object into a dict
coins_historical_data_developer_data_dict = coins_historical_data_developer_data_instance.to_dict()
# create an instance of CoinsHistoricalDataDeveloperData from a dict
coins_historical_data_developer_data_from_dict = CoinsHistoricalDataDeveloperData.from_dict(coins_historical_data_developer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


