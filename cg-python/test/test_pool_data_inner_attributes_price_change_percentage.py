# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.pool_data_inner_attributes_price_change_percentage import PoolDataInnerAttributesPriceChangePercentage

class TestPoolDataInnerAttributesPriceChangePercentage(unittest.TestCase):
    """PoolDataInnerAttributesPriceChangePercentage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolDataInnerAttributesPriceChangePercentage:
        """Test PoolDataInnerAttributesPriceChangePercentage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolDataInnerAttributesPriceChangePercentage`
        """
        model = PoolDataInnerAttributesPriceChangePercentage()
        if include_optional:
            return PoolDataInnerAttributesPriceChangePercentage(
                m5 = '',
                h1 = '',
                h6 = '',
                h24 = ''
            )
        else:
            return PoolDataInnerAttributesPriceChangePercentage(
        )
        """

    def testPoolDataInnerAttributesPriceChangePercentage(self):
        """Test PoolDataInnerAttributesPriceChangePercentage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
