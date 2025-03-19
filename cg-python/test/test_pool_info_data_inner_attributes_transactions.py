# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.pool_info_data_inner_attributes_transactions import PoolInfoDataInnerAttributesTransactions

class TestPoolInfoDataInnerAttributesTransactions(unittest.TestCase):
    """PoolInfoDataInnerAttributesTransactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolInfoDataInnerAttributesTransactions:
        """Test PoolInfoDataInnerAttributesTransactions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolInfoDataInnerAttributesTransactions`
        """
        model = PoolInfoDataInnerAttributesTransactions()
        if include_optional:
            return PoolInfoDataInnerAttributesTransactions(
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
                m30 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                    buys = 56, 
                    sells = 56, 
                    buyers = 56, 
                    sellers = 56, ),
                h1 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                    buys = 56, 
                    sells = 56, 
                    buyers = 56, 
                    sellers = 56, ),
                h6 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                    buys = 56, 
                    sells = 56, 
                    buyers = 56, 
                    sellers = 56, ),
                h24 = coingecko_sdk.models.pool_data_inner_attributes_transactions_m5.Pool_data_inner_attributes_transactions_m5(
                    buys = 56, 
                    sells = 56, 
                    buyers = 56, 
                    sellers = 56, )
            )
        else:
            return PoolInfoDataInnerAttributesTransactions(
        )
        """

    def testPoolInfoDataInnerAttributesTransactions(self):
        """Test PoolInfoDataInnerAttributesTransactions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
