"""
Python module generated from Java source file org.bukkit.entity.Allay

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from org.bukkit.event.entity import CreatureSpawnEvent
from org.bukkit.inventory import InventoryHolder
from typing import Any, Callable, Iterable, Tuple


class Allay(Creature, InventoryHolder):
    """
    An Allay.
    """

    def canDuplicate(self) -> bool:
        """
        Gets if the allay can duplicate.
        
        **Note:** Duplication is based when the
        .getDuplicationCooldown its lower than zero.

        Returns
        - if the allay can duplicate itself.
        """
        ...


    def setCanDuplicate(self, canDuplicate: bool) -> None:
        """
        Sets if the allay can duplicate.
        
        **Note:** this value can be overridden later by
        .getDuplicationCooldown if is lower than zero. You can also use
        .setDuplicationCooldown to allow the allay to duplicate

        Arguments
        - canDuplicate: if the allay can duplicate itself
        """
        ...


    def getDuplicationCooldown(self) -> int:
        """
        Gets the cooldown for duplicating the allay.

        Returns
        - the time in ticks when allay can duplicate
        """
        ...


    def setDuplicationCooldown(self, cooldown: int) -> None:
        """
        Sets the cooldown before the allay can duplicate again.

        Arguments
        - cooldown: the cooldown, use a negative number to deny allay to
        duplicate again.
        """
        ...


    def resetDuplicationCooldown(self) -> None:
        """
        Reset the cooldown for duplication.
        
        This will set the cooldown ticks to the same value as is set after an
        Allay has duplicated.
        """
        ...


    def isDancing(self) -> bool:
        """
        Gets if the allay is dancing.

        Returns
        - `True` if it is dancing, False otherwise.
        """
        ...


    def startDancing(self, location: "Location") -> None:
        """
        Causes the allay to start dancing because of the provided jukebox
        location.

        Arguments
        - location: the location of the jukebox

        Raises
        - IllegalArgumentException: if the block at the location is not a
        jukebox
        """
        ...


    def startDancing(self) -> None:
        """
        Force sets the dancing status of the allay.
        
        **Note:** This method forces the allay to dance, ignoring any nearby
        jukebox being required.
        """
        ...


    def stopDancing(self) -> None:
        """
        Makes the allay stop dancing.
        """
        ...


    def duplicateAllay(self) -> "Allay":
        """
        This make the current allay duplicate itself without dance or item
        necessary.
        **Note:** this will fire a CreatureSpawnEvent

        Returns
        - the new entity Allay or null if the spawn was cancelled
        """
        ...


    def getJukebox(self) -> "Location":
        """
        Gets the jukebox the allay is set to dance to.

        Returns
        - the location of the jukebox to dance if it exists
        """
        ...
