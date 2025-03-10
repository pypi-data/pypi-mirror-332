"""
Python module generated from Java source file org.bukkit.command.defaults.PluginsCommand

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util import Collections
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.command.defaults import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PluginsCommand(BukkitCommand):

    def __init__(self, name: str):
        ...


    def execute(self, sender: "CommandSender", currentAlias: str, args: list[str]) -> bool:
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> list[str]:
        ...
