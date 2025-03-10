"""
Python module generated from Java source file org.bukkit.configuration.Configuration

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class Configuration(ConfigurationSection):
    """
    Represents a source of configurable options and settings
    """

    def addDefault(self, path: str, value: "Object") -> None:
        """
        Sets the default value of the given path as provided.
        
        If no source Configuration was provided as a default
        collection, then a new MemoryConfiguration will be created to
        hold the new default value.
        
        If value is null, the value will be removed from the default
        Configuration source.

        Arguments
        - path: Path of the value to set.
        - value: Value to set the default to.

        Raises
        - IllegalArgumentException: Thrown if path is null.
        """
        ...


    def addDefaults(self, defaults: dict[str, "Object"]) -> None:
        """
        Sets the default values of the given paths as provided.
        
        If no source Configuration was provided as a default
        collection, then a new MemoryConfiguration will be created to
        hold the new default values.

        Arguments
        - defaults: A map of Path->Values to add to defaults.

        Raises
        - IllegalArgumentException: Thrown if defaults is null.
        """
        ...


    def addDefaults(self, defaults: "Configuration") -> None:
        """
        Sets the default values of the given paths as provided.
        
        If no source Configuration was provided as a default
        collection, then a new MemoryConfiguration will be created to
        hold the new default value.
        
        This method will not hold a reference to the specified Configuration,
        nor will it automatically update if that Configuration ever changes. If
        you require this, you should set the default source with .setDefaults(org.bukkit.configuration.Configuration).

        Arguments
        - defaults: A configuration holding a list of defaults to copy.

        Raises
        - IllegalArgumentException: Thrown if defaults is null or this.
        """
        ...


    def setDefaults(self, defaults: "Configuration") -> None:
        """
        Sets the source of all default values for this Configuration.
        
        If a previous source was set, or previous default values were defined,
        then they will not be copied to the new source.

        Arguments
        - defaults: New source of default values for this configuration.

        Raises
        - IllegalArgumentException: Thrown if defaults is null or this.
        """
        ...


    def getDefaults(self) -> "Configuration":
        """
        Gets the source Configuration for this configuration.
        
        If no configuration source was set, but default values were added, then
        a MemoryConfiguration will be returned. If no source was set
        and no defaults were set, then this method will return null.

        Returns
        - Configuration source for default values, or null if none exist.
        """
        ...


    def options(self) -> "ConfigurationOptions":
        """
        Gets the ConfigurationOptions for this Configuration.
        
        All setters through this method are chainable.

        Returns
        - Options for this configuration
        """
        ...
