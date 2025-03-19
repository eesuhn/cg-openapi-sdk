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
from coingecko-sdk.models.coins_historical_data_developer_data_code_additions_deletions4_weeks import CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks
from typing import Optional, Set
from typing_extensions import Self

class CoinsHistoricalDataDeveloperData(BaseModel):
    """
    coin developer data
    """ # noqa: E501
    forks: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository forks")
    stars: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository stars")
    subscribers: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository subscribers")
    total_issues: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository total issues")
    closed_issues: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository closed issues")
    pull_requests_merged: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository pull requests merged")
    pull_request_contributors: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin repository pull request contributors")
    code_additions_deletions_4_weeks: Optional[CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks] = None
    commit_count_4_weeks: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="coin commit count 4 weeks")
    __properties: ClassVar[List[str]] = ["forks", "stars", "subscribers", "total_issues", "closed_issues", "pull_requests_merged", "pull_request_contributors", "code_additions_deletions_4_weeks", "commit_count_4_weeks"]

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
        """Create an instance of CoinsHistoricalDataDeveloperData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code_additions_deletions_4_weeks
        if self.code_additions_deletions_4_weeks:
            _dict['code_additions_deletions_4_weeks'] = self.code_additions_deletions_4_weeks.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CoinsHistoricalDataDeveloperData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forks": obj.get("forks"),
            "stars": obj.get("stars"),
            "subscribers": obj.get("subscribers"),
            "total_issues": obj.get("total_issues"),
            "closed_issues": obj.get("closed_issues"),
            "pull_requests_merged": obj.get("pull_requests_merged"),
            "pull_request_contributors": obj.get("pull_request_contributors"),
            "code_additions_deletions_4_weeks": CoinsHistoricalDataDeveloperDataCodeAdditionsDeletions4Weeks.from_dict(obj["code_additions_deletions_4_weeks"]) if obj.get("code_additions_deletions_4_weeks") is not None else None,
            "commit_count_4_weeks": obj.get("commit_count_4_weeks")
        })
        return _obj


