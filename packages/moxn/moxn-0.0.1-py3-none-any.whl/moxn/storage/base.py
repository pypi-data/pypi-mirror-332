from abc import ABC, abstractmethod
from typing import TypeVar
from moxn.models.task import Task
from moxn.models.request import Request

T = TypeVar("T", Task, Request)


class StorageBackend(ABC):
    """Abstract base class for storage backends."""

    @abstractmethod
    async def store_task(self, task: Task) -> None:
        """Store a task version."""
        pass

    @abstractmethod
    async def store_request(self, request: Request) -> None:
        """Store a request version."""
        pass

    @abstractmethod
    async def get_task(self, task_id: str, version_id: str) -> Task:
        """Retrieve a task version."""
        pass

    @abstractmethod
    async def get_request(self, request_id: str, version_id: str) -> Request:
        """Retrieve a request version."""
        pass

    @abstractmethod
    async def has_task_version(self, task_id: str, version_id: str) -> bool:
        """Check if a task version exists."""
        pass

    @abstractmethod
    async def has_request_version(self, request_id: str, version_id: str) -> bool:
        """Check if a request version exists."""
        pass

    @abstractmethod
    async def clear(self) -> None:
        """Clear all stored data."""
        pass
