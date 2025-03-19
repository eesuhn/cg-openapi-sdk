# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.exchange_data import ExchangeData

class TestExchangeData(unittest.TestCase):
    """ExchangeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeData:
        """Test ExchangeData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeData`
        """
        model = ExchangeData()
        if include_optional:
            return ExchangeData(
                name = '',
                year_established = 1.337,
                country = '',
                description = '',
                url = '',
                image = '',
                facebook_url = '',
                reddit_url = '',
                telegram_url = '',
                slack_url = '',
                other_url_1 = '',
                other_url_2 = '',
                twitter_handle = '',
                has_trading_incentive = True,
                centralized = True,
                public_notice = '',
                alert_notice = '',
                trust_score = 1.337,
                trust_score_rank = 1.337,
                trade_volume_24h_btc = 1.337,
                trade_volume_24h_btc_normalized = 1.337,
                coins = 1.337,
                pairs = 1.337,
                tickers = [
                    null
                    ]
            )
        else:
            return ExchangeData(
        )
        """

    def testExchangeData(self):
        """Test ExchangeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
