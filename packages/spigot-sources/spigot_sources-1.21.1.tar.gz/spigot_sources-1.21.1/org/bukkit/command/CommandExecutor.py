"""
Python module generated from Java source file org.bukkit.command.CommandExecutor

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class CommandExecutor:
    """
    Represents a class which contains a single method for executing commands
    """

    def onCommand(self, sender: "CommandSender", command: "Command", label: str, args: list[str]) -> bool:
        """
        Executes the given command, returning its success.
        
        If False is returned, then the "usage" plugin.yml entry for this command
        (if defined) will be sent to the player.

        Arguments
        - sender: Source of the command
        - command: Command which was executed
        - label: Alias of the command which was used
        - args: Passed command arguments

        Returns
        - True if a valid command, otherwise False
        """
        ...
