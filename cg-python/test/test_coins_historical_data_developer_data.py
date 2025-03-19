# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.coins_historical_data_developer_data import CoinsHistoricalDataDeveloperData

class TestCoinsHistoricalDataDeveloperData(unittest.TestCase):
    """CoinsHistoricalDataDeveloperData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsHistoricalDataDeveloperData:
        """Test CoinsHistoricalDataDeveloperData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsHistoricalDataDeveloperData`
        """
        model = CoinsHistoricalDataDeveloperData()
        if include_optional:
            return CoinsHistoricalDataDeveloperData(
                forks = 1.337,
                stars = 1.337,
                subscribers = 1.337,
                total_issues = 1.337,
                closed_issues = 1.337,
                pull_requests_merged = 1.337,
                pull_request_contributors = 1.337,
                code_additions_deletions_4_weeks = coingecko-sdk.models.coins_historical_data_developer_data_code_additions_deletions_4_weeks.CoinsHistoricalData_developer_data_code_additions_deletions_4_weeks(
                    additions = 1.337, 
                    deletions = 1.337, ),
                commit_count_4_weeks = 1.337
            )
        else:
            return CoinsHistoricalDataDeveloperData(
        )
        """

    def testCoinsHistoricalDataDeveloperData(self):
        """Test CoinsHistoricalDataDeveloperData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
