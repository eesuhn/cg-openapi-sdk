# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from coingecko-sdk.models.pool_data_inner_attributes_price_change_percentage import PoolDataInnerAttributesPriceChangePercentage
from typing import Optional, Set
from typing_extensions import Self

class CategoriesPoolsDataInnerAttributes(BaseModel):
    """
    CategoriesPoolsDataInnerAttributes
    """ # noqa: E501
    base_token_price_usd: Optional[StrictStr] = None
    base_token_price_native_currency: Optional[StrictStr] = None
    quote_token_price_usd: Optional[StrictStr] = None
    quote_token_price_native_currency: Optional[StrictStr] = None
    base_token_price_quote_token: Optional[StrictStr] = None
    quote_token_price_base_token: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    pool_created_at: Optional[datetime] = None
    fdv_usd: Optional[StrictStr] = None
    market_cap_usd: Optional[StrictStr] = None
    price_change_percentage: Optional[PoolDataInnerAttributesPriceChangePercentage] = None
    reserve_in_usd: Optional[StrictStr] = None
    h24_volume_usd: Optional[StrictStr] = None
    h24_tx_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["base_token_price_usd", "base_token_price_native_currency", "quote_token_price_usd", "quote_token_price_native_currency", "base_token_price_quote_token", "quote_token_price_base_token", "address", "name", "pool_created_at", "fdv_usd", "market_cap_usd", "price_change_percentage", "reserve_in_usd", "h24_volume_usd", "h24_tx_count"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CategoriesPoolsDataInnerAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of price_change_percentage
        if self.price_change_percentage:
            _dict['price_change_percentage'] = self.price_change_percentage.to_dict()
        # set to None if fdv_usd (nullable) is None
        # and model_fields_set contains the field
        if self.fdv_usd is None and "fdv_usd" in self.model_fields_set:
            _dict['fdv_usd'] = None

        # set to None if market_cap_usd (nullable) is None
        # and model_fields_set contains the field
        if self.market_cap_usd is None and "market_cap_usd" in self.model_fields_set:
            _dict['market_cap_usd'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CategoriesPoolsDataInnerAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base_token_price_usd": obj.get("base_token_price_usd"),
            "base_token_price_native_currency": obj.get("base_token_price_native_currency"),
            "quote_token_price_usd": obj.get("quote_token_price_usd"),
            "quote_token_price_native_currency": obj.get("quote_token_price_native_currency"),
            "base_token_price_quote_token": obj.get("base_token_price_quote_token"),
            "quote_token_price_base_token": obj.get("quote_token_price_base_token"),
            "address": obj.get("address"),
            "name": obj.get("name"),
            "pool_created_at": obj.get("pool_created_at"),
            "fdv_usd": obj.get("fdv_usd"),
            "market_cap_usd": obj.get("market_cap_usd"),
            "price_change_percentage": PoolDataInnerAttributesPriceChangePercentage.from_dict(obj["price_change_percentage"]) if obj.get("price_change_percentage") is not None else None,
            "reserve_in_usd": obj.get("reserve_in_usd"),
            "h24_volume_usd": obj.get("h24_volume_usd"),
            "h24_tx_count": obj.get("h24_tx_count")
        })
        return _obj


