# coingecko-sdk.TokensApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pool_token_info_contract_address**](TokensApi.md#pool_token_info_contract_address) | **GET** /onchain/networks/{network}/pools/{pool_address}/info | Pool Tokens Info by Pool Address
[**token_data_contract_address**](TokensApi.md#token_data_contract_address) | **GET** /onchain/networks/{network}/tokens/{address} | Token Data by Token Address
[**token_info_contract_address**](TokensApi.md#token_info_contract_address) | **GET** /onchain/networks/{network}/tokens/{address}/info | Token Info by Token Address
[**tokens_data_contract_addresses**](TokensApi.md#tokens_data_contract_addresses) | **GET** /onchain/networks/{network}/tokens/multi/{addresses} | Tokens Data by Token Addresses
[**tokens_info_recent_updated**](TokensApi.md#tokens_info_recent_updated) | **GET** /onchain/tokens/info_recently_updated | Most Recently Updated Tokens List
[**top_pools_contract_address**](TokensApi.md#top_pools_contract_address) | **GET** /onchain/networks/{network}/tokens/{token_address}/pools | Top Pools by Token Address


# **pool_token_info_contract_address**
> PoolTokensInfo pool_token_info_contract_address(network, pool_address)

Pool Tokens Info by Pool Address

This endpoint allows you to **query pool metadata (base and quote  token details, image, socials, websites, description, contract  address, etc.) based on a provided pool contract address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.pool_tokens_info import PoolTokensInfo
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    pool_address = '0x06da0fd433c1a5d7a4faa01111c044910a184553' # str | pool contract address

    try:
        # Pool Tokens Info by Pool Address
        api_response = api_instance.pool_token_info_contract_address(network, pool_address)
        print("The response of TokensApi->pool_token_info_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->pool_token_info_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **pool_address** | **str**| pool contract address | 

### Return type

[**PoolTokensInfo**](PoolTokensInfo.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get pool tokens info on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_data_contract_address**
> Token token_data_contract_address(network, address, include=include)

Token Data by Token Address

This endpoint allows you to **query specific token data based on the provided token contract address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.token import Token
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    address = '0xdac17f958d2ee523a2206206994597c13d831ec7' # str | token contract address
    include = 'include_example' # str | attributes to include (optional)

    try:
        # Token Data by Token Address
        api_response = api_instance.token_data_contract_address(network, address, include=include)
        print("The response of TokensApi->token_data_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->token_data_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **address** | **str**| token contract address | 
 **include** | **str**| attributes to include | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get specific token on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_info_contract_address**
> TokenInfo token_info_contract_address(network, address)

Token Info by Token Address

This endpoint allows you to **query token metadata (name, symbol,  CoinGecko ID, image, socials, websites, description, etc.) based  on a provided token contract address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.token_info import TokenInfo
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    address = '0xdac17f958d2ee523a2206206994597c13d831ec7' # str | token contract address

    try:
        # Token Info by Token Address
        api_response = api_instance.token_info_contract_address(network, address)
        print("The response of TokensApi->token_info_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->token_info_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **address** | **str**| token contract address | 

### Return type

[**TokenInfo**](TokenInfo.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get specific token info on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_data_contract_addresses**
> Token tokens_data_contract_addresses(network, addresses, include=include)

Tokens Data by Token Addresses

This endpoint allows you to **query multiple tokens data based on the provided token contract addresses on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.token import Token
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    addresses = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2' # str | token contract address, comma-separated if more than one token contract address
    include = 'include_example' # str | attributes to include (optional)

    try:
        # Tokens Data by Token Addresses
        api_response = api_instance.tokens_data_contract_addresses(network, addresses, include=include)
        print("The response of TokensApi->tokens_data_contract_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->tokens_data_contract_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **addresses** | **str**| token contract address, comma-separated if more than one token contract address | 
 **include** | **str**| attributes to include | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get multiple tokens on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_info_recent_updated**
> TokenInfoRecentlyUpdated tokens_info_recent_updated(include=include, network=network)

Most Recently Updated Tokens List

This endpoint allows you to **query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.token_info_recently_updated import TokenInfoRecentlyUpdated
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    include = 'include_example' # str | Attributes for related resources to include, which will be returned under the top-level 'included' key (optional)
    network = 'eth' # str | filter tokens by provided network <br> *refers to [/networks](/reference/networks-list) (optional)

    try:
        # Most Recently Updated Tokens List
        api_response = api_instance.tokens_info_recent_updated(include=include, network=network)
        print("The response of TokensApi->tokens_info_recent_updated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->tokens_info_recent_updated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Attributes for related resources to include, which will be returned under the top-level &#39;included&#39; key | [optional] 
 **network** | **str**| filter tokens by provided network &lt;br&gt; *refers to [/networks](/reference/networks-list) | [optional] 

### Return type

[**TokenInfoRecentlyUpdated**](TokenInfoRecentlyUpdated.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get 100 tokens info across all networks ordered by most recently updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_pools_contract_address**
> Pool top_pools_contract_address(network, token_address, include=include, page=page, sort=sort)

Top Pools by Token Address

This endpoint allows you to **query top pools based on the provided token contract address on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko-sdk
from coingecko-sdk.models.pool import Pool
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
    api_instance = coingecko-sdk.TokensApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    token_address = '0xdac17f958d2ee523a2206206994597c13d831ec7' # str | token contract address
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)
    sort = 'sort_example' # str | sort the pools by field <br> Default value: h24_volume_usd_liquidity_desc (optional)

    try:
        # Top Pools by Token Address
        api_response = api_instance.top_pools_contract_address(network, token_address, include=include, page=page, sort=sort)
        print("The response of TokensApi->top_pools_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->top_pools_contract_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **token_address** | **str**| token contract address | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 
 **sort** | **str**| sort the pools by field &lt;br&gt; Default value: h24_volume_usd_liquidity_desc | [optional] 

### Return type

[**Pool**](Pool.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get top pools for a token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

