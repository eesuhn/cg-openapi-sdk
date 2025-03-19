# coingecko_python.ExchangeRatesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_rates**](ExchangeRatesApi.md#exchange_rates) | **GET** /exchange_rates | BTC-to-Currency Exchange Rates


# **exchange_rates**
> ExchangeRates exchange_rates()

BTC-to-Currency Exchange Rates

This endpoint allows you to **query BTC exchange rates with other currencies**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.exchange_rates import ExchangeRates
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
    api_instance = coingecko_python.ExchangeRatesApi(api_client)

    try:
        # BTC-to-Currency Exchange Rates
        api_response = api_instance.exchange_rates()
        print("The response of ExchangeRatesApi->exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeRatesApi->exchange_rates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExchangeRates**](ExchangeRates.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List rates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

