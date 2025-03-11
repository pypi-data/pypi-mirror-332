"""
Python module generated from Java source file org.bukkit.event.entity.EntityPotionEffectEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class EntityPotionEffectEvent(EntityEvent, Cancellable):
    """
    Called when a potion effect is modified on an entity.
    
    If the event is cancelled, no change will be made on the entity.
    """

    def __init__(self, livingEntity: "LivingEntity", oldEffect: "PotionEffect", newEffect: "PotionEffect", cause: "Cause", action: "Action", override: bool):
        ...


    def getOldEffect(self) -> "PotionEffect":
        """
        Gets the old potion effect of the changed type, which will be removed.

        Returns
        - The old potion effect or null if the entity did not have the
        changed effect type.
        """
        ...


    def getNewEffect(self) -> "PotionEffect":
        """
        Gets new potion effect of the changed type to be applied.

        Returns
        - The new potion effect or null if the effect of the changed type
        will be removed.
        """
        ...


    def getCause(self) -> "Cause":
        """
        Gets the cause why the effect has changed.

        Returns
        - A Cause value why the effect has changed.
        """
        ...


    def getAction(self) -> "Action":
        """
        Gets the action which will be performed on the potion effect type.

        Returns
        - An action to be performed on the potion effect type.
        """
        ...


    def getModifiedType(self) -> "PotionEffectType":
        """
        Gets the modified potion effect type.

        Returns
        - The effect type which will be modified on the entity.
        """
        ...


    def isOverride(self) -> bool:
        """
        Returns if the new potion effect will override the old potion effect
        (Only applicable for the CHANGED Action).

        Returns
        - If the new effect will override the old one.
        """
        ...


    def setOverride(self, override: bool) -> None:
        """
        Sets if the new potion effect will override the old potion effect (Only
        applicable for the CHANGED action).

        Arguments
        - override: If the new effect will override the old one.
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


    class Action(Enum):
        """
        An enum to specify the action to be performed.
        """

        ADDED = 0
        """
        When the potion effect is added because the entity didn't have it's
        type.
        """
        CHANGED = 1
        """
        When the entity already had the potion effect type, but the effect is
        changed.
        """
        CLEARED = 2
        """
        When the effect is removed due to all effects being removed.
        """
        REMOVED = 3
        """
        When the potion effect type is completely removed.
        """


    class Cause(Enum):
        """
        An enum to specify the cause why an effect was changed.
        """

        AREA_EFFECT_CLOUD = 0
        """
        When the entity stands inside an area effect cloud.
        """
        ARROW = 1
        """
        When the entity is hit by an spectral or tipped arrow.
        """
        ATTACK = 2
        """
        When the entity is inflicted with a potion effect due to an entity
        attack (e.g. a cave spider or a shulker bullet).
        """
        AXOLOTL = 3
        """
        When an entity gets the effect from an axolotl.
        """
        BEACON = 4
        """
        When beacon effects get applied due to the entity being nearby.
        """
        COMMAND = 5
        """
        When a potion effect is changed due to the /effect command.
        """
        CONDUIT = 6
        """
        When the entity gets the effect from a conduit.
        """
        CONVERSION = 7
        """
        When a conversion from a villager zombie to a villager is started or
        finished.
        """
        DEATH = 8
        """
        When all effects are removed due to death.
        """
        DOLPHIN = 9
        """
        When the entity gets the effect from a dolphin.
        """
        EXPIRATION = 10
        """
        When the effect was removed due to expiration.
        """
        FOOD = 11
        """
        When an effect is inflicted due to food (e.g. when a player eats or a
        cookie is given to a parrot).
        """
        ILLUSION = 12
        """
        When an illusion illager makes himself disappear.
        """
        MILK = 13
        """
        When all effects are removed due to a bucket of milk.
        """
        PATROL_CAPTAIN = 14
        """
        When a player gets bad omen after killing a patrol captain.
        """
        PLUGIN = 15
        """
        When a potion effect is modified through the plugin methods.
        """
        POTION_DRINK = 16
        """
        When the entity drinks a potion.
        """
        POTION_SPLASH = 17
        """
        When the entity is inflicted with an effect due to a splash potion.
        """
        SPIDER_SPAWN = 18
        """
        When a spider gets effects when spawning on hard difficulty.
        """
        TOTEM = 19
        """
        When the entity gets effects from a totem item saving it's life.
        """
        TURTLE_HELMET = 20
        """
        When the entity gets water breathing by wearing a turtle helmet.
        """
        UNKNOWN = 21
        """
        When the Cause is missing.
        """
        VILLAGER_TRADE = 22
        """
        When a villager gets regeneration after a trade.
        """
        WARDEN = 23
        """
        When an entity gets the effect from a warden.
        """
        WITHER_ROSE = 24
        """
        When an entity comes in contact with a wither rose.
        """
