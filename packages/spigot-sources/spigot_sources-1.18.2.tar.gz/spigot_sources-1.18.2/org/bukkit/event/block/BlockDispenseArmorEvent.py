"""
Python module generated from Java source file org.bukkit.event.block.BlockDispenseArmorEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import LivingEntity
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class BlockDispenseArmorEvent(BlockDispenseEvent):
    """
    Called when an equippable item is dispensed from a block and equipped on a
    nearby entity.
    
    If a Block Dispense Armor event is cancelled, the equipment will not be
    equipped on the target entity.
    """

    def __init__(self, block: "Block", dispensed: "ItemStack", target: "LivingEntity"):
        ...


    def getTargetEntity(self) -> "LivingEntity":
        """
        Get the living entity on which the armor was dispensed.

        Returns
        - the target entity
        """
        ...
