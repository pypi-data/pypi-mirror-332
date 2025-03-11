"""
Python module generated from Java source file org.bukkit.inventory.meta.components.CustomModelDataComponent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components import *
from typing import Any, Callable, Iterable, Tuple


class CustomModelDataComponent(ConfigurationSerializable):
    """
    Represents a component which adds custom model data.
    """

    def getFloats(self) -> list["Float"]:
        """
        Gets a list of the custom floats.

        Returns
        - unmodifiable list
        """
        ...


    def setFloats(self, floats: list["Float"]) -> None:
        """
        Sets a list of the custom floats.

        Arguments
        - floats: new list
        """
        ...


    def getFlags(self) -> list["Boolean"]:
        """
        Gets a list of the custom flags.

        Returns
        - unmodifiable list
        """
        ...


    def setFlags(self, flags: list["Boolean"]) -> None:
        """
        Sets a list of the custom flags.

        Arguments
        - flags: new list
        """
        ...


    def getStrings(self) -> list[str]:
        """
        Gets a list of the custom strings.

        Returns
        - unmodifiable list
        """
        ...


    def setStrings(self, strings: list[str]) -> None:
        """
        Sets a list of the custom strings.

        Arguments
        - strings: new list
        """
        ...


    def getColors(self) -> list["Color"]:
        """
        Gets a list of the custom colors.

        Returns
        - unmodifiable list
        """
        ...


    def setColors(self, colors: list["Color"]) -> None:
        """
        Sets a list of the custom colors.

        Arguments
        - colors: new list
        """
        ...
