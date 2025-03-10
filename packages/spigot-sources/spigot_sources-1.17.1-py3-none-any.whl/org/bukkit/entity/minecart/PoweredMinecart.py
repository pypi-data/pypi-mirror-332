"""
Python module generated from Java source file org.bukkit.entity.minecart.PoweredMinecart

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from typing import Any, Callable, Iterable, Tuple


class PoweredMinecart(Minecart):
    """
    Represents a powered minecart. A powered minecart moves on its own when a
    player deposits org.bukkit.Material.COAL fuel.
    """

    def getFuel(self) -> int:
        """
        Get the number of ticks until the minecart runs out of fuel.

        Returns
        - Number of ticks until the minecart runs out of fuel
        """
        ...


    def setFuel(self, fuel: int) -> None:
        """
        Set the number of ticks until the minecart runs out of fuel.

        Arguments
        - fuel: Number of ticks until the minecart runs out of fuel
        """
        ...
