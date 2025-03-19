# TradesDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_number** | **int** |  | [optional] 
**tx_hash** | **str** |  | [optional] 
**tx_from_address** | **str** |  | [optional] 
**from_token_amount** | **str** |  | [optional] 
**to_token_amount** | **str** |  | [optional] 
**price_from_in_currency_token** | **str** |  | [optional] 
**price_to_in_currency_token** | **str** |  | [optional] 
**price_from_in_usd** | **str** |  | [optional] 
**price_to_in_usd** | **str** |  | [optional] 
**block_timestamp** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**volume_in_usd** | **str** |  | [optional] 
**from_token_address** | **str** |  | [optional] 
**to_token_address** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.trades_data_inner_attributes import TradesDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TradesDataInnerAttributes from a JSON string
trades_data_inner_attributes_instance = TradesDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(TradesDataInnerAttributes.to_json())

# convert the object into a dict
trades_data_inner_attributes_dict = trades_data_inner_attributes_instance.to_dict()
# create an instance of TradesDataInnerAttributes from a dict
trades_data_inner_attributes_from_dict = TradesDataInnerAttributes.from_dict(trades_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


