# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.api.categories_api import CategoriesApi


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CategoriesApi()

    def tearDown(self) -> None:
        pass

    def test_categories_list(self) -> None:
        """Test case for categories_list

        Categories List
        """
        pass

    def test_coins_categories(self) -> None:
        """Test case for coins_categories

        Coins Categories List with Market Data
        """
        pass

    def test_coins_categories_list(self) -> None:
        """Test case for coins_categories_list

        Coins Categories List (ID Map)
        """
        pass

    def test_pools_category(self) -> None:
        """Test case for pools_category

        Pools by Category ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
