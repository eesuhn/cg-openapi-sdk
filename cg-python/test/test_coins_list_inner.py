# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.coins_list_inner import CoinsListInner

class TestCoinsListInner(unittest.TestCase):
    """CoinsListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsListInner:
        """Test CoinsListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsListInner`
        """
        model = CoinsListInner()
        if include_optional:
            return CoinsListInner(
                id = '',
                symbol = '',
                name = '',
                platforms = {
                    'key' : ''
                    }
            )
        else:
            return CoinsListInner(
        )
        """

    def testCoinsListInner(self):
        """Test CoinsListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
