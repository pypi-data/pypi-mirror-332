"""
Python module generated from Java source file org.bukkit.SoundGroup

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class SoundGroup:
    """
    Represents a group of sounds for blocks that are played when various actions
    happen (ie stepping, breaking, hitting, etc).
    """

    def getVolume(self) -> float:
        """
        Get the volume these sounds are played at.
        
        Note that this volume does not always represent the actual volume
        received by the client.

        Returns
        - volume
        """
        ...


    def getPitch(self) -> float:
        """
        Gets the pitch these sounds are played at.
        
        Note that this pitch does not always represent the actual pitch received
        by the client.

        Returns
        - pitch
        """
        ...


    def getBreakSound(self) -> "Sound":
        """
        Gets the corresponding breaking sound for this group.

        Returns
        - the break sound
        """
        ...


    def getStepSound(self) -> "Sound":
        """
        Gets the corresponding step sound for this group.

        Returns
        - the step sound
        """
        ...


    def getPlaceSound(self) -> "Sound":
        """
        Gets the corresponding place sound for this group.

        Returns
        - the place sound
        """
        ...


    def getHitSound(self) -> "Sound":
        """
        Gets the corresponding hit sound for this group.

        Returns
        - the hit sound
        """
        ...


    def getFallSound(self) -> "Sound":
        """
        Gets the corresponding fall sound for this group.

        Returns
        - the fall sound
        """
        ...
