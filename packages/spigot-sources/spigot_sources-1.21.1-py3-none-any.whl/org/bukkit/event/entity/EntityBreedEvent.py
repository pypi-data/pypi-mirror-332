"""
Python module generated from Java source file org.bukkit.event.entity.EntityBreedEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EntityBreedEvent(EntityEvent, Cancellable):
    """
    Called when one Entity breeds with another Entity.
    """

    def __init__(self, child: "LivingEntity", mother: "LivingEntity", father: "LivingEntity", breeder: "LivingEntity", bredWith: "ItemStack", experience: int):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getMother(self) -> "LivingEntity":
        """
        Gets the parent creating this entity.

        Returns
        - The "birth" parent
        """
        ...


    def getFather(self) -> "LivingEntity":
        """
        Gets the other parent of the newly born entity.

        Returns
        - the other parent
        """
        ...


    def getBreeder(self) -> "LivingEntity":
        """
        Gets the Entity responsible for breeding. Breeder is null for spontaneous
        conception.

        Returns
        - The Entity who initiated breeding.
        """
        ...


    def getBredWith(self) -> "ItemStack":
        """
        The ItemStack that was used to initiate breeding, if present.

        Returns
        - ItemStack used to initiate breeding.
        """
        ...


    def getExperience(self) -> int:
        """
        Get the amount of experience granted by breeding.

        Returns
        - experience amount
        """
        ...


    def setExperience(self, experience: int) -> None:
        """
        Set the amount of experience granted by breeding.

        Arguments
        - experience: experience amount
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
