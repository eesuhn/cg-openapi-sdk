# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.coins_historical_data import CoinsHistoricalData

class TestCoinsHistoricalData(unittest.TestCase):
    """CoinsHistoricalData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsHistoricalData:
        """Test CoinsHistoricalData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsHistoricalData`
        """
        model = CoinsHistoricalData()
        if include_optional:
            return CoinsHistoricalData(
                id = '',
                symbol = '',
                name = '',
                localization = {
                    'key' : ''
                    },
                image = coingecko_python.models.coins_historical_data_image.CoinsHistoricalData_image(
                    thumb = '', 
                    small = '', ),
                market_data = coingecko_python.models.coins_historical_data_market_data.CoinsHistoricalData_market_data(
                    current_price = coingecko_python.models.coins_historical_data_market_data_current_price.CoinsHistoricalData_market_data_current_price(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    market_cap = coingecko_python.models.coins_historical_data_market_data_market_cap.CoinsHistoricalData_market_data_market_cap(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), 
                    total_volume = coingecko_python.models.coins_historical_data_market_data_total_volume.CoinsHistoricalData_market_data_total_volume(
                        btc = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, ), ),
                community_data = coingecko_python.models.coins_historical_data_community_data.CoinsHistoricalData_community_data(
                    facebook_likes = 1.337, 
                    twitter_followers = 1.337, 
                    reddit_average_posts_48h = 1.337, 
                    reddit_average_comments_48h = 1.337, 
                    reddit_subscribers = 1.337, 
                    reddit_accounts_active_48h = 1.337, ),
                developer_data = coingecko_python.models.coins_historical_data_developer_data.CoinsHistoricalData_developer_data(
                    forks = 1.337, 
                    stars = 1.337, 
                    subscribers = 1.337, 
                    total_issues = 1.337, 
                    closed_issues = 1.337, 
                    pull_requests_merged = 1.337, 
                    pull_request_contributors = 1.337, 
                    code_additions_deletions_4_weeks = coingecko_python.models.coins_historical_data_developer_data_code_additions_deletions_4_weeks.CoinsHistoricalData_developer_data_code_additions_deletions_4_weeks(
                        additions = 1.337, 
                        deletions = 1.337, ), 
                    commit_count_4_weeks = 1.337, ),
                public_interest_stats = coingecko_python.models.coins_historical_data_public_interest_stats.CoinsHistoricalData_public_interest_stats(
                    alexa_rank = 1.337, 
                    bing_matches = 1.337, )
            )
        else:
            return CoinsHistoricalData(
        )
        """

    def testCoinsHistoricalData(self):
        """Test CoinsHistoricalData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
