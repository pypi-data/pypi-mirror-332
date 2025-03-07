# coding: utf-8

"""
    Terra Scientific Pipelines Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class QuotaWithDetails(BaseModel):
    """
    Object containing the pipeline identifier, quota limit, and quota usage of a Pipeline. 
    """ # noqa: E501
    pipeline_name: StrictStr = Field(description="The identifier string for the Pipeline. ", alias="pipelineName")
    quota_limit: StrictInt = Field(description="Maximum allowable quota for the pipeline ", alias="quotaLimit")
    quota_consumed: StrictInt = Field(description="Quota consumed by the user ", alias="quotaConsumed")
    quota_units: StrictStr = Field(description="Units for pipeline quota ", alias="quotaUnits")
    __properties: ClassVar[List[str]] = ["pipelineName", "quotaLimit", "quotaConsumed", "quotaUnits"]

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
        """Create an instance of QuotaWithDetails from a JSON string"""
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
        """Create an instance of QuotaWithDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pipelineName": obj.get("pipelineName"),
            "quotaLimit": obj.get("quotaLimit"),
            "quotaConsumed": obj.get("quotaConsumed"),
            "quotaUnits": obj.get("quotaUnits")
        })
        return _obj


