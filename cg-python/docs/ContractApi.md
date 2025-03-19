# coingecko_sdk.ContractApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coins_contract_address**](ContractApi.md#coins_contract_address) | **GET** /coins/{id}/contract/{contract_address} | Coin Data by Token Address
[**contract_address_market_chart**](ContractApi.md#contract_address_market_chart) | **GET** /coins/{id}/contract/{contract_address}/market_chart | Coin Historical Chart Data by Token Address
[**contract_address_market_chart_range**](ContractApi.md#contract_address_market_chart_range) | **GET** /coins/{id}/contract/{contract_address}/market_chart/range | Coin Historical Chart Data within Time Range by Token Address


# **coins_contract_address**
> CoinsContractAddress coins_contract_address(id, contract_address)

Coin Data by Token Address

This endpoint allows you to **query all the metadata (image,  websites, socials, description, contract address, etc.) and  market data (price, ATH, exchange tickers, etc.) of a coin  from the CoinGecko coin page based on an asset platform and  a particular token contract address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.coins_contract_address import CoinsContractAddress
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
    api_instance = coingecko_sdk.ContractApi(api_client)
    id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list).
    contract_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' # str | the contract address of token

    try:
        # Coin Data by Token Address
        api_response = api_instance.coins_contract_address(id, contract_address)
        print("The response of ContractApi->coins_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->coins_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list). | 
 **contract_address** | **str**| the contract address of token | 

### Return type

[**CoinsContractAddress**](CoinsContractAddress.md)

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

# **contract_address_market_chart**
> CoinsMarketChart contract_address_market_chart(id, contract_address, vs_currency, days, interval=interval, precision=precision)

Coin Historical Chart Data by Token Address

This endpoint allows you to **get the historical chart data including time in UNIX, price, market cap and 24hr volume based on asset platform and particular token contract address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.coins_market_chart import CoinsMarketChart
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
    api_instance = coingecko_sdk.ContractApi(api_client)
    id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list).
    contract_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' # str | the contract address of token
    vs_currency = 'usd' # str | target currency of market data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    days = '1' # str | data up to number of days ago <br> You may use any integer or `max` for number of days
    interval = 'interval_example' # str | data interval, leave empty for auto granularity (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coin Historical Chart Data by Token Address
        api_response = api_instance.contract_address_market_chart(id, contract_address, vs_currency, days, interval=interval, precision=precision)
        print("The response of ContractApi->contract_address_market_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->contract_address_market_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list). | 
 **contract_address** | **str**| the contract address of token | 
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
**200** | Get historical market data include price, market cap, and 24hr volume |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_address_market_chart_range**
> CoinsMarketChartRange contract_address_market_chart_range(id, contract_address, vs_currency, var_from, to, interval=interval, precision=precision)

Coin Historical Chart Data within Time Range by Token Address

This endpoint allows you to **get the historical chart data within certain time range in UNIX along with price, market cap and 24hr volume based on asset platform and particular token contract address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.coins_market_chart_range import CoinsMarketChartRange
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
    api_instance = coingecko_sdk.ContractApi(api_client)
    id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list)
    contract_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' # str | the contract address of token
    vs_currency = 'usd' # str | target currency of market data <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    var_from = 1609459200 # float | starting date in UNIX timestamp
    to = 1640908800 # float | ending date in UNIX timestamp
    interval = 'interval_example' # str | data interval, leave empty for auto granularity (optional)
    precision = 'precision_example' # str | decimal place for currency price value (optional)

    try:
        # Coin Historical Chart Data within Time Range by Token Address
        api_response = api_instance.contract_address_market_chart_range(id, contract_address, vs_currency, var_from, to, interval=interval, precision=precision)
        print("The response of ContractApi->contract_address_market_chart_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->contract_address_market_chart_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list) | 
 **contract_address** | **str**| the contract address of token | 
 **vs_currency** | **str**| target currency of market data &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **var_from** | **float**| starting date in UNIX timestamp | 
 **to** | **float**| ending date in UNIX timestamp | 
 **interval** | **str**| data interval, leave empty for auto granularity | [optional] 
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
**200** | Get historical market data include price, market cap, and 24hr volume |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

