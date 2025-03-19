# PoolInfoDataInnerAttributesTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m5** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 
**m15** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 
**m30** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 
**h1** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 
**h6** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 
**h24** | [**PoolDataInnerAttributesTransactionsM5**](PoolDataInnerAttributesTransactionsM5.md) |  | [optional] 

## Example

```python
from coingecko-sdk.models.pool_info_data_inner_attributes_transactions import PoolInfoDataInnerAttributesTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfoDataInnerAttributesTransactions from a JSON string
pool_info_data_inner_attributes_transactions_instance = PoolInfoDataInnerAttributesTransactions.from_json(json)
# print the JSON string representation of the object
print(PoolInfoDataInnerAttributesTransactions.to_json())

# convert the object into a dict
pool_info_data_inner_attributes_transactions_dict = pool_info_data_inner_attributes_transactions_instance.to_dict()
# create an instance of PoolInfoDataInnerAttributesTransactions from a dict
pool_info_data_inner_attributes_transactions_from_dict = PoolInfoDataInnerAttributesTransactions.from_dict(pool_info_data_inner_attributes_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


