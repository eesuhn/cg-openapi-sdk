# coingecko-sdk.KeyApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_usage**](KeyApi.md#api_usage) | **GET** /key | 💼 API Usage


# **api_usage**
> Key api_usage()

💼 API Usage

This endpoint allows you to **monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.key import Key
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
    api_instance = coingecko-sdk.KeyApi(api_client)

    try:
        # 💼 API Usage
        api_response = api_instance.api_usage()
        print("The response of KeyApi->api_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->api_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Key**](Key.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

