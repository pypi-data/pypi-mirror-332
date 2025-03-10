"""
Python module generated from Java source file org.bukkit.inventory.Recipe

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class Recipe:
    """
    Represents some type of crafting recipe.
    """

    def getResult(self) -> "ItemStack":
        """
        Get the result of this recipe.

        Returns
        - The result stack
        """
        ...
