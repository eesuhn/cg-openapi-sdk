# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.coins_data_base_developer_data_code_additions_deletions4_weeks import CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks

class TestCoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks(unittest.TestCase):
    """CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks:
        """Test CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks`
        """
        model = CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks()
        if include_optional:
            return CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks(
                additions = 1.337,
                deletions = 1.337
            )
        else:
            return CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks(
        )
        """

    def testCoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks(self):
        """Test CoinsDataBaseDeveloperDataCodeAdditionsDeletions4Weeks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
