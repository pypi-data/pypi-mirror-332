"""
Python module generated from Java source file org.bukkit.entity.GlowSquid

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class GlowSquid(Squid):
    """
    A Glow Squid.
    """

    def getDarkTicksRemaining(self) -> int:
        """
        Get the number of dark ticks remaining for this squid.
        
        Bravo Six will go dark for 100 ticks (5 seconds) if damaged.

        Returns
        - dark ticks remaining
        """
        ...


    def setDarkTicksRemaining(self, darkTicksRemaining: int) -> None:
        """
        Sets the number of dark ticks remaining for this squid.
        
        Bravo Six will go dark for 100 ticks (5 seconds) if damaged.

        Arguments
        - darkTicksRemaining: dark ticks remaining
        """
        ...
