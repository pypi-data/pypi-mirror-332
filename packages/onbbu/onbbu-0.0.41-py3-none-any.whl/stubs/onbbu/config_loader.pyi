from _typeshed import Incomplete
from onbbu.types import T as T

class ConfigLoader:
    base_dir: Incomplete
    def __init__(self, base_dir: str) -> None: ...
    def load_python_config(self, path: str, attribute: str, default: T | None) -> T | None: ...
