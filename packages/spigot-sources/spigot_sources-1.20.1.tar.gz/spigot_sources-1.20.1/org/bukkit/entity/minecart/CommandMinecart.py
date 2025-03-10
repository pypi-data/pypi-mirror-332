"""
Python module generated from Java source file org.bukkit.entity.minecart.CommandMinecart

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from typing import Any, Callable, Iterable, Tuple


class CommandMinecart(Minecart):

    def getCommand(self) -> str:
        """
        Gets the command that this CommandMinecart will run when activated.
        This will never return null.  If the CommandMinecart does not have a
        command, an empty String will be returned instead.

        Returns
        - Command that this CommandMinecart will run when powered.
        """
        ...


    def setCommand(self, command: str) -> None:
        """
        Sets the command that this CommandMinecart will run when activated.
        Setting the command to null is the same as setting it to an empty
        String.

        Arguments
        - command: Command that this CommandMinecart will run when
            activated.
        """
        ...


    def setName(self, name: str) -> None:
        """
        Sets the name of this CommandMinecart.  The name is used with commands
        that this CommandMinecart executes.  Setting the name to null is the
        same as setting it to "@".

        Arguments
        - name: New name for this CommandMinecart.
        """
        ...
