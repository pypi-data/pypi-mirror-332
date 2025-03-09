from argparse import ArgumentParser, HelpFormatter, Namespace
import importlib
import os
import pkgutil
from typing import Any, Dict, List, Optional, Type

from onbbu.emitter import EventEmitter


async def create_module(path: str, name: str) -> None:

    folders: list[str] = [
        "domain",
        "domain/entities",
        "domain/services",
        "application/dto",
        "application/commands",
        "application/use_cases",
        "infrastructure/adapters",
        "infrastructure/cache",
        "infrastructure/logger",
        "infrastructure/messaging",
        "infrastructure/persistence/models",
        "infrastructure/persistence/repositories",
        "infrastructure/services",
        "infrastructure/storage",
        "infrastructure/transformers",
    ]

    for folder in folders:
        dir_path = os.path.join(path, "pkg", name, folder)
        os.makedirs(dir_path, exist_ok=True)


class BaseCommand:
    """Base class for all commands."""
    name: str
    help: str = "Base command description"
    parser: Optional[ArgumentParser]

    def __init__(self, emitter: EventEmitter) -> None:
        self.parser: Optional[ArgumentParser] = None
        self.emitter = emitter

    async def add_arguments(self, parser: ArgumentParser) -> None:
        """Override this method to add custom arguments."""
        pass

    async def handle(self, *args: Namespace, **kwargs: dict[str, Any]) -> None:
        """Override this method to implement command logic."""
        raise NotImplementedError("Subclasses must implement handle()")

    async def emit_event(self, event_name: str, *args: Any) -> None:
        """Emit an event when the command is executed."""
        await self.emitter.emit(event_name, *args)


COMMANDS: Dict[str, Type[BaseCommand]] = {}


def register_command(cls: Type[BaseCommand]) -> Type[BaseCommand]:
    """Decorator to register commands automatically."""
    COMMANDS[cls.name.lower()] = cls

    return cls


class Manager:
    """Command-line manager for executing various tasks."""

    installed_apps: List[str]
    parser: ArgumentParser
    commands: Dict[str, BaseCommand]

    def __init__(self, INSTALLED_APPS: List[str], COMMANDS: Dict[str, BaseCommand]):
        self.parser = ArgumentParser(
            description="Management script",
            formatter_class=lambda prog: HelpFormatter(prog, max_help_position=30),
        )

        self.subparsers = self.parser.add_subparsers(dest="command", metavar="command")

        self.installed_apps = INSTALLED_APPS

        self.commands = COMMANDS

    async def internal_command(self, commands: list[BaseCommand]) -> None:
        """Execute a system command."""

        for command in commands:
            self.commands[command.name] = command

    async def load_commands(self):
        """Dynamically load commands from installed apps."""
        for app in self.installed_apps:
            commands_path = f"pkg.{app}.application.commands"
            try:
                module = importlib.import_module(commands_path)

                if hasattr(module, "__path__"):
                    for _, module_name, _ in pkgutil.iter_modules(module.__path__):

                        full_module_name = f"{commands_path}.{module_name}"

                        command_module = importlib.import_module(full_module_name)

                        if hasattr(command_module, "Command"):
                            command_instance: BaseCommand = command_module.Command()
                            self.commands[command_instance.name] = command_instance

            except ModuleNotFoundError as e:
                print(f"Warning: Could not import {commands_path}: {e}")

        for name, command in self.commands.items():

            command_parser = self.subparsers.add_parser(name, help=command.help)

            await command.add_arguments(command_parser)

            command.parser = command_parser

    async def execute(self):
        """Parse and execute commands dynamically."""

        args: Namespace = self.parser.parse_args()

        command = self.commands.get(args.command)

        if command:
            await command.handle(args)
        else:
            self.parser.print_help()
