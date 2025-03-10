"""
Python module generated from Java source file org.bukkit.entity.FishHook

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

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
        Get the minimum number of ticks one has to wait for a fish appearing.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.

        Returns
        - Minimum number of ticks one has to wait for a fish appearing
        """
        ...


    def setMinWaitTime(self, minWaitTime: int) -> None:
        """
        Set the minimum number of ticks one has to wait for a fish appearing.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.

        Arguments
        - minWaitTime: Minimum number of ticks one has to wait for a fish
        appearing
        """
        ...


    def getMaxWaitTime(self) -> int:
        """
        Get the maximum number of ticks one has to wait for a fish appearing.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.

        Returns
        - Maximum number of ticks one has to wait for a fish appearing
        """
        ...


    def setMaxWaitTime(self, maxWaitTime: int) -> None:
        """
        Set the maximum number of ticks one has to wait for a fish appearing.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.

        Arguments
        - maxWaitTime: Maximum number of ticks one has to wait for a fish
        appearing
        """
        ...


    def setWaitTime(self, min: int, max: int) -> None:
        """
        Set both the minimum (default 100) and maximum (default 600) amount
        of ticks one has to wait for a fish appearing.

        Arguments
        - min: minimum ticks for a fish to appear
        - max: maximum ticks for a fish to appear
        """
        ...


    def getMinLureTime(self) -> int:
        """
        Get the minimum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 20 ticks (1 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.

        Returns
        - Minimum number of ticks one has to wait for a fish to bite
        """
        ...


    def setMinLureTime(self, minLureTime: int) -> None:
        """
        Set the minimum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 20 ticks (1 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.

        Arguments
        - minLureTime: Minimum number of ticks one has to wait for a fish
        to bite
        """
        ...


    def getMaxLureTime(self) -> int:
        """
        Get the maximum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 80 ticks (4 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.

        Returns
        - Maximum number of ticks one has to wait for a fish to bite
        """
        ...


    def setMaxLureTime(self, maxLureTime: int) -> None:
        """
        Set the maximum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 80 ticks (4 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.

        Arguments
        - maxLureTime: Maximum number of ticks one has to wait for a fish
        to bite
        """
        ...


    def setLureTime(self, min: int, max: int) -> None:
        """
        Set both the minimum (default 20) and maximum (default 80) amount
        of ticks one has to wait for a fish to bite after appearing.

        Arguments
        - min: minimum ticks to wait for a bite
        - max: maximum ticks to wait for a bite
        """
        ...


    def getMinLureAngle(self) -> float:
        """
        Get the minimum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 0 degrees.

        Returns
        - Minimum angle of where a fish will appear
        """
        ...


    def setMinLureAngle(self, minLureAngle: float) -> None:
        """
        Set the minimum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 0 degrees.

        Arguments
        - minLureAngle: Minimum angle of where a fish may appear
        """
        ...


    def getMaxLureAngle(self) -> float:
        """
        Get the maximum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 360 degrees.

        Returns
        - Maximum angle of where a fish will appear
        """
        ...


    def setMaxLureAngle(self, maxLureAngle: float) -> None:
        """
        Set the maximum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 360 degrees.

        Arguments
        - maxLureAngle: Maximum angle of where a fish may appear
        """
        ...


    def setLureAngle(self, min: float, max: float) -> None:
        """
        Set both the minimum (default 0) and maximum (default 360) angle of where
        a fish will appear after the wait time.
        
        0 degrees is positive Z, 90 degrees is negative X.

        Arguments
        - min: minimum angle in degrees
        - max: maximum angle in degrees
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


    def isSkyInfluenced(self) -> bool:
        """
        Whether or not wait and lure time will be impacted by direct sky access.
        
        True by default, causes a 50% time increase on average.

        Returns
        - skylight access influences catch rate
        """
        ...


    def setSkyInfluenced(self, skyInfluenced: bool) -> None:
        """
        Set whether or not wait and lure time will be impacted by direct sky
        access.
        
        True by default, causes a 50% time increase on average.

        Arguments
        - skyInfluenced: if this hook is influenced by skylight access
        """
        ...


    def isRainInfluenced(self) -> bool:
        """
        Whether or not wait and lure time will be impacted by rain.
        
        True by default, causes a 25% time decrease on average.

        Returns
        - rain influences catch rate
        """
        ...


    def setRainInfluenced(self, rainInfluenced: bool) -> None:
        """
        Set whether or not wait and lure time will be impacted by rain.
        
        True by default, causes a 25% time decrease on average.

        Arguments
        - rainInfluenced: if this hook is influenced by rain
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
