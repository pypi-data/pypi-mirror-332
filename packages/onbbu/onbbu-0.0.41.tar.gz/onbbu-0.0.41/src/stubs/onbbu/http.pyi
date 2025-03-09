from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from onbbu.database import DatabaseManager as DatabaseManager
from onbbu.types import T as T
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse
from typing import Awaitable, Callable, Generic

class Request(StarletteRequest): ...

class ResponseNotFoundError(JSONResponse, Generic[T]):
    def render(self, content: T) -> bytes: ...

class ResponseValueError(JSONResponse, Generic[T]):
    def render(self, content: T) -> bytes: ...

class ResponseValidationError(JSONResponse, Generic[T]):
    def render(self, content: T) -> bytes: ...

class Response(JSONResponse, Generic[T]):
    def render(self, content: T) -> bytes: ...

class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
EndpointHttpType = Callable[[Request], Awaitable[JSONResponse]]

class RouterHttp:
    def __init__(self, prefix: str = '') -> None: ...
    def add_route(self, path: str, endpoint: EndpointHttpType, method: HTTPMethod): ...
    def get_router(self): ...
    def get_routes(self): ...
    def get_endpoints(self): ...

class ServerHttp:
    database: DatabaseManager
    host: str
    port: Incomplete
    environment: Incomplete
    reload: Incomplete
    workers: Incomplete
    server: Incomplete
    config: Incomplete
    def __init__(self, environment: str, database: DatabaseManager, port: int = 8000) -> None: ...
    def include_router(self, router: RouterHttp): ...

@dataclass(frozen=True, slots=True)
class ConfigInit:
    http: ServerHttp
