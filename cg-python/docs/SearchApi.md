# coingecko_python.SearchApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_data**](SearchApi.md#search_data) | **GET** /search | Search Queries


# **search_data**
> Search search_data(query)

Search Queries

This endpoint allows you to **search for coins, categories and markets listed on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.search import Search
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
    api_instance = coingecko_python.SearchApi(api_client)
    query = 'query_example' # str | search query

    try:
        # Search Queries
        api_response = api_instance.search_data(query)
        print("The response of SearchApi->search_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search query | 

### Return type

[**Search**](Search.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of coins, categories and markets matching search term ordered by market cap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

