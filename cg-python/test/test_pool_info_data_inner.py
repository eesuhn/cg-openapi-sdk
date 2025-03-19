# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.pool_info_data_inner import PoolInfoDataInner

class TestPoolInfoDataInner(unittest.TestCase):
    """PoolInfoDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolInfoDataInner:
        """Test PoolInfoDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolInfoDataInner`
        """
        model = PoolInfoDataInner()
        if include_optional:
            return PoolInfoDataInner(
                id = '',
                type = '',
                attributes = coingecko_sdk.models.pool_info_data_inner_attributes.PoolInfo_data_inner_attributes(
                    base_token_price_usd = '', 
                    base_token_price_native_currency = '', 
                    quote_token_price_usd = '', 
                    quote_token_price_native_currency = '', 
                    base_token_price_quote_token = '', 
                    quote_token_price_base_token = '', 
                    address = '', 
                    name = '', 
                    pool_created_at = '', 
                    fdv_usd = '', 
                    market_cap_usd = '', 
                    price_change_percentage = coingecko_sdk.models.pool_data_inner_attributes_price_change_percentage.Pool_data_inner_attributes_price_change_percentage(
                        m5 = '', 
                        h1 = '', 
                        h6 = '', 
                        h24 = '', ), 
                    transactions = coingecko_sdk.models.pool_info_data_inner_attributes_transactions.PoolInfo_data_inner_attributes_transactions(
                        m5 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                            buys = 56, 
                            sells = 56, 
                            buyers = 56, 
                            sellers = 56, ), 
                        m15 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                            buys = 56, 
                            sells = 56, 
                            buyers = 56, 
                            sellers = 56, ), 
                        m30 = , 
                        h1 = , 
                        h6 = , 
                        h24 = , ), 
                    volume_usd = coingecko_sdk.models.pool_info_data_inner_attributes_volume_usd.PoolInfo_data_inner_attributes_volume_usd(), 
                    reserve_in_usd = '', 
                    locked_liquidity_percentage = '', ),
                relationships = coingecko_sdk.models.pool_data_inner_relationships.Pool_data_inner_relationships(
                    base_token = coingecko_sdk.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(
                        data = coingecko_sdk.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                            id = '', 
                            type = '', ), ), 
                    quote_token = coingecko_sdk.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(), 
                    network = , 
                    dex = , )
            )
        else:
            return PoolInfoDataInner(
        )
        """

    def testPoolInfoDataInner(self):
        """Test PoolInfoDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
