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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from coingecko-sdk.models.companies_treasury_companies_inner import CompaniesTreasuryCompaniesInner
from typing import Optional, Set
from typing_extensions import Self

class CompaniesTreasury(BaseModel):
    """
    CompaniesTreasury
    """ # noqa: E501
    total_holdings: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total btc/eth holdings of companies")
    total_value_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total btc/eth holdings value in usd")
    market_cap_dominance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="market cap dominance")
    companies: Optional[List[CompaniesTreasuryCompaniesInner]] = None
    __properties: ClassVar[List[str]] = ["total_holdings", "total_value_usd", "market_cap_dominance", "companies"]

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
        """Create an instance of CompaniesTreasury from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in companies (list)
        _items = []
        if self.companies:
            for _item_companies in self.companies:
                if _item_companies:
                    _items.append(_item_companies.to_dict())
            _dict['companies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompaniesTreasury from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_holdings": obj.get("total_holdings"),
            "total_value_usd": obj.get("total_value_usd"),
            "market_cap_dominance": obj.get("market_cap_dominance"),
            "companies": [CompaniesTreasuryCompaniesInner.from_dict(_item) for _item in obj["companies"]] if obj.get("companies") is not None else None
        })
        return _obj


