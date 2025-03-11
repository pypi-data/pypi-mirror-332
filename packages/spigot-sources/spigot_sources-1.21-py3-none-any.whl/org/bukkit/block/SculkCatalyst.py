"""
Python module generated from Java source file org.bukkit.block.SculkCatalyst

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.event.entity import EntityDeathEvent
from typing import Any, Callable, Iterable, Tuple


class SculkCatalyst(TileState):
    """
    Represents a captured state of a sculk catalyst.
    """

    def bloom(self, block: "Block", charges: int) -> None:
        """
        Causes a new sculk bloom, as if an entity just died around this catalyst.
        
        Typically, charges should be set to the exp reward of a mob
        (EntityDeathEvent.getDroppedExp()), which is usually
        3-5 for animals, and 5-10 for the average mob (up to 50 for
        wither skeletons). Roughly speaking, for each charge, 1 more
        sculk block will be placed.
        
        If `charges > 1000`, multiple cursors will be spawned in the
        block.

        Arguments
        - block: which block to spawn the cursor in
        - charges: how much charge to spawn.
        """
        ...
