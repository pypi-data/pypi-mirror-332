# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, constr 

class AuditProcess(BaseModel):
    """
    AuditProcess
    """
    name:  StrictStr = Field(...,alias="name") 
    run_id:  StrictStr = Field(...,alias="runId") 
    start_time: datetime = Field(..., alias="startTime")
    end_time: Optional[datetime] = Field(None, alias="endTime")
    succeeded: Optional[StrictBool] = None
    __properties = ["name", "runId", "startTime", "endTime", "succeeded"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuditProcess:
        """Create an instance of AuditProcess from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.end_time is None and "end_time" in self.__fields_set__:
            _dict['endTime'] = None

        # set to None if succeeded (nullable) is None
        # and __fields_set__ contains the field
        if self.succeeded is None and "succeeded" in self.__fields_set__:
            _dict['succeeded'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditProcess:
        """Create an instance of AuditProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditProcess.parse_obj(obj)

        _obj = AuditProcess.parse_obj({
            "name": obj.get("name"),
            "run_id": obj.get("runId"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "succeeded": obj.get("succeeded")
        })
        return _obj
