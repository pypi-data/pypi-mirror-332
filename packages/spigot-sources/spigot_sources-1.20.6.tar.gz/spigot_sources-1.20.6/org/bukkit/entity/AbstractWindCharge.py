"""
Python module generated from Java source file org.bukkit.entity.AbstractWindCharge

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.MinecraftExperimental import Requires
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class AbstractWindCharge(Fireball):
    """
    Represents a Wind Charge.
    """

    def explode(self) -> None:
        """
        Immediately explode this WindCharge.
        """
        ...
