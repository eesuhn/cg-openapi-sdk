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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from coingecko-sdk.models.coins_data_base_links_repos_url import CoinsDataBaseLinksReposUrl
from typing import Optional, Set
from typing_extensions import Self

class CoinsDataBaseLinks(BaseModel):
    """
    links
    """ # noqa: E501
    homepage: Optional[List[StrictStr]] = Field(default=None, description="coin website url")
    whitepaper: Optional[List[StrictStr]] = Field(default=None, description="coin whitepaper url")
    blockchain_site: Optional[List[StrictStr]] = Field(default=None, description="coin block explorer url")
    official_forum_url: Optional[List[StrictStr]] = Field(default=None, description="coin official forum url")
    chat_url: Optional[List[StrictStr]] = Field(default=None, description="coin chat url")
    announcement_url: Optional[List[StrictStr]] = Field(default=None, description="coin announcement url")
    snapshot_url: Optional[StrictStr] = Field(default=None, description="coin snapshot url")
    twitter_screen_name: Optional[StrictStr] = Field(default=None, description="coin twitter handle")
    facebook_username: Optional[StrictStr] = Field(default=None, description="coin facebook username")
    bitcointalk_thread_identifier: Optional[StrictStr] = Field(default=None, description="coin bitcointalk thread identifier")
    telegram_channel_identifier: Optional[StrictStr] = Field(default=None, description="coin telegram channel identifier")
    subreddit_url: Optional[StrictStr] = Field(default=None, description="coin subreddit url")
    repos_url: Optional[CoinsDataBaseLinksReposUrl] = None
    __properties: ClassVar[List[str]] = ["homepage", "whitepaper", "blockchain_site", "official_forum_url", "chat_url", "announcement_url", "snapshot_url", "twitter_screen_name", "facebook_username", "bitcointalk_thread_identifier", "telegram_channel_identifier", "subreddit_url", "repos_url"]

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
        """Create an instance of CoinsDataBaseLinks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of repos_url
        if self.repos_url:
            _dict['repos_url'] = self.repos_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CoinsDataBaseLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "homepage": obj.get("homepage"),
            "whitepaper": obj.get("whitepaper"),
            "blockchain_site": obj.get("blockchain_site"),
            "official_forum_url": obj.get("official_forum_url"),
            "chat_url": obj.get("chat_url"),
            "announcement_url": obj.get("announcement_url"),
            "snapshot_url": obj.get("snapshot_url"),
            "twitter_screen_name": obj.get("twitter_screen_name"),
            "facebook_username": obj.get("facebook_username"),
            "bitcointalk_thread_identifier": obj.get("bitcointalk_thread_identifier"),
            "telegram_channel_identifier": obj.get("telegram_channel_identifier"),
            "subreddit_url": obj.get("subreddit_url"),
            "repos_url": CoinsDataBaseLinksReposUrl.from_dict(obj["repos_url"]) if obj.get("repos_url") is not None else None
        })
        return _obj


