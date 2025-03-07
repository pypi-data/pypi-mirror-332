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
from cdo_sdk_python.models.domain_settings import DomainSettings
from typing import Optional, Set
from typing_extensions import Self

class Deployed(BaseModel):
    """
    Indicates that the settings have been successfully configured and deployed.
    """ # noqa: E501
    auto_deploy_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether changes to ZTNA settings are automatically deployed to the device. Note: This applies only to ZTNA-specific changes and does not affect the deployment of other pending changes.", alias="autoDeployEnabled")
    domain_settings: Optional[List[DomainSettings]] = Field(default=None, description="Configuration that defines how Secure Client communicates with the device.", alias="domainSettings")
    __properties: ClassVar[List[str]] = ["autoDeployEnabled", "domainSettings"]

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
        """Create an instance of Deployed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in domain_settings (list)
        _items = []
        if self.domain_settings:
            for _item in self.domain_settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['domainSettings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Deployed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoDeployEnabled": obj.get("autoDeployEnabled"),
            "domainSettings": [DomainSettings.from_dict(_item) for _item in obj["domainSettings"]] if obj.get("domainSettings") is not None else None
        })
        return _obj


