"""
Python module generated from Java source file org.bukkit.loot.LootContext

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.entity import HumanEntity
from org.bukkit.loot import *
from typing import Any, Callable, Iterable, Tuple


class LootContext:
    """
    Represents additional information a LootTable can use to modify it's
    generated loot.
    """

    DEFAULT_LOOT_MODIFIER = -1


    def getLocation(self) -> "Location":
        """
        The Location to store where the loot will be generated.

        Returns
        - the Location of where the loot will be generated
        """
        ...


    def getLuck(self) -> float:
        """
        Represents the org.bukkit.potion.PotionEffectType.LUCK that an
        entity can have. The higher the value the better chance of receiving more
        loot.

        Returns
        - luck
        """
        ...


    def getLootingModifier(self) -> int:
        """
        Represents the
        org.bukkit.enchantments.Enchantment.LOOT_BONUS_MOBS the
        .getKiller() entity has on their equipped item.
        
        This value is only set via
        LootContext.Builder.lootingModifier(int). If not set, the
        .getKiller() entity's looting level will be used instead.

        Returns
        - the looting level
        """
        ...


    def getLootedEntity(self) -> "Entity":
        """
        Get the Entity that was killed. Can be null.

        Returns
        - the looted entity or null
        """
        ...


    def getKiller(self) -> "HumanEntity":
        """
        Get the HumanEntity who killed the .getLootedEntity().
        Can be null.

        Returns
        - the killer entity, or null.
        """
        ...


    class Builder:
        """
        Utility class to make building LootContext easier. The only
        required argument is Location with a valid (non-null)
        org.bukkit.World.
        """

        def __init__(self, location: "Location"):
            """
            Creates a new LootContext.Builder instance to facilitate easy
            creation of LootContexts.

            Arguments
            - location: the location the LootContext should use
            """
            ...


        def luck(self, luck: float) -> "Builder":
            """
            Set how much luck to have when generating loot.

            Arguments
            - luck: the luck level

            Returns
            - the Builder
            """
            ...


        def lootingModifier(self, modifier: int) -> "Builder":
            """
            Set the org.bukkit.enchantments.Enchantment.LOOT_BONUS_MOBS
            level equivalent to use when generating loot. Values less than or
            equal to 0 will force the LootTable to only return a single
            org.bukkit.inventory.ItemStack per pool.

            Arguments
            - modifier: the looting level modifier

            Returns
            - the Builder
            """
            ...


        def lootedEntity(self, lootedEntity: "Entity") -> "Builder":
            """
            The entity that was killed.

            Arguments
            - lootedEntity: the looted entity

            Returns
            - the Builder
            """
            ...


        def killer(self, killer: "HumanEntity") -> "Builder":
            """
            Set the org.bukkit.entity.HumanEntity that killed
            .getLootedEntity(). This entity will be used to get the
            looting level if .lootingModifier(int) is not set.

            Arguments
            - killer: the killer entity

            Returns
            - the Builder
            """
            ...


        def build(self) -> "LootContext":
            """
            Create a new LootContext instance using the supplied
            parameters.

            Returns
            - a new LootContext instance
            """
            ...
