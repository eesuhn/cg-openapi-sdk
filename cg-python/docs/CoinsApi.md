# coingecko-sdk.CoinsApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coins_id**](CoinsApi.md#coins_id) | **GET** /coins/{id} | Coin Data by ID
[**coins_id_circulating_supply_chart**](CoinsApi.md#coins_id_circulating_supply_chart) | **GET** /coins/{id}/circulating_supply_chart | 👑 Circulating Supply Chart by ID
[**coins_id_circulating_supply_chart_range**](CoinsApi.md#coins_id_circulating_supply_chart_range) | **GET** /coins/{id}/circulating_supply_chart/range | 👑 Circulating Supply Chart within Time Range by ID
[**coins_id_history**](CoinsApi.md#coins_id_history) | **GET** /coins/{id}/history | Coin Historical Data by ID
[**coins_id_market_chart**](CoinsApi.md#coins_id_market_chart) | **GET** /coins/{id}/market_chart | Coin Historical Chart Data by ID
[**coins_id_market_chart_range**](CoinsApi.md#coins_id_market_chart_range) | **GET** /coins/{id}/market_chart/range | Coin Historical Chart Data within Time Range by ID
[**coins_id_ohlc**](CoinsApi.md#coins_id_ohlc) | **GET** /coins/{id}/ohlc | Coin OHLC Chart by ID
[**coins_id_ohlc_range**](CoinsApi.md#coins_id_ohlc_range) | **GET** /coins/{id}/ohlc/range | 💼 Coin OHLC Chart within Time Range by ID
[**coins_id_tickers**](CoinsApi.md#coins_id_tickers) | **GET** /coins/{id}/tickers | Coin Tickers by ID
[**coins_id_total_supply_chart**](CoinsApi.md#coins_id_total_supply_chart) | **GET** /coins/{id}/total_supply_chart | 👑 Total Supply Chart by ID
[**coins_id_total_supply_chart_range**](CoinsApi.md#coins_id_total_supply_chart_range) | **GET** /coins/{id}/total_supply_chart/range | 👑 Total Supply Chart within time range by ID
[**coins_list**](CoinsApi.md#coins_list) | **GET** /coins/list | Coins List (ID Map)
[**coins_list_new**](CoinsApi.md#coins_list_new) | **GET** /coins/list/new | 💼 Recently Added Coins
[**coins_markets**](CoinsApi.md#coins_markets) | **GET** /coins/markets | Coins List with Market Data
[**coins_top_gainers_losers**](CoinsApi.md#coins_top_gainers_losers) | **GET** /coins/top_gainers_losers | 💼 Top Gainers &amp; Losers


# **coins_id**
> CoinsID coins_id(id, localization=localization, tickers=tickers, market_data=market_data, community_data=community_data, developer_data=developer_data, sparkline=sparkline)

Coin Data by ID

This endpoint allows you to **query all the metadata (image,  websites, socials, description, contract address, etc.) and  market data (price, ATH, exchange tickers, etc.) of a coin  from the CoinGecko coin page based on a particular coin ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_id import CoinsID
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    localization = True # bool | include all the localized languages in the response, default: true (optional)
    tickers = True # bool | include tickers data, default: true (optional)
    market_data = True # bool | include market data, default: true (optional)
    community_data = True # bool | include community data, default: true (optional)
    developer_data = True # bool | include developer data, default: true (optional)
    sparkline = True # bool | include sparkline 7 days data, default: false (optional)

    try:
        # Coin Data by ID
        api_response = api_instance.coins_id(id, localization=localization, tickers=tickers, market_data=market_data, community_data=community_data, developer_data=developer_data, sparkline=sparkline)
        print("The response of CoinsApi->coins_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **localization** | **bool**| include all the localized languages in the response, default: true | [optional] 
 **tickers** | **bool**| include tickers data, default: true | [optional] 
 **market_data** | **bool**| include market data, default: true | [optional] 
 **community_data** | **bool**| include community data, default: true | [optional] 
 **developer_data** | **bool**| include developer data, default: true | [optional] 
 **sparkline** | **bool**| include sparkline 7 days data, default: false | [optional] 

### Return type

[**CoinsID**](CoinsID.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current data for a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_circulating_supply_chart**
> List[List[float]] coins_id_circulating_supply_chart(id, days, interval=interval)

👑 Circulating Supply Chart by ID

This endpoint allows you to **query historical circulating supply of a coin by number of days away from now based on provided coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    days = '1' # str | data up to number of days ago <br> Valid values: any integer or `max`
    interval = 'interval_example' # str | data interval (optional)

    try:
        # 👑 Circulating Supply Chart by ID
        api_response = api_instance.coins_id_circulating_supply_chart(id, days, interval=interval)
        print("The response of CoinsApi->coins_id_circulating_supply_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_circulating_supply_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **days** | **str**| data up to number of days ago &lt;br&gt; Valid values: any integer or &#x60;max&#x60; | 
 **interval** | **str**| data interval | [optional] 

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
**200** | Get historical circulating supply chart of a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_circulating_supply_chart_range**
> List[List[float]] coins_id_circulating_supply_chart_range(id, var_from, to)

👑 Circulating Supply Chart within Time Range by ID

This endpoint allows you to **query historical circulating supply of a coin, within a range of timestamp based on the provided coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    var_from = 1609459200 # float | starting date in UNIX timestamp 
    to = 1640908800 # float | ending date in UNIX timestamp 

    try:
        # 👑 Circulating Supply Chart within Time Range by ID
        api_response = api_instance.coins_id_circulating_supply_chart_range(id, var_from, to)
        print("The response of CoinsApi->coins_id_circulating_supply_chart_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_circulating_supply_chart_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **var_from** | **float**| starting date in UNIX timestamp  | 
 **to** | **float**| ending date in UNIX timestamp  | 

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
**200** | Get historical circulating supply chart of a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_history**
> CoinsHistoricalData coins_id_history(id, var_date, localization=localization)

Coin Historical Data by ID

This endpoint allows you to **query the historical data (price, market cap, 24hrs volume, ...) at a given date for a coin based on a particular coin ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_historical_data import CoinsHistoricalData
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    var_date = '30-12-2017' # str | the date of data snapshot <br> Format: `dd-mm-yyyy`
    localization = True # bool | include all the localized languages in response, default: true (optional)

    try:
        # Coin Historical Data by ID
        api_response = api_instance.coins_id_history(id, var_date, localization=localization)
        print("The response of CoinsApi->coins_id_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **var_date** | **str**| the date of data snapshot &lt;br&gt; Format: &#x60;dd-mm-yyyy&#x60; | 
 **localization** | **bool**| include all the localized languages in response, default: true | [optional] 

### Return type

[**CoinsHistoricalData**](CoinsHistoricalData.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get historical data (name, price, market, stats) at a given date for a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_market_chart**
> CoinsMarketChart coins_id_market_chart(id, vs_currency, days, interval=interval, precision=precision)

Coin Historical Chart Data by ID

This endpoint allows you to **get the historical chart data of a coin including time in UNIX, price, market cap and 24hr volume based on particular coin ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_market_chart import CoinsMarketChart
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    vs_currency = 'usd' # str | target currency of market data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    days = '1' # str | data up to number of days ago <br> You may use any integer or `max` for number of days
    interval = 'interval_example' # str | data interval, leave empty for auto granularity (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coin Historical Chart Data by ID
        api_response = api_instance.coins_id_market_chart(id, vs_currency, days, interval=interval, precision=precision)
        print("The response of CoinsApi->coins_id_market_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_market_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **vs_currency** | **str**| target currency of market data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **days** | **str**| data up to number of days ago &lt;br&gt; You may use any integer or &#x60;max&#x60; for number of days | 
 **interval** | **str**| data interval, leave empty for auto granularity | [optional] 
 **precision** | **str**| decimal place for currency price value | [optional] 

### Return type

[**CoinsMarketChart**](CoinsMarketChart.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get historical market data include price, market cap, and 24hr volume (granularity auto) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_market_chart_range**
> CoinsMarketChartRange coins_id_market_chart_range(id, vs_currency, var_from, to, interval=interval, precision=precision)

Coin Historical Chart Data within Time Range by ID

This endpoint allows you to **get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hr volume based on particular coin ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_market_chart_range import CoinsMarketChartRange
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    vs_currency = 'usd' # str | target currency of market data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    var_from = 1609459200 # float | starting date in UNIX timestamp 
    to = 1640908800 # float | ending date in UNIX timestamp
    interval = 'interval_example' # str | data interval, leave empty for auto granularity  (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coin Historical Chart Data within Time Range by ID
        api_response = api_instance.coins_id_market_chart_range(id, vs_currency, var_from, to, interval=interval, precision=precision)
        print("The response of CoinsApi->coins_id_market_chart_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_market_chart_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **vs_currency** | **str**| target currency of market data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **var_from** | **float**| starting date in UNIX timestamp  | 
 **to** | **float**| ending date in UNIX timestamp | 
 **interval** | **str**| data interval, leave empty for auto granularity  | [optional] 
 **precision** | **str**| decimal place for currency price value | [optional] 

### Return type

[**CoinsMarketChartRange**](CoinsMarketChartRange.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get historical market data include price, market cap, and 24hr volume (granularity auto) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_ohlc**
> List[List[float]] coins_id_ohlc(id, vs_currency, days, interval=interval, precision=precision)

Coin OHLC Chart by ID

This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    vs_currency = 'usd' # str | target currency of price data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    days = 'days_example' # str | data up to number of days ago 
    interval = 'interval_example' # str | data interval, leave empty for auto granularity (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coin OHLC Chart by ID
        api_response = api_instance.coins_id_ohlc(id, vs_currency, days, interval=interval, precision=precision)
        print("The response of CoinsApi->coins_id_ohlc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_ohlc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **vs_currency** | **str**| target currency of price data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **days** | **str**| data up to number of days ago  | 
 **interval** | **str**| data interval, leave empty for auto granularity | [optional] 
 **precision** | **str**| decimal place for currency price value | [optional] 

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
**200** | Get coin&#39;s OHLC |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_ohlc_range**
> List[List[float]] coins_id_ohlc_range(id, vs_currency, var_from, to, interval)

💼 Coin OHLC Chart within Time Range by ID

This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a coin within a range of timestamp based on particular coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    vs_currency = 'usd' # str | target currency of price data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    var_from = 1709251200 # float | starting date in UNIX timestamp
    to = 1709596800 # float | ending date in UNIX timestamp
    interval = 'interval_example' # str | data interval

    try:
        # 💼 Coin OHLC Chart within Time Range by ID
        api_response = api_instance.coins_id_ohlc_range(id, vs_currency, var_from, to, interval)
        print("The response of CoinsApi->coins_id_ohlc_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_ohlc_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **vs_currency** | **str**| target currency of price data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **var_from** | **float**| starting date in UNIX timestamp | 
 **to** | **float**| ending date in UNIX timestamp | 
 **interval** | **str**| data interval | 

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
**200** | Get coin&#39;s OHLC within time range |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_tickers**
> CoinsTickers coins_id_tickers(id, exchange_ids=exchange_ids, include_exchange_logo=include_exchange_logo, page=page, order=order, depth=depth)

Coin Tickers by ID

This endpoint allows you to **query the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_tickers import CoinsTickers
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    exchange_ids = 'binance' # str | exchange ID <br> *refers to [`/exchanges/list`](/reference/exchanges-list). (optional)
    include_exchange_logo = True # bool | include exchange logo, default: false (optional)
    page = 3.4 # float | page through results (optional)
    order = 'order_example' # str | use this to sort the order of responses, default: trust_score_desc (optional)
    depth = True # bool | include 2% orderbook depth, ie. `cost_to_move_up_usd` and `cost_to_move_down_usd` <br> Default: false (optional)

    try:
        # Coin Tickers by ID
        api_response = api_instance.coins_id_tickers(id, exchange_ids=exchange_ids, include_exchange_logo=include_exchange_logo, page=page, order=order, depth=depth)
        print("The response of CoinsApi->coins_id_tickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_tickers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **exchange_ids** | **str**| exchange ID &lt;br&gt; *refers to [&#x60;/exchanges/list&#x60;](/reference/exchanges-list). | [optional] 
 **include_exchange_logo** | **bool**| include exchange logo, default: false | [optional] 
 **page** | **float**| page through results | [optional] 
 **order** | **str**| use this to sort the order of responses, default: trust_score_desc | [optional] 
 **depth** | **bool**| include 2% orderbook depth, ie. &#x60;cost_to_move_up_usd&#x60; and &#x60;cost_to_move_down_usd&#x60; &lt;br&gt; Default: false | [optional] 

### Return type

[**CoinsTickers**](CoinsTickers.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get coin tickers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_total_supply_chart**
> List[List[float]] coins_id_total_supply_chart(id, days, interval=interval)

👑 Total Supply Chart by ID

This endpoint allows you to **query historical total supply of a coin by number of days away from now based on provided coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    days = '1' # str | data up to number of days ago <br> Valid values: any integer or `max`
    interval = 'interval_example' # str | data interval (optional)

    try:
        # 👑 Total Supply Chart by ID
        api_response = api_instance.coins_id_total_supply_chart(id, days, interval=interval)
        print("The response of CoinsApi->coins_id_total_supply_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_total_supply_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **days** | **str**| data up to number of days ago &lt;br&gt; Valid values: any integer or &#x60;max&#x60; | 
 **interval** | **str**| data interval | [optional] 

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
**200** | Get historical total supply chart of a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_id_total_supply_chart_range**
> List[List[float]] coins_id_total_supply_chart_range(id, var_from, to)

👑 Total Supply Chart within time range by ID

This endpoint allows you to **query historical total supply of a coin, within a range of timestamp based on the provided coin ID**

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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    id = 'bitcoin' # str | coin ID <br> *refers to [`/coins/list`](/reference/coins-list).
    var_from = 1609459200 # float | starting date in UNIX timestamp 
    to = 1640908800 # float | ending date in UNIX timestamp 

    try:
        # 👑 Total Supply Chart within time range by ID
        api_response = api_instance.coins_id_total_supply_chart_range(id, var_from, to)
        print("The response of CoinsApi->coins_id_total_supply_chart_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_id_total_supply_chart_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| coin ID &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **var_from** | **float**| starting date in UNIX timestamp  | 
 **to** | **float**| ending date in UNIX timestamp  | 

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
**200** | Get historical total supply chart range of a coin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_list**
> List[CoinsListInner] coins_list(include_platform=include_platform, status=status)

Coins List (ID Map)

This endpoint allows you to **query all the supported coins on CoinGecko with coins ID, name and symbol**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_list_inner import CoinsListInner
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    include_platform = True # bool | include platform and token's contract addresses, default: false (optional)
    status = 'status_example' # str | filter by status of coins, default: active (optional)

    try:
        # Coins List (ID Map)
        api_response = api_instance.coins_list(include_platform=include_platform, status=status)
        print("The response of CoinsApi->coins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_platform** | **bool**| include platform and token&#39;s contract addresses, default: false | [optional] 
 **status** | **str**| filter by status of coins, default: active | [optional] 

### Return type

[**List[CoinsListInner]**](CoinsListInner.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all coins with ID, name, and symbol |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_list_new**
> List[CoinsListNewInner] coins_list_new()

💼 Recently Added Coins

This endpoint allows you to **query the latest 200 coins that recently listed on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_list_new_inner import CoinsListNewInner
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
    api_instance = coingecko-sdk.CoinsApi(api_client)

    try:
        # 💼 Recently Added Coins
        api_response = api_instance.coins_list_new()
        print("The response of CoinsApi->coins_list_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_list_new: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CoinsListNewInner]**](CoinsListNewInner.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List latest 200 coins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_markets**
> CoinsMarkets coins_markets(vs_currency, ids=ids, category=category, order=order, per_page=per_page, page=page, sparkline=sparkline, price_change_percentage=price_change_percentage, locale=locale, precision=precision)

Coins List with Market Data

This endpoint allows you to **query all the supported coins with price, market cap, volume and market related data**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.coins_markets import CoinsMarkets
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    vs_currency = 'usd' # str | target currency of coins and market data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    ids = 'bitcoin' # str | coins' IDs, comma-separated if querying more than 1 coin. <br> *refers to [`/coins/list`](/reference/coins-list). (optional)
    category = 'layer-1' # str | filter based on coins' category <br> *refers to [`/coins/categories/list`](/reference/coins-categories-list). (optional)
    order = 'order_example' # str | sort result by field, default: market_cap_desc (optional)
    per_page = 3.4 # float | total results per page, default: 100 <br> Valid values: 1...250 (optional)
    page = 3.4 # float | page through results, default: 1 (optional)
    sparkline = True # bool | include sparkline 7 days data, default: false (optional)
    price_change_percentage = '1h' # str | include price change percentage timeframe, comma-separated if query more than 1 price change percentage timeframe <br> Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y (optional)
    locale = 'locale_example' # str | language background, default: en (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coins List with Market Data
        api_response = api_instance.coins_markets(vs_currency, ids=ids, category=category, order=order, per_page=per_page, page=page, sparkline=sparkline, price_change_percentage=price_change_percentage, locale=locale, precision=precision)
        print("The response of CoinsApi->coins_markets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_markets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vs_currency** | **str**| target currency of coins and market data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **ids** | **str**| coins&#39; IDs, comma-separated if querying more than 1 coin. &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | [optional] 
 **category** | **str**| filter based on coins&#39; category &lt;br&gt; *refers to [&#x60;/coins/categories/list&#x60;](/reference/coins-categories-list). | [optional] 
 **order** | **str**| sort result by field, default: market_cap_desc | [optional] 
 **per_page** | **float**| total results per page, default: 100 &lt;br&gt; Valid values: 1...250 | [optional] 
 **page** | **float**| page through results, default: 1 | [optional] 
 **sparkline** | **bool**| include sparkline 7 days data, default: false | [optional] 
 **price_change_percentage** | **str**| include price change percentage timeframe, comma-separated if query more than 1 price change percentage timeframe &lt;br&gt; Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y | [optional] 
 **locale** | **str**| language background, default: en | [optional] 
 **precision** | **str**| decimal place for currency price value | [optional] 

### Return type

[**CoinsMarkets**](CoinsMarkets.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all coins with market data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_top_gainers_losers**
> List[TopGainersLosersInner] coins_top_gainers_losers(vs_currency, duration=duration, top_coins=top_coins)

💼 Top Gainers & Losers

This endpoint allows you to **query the top 30 coins with largest price gain and loss by a specific time duration**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.top_gainers_losers_inner import TopGainersLosersInner
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
    api_instance = coingecko-sdk.CoinsApi(api_client)
    vs_currency = 'usd' # str | target currency of coins <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    duration = 'duration_example' # str | filter result by time range <br> Default value: `24h` (optional)
    top_coins = 'top_coins_example' # str | filter result by market cap ranking (top 300 to 1000) or all coins (including coins that do not have market cap) <br> Default value: `1000` (optional)

    try:
        # 💼 Top Gainers & Losers
        api_response = api_instance.coins_top_gainers_losers(vs_currency, duration=duration, top_coins=top_coins)
        print("The response of CoinsApi->coins_top_gainers_losers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoinsApi->coins_top_gainers_losers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vs_currency** | **str**| target currency of coins &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **duration** | **str**| filter result by time range &lt;br&gt; Default value: &#x60;24h&#x60; | [optional] 
 **top_coins** | **str**| filter result by market cap ranking (top 300 to 1000) or all coins (including coins that do not have market cap) &lt;br&gt; Default value: &#x60;1000&#x60; | [optional] 

### Return type

[**List[TopGainersLosersInner]**](TopGainersLosersInner.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List top 30 gainers and losers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

