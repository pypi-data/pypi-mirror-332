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
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.cluster_node import ClusterNode
from typing import Optional, Set
from typing_extensions import Self

class FtdClusterInfo(BaseModel):
    """
    (Device Clusters managed by FMC only) Clustering information. Note: Security Cloud Control represents all of the nodes on an FTD cluster in a single device record with the UID of the cluster control node.
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster on the FMC.", alias="clusterName")
    cluster_node_status: Optional[StrictStr] = Field(default=None, description="(on-prem FMC-managed FTDs only) Information on the type of this node in the FTD cluster. Note: Each node in an on-prem-FMC-managed FTD cluster is represented as a separate device entry in the API.", alias="clusterNodeStatus")
    cluster_node_type: Optional[StrictStr] = Field(default=None, description="(on-prem FMC-managed FTDs only) Information on the type of this node in the FTD cluster. Note: Each node in an on-prem-FMC-managed FTD cluster is represented as a separate device entry in the API.", alias="clusterNodeType")
    cluster_uid: Optional[StrictStr] = Field(default=None, description="The unique identifier, represented as a UUID, of the cluster, on the FMC", alias="clusterUid")
    control_node: Optional[ClusterNode] = Field(default=None, alias="controlNode")
    data_nodes: Optional[List[ClusterNode]] = Field(default=None, description="(cdFMC-managed FTDs only) Information on the data nodes, which are individual units within a cluster that process and forward network traffic based on policies and configurations managed by the control node.", alias="dataNodes")
    __properties: ClassVar[List[str]] = ["clusterName", "clusterNodeStatus", "clusterNodeType", "clusterUid", "controlNode", "dataNodes"]

    @field_validator('cluster_node_status')
    def cluster_node_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ADDED_OUT_OF_BOX', 'DISABLED', 'JOINING', 'NORMAL', 'NOT_AVAILABLE', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('ADDED_OUT_OF_BOX', 'DISABLED', 'JOINING', 'NORMAL', 'NOT_AVAILABLE', 'UNKNOWN')")
        return value

    @field_validator('cluster_node_type')
    def cluster_node_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CONTROL', 'DATA']):
            raise ValueError("must be one of enum values ('CONTROL', 'DATA')")
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
        """Create an instance of FtdClusterInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of control_node
        if self.control_node:
            _dict['controlNode'] = self.control_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data_nodes (list)
        _items = []
        if self.data_nodes:
            for _item in self.data_nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataNodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FtdClusterInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "clusterNodeStatus": obj.get("clusterNodeStatus"),
            "clusterNodeType": obj.get("clusterNodeType"),
            "clusterUid": obj.get("clusterUid"),
            "controlNode": ClusterNode.from_dict(obj["controlNode"]) if obj.get("controlNode") is not None else None,
            "dataNodes": [ClusterNode.from_dict(_item) for _item in obj["dataNodes"]] if obj.get("dataNodes") is not None else None
        })
        return _obj


