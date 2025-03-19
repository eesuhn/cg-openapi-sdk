# TokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TokenInfoData**](TokenInfoData.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.token_info import TokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfo from a JSON string
token_info_instance = TokenInfo.from_json(json)
# print the JSON string representation of the object
print(TokenInfo.to_json())

# convert the object into a dict
token_info_dict = token_info_instance.to_dict()
# create an instance of TokenInfo from a dict
token_info_from_dict = TokenInfo.from_dict(token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


