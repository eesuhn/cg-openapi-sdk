# coingecko_python.DexesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dexes_list**](DexesApi.md#dexes_list) | **GET** /onchain/networks/{network}/dexes | Supported Dexes List by Network (ID Map)


# **dexes_list**
> DexesList dexes_list(network, page=page)

Supported Dexes List by Network (ID Map)

This endpoint allows you to **query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.dexes_list import DexesList
from coingecko_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro-api.coingecko.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = coingecko_python.Configuration(
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
with coingecko_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coingecko_python.DexesApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    page = 56 # int | page through results <br> Default value: 1 (optional)

    try:
        # Supported Dexes List by Network (ID Map)
        api_response = api_instance.dexes_list(network, page=page)
        print("The response of DexesApi->dexes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexesApi->dexes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 

### Return type

[**DexesList**](DexesList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of supported DEXs on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

