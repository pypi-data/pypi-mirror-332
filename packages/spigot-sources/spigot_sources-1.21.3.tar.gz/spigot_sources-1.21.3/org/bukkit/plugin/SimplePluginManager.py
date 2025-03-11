"""
Python module generated from Java source file org.bukkit.plugin.SimplePluginManager

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableSet
from com.google.common.graph import GraphBuilder
from com.google.common.graph import Graphs
from com.google.common.graph import MutableGraph
from java.io import File
from java.lang.reflect import Constructor
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.util import Iterator
from java.util import LinkedHashSet
from java.util import Locale
from java.util import WeakHashMap
from java.util.regex import Matcher
from java.util.regex import Pattern
from org.bukkit import Server
from org.bukkit import World
from org.bukkit.command import Command
from org.bukkit.command import PluginCommandYamlParser
from org.bukkit.command import SimpleCommandMap
from org.bukkit.event import Event
from org.bukkit.event import EventPriority
from org.bukkit.event import HandlerList
from org.bukkit.event import Listener
from org.bukkit.permissions import Permissible
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.bukkit.plugin import *
from org.bukkit.util import FileUtil
from typing import Any, Callable, Iterable, Tuple


class SimplePluginManager(PluginManager):
    """
    Handles all plugin management from the Server
    """

    def __init__(self, instance: "Server", commandMap: "SimpleCommandMap"):
        ...


    def registerInterface(self, loader: type["PluginLoader"]) -> None:
        """
        Registers the specified plugin loader

        Arguments
        - loader: Class name of the PluginLoader to register

        Raises
        - IllegalArgumentException: Thrown when the given Class is not a
            valid PluginLoader
        """
        ...


    def loadPlugins(self, directory: "File") -> list["Plugin"]:
        """
        Loads the plugins contained within the specified directory

        Arguments
        - directory: Directory to check for plugins

        Returns
        - A list of all plugins loaded
        """
        ...


    def loadPlugins(self, files: list["File"]) -> list["Plugin"]:
        """
        Loads the plugins in the list of the files

        Arguments
        - files: List of files containing plugins to load

        Returns
        - A list of all plugins loaded
        """
        ...


    def loadPlugin(self, file: "File") -> "Plugin":
        """
        Loads the plugin in the specified file
        
        File must be valid according to the current enabled Plugin interfaces

        Arguments
        - file: File containing the plugin to load

        Returns
        - The Plugin loaded, or null if it was invalid

        Raises
        - InvalidPluginException: Thrown when the specified file is not a
            valid plugin
        - UnknownDependencyException: If a required dependency could not
            be found
        """
        ...


    def getPlugin(self, name: str) -> "Plugin":
        """
        Checks if the given plugin is loaded and returns it when applicable
        
        Please note that the name of the plugin is case-sensitive

        Arguments
        - name: Name of the plugin to check

        Returns
        - Plugin if it exists, otherwise null
        """
        ...


    def getPlugins(self) -> list["Plugin"]:
        ...


    def isPluginEnabled(self, name: str) -> bool:
        """
        Checks if the given plugin is enabled or not
        
        Please note that the name of the plugin is case-sensitive.

        Arguments
        - name: Name of the plugin to check

        Returns
        - True if the plugin is enabled, otherwise False
        """
        ...


    def isPluginEnabled(self, plugin: "Plugin") -> bool:
        """
        Checks if the given plugin is enabled or not

        Arguments
        - plugin: Plugin to check

        Returns
        - True if the plugin is enabled, otherwise False
        """
        ...


    def enablePlugin(self, plugin: "Plugin") -> None:
        ...


    def disablePlugins(self) -> None:
        ...


    def disablePlugin(self, plugin: "Plugin") -> None:
        ...


    def clearPlugins(self) -> None:
        ...


    def callEvent(self, event: "Event") -> None:
        """
        Calls an event with the given details.

        Arguments
        - event: Event details
        """
        ...


    def registerEvents(self, listener: "Listener", plugin: "Plugin") -> None:
        ...


    def registerEvent(self, event: type["Event"], listener: "Listener", priority: "EventPriority", executor: "EventExecutor", plugin: "Plugin") -> None:
        ...


    def registerEvent(self, event: type["Event"], listener: "Listener", priority: "EventPriority", executor: "EventExecutor", plugin: "Plugin", ignoreCancelled: bool) -> None:
        """
        Registers the given event to the specified listener using a directly
        passed EventExecutor

        Arguments
        - event: Event class to register
        - listener: PlayerListener to register
        - priority: Priority of this event
        - executor: EventExecutor to register
        - plugin: Plugin to register
        - ignoreCancelled: Do not call executor if event was already
            cancelled
        """
        ...


    def getPermission(self, name: str) -> "Permission":
        ...


    def addPermission(self, perm: "Permission") -> None:
        ...


    def addPermission(self, perm: "Permission", dirty: bool) -> None:
        ...


    def getDefaultPermissions(self, op: bool) -> set["Permission"]:
        ...


    def removePermission(self, perm: "Permission") -> None:
        ...


    def removePermission(self, name: str) -> None:
        ...


    def recalculatePermissionDefaults(self, perm: "Permission") -> None:
        ...


    def dirtyPermissibles(self) -> None:
        ...


    def subscribeToPermission(self, permission: str, permissible: "Permissible") -> None:
        ...


    def unsubscribeFromPermission(self, permission: str, permissible: "Permissible") -> None:
        ...


    def getPermissionSubscriptions(self, permission: str) -> set["Permissible"]:
        ...


    def subscribeToDefaultPerms(self, op: bool, permissible: "Permissible") -> None:
        ...


    def unsubscribeFromDefaultPerms(self, op: bool, permissible: "Permissible") -> None:
        ...


    def getDefaultPermSubscriptions(self, op: bool) -> set["Permissible"]:
        ...


    def getPermissions(self) -> set["Permission"]:
        ...


    def isTransitiveDepend(self, plugin: "PluginDescriptionFile", depend: "PluginDescriptionFile") -> bool:
        ...


    def useTimings(self) -> bool:
        ...


    def useTimings(self, use: bool) -> None:
        """
        Sets whether or not per event timing code should be used

        Arguments
        - use: True if per event timing code should be used
        """
        ...
