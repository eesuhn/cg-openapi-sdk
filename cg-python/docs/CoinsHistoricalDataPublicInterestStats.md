# CoinsHistoricalDataPublicInterestStats

coin public interest stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alexa_rank** | **float** | coin alexa rank | [optional] 
**bing_matches** | **float** | coin bing matches | [optional] 

## Example

```python
from coingecko_sdk.models.coins_historical_data_public_interest_stats import CoinsHistoricalDataPublicInterestStats

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataPublicInterestStats from a JSON string
coins_historical_data_public_interest_stats_instance = CoinsHistoricalDataPublicInterestStats.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataPublicInterestStats.to_json())

# convert the object into a dict
coins_historical_data_public_interest_stats_dict = coins_historical_data_public_interest_stats_instance.to_dict()
# create an instance of CoinsHistoricalDataPublicInterestStats from a dict
coins_historical_data_public_interest_stats_from_dict = CoinsHistoricalDataPublicInterestStats.from_dict(coins_historical_data_public_interest_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


