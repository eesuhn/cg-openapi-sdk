# coingecko_sdk.PoolsApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**latest_pools_list**](PoolsApi.md#latest_pools_list) | **GET** /onchain/networks/new_pools | New Pools List
[**latest_pools_network**](PoolsApi.md#latest_pools_network) | **GET** /onchain/networks/{network}/new_pools | New Pools by Network
[**pool_address**](PoolsApi.md#pool_address) | **GET** /onchain/networks/{network}/pools/{address} | Specific Pool Data by Pool Address
[**pools_addresses**](PoolsApi.md#pools_addresses) | **GET** /onchain/networks/{network}/pools/multi/{addresses} | Multiple Pools Data by Pool Addresses
[**pools_megafilter**](PoolsApi.md#pools_megafilter) | **GET** /onchain/pools/megafilter | 🔥 Megafilter for Pools
[**search_pools**](PoolsApi.md#search_pools) | **GET** /onchain/search/pools | Search Pools
[**top_pools_dex**](PoolsApi.md#top_pools_dex) | **GET** /onchain/networks/{network}/dexes/{dex}/pools | Top Pools by Dex
[**top_pools_network**](PoolsApi.md#top_pools_network) | **GET** /onchain/networks/{network}/pools | Top Pools by Network
[**trending_pools_list**](PoolsApi.md#trending_pools_list) | **GET** /onchain/networks/trending_pools | Trending Pools List
[**trending_pools_network**](PoolsApi.md#trending_pools_network) | **GET** /onchain/networks/{network}/trending_pools | Trending Pools by Network


# **latest_pools_list**
> Pool latest_pools_list(include=include, page=page)

New Pools List

This endpoint allows you to **query all the latest pools across all networks on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex`, `network` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)

    try:
        # New Pools List
        api_response = api_instance.latest_pools_list(include=include, page=page)
        print("The response of PoolsApi->latest_pools_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->latest_pools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60;, &#x60;network&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 

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
**200** | Get latest pools across all networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_pools_network**
> Pool latest_pools_network(network, include=include, page=page)

New Pools by Network

This endpoint allows you to **query all the latest pools based on provided network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)

    try:
        # New Pools by Network
        api_response = api_instance.latest_pools_network(network, include=include, page=page)
        print("The response of PoolsApi->latest_pools_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->latest_pools_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 

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
**200** | Get latest pools on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pool_address**
> PoolInfo pool_address(network, address, include=include)

Specific Pool Data by Pool Address

This endpoint allows you to **query the specific pool based on the provided network and pool address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool_info import PoolInfo
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    address = '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' # str | pool address
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)

    try:
        # Specific Pool Data by Pool Address
        api_response = api_instance.pool_address(network, address, include=include)
        print("The response of PoolsApi->pool_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->pool_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **address** | **str**| pool address | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 

### Return type

[**PoolInfo**](PoolInfo.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get specific pool on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pools_addresses**
> PoolInfo pools_addresses(network, addresses, include=include)

Multiple Pools Data by Pool Addresses

This endpoint allows you to **query multiple pools based on the provided network and pool address**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool_info import PoolInfo
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    addresses = '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' # str | pool contract address, comma-separated if more than one pool contract address
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)

    try:
        # Multiple Pools Data by Pool Addresses
        api_response = api_instance.pools_addresses(network, addresses, include=include)
        print("The response of PoolsApi->pools_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->pools_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **addresses** | **str**| pool contract address, comma-separated if more than one pool contract address | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 

### Return type

[**PoolInfo**](PoolInfo.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get multiple pools on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pools_megafilter**
> Pool pools_megafilter(include=include, page=page, networks=networks, dexes=dexes, sort=sort, fdv_usd_min=fdv_usd_min, fdv_usd_max=fdv_usd_max, reserve_in_usd_min=reserve_in_usd_min, reserve_in_usd_max=reserve_in_usd_max, h24_volume_usd_min=h24_volume_usd_min, h24_volume_usd_max=h24_volume_usd_max, pool_created_hour_min=pool_created_hour_min, pool_created_hour_max=pool_created_hour_max, tx_count_min=tx_count_min, tx_count_max=tx_count_max, tx_count_duration=tx_count_duration, buys_min=buys_min, buys_max=buys_max, buys_duration=buys_duration, sells_min=sells_min, sells_max=sells_max, sells_duration=sells_duration, checks=checks, buy_tax_percentage_min=buy_tax_percentage_min, buy_tax_percentage_max=buy_tax_percentage_max, sell_tax_percentage_min=sell_tax_percentage_min, sell_tax_percentage_max=sell_tax_percentage_max)

🔥 Megafilter for Pools

This endpoint allows you to **query pools based on various filters across all networks on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex`, `network` (optional)
    page = 1 # int | page through results <br> Default value: 1 (optional) (default to 1)
    networks = 'networks_example' # str | filter pools by networks, comma-separated if more than one <br> Network ID refers to [/networks](/reference/networks-list) (optional)
    dexes = 'dexes_example' # str | filter pools by DEXes, comma-separated if more than one <br> DEX ID refers to [/networks/{network}/dexes](/reference/dexes-list) (optional)
    sort = h6_trending # str | sort the pools by field <br> Default value: h6_trending (optional) (default to h6_trending)
    fdv_usd_min = 3.4 # float | minimum fully diluted value in USD (optional)
    fdv_usd_max = 3.4 # float | maximum fully diluted value in USD (optional)
    reserve_in_usd_min = 3.4 # float | minimum reserve in USD (optional)
    reserve_in_usd_max = 3.4 # float | maximum reserve in USD (optional)
    h24_volume_usd_min = 3.4 # float | minimum 24hr volume in USD (optional)
    h24_volume_usd_max = 3.4 # float | maximum 24hr volume in USD (optional)
    pool_created_hour_min = 3.4 # float | minimum pool age in hours (optional)
    pool_created_hour_max = 3.4 # float | maximum pool age in hours (optional)
    tx_count_min = 56 # int | minimum transaction count (optional)
    tx_count_max = 56 # int | maximum transaction count (optional)
    tx_count_duration = 24h # str | duration for transaction count metric <br> Default value: 24h (optional) (default to 24h)
    buys_min = 56 # int | minimum number of buy transactions (optional)
    buys_max = 56 # int | maximum number of buy transactions (optional)
    buys_duration = 24h # str | duration for buy transactions metric <br> Default value: 24h (optional) (default to 24h)
    sells_min = 56 # int | minimum number of sell transactions (optional)
    sells_max = 56 # int | maximum number of sell transactions (optional)
    sells_duration = 24h # str | duration for sell transactions metric <br> Default value: 24h (optional) (default to 24h)
    checks = 'no_honeypot' # str | filter options for various checks, comma-separated if more than one <br> Available values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social` (optional)
    buy_tax_percentage_min = 3.4 # float | minimum buy tax percentage (optional)
    buy_tax_percentage_max = 3.4 # float | maximum buy tax percentage (optional)
    sell_tax_percentage_min = 3.4 # float | minimum sell tax percentage (optional)
    sell_tax_percentage_max = 3.4 # float | maximum sell tax percentage (optional)

    try:
        # 🔥 Megafilter for Pools
        api_response = api_instance.pools_megafilter(include=include, page=page, networks=networks, dexes=dexes, sort=sort, fdv_usd_min=fdv_usd_min, fdv_usd_max=fdv_usd_max, reserve_in_usd_min=reserve_in_usd_min, reserve_in_usd_max=reserve_in_usd_max, h24_volume_usd_min=h24_volume_usd_min, h24_volume_usd_max=h24_volume_usd_max, pool_created_hour_min=pool_created_hour_min, pool_created_hour_max=pool_created_hour_max, tx_count_min=tx_count_min, tx_count_max=tx_count_max, tx_count_duration=tx_count_duration, buys_min=buys_min, buys_max=buys_max, buys_duration=buys_duration, sells_min=sells_min, sells_max=sells_max, sells_duration=sells_duration, checks=checks, buy_tax_percentage_min=buy_tax_percentage_min, buy_tax_percentage_max=buy_tax_percentage_max, sell_tax_percentage_min=sell_tax_percentage_min, sell_tax_percentage_max=sell_tax_percentage_max)
        print("The response of PoolsApi->pools_megafilter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->pools_megafilter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60;, &#x60;network&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] [default to 1]
 **networks** | **str**| filter pools by networks, comma-separated if more than one &lt;br&gt; Network ID refers to [/networks](/reference/networks-list) | [optional] 
 **dexes** | **str**| filter pools by DEXes, comma-separated if more than one &lt;br&gt; DEX ID refers to [/networks/{network}/dexes](/reference/dexes-list) | [optional] 
 **sort** | **str**| sort the pools by field &lt;br&gt; Default value: h6_trending | [optional] [default to h6_trending]
 **fdv_usd_min** | **float**| minimum fully diluted value in USD | [optional] 
 **fdv_usd_max** | **float**| maximum fully diluted value in USD | [optional] 
 **reserve_in_usd_min** | **float**| minimum reserve in USD | [optional] 
 **reserve_in_usd_max** | **float**| maximum reserve in USD | [optional] 
 **h24_volume_usd_min** | **float**| minimum 24hr volume in USD | [optional] 
 **h24_volume_usd_max** | **float**| maximum 24hr volume in USD | [optional] 
 **pool_created_hour_min** | **float**| minimum pool age in hours | [optional] 
 **pool_created_hour_max** | **float**| maximum pool age in hours | [optional] 
 **tx_count_min** | **int**| minimum transaction count | [optional] 
 **tx_count_max** | **int**| maximum transaction count | [optional] 
 **tx_count_duration** | **str**| duration for transaction count metric &lt;br&gt; Default value: 24h | [optional] [default to 24h]
 **buys_min** | **int**| minimum number of buy transactions | [optional] 
 **buys_max** | **int**| maximum number of buy transactions | [optional] 
 **buys_duration** | **str**| duration for buy transactions metric &lt;br&gt; Default value: 24h | [optional] [default to 24h]
 **sells_min** | **int**| minimum number of sell transactions | [optional] 
 **sells_max** | **int**| maximum number of sell transactions | [optional] 
 **sells_duration** | **str**| duration for sell transactions metric &lt;br&gt; Default value: 24h | [optional] [default to 24h]
 **checks** | **str**| filter options for various checks, comma-separated if more than one &lt;br&gt; Available values: &#x60;no_honeypot&#x60;, &#x60;good_gt_score&#x60;, &#x60;on_coingecko&#x60;, &#x60;has_social&#x60; | [optional] 
 **buy_tax_percentage_min** | **float**| minimum buy tax percentage | [optional] 
 **buy_tax_percentage_max** | **float**| maximum buy tax percentage | [optional] 
 **sell_tax_percentage_min** | **float**| minimum sell tax percentage | [optional] 
 **sell_tax_percentage_max** | **float**| maximum sell tax percentage | [optional] 

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
**200** | TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_pools**
> Pool search_pools(query=query, network=network, include=include, page=page)

Search Pools

This endpoint allows you to **search for pools on a network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    query = 'weth' # str | search query (optional)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list) (optional)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)

    try:
        # Search Pools
        api_response = api_instance.search_pools(query=query, network=network, include=include, page=page)
        print("The response of PoolsApi->search_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->search_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search query | [optional] 
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | [optional] 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 

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
**200** | Search for pools on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_pools_dex**
> Pool top_pools_dex(network, dex, include=include, page=page, sort=sort)

Top Pools by Dex

This endpoint allows you to **query all the top pools based on the provided network and decentralized exchange (DEX)**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    dex = 'sushiswap' # str | DEX ID <br> *refers to [/networks/{network}/dexes](/reference/dexes-list)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)
    sort = 'sort_example' # str | sort the pools by field <br> Default value: h24_tx_count_desc (optional)

    try:
        # Top Pools by Dex
        api_response = api_instance.top_pools_dex(network, dex, include=include, page=page, sort=sort)
        print("The response of PoolsApi->top_pools_dex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->top_pools_dex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **dex** | **str**| DEX ID &lt;br&gt; *refers to [/networks/{network}/dexes](/reference/dexes-list) | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 
 **sort** | **str**| sort the pools by field &lt;br&gt; Default value: h24_tx_count_desc | [optional] 

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
**200** | Get top pools on a network&#39;s DEX |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_pools_network**
> Pool top_pools_network(network, include=include, page=page, sort=sort)

Top Pools by Network

This endpoint allows you to **query all the top pools based on the provided network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)
    sort = 'sort_example' # str | sort the pools by field <br> Default value: h24_tx_count_desc (optional)

    try:
        # Top Pools by Network
        api_response = api_instance.top_pools_network(network, include=include, page=page, sort=sort)
        print("The response of PoolsApi->top_pools_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->top_pools_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 
 **sort** | **str**| sort the pools by field &lt;br&gt; Default value: h24_tx_count_desc | [optional] 

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
**200** | Get top pools on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_pools_list**
> Pool trending_pools_list(include=include, page=page, duration=duration)

Trending Pools List

This endpoint allows you to **query all the trending pools across all networks on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex`, `network`. <br> Example: `base_token` or `base_token,dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)
    duration = 56 # int | duration to sort trending list by <br> Default value: 24h (optional)

    try:
        # Trending Pools List
        api_response = api_instance.trending_pools_list(include=include, page=page, duration=duration)
        print("The response of PoolsApi->trending_pools_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->trending_pools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60;, &#x60;network&#x60;. &lt;br&gt; Example: &#x60;base_token&#x60; or &#x60;base_token,dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 
 **duration** | **int**| duration to sort trending list by &lt;br&gt; Default value: 24h | [optional] 

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
**200** | Get trending pools across all networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_pools_network**
> Pool trending_pools_network(network, include=include, page=page, duration=duration)

Trending Pools by Network

This endpoint allows you to **query the trending pools based on the provided network**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.pool import Pool
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
    api_instance = coingecko_sdk.PoolsApi(api_client)
    network = 'eth' # str | network ID <br> *refers to [/networks](/reference/networks-list)
    include = 'base_token' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex` (optional)
    page = 56 # int | page through results <br> Default value: 1 (optional)
    duration = 56 # int | duration to sort trending list by <br> Default value: 24h (optional)

    try:
        # Trending Pools by Network
        api_response = api_instance.trending_pools_network(network, include=include, page=page, duration=duration)
        print("The response of PoolsApi->trending_pools_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->trending_pools_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| network ID &lt;br&gt; *refers to [/networks](/reference/networks-list) | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: 1 | [optional] 
 **duration** | **int**| duration to sort trending list by &lt;br&gt; Default value: 24h | [optional] 

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
**200** | Get trending pools on a network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

