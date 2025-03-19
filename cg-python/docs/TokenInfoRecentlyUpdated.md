# TokenInfoRecentlyUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TokenInfoData**](TokenInfoData.md) |  | [optional] 

## Example

```python
from coingecko_sdk.models.token_info_recently_updated import TokenInfoRecentlyUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoRecentlyUpdated from a JSON string
token_info_recently_updated_instance = TokenInfoRecentlyUpdated.from_json(json)
# print the JSON string representation of the object
print(TokenInfoRecentlyUpdated.to_json())

# convert the object into a dict
token_info_recently_updated_dict = token_info_recently_updated_instance.to_dict()
# create an instance of TokenInfoRecentlyUpdated from a dict
token_info_recently_updated_from_dict = TokenInfoRecentlyUpdated.from_dict(token_info_recently_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


