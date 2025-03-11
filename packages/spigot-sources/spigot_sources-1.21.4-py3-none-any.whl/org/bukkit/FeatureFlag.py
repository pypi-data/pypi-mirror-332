"""
Python module generated from Java source file org.bukkit.FeatureFlag

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class FeatureFlag(Keyed):
    """
    This represents a Feature Flag for a World.
    
    Flags which are unavailable in the current version will be null and/or
    removed.
    """

    VANILLA = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("vanilla"))
    BUNDLE = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("bundle"))
    """
    <strong>AVAILABLE BETWEEN VERSIONS:</strong> 1.19.3 - 1.21.1

    Deprecated
    - not available since 1.21.2
    """
    UPDATE_1_20 = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("update_1_20"))
    """
    <strong>AVAILABLE BETWEEN VERSIONS:</strong> 1.19 - 1.19.4

    Deprecated
    - not available since 1.20
    """
    TRADE_REBALANCE = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("trade_rebalance"))
    UPDATE_121 = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("update_1_21"))
    """
    <strong>AVAILABLE BETWEEN VERSIONS:</strong> 1.20.5 - 1.20.6

    Deprecated
    - not available since 1.21
    """
    WINTER_DROP = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("winter_drop"))
    """
    <strong>AVAILABLE BETWEEN VERSIONS:</strong> 1.21.2 - 1.21.3

    Deprecated
    - not available since 1.21.4
    """
    REDSTONE_EXPERIMENTS = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("redstone_experiments"))
    MINECART_IMPROVEMENTS = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("minecart_improvements"))
