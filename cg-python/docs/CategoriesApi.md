# coingecko_python.CategoriesApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_list**](CategoriesApi.md#categories_list) | **GET** /onchain/categories | Categories List
[**coins_categories**](CategoriesApi.md#coins_categories) | **GET** /coins/categories | Coins Categories List with Market Data
[**coins_categories_list**](CategoriesApi.md#coins_categories_list) | **GET** /coins/categories/list | Coins Categories List (ID Map)
[**pools_category**](CategoriesApi.md#pools_category) | **GET** /onchain/categories/{category_id}/pools | Pools by Category ID


# **categories_list**
> OnchainCategoriesList categories_list(page=page, sort=sort)

Categories List

This endpoint allows you to **query all the supported categories on GeckoTerminal**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.onchain_categories_list import OnchainCategoriesList
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
    api_instance = coingecko_python.CategoriesApi(api_client)
    page = 56 # int | page through results <br> Default value: `1` (optional)
    sort = 'sort_example' # str | sort the categories by field <br> Default value: `h6_volume_percentage_desc` (optional)

    try:
        # Categories List
        api_response = api_instance.categories_list(page=page, sort=sort)
        print("The response of CategoriesApi->categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page through results &lt;br&gt; Default value: &#x60;1&#x60; | [optional] 
 **sort** | **str**| sort the categories by field &lt;br&gt; Default value: &#x60;h6_volume_percentage_desc&#x60; | [optional] 

### Return type

[**OnchainCategoriesList**](OnchainCategoriesList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of supported categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_categories**
> Categories coins_categories(order=order)

Coins Categories List with Market Data

This endpoint allows you to **query all the coins categories with market data (market cap, volume, ...) on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.categories import Categories
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
    api_instance = coingecko_python.CategoriesApi(api_client)
    order = 'order_example' # str | sort results by field, default: market_cap_desc (optional)

    try:
        # Coins Categories List with Market Data
        api_response = api_instance.coins_categories(order=order)
        print("The response of CategoriesApi->coins_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->coins_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| sort results by field, default: market_cap_desc | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all categories with market data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coins_categories_list**
> CategoriesList coins_categories_list()

Coins Categories List (ID Map)

This endpoint allows you to **query all the coins categories on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.categories_list import CategoriesList
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
    api_instance = coingecko_python.CategoriesApi(api_client)

    try:
        # Coins Categories List (ID Map)
        api_response = api_instance.coins_categories_list()
        print("The response of CategoriesApi->coins_categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->coins_categories_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CategoriesList**](CategoriesList.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pools_category**
> CategoriesPools pools_category(category_id, include=include, page=page, sort=sort)

Pools by Category ID

This endpoint allows you to **query all the pools based on the provided category ID**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_python
from coingecko_python.models.categories_pools import CategoriesPools
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
    api_instance = coingecko_python.CategoriesApi(api_client)
    category_id = 'pump-fun' # str | category ID
    include = 'include_example' # str | attributes to include, comma-separated if more than one to include <br> Available values: `base_token`, `quote_token`, `dex`, `network`. <br> Example: `base_token` or `base_token,dex` (optional)
    page = 56 # int | page through results <br> Default value: `1` (optional)
    sort = 'sort_example' # str | sort the pools by field <br> Default value: `pool_created_at_desc` (optional)

    try:
        # Pools by Category ID
        api_response = api_instance.pools_category(category_id, include=include, page=page, sort=sort)
        print("The response of CategoriesApi->pools_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->pools_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| category ID | 
 **include** | **str**| attributes to include, comma-separated if more than one to include &lt;br&gt; Available values: &#x60;base_token&#x60;, &#x60;quote_token&#x60;, &#x60;dex&#x60;, &#x60;network&#x60;. &lt;br&gt; Example: &#x60;base_token&#x60; or &#x60;base_token,dex&#x60; | [optional] 
 **page** | **int**| page through results &lt;br&gt; Default value: &#x60;1&#x60; | [optional] 
 **sort** | **str**| sort the pools by field &lt;br&gt; Default value: &#x60;pool_created_at_desc&#x60; | [optional] 

### Return type

[**CategoriesPools**](CategoriesPools.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get pools by category ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

