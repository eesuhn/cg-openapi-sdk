# ModelGlobal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GlobalData**](GlobalData.md) |  | [optional] 
**market_cap_change_percentage_24h_usd** | **float** | cryptocurrencies market cap change percentage in 24 hours in usd | [optional] 
**updated_at** | **float** |  | [optional] 

## Example

```python
from coingecko_sdk.models.model_global import ModelGlobal

# TODO update the JSON string below
json = "{}"
# create an instance of ModelGlobal from a JSON string
model_global_instance = ModelGlobal.from_json(json)
# print the JSON string representation of the object
print(ModelGlobal.to_json())

# convert the object into a dict
model_global_dict = model_global_instance.to_dict()
# create an instance of ModelGlobal from a dict
model_global_from_dict = ModelGlobal.from_dict(model_global_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


