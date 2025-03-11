from os import getcwd
from sys import path
import asyncio

BASE_DIR: str = getcwd()

path.append(BASE_DIR)

from .manager import cli

__all__ = [
    
]


if __name__ == "__main__":
    asyncio.run(cli())