"""
Python module generated from Java source file org.bukkit.help.IndexHelpTopic

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.command import ConsoleCommandSender
from org.bukkit.entity import Player
from org.bukkit.help import *
from org.bukkit.util import ChatPaginator
from typing import Any, Callable, Iterable, Tuple


class IndexHelpTopic(HelpTopic):
    """
    This help topic generates a list of other help topics. This class is useful
    for adding your own index help topics. To enforce a particular order, use a
    sorted collection.
    
    If a preamble is provided to the constructor, that text will be displayed
    before the first item in the index.
    """

    def __init__(self, name: str, shortText: str, permission: str, topics: Iterable["HelpTopic"]):
        ...


    def __init__(self, name: str, shortText: str, permission: str, topics: Iterable["HelpTopic"], preamble: str):
        ...


    def canSee(self, sender: "CommandSender") -> bool:
        ...


    def amendCanSee(self, amendedPermission: str) -> None:
        ...


    def getFullText(self, sender: "CommandSender") -> str:
        ...
