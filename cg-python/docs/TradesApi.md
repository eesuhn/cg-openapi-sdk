# coingecko_sdk.TradesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pool_trades_contract_address**](TradesApi.md#pool_trades_contract_address) | **GET** /onchain/networks/{network}/pools/{pool_address}/trades | Past 24 Hour Trades by Pool Address


# **pool_trades_contract_address**
> Trades pool_trades_contract_address(network, pool_address, trade_volume_in_usd_greater_than=trade_volume_in_usd_greater_than, token=token)

Past 24 Hour Trades by Pool Address

This endpoint allows you to **query the last 300 trades in the past 24 hours based on the provided pool address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.trades import Trades
from coingecko_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro-api.coingecko.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = coingecko_sdk.Configuration(
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
with coingecko_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coingecko_sdk.TradesApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    pool_address = '0x06da0fd433c1a5d7a4faa01111c044910a184553' # str | pool contract address
    trade_volume_in_usd_greater_than = 3.4 # float | filter trades by trade volume in USD greater than this value <br> Default value: 0 (optional)
    token = 'base' # str | return trades for token <br> use this to invert the chart <br> Available values: 'base', 'quote' or token address <br> Default value: 'base' (optional)

    try:
        # Past 24 Hour Trades by Pool Address
        api_response = api_instance.pool_trades_contract_address(network, pool_address, trade_volume_in_usd_greater_than=trade_volume_in_usd_greater_than, token=token)
        print("The response of TradesApi->pool_trades_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradesApi->pool_trades_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **pool_address** | **str**| pool contract address | 
 **trade_volume_in_usd_greater_than** | **float**| filter trades by trade volume in USD greater than this value &lt;br&gt; Default value: 0 | [optional] 
 **token** | **str**| return trades for token &lt;br&gt; use this to invert the chart &lt;br&gt; Available values: &#39;base&#39;, &#39;quote&#39; or token address &lt;br&gt; Default value: &#39;base&#39; | [optional] 

### Return type

[**Trades**](Trades.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get last 300 trades in past 24 hours from a pool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

