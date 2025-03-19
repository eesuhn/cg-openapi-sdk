# coingecko-sdk.ExchangesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchanges**](ExchangesApi.md#exchanges) | **GET** /exchanges | Exchanges List with data
[**exchanges_id**](ExchangesApi.md#exchanges_id) | **GET** /exchanges/{id} | Exchange Data by ID
[**exchanges_id_tickers**](ExchangesApi.md#exchanges_id_tickers) | **GET** /exchanges/{id}/tickers | Exchange Tickers by ID
[**exchanges_id_volume_chart**](ExchangesApi.md#exchanges_id_volume_chart) | **GET** /exchanges/{id}/volume_chart | Exchange Volume Chart by ID
[**exchanges_id_volume_chart_range**](ExchangesApi.md#exchanges_id_volume_chart_range) | **GET** /exchanges/{id}/volume_chart/range | 💼 Exchange Volume Chart within Time Range by ID
[**exchanges_list**](ExchangesApi.md#exchanges_list) | **GET** /exchanges/list | Exchanges List (ID Map)


# **exchanges**
> Exchanges exchanges(per_page=per_page, page=page)

Exchanges List with data

This endpoint allows you to **query all the supported exchanges with exchanges’ data (ID, name, country, ...) that have active trading volumes on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.exchanges import Exchanges
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    per_page = 3.4 # float | total results per page, default: 100 <br> Valid values: 1...250 (optional)
    page = 3.4 # float | page through results, default: 1 (optional)

    try:
        # Exchanges List with data
        api_response = api_instance.exchanges(per_page=per_page, page=page)
        print("The response of ExchangesApi->exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **float**| total results per page, default: 100 &lt;br&gt; Valid values: 1...250 | [optional] 
 **page** | **float**| page through results, default: 1 | [optional] 

### Return type

[**Exchanges**](Exchanges.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all exchanges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchanges_id**
> ExchangeData exchanges_id(id)

Exchange Data by ID

This endpoint allows you to **query exchange’s data (name, year established, country, ...), exchange volume in BTC and top 100 tickers based on exchange’s ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.exchange_data import ExchangeData
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    id = 'binance' # str | exchange ID <br> *refers to [`/exchanges/list`](/reference/exchanges-list).

    try:
        # Exchange Data by ID
        api_response = api_instance.exchanges_id(id)
        print("The response of ExchangesApi->exchanges_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| exchange ID &lt;br&gt; *refers to [&#x60;/exchanges/list&#x60;](/reference/exchanges-list). | 

### Return type

[**ExchangeData**](ExchangeData.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get exchange volume in BTC and top 100 tickers only |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchanges_id_tickers**
> ExchangeTickers exchanges_id_tickers(id, coin_ids=coin_ids, include_exchange_logo=include_exchange_logo, page=page, depth=depth, order=order)

Exchange Tickers by ID

This endpoint allows you to **query exchange's tickers based on exchange’s ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.exchange_tickers import ExchangeTickers
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    id = 'binance' # str | exchange ID <br> *refers to [`/exchanges/list`](/reference/exchanges-list).
    coin_ids = 'bitcoin' # str | filter tickers by coin IDs, comma-separated if querying more than 1 coin <br> *refers to [`/coins/list`](/reference/coins-list). (optional)
    include_exchange_logo = True # bool | include exchange logo, default: false (optional)
    page = 3.4 # float | page through results (optional)
    depth = True # bool | include 2% orderbook depth (Example: cost_to_move_up_usd & cost_to_move_down_usd),default: false (optional)
    order = 'order_example' # str | use this to sort the order of responses, default: trust_score_desc (optional)

    try:
        # Exchange Tickers by ID
        api_response = api_instance.exchanges_id_tickers(id, coin_ids=coin_ids, include_exchange_logo=include_exchange_logo, page=page, depth=depth, order=order)
        print("The response of ExchangesApi->exchanges_id_tickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges_id_tickers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| exchange ID &lt;br&gt; *refers to [&#x60;/exchanges/list&#x60;](/reference/exchanges-list). | 
 **coin_ids** | **str**| filter tickers by coin IDs, comma-separated if querying more than 1 coin &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | [optional] 
 **include_exchange_logo** | **bool**| include exchange logo, default: false | [optional] 
 **page** | **float**| page through results | [optional] 
 **depth** | **bool**| include 2% orderbook depth (Example: cost_to_move_up_usd &amp; cost_to_move_down_usd),default: false | [optional] 
 **order** | **str**| use this to sort the order of responses, default: trust_score_desc | [optional] 

### Return type

[**ExchangeTickers**](ExchangeTickers.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get exchange tickers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchanges_id_volume_chart**
> List[List[float]] exchanges_id_volume_chart(id, days)

Exchange Volume Chart by ID

This endpoint allows you to **query the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange’s ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    id = 'binance' # str | exchange ID or derivative exchange ID <br> *refers to [`/exchanges/list`](/reference/exchanges-list) or [`/derivatives/exchanges/list`](/reference/derivatives-exchanges-list).
    days = 'days_example' # str | data up to number of days ago

    try:
        # Exchange Volume Chart by ID
        api_response = api_instance.exchanges_id_volume_chart(id, days)
        print("The response of ExchangesApi->exchanges_id_volume_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges_id_volume_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| exchange ID or derivative exchange ID &lt;br&gt; *refers to [&#x60;/exchanges/list&#x60;](/reference/exchanges-list) or [&#x60;/derivatives/exchanges/list&#x60;](/reference/derivatives-exchanges-list). | 
 **days** | **str**| data up to number of days ago | 

### Return type

**List[List[float]]**

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get exchange volume chart data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchanges_id_volume_chart_range**
> List[List[float]] exchanges_id_volume_chart_range(id, var_from, to)

💼 Exchange Volume Chart within Time Range by ID

This endpoint allows you to **query the historical volume chart data in BTC by specifying date range in UNIX based on exchange’s ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    id = 'binance' # str | exchange ID or derivative exchange ID <br> *refers to [`/exchanges/list`](/reference/exchanges-list) or [`/derivatives/exchanges/list`](/reference/derivatives-exchanges-list).
    var_from = 1672531200 # float | starting date in UNIX timestamp 
    to = 1675123200 # float | ending date in UNIX timestamp

    try:
        # 💼 Exchange Volume Chart within Time Range by ID
        api_response = api_instance.exchanges_id_volume_chart_range(id, var_from, to)
        print("The response of ExchangesApi->exchanges_id_volume_chart_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges_id_volume_chart_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| exchange ID or derivative exchange ID &lt;br&gt; *refers to [&#x60;/exchanges/list&#x60;](/reference/exchanges-list) or [&#x60;/derivatives/exchanges/list&#x60;](/reference/derivatives-exchanges-list). | 
 **var_from** | **float**| starting date in UNIX timestamp  | 
 **to** | **float**| ending date in UNIX timestamp | 

### Return type

**List[List[float]]**

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get exchange volume chart data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchanges_list**
> ExchangesList exchanges_list(status=status)

Exchanges List (ID Map)

This endpoint allows you to **query all the exchanges with ID and name**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.exchanges_list import ExchangesList
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
    api_instance = coingecko-sdk.ExchangesApi(api_client)
    status = 'status_example' # str | filter by status of exchanges, default: active (optional)

    try:
        # Exchanges List (ID Map)
        api_response = api_instance.exchanges_list(status=status)
        print("The response of ExchangesApi->exchanges_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->exchanges_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| filter by status of exchanges, default: active | [optional] 

### Return type

[**ExchangesList**](ExchangesList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all exchanges with ID and name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

