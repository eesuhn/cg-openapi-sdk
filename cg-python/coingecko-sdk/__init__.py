# coding: utf-8

# flake8: noqa

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from coingecko-sdk.api.asset_platforms_api import AssetPlatformsApi
from coingecko-sdk.api.categories_api import CategoriesApi
from coingecko-sdk.api.coins_api import CoinsApi
from coingecko-sdk.api.companies_beta_api import CompaniesBetaApi
from coingecko-sdk.api.contract_api import ContractApi
from coingecko-sdk.api.derivatives_api import DerivativesApi
from coingecko-sdk.api.dexes_api import DexesApi
from coingecko-sdk.api.exchange_rates_api import ExchangeRatesApi
from coingecko-sdk.api.exchanges_api import ExchangesApi
from coingecko-sdk.api.global_api import GlobalApi
from coingecko-sdk.api.key_api import KeyApi
from coingecko-sdk.api.nfts_beta_api import NFTsBetaApi
from coingecko-sdk.api.networks_api import NetworksApi
from coingecko-sdk.api.ohlcv_api import OHLCVApi
from coingecko-sdk.api.ping_api import PingApi
from coingecko-sdk.api.pools_api import PoolsApi
from coingecko-sdk.api.search_api import SearchApi
from coingecko-sdk.api.simple_api import SimpleApi
from coingecko-sdk.api.tokens_api import TokensApi
from coingecko-sdk.api.trades_api import TradesApi
from coingecko-sdk.api.trending_api import TrendingApi

# import ApiClient
from coingecko-sdk.api_response import ApiResponse
from coingecko-sdk.api_client import ApiClient
from coingecko-sdk.configuration import Configuration
from coingecko-sdk.exceptions import OpenApiException
from coingecko-sdk.exceptions import ApiTypeError
from coingecko-sdk.exceptions import ApiValueError
from coingecko-sdk.exceptions import ApiKeyError
from coingecko-sdk.exceptions import ApiAttributeError
from coingecko-sdk.exceptions import ApiException

