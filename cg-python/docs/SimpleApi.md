# coingecko_sdk.SimpleApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**onchain_simple_price**](SimpleApi.md#onchain_simple_price) | **GET** /onchain/simple/networks/{network}/token_price/{addresses} | Token Price by Token Addresses
[**simple_price**](SimpleApi.md#simple_price) | **GET** /simple/price | Coin Price by IDs
[**simple_supported_currencies**](SimpleApi.md#simple_supported_currencies) | **GET** /simple/supported_vs_currencies | Supported Currencies List
[**simple_token_price**](SimpleApi.md#simple_token_price) | **GET** /simple/token_price/{id} | Coin Price by Token Addresses


# **onchain_simple_price**
> OnchainSimplePrice onchain_simple_price(network, addresses, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_price_change=include_24hr_price_change, include_total_reserve_in_usd=include_total_reserve_in_usd)

Token Price by Token Addresses

This endpoint allows you to **get token price based on the provided token contract address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.onchain_simple_price import OnchainSimplePrice
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
    api_instance = coingecko_sdk.SimpleApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    addresses = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2' # str | token contract address, comma-separated if more than one token contract address
    include_market_cap = True # bool | include market capitalization, default: false (optional)
    include_24hr_vol = True # bool | include 24hr volume, default: false (optional)
    include_24hr_price_change = True # bool | include 24hr price change, default: false (optional)
    include_total_reserve_in_usd = True # bool | include total reserve in USD, default: false (optional)

    try:
        # Token Price by Token Addresses
        api_response = api_instance.onchain_simple_price(network, addresses, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_price_change=include_24hr_price_change, include_total_reserve_in_usd=include_total_reserve_in_usd)
        print("The response of SimpleApi->onchain_simple_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleApi->onchain_simple_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **addresses** | **str**| token contract address, comma-separated if more than one token contract address | 
 **include_market_cap** | **bool**| include market capitalization, default: false | [optional] 
 **include_24hr_vol** | **bool**| include 24hr volume, default: false | [optional] 
 **include_24hr_price_change** | **bool**| include 24hr price change, default: false | [optional] 
 **include_total_reserve_in_usd** | **bool**| include total reserve in USD, default: false | [optional] 

### Return type

[**OnchainSimplePrice**](OnchainSimplePrice.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current USD prices of multiple tokens on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simple_price**
> SimplePrice simple_price(ids, vs_currencies, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_change=include_24hr_change, include_last_updated_at=include_last_updated_at, precision=precision)

Coin Price by IDs

This endpoint allows you to **query the prices of one or more coins by using their unique Coin API IDs**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.simple_price import SimplePrice
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
    api_instance = coingecko_sdk.SimpleApi(api_client)
    ids = 'bitcoin' # str | coins' IDs, comma-separated if querying more than 1 coin. <br> *refers to [`/coins/list`](/reference/coins-list).
    vs_currencies = 'usd' # str | target currency of coins, comma-separated if querying more than 1 currency. <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    include_market_cap = True # bool | include market capitalization, default: false (optional)
    include_24hr_vol = True # bool | include 24hr volume, default: false (optional)
    include_24hr_change = True # bool | include 24hr change, default: false (optional)
    include_last_updated_at = True # bool | include last updated price time in UNIX, default: false (optional)
    precision = 'precision_example' # str | decimal place for currency price value  (optional)

    try:
        # Coin Price by IDs
        api_response = api_instance.simple_price(ids, vs_currencies, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_change=include_24hr_change, include_last_updated_at=include_last_updated_at, precision=precision)
        print("The response of SimpleApi->simple_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleApi->simple_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| coins&#39; IDs, comma-separated if querying more than 1 coin. &lt;br&gt; *refers to [&#x60;/coins/list&#x60;](/reference/coins-list). | 
 **vs_currencies** | **str**| target currency of coins, comma-separated if querying more than 1 currency. &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **include_market_cap** | **bool**| include market capitalization, default: false | [optional] 
 **include_24hr_vol** | **bool**| include 24hr volume, default: false | [optional] 
 **include_24hr_change** | **bool**| include 24hr change, default: false | [optional] 
 **include_last_updated_at** | **bool**| include last updated price time in UNIX, default: false | [optional] 
 **precision** | **str**| decimal place for currency price value  | [optional] 

### Return type

[**SimplePrice**](SimplePrice.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | price(s) of cryptocurrency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simple_supported_currencies**
> List[str] simple_supported_currencies()

Supported Currencies List

This endpoint allows you to **query all the supported currencies on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
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
    api_instance = coingecko_sdk.SimpleApi(api_client)

    try:
        # Supported Currencies List
        api_response = api_instance.simple_supported_currencies()
        print("The response of SimpleApi->simple_supported_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleApi->simple_supported_currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of supported currencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simple_token_price**
> SimpleTokenPrice simple_token_price(id, contract_addresses, vs_currencies, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_change=include_24hr_change, include_last_updated_at=include_last_updated_at, precision=precision)

Coin Price by Token Addresses

This endpoint allows you to **query a token price by using token contract address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.simple_token_price import SimpleTokenPrice
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
    api_instance = coingecko_sdk.SimpleApi(api_client)
    id = 'ethereum' # str | asset platform's ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list).
    contract_addresses = '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599' # str | the contract addresses of tokens, comma-separated if querying more than 1 token's contract address
    vs_currencies = 'usd' # str | target currency of coins, comma-separated if querying more than 1 currency. <br> *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    include_market_cap = True # bool | include market capitalization, default: false (optional)
    include_24hr_vol = True # bool | include 24hr volume, default: false (optional)
    include_24hr_change = True # bool | include 24hr change <br> default: false (optional)
    include_last_updated_at = True # bool | include last updated price time in UNIX , default: false (optional)
    precision = 'precision_example' # str | decimal place for currency price value  (optional)

    try:
        # Coin Price by Token Addresses
        api_response = api_instance.simple_token_price(id, contract_addresses, vs_currencies, include_market_cap=include_market_cap, include_24hr_vol=include_24hr_vol, include_24hr_change=include_24hr_change, include_last_updated_at=include_last_updated_at, precision=precision)
        print("The response of SimpleApi->simple_token_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleApi->simple_token_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| asset platform&#39;s ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list). | 
 **contract_addresses** | **str**| the contract addresses of tokens, comma-separated if querying more than 1 token&#39;s contract address | 
 **vs_currencies** | **str**| target currency of coins, comma-separated if querying more than 1 currency. &lt;br&gt; *refers to [&#x60;/simple/supported_vs_currencies&#x60;](/reference/simple-supported-currencies). | 
 **include_market_cap** | **bool**| include market capitalization, default: false | [optional] 
 **include_24hr_vol** | **bool**| include 24hr volume, default: false | [optional] 
 **include_24hr_change** | **bool**| include 24hr change &lt;br&gt; default: false | [optional] 
 **include_last_updated_at** | **bool**| include last updated price time in UNIX , default: false | [optional] 
 **precision** | **str**| decimal place for currency price value  | [optional] 

### Return type

[**SimpleTokenPrice**](SimpleTokenPrice.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | price(s) of cryptocurrency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

