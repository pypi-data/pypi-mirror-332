"""
Python module generated from Java source file org.bukkit.block.data.type.DaylightDetector

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import AnaloguePowerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class DaylightDetector(AnaloguePowerable):
    """
    'inverted' denotes whether this daylight detector is in the inverted mode,
    i.e. activates in the absence of light rather than presence."
    """

    def isInverted(self) -> bool:
        """
        Gets the value of the 'inverted' property.

        Returns
        - the 'inverted' value
        """
        ...


    def setInverted(self, inverted: bool) -> None:
        """
        Sets the value of the 'inverted' property.

        Arguments
        - inverted: the new 'inverted' value
        """
        ...
