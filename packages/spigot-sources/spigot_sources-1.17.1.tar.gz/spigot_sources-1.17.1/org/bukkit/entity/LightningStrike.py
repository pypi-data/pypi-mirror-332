"""
Python module generated from Java source file org.bukkit.entity.LightningStrike

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class LightningStrike(Entity):
    """
    Represents an instance of a lightning strike. May or may not do damage.
    """

    def isEffect(self) -> bool:
        """
        Returns whether the strike is an effect that does no damage.

        Returns
        - whether the strike is an effect
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot(Spigot):

        def isSilent(self) -> bool:
            ...
