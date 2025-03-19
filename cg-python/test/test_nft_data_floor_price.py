# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.nft_data_floor_price import NFTDataFloorPrice

class TestNFTDataFloorPrice(unittest.TestCase):
    """NFTDataFloorPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTDataFloorPrice:
        """Test NFTDataFloorPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTDataFloorPrice`
        """
        model = NFTDataFloorPrice()
        if include_optional:
            return NFTDataFloorPrice(
                native_currency = 1.337,
                usd = 1.337
            )
        else:
            return NFTDataFloorPrice(
        )
        """

    def testNFTDataFloorPrice(self):
        """Test NFTDataFloorPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
