# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.token_included_inner_relationships import TokenIncludedInnerRelationships

class TestTokenIncludedInnerRelationships(unittest.TestCase):
    """TokenIncludedInnerRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenIncludedInnerRelationships:
        """Test TokenIncludedInnerRelationships
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenIncludedInnerRelationships`
        """
        model = TokenIncludedInnerRelationships()
        if include_optional:
            return TokenIncludedInnerRelationships(
                base_token = coingecko_sdk.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(
                    data = coingecko_sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                        id = '', 
                        type = '', ), ),
                quote_token = coingecko_sdk.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(
                    data = coingecko_sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                        id = '', 
                        type = '', ), ),
                dex = coingecko_sdk.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(
                    data = coingecko_sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                        id = '', 
                        type = '', ), )
            )
        else:
            return TokenIncludedInnerRelationships(
        )
        """

    def testTokenIncludedInnerRelationships(self):
        """Test TokenIncludedInnerRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
