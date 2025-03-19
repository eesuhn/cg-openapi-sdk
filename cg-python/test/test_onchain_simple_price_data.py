# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.onchain_simple_price_data import OnchainSimplePriceData

class TestOnchainSimplePriceData(unittest.TestCase):
    """OnchainSimplePriceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnchainSimplePriceData:
        """Test OnchainSimplePriceData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnchainSimplePriceData`
        """
        model = OnchainSimplePriceData()
        if include_optional:
            return OnchainSimplePriceData(
                id = '',
                type = '',
                attributes = coingecko_sdk.models.onchain_simple_price_data_attributes.OnchainSimplePrice_data_attributes(
                    token_prices = {
                        'key' : ''
                        }, )
            )
        else:
            return OnchainSimplePriceData(
        )
        """

    def testOnchainSimplePriceData(self):
        """Test OnchainSimplePriceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
