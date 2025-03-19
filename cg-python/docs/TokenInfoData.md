# TokenInfoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**TokenInfoDataAttributes**](TokenInfoDataAttributes.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.token_info_data import TokenInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoData from a JSON string
token_info_data_instance = TokenInfoData.from_json(json)
# print the JSON string representation of the object
print(TokenInfoData.to_json())

# convert the object into a dict
token_info_data_dict = token_info_data_instance.to_dict()
# create an instance of TokenInfoData from a dict
token_info_data_from_dict = TokenInfoData.from_dict(token_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


