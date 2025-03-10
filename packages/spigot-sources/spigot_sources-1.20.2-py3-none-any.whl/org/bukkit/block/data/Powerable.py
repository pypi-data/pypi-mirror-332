"""
Python module generated from Java source file org.bukkit.block.data.Powerable

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Powerable(BlockData):
    """
    'powered' indicates whether this block is in the powered state or not, i.e.
    receiving a redstone current of power &gt; 0.
    """

    def isPowered(self) -> bool:
        """
        Gets the value of the 'powered' property.

        Returns
        - the 'powered' value
        """
        ...


    def setPowered(self, powered: bool) -> None:
        """
        Sets the value of the 'powered' property.

        Arguments
        - powered: the new 'powered' value
        """
        ...
