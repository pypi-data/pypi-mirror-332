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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.application_context_class_loader_defined_packages_inner import ApplicationContextClassLoaderDefinedPackagesInner
from cdo_sdk_python.models.application_context_class_loader_parent import ApplicationContextClassLoaderParent
from cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module import ApplicationContextClassLoaderParentUnnamedModule
from typing import Optional, Set
from typing_extensions import Self

class ApplicationContextClassLoader(BaseModel):
    """
    ApplicationContextClassLoader
    """ # noqa: E501
    default_assertion_status: Optional[StrictBool] = Field(default=None, alias="defaultAssertionStatus")
    defined_packages: Optional[List[ApplicationContextClassLoaderDefinedPackagesInner]] = Field(default=None, alias="definedPackages")
    name: Optional[StrictStr] = None
    parent: Optional[ApplicationContextClassLoaderParent] = None
    registered_as_parallel_capable: Optional[StrictBool] = Field(default=None, alias="registeredAsParallelCapable")
    unnamed_module: Optional[ApplicationContextClassLoaderParentUnnamedModule] = Field(default=None, alias="unnamedModule")
    __properties: ClassVar[List[str]] = ["defaultAssertionStatus", "definedPackages", "name", "parent", "registeredAsParallelCapable", "unnamedModule"]

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
        """Create an instance of ApplicationContextClassLoader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in defined_packages (list)
        _items = []
        if self.defined_packages:
            for _item in self.defined_packages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['definedPackages'] = _items
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unnamed_module
        if self.unnamed_module:
            _dict['unnamedModule'] = self.unnamed_module.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationContextClassLoader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "defaultAssertionStatus": obj.get("defaultAssertionStatus"),
            "definedPackages": [ApplicationContextClassLoaderDefinedPackagesInner.from_dict(_item) for _item in obj["definedPackages"]] if obj.get("definedPackages") is not None else None,
            "name": obj.get("name"),
            "parent": ApplicationContextClassLoaderParent.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "registeredAsParallelCapable": obj.get("registeredAsParallelCapable"),
            "unnamedModule": ApplicationContextClassLoaderParentUnnamedModule.from_dict(obj["unnamedModule"]) if obj.get("unnamedModule") is not None else None
        })
        return _obj


