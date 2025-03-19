# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.coins_tickers_tickers_inner_market import CoinsTickersTickersInnerMarket

class TestCoinsTickersTickersInnerMarket(unittest.TestCase):
    """CoinsTickersTickersInnerMarket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsTickersTickersInnerMarket:
        """Test CoinsTickersTickersInnerMarket
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsTickersTickersInnerMarket`
        """
        model = CoinsTickersTickersInnerMarket()
        if include_optional:
            return CoinsTickersTickersInnerMarket(
                name = '',
                identifier = '',
                has_trading_incentive = True,
                logo = ''
            )
        else:
            return CoinsTickersTickersInnerMarket(
                name = '',
                identifier = '',
                has_trading_incentive = True,
        )
        """

    def testCoinsTickersTickersInnerMarket(self):
        """Test CoinsTickersTickersInnerMarket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
