# CoinsHistoricalDataImage

coin image url

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumb** | **str** |  | [optional] 
**small** | **str** |  | [optional] 

## Example

```python
from coingecko_python.models.coins_historical_data_image import CoinsHistoricalDataImage

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsHistoricalDataImage from a JSON string
coins_historical_data_image_instance = CoinsHistoricalDataImage.from_json(json)
# print the JSON string representation of the object
print(CoinsHistoricalDataImage.to_json())

# convert the object into a dict
coins_historical_data_image_dict = coins_historical_data_image_instance.to_dict()
# create an instance of CoinsHistoricalDataImage from a dict
coins_historical_data_image_from_dict = CoinsHistoricalDataImage.from_dict(coins_historical_data_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


