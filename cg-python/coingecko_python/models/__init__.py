# coding: utf-8

# flake8: noqa
"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from coingecko_python.models.asset_platforms_inner import AssetPlatformsInner
from coingecko_python.models.asset_platforms_inner_image import AssetPlatformsInnerImage
from coingecko_python.models.categories import Categories
from coingecko_python.models.categories_list import CategoriesList
from coingecko_python.models.categories_pools import CategoriesPools
from coingecko_python.models.categories_pools_data_inner import CategoriesPoolsDataInner
from coingecko_python.models.categories_pools_data_inner_attributes import CategoriesPoolsDataInnerAttributes
from coingecko_python.models.categories_pools_data_inner_relationships import CategoriesPoolsDataInnerRelationships
from coingecko_python.models.categories_pools_included_inner import CategoriesPoolsIncludedInner
from coingecko_python.models.categories_pools_included_inner_attributes import CategoriesPoolsIncludedInnerAttributes
from coingecko_python.models.coins_contract_address import CoinsContractAddress
from coingecko_python.models.coins_data_base import CoinsDataBase
from coingecko_python.models.coins_data_base_community_data import CoinsDataBaseCommunityData
from coingecko_python.models.coins_data_base_developer_data import CoinsDataBaseDeveloperData
from coingecko_python.models.coins_data_base_developer_data_code_additions_deletions4_weeks import CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks
from coingecko_python.models.coins_data_base_image import CoinsDataBaseImage
from coingecko_python.models.coins_data_base_links import CoinsDataBaseLinks
from coingecko_python.models.coins_data_base_links_repos_url import CoinsDataBaseLinksReposUrl
from coingecko_python.models.coins_data_base_market_data import CoinsDataBaseMarketData
from coingecko_python.models.coins_data_base_market_data_ath import CoinsDataBaseMarketDataAth
from coingecko_python.models.coins_data_base_market_data_ath_change_percentage import CoinsDataBaseMarketDataAthChangePercentage
from coingecko_python.models.coins_data_base_market_data_ath_date import CoinsDataBaseMarketDataAthDate
from coingecko_python.models.coins_data_base_market_data_atl import CoinsDataBaseMarketDataAtl
from coingecko_python.models.coins_data_base_market_data_atl_change_percentage import CoinsDataBaseMarketDataAtlChangePercentage
from coingecko_python.models.coins_data_base_market_data_atl_date import CoinsDataBaseMarketDataAtlDate
from coingecko_python.models.coins_data_base_market_data_current_price import CoinsDataBaseMarketDataCurrentPrice
from coingecko_python.models.coins_data_base_market_data_fully_diluted_valuation import CoinsDataBaseMarketDataFullyDilutedValuation
from coingecko_python.models.coins_data_base_market_data_high24h import CoinsDataBaseMarketDataHigh24h
from coingecko_python.models.coins_data_base_market_data_low24h import CoinsDataBaseMarketDataLow24h
from coingecko_python.models.coins_data_base_market_data_market_cap import CoinsDataBaseMarketDataMarketCap
from coingecko_python.models.coins_data_base_market_data_market_cap_change24h_in_currency import CoinsDataBaseMarketDataMarketCapChange24hInCurrency
from coingecko_python.models.coins_data_base_market_data_market_cap_change_percentage24h_in_currency import CoinsDataBaseMarketDataMarketCapChangePercentage24hInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage14d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage14dInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage1h_in_currency import CoinsDataBaseMarketDataPriceChangePercentage1hInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage1y_in_currency import CoinsDataBaseMarketDataPriceChangePercentage1yInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage200d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage200dInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage24h_in_currency import CoinsDataBaseMarketDataPriceChangePercentage24hInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage30d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage30dInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage60d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage60dInCurrency
from coingecko_python.models.coins_data_base_market_data_price_change_percentage7d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage7dInCurrency
from coingecko_python.models.coins_data_base_market_data_total_volume import CoinsDataBaseMarketDataTotalVolume
from coingecko_python.models.coins_data_base_tickers_inner import CoinsDataBaseTickersInner
from coingecko_python.models.coins_data_base_tickers_inner_converted_last import CoinsDataBaseTickersInnerConvertedLast
from coingecko_python.models.coins_data_base_tickers_inner_converted_volume import CoinsDataBaseTickersInnerConvertedVolume
from coingecko_python.models.coins_data_base_tickers_inner_market import CoinsDataBaseTickersInnerMarket
from coingecko_python.models.coins_historical_data import CoinsHistoricalData
from coingecko_python.models.coins_historical_data_community_data import CoinsHistoricalDataCommunityData
from coingecko_python.models.coins_historical_data_developer_data import CoinsHistoricalDataDeveloperData
from coingecko_python.models.coins_historical_data_developer_data_code_additions_deletions4_weeks import CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks
from coingecko_python.models.coins_historical_data_image import CoinsHistoricalDataImage
from coingecko_python.models.coins_historical_data_market_data import CoinsHistoricalDataMarketData
from coingecko_python.models.coins_historical_data_market_data_current_price import CoinsHistoricalDataMarketDataCurrentPrice
from coingecko_python.models.coins_historical_data_market_data_market_cap import CoinsHistoricalDataMarketDataMarketCap
from coingecko_python.models.coins_historical_data_market_data_total_volume import CoinsHistoricalDataMarketDataTotalVolume
from coingecko_python.models.coins_historical_data_public_interest_stats import CoinsHistoricalDataPublicInterestStats
from coingecko_python.models.coins_id import CoinsID
from coingecko_python.models.coins_list_inner import CoinsListInner
from coingecko_python.models.coins_list_new_inner import CoinsListNewInner
from coingecko_python.models.coins_market_chart import CoinsMarketChart
from coingecko_python.models.coins_market_chart_range import CoinsMarketChartRange
from coingecko_python.models.coins_markets import CoinsMarkets
from coingecko_python.models.coins_markets_sparkline_in7d import CoinsMarketsSparklineIn7d
from coingecko_python.models.coins_tickers import CoinsTickers
from coingecko_python.models.coins_tickers_tickers_inner import CoinsTickersTickersInner
from coingecko_python.models.coins_tickers_tickers_inner_market import CoinsTickersTickersInnerMarket
from coingecko_python.models.companies_treasury import CompaniesTreasury
from coingecko_python.models.companies_treasury_companies_inner import CompaniesTreasuryCompaniesInner
from coingecko_python.models.derivatives_exchanges import DerivativesExchanges
from coingecko_python.models.derivatives_exchanges_id import DerivativesExchangesID
from coingecko_python.models.derivatives_exchanges_list import DerivativesExchangesList
from coingecko_python.models.derivatives_tickers_list import DerivativesTickersList
from coingecko_python.models.dexes_list import DexesList
from coingecko_python.models.dexes_list_data_inner import DexesListDataInner
from coingecko_python.models.dexes_list_data_inner_attributes import DexesListDataInnerAttributes
from coingecko_python.models.exchange_data import ExchangeData
from coingecko_python.models.exchange_rates import ExchangeRates
from coingecko_python.models.exchange_rates_rates_value import ExchangeRatesRatesValue
from coingecko_python.models.exchange_tickers import ExchangeTickers
from coingecko_python.models.exchanges import Exchanges
from coingecko_python.models.exchanges_list import ExchangesList
from coingecko_python.models.global_data import GlobalData
from coingecko_python.models.global_data_market_cap_percentage import GlobalDataMarketCapPercentage
from coingecko_python.models.global_data_total_market_cap import GlobalDataTotalMarketCap
from coingecko_python.models.global_data_total_volume import GlobalDataTotalVolume
from coingecko_python.models.global_de_fi import GlobalDeFi
from coingecko_python.models.global_de_fi_data import GlobalDeFiData
from coingecko_python.models.global_market_cap_chart import GlobalMarketCapChart
from coingecko_python.models.global_market_cap_chart_market_cap_chart import GlobalMarketCapChartMarketCapChart
from coingecko_python.models.key import Key
from coingecko_python.models.model_global import ModelGlobal
from coingecko_python.models.nft_data import NFTData
from coingecko_python.models.nft_data_ath import NFTDataAth
from coingecko_python.models.nft_data_ath_change_percentage import NFTDataAthChangePercentage
from coingecko_python.models.nft_data_ath_date import NFTDataAthDate
from coingecko_python.models.nft_data_banner_image import NFTDataBannerImage
from coingecko_python.models.nft_data_explorers_inner import NFTDataExplorersInner
from coingecko_python.models.nft_data_floor_price import NFTDataFloorPrice
from coingecko_python.models.nft_data_floor_price14d_percentage_change import NFTDataFloorPrice14dPercentageChange
from coingecko_python.models.nft_data_floor_price1y_percentage_change import NFTDataFloorPrice1yPercentageChange
from coingecko_python.models.nft_data_floor_price24h_percentage_change import NFTDataFloorPrice24hPercentageChange
from coingecko_python.models.nft_data_floor_price30d_percentage_change import NFTDataFloorPrice30dPercentageChange
from coingecko_python.models.nft_data_floor_price60d_percentage_change import NFTDataFloorPrice60dPercentageChange
from coingecko_python.models.nft_data_floor_price7d_percentage_change import NFTDataFloorPrice7dPercentageChange
from coingecko_python.models.nft_data_image import NFTDataImage
from coingecko_python.models.nft_data_links import NFTDataLinks
from coingecko_python.models.nft_data_market_cap import NFTDataMarketCap
from coingecko_python.models.nft_data_market_cap24h_percentage_change import NFTDataMarketCap24hPercentageChange
from coingecko_python.models.nft_data_volume24h import NFTDataVolume24h
from coingecko_python.models.nft_data_volume24h_percentage_change import NFTDataVolume24hPercentageChange
from coingecko_python.models.nft_list import NFTList
from coingecko_python.models.nft_market_chart import NFTMarketChart
from coingecko_python.models.nft_tickers import NFTTickers
from coingecko_python.models.nft_tickers_tickers_inner import NFTTickersTickersInner
from coingecko_python.models.nfts_markets_inner import NFTsMarketsInner
from coingecko_python.models.nfts_markets_inner_floor_price24h_percentage_change import NFTsMarketsInnerFloorPrice24hPercentageChange
from coingecko_python.models.networks_list import NetworksList
from coingecko_python.models.networks_list_data_inner import NetworksListDataInner
from coingecko_python.models.networks_list_data_inner_attributes import NetworksListDataInnerAttributes
from coingecko_python.models.ohlcv import OHLCV
from coingecko_python.models.ohlcv_data import OHLCVData
from coingecko_python.models.ohlcv_data_attributes import OHLCVDataAttributes
from coingecko_python.models.ohlcv_meta import OHLCVMeta
from coingecko_python.models.ohlcv_meta_base import OHLCVMetaBase
from coingecko_python.models.onchain_categories_list import OnchainCategoriesList
from coingecko_python.models.onchain_categories_list_data_inner import OnchainCategoriesListDataInner
from coingecko_python.models.onchain_categories_list_data_inner_attributes import OnchainCategoriesListDataInnerAttributes
from coingecko_python.models.onchain_categories_list_data_inner_attributes_volume_change_percentage import OnchainCategoriesListDataInnerAttributesVolumeChangePercentage
from coingecko_python.models.onchain_simple_price import OnchainSimplePrice
from coingecko_python.models.onchain_simple_price_data import OnchainSimplePriceData
from coingecko_python.models.onchain_simple_price_data_attributes import OnchainSimplePriceDataAttributes
from coingecko_python.models.ping import Ping
from coingecko_python.models.pool import Pool
from coingecko_python.models.pool_data_inner import PoolDataInner
from coingecko_python.models.pool_data_inner_attributes import PoolDataInnerAttributes
from coingecko_python.models.pool_data_inner_attributes_price_change_percentage import PoolDataInnerAttributesPriceChangePercentage
from coingecko_python.models.pool_data_inner_attributes_transactions import PoolDataInnerAttributesTransactions
from coingecko_python.models.pool_data_inner_attributes_transactions_m5 import PoolDataInnerAttributesTransactionsM5
from coingecko_python.models.pool_data_inner_relationships import PoolDataInnerRelationships
from coingecko_python.models.pool_data_inner_relationships_base_token import PoolDataInnerRelationshipsBaseToken
from coingecko_python.models.pool_data_inner_relationships_base_token_data import PoolDataInnerRelationshipsBaseTokenData
from coingecko_python.models.pool_included_inner import PoolIncludedInner
from coingecko_python.models.pool_included_inner_attributes import PoolIncludedInnerAttributes
from coingecko_python.models.pool_info import PoolInfo
from coingecko_python.models.pool_info_data_inner import PoolInfoDataInner
from coingecko_python.models.pool_info_data_inner_attributes import PoolInfoDataInnerAttributes
from coingecko_python.models.pool_info_data_inner_attributes_transactions import PoolInfoDataInnerAttributesTransactions
from coingecko_python.models.pool_info_data_inner_attributes_volume_usd import PoolInfoDataInnerAttributesVolumeUsd
from coingecko_python.models.pool_tokens_info import PoolTokensInfo
from coingecko_python.models.search import Search
from coingecko_python.models.search_categories_inner import SearchCategoriesInner
from coingecko_python.models.search_coins_inner import SearchCoinsInner
from coingecko_python.models.search_exchanges_inner import SearchExchangesInner
from coingecko_python.models.search_nfts_inner import SearchNftsInner
from coingecko_python.models.simple_price import SimplePrice
from coingecko_python.models.simple_token_price import SimpleTokenPrice
from coingecko_python.models.token import Token
from coingecko_python.models.token_data import TokenData
from coingecko_python.models.token_data_attributes import TokenDataAttributes
from coingecko_python.models.token_data_attributes_volume_usd import TokenDataAttributesVolumeUsd
from coingecko_python.models.token_data_relationships import TokenDataRelationships
from coingecko_python.models.token_data_relationships_top_pools import TokenDataRelationshipsTopPools
from coingecko_python.models.token_included_inner import TokenIncludedInner
from coingecko_python.models.token_included_inner_attributes import TokenIncludedInnerAttributes
from coingecko_python.models.token_included_inner_relationships import TokenIncludedInnerRelationships
from coingecko_python.models.token_info import TokenInfo
from coingecko_python.models.token_info_data import TokenInfoData
from coingecko_python.models.token_info_data_attributes import TokenInfoDataAttributes
from coingecko_python.models.token_info_data_attributes_holders import TokenInfoDataAttributesHolders
from coingecko_python.models.token_info_data_attributes_holders_distribution_percentage import TokenInfoDataAttributesHoldersDistributionPercentage
from coingecko_python.models.token_info_recently_updated import TokenInfoRecentlyUpdated
from coingecko_python.models.token_lists import TokenLists
from coingecko_python.models.token_lists_tokens_inner import TokenListsTokensInner
from coingecko_python.models.top_gainers_losers_inner import TopGainersLosersInner
from coingecko_python.models.trades import Trades
from coingecko_python.models.trades_data_inner import TradesDataInner
from coingecko_python.models.trades_data_inner_attributes import TradesDataInnerAttributes
from coingecko_python.models.trending_search import TrendingSearch
from coingecko_python.models.trending_search_categories_inner import TrendingSearchCategoriesInner
from coingecko_python.models.trending_search_categories_inner_data import TrendingSearchCategoriesInnerData
from coingecko_python.models.trending_search_categories_inner_data_market_cap_change_percentage24h import TrendingSearchCategoriesInnerDataMarketCapChangePercentage24h
from coingecko_python.models.trending_search_coins_inner import TrendingSearchCoinsInner
from coingecko_python.models.trending_search_coins_inner_data import TrendingSearchCoinsInnerData
from coingecko_python.models.trending_search_coins_inner_data_price_change_percentage24h import TrendingSearchCoinsInnerDataPriceChangePercentage24h
from coingecko_python.models.trending_search_nfts_inner import TrendingSearchNftsInner
from coingecko_python.models.trending_search_nfts_inner_data import TrendingSearchNftsInnerData
