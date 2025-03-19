# CoinsHistoricalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**localization** | **Dict[str, str]** | coin localization | [optional] 
**image** | [**CoinsHistoricalDataImage**](CoinsHistoricalDataImage.md) |  | [optional] 
**market_data** | [**CoinsHistoricalDataMarketData**](CoinsHistoricalDataMarketData.md) |  | [optional] 
**community_data** | [**CoinsHistoricalDataCommunityData**](CoinsHistoricalDataCommunityData.md) |  | [optional] 
**developer_data** | [**CoinsHistoricalDataDeveloperData**](CoinsHistoricalDataDeveloperData.md) |  | [optional] 
**public_interest_stats** | [**CoinsHistoricalDataPublicInterestStats**](CoinsHistoricalDataPublicInterestStats.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.coins_historical_data import CoinsHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalData from a JSON string
coins_historical_data_instance = CoinsHistoricalData.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalData.to_json())

# convert the object into a dict
coins_historical_data_dict = coins_historical_data_instance.to_dict()
# create an instance of CoinsHistoricalData from a dict
coins_historical_data_from_dict = CoinsHistoricalData.from_dict(coins_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


