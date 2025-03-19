# TokenInfoDataAttributesHolders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**distribution_percentage** | [**TokenInfoDataAttributesHoldersDistributionPercentage**](TokenInfoDataAttributesHoldersDistributionPercentage.md) |  | [optional] 
**last_updated** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_info_data_attributes_holders import TokenInfoDataAttributesHolders

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoDataAttributesHolders from a JSON string
token_info_data_attributes_holders_instance = TokenInfoDataAttributesHolders.from_json(json)
# print the JSON string representation of the object
print(TokenInfoDataAttributesHolders.to_json())

# convert the object into a dict
token_info_data_attributes_holders_dict = token_info_data_attributes_holders_instance.to_dict()
# create an instance of TokenInfoDataAttributesHolders from a dict
token_info_data_attributes_holders_from_dict = TokenInfoDataAttributesHolders.from_dict(token_info_data_attributes_holders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


