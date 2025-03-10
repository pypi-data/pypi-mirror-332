"""
Python module generated from Java source file org.bukkit.WeatherType

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class WeatherType(Enum):
    """
    An enum of all current weather types
    """

    DOWNFALL = 0
    """
    Raining or snowing depending on biome.
    """
    CLEAR = 1
    """
    Clear weather, clouds but no rain.
    """
