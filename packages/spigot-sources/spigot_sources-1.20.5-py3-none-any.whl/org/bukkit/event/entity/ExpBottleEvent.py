"""
Python module generated from Java source file org.bukkit.event.entity.ExpBottleEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import ThrownExpBottle
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ExpBottleEvent(ProjectileHitEvent):
    """
    Called when a ThrownExpBottle hits and releases experience.
    """

    def __init__(self, bottle: "ThrownExpBottle", exp: int):
        ...


    def __init__(self, bottle: "ThrownExpBottle", hitEntity: "Entity", hitBlock: "Block", hitFace: "BlockFace", exp: int):
        ...


    def getEntity(self) -> "ThrownExpBottle":
        ...


    def getShowEffect(self) -> bool:
        """
        This method indicates if the particle effect should be shown.

        Returns
        - True if the effect will be shown, False otherwise
        """
        ...


    def setShowEffect(self, showEffect: bool) -> None:
        """
        This method sets if the particle effect will be shown.
        
        This does not change the experience created.

        Arguments
        - showEffect: True indicates the effect will be shown, False
            indicates no effect will be shown
        """
        ...


    def getExperience(self) -> int:
        """
        This method retrieves the amount of experience to be created.
        
        The number indicates a total amount to be divided into orbs.

        Returns
        - the total amount of experience to be created
        """
        ...


    def setExperience(self, exp: int) -> None:
        """
        This method sets the amount of experience to be created.
        
        The number indicates a total amount to be divided into orbs.

        Arguments
        - exp: the total amount of experience to be created
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
