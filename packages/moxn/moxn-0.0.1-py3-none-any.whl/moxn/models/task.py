from typing import Sequence

from moxn import base_models
from moxn.models.request import Request
from pydantic import Field


class Task(base_models._Task):
    requests: Sequence[Request] = Field(default_factory=list)

    def get_request_by_name(self, name: str) -> Request:
        """Get a request by its name"""
        matching = [r for r in self.requests if r.name == name]
        if not matching:
            raise ValueError(f"No request found with name: {name}")
        if len(matching) > 1:
            raise ValueError(f"Multiple requests found with name: {name}")
        return matching[0]

    def get_request_by_id(self, request_id: str) -> Request:
        """Get a request by its ID"""
        matching = [r for r in self.requests if r.id == request_id]
        if not matching:
            raise ValueError(f"No request found with ID: {request_id}")
        if len(matching) > 1:
            raise ValueError(f"Multiple requests found with ID: {request_id}")
        return matching[0]
