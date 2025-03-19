# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko_sdk.models.coins_market_chart_range import CoinsMarketChartRange

class TestCoinsMarketChartRange(unittest.TestCase):
    """CoinsMarketChartRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoinsMarketChartRange:
        """Test CoinsMarketChartRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsMarketChartRange`
        """
        model = CoinsMarketChartRange()
        if include_optional:
            return CoinsMarketChartRange(
                prices = [[1704067241331,42261.0406175669],[1704070847420,42493.2764087546],[1704074443652,42654.0731066594]],
                market_caps = [[1704067241331,8.27596236151196E11],[1704070847420,8.31531023621411E11],[1704074443652,8.35499399014932E11]],
                total_volumes = [[1704067241331,1.43057691709498E10],[1704070847420,1.41302053761709E10],[1704074443652,1.36973829022424E10]]
            )
        else:
            return CoinsMarketChartRange(
        )
        """

    def testCoinsMarketChartRange(self):
        """Test CoinsMarketChartRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
