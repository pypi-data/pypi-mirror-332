"""
Python module generated from Java source file org.bukkit.command.TabCompleter

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class TabCompleter:
    """
    Represents a class which can suggest tab completions for commands.
    """

    def onTabComplete(self, sender: "CommandSender", command: "Command", label: str, args: list[str]) -> list[str]:
        """
        Requests a list of possible completions for a command argument.

        Arguments
        - sender: Source of the command.  For players tab-completing a
            command inside of a command block, this will be the player, not
            the command block.
        - command: Command which was executed
        - label: Alias of the command which was used
        - args: The arguments passed to the command, including final
            partial argument to be completed

        Returns
        - A List of possible completions for the final argument, or null
            to default to the command executor
        """
        ...
