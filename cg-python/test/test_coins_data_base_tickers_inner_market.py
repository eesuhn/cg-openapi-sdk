# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.coins_data_base_tickers_inner_market import CoinsDataBaseTickersInnerMarket

class TestCoinsDataBaseTickersInnerMarket(unittest.TestCase):
    """CoinsDataBaseTickersInnerMarket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsDataBaseTickersInnerMarket:
        """Test CoinsDataBaseTickersInnerMarket
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsDataBaseTickersInnerMarket`
        """
        model = CoinsDataBaseTickersInnerMarket()
        if include_optional:
            return CoinsDataBaseTickersInnerMarket(
                name = '',
                identifier = '',
                has_trading_incentive = True
            )
        else:
            return CoinsDataBaseTickersInnerMarket(
        )
        """

    def testCoinsDataBaseTickersInnerMarket(self):
        """Test CoinsDataBaseTickersInnerMarket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
