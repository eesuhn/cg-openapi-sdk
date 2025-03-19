# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.nfts_markets_inner_floor_price24h_percentage_change import NFTsMarketsInnerFloorPrice24hPercentageChange

class TestNFTsMarketsInnerFloorPrice24hPercentageChange(unittest.TestCase):
    """NFTsMarketsInnerFloorPrice24hPercentageChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTsMarketsInnerFloorPrice24hPercentageChange:
        """Test NFTsMarketsInnerFloorPrice24hPercentageChange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTsMarketsInnerFloorPrice24hPercentageChange`
        """
        model = NFTsMarketsInnerFloorPrice24hPercentageChange()
        if include_optional:
            return NFTsMarketsInnerFloorPrice24hPercentageChange(
                usd = 1.337,
                native_currency = 1.337
            )
        else:
            return NFTsMarketsInnerFloorPrice24hPercentageChange(
        )
        """

    def testNFTsMarketsInnerFloorPrice24hPercentageChange(self):
        """Test NFTsMarketsInnerFloorPrice24hPercentageChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
