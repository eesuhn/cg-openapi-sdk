# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.nft_data_volume24h_percentage_change import NFTDataVolume24hPercentageChange

class TestNFTDataVolume24hPercentageChange(unittest.TestCase):
    """NFTDataVolume24hPercentageChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTDataVolume24hPercentageChange:
        """Test NFTDataVolume24hPercentageChange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTDataVolume24hPercentageChange`
        """
        model = NFTDataVolume24hPercentageChange()
        if include_optional:
            return NFTDataVolume24hPercentageChange(
                usd = 1.337,
                native_currency = 1.337
            )
        else:
            return NFTDataVolume24hPercentageChange(
        )
        """

    def testNFTDataVolume24hPercentageChange(self):
        """Test NFTDataVolume24hPercentageChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
