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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class JobReport(BaseModel):
    """
    JobReport
    """ # noqa: E501
    id: StrictStr = Field(description="caller-provided unique identifier for the job")
    description: Optional[StrictStr] = Field(default=None, description="caller-provided description of the job")
    status: StrictStr = Field(description="status of the job")
    status_code: StrictInt = Field(description="HTTP code providing status of the job.", alias="statusCode")
    submitted: Optional[StrictStr] = Field(default=None, description="timestamp when the job was submitted; in ISO-8601 format")
    completed: Optional[StrictStr] = Field(default=None, description="timestamp when the job completed - in ISO-8601 format. Present if status is SUCCEEDED or FAILED.")
    result_url: StrictStr = Field(description="URL where the result of the job can be retrieved. Equivalent to a Location header in HTTP.", alias="resultURL")
    __properties: ClassVar[List[str]] = ["id", "description", "status", "statusCode", "submitted", "completed", "resultURL"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RUNNING', 'SUCCEEDED', 'FAILED']):
            raise ValueError("must be one of enum values ('RUNNING', 'SUCCEEDED', 'FAILED')")
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
        """Create an instance of JobReport from a JSON string"""
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
        """Create an instance of JobReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "statusCode": obj.get("statusCode"),
            "submitted": obj.get("submitted"),
            "completed": obj.get("completed"),
            "resultURL": obj.get("resultURL")
        })
        return _obj


