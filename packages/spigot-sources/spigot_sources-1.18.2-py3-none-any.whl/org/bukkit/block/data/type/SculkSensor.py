"""
Python module generated from Java source file org.bukkit.block.data.type.SculkSensor

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import AnaloguePowerable
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class SculkSensor(AnaloguePowerable, Waterlogged):
    """
    'sculk_sensor_phase' indicates the current operational phase of the sensor.
    """

    def getPhase(self) -> "Phase":
        """
        Gets the value of the 'sculk_sensor_phase' property.

        Returns
        - the 'sculk_sensor_phase' value
        """
        ...


    def setPhase(self, phase: "Phase") -> None:
        """
        Sets the value of the 'sculk_sensor_phase' property.

        Arguments
        - phase: the new 'sculk_sensor_phase' value
        """
        ...


    class Phase(Enum):
        """
        The Phase of the sensor.
        """

        INACTIVE = 0
        """
        The sensor is inactive.
        """
        ACTIVE = 1
        """
        The sensor is active.
        """
        COOLDOWN = 2
        """
        The sensor is cooling down.
        """
