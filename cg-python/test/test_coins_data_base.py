# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.coins_data_base import CoinsDataBase

class TestCoinsDataBase(unittest.TestCase):
    """CoinsDataBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsDataBase:
        """Test CoinsDataBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsDataBase`
        """
        model = CoinsDataBase()
        if include_optional:
            return CoinsDataBase(
                id = '',
                symbol = '',
                name = '',
                web_slug = '',
                asset_platform_id = '',
                platforms = {
                    'key' : ''
                    },
                detail_platforms = {
                    'key' : ''
                    },
                block_time_in_minutes = 1.337,
                hashing_algorithm = '',
                categories = [
                    ''
                    ],
                preview_listing = True,
                public_notice = '',
                additional_notices = [
                    ''
                    ],
                localization = {
                    'key' : ''
                    },
                description = {
                    'key' : ''
                    },
                links = coingecko_sdk.models.coins_data_base_links.CoinsDataBase_links(
                    homepage = [
                        ''
                        ], 
                    whitepaper = [
                        ''
                        ], 
                    blockchain_site = [
                        ''
                        ], 
                    official_forum_url = [
                        ''
                        ], 
                    chat_url = [
                        ''
                        ], 
                    announcement_url = [
                        ''
                        ], 
                    snapshot_url = '', 
                    twitter_screen_name = '', 
                    facebook_username = '', 
                    bitcointalk_thread_identifier = '', 
                    telegram_channel_identifier = '', 
                    subreddit_url = '', 
                    repos_url = coingecko_sdk.models.coins_data_base_links_repos_url.CoinsDataBase_links_repos_url(
                        github = [
                            ''
                            ], 
                        bitbucket = [
                            ''
                            ], ), ),
                image = coingecko_sdk.models.coins_data_base_image.CoinsDataBase_image(
                    thumb = '', 
                    small = '', 
                    large = '', ),
                country_origin = '',
                genesis_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sentiment_votes_up_percentage = 1.337,
                sentiment_votes_down_percentage = 1.337,
                market_cap_rank = 1.337,
                market_data = coingecko_sdk.models.coins_data_base_market_data.CoinsDataBase_market_data(
                    current_price = coingecko_sdk.models.coins_data_base_market_data_current_price.CoinsDataBase_market_data_current_price(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    total_value_locked = 1.337, 
                    mcap_to_tvl_ratio = 1.337, 
                    fdv_to_tvl_ratio = 1.337, 
                    roi = 1.337, 
                    ath = coingecko_sdk.models.coins_data_base_market_data_ath.CoinsDataBase_market_data_ath(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    ath_change_percentage = coingecko_sdk.models.coins_data_base_market_data_ath_change_percentage.CoinsDataBase_market_data_ath_change_percentage(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    ath_date = coingecko_sdk.models.coins_data_base_market_data_ath_date.CoinsDataBase_market_data_ath_date(
                        btc = '', 
                        eur = '', 
                        usd = '', ), 
                    atl = coingecko_sdk.models.coins_data_base_market_data_atl.CoinsDataBase_market_data_atl(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    atl_change_percentage = coingecko_sdk.models.coins_data_base_market_data_atl_change_percentage.CoinsDataBase_market_data_atl_change_percentage(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    atl_date = coingecko_sdk.models.coins_data_base_market_data_atl_date.CoinsDataBase_market_data_atl_date(
                        btc = '', 
                        eur = '', 
                        usd = '', ), 
                    market_cap = coingecko_sdk.models.coins_data_base_market_data_market_cap.CoinsDataBase_market_data_market_cap(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    market_cap_rank = 1.337, 
                    fully_diluted_valuation = coingecko_sdk.models.coins_data_base_market_data_fully_diluted_valuation.CoinsDataBase_market_data_fully_diluted_valuation(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    market_cap_fdv_ratio = 1.337, 
                    total_volume = coingecko_sdk.models.coins_data_base_market_data_total_volume.CoinsDataBase_market_data_total_volume(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    high_24h = coingecko_sdk.models.coins_data_base_market_data_high_24h.CoinsDataBase_market_data_high_24h(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    low_24h = coingecko_sdk.models.coins_data_base_market_data_low_24h.CoinsDataBase_market_data_low_24h(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_24h = 1.337, 
                    price_change_percentage_24h = 1.337, 
                    price_change_percentage_7d = 1.337, 
                    price_change_percentage_14d = 1.337, 
                    price_change_percentage_30d = 1.337, 
                    price_change_percentage_60d = 1.337, 
                    price_change_percentage_200d = 1.337, 
                    price_change_percentage_1y = 1.337, 
                    market_cap_change_24h = 1.337, 
                    market_cap_change_percentage_24h = 1.337, 
                    price_change_percentage_1h_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_1h_in_currency.CoinsDataBase_market_data_price_change_percentage_1h_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_24h_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_24h_in_currency.CoinsDataBase_market_data_price_change_percentage_24h_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_7d_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_7d_in_currency.CoinsDataBase_market_data_price_change_percentage_7d_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_14d_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_14d_in_currency.CoinsDataBase_market_data_price_change_percentage_14d_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_30d_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_30d_in_currency.CoinsDataBase_market_data_price_change_percentage_30d_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_60d_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_60d_in_currency.CoinsDataBase_market_data_price_change_percentage_60d_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_200d_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_200d_in_currency.CoinsDataBase_market_data_price_change_percentage_200d_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    price_change_percentage_1y_in_currency = coingecko_sdk.models.coins_data_base_market_data_price_change_percentage_1y_in_currency.CoinsDataBase_market_data_price_change_percentage_1y_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    market_cap_change_24h_in_currency = coingecko_sdk.models.coins_data_base_market_data_market_cap_change_24h_in_currency.CoinsDataBase_market_data_market_cap_change_24h_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    market_cap_change_percentage_24h_in_currency = coingecko_sdk.models.coins_data_base_market_data_market_cap_change_percentage_24h_in_currency.CoinsDataBase_market_data_market_cap_change_percentage_24h_in_currency(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    total_supply = 1.337, 
                    max_supply = 1.337, 
                    circulating_supply = 1.337, 
                    last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                community_data = coingecko_sdk.models.coins_data_base_community_data.CoinsDataBase_community_data(
                    facebook_likes = 1.337, 
                    twitter_followers = 1.337, 
                    reddit_average_posts_48h = 1.337, 
                    reddit_average_comments_48h = 1.337, 
                    reddit_subscribers = 1.337, 
                    reddit_accounts_active_48h = 1.337, 
                    telegram_channel_user_count = 1.337, ),
                developer_data = coingecko_sdk.models.coins_data_base_developer_data.CoinsDataBase_developer_data(
                    forks = 1.337, 
                    stars = 1.337, 
                    subscribers = 1.337, 
                    total_issues = 1.337, 
                    closed_issues = 1.337, 
                    pull_requests_merged = 1.337, 
                    pull_request_contributors = 1.337, 
                    code_additions_deletions_4_weeks = coingecko_sdk.models.coins_data_base_developer_data_code_additions_deletions_4_weeks.CoinsDataBase_developer_data_code_additions_deletions_4_weeks(
                        additions = 1.337, 
                        deletions = 1.337, ), 
                    commit_count_4_weeks = 1.337, 
                    last_4_weeks_commit_activity_series = [], ),
                status_updates = [],
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tickers = [
                    coingecko_sdk.models.coins_data_base_tickers_inner.CoinsDataBase_tickers_inner(
                        base = '', 
                        target = '', 
                        market = coingecko_sdk.models.coins_data_base_tickers_inner_market.CoinsDataBase_tickers_inner_market(
                            name = '', 
                            identifier = '', 
                            has_trading_incentive = True, ), 
                        last = 1.337, 
                        volume = 1.337, 
                        converted_last = coingecko_sdk.models.coins_data_base_tickers_inner_converted_last.CoinsDataBase_tickers_inner_converted_last(
                            btc = 1.337, 
                            eth = 1.337, 
                            usd = 1.337, ), 
                        converted_volume = coingecko_sdk.models.coins_data_base_tickers_inner_converted_volume.CoinsDataBase_tickers_inner_converted_volume(
                            btc = 1.337, 
                            eth = 1.337, 
                            usd = 1.337, ), 
                        trust_score = '', 
                        bid_ask_spread_percentage = 1.337, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_traded_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_anomaly = True, 
                        is_stale = True, 
                        trade_url = '', 
                        token_info_url = '', 
                        coin_id = '', 
                        target_coin_id = '', )
                    ]
            )
        else:
            return CoinsDataBase(
        )
        """

    def testCoinsDataBase(self):
        """Test CoinsDataBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
