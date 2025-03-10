"""
Python module generated from Java source file org.bukkit.entity.Ocelot

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Ocelot(Animals):
    """
    A wild tameable cat
    """

    def isTrusting(self) -> bool:
        """
        Checks if this ocelot trusts players.

        Returns
        - True if it trusts players
        """
        ...


    def setTrusting(self, trust: bool) -> None:
        """
        Sets if this ocelot trusts players.

        Arguments
        - trust: True if it trusts players
        """
        ...


    def getCatType(self) -> "Type":
        """
        Gets the current type of this cat.

        Returns
        - Type of the cat.

        Deprecated
        - Cats are now a separate entity.
        """
        ...


    def setCatType(self, type: "Type") -> None:
        """
        Sets the current type of this cat.

        Arguments
        - type: New type of this cat.

        Deprecated
        - Cats are now a separate entity.
        """
        ...


    class Type(Enum):
        """
        Represents the various different cat types there are.

        Deprecated
        - Cats are now a separate entity.
        """

        WILD_OCELOT = (0)
        BLACK_CAT = (1)
        RED_CAT = (2)
        SIAMESE_CAT = (3)


        def getId(self) -> int:
            """
            Gets the ID of this cat type.

            Returns
            - Type ID.

            Deprecated
            - Magic value
            """
            ...


        @staticmethod
        def getType(id: int) -> "Type":
            """
            Gets a cat type by its ID.

            Arguments
            - id: ID of the cat type to get.

            Returns
            - Resulting type, or null if not found.

            Deprecated
            - Magic value
            """
            ...
