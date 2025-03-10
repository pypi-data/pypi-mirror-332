"""
Python module generated from Java source file org.bukkit.event.player.PlayerEggThrowEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Egg
from org.bukkit.entity import EntityType
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerEggThrowEvent(PlayerEvent):
    """
    Called when a player throws an egg and it might hatch
    """

    def __init__(self, player: "Player", egg: "Egg", hatching: bool, numHatches: int, hatchingType: "EntityType"):
        ...


    def getEgg(self) -> "Egg":
        """
        Gets the egg involved in this event.

        Returns
        - the egg involved in this event
        """
        ...


    def isHatching(self) -> bool:
        """
        Gets whether the egg is hatching or not. Will be what the server
        would've done without interaction.

        Returns
        - boolean Whether the egg is going to hatch or not
        """
        ...


    def setHatching(self, hatching: bool) -> None:
        """
        Sets whether the egg will hatch or not.

        Arguments
        - hatching: True if you want the egg to hatch, False if you want it
            not to
        """
        ...


    def getHatchingType(self) -> "EntityType":
        """
        Get the type of the mob being hatched (EntityType.CHICKEN by default)

        Returns
        - The type of the mob being hatched by the egg
        """
        ...


    def setHatchingType(self, hatchType: "EntityType") -> None:
        """
        Change the type of mob being hatched by the egg

        Arguments
        - hatchType: The type of the mob being hatched by the egg
        """
        ...


    def getNumHatches(self) -> int:
        """
        Get the number of mob hatches from the egg. By default the number will
        be the number the server would've done
        
        - 7/8 chance of being 0
        - 31/256 ~= 1/8 chance to be 1
        - 1/256 chance to be 4

        Returns
        - The number of mobs going to be hatched by the egg
        """
        ...


    def setNumHatches(self, numHatches: int) -> None:
        """
        Change the number of mobs coming out of the hatched egg
        
        The boolean hatching will override this number. Ie. If hatching =
        False, this number will not matter

        Arguments
        - numHatches: The number of mobs coming out of the egg
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
