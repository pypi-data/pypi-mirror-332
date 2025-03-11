"""
Python module generated from Java source file org.bukkit.event.entity.EntityDamageByBlockEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Function
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityDamageByBlockEvent(EntityDamageEvent):
    """
    Called when an entity is damaged by a block
    """

    def __init__(self, damager: "Block", damagee: "Entity", cause: "DamageCause", damage: float):
        ...


    def __init__(self, damager: "Block", damagerState: "BlockState", damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", damage: float):
        ...


    def __init__(self, damager: "Block", damagee: "Entity", cause: "DamageCause", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def __init__(self, damager: "Block", damagerState: "BlockState", damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def getDamager(self) -> "Block":
        """
        Returns the block that damaged the player.

        Returns
        - Block that damaged the player
        """
        ...


    def getDamagerBlockState(self) -> "BlockState":
        """
        Returns the captured BlockState of the block that damaged the player.

        Returns
        - the block state
        """
        ...
