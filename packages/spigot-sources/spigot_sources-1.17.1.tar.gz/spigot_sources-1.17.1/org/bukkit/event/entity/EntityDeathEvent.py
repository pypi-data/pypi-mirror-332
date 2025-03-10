"""
Python module generated from Java source file org.bukkit.event.entity.EntityDeathEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EntityDeathEvent(EntityEvent):
    """
    Thrown whenever a LivingEntity dies
    """

    def __init__(self, entity: "LivingEntity", drops: list["ItemStack"]):
        ...


    def __init__(self, what: "LivingEntity", drops: list["ItemStack"], droppedExp: int):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getDroppedExp(self) -> int:
        """
        Gets how much EXP should be dropped from this death.
        
        This does not indicate how much EXP should be taken from the entity in
        question, merely how much should be created after its death.

        Returns
        - Amount of EXP to drop.
        """
        ...


    def setDroppedExp(self, exp: int) -> None:
        """
        Sets how much EXP should be dropped from this death.
        
        This does not indicate how much EXP should be taken from the entity in
        question, merely how much should be created after its death.

        Arguments
        - exp: Amount of EXP to drop.
        """
        ...


    def getDrops(self) -> list["ItemStack"]:
        """
        Gets all the items which will drop when the entity dies

        Returns
        - Items to drop when the entity dies
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
