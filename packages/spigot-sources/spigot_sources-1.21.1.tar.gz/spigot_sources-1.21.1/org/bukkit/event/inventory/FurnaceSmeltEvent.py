"""
Python module generated from Java source file org.bukkit.event.inventory.FurnaceSmeltEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event.block import BlockCookEvent
from org.bukkit.event.inventory import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class FurnaceSmeltEvent(BlockCookEvent):
    """
    Called when an ItemStack is successfully smelted in a furnace.
    """

    def __init__(self, furnace: "Block", source: "ItemStack", result: "ItemStack"):
        ...
