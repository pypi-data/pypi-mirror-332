"""
Python module generated from Java source file org.bukkit.block.data.type.SculkShrieker

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class SculkShrieker(Waterlogged):
    """
    'can_summon' indicates whether the sculk shrieker can summon the warden.
    
    'shrieking' indicated whether the sculk shrieker is shrieking or not.
    """

    def isCanSummon(self) -> bool:
        """
        Gets the value of the 'can_summon' property.

        Returns
        - the 'can_summon' value
        """
        ...


    def setCanSummon(self, can_summon: bool) -> None:
        """
        Sets the value of the 'can_summon' property.

        Arguments
        - can_summon: the new 'can_summon' value
        """
        ...


    def isShrieking(self) -> bool:
        """
        Gets the value of the 'shrieking' property.

        Returns
        - the 'shrieking' value
        """
        ...


    def setShrieking(self, shrieking: bool) -> None:
        """
        Sets the value of the 'shrieking' property.

        Arguments
        - shrieking: the new 'shrieking' value
        """
        ...
