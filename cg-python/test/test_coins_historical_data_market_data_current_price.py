# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.coins_historical_data_market_data_current_price import CoinsHistoricalDataMarketDataCurrentPrice

class TestCoinsHistoricalDataMarketDataCurrentPrice(unittest.TestCase):
    """CoinsHistoricalDataMarketDataCurrentPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsHistoricalDataMarketDataCurrentPrice:
        """Test CoinsHistoricalDataMarketDataCurrentPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsHistoricalDataMarketDataCurrentPrice`
        """
        model = CoinsHistoricalDataMarketDataCurrentPrice()
        if include_optional:
            return CoinsHistoricalDataMarketDataCurrentPrice(
                btc = 1.337,
                eur = 1.337,
                usd = 1.337
            )
        else:
            return CoinsHistoricalDataMarketDataCurrentPrice(
        )
        """

    def testCoinsHistoricalDataMarketDataCurrentPrice(self):
        """Test CoinsHistoricalDataMarketDataCurrentPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
