"""
Python module generated from Java source file org.bukkit.plugin.PluginLoader

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.util.regex import Pattern
from org.bukkit.event import Event
from org.bukkit.event import Listener
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class PluginLoader:
    """
    Represents a plugin loader, which handles direct access to specific types
    of plugins
    """

    def loadPlugin(self, file: "File") -> "Plugin":
        """
        Loads the plugin contained in the specified file

        Arguments
        - file: File to attempt to load

        Returns
        - Plugin that was contained in the specified file, or null if
            unsuccessful

        Raises
        - InvalidPluginException: Thrown when the specified file is not a
            plugin
        - UnknownDependencyException: If a required dependency could not
            be found
        """
        ...


    def getPluginDescription(self, file: "File") -> "PluginDescriptionFile":
        """
        Loads a PluginDescriptionFile from the specified file

        Arguments
        - file: File to attempt to load from

        Returns
        - A new PluginDescriptionFile loaded from the plugin.yml in the
            specified file

        Raises
        - InvalidDescriptionException: If the plugin description file
            could not be created
        """
        ...


    def getPluginFileFilters(self) -> list["Pattern"]:
        """
        Returns a list of all filename filters expected by this PluginLoader

        Returns
        - The filters
        """
        ...


    def createRegisteredListeners(self, listener: "Listener", plugin: "Plugin") -> dict[type["Event"], set["RegisteredListener"]]:
        """
        Creates and returns registered listeners for the event classes used in
        this listener

        Arguments
        - listener: The object that will handle the eventual call back
        - plugin: The plugin to use when creating registered listeners

        Returns
        - The registered listeners.
        """
        ...


    def enablePlugin(self, plugin: "Plugin") -> None:
        """
        Enables the specified plugin
        
        Attempting to enable a plugin that is already enabled will have no
        effect

        Arguments
        - plugin: Plugin to enable
        """
        ...


    def disablePlugin(self, plugin: "Plugin") -> None:
        """
        Disables the specified plugin
        
        Attempting to disable a plugin that is not enabled will have no effect

        Arguments
        - plugin: Plugin to disable
        """
        ...
