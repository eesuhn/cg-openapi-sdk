# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.token_data_relationships_top_pools import TokenDataRelationshipsTopPools

class TestTokenDataRelationshipsTopPools(unittest.TestCase):
    """TokenDataRelationshipsTopPools unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenDataRelationshipsTopPools:
        """Test TokenDataRelationshipsTopPools
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenDataRelationshipsTopPools`
        """
        model = TokenDataRelationshipsTopPools()
        if include_optional:
            return TokenDataRelationshipsTopPools(
                data = [
                    coingecko-sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                        id = '', 
                        type = '', )
                    ]
            )
        else:
            return TokenDataRelationshipsTopPools(
        )
        """

    def testTokenDataRelationshipsTopPools(self):
        """Test TokenDataRelationshipsTopPools"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
