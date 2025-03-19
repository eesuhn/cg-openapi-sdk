# TokenDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**coingecko_coin_id** | **str** |  | [optional] 
**decimals** | **int** |  | [optional] 
**total_supply** | **str** |  | [optional] 
**price_usd** | **str** |  | [optional] 
**fdv_usd** | **str** |  | [optional] 
**total_reserve_in_usd** | **str** |  | [optional] 
**volume_usd** | [**TokenDataAttributesVolumeUsd**](TokenDataAttributesVolumeUsd.md) |  | [optional] 
**market_cap_usd** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_data_attributes import TokenDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDataAttributes from a JSON string
token_data_attributes_instance = TokenDataAttributes.from_json(json)
# print the JSON string representation of the object
print(TokenDataAttributes.to_json())

# convert the object into a dict
token_data_attributes_dict = token_data_attributes_instance.to_dict()
# create an instance of TokenDataAttributes from a dict
token_data_attributes_from_dict = TokenDataAttributes.from_dict(token_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


