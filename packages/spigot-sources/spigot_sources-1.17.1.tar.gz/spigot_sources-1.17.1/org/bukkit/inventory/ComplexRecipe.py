"""
Python module generated from Java source file org.bukkit.inventory.ComplexRecipe

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ComplexRecipe(Recipe, Keyed):
    """
    Represents a complex recipe which has imperative server-defined behavior, eg
    armor dyeing.
    
    Note: Since a complex recipe has dynamic outputs, .getResult() will
    sometimes return an AIR ItemStack.
    """


