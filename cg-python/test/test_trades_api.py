# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.api.trades_api import TradesApi


class TestTradesApi(unittest.TestCase):
    """TradesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TradesApi()

    def tearDown(self) -> None:
        pass

    def test_pool_trades_contract_address(self) -> None:
        """Test case for pool_trades_contract_address

        Past 24 Hour Trades by Pool Address
        """
        pass


if __name__ == '__main__':
    unittest.main()
