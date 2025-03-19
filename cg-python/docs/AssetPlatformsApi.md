# coingecko_sdk.AssetPlatformsApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_platforms_list**](AssetPlatformsApi.md#asset_platforms_list) | **GET** /asset_platforms | Asset Platforms List (ID Map)
[**token_lists**](AssetPlatformsApi.md#token_lists) | **GET** /token_lists/{asset_platform_id}/all.json | 👑 Token Lists by Asset Platform ID


# **asset_platforms_list**
> List[AssetPlatformsInner] asset_platforms_list(filter=filter)

Asset Platforms List (ID Map)

This endpoint allows you to **query all the asset platforms on CoinGecko**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.asset_platforms_inner import AssetPlatformsInner
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
    api_instance = coingecko_sdk.AssetPlatformsApi(api_client)
    filter = 'filter_example' # str | apply relevant filters to results (optional)

    try:
        # Asset Platforms List (ID Map)
        api_response = api_instance.asset_platforms_list(filter=filter)
        print("The response of AssetPlatformsApi->asset_platforms_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPlatformsApi->asset_platforms_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| apply relevant filters to results | [optional] 

### Return type

[**List[AssetPlatformsInner]**](AssetPlatformsInner.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all asset platforms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_lists**
> TokenLists token_lists(asset_platform_id)

👑 Token Lists by Asset Platform ID

This endpoint allows you to **get full list of tokens of a blockchain network (asset platform) that is supported by [Ethereum token list standard](https://tokenlists.org/)**

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import coingecko_sdk
from coingecko_sdk.models.token_lists import TokenLists
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
    api_instance = coingecko_sdk.AssetPlatformsApi(api_client)
    asset_platform_id = 'ethereum' # str | asset platform ID <br> *refers to [`/asset_platforms`](/reference/asset-platforms-list)

    try:
        # 👑 Token Lists by Asset Platform ID
        api_response = api_instance.token_lists(asset_platform_id)
        print("The response of AssetPlatformsApi->token_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPlatformsApi->token_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_platform_id** | **str**| asset platform ID &lt;br&gt; *refers to [&#x60;/asset_platforms&#x60;](/reference/asset-platforms-list) | 

### Return type

[**TokenLists**](TokenLists.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all tokens on CoinGecko based on asset platform ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

