# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from coingecko-sdk.models.nft_data import NFTData

class TestNFTData(unittest.TestCase):
    """NFTData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NFTData:
        """Test NFTData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NFTData`
        """
        model = NFTData()
        if include_optional:
            return NFTData(
                id = '',
                contract_address = '',
                asset_platform_id = '',
                name = '',
                symbol = '',
                image = coingecko-sdk.models.nft_data_image.NFTData_image(
                    small = '', 
                    small_2x = '', ),
                banner_image = coingecko-sdk.models.nft_data_banner_image.NFTData_banner_image(
                    small = '', ),
                description = '',
                native_currency = '',
                native_currency_symbol = '',
                market_cap_rank = 1.337,
                floor_price = coingecko-sdk.models.nft_data_floor_price.NFTData_floor_price(
                    native_currency = 1.337, 
                    usd = 1.337, ),
                market_cap = coingecko-sdk.models.nft_data_market_cap.NFTData_market_cap(
                    native_currency = 1.337, 
                    usd = 1.337, ),
                volume_24h = coingecko-sdk.models.nft_data_volume_24h.NFTData_volume_24h(
                    native_currency = 1.337, 
                    usd = 1.337, ),
                floor_price_in_usd_24h_percentage_change = 1.337,
                floor_price_24h_percentage_change = coingecko-sdk.models.nft_data_floor_price_24h_percentage_change.NFTData_floor_price_24h_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                market_cap_24h_percentage_change = coingecko-sdk.models.nft_data_market_cap_24h_percentage_change.NFTData_market_cap_24h_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                volume_24h_percentage_change = coingecko-sdk.models.nft_data_volume_24h_percentage_change.NFTData_volume_24h_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                number_of_unique_addresses = 1.337,
                number_of_unique_addresses_24h_percentage_change = 1.337,
                volume_in_usd_24h_percentage_change = 1.337,
                total_supply = 1.337,
                one_day_sales = 1.337,
                one_day_sales_24h_percentage_change = 1.337,
                one_day_average_sale_price = 1.337,
                one_day_average_sale_price_24h_percentage_change = 1.337,
                links = coingecko-sdk.models.nft_data_links.NFTData_links(
                    homepage = '', 
                    twitter = '', 
                    discord = '', ),
                floor_price_7d_percentage_change = coingecko-sdk.models.nft_data_floor_price_7d_percentage_change.NFTData_floor_price_7d_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                floor_price_14d_percentage_change = coingecko-sdk.models.nft_data_floor_price_14d_percentage_change.NFTData_floor_price_14d_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                floor_price_30d_percentage_change = coingecko-sdk.models.nft_data_floor_price_30d_percentage_change.NFTData_floor_price_30d_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                floor_price_60d_percentage_change = coingecko-sdk.models.nft_data_floor_price_60d_percentage_change.NFTData_floor_price_60d_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                floor_price_1y_percentage_change = coingecko-sdk.models.nft_data_floor_price_1y_percentage_change.NFTData_floor_price_1y_percentage_change(
                    usd = 1.337, 
                    native_currency = 1.337, ),
                explorers = [
                    coingecko-sdk.models.nft_data_explorers_inner.NFTData_explorers_inner(
                        name = '', 
                        link = '', )
                    ],
                user_favorites_count = 1.337,
                ath = coingecko-sdk.models.nft_data_ath.NFTData_ath(
                    native_currency = 1.337, 
                    usd = 1.337, ),
                ath_change_percentage = coingecko-sdk.models.nft_data_ath_change_percentage.NFTData_ath_change_percentage(
                    native_currency = 1.337, 
                    usd = 1.337, ),
                ath_date = coingecko-sdk.models.nft_data_ath_date.NFTData_ath_date(
                    native_currency = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    usd = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return NFTData(
        )
        """

    def testNFTData(self):
        """Test NFTData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
