"""
Python module generated from Java source file org.bukkit.command.SimpleCommandMap

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Arrays
from java.util import Collections
from java.util import Iterator
from org.bukkit import Location
from org.bukkit import Server
from org.bukkit.command import *
from org.bukkit.command.defaults import BukkitCommand
from org.bukkit.command.defaults import HelpCommand
from org.bukkit.command.defaults import PluginsCommand
from org.bukkit.command.defaults import ReloadCommand
from org.bukkit.command.defaults import TimingsCommand
from org.bukkit.command.defaults import VersionCommand
from org.bukkit.entity import Player
from org.bukkit.util import StringUtil
from typing import Any, Callable, Iterable, Tuple


class SimpleCommandMap(CommandMap):

    def __init__(self, server: "Server"):
        ...


    def setFallbackCommands(self) -> None:
        ...


    def registerAll(self, fallbackPrefix: str, commands: list["Command"]) -> None:
        """

        """
        ...


    def register(self, fallbackPrefix: str, command: "Command") -> bool:
        """

        """
        ...


    def register(self, label: str, fallbackPrefix: str, command: "Command") -> bool:
        """

        """
        ...


    def dispatch(self, sender: "CommandSender", commandLine: str) -> bool:
        """

        """
        ...


    def clearCommands(self) -> None:
        ...


    def getCommand(self, name: str) -> "Command":
        ...


    def tabComplete(self, sender: "CommandSender", cmdLine: str) -> list[str]:
        ...


    def tabComplete(self, sender: "CommandSender", cmdLine: str, location: "Location") -> list[str]:
        ...


    def getCommands(self) -> Iterable["Command"]:
        ...


    def registerServerAliases(self) -> None:
        ...
