"""
Python module generated from Java source file org.bukkit.inventory.meta.FireworkMeta

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import FireworkEffect
from org.bukkit import Material
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class FireworkMeta(ItemMeta):
    """
    Represents a Material.FIREWORK_ROCKET and its effects.
    """

    def addEffect(self, effect: "FireworkEffect") -> None:
        """
        Add another effect to this firework.

        Arguments
        - effect: The firework effect to add

        Raises
        - IllegalArgumentException: If effect is null
        """
        ...


    def addEffects(self, *effects: Tuple["FireworkEffect", ...]) -> None:
        """
        Add several effects to this firework.

        Arguments
        - effects: The firework effects to add

        Raises
        - IllegalArgumentException: If effects is null
        - IllegalArgumentException: If any effect is null (may be thrown
            after changes have occurred)
        """
        ...


    def addEffects(self, effects: Iterable["FireworkEffect"]) -> None:
        """
        Add several firework effects to this firework.

        Arguments
        - effects: An iterable object whose iterator yields the desired
            firework effects

        Raises
        - IllegalArgumentException: If effects is null
        - IllegalArgumentException: If any effect is null (may be thrown
            after changes have occurred)
        """
        ...


    def getEffects(self) -> list["FireworkEffect"]:
        """
        Get the effects in this firework.

        Returns
        - An immutable list of the firework effects
        """
        ...


    def getEffectsSize(self) -> int:
        """
        Get the number of effects in this firework.

        Returns
        - The number of effects
        """
        ...


    def removeEffect(self, index: int) -> None:
        """
        Remove an effect from this firework.

        Arguments
        - index: The index of the effect to remove

        Raises
        - IndexOutOfBoundsException: If index < 0 or index > .getEffectsSize()
        """
        ...


    def clearEffects(self) -> None:
        """
        Remove all effects from this firework.
        """
        ...


    def hasEffects(self) -> bool:
        """
        Get whether this firework has any effects.

        Returns
        - True if it has effects, False if there are no effects
        """
        ...


    def getPower(self) -> int:
        """
        Gets the approximate height the firework will fly.

        Returns
        - approximate flight height of the firework.
        """
        ...


    def setPower(self, power: int) -> None:
        """
        Sets the approximate power of the firework. Each level of power is half
        a second of flight time.

        Arguments
        - power: the power of the firework, from 0-128

        Raises
        - IllegalArgumentException: if height<0 or height>128
        """
        ...


    def clone(self) -> "FireworkMeta":
        ...
