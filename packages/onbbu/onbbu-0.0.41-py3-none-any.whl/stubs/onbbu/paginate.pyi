from onbbu.types import T as T, U as U
from typing import Callable, Generic

class PaginateDTO:
    page: int
    limit: int
    def validate_page(cls, v: int): ...
    def validate_limit(cls, v: int): ...

class Paginate(Generic[T]):
    page: int
    limit: int
    total: int
    total_page: int
    data: list[T]
    @staticmethod
    def calculate_total_pages(total: int, limit: int) -> int: ...

def createPaginateResponse(paginate: Paginate[T], transform: Callable[[list[T]], list[U]]) -> Paginate[U]: ...
