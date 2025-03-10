"""
Python module generated from Java source file org.bukkit.entity.minecart.RideableMinecart

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from typing import Any, Callable, Iterable, Tuple


class RideableMinecart(Minecart):
    """
    Represents a minecart that can have certain org.bukkit.entity.Entity entities as passengers. Normal passengers
    include all org.bukkit.entity.LivingEntity living entities with
    the exception of org.bukkit.entity.IronGolem iron golems.
    Non-player entities that meet normal passenger criteria automatically
    mount these minecarts when close enough.
    """


