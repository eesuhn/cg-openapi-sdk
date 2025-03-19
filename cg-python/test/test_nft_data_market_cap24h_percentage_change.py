# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.nft_data_market_cap24h_percentage_change import NFTDataMarketCap24hPercentageChange

class TestNFTDataMarketCap24hPercentageChange(unittest.TestCase):
    """NFTDataMarketCap24hPercentageChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTDataMarketCap24hPercentageChange:
        """Test NFTDataMarketCap24hPercentageChange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTDataMarketCap24hPercentageChange`
        """
        model = NFTDataMarketCap24hPercentageChange()
        if include_optional:
            return NFTDataMarketCap24hPercentageChange(
                usd = 1.337,
                native_currency = 1.337
            )
        else:
            return NFTDataMarketCap24hPercentageChange(
        )
        """

    def testNFTDataMarketCap24hPercentageChange(self):
        """Test NFTDataMarketCap24hPercentageChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
