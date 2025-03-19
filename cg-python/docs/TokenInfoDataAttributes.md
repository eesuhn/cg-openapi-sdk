# TokenInfoDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**coingecko_coin_id** | **str** |  | [optional] 
**websites** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**gt_score** | **float** |  | [optional] 
**discord_url** | **str** |  | [optional] 
**telegram_handle** | **str** |  | [optional] 
**twitter_handle** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**gt_categories_id** | **List[str]** |  | [optional] 
**holders** | [**TokenInfoDataAttributesHolders**](TokenInfoDataAttributesHolders.md) |  | [optional] 

## Example

```python
from coingecko_python.models.token_info_data_attributes import TokenInfoDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoDataAttributes from a JSON string
token_info_data_attributes_instance = TokenInfoDataAttributes.from_json(json)
# print the JSON string representation of the object
print(TokenInfoDataAttributes.to_json())

# convert the object into a dict
token_info_data_attributes_dict = token_info_data_attributes_instance.to_dict()
# create an instance of TokenInfoDataAttributes from a dict
token_info_data_attributes_from_dict = TokenInfoDataAttributes.from_dict(token_info_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


