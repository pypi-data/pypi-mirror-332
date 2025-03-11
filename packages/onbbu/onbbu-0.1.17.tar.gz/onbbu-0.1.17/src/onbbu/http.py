from dataclasses import asdict, is_dataclass, dataclass
from enum import Enum
from typing import Awaitable, Callable, Generic, Optional, TypeVar
import multiprocessing
from contextlib import asynccontextmanager
from os import getenv

from starlette.applications import Starlette
from starlette.responses import JSONResponse as StarletteJSONResponse
from starlette.requests import Request as StarletteRequest
from starlette.routing import Route
import uvicorn

from onbbu.database import DatabaseManager, database

from pydantic import ValidationError

from onbbu.logger import LogLevel, logger

T = TypeVar("T")


class Request(StarletteRequest):
    pass


class JSONResponse(StarletteJSONResponse):
    pass


class ResponseNotFoundError(JSONResponse):

    def render(self, content: str) -> bytes:
        content = {"error": content}  # type: ignore

        return super().render(content, status_code=404)  # type: ignore


class ResponseValueError(JSONResponse):

    def render(self, content: ValueError) -> bytes:
        content = {"error": str(content)}  # type: ignore

        return super().render(content, status_code=500)  # type: ignore


class ResponseValidationError(JSONResponse):

    def render(self, content: ValidationError) -> bytes:
        content = {"detail": content.errors()}  # type: ignore

        return super().render(content, status_code=400)  # type: ignore


class Response(Generic[T], JSONResponse):

    def render(self, content: T) -> bytes:  # type: ignore

        if is_dataclass(content):
            content = asdict(content)  # type: ignore

        elif isinstance(content, list):
            content = [
                (asdict(item) if is_dataclass(item) else item) for item in content  # type: ignore
            ]

        return super().render(content)


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


EndpointHttpType = Callable[[Request], Awaitable[JSONResponse]]


@dataclass(frozen=True, slots=True)
class RouteDTO:
    path: str
    endpoint: EndpointHttpType
    method: HTTPMethod


class RouterHttp:
    __router: list[Route]
    __prefix: str

    def __init__(self, prefix: str = ""):
        self.__router = []
        self.__prefix = prefix.rstrip("/")

    def add_route(self, dto: RouteDTO) -> None:

        full_path: str = f"{self.__prefix}{dto.path}"

        self.__router.append(
            Route(path=full_path, endpoint=dto.endpoint, methods=[dto.method.value])
        )

    def add_routes(self, dtos: list[RouteDTO]) -> None:
        for dto in dtos:
            self.add_route(dto)

    def get_router(self) -> list[Route]:
        return self.__router

    def get_routes(self) -> list[str]:
        return [route.path for route in self.__router]


class ServerHttp:
    database: DatabaseManager
    host: str
    port: int
    environment: str
    reload: bool
    workers: int
    server: Starlette

    def __init__(self, environment: str, port: Optional[int]):
        self.host = "0.0.0.0"
        self.port = port or 8000
        self.environment = environment
        self.reload = self.environment == "development"
        self.workers = 1 if self.reload else max(2, multiprocessing.cpu_count() - 1)

        self.server = Starlette(debug=True, routes=[], lifespan=self._lifespan)

        self.database = database

    @asynccontextmanager
    async def _lifespan(self, app: Starlette):
        """Gestor de eventos de vida para FastAPI"""
        await self.database.init()
        yield
        await self.database.close()

    def include_router(self, router: RouterHttp) -> None:
        """Agrega todas las rutas de un RouterHttp a la aplicación"""
        self.server.router.routes.extend(router.get_router())


server_http: ServerHttp = ServerHttp(
    port=int(getenv("HTTP_PORT", "8000")),
    environment=getenv("ENVIRONMENT", "development"),
)

def runserver(server_http: ServerHttp) -> None:
    logger.log(
        level=LogLevel.INFO,
        message=f"🚀 Iniciando servidor en {server_http.host}:{server_http.port} ...",
        extra_data={},
    )

    for route in server_http.server.routes:
        logger.log(
            level=LogLevel.INFO,
            message=f"🔗 {route.path} -> {route.name} ({route.methods})",  # type: ignore
            extra_data={},
        )

    uvicorn.run(server_http.server, host=server_http.host, port=server_http.port)