# coingecko_python.CompaniesBetaApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_public_treasury**](CompaniesBetaApi.md#companies_public_treasury) | **GET** /companies/public_treasury/{coin_id} | Public Companies Holdings


# **companies_public_treasury**
> CompaniesTreasury companies_public_treasury(coin_id)

Public Companies Holdings

This endpoint allows you **query public companies’ Bitcoin or Ethereum holdings**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.companies_treasury import CompaniesTreasury
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
    api_instance = coingecko_python.CompaniesBetaApi(api_client)
    coin_id = 'coin_id_example' # str | coin ID

    try:
        # Public Companies Holdings
        api_response = api_instance.companies_public_treasury(coin_id)
        print("The response of CompaniesBetaApi->companies_public_treasury:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesBetaApi->companies_public_treasury: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin_id** | **str**| coin ID | 

### Return type

[**CompaniesTreasury**](CompaniesTreasury.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get public companies treasury data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

