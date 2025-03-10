"""
Python module generated from Java source file org.bukkit.block.data.type.Lectern

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Lectern(Directional, Powerable):
    """
    'has_book' is a quick flag to check whether this lectern has a book inside
    it.
    """

    def hasBook(self) -> bool:
        """
        Gets the value of the 'has_book' property.

        Returns
        - the 'has_book' value
        """
        ...
