# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.coins_data_base_market_data_market_cap import CoinsDataBaseMarketDataMarketCap

class TestCoinsDataBaseMarketDataMarketCap(unittest.TestCase):
    """CoinsDataBaseMarketDataMarketCap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsDataBaseMarketDataMarketCap:
        """Test CoinsDataBaseMarketDataMarketCap
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsDataBaseMarketDataMarketCap`
        """
        model = CoinsDataBaseMarketDataMarketCap()
        if include_optional:
            return CoinsDataBaseMarketDataMarketCap(
                btc = 1.337,
                eur = 1.337,
                usd = 1.337
            )
        else:
            return CoinsDataBaseMarketDataMarketCap(
        )
        """

    def testCoinsDataBaseMarketDataMarketCap(self):
        """Test CoinsDataBaseMarketDataMarketCap"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
