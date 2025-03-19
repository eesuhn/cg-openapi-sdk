# coingecko_sdk.NFTsBetaApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nfts_contract_address**](NFTsBetaApi.md#nfts_contract_address) | **GET** /nfts/{asset_platform_id}/contract/{contract_address} | NFTs Collection Data by Contract Address
[**nfts_contract_address_market_chart**](NFTsBetaApi.md#nfts_contract_address_market_chart) | **GET** /nfts/{asset_platform_id}/contract/{contract_address}/market_chart | 💼 NFTs Collection Historical Chart Data by Contract Address
[**nfts_id**](NFTsBetaApi.md#nfts_id) | **GET** /nfts/{id} | NFTs Collection Data by ID
[**nfts_id_market_chart**](NFTsBetaApi.md#nfts_id_market_chart) | **GET** /nfts/{id}/market_chart | 💼 NFTs Collection Historical Chart Data by ID
[**nfts_id_tickers**](NFTsBetaApi.md#nfts_id_tickers) | **GET** /nfts/{id}/tickers | 💼 NFTs Collection Tickers by ID
[**nfts_list**](NFTsBetaApi.md#nfts_list) | **GET** /nfts/list | NFTs List (ID Map)
[**nfts_markets**](NFTsBetaApi.md#nfts_markets) | **GET** /nfts/markets | 💼 NFTs List with Market Data


# **nfts_contract_address**
> NFTData nfts_contract_address(asset_platform_id, contract_address)

NFTs Collection Data by Contract Address

This endpoint allows you to **query all the NFT data (name, floor price, 24hr volume ...) based on the NFT collection contract address and respective asset platform**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_data import NFTData
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    asset_platform_id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list)
    contract_address = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8' # str | the contract address of token

    try:
        # NFTs Collection Data by Contract Address
        api_response = api_instance.nfts_contract_address(asset_platform_id, contract_address)
        print("The response of NFTsBetaApi->nfts_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_platform_id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list) | 
 **contract_address** | **str**| the contract address of token | 

### Return type

[**NFTData**](NFTData.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get NFTs data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfts_contract_address_market_chart**
> NFTMarketChart nfts_contract_address_market_chart(asset_platform_id, contract_address, days)

💼 NFTs Collection Historical Chart Data by Contract Address

This endpoint allows you **query historical market data of a NFT collection, including floor price, market cap, and 24hr volume, by number of days away from now based on the provided contract address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_market_chart import NFTMarketChart
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    asset_platform_id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list)
    contract_address = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8' # str | contract address of the NFT collection
    days = '1' # str | data up to number of days ago <br> Valid values: any integer or max

    try:
        # 💼 NFTs Collection Historical Chart Data by Contract Address
        api_response = api_instance.nfts_contract_address_market_chart(asset_platform_id, contract_address, days)
        print("The response of NFTsBetaApi->nfts_contract_address_market_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_contract_address_market_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_platform_id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list) | 
 **contract_address** | **str**| contract address of the NFT collection | 
 **days** | **str**| data up to number of days ago &lt;br&gt; Valid values: any integer or max | 

### Return type

[**NFTMarketChart**](NFTMarketChart.md)

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

# **nfts_id**
> NFTData nfts_id(id)

NFTs Collection Data by ID

This endpoint allows you to **query all the NFT data (name, floor price, 24hr volume ...) based on the NFT collection ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_data import NFTData
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    id = 'pudgy-penguins' # str | NFTs ID <br> *refers to [`/nfts/list`](/reference/nfts-list).

    try:
        # NFTs Collection Data by ID
        api_response = api_instance.nfts_id(id)
        print("The response of NFTsBetaApi->nfts_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFTs ID &lt;br&gt; *refers to [&#x60;/nfts/list&#x60;](/reference/nfts-list). | 

### Return type

[**NFTData**](NFTData.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get NFTs data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfts_id_market_chart**
> NFTMarketChart nfts_id_market_chart(id, days)

💼 NFTs Collection Historical Chart Data by ID

This endpoint allows you **query historical market data of a NFT collection, including floor price, market cap, and 24hr volume, by number of days away from now**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_market_chart import NFTMarketChart
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    id = 'pudgy-penguins' # str | NFTs ID <br> *refers to [`/nfts/list`](/reference/nfts-list).
    days = '1' # str | data up to number of days <br> Valid values: any integer or max

    try:
        # 💼 NFTs Collection Historical Chart Data by ID
        api_response = api_instance.nfts_id_market_chart(id, days)
        print("The response of NFTsBetaApi->nfts_id_market_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_id_market_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFTs ID &lt;br&gt; *refers to [&#x60;/nfts/list&#x60;](/reference/nfts-list). | 
 **days** | **str**| data up to number of days &lt;br&gt; Valid values: any integer or max | 

### Return type

[**NFTMarketChart**](NFTMarketChart.md)

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

# **nfts_id_tickers**
> NFTTickers nfts_id_tickers(id)

💼 NFTs Collection Tickers by ID

This endpoint allows you to **query the latest floor price and 24hr volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_tickers import NFTTickers
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    id = 'pudgy-penguins' # str | NFTs ID <br> *refers to [`/nfts/list`](/reference/nfts-list).

    try:
        # 💼 NFTs Collection Tickers by ID
        api_response = api_instance.nfts_id_tickers(id)
        print("The response of NFTsBetaApi->nfts_id_tickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_id_tickers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFTs ID &lt;br&gt; *refers to [&#x60;/nfts/list&#x60;](/reference/nfts-list). | 

### Return type

[**NFTTickers**](NFTTickers.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get NFTs tickers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfts_list**
> NFTList nfts_list(order=order, per_page=per_page, page=page)

NFTs List (ID Map)

This endpoint allows you to **query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nft_list import NFTList
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    order = 'order_example' # str | use this to sort the order of responses (optional)
    per_page = 3.4 # float | total results per page <br> Valid values: 1...250 (optional)
    page = 3.4 # float | page through results (optional)

    try:
        # NFTs List (ID Map)
        api_response = api_instance.nfts_list(order=order, per_page=per_page, page=page)
        print("The response of NFTsBetaApi->nfts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| use this to sort the order of responses | [optional] 
 **per_page** | **float**| total results per page &lt;br&gt; Valid values: 1...250 | [optional] 
 **page** | **float**| page through results | [optional] 

### Return type

[**NFTList**](NFTList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all NFTs categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfts_markets**
> List[NFTsMarketsInner] nfts_markets(asset_platform_id=asset_platform_id, order=order, per_page=per_page, page=page)

💼 NFTs List with Market Data

This endpoint allows you to **query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.nfts_markets_inner import NFTsMarketsInner
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
    api_instance = coingecko_sdk.NFTsBetaApi(api_client)
    asset_platform_id = 'ethereum' # str | filter result by asset platform (blockchain network) <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list) filter=`nft` (optional)
    order = 'order_example' # str | sort results by field <br> Default: `market_cap_usd_desc` (optional)
    per_page = 3.4 # float | total results per page <br> Valid values: any integer between 1 and 250 <br> Default: `100` (optional)
    page = 3.4 # float | page through results <br> Default: `1` (optional)

    try:
        # 💼 NFTs List with Market Data
        api_response = api_instance.nfts_markets(asset_platform_id=asset_platform_id, order=order, per_page=per_page, page=page)
        print("The response of NFTsBetaApi->nfts_markets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->nfts_markets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_platform_id** | **str**| filter result by asset platform (blockchain network) &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list) filter&#x3D;&#x60;nft&#x60; | [optional] 
 **order** | **str**| sort results by field &lt;br&gt; Default: &#x60;market_cap_usd_desc&#x60; | [optional] 
 **per_page** | **float**| total results per page &lt;br&gt; Valid values: any integer between 1 and 250 &lt;br&gt; Default: &#x60;100&#x60; | [optional] 
 **page** | **float**| page through results &lt;br&gt; Default: &#x60;1&#x60; | [optional] 

### Return type

[**List[NFTsMarketsInner]**](NFTsMarketsInner.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all NFTs markets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

