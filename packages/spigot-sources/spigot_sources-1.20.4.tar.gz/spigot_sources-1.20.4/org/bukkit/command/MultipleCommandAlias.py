"""
Python module generated from Java source file org.bukkit.command.MultipleCommandAlias

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class MultipleCommandAlias(Command):
    """
    Represents a command that delegates to one or more other commands
    """

    def __init__(self, name: str, commands: list["Command"]):
        ...


    def getCommands(self) -> list["Command"]:
        """
        Gets the commands associated with the multi-command alias.

        Returns
        - commands associated with alias
        """
        ...


    def execute(self, sender: "CommandSender", commandLabel: str, args: list[str]) -> bool:
        ...
