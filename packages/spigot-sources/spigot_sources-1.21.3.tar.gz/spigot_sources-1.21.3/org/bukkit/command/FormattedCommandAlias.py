"""
Python module generated from Java source file org.bukkit.command.FormattedCommandAlias

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class FormattedCommandAlias(Command):

    def __init__(self, alias: str, formatStrings: list[str]):
        ...


    def execute(self, sender: "CommandSender", commandLabel: str, args: list[str]) -> bool:
        ...
