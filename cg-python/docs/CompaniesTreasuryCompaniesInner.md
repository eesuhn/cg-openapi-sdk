# CompaniesTreasuryCompaniesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | company name | [optional] 
**symbol** | **str** | company symbol | [optional] 
**country** | **str** | company incorporated country | [optional] 
**total_holdings** | **float** | total btc/eth holdings of company | [optional] 
**total_entry_value_usd** | **float** | total entry value in usd | [optional] 
**total_current_value_usd** | **float** | total current value of btc/eth holdings in usd | [optional] 
**percentage_of_total_supply** | **float** | percentage of total btc/eth supply | [optional] 

## Example

```python
from coingecko_sdk.models.companies_treasury_companies_inner import CompaniesTreasuryCompaniesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesTreasuryCompaniesInner from a JSON string
companies_treasury_companies_inner_instance = CompaniesTreasuryCompaniesInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesTreasuryCompaniesInner.to_json())

# convert the object into a dict
companies_treasury_companies_inner_dict = companies_treasury_companies_inner_instance.to_dict()
# create an instance of CompaniesTreasuryCompaniesInner from a dict
companies_treasury_companies_inner_from_dict = CompaniesTreasuryCompaniesInner.from_dict(companies_treasury_companies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


