# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.trending_search_coins_inner_data import TrendingSearchCoinsInnerData

class TestTrendingSearchCoinsInnerData(unittest.TestCase):
    """TrendingSearchCoinsInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrendingSearchCoinsInnerData:
        """Test TrendingSearchCoinsInnerData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrendingSearchCoinsInnerData`
        """
        model = TrendingSearchCoinsInnerData()
        if include_optional:
            return TrendingSearchCoinsInnerData(
                price = 1.337,
                price_btc = '',
                price_change_percentage_24h = coingecko_sdk.models.trending_search_coins_inner_data_price_change_percentage_24h.TrendingSearch_coins_inner_data_price_change_percentage_24h(
                    btc = 1.337, 
                    usd = 1.337, ),
                market_cap = '',
                market_cap_btc = '',
                total_volume = '',
                total_volume_btc = '',
                sparkline = '',
                content = ''
            )
        else:
            return TrendingSearchCoinsInnerData(
        )
        """

    def testTrendingSearchCoinsInnerData(self):
        """Test TrendingSearchCoinsInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
