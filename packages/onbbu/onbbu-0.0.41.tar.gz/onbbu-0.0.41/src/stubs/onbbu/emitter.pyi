from collections import defaultdict
from enum import Enum
from typing import Callable

class Event(Enum):
    DEFAULT_DISCOUNT = 'add_default_discounts'

class EventEmitter:
    events: defaultdict[str, list[Callable[..., None]]]
    def __init__(self) -> None: ...
    def on(self, event: Event, callback: Callable[..., None]) -> None: ...
    def emit(self, event: Event, *args: object, **kwargs: object) -> None: ...

emitter: EventEmitter
