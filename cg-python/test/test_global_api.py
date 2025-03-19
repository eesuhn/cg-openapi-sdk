# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.api.global_api import GlobalApi


class TestGlobalApi(unittest.TestCase):
    """GlobalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GlobalApi()

    def tearDown(self) -> None:
        pass

    def test_crypto_global(self) -> None:
        """Test case for crypto_global

        Crypto Global Market Data
        """
        pass

    def test_global_de_fi(self) -> None:
        """Test case for global_de_fi

        Global De-Fi Market Data
        """
        pass

    def test_global_market_cap_chart(self) -> None:
        """Test case for global_market_cap_chart

        💼 Global Market Cap Chart Data
        """
        pass


if __name__ == '__main__':
    unittest.main()
