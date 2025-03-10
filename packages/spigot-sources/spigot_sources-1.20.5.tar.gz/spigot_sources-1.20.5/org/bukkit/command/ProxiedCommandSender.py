"""
Python module generated from Java source file org.bukkit.command.ProxiedCommandSender

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class ProxiedCommandSender(CommandSender):

    def getCaller(self) -> "CommandSender":
        """
        Returns the CommandSender which triggered this proxied command

        Returns
        - the caller which triggered the command
        """
        ...


    def getCallee(self) -> "CommandSender":
        """
        Returns the CommandSender which is being used to call the command

        Returns
        - the caller which the command is being run as
        """
        ...
