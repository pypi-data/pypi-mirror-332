"""
Python module generated from Java source file org.bukkit.event.world.StructureGrowEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import TreeType
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class StructureGrowEvent(WorldEvent, Cancellable):
    """
    Event that is called when an organic structure attempts to grow (Sapling ->
    Tree), (Mushroom -> Huge Mushroom), naturally or using bonemeal.
    """

    def __init__(self, location: "Location", species: "TreeType", bonemeal: bool, player: "Player", blocks: list["BlockState"]):
        ...


    def getLocation(self) -> "Location":
        """
        Gets the location of the structure.

        Returns
        - Location of the structure
        """
        ...


    def getSpecies(self) -> "TreeType":
        """
        Gets the species type (birch, normal, pine, red mushroom, brown
        mushroom)

        Returns
        - Structure species
        """
        ...


    def isFromBonemeal(self) -> bool:
        """
        Checks if structure was grown using bonemeal.

        Returns
        - True if the structure was grown using bonemeal.
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player that created the structure.

        Returns
        - Player that created the structure, null if was not created
            manually
        """
        ...


    def getBlocks(self) -> list["BlockState"]:
        """
        Gets a list of all blocks associated with the structure.

        Returns
        - list of all blocks associated with the structure.
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
