# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.trending_search_categories_inner import TrendingSearchCategoriesInner

class TestTrendingSearchCategoriesInner(unittest.TestCase):
    """TrendingSearchCategoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrendingSearchCategoriesInner:
        """Test TrendingSearchCategoriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrendingSearchCategoriesInner`
        """
        model = TrendingSearchCategoriesInner()
        if include_optional:
            return TrendingSearchCategoriesInner(
                id = 1.337,
                name = '',
                market_cap_1h_change = 1.337,
                slug = '',
                coins_count = 1.337,
                data = coingecko_python.models.trending_search_categories_inner_data.TrendingSearch_categories_inner_data(
                    market_cap = 1.337, 
                    market_cap_btc = 1.337, 
                    total_volume = 1.337, 
                    total_volume_btc = 1.337, 
                    market_cap_change_percentage_24h = coingecko_python.models.trending_search_categories_inner_data_market_cap_change_percentage_24h.TrendingSearch_categories_inner_data_market_cap_change_percentage_24h(
                        btc = 1.337, 
                        usd = 1.337, ), 
                    sparkline = '', )
            )
        else:
            return TrendingSearchCategoriesInner(
        )
        """

    def testTrendingSearchCategoriesInner(self):
        """Test TrendingSearchCategoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
