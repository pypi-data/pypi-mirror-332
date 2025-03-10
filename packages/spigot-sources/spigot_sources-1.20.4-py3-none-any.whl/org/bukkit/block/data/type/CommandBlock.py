"""
Python module generated from Java source file org.bukkit.block.data.type.CommandBlock

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class CommandBlock(Directional):
    """
    'conditional' denotes whether this command block is conditional or not, i.e.
    will only execute if the preceeding command block also executed successfully.
    """

    def isConditional(self) -> bool:
        """
        Gets the value of the 'conditional' property.

        Returns
        - the 'conditional' value
        """
        ...


    def setConditional(self, conditional: bool) -> None:
        """
        Sets the value of the 'conditional' property.

        Arguments
        - conditional: the new 'conditional' value
        """
        ...
