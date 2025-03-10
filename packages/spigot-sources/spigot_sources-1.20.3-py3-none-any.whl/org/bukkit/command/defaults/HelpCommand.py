"""
Python module generated from Java source file org.bukkit.command.defaults.HelpCommand

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Joiner
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from java.util import Arrays
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.command import ConsoleCommandSender
from org.bukkit.command.defaults import *
from org.bukkit.help import HelpMap
from org.bukkit.help import HelpTopic
from org.bukkit.help import HelpTopicComparator
from org.bukkit.help import IndexHelpTopic
from org.bukkit.util import ChatPaginator
from typing import Any, Callable, Iterable, Tuple


class HelpCommand(BukkitCommand):

    def __init__(self):
        ...


    def execute(self, sender: "CommandSender", currentAlias: str, args: list[str]) -> bool:
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> list[str]:
        ...
