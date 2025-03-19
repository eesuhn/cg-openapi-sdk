# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.token_data import TokenData

class TestTokenData(unittest.TestCase):
    """TokenData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenData:
        """Test TokenData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenData`
        """
        model = TokenData()
        if include_optional:
            return TokenData(
                id = '',
                type = '',
                attributes = coingecko-sdk.models.token_data_attributes.Token_data_attributes(
                    address = '', 
                    name = '', 
                    symbol = '', 
                    image_url = '', 
                    coingecko_coin_id = '', 
                    decimals = 56, 
                    total_supply = '', 
                    price_usd = '', 
                    fdv_usd = '', 
                    total_reserve_in_usd = '', 
                    volume_usd = coingecko-sdk.models.token_data_attributes_volume_usd.Token_data_attributes_volume_usd(
                        h24 = '', ), 
                    market_cap_usd = '', ),
                relationships = coingecko-sdk.models.token_data_relationships.Token_data_relationships(
                    top_pools = coingecko-sdk.models.token_data_relationships_top_pools.Token_data_relationships_top_pools(
                        data = [
                            coingecko-sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                                id = '', 
                                type = '', )
                            ], ), )
            )
        else:
            return TokenData(
        )
        """

    def testTokenData(self):
        """Test TokenData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
