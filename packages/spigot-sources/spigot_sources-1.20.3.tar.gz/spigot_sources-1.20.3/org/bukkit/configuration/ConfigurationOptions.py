"""
Python module generated from Java source file org.bukkit.configuration.ConfigurationOptions

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class ConfigurationOptions:
    """
    Various settings for controlling the input and output of a Configuration
    """

    def configuration(self) -> "Configuration":
        """
        Returns the Configuration that this object is responsible for.

        Returns
        - Parent configuration
        """
        ...


    def pathSeparator(self) -> str:
        """
        Gets the char that will be used to separate ConfigurationSections
        
        This value does not affect how the Configuration is stored,
        only in how you access the data. The default value is '.'.

        Returns
        - Path separator
        """
        ...


    def pathSeparator(self, value: str) -> "ConfigurationOptions":
        """
        Sets the char that will be used to separate ConfigurationSections
        
        This value does not affect how the Configuration is stored,
        only in how you access the data. The default value is '.'.

        Arguments
        - value: Path separator

        Returns
        - This object, for chaining
        """
        ...


    def copyDefaults(self) -> bool:
        """
        Checks if the Configuration should copy values from its default
        Configuration directly.
        
        If this is True, all values in the default Configuration will be
        directly copied, making it impossible to distinguish between values
        that were set and values that are provided by default. As a result,
        ConfigurationSection.contains(java.lang.String) will always
        return the same value as ConfigurationSection.isSet(java.lang.String). The default value is
        False.

        Returns
        - Whether or not defaults are directly copied
        """
        ...


    def copyDefaults(self, value: bool) -> "ConfigurationOptions":
        """
        Sets if the Configuration should copy values from its default
        Configuration directly.
        
        If this is True, all values in the default Configuration will be
        directly copied, making it impossible to distinguish between values
        that were set and values that are provided by default. As a result,
        ConfigurationSection.contains(java.lang.String) will always
        return the same value as ConfigurationSection.isSet(java.lang.String). The default value is
        False.

        Arguments
        - value: Whether or not defaults are directly copied

        Returns
        - This object, for chaining
        """
        ...
