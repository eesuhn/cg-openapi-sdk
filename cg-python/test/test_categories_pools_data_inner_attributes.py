# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.categories_pools_data_inner_attributes import CategoriesPoolsDataInnerAttributes

class TestCategoriesPoolsDataInnerAttributes(unittest.TestCase):
    """CategoriesPoolsDataInnerAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoriesPoolsDataInnerAttributes:
        """Test CategoriesPoolsDataInnerAttributes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesPoolsDataInnerAttributes`
        """
        model = CategoriesPoolsDataInnerAttributes()
        if include_optional:
            return CategoriesPoolsDataInnerAttributes(
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
                h24_tx_count = 56
            )
        else:
            return CategoriesPoolsDataInnerAttributes(
        )
        """

    def testCategoriesPoolsDataInnerAttributes(self):
        """Test CategoriesPoolsDataInnerAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
