"""
Python module generated from Java source file org.bukkit.event.entity.EntityDamageByEntityEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Function
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityDamageByEntityEvent(EntityDamageEvent):
    """
    Called when an entity is damaged by an entity
    """

    def __init__(self, damager: "Entity", damagee: "Entity", cause: "DamageCause", damage: float):
        ...


    def __init__(self, damager: "Entity", damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", damage: float):
        ...


    def __init__(self, damager: "Entity", damagee: "Entity", cause: "DamageCause", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def __init__(self, damager: "Entity", damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def getDamager(self) -> "Entity":
        """
        Returns the entity that damaged the defender.

        Returns
        - Entity that damaged the defender.
        """
        ...
