"""
Python module generated from Java source file org.bukkit.entity.Interaction

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Interaction(Entity):
    """
    Represents an entity designed to only record interactions.
    """

    def getInteractionWidth(self) -> float:
        """
        Gets the width of this interaction entity.

        Returns
        - width
        """
        ...


    def setInteractionWidth(self, width: float) -> None:
        """
        Sets the width of this interaction entity.

        Arguments
        - width: new width
        """
        ...


    def getInteractionHeight(self) -> float:
        """
        Gets the height of this interaction entity.

        Returns
        - height
        """
        ...


    def setInteractionHeight(self, height: float) -> None:
        """
        Sets the height of this interaction entity.

        Arguments
        - height: new height
        """
        ...


    def isResponsive(self) -> bool:
        """
        Gets if this interaction entity should trigger a response when interacted
        with.

        Returns
        - response setting
        """
        ...


    def setResponsive(self, response: bool) -> None:
        """
        Sets if this interaction entity should trigger a response when interacted
        with.

        Arguments
        - response: new setting
        """
        ...


    def getLastAttack(self) -> "PreviousInteraction":
        """
        Gets the last attack on this interaction entity.

        Returns
        - last attack data, if present
        """
        ...


    def getLastInteraction(self) -> "PreviousInteraction":
        """
        Gets the last interaction on this entity.

        Returns
        - last interaction data, if present
        """
        ...


    class PreviousInteraction:
        """
        Represents a previous interaction with this entity.
        """

        def getPlayer(self) -> "OfflinePlayer":
            """
            Get the previous interacting player.

            Returns
            - interacting player
            """
            ...


        def getTimestamp(self) -> int:
            """
            Gets the Unix timestamp at when this interaction occurred.

            Returns
            - interaction timestamp
            """
            ...
