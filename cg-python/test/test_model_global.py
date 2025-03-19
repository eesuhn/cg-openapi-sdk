# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_python.models.model_global import ModelGlobal

class TestModelGlobal(unittest.TestCase):
    """ModelGlobal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelGlobal:
        """Test ModelGlobal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelGlobal`
        """
        model = ModelGlobal()
        if include_optional:
            return ModelGlobal(
                data = coingecko_python.models.global_data.Global_data(
                    active_cryptocurrencies = 1.337, 
                    upcoming_icos = 1.337, 
                    ongoing_icos = 1.337, 
                    ended_icos = 1.337, 
                    markets = 1.337, 
                    total_market_cap = coingecko_python.models.global_data_total_market_cap.Global_data_total_market_cap(
                        btc = 1.337, 
                        eth = 1.337, ), 
                    total_volume = coingecko_python.models.global_data_total_volume.Global_data_total_volume(
                        btc = 1.337, 
                        eth = 1.337, ), 
                    market_cap_percentage = coingecko_python.models.global_data_market_cap_percentage.Global_data_market_cap_percentage(
                        btc = 1.337, 
                        eth = 1.337, ), ),
                market_cap_change_percentage_24h_usd = 1.337,
                updated_at = 1.337
            )
        else:
            return ModelGlobal(
        )
        """

    def testModelGlobal(self):
        """Test ModelGlobal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
