"""
Python module generated from Java source file org.bukkit.configuration.serialization.ConfigurationSerialization

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from org.bukkit import Color
from org.bukkit import FireworkEffect
from org.bukkit import Location
from org.bukkit.attribute import AttributeModifier
from org.bukkit.block.banner import Pattern
from org.bukkit.block.spawner import SpawnRule
from org.bukkit.configuration import Configuration
from org.bukkit.configuration.serialization import *
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffect
from org.bukkit.util import BlockVector
from org.bukkit.util import BoundingBox
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class ConfigurationSerialization:
    """
    Utility class for storing and retrieving classes for Configuration.
    """

    SERIALIZED_TYPE_KEY = "=="


    def deserialize(self, args: dict[str, Any]) -> "ConfigurationSerializable":
        ...


    @staticmethod
    def deserializeObject(args: dict[str, Any], clazz: type["ConfigurationSerializable"]) -> "ConfigurationSerializable":
        """
        Attempts to deserialize the given arguments into a new instance of the
        given class.
        
        The class must implement ConfigurationSerializable, including
        the extra methods as specified in the javadoc of
        ConfigurationSerializable.
        
        If a new instance could not be made, an example being the class not
        fully implementing the interface, null will be returned.

        Arguments
        - args: Arguments for deserialization
        - clazz: Class to deserialize into

        Returns
        - New instance of the specified class
        """
        ...


    @staticmethod
    def deserializeObject(args: dict[str, Any]) -> "ConfigurationSerializable":
        """
        Attempts to deserialize the given arguments into a new instance of the
        given class.
        
        The class must implement ConfigurationSerializable, including
        the extra methods as specified in the javadoc of
        ConfigurationSerializable.
        
        If a new instance could not be made, an example being the class not
        fully implementing the interface, null will be returned.

        Arguments
        - args: Arguments for deserialization

        Returns
        - New instance of the specified class
        """
        ...


    @staticmethod
    def registerClass(clazz: type["ConfigurationSerializable"]) -> None:
        """
        Registers the given ConfigurationSerializable class by its
        alias

        Arguments
        - clazz: Class to register
        """
        ...


    @staticmethod
    def registerClass(clazz: type["ConfigurationSerializable"], alias: str) -> None:
        """
        Registers the given alias to the specified ConfigurationSerializable class

        Arguments
        - clazz: Class to register
        - alias: Alias to register as

        See
        - SerializableAs
        """
        ...


    @staticmethod
    def unregisterClass(alias: str) -> None:
        """
        Unregisters the specified alias to a ConfigurationSerializable

        Arguments
        - alias: Alias to unregister
        """
        ...


    @staticmethod
    def unregisterClass(clazz: type["ConfigurationSerializable"]) -> None:
        """
        Unregisters any aliases for the specified ConfigurationSerializable class

        Arguments
        - clazz: Class to unregister
        """
        ...


    @staticmethod
    def getClassByAlias(alias: str) -> type["ConfigurationSerializable"]:
        """
        Attempts to get a registered ConfigurationSerializable class by
        its alias

        Arguments
        - alias: Alias of the serializable

        Returns
        - Registered class, or null if not found
        """
        ...


    @staticmethod
    def getAlias(clazz: type["ConfigurationSerializable"]) -> str:
        """
        Gets the correct alias for the given ConfigurationSerializable
        class

        Arguments
        - clazz: Class to get alias for

        Returns
        - Alias to use for the class
        """
        ...
