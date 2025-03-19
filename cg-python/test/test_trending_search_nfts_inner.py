# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.trending_search_nfts_inner import TrendingSearchNftsInner

class TestTrendingSearchNftsInner(unittest.TestCase):
    """TrendingSearchNftsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrendingSearchNftsInner:
        """Test TrendingSearchNftsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrendingSearchNftsInner`
        """
        model = TrendingSearchNftsInner()
        if include_optional:
            return TrendingSearchNftsInner(
                id = '',
                name = '',
                symbol = '',
                thumb = '',
                nft_contract_id = 1.337,
                native_currency_symbol = '',
                floor_price_in_native_currency = 1.337,
                floor_price_24h_percentage_change = 1.337,
                data = coingecko_sdk.models.trending_search_nfts_inner_data.TrendingSearch_nfts_inner_data(
                    floor_price = '', 
                    floor_price_in_usd_24h_percentage_change = '', 
                    h24_volume = '', 
                    h24_average_sale_price = '', 
                    sparkline = '', 
                    content = '', )
            )
        else:
            return TrendingSearchNftsInner(
        )
        """

    def testTrendingSearchNftsInner(self):
        """Test TrendingSearchNftsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
