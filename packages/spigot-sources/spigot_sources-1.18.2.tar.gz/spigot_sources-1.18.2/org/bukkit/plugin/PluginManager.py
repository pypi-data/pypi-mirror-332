"""
Python module generated from Java source file org.bukkit.plugin.PluginManager

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from org.bukkit.event import Event
from org.bukkit.event import EventPriority
from org.bukkit.event import Listener
from org.bukkit.permissions import Permissible
from org.bukkit.permissions import Permission
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class PluginManager:
    """
    Handles all plugin management from the Server
    """

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
        """
        Gets a list of all currently loaded plugins

        Returns
        - Array of Plugins
        """
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
        - InvalidDescriptionException: Thrown when the specified file
            contains an invalid description
        - UnknownDependencyException: If a required dependency could not
            be resolved
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


    def disablePlugins(self) -> None:
        """
        Disables all the loaded plugins
        """
        ...


    def clearPlugins(self) -> None:
        """
        Disables and removes all plugins
        """
        ...


    def callEvent(self, event: "Event") -> None:
        """
        Calls an event with the given details

        Arguments
        - event: Event details

        Raises
        - IllegalStateException: Thrown when an asynchronous event is
            fired from synchronous code.
            
            *Note: This is best-effort basis, and should not be used to test
            synchronized state. This is an indicator for flawed flow logic.*
        """
        ...


    def registerEvents(self, listener: "Listener", plugin: "Plugin") -> None:
        """
        Registers all the events in the given listener class

        Arguments
        - listener: Listener to register
        - plugin: Plugin to register
        """
        ...


    def registerEvent(self, event: type["Event"], listener: "Listener", priority: "EventPriority", executor: "EventExecutor", plugin: "Plugin") -> None:
        """
        Registers the specified executor to the given event class

        Arguments
        - event: Event type to register
        - listener: Listener to register
        - priority: Priority to register this event at
        - executor: EventExecutor to register
        - plugin: Plugin to register
        """
        ...


    def registerEvent(self, event: type["Event"], listener: "Listener", priority: "EventPriority", executor: "EventExecutor", plugin: "Plugin", ignoreCancelled: bool) -> None:
        """
        Registers the specified executor to the given event class

        Arguments
        - event: Event type to register
        - listener: Listener to register
        - priority: Priority to register this event at
        - executor: EventExecutor to register
        - plugin: Plugin to register
        - ignoreCancelled: Whether to pass cancelled events or not
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


    def getPermission(self, name: str) -> "Permission":
        """
        Gets a Permission from its fully qualified name

        Arguments
        - name: Name of the permission

        Returns
        - Permission, or null if none
        """
        ...


    def addPermission(self, perm: "Permission") -> None:
        """
        Adds a Permission to this plugin manager.
        
        If a permission is already defined with the given name of the new
        permission, an exception will be thrown.

        Arguments
        - perm: Permission to add

        Raises
        - IllegalArgumentException: Thrown when a permission with the same
            name already exists
        """
        ...


    def removePermission(self, perm: "Permission") -> None:
        """
        Removes a Permission registration from this plugin manager.
        
        If the specified permission does not exist in this plugin manager,
        nothing will happen.
        
        Removing a permission registration will **not** remove the
        permission from any Permissibles that have it.

        Arguments
        - perm: Permission to remove
        """
        ...


    def removePermission(self, name: str) -> None:
        """
        Removes a Permission registration from this plugin manager.
        
        If the specified permission does not exist in this plugin manager,
        nothing will happen.
        
        Removing a permission registration will **not** remove the
        permission from any Permissibles that have it.

        Arguments
        - name: Permission to remove
        """
        ...


    def getDefaultPermissions(self, op: bool) -> set["Permission"]:
        """
        Gets the default permissions for the given op status

        Arguments
        - op: Which set of default permissions to get

        Returns
        - The default permissions
        """
        ...


    def recalculatePermissionDefaults(self, perm: "Permission") -> None:
        """
        Recalculates the defaults for the given Permission.
        
        This will have no effect if the specified permission is not registered
        here.

        Arguments
        - perm: Permission to recalculate
        """
        ...


    def subscribeToPermission(self, permission: str, permissible: "Permissible") -> None:
        """
        Subscribes the given Permissible for information about the requested
        Permission, by name.
        
        If the specified Permission changes in any form, the Permissible will
        be asked to recalculate.

        Arguments
        - permission: Permission to subscribe to
        - permissible: Permissible subscribing
        """
        ...


    def unsubscribeFromPermission(self, permission: str, permissible: "Permissible") -> None:
        """
        Unsubscribes the given Permissible for information about the requested
        Permission, by name.

        Arguments
        - permission: Permission to unsubscribe from
        - permissible: Permissible subscribing
        """
        ...


    def getPermissionSubscriptions(self, permission: str) -> set["Permissible"]:
        """
        Gets a set containing all subscribed Permissibles to the given
        permission, by name

        Arguments
        - permission: Permission to query for

        Returns
        - Set containing all subscribed permissions
        """
        ...


    def subscribeToDefaultPerms(self, op: bool, permissible: "Permissible") -> None:
        """
        Subscribes to the given Default permissions by operator status
        
        If the specified defaults change in any form, the Permissible will be
        asked to recalculate.

        Arguments
        - op: Default list to subscribe to
        - permissible: Permissible subscribing
        """
        ...


    def unsubscribeFromDefaultPerms(self, op: bool, permissible: "Permissible") -> None:
        """
        Unsubscribes from the given Default permissions by operator status

        Arguments
        - op: Default list to unsubscribe from
        - permissible: Permissible subscribing
        """
        ...


    def getDefaultPermSubscriptions(self, op: bool) -> set["Permissible"]:
        """
        Gets a set containing all subscribed Permissibles to the given
        default list, by op status

        Arguments
        - op: Default list to query for

        Returns
        - Set containing all subscribed permissions
        """
        ...


    def getPermissions(self) -> set["Permission"]:
        """
        Gets a set of all registered permissions.
        
        This set is a copy and will not be modified live.

        Returns
        - Set containing all current registered permissions
        """
        ...


    def useTimings(self) -> bool:
        """
        Returns whether or not timing code should be used for event calls

        Returns
        - True if event timings are to be used
        """
        ...
