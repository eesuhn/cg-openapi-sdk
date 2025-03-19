# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.ohlcv_meta_base import OHLCVMetaBase

class TestOHLCVMetaBase(unittest.TestCase):
    """OHLCVMetaBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OHLCVMetaBase:
        """Test OHLCVMetaBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OHLCVMetaBase`
        """
        model = OHLCVMetaBase()
        if include_optional:
            return OHLCVMetaBase(
                address = '',
                name = '',
                symbol = '',
                coingecko_coin_id = ''
            )
        else:
            return OHLCVMetaBase(
        )
        """

    def testOHLCVMetaBase(self):
        """Test OHLCVMetaBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
