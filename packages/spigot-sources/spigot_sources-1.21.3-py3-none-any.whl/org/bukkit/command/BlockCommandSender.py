"""
Python module generated from Java source file org.bukkit.command.BlockCommandSender

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class BlockCommandSender(CommandSender):

    def getBlock(self) -> "Block":
        """
        Returns the block this command sender belongs to

        Returns
        - Block for the command sender
        """
        ...
