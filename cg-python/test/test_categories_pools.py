# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.categories_pools import CategoriesPools

class TestCategoriesPools(unittest.TestCase):
    """CategoriesPools unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoriesPools:
        """Test CategoriesPools
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesPools`
        """
        model = CategoriesPools()
        if include_optional:
            return CategoriesPools(
                data = [
                    coingecko_python.models.categories_pools_data_inner.CategoriesPools_data_inner(
                        id = '', 
                        type = '', 
                        attributes = coingecko_python.models.categories_pools_data_inner_attributes.CategoriesPools_data_inner_attributes(
                            base_token_price_usd = '', 
                            base_token_price_native_currency = '', 
                            quote_token_price_usd = '', 
                            quote_token_price_native_currency = '', 
                            base_token_price_quote_token = '', 
                            quote_token_price_base_token = '', 
                            address = '', 
                            name = '', 
                            pool_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            fdv_usd = '', 
                            market_cap_usd = '', 
                            price_change_percentage = coingecko_python.models.pool_data_inner_attributes_price_change_percentage.Pool_data_inner_attributes_price_change_percentage(
                                m5 = '', 
                                h1 = '', 
                                h6 = '', 
                                h24 = '', ), 
                            reserve_in_usd = '', 
                            h24_volume_usd = '', 
                            h24_tx_count = 56, ), 
                        relationships = coingecko_python.models.categories_pools_data_inner_relationships.CategoriesPools_data_inner_relationships(
                            network = coingecko_python.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(
                                data = coingecko_python.models.pool_data_inner_relationships_base_token_data.Pool_data_inner_relationships_base_token_data(
                                    id = '', 
                                    type = '', ), ), 
                            dex = coingecko_python.models.pool_data_inner_relationships_base_token.Pool_data_inner_relationships_base_token(), 
                            base_token = , 
                            quote_token = , ), )
                    ],
                included = [
                    coingecko_python.models.categories_pools_included_inner.CategoriesPools_included_inner(
                        id = '', 
                        type = '', 
                        attributes = coingecko_python.models.categories_pools_included_inner_attributes.CategoriesPools_included_inner_attributes(
                            address = '', 
                            name = '', 
                            symbol = '', 
                            decimals = 56, 
                            image_url = '', 
                            coingecko_coin_id = '', ), )
                    ]
            )
        else:
            return CategoriesPools(
        )
        """

    def testCategoriesPools(self):
        """Test CategoriesPools"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
