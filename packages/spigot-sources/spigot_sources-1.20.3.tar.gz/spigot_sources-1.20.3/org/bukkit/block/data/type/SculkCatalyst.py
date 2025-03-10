"""
Python module generated from Java source file org.bukkit.block.data.type.SculkCatalyst

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class SculkCatalyst(BlockData):
    """
    'bloom' indicates whether the sculk catalyst is actively spreading the sculk
    or not.
    """

    def isBloom(self) -> bool:
        """
        Gets the value of the 'bloom' property.

        Returns
        - the 'bloom' value
        """
        ...


    def setBloom(self, bloom: bool) -> None:
        """
        Sets the value of the 'bloom' property.

        Arguments
        - bloom: the new 'bloom' value
        """
        ...
