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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class FmcObjectOverride(BaseModel):
    """
    Specify a list of objects to override. All objects that have been marked as overridable in the template must be defined here. Note: Any overrides defined here that are not present in the template configuration will be ignored.
    """ # noqa: E501
    name: StrictStr = Field(description="Specify the name of the object to override.")
    type: StrictStr = Field(description="Specify the type of the object to override. The type should match the type of the object used in the template.")
    uid: StrictStr = Field(description="Specify the unique identifier, represented as a UUID, of the object to override.")
    value: StrictStr = Field(description="Specify the value to override the object with.")
    __properties: ClassVar[List[str]] = ["name", "type", "uid", "value"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Network', 'Host', 'FQDN', 'Range']):
            raise ValueError("must be one of enum values ('Network', 'Host', 'FQDN', 'Range')")
        return value

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
        """Create an instance of FmcObjectOverride from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FmcObjectOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "uid": obj.get("uid"),
            "value": obj.get("value")
        })
        return _obj


