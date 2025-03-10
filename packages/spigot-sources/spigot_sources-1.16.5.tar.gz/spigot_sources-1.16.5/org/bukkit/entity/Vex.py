"""
Python module generated from Java source file org.bukkit.entity.Vex

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Vex(Monster):
    """
    Represents a Vex.
    """

    def isCharging(self) -> bool:
        """
        Gets the charging state of this entity.
        
        When this entity is charging it will having a glowing red texture.

        Returns
        - charging state
        """
        ...


    def setCharging(self, charging: bool) -> None:
        """
        Sets the charging state of this entity.
        
        When this entity is charging it will having a glowing red texture.

        Arguments
        - charging: new state
        """
        ...
