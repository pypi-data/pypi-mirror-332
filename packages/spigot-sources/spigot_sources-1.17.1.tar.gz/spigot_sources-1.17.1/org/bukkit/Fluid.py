"""
Python module generated from Java source file org.bukkit.Fluid

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Fluid(Enum):

    WATER = 0
    FLOWING_WATER = 1
    LAVA = 2
    FLOWING_LAVA = 3


    def getKey(self) -> "NamespacedKey":
        ...
