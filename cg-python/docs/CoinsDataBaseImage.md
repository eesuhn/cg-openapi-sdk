# CoinsDataBaseImage

coin image url

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumb** | **str** |  | [optional] 
**small** | **str** |  | [optional] 
**large** | **str** |  | [optional] 

## Example

```python
from coingecko_sdk.models.coins_data_base_image import CoinsDataBaseImage

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseImage from a JSON string
coins_data_base_image_instance = CoinsDataBaseImage.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseImage.to_json())

# convert the object into a dict
coins_data_base_image_dict = coins_data_base_image_instance.to_dict()
# create an instance of CoinsDataBaseImage from a dict
coins_data_base_image_from_dict = CoinsDataBaseImage.from_dict(coins_data_base_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


