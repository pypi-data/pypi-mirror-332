"""
Python module generated from Java source file org.bukkit.enchantments.EnchantmentWrapper

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.enchantments import *
from typing import Any, Callable, Iterable, Tuple


class EnchantmentWrapper(Enchantment):
    """
    A simple wrapper for ease of selecting Enchantments

    Deprecated
    - only for backwards compatibility, EnchantmentWrapper is no longer used.
    """

    def getEnchantment(self) -> "Enchantment":
        """
        Gets the enchantment bound to this wrapper

        Returns
        - Enchantment
        """
        ...
