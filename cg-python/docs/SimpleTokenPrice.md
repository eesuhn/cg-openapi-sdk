# SimpleTokenPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usd** | **float** | price in USD | [optional] 
**usd_market_cap** | **float** | market cap in USD | [optional] 
**usd_24h_vol** | **float** | 24hr volume in USD | [optional] 
**usd_24h_change** | **float** | 24hr change in USD | [optional] 
**last_updated_at** | **float** | last updated timestamp | [optional] 

## Example

```python
from coingecko_python.models.simple_token_price import SimpleTokenPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTokenPrice from a JSON string
simple_token_price_instance = SimpleTokenPrice.from_json(json)
# print the JSON string representation of the object
print(SimpleTokenPrice.to_json())

# convert the object into a dict
simple_token_price_dict = simple_token_price_instance.to_dict()
# create an instance of SimpleTokenPrice from a dict
simple_token_price_from_dict = SimpleTokenPrice.from_dict(simple_token_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


