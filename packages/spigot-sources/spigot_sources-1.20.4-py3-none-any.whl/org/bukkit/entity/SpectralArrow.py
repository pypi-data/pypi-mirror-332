"""
Python module generated from Java source file org.bukkit.entity.SpectralArrow

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class SpectralArrow(AbstractArrow):
    """
    Represents a spectral arrow.
    """

    def getGlowingTicks(self) -> int:
        """
        Returns the amount of time that this arrow will apply
        the glowing effect for.

        Returns
        - the glowing effect ticks
        """
        ...


    def setGlowingTicks(self, duration: int) -> None:
        """
        Sets the amount of time to apply the glowing effect for.

        Arguments
        - duration: the glowing effect ticks
        """
        ...
