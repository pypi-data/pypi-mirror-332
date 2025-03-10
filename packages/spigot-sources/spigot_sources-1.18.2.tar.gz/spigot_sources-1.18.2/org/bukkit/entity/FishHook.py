"""
Python module generated from Java source file org.bukkit.entity.FishHook

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class FishHook(Projectile):
    """
    Represents a fishing hook.
    """

    def getMinWaitTime(self) -> int:
        """
        Get the minimum number of ticks one has to wait for a fish biting.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.

        Returns
        - Minimum number of ticks one has to wait for a fish biting
        """
        ...


    def setMinWaitTime(self, minWaitTime: int) -> None:
        """
        Set the minimum number of ticks one has to wait for a fish biting.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.

        Arguments
        - minWaitTime: Minimum number of ticks one has to wait for a fish
        biting
        """
        ...


    def getMaxWaitTime(self) -> int:
        """
        Get the maximum number of ticks one has to wait for a fish biting.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.

        Returns
        - Maximum number of ticks one has to wait for a fish biting
        """
        ...


    def setMaxWaitTime(self, maxWaitTime: int) -> None:
        """
        Set the maximum number of ticks one has to wait for a fish biting.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.

        Arguments
        - maxWaitTime: Maximum number of ticks one has to wait for a fish
        biting
        """
        ...


    def getApplyLure(self) -> bool:
        """
        Get whether the lure enchantment should be applied to reduce the wait
        time.
        
        The default is True.
        Lure reduces the wait time by 100 ticks (5 seconds) for each level of the
        enchantment.

        Returns
        - Whether the lure enchantment should be applied to reduce the wait
        time
        """
        ...


    def setApplyLure(self, applyLure: bool) -> None:
        """
        Set whether the lure enchantment should be applied to reduce the wait
        time.
        
        The default is True.
        Lure reduces the wait time by 100 ticks (5 seconds) for each level of the
        enchantment.

        Arguments
        - applyLure: Whether the lure enchantment should be applied to reduce
        the wait time
        """
        ...


    def getBiteChance(self) -> float:
        """
        Gets the chance of a fish biting.
        
        0.0 = No Chance.
        1.0 = Instant catch.

        Returns
        - chance the bite chance

        Deprecated
        - has no effect in newer Minecraft versions
        """
        ...


    def setBiteChance(self, chance: float) -> None:
        """
        Sets the chance of a fish biting.
        
        0.0 = No Chance.
        1.0 = Instant catch.

        Arguments
        - chance: the bite chance

        Raises
        - IllegalArgumentException: if the bite chance is not between 0
            and 1

        Deprecated
        - has no effect in newer Minecraft versions
        """
        ...


    def isInOpenWater(self) -> bool:
        """
        Check whether or not this fish hook is in open water.
        
        Open water is defined by a 5x4x5 area of water, air and lily pads. If in
        open water, treasure items may be caught.

        Returns
        - True if in open water, False otherwise
        """
        ...


    def getHookedEntity(self) -> "Entity":
        """
        Get the entity hooked by this fish hook.

        Returns
        - the hooked entity. null if none
        """
        ...


    def setHookedEntity(self, entity: "Entity") -> None:
        """
        Set the entity hooked by this fish hook.

        Arguments
        - entity: the entity to set, or null to unhook
        """
        ...


    def pullHookedEntity(self) -> bool:
        """
        Pull the hooked entity to the caster of this fish hook. If no entity is
        hooked, this method has no effect.

        Returns
        - True if pulled, False if no entity is hooked
        """
        ...


    def getState(self) -> "HookState":
        """
        Get the current state of this fish hook.

        Returns
        - the fish hook state
        """
        ...


    class HookState(Enum):
        """
        Represents a state in which a fishing hook may be.
        """

        UNHOOKED = 0
        """
        The fishing hook has been cast and is either in the air or resting
        against a block on the ground.
        """
        HOOKED_ENTITY = 1
        """
        The fishing hook has hooked an entity.
        """
        BOBBING = 2
        """
        The fishing hook is bobbing in the water, waiting for a bite.
        """
