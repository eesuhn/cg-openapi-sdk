# NFTTickers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickers** | [**List[NFTTickersTickersInner]**](NFTTickersTickersInner.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.nft_tickers import NFTTickers

# TODO update the JSON string below
json = "{}"
# create an instance of NFTTickers from a JSON string
nft_tickers_instance = NFTTickers.from_json(json)
# print the JSON string representation of the object
print(NFTTickers.to_json())

# convert the object into a dict
nft_tickers_dict = nft_tickers_instance.to_dict()
# create an instance of NFTTickers from a dict
nft_tickers_from_dict = NFTTickers.from_dict(nft_tickers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


