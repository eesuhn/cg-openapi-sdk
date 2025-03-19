# CoinsContractAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | coin ID | [optional] 
**symbol** | **str** | coin symbol | [optional] 
**name** | **str** | coin name | [optional] 
**web_slug** | **str** | coin web slug | [optional] 
**asset_platform_id** | **str** | coin asset platform ID | [optional] 
**platforms** | **Dict[str, str]** | coin asset platform and contract address | [optional] 
**detail_platforms** | **Dict[str, str]** | detailed coin asset platform and contract address | [optional] 
**block_time_in_minutes** | **float** | blockchain block time in minutes | [optional] 
**hashing_algorithm** | **str** | blockchain hashing algorithm | [optional] 
**categories** | **List[str]** | coin categories | [optional] 
**preview_listing** | **bool** | preview listing coin | [optional] 
**public_notice** | **str** | public notice | [optional] 
**additional_notices** | **List[str]** | additional notices | [optional] 
**localization** | **Dict[str, str]** | coin name localization | [optional] 
**description** | **Dict[str, str]** | coin description | [optional] 
**links** | [**CoinsDataBaseLinks**](CoinsDataBaseLinks.md) |  | [optional] 
**image** | [**CoinsDataBaseImage**](CoinsDataBaseImage.md) |  | [optional] 
**country_origin** | **str** | coin country of origin | [optional] 
**genesis_date** | **datetime** | coin genesis date | [optional] 
**sentiment_votes_up_percentage** | **float** | coin sentiment votes up percentage | [optional] 
**sentiment_votes_down_percentage** | **float** | coin sentiment votes down percentage | [optional] 
**market_cap_rank** | **float** | coin rank by market cap | [optional] 
**market_data** | [**CoinsDataBaseMarketData**](CoinsDataBaseMarketData.md) |  | [optional] 
**community_data** | [**CoinsDataBaseCommunityData**](CoinsDataBaseCommunityData.md) |  | [optional] 
**developer_data** | [**CoinsDataBaseDeveloperData**](CoinsDataBaseDeveloperData.md) |  | [optional] 
**status_updates** | **List[object]** | coin status updates | [optional] 
**last_updated** | **datetime** | coin last updated timestamp | [optional] 
**tickers** | [**List[CoinsDataBaseTickersInner]**](CoinsDataBaseTickersInner.md) | coin tickers | [optional] 

## Example

```python
from coingecko-sdk.models.coins_contract_address import CoinsContractAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsContractAddress from a JSON string
coins_contract_address_instance = CoinsContractAddress.from_json(json)
# print the JSON string representation of the object
print(CoinsContractAddress.to_json())

# convert the object into a dict
coins_contract_address_dict = coins_contract_address_instance.to_dict()
# create an instance of CoinsContractAddress from a dict
coins_contract_address_from_dict = CoinsContractAddress.from_dict(coins_contract_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


