"""
Python module generated from Java source file org.bukkit.FeatureFlag

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class FeatureFlag(Keyed):
    """
    This represents a Feature Flag for a World.
    """

    VANILLA = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("vanilla"))
    BUNDLE = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("bundle"))
    UPDATE_1_20 = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("update_1_20"))
    """
    <strong>AVAILABLE BETWEEN VERSIONS:</strong> 1.19 - 1.19.4
    """
