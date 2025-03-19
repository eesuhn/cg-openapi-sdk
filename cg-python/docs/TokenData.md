# TokenData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**TokenDataAttributes**](TokenDataAttributes.md) |  | [optional] 
**relationships** | [**TokenDataRelationships**](TokenDataRelationships.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_data import TokenData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenData from a JSON string
token_data_instance = TokenData.from_json(json)
# print the JSON string representation of the object
print(TokenData.to_json())

# convert the object into a dict
token_data_dict = token_data_instance.to_dict()
# create an instance of TokenData from a dict
token_data_from_dict = TokenData.from_dict(token_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


