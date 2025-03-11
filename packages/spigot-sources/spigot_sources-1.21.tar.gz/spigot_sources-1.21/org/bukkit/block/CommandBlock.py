"""
Python module generated from Java source file org.bukkit.block.CommandBlock

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class CommandBlock(TileState):
    """
    Represents a captured state of a command block.
    """

    def getCommand(self) -> str:
        """
        Gets the command that this CommandBlock will run when powered.
        This will never return null.  If the CommandBlock does not have a
        command, an empty String will be returned instead.

        Returns
        - Command that this CommandBlock will run when powered.
        """
        ...


    def setCommand(self, command: str) -> None:
        """
        Sets the command that this CommandBlock will run when powered.
        Setting the command to null is the same as setting it to an empty
        String.

        Arguments
        - command: Command that this CommandBlock will run when powered.
        """
        ...


    def getName(self) -> str:
        """
        Gets the name of this CommandBlock.  The name is used with commands
        that this CommandBlock executes.  This name will never be null, and
        by default is "@".

        Returns
        - Name of this CommandBlock.
        """
        ...


    def setName(self, name: str) -> None:
        """
        Sets the name of this CommandBlock.  The name is used with commands
        that this CommandBlock executes.  Setting the name to null is the
        same as setting it to "@".

        Arguments
        - name: New name for this CommandBlock.
        """
        ...
