from collections import defaultdict
from typing import Literal
from datetime import datetime
from moxn.storage.base import StorageBackend
from moxn.models.task import Task
from moxn.models.request import Request


class InMemoryStorage(StorageBackend):
    def __init__(self):
        self._tasks: dict[str, dict[str, Task]] = defaultdict(dict)
        self._requests: dict[str, dict[str, Request]] = defaultdict(dict)
        self._last_polled: dict[tuple[str, Literal["task", "request"]], datetime] = {}

    async def store_task(self, task: Task) -> None:
        """Store a task version if not already stored."""
        task_id = str(task.id)  # Convert UUID to string if needed
        version_id = str(task.version_id)  # Convert UUID to string if needed
        if version_id not in self._tasks[task_id]:
            self._tasks[task_id][version_id] = task.model_copy(deep=True)

    async def store_request(self, request: Request) -> None:
        """Store a request version if not already stored."""
        request_id = str(request.id)  # Convert UUID to string if needed
        version_id = str(request.version_id)  # Convert UUID to string if needed
        if version_id not in self._requests[request_id]:
            self._requests[request_id][version_id] = request.model_copy(deep=True)

    async def get_task(self, task_id: str, version_id: str | None) -> Task:
        try:
            if version_id:
                return self._tasks[task_id][version_id]
            else:
                # Sort versions by created_at and return the latest
                return max(
                    self._tasks[task_id].values(), key=lambda task: task.created_at
                ).model_copy(deep=True)
        except KeyError:
            raise KeyError(f"Task not found: {task_id} version: {version_id}")

    async def get_request(self, request_id: str, version_id: str | None) -> Request:
        try:
            if version_id:
                return self._requests[request_id][version_id]
            else:
                # Sort versions by created_at and return the latest
                return max(
                    self._requests[request_id].values(),
                    key=lambda request: request.created_at,
                ).model_copy(deep=True)
        except KeyError:
            raise KeyError(f"Request not found: {request_id} version: {version_id}")

    async def has_task_version(self, task_id: str, version_id: str) -> bool:
        return task_id in self._tasks and version_id in self._tasks[task_id]

    async def has_request_version(self, request_id: str, version_id: str) -> bool:
        return request_id in self._requests and version_id in self._requests[request_id]

    async def clear(self) -> None:
        self._tasks.clear()
        self._requests.clear()

    async def get_last_polled(
        self, item_id: str, item_type: Literal["task", "request"]
    ) -> datetime | None:
        """Get the last time an item was polled for updates."""
        return self._last_polled.get((item_id, item_type))

    async def update_last_polled(
        self, item_id: str, item_type: Literal["task", "request"], timestamp: datetime
    ) -> None:
        """Update the last polled time for an item."""
        self._last_polled[(item_id, item_type)] = timestamp
