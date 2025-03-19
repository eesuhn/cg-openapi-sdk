# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.token_info_data_attributes_holders_distribution_percentage import TokenInfoDataAttributesHoldersDistributionPercentage

class TestTokenInfoDataAttributesHoldersDistributionPercentage(unittest.TestCase):
    """TokenInfoDataAttributesHoldersDistributionPercentage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenInfoDataAttributesHoldersDistributionPercentage:
        """Test TokenInfoDataAttributesHoldersDistributionPercentage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenInfoDataAttributesHoldersDistributionPercentage`
        """
        model = TokenInfoDataAttributesHoldersDistributionPercentage()
        if include_optional:
            return TokenInfoDataAttributesHoldersDistributionPercentage(
                top_10 = 1.337,
                var_11_30 = 1.337,
                var_31_50 = 1.337,
                rest = 1.337
            )
        else:
            return TokenInfoDataAttributesHoldersDistributionPercentage(
        )
        """

    def testTokenInfoDataAttributesHoldersDistributionPercentage(self):
        """Test TokenInfoDataAttributesHoldersDistributionPercentage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
