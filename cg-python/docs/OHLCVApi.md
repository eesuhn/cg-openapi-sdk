# coingecko-sdk.OHLCVApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pool_ohlcv_contract_address**](OHLCVApi.md#pool_ohlcv_contract_address) | **GET** /onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe} | Pool OHLCV chart by Pool Address


# **pool_ohlcv_contract_address**
> OHLCV pool_ohlcv_contract_address(network, pool_address, timeframe, aggregate=aggregate, before_timestamp=before_timestamp, limit=limit, currency=currency, token=token)

Pool OHLCV chart by Pool Address

This endpoint allows you to **get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.ohlcv import OHLCV
from coingecko-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro-api.coingecko.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = coingecko-sdk.Configuration(
    host = "https://pro-api.coingecko.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: proKeyAuth
configuration.api_key['proKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['proKeyAuth'] = 'Bearer'

# Configure API key authorization: demoKeyAuth
configuration.api_key['demoKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['demoKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with coingecko-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coingecko-sdk.OHLCVApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    pool_address = '0x06da0fd433c1a5d7a4faa01111c044910a184553' # str | pool contract address
    timeframe = 'timeframe_example' # str | timeframe of the OHLCV chart
    aggregate = 'aggregate_example' # str | time period to aggregate each OHLCV <br> Available values (day): `1` <br> Available values (hour): `1` , `4` , `12` <br> Available values (minute): `1` , `5` , `15` <br> Default value: 1 (optional)
    before_timestamp = 56 # int | return OHLCV data before this timestamp (integer seconds since epoch) (optional)
    limit = 56 # int | number of OHLCV results to return, maximum 1000 <br> Default value: 100 (optional)
    currency = 'currency_example' # str | return OHLCV in USD or quote token <br> Default value: usd (optional)
    token = 'base' # str | return OHLCV for token <br> use this to invert the chart <br> Available values: 'base', 'quote' or token address <br> Default value: 'base' (optional)

    try:
        # Pool OHLCV chart by Pool Address
        api_response = api_instance.pool_ohlcv_contract_address(network, pool_address, timeframe, aggregate=aggregate, before_timestamp=before_timestamp, limit=limit, currency=currency, token=token)
        print("The response of OHLCVApi->pool_ohlcv_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OHLCVApi->pool_ohlcv_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **pool_address** | **str**| pool contract address | 
 **timeframe** | **str**| timeframe of the OHLCV chart | 
 **aggregate** | **str**| time period to aggregate each OHLCV &lt;br&gt; Available values (day): &#x60;1&#x60; &lt;br&gt; Available values (hour): &#x60;1&#x60; , &#x60;4&#x60; , &#x60;12&#x60; &lt;br&gt; Available values (minute): &#x60;1&#x60; , &#x60;5&#x60; , &#x60;15&#x60; &lt;br&gt; Default value: 1 | [optional] 
 **before_timestamp** | **int**| return OHLCV data before this timestamp (integer seconds since epoch) | [optional] 
 **limit** | **int**| number of OHLCV results to return, maximum 1000 &lt;br&gt; Default value: 100 | [optional] 
 **currency** | **str**| return OHLCV in USD or quote token &lt;br&gt; Default value: usd | [optional] 
 **token** | **str**| return OHLCV for token &lt;br&gt; use this to invert the chart &lt;br&gt; Available values: &#39;base&#39;, &#39;quote&#39; or token address &lt;br&gt; Default value: &#39;base&#39; | [optional] 

### Return type

[**OHLCV**](OHLCV.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get OHLCV data of a pool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

