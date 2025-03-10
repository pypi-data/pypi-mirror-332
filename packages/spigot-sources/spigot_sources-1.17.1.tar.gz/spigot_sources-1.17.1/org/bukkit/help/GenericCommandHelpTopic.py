"""
Python module generated from Java source file org.bukkit.help.GenericCommandHelpTopic

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import StringUtils
from org.bukkit import ChatColor
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import ConsoleCommandSender
from org.bukkit.help import *
from typing import Any, Callable, Iterable, Tuple


class GenericCommandHelpTopic(HelpTopic):
    """
    Lacking an alternative, the help system will create instances of
    GenericCommandHelpTopic for each command in the server's CommandMap. You
    can use this class as a base class for custom help topics, or as an example
    for how to write your own.
    """

    def __init__(self, command: "Command"):
        ...


    def canSee(self, sender: "CommandSender") -> bool:
        ...
