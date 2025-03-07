# coding: utf-8

"""
    Cisco Security Cloud Control API

    Use the documentation to explore the endpoints Security Cloud Control has to offer

    The version of the OpenAPI document: 1.5.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.deployed import Deployed
from cdo_sdk_python.models.staged import Staged
from typing import Optional, Set
from typing_extensions import Self

class UniversalZtnaSettings(BaseModel):
    """
    (FMC-managed FTDs only) Universal Zero-Trust Network Access (ZTNA) configuration.
    """ # noqa: E501
    deployed: Optional[Deployed] = None
    staged: Optional[Staged] = None
    universal_ztna_configured: Optional[StrictBool] = Field(default=None, description="Indicates whether a device is configured for Zero Trust Network Access (ZTNA).", alias="universalZtnaConfigured")
    universal_ztna_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether a device is enabled for Zero Trust Network Access (ZTNA).", alias="universalZtnaEnabled")
    universal_ztna_supported: Optional[StrictBool] = Field(default=None, description="Indicates whether a device supports Zero Trust Network Access (ZTNA).", alias="universalZtnaSupported")
    __properties: ClassVar[List[str]] = ["deployed", "staged", "universalZtnaConfigured", "universalZtnaEnabled", "universalZtnaSupported"]

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
        """Create an instance of UniversalZtnaSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deployed
        if self.deployed:
            _dict['deployed'] = self.deployed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of staged
        if self.staged:
            _dict['staged'] = self.staged.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniversalZtnaSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deployed": Deployed.from_dict(obj["deployed"]) if obj.get("deployed") is not None else None,
            "staged": Staged.from_dict(obj["staged"]) if obj.get("staged") is not None else None,
            "universalZtnaConfigured": obj.get("universalZtnaConfigured"),
            "universalZtnaEnabled": obj.get("universalZtnaEnabled"),
            "universalZtnaSupported": obj.get("universalZtnaSupported")
        })
        return _obj


