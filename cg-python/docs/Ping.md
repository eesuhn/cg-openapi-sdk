# Ping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gecko_says** | **str** |  | [optional] 

## Example

```python
from coingecko-sdk.models.ping import Ping

# TODO update the JSON string below
json = "{}"
# create an instance of Ping from a JSON string
ping_instance = Ping.from_json(json)
# print the JSON string representation of the object
print(Ping.to_json())

# convert the object into a dict
ping_dict = ping_instance.to_dict()
# create an instance of Ping from a dict
ping_from_dict = Ping.from_dict(ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


