"""
Python module generated from Java source file org.bukkit.block.SculkSensor

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class SculkSensor(TileState):
    """
    Represents a captured state of a sculk sensor
    """

    def getLastVibrationFrequency(self) -> int:
        """
        Gets the last vibration frequency of this sensor.
        
        Different activities detected by the sensor will produce different
        frequencies and dictate the output of connected comparators.

        Returns
        - frequency between 0-15.
        """
        ...


    def setLastVibrationFrequency(self, lastVibrationFrequency: int) -> None:
        """
        Sets the last vibration frequency of this sensor.
        
        Different activities detected by the sensor will produce different
        frequencies and dictate the output of connected comparators.

        Arguments
        - lastVibrationFrequency: frequency between 0-15.
        """
        ...
