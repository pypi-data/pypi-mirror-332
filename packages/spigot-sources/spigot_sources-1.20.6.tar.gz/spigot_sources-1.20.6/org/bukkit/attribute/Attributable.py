"""
Python module generated from Java source file org.bukkit.attribute.Attributable

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.attribute import *
from typing import Any, Callable, Iterable, Tuple


class Attributable:
    """
    Represents an object which may contain attributes.
    """

    def getAttribute(self, attribute: "Attribute") -> "AttributeInstance":
        """
        Gets the specified attribute instance from the object. This instance will
        be backed directly to the object and any changes will be visible at once.

        Arguments
        - attribute: the attribute to get

        Returns
        - the attribute instance or null if not applicable to this object
        """
        ...
