# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.api.ping_api import PingApi


class TestPingApi(unittest.TestCase):
    """PingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PingApi()

    def tearDown(self) -> None:
        pass

    def test_ping_server(self) -> None:
        """Test case for ping_server

        Check API server status
        """
        pass


if __name__ == '__main__':
    unittest.main()
