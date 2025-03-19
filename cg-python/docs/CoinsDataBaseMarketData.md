# CoinsDataBaseMarketData

coin market data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_price** | [**CoinsDataBaseMarketDataCurrentPrice**](CoinsDataBaseMarketDataCurrentPrice.md) |  | [optional] 
**total_value_locked** | **float** | total value locked | [optional] 
**mcap_to_tvl_ratio** | **float** | market cap to total value locked ratio | [optional] 
**fdv_to_tvl_ratio** | **float** | fully diluted valuation to total value locked ratio | [optional] 
**roi** | **float** | coin return on investment | [optional] 
**ath** | [**CoinsDataBaseMarketDataAth**](CoinsDataBaseMarketDataAth.md) |  | [optional] 
**ath_change_percentage** | [**CoinsDataBaseMarketDataAthChangePercentage**](CoinsDataBaseMarketDataAthChangePercentage.md) |  | [optional] 
**ath_date** | [**CoinsDataBaseMarketDataAthDate**](CoinsDataBaseMarketDataAthDate.md) |  | [optional] 
**atl** | [**CoinsDataBaseMarketDataAtl**](CoinsDataBaseMarketDataAtl.md) |  | [optional] 
**atl_change_percentage** | [**CoinsDataBaseMarketDataAtlChangePercentage**](CoinsDataBaseMarketDataAtlChangePercentage.md) |  | [optional] 
**atl_date** | [**CoinsDataBaseMarketDataAtlDate**](CoinsDataBaseMarketDataAtlDate.md) |  | [optional] 
**market_cap** | [**CoinsDataBaseMarketDataMarketCap**](CoinsDataBaseMarketDataMarketCap.md) |  | [optional] 
**market_cap_rank** | **float** | coin rank by market cap | [optional] 
**fully_diluted_valuation** | [**CoinsDataBaseMarketDataFullyDilutedValuation**](CoinsDataBaseMarketDataFullyDilutedValuation.md) |  | [optional] 
**market_cap_fdv_ratio** | **float** | market cap to fully diluted valuation ratio | [optional] 
**total_volume** | [**CoinsDataBaseMarketDataTotalVolume**](CoinsDataBaseMarketDataTotalVolume.md) |  | [optional] 
**high_24h** | [**CoinsDataBaseMarketDataHigh24h**](CoinsDataBaseMarketDataHigh24h.md) |  | [optional] 
**low_24h** | [**CoinsDataBaseMarketDataLow24h**](CoinsDataBaseMarketDataLow24h.md) |  | [optional] 
**price_change_24h** | **float** | coin 24hr price change in currency | [optional] 
**price_change_percentage_24h** | **float** | coin 24hr price change in percentage | [optional] 
**price_change_percentage_7d** | **float** | coin 7d price change in percentage | [optional] 
**price_change_percentage_14d** | **float** | coin 14d price change in percentage | [optional] 
**price_change_percentage_30d** | **float** | coin 30d price change in percentage | [optional] 
**price_change_percentage_60d** | **float** | coin 60d price change in percentage | [optional] 
**price_change_percentage_200d** | **float** | coin 200d price change in percentage | [optional] 
**price_change_percentage_1y** | **float** | coin 1y price change in percentage | [optional] 
**market_cap_change_24h** | **float** | coin 24hr market cap change in currency | [optional] 
**market_cap_change_percentage_24h** | **float** | coin 24hr market cap change in percentage | [optional] 
**price_change_percentage_1h_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage1hInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage1hInCurrency.md) |  | [optional] 
**price_change_percentage_24h_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage24hInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage24hInCurrency.md) |  | [optional] 
**price_change_percentage_7d_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage7dInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage7dInCurrency.md) |  | [optional] 
**price_change_percentage_14d_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage14dInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage14dInCurrency.md) |  | [optional] 
**price_change_percentage_30d_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage30dInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage30dInCurrency.md) |  | [optional] 
**price_change_percentage_60d_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage60dInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage60dInCurrency.md) |  | [optional] 
**price_change_percentage_200d_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage200dInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage200dInCurrency.md) |  | [optional] 
**price_change_percentage_1y_in_currency** | [**CoinsDataBaseMarketDataPriceChangePercentage1yInCurrency**](CoinsDataBaseMarketDataPriceChangePercentage1yInCurrency.md) |  | [optional] 
**market_cap_change_24h_in_currency** | [**CoinsDataBaseMarketDataMarketCapChange24hInCurrency**](CoinsDataBaseMarketDataMarketCapChange24hInCurrency.md) |  | [optional] 
**market_cap_change_percentage_24h_in_currency** | [**CoinsDataBaseMarketDataMarketCapChangePercentage24hInCurrency**](CoinsDataBaseMarketDataMarketCapChangePercentage24hInCurrency.md) |  | [optional] 
**total_supply** | **float** | coin total supply | [optional] 
**max_supply** | **float** | coin max supply | [optional] 
**circulating_supply** | **float** | coin circulating supply | [optional] 
**last_updated** | **datetime** | coin market data last updated timestamp | [optional] 

## Example

```python
from coingecko-sdk.models.coins_data_base_market_data import CoinsDataBaseMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsDataBaseMarketData from a JSON string
coins_data_base_market_data_instance = CoinsDataBaseMarketData.from_json(json)
# print the JSON string representation of the object
print(CoinsDataBaseMarketData.to_json())

# convert the object into a dict
coins_data_base_market_data_dict = coins_data_base_market_data_instance.to_dict()
# create an instance of CoinsDataBaseMarketData from a dict
coins_data_base_market_data_from_dict = CoinsDataBaseMarketData.from_dict(coins_data_base_market_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


