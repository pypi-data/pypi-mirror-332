from argparse import ArgumentParser, Namespace
from onbbu.database import DatabaseManager as DatabaseManager
from onbbu.http import EndpointHttpType as EndpointHttpType, HTTPMethod as HTTPMethod, JSONResponse as JSONResponse, Request as Request, Response as Response, ResponseNotFoundError as ResponseNotFoundError, ResponseValidationError as ResponseValidationError, ResponseValueError as ResponseValueError
from onbbu.manager import BaseCommand as BaseCommand, COMMANDS as COMMANDS, register_command as register_command
from onbbu.paginate import Paginate as Paginate, PaginateDTO as PaginateDTO, createPaginateResponse as createPaginateResponse
from typing import Any

__all__ = ['COMMANDS', 'BaseCommand', 'register_command', 'DatabaseManager', 'HTTPMethod', 'EndpointHttpType', 'Paginate', 'PaginateDTO', 'createPaginateResponse', 'Request', 'JSONResponse', 'Response', 'ResponseNotFoundError', 'ResponseValidationError', 'ResponseValueError']

class CommandMigrate(BaseCommand):
    name: str
    help: str
    async def handle(self, *args: Namespace, **kwargs: dict[str, Any]) -> None: ...

class CommandCreateModule(BaseCommand):
    name: str
    help: str
    async def add_arguments(self, parser: ArgumentParser): ...
    async def handle(self, *args: Namespace, **kwargs: dict[str, Any]) -> None: ...

class CommandRunServer(BaseCommand):
    name: str
    help: str
    async def handle(self, *args: Namespace, **kwargs: dict[str, Any]) -> None: ...
