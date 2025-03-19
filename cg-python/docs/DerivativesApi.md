# coingecko_python.DerivativesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**derivatives_exchanges**](DerivativesApi.md#derivatives_exchanges) | **GET** /derivatives/exchanges | Derivatives Exchanges List with Data
[**derivatives_exchanges_id**](DerivativesApi.md#derivatives_exchanges_id) | **GET** /derivatives/exchanges/{id} | Derivatives Exchange Data by ID
[**derivatives_exchanges_list**](DerivativesApi.md#derivatives_exchanges_list) | **GET** /derivatives/exchanges/list | Derivatives Exchanges List (ID Map)
[**derivatives_tickers**](DerivativesApi.md#derivatives_tickers) | **GET** /derivatives | Derivatives Tickers List


# **derivatives_exchanges**
> DerivativesExchanges derivatives_exchanges(order=order, per_page=per_page, page=page)

Derivatives Exchanges List with Data

This endpoint allows you to **query all the derivatives exchanges with related data (ID, name, open interest, ...) on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.derivatives_exchanges import DerivativesExchanges
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
    api_instance = coingecko_python.DerivativesApi(api_client)
    order = 'order_example' # str | use this to sort the order of responses, default: open_interest_btc_desc (optional)
    per_page = 3.4 # float | total results per page (optional)
    page = 3.4 # float | page through results, default: 1 (optional)

    try:
        # Derivatives Exchanges List with Data
        api_response = api_instance.derivatives_exchanges(order=order, per_page=per_page, page=page)
        print("The response of DerivativesApi->derivatives_exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_exchanges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| use this to sort the order of responses, default: open_interest_btc_desc | [optional] 
 **per_page** | **float**| total results per page | [optional] 
 **page** | **float**| page through results, default: 1 | [optional] 

### Return type

[**DerivativesExchanges**](DerivativesExchanges.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all derivative exchanges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **derivatives_exchanges_id**
> DerivativesExchangesID derivatives_exchanges_id(id, include_tickers=include_tickers)

Derivatives Exchange Data by ID

This endpoint allows you to **query the derivatives exchange’s related data (ID, name, open interest, ...) based on the exchanges’ ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.derivatives_exchanges_id import DerivativesExchangesID
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
    api_instance = coingecko_python.DerivativesApi(api_client)
    id = 'binance_futures' # str | derivative exchange ID <br> *refers to [`/derivatives/exchanges/list`](/reference/derivatives-exchanges-list).
    include_tickers = 'include_tickers_example' # str | include tickers data (optional)

    try:
        # Derivatives Exchange Data by ID
        api_response = api_instance.derivatives_exchanges_id(id, include_tickers=include_tickers)
        print("The response of DerivativesApi->derivatives_exchanges_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_exchanges_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| derivative exchange ID &lt;br&gt; *refers to [&#x60;/derivatives/exchanges/list&#x60;](/reference/derivatives-exchanges-list). | 
 **include_tickers** | **str**| include tickers data | [optional] 

### Return type

[**DerivativesExchangesID**](DerivativesExchangesID.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get derivative exchange data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **derivatives_exchanges_list**
> DerivativesExchangesList derivatives_exchanges_list()

Derivatives Exchanges List (ID Map)

This endpoint allows you to **query all the derivatives exchanges with ID and name on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.derivatives_exchanges_list import DerivativesExchangesList
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
    api_instance = coingecko_python.DerivativesApi(api_client)

    try:
        # Derivatives Exchanges List (ID Map)
        api_response = api_instance.derivatives_exchanges_list()
        print("The response of DerivativesApi->derivatives_exchanges_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_exchanges_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DerivativesExchangesList**](DerivativesExchangesList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all derivative exchanges name and identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **derivatives_tickers**
> DerivativesTickersList derivatives_tickers()

Derivatives Tickers List

This endpoint allows you to **query all the tickers from derivatives exchanges on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.derivatives_tickers_list import DerivativesTickersList
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
    api_instance = coingecko_python.DerivativesApi(api_client)

    try:
        # Derivatives Tickers List
        api_response = api_instance.derivatives_tickers()
        print("The response of DerivativesApi->derivatives_tickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_tickers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DerivativesTickersList**](DerivativesTickersList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all derivative tickers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

