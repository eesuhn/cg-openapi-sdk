# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.nft_data_explorers_inner import NFTDataExplorersInner

class TestNFTDataExplorersInner(unittest.TestCase):
    """NFTDataExplorersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTDataExplorersInner:
        """Test NFTDataExplorersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTDataExplorersInner`
        """
        model = NFTDataExplorersInner()
        if include_optional:
            return NFTDataExplorersInner(
                name = '',
                link = ''
            )
        else:
            return NFTDataExplorersInner(
        )
        """

    def testNFTDataExplorersInner(self):
        """Test NFTDataExplorersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
