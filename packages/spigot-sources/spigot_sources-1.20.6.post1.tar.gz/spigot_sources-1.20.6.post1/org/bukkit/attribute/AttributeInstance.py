"""
Python module generated from Java source file org.bukkit.attribute.AttributeInstance

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.attribute import *
from typing import Any, Callable, Iterable, Tuple


class AttributeInstance:
    """
    Represents a mutable instance of an attribute and its associated modifiers
    and values.
    """

    def getAttribute(self) -> "Attribute":
        """
        The attribute pertaining to this instance.

        Returns
        - the attribute
        """
        ...


    def getBaseValue(self) -> float:
        """
        Base value of this instance before modifiers are applied.

        Returns
        - base value
        """
        ...


    def setBaseValue(self, value: float) -> None:
        """
        Set the base value of this instance.

        Arguments
        - value: new base value
        """
        ...


    def getModifiers(self) -> Iterable["AttributeModifier"]:
        """
        Get all modifiers present on this instance.

        Returns
        - a copied collection of all modifiers
        """
        ...


    def addModifier(self, modifier: "AttributeModifier") -> None:
        """
        Add a modifier to this instance.

        Arguments
        - modifier: to add
        """
        ...


    def removeModifier(self, modifier: "AttributeModifier") -> None:
        """
        Remove a modifier from this instance.

        Arguments
        - modifier: to remove
        """
        ...


    def getValue(self) -> float:
        """
        Get the value of this instance after all associated modifiers have been
        applied.

        Returns
        - the total attribute value
        """
        ...


    def getDefaultValue(self) -> float:
        """
        Gets the default value of the Attribute attached to this instance.

        Returns
        - server default value
        """
        ...
