"""
Python module generated from Java source file org.bukkit.event.HandlerList

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import EnumMap
from java.util import ListIterator
from org.bukkit.event import *
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import RegisteredListener
from typing import Any, Callable, Iterable, Tuple


class HandlerList:
    """
    A list of event handlers, stored per-event. Based on lahwran's fevents.
    """

    def __init__(self):
        """
        Create a new handler list and initialize using EventPriority.
        
        The HandlerList is then added to meta-list for use in bakeAll()
        """
        ...


    @staticmethod
    def bakeAll() -> None:
        """
        Bake all handler lists. Best used just after all normal event
        registration is complete, ie just after all plugins are loaded if
        you're using fevents in a plugin system.
        """
        ...


    @staticmethod
    def unregisterAll() -> None:
        """
        Unregister all listeners from all handler lists.
        """
        ...


    @staticmethod
    def unregisterAll(plugin: "Plugin") -> None:
        """
        Unregister a specific plugin's listeners from all handler lists.

        Arguments
        - plugin: plugin to unregister
        """
        ...


    @staticmethod
    def unregisterAll(listener: "Listener") -> None:
        """
        Unregister a specific listener from all handler lists.

        Arguments
        - listener: listener to unregister
        """
        ...


    def register(self, listener: "RegisteredListener") -> None:
        """
        Register a new listener in this handler list

        Arguments
        - listener: listener to register
        """
        ...


    def registerAll(self, listeners: Iterable["RegisteredListener"]) -> None:
        """
        Register a collection of new listeners in this handler list

        Arguments
        - listeners: listeners to register
        """
        ...


    def unregister(self, listener: "RegisteredListener") -> None:
        """
        Remove a listener from a specific order slot

        Arguments
        - listener: listener to remove
        """
        ...


    def unregister(self, plugin: "Plugin") -> None:
        """
        Remove a specific plugin's listeners from this handler

        Arguments
        - plugin: plugin to remove
        """
        ...


    def unregister(self, listener: "Listener") -> None:
        """
        Remove a specific listener from this handler

        Arguments
        - listener: listener to remove
        """
        ...


    def bake(self) -> None:
        """
        Bake HashMap and ArrayLists to 2d array - does nothing if not necessary
        """
        ...


    def getRegisteredListeners(self) -> list["RegisteredListener"]:
        """
        Get the baked registered listeners associated with this handler list

        Returns
        - the array of registered listeners
        """
        ...


    @staticmethod
    def getRegisteredListeners(plugin: "Plugin") -> list["RegisteredListener"]:
        """
        Get a specific plugin's registered listeners associated with this
        handler list

        Arguments
        - plugin: the plugin to get the listeners of

        Returns
        - the list of registered listeners
        """
        ...


    @staticmethod
    def getHandlerLists() -> list["HandlerList"]:
        """
        Get a list of all handler lists for every event type

        Returns
        - the list of all handler lists
        """
        ...
