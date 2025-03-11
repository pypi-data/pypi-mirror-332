"""
Python module generated from Java source file org.bukkit.damage.DamageEffect

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Bukkit
from org.bukkit import Sound
from org.bukkit.damage import *
from typing import Any, Callable, Iterable, Tuple


class DamageEffect:
    """
    Represents a type of effect that occurs when damage is inflicted. Currently,
    effects only determine the sound that plays.
    """

    HURT = getDamageEffect("hurt")
    """
    The default damage effect.
    """
    THORNS = getDamageEffect("thorns")
    """
    Thorns.
    """
    DROWNING = getDamageEffect("drowning")
    """
    Drowning.
    """
    BURNING = getDamageEffect("burning")
    """
    A single burn tick (fire, lava, etc.).
    """
    POKING = getDamageEffect("poking")
    """
    Poked by a berry bush.
    """
    FREEZING = getDamageEffect("freezing")
    """
    Freeze tick (powder snow).
    """


    @staticmethod
    def getDamageEffect(key: str) -> "DamageEffect":
        ...


    def getSound(self) -> "Sound":
        """
        Get the Sound played for this DamageEffect.

        Returns
        - the sound
        """
        ...
