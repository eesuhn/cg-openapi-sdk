# CompaniesTreasury


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_holdings** | **float** | total btc/eth holdings of companies | [optional] 
**total_value_usd** | **float** | total btc/eth holdings value in usd | [optional] 
**market_cap_dominance** | **float** | market cap dominance | [optional] 
**companies** | [**List[CompaniesTreasuryCompaniesInner]**](CompaniesTreasuryCompaniesInner.md) |  | [optional] 

## Example

```python
from coingecko_python.models.companies_treasury import CompaniesTreasury

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesTreasury from a JSON string
companies_treasury_instance = CompaniesTreasury.from_json(json)
# print the JSON string representation of the object
print(CompaniesTreasury.to_json())

# convert the object into a dict
companies_treasury_dict = companies_treasury_instance.to_dict()
# create an instance of CompaniesTreasury from a dict
companies_treasury_from_dict = CompaniesTreasury.from_dict(companies_treasury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


