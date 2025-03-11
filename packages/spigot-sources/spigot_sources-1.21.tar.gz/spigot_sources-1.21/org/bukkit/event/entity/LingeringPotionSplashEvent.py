"""
Python module generated from Java source file org.bukkit.event.entity.LingeringPotionSplashEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import AreaEffectCloud
from org.bukkit.entity import Entity
from org.bukkit.entity import ThrownPotion
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class LingeringPotionSplashEvent(ProjectileHitEvent, Cancellable):
    """
    Called when a splash potion hits an area
    """

    def __init__(self, potion: "ThrownPotion", entity: "AreaEffectCloud"):
        ...


    def __init__(self, potion: "ThrownPotion", hitEntity: "Entity", hitBlock: "Block", hitFace: "BlockFace", entity: "AreaEffectCloud"):
        ...


    def getEntity(self) -> "ThrownPotion":
        ...


    def getAreaEffectCloud(self) -> "AreaEffectCloud":
        """
        Gets the AreaEffectCloud spawned

        Returns
        - The spawned AreaEffectCloud
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
