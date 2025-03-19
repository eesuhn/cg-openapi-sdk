# coingecko_sdk.NetworksApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networks_list**](NetworksApi.md#networks_list) | **GET** /onchain/networks | Supported Networks List (ID Map)


# **networks_list**
> NetworksList networks_list(page=page)

Supported Networks List (ID Map)

This endpoint allows you to **query all the supported networks on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.networks_list import NetworksList
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
    api_instance = coingecko_sdk.NetworksApi(api_client)
    page = 56 # int | page through results <br> Default value: 1 (optional)

    try:
        # Supported Networks List (ID Map)
        api_response = api_instance.networks_list(page=page)
        print("The response of NetworksApi->networks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 

### Return type

[**NetworksList**](NetworksList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of supported networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

