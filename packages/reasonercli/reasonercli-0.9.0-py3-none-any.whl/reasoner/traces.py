from datetime import datetime
from typing import List, TypedDict, Union

TRACES_LIMIT = 50


class Trace(TypedDict):
    uid: str
    query: str
    created_at: str
    updated_at: str
    status: str


class TraceCursor(TypedDict):
    before_created_at: Union[datetime, None]


class GetTracesResponse(TypedDict):
    traces: List[Trace]
    next: TraceCursor


class Traces:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    def list(self, next: TraceCursor = None, limit: int = TRACES_LIMIT):
        params = {}
        if next is not None:
            params["before_created_at"] = next["before_created_at"]
        if limit is not None:
            params["limit"] = limit

        response = self.client.get(f"{self.base_url}/public/v1/traces", params=params)
        response.raise_for_status()

        traces_response = GetTracesResponse(**response.json())
        return traces_response["traces"], traces_response["next"]

    def get(self, response_uid: str):
        response = self.client.get(
            f"{self.base_url}/public/v1/traces/{response_uid}",
        )
        response.raise_for_status()
        response_json = response.json() or {}
        return response_json


class TracesAsync:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    async def list(self, next: TraceCursor = None, limit: int = TRACES_LIMIT):
        params = {}
        if next is not None:
            params["before_created_at"] = next["before_created_at"]
        if limit is not None:
            params["limit"] = limit

        response = await self.client.get(
            f"{self.base_url}/public/v1/traces", params=params
        )
        response.raise_for_status()

        traces_response = GetTracesResponse(**response.json())
        return traces_response["traces"], traces_response["next"]

    async def get(self, response_uid: str):
        response = await self.client.get(
            f"{self.base_url}/public/v1/traces/{response_uid}",
        )
        response.raise_for_status()
        response_json = response.json() or {}
        return response_json