# import models into sdk package
from coingecko-sdk.models.asset_platforms_inner import AssetPlatformsInner
from coingecko-sdk.models.asset_platforms_inner_image import AssetPlatformsInnerImage
from coingecko-sdk.models.categories import Categories
from coingecko-sdk.models.categories_list import CategoriesList
from coingecko-sdk.models.categories_pools import CategoriesPools
from coingecko-sdk.models.categories_pools_data_inner import CategoriesPoolsDataInner
from coingecko-sdk.models.categories_pools_data_inner_attributes import CategoriesPoolsDataInnerAttributes
from coingecko-sdk.models.categories_pools_data_inner_relationships import CategoriesPoolsDataInnerRelationships
from coingecko-sdk.models.categories_pools_included_inner import CategoriesPoolsIncludedInner
from coingecko-sdk.models.categories_pools_included_inner_attributes import CategoriesPoolsIncludedInnerAttributes
from coingecko-sdk.models.coins_contract_address import CoinsContractAddress
from coingecko-sdk.models.coins_data_base import CoinsDataBase
from coingecko-sdk.models.coins_data_base_community_data import CoinsDataBaseCommunityData
from coingecko-sdk.models.coins_data_base_developer_data import CoinsDataBaseDeveloperData
from coingecko-sdk.models.coins_data_base_developer_data_code_additions_deletions4_weeks import CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks
from coingecko-sdk.models.coins_data_base_image import CoinsDataBaseImage
from coingecko-sdk.models.coins_data_base_links import CoinsDataBaseLinks
from coingecko-sdk.models.coins_data_base_links_repos_url import CoinsDataBaseLinksReposUrl
from coingecko-sdk.models.coins_data_base_market_data import CoinsDataBaseMarketData
from coingecko-sdk.models.coins_data_base_market_data_ath import CoinsDataBaseMarketDataAth
from coingecko-sdk.models.coins_data_base_market_data_ath_change_percentage import CoinsDataBaseMarketDataAthChangePercentage
from coingecko-sdk.models.coins_data_base_market_data_ath_date import CoinsDataBaseMarketDataAthDate
from coingecko-sdk.models.coins_data_base_market_data_atl import CoinsDataBaseMarketDataAtl
from coingecko-sdk.models.coins_data_base_market_data_atl_change_percentage import CoinsDataBaseMarketDataAtlChangePercentage
from coingecko-sdk.models.coins_data_base_market_data_atl_date import CoinsDataBaseMarketDataAtlDate
from coingecko-sdk.models.coins_data_base_market_data_current_price import CoinsDataBaseMarketDataCurrentPrice
from coingecko-sdk.models.coins_data_base_market_data_fully_diluted_valuation import CoinsDataBaseMarketDataFullyDilutedValuation
from coingecko-sdk.models.coins_data_base_market_data_high24h import CoinsDataBaseMarketDataHigh24h
from coingecko-sdk.models.coins_data_base_market_data_low24h import CoinsDataBaseMarketDataLow24h
from coingecko-sdk.models.coins_data_base_market_data_market_cap import CoinsDataBaseMarketDataMarketCap
from coingecko-sdk.models.coins_data_base_market_data_market_cap_change24h_in_currency import CoinsDataBaseMarketDataMarketCapChange24hInCurrency
from coingecko-sdk.models.coins_data_base_market_data_market_cap_change_percentage24h_in_currency import CoinsDataBaseMarketDataMarketCapChangePercentage24hInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage14d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage14dInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage1h_in_currency import CoinsDataBaseMarketDataPriceChangePercentage1hInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage1y_in_currency import CoinsDataBaseMarketDataPriceChangePercentage1yInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage200d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage200dInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage24h_in_currency import CoinsDataBaseMarketDataPriceChangePercentage24hInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage30d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage30dInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage60d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage60dInCurrency
from coingecko-sdk.models.coins_data_base_market_data_price_change_percentage7d_in_currency import CoinsDataBaseMarketDataPriceChangePercentage7dInCurrency
from coingecko-sdk.models.coins_data_base_market_data_total_volume import CoinsDataBaseMarketDataTotalVolume
from coingecko-sdk.models.coins_data_base_tickers_inner import CoinsDataBaseTickersInner
from coingecko-sdk.models.coins_data_base_tickers_inner_converted_last import CoinsDataBaseTickersInnerConvertedLast
from coingecko-sdk.models.coins_data_base_tickers_inner_converted_volume import CoinsDataBaseTickersInnerConvertedVolume
from coingecko-sdk.models.coins_data_base_tickers_inner_market import CoinsDataBaseTickersInnerMarket
from coingecko-sdk.models.coins_historical_data import CoinsHistoricalData
from coingecko-sdk.models.coins_historical_data_community_data import CoinsHistoricalDataCommunityData
from coingecko-sdk.models.coins_historical_data_developer_data import CoinsHistoricalDataDeveloperData
from coingecko-sdk.models.coins_historical_data_developer_data_code_additions_deletions4_weeks import CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks
from coingecko-sdk.models.coins_historical_data_image import CoinsHistoricalDataImage
from coingecko-sdk.models.coins_historical_data_market_data import CoinsHistoricalDataMarketData
from coingecko-sdk.models.coins_historical_data_market_data_current_price import CoinsHistoricalDataMarketDataCurrentPrice
from coingecko-sdk.models.coins_historical_data_market_data_market_cap import CoinsHistoricalDataMarketDataMarketCap
from coingecko-sdk.models.coins_historical_data_market_data_total_volume import CoinsHistoricalDataMarketDataTotalVolume
from coingecko-sdk.models.coins_historical_data_public_interest_stats import CoinsHistoricalDataPublicInterestStats
from coingecko-sdk.models.coins_id import CoinsID
from coingecko-sdk.models.coins_list_inner import CoinsListInner
from coingecko-sdk.models.coins_list_new_inner import CoinsListNewInner
from coingecko-sdk.models.coins_market_chart import CoinsMarketChart
from coingecko-sdk.models.coins_market_chart_range import CoinsMarketChartRange
from coingecko-sdk.models.coins_markets import CoinsMarkets
from coingecko-sdk.models.coins_markets_sparkline_in7d import CoinsMarketsSparklineIn7d
from coingecko-sdk.models.coins_tickers import CoinsTickers
from coingecko-sdk.models.coins_tickers_tickers_inner import CoinsTickersTickersInner
from coingecko-sdk.models.coins_tickers_tickers_inner_market import CoinsTickersTickersInnerMarket
from coingecko-sdk.models.companies_treasury import CompaniesTreasury
from coingecko-sdk.models.companies_treasury_companies_inner import CompaniesTreasuryCompaniesInner
from coingecko-sdk.models.derivatives_exchanges import DerivativesExchanges
from coingecko-sdk.models.derivatives_exchanges_id import DerivativesExchangesID
from coingecko-sdk.models.derivatives_exchanges_list import DerivativesExchangesList
from coingecko-sdk.models.derivatives_tickers_list import DerivativesTickersList
from coingecko-sdk.models.dexes_list import DexesList
from coingecko-sdk.models.dexes_list_data_inner import DexesListDataInner
from coingecko-sdk.models.dexes_list_data_inner_attributes import DexesListDataInnerAttributes
from coingecko-sdk.models.exchange_data import ExchangeData
from coingecko-sdk.models.exchange_rates import ExchangeRates
from coingecko-sdk.models.exchange_rates_rates_value import ExchangeRatesRatesValue
from coingecko-sdk.models.exchange_tickers import ExchangeTickers
from coingecko-sdk.models.exchanges import Exchanges
from coingecko-sdk.models.exchanges_list import ExchangesList
from coingecko-sdk.models.global_data import GlobalData
from coingecko-sdk.models.global_data_market_cap_percentage import GlobalDataMarketCapPercentage
from coingecko-sdk.models.global_data_total_market_cap import GlobalDataTotalMarketCap
from coingecko-sdk.models.global_data_total_volume import GlobalDataTotalVolume
from coingecko-sdk.models.global_de_fi import GlobalDeFi
from coingecko-sdk.models.global_de_fi_data import GlobalDeFiData
from coingecko-sdk.models.global_market_cap_chart import GlobalMarketCapChart
from coingecko-sdk.models.global_market_cap_chart_market_cap_chart import GlobalMarketCapChartMarketCapChart
from coingecko-sdk.models.key import Key
from coingecko-sdk.models.model_global import ModelGlobal
from coingecko-sdk.models.nft_data import NFTData
from coingecko-sdk.models.nft_data_ath import NFTDataAth
from coingecko-sdk.models.nft_data_ath_change_percentage import NFTDataAthChangePercentage
from coingecko-sdk.models.nft_data_ath_date import NFTDataAthDate
from coingecko-sdk.models.nft_data_banner_image import NFTDataBannerImage
from coingecko-sdk.models.nft_data_explorers_inner import NFTDataExplorersInner
from coingecko-sdk.models.nft_data_floor_price import NFTDataFloorPrice
from coingecko-sdk.models.nft_data_floor_price14d_percentage_change import NFTDataFloorPrice14dPercentageChange
from coingecko-sdk.models.nft_data_floor_price1y_percentage_change import NFTDataFloorPrice1yPercentageChange
from coingecko-sdk.models.nft_data_floor_price24h_percentage_change import NFTDataFloorPrice24hPercentageChange
from coingecko-sdk.models.nft_data_floor_price30d_percentage_change import NFTDataFloorPrice30dPercentageChange
from coingecko-sdk.models.nft_data_floor_price60d_percentage_change import NFTDataFloorPrice60dPercentageChange
from coingecko-sdk.models.nft_data_floor_price7d_percentage_change import NFTDataFloorPrice7dPercentageChange
from coingecko-sdk.models.nft_data_image import NFTDataImage
from coingecko-sdk.models.nft_data_links import NFTDataLinks
from coingecko-sdk.models.nft_data_market_cap import NFTDataMarketCap
from coingecko-sdk.models.nft_data_market_cap24h_percentage_change import NFTDataMarketCap24hPercentageChange
from coingecko-sdk.models.nft_data_volume24h import NFTDataVolume24h
from coingecko-sdk.models.nft_data_volume24h_percentage_change import NFTDataVolume24hPercentageChange
from coingecko-sdk.models.nft_list import NFTList
from coingecko-sdk.models.nft_market_chart import NFTMarketChart
from coingecko-sdk.models.nft_tickers import NFTTickers
from coingecko-sdk.models.nft_tickers_tickers_inner import NFTTickersTickersInner
from coingecko-sdk.models.nfts_markets_inner import NFTsMarketsInner
from coingecko-sdk.models.nfts_markets_inner_floor_price24h_percentage_change import NFTsMarketsInnerFloorPrice24hPercentageChange
from coingecko-sdk.models.networks_list import NetworksList
from coingecko-sdk.models.networks_list_data_inner import NetworksListDataInner
from coingecko-sdk.models.networks_list_data_inner_attributes import NetworksListDataInnerAttributes
from coingecko-sdk.models.ohlcv import OHLCV
from coingecko-sdk.models.ohlcv_data import OHLCVData
from coingecko-sdk.models.ohlcv_data_attributes import OHLCVDataAttributes
from coingecko-sdk.models.ohlcv_meta import OHLCVMeta
from coingecko-sdk.models.ohlcv_meta_base import OHLCVMetaBase
from coingecko-sdk.models.onchain_categories_list import OnchainCategoriesList
from coingecko-sdk.models.onchain_categories_list_data_inner import OnchainCategoriesListDataInner
from coingecko-sdk.models.onchain_categories_list_data_inner_attributes import OnchainCategoriesListDataInnerAttributes
from coingecko-sdk.models.onchain_categories_list_data_inner_attributes_volume_change_percentage import OnchainCategoriesListDataInnerAttributesVolumeChangePercentage
from coingecko-sdk.models.onchain_simple_price import OnchainSimplePrice
from coingecko-sdk.models.onchain_simple_price_data import OnchainSimplePriceData
from coingecko-sdk.models.onchain_simple_price_data_attributes import OnchainSimplePriceDataAttributes
from coingecko-sdk.models.ping import Ping
from coingecko-sdk.models.pool import Pool
from coingecko-sdk.models.pool_data_inner import PoolDataInner
from coingecko-sdk.models.pool_data_inner_attributes import PoolDataInnerAttributes
from coingecko-sdk.models.pool_data_inner_attributes_price_change_percentage import PoolDataInnerAttributesPriceChangePercentage
from coingecko-sdk.models.pool_data_inner_attributes_transactions import PoolDataInnerAttributesTransactions
from coingecko-sdk.models.pool_data_inner_attributes_transactions_m5 import PoolDataInnerAttributesTransactionsM5
from coingecko-sdk.models.pool_data_inner_relationships import PoolDataInnerRelationships
from coingecko-sdk.models.pool_data_inner_relationships_base_token import PoolDataInnerRelationshipsBaseToken
from coingecko-sdk.models.pool_data_inner_relationships_base_token_data import PoolDataInnerRelationshipsBaseTokenData
from coingecko-sdk.models.pool_included_inner import PoolIncludedInner
from coingecko-sdk.models.pool_included_inner_attributes import PoolIncludedInnerAttributes
from coingecko-sdk.models.pool_info import PoolInfo
from coingecko-sdk.models.pool_info_data_inner import PoolInfoDataInner
from coingecko-sdk.models.pool_info_data_inner_attributes import PoolInfoDataInnerAttributes
from coingecko-sdk.models.pool_info_data_inner_attributes_transactions import PoolInfoDataInnerAttributesTransactions
from coingecko-sdk.models.pool_info_data_inner_attributes_volume_usd import PoolInfoDataInnerAttributesVolumeUsd
from coingecko-sdk.models.pool_tokens_info import PoolTokensInfo
from coingecko-sdk.models.search import Search
from coingecko-sdk.models.search_categories_inner import SearchCategoriesInner
from coingecko-sdk.models.search_coins_inner import SearchCoinsInner
from coingecko-sdk.models.search_exchanges_inner import SearchExchangesInner
from coingecko-sdk.models.search_nfts_inner import SearchNftsInner
from coingecko-sdk.models.simple_price import SimplePrice
from coingecko-sdk.models.simple_token_price import SimpleTokenPrice
from coingecko-sdk.models.token import Token
from coingecko-sdk.models.token_data import TokenData
from coingecko-sdk.models.token_data_attributes import TokenDataAttributes
from coingecko-sdk.models.token_data_attributes_volume_usd import TokenDataAttributesVolumeUsd
from coingecko-sdk.models.token_data_relationships import TokenDataRelationships
from coingecko-sdk.models.token_data_relationships_top_pools import TokenDataRelationshipsTopPools
from coingecko-sdk.models.token_included_inner import TokenIncludedInner
from coingecko-sdk.models.token_included_inner_attributes import TokenIncludedInnerAttributes
from coingecko-sdk.models.token_included_inner_relationships import TokenIncludedInnerRelationships
from coingecko-sdk.models.token_info import TokenInfo
from coingecko-sdk.models.token_info_data import TokenInfoData
from coingecko-sdk.models.token_info_data_attributes import TokenInfoDataAttributes
from coingecko-sdk.models.token_info_data_attributes_holders import TokenInfoDataAttributesHolders
from coingecko-sdk.models.token_info_data_attributes_holders_distribution_percentage import TokenInfoDataAttributesHoldersDistributionPercentage
from coingecko-sdk.models.token_info_recently_updated import TokenInfoRecentlyUpdated
from coingecko-sdk.models.token_lists import TokenLists
from coingecko-sdk.models.token_lists_tokens_inner import TokenListsTokensInner
from coingecko-sdk.models.top_gainers_losers_inner import TopGainersLosersInner
from coingecko-sdk.models.trades import Trades
from coingecko-sdk.models.trades_data_inner import TradesDataInner
from coingecko-sdk.models.trades_data_inner_attributes import TradesDataInnerAttributes
from coingecko-sdk.models.trending_search import TrendingSearch
from coingecko-sdk.models.trending_search_categories_inner import TrendingSearchCategoriesInner
from coingecko-sdk.models.trending_search_categories_inner_data import TrendingSearchCategoriesInnerData
from coingecko-sdk.models.trending_search_categories_inner_data_market_cap_change_percentage24h import TrendingSearchCategoriesInnerDataMarketCapChangePercentage24h
from coingecko-sdk.models.trending_search_coins_inner import TrendingSearchCoinsInner
from coingecko-sdk.models.trending_search_coins_inner_data import TrendingSearchCoinsInnerData
from coingecko-sdk.models.trending_search_coins_inner_data_price_change_percentage24h import TrendingSearchCoinsInnerDataPriceChangePercentage24h
from coingecko-sdk.models.trending_search_nfts_inner import TrendingSearchNftsInner
from coingecko-sdk.models.trending_search_nfts_inner_data import TrendingSearchNftsInnerData
