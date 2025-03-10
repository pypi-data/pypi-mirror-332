"""
Python module generated from Java source file org.bukkit.plugin.java.JavaPluginLoader

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.io import File
from java.io import FileNotFoundException
from java.io import IOException
from java.io import InputStream
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.util import Arrays
from java.util.concurrent import CopyOnWriteArrayList
from java.util.jar import JarEntry
from java.util.jar import JarFile
from java.util.regex import Pattern
from org.bukkit import Server
from org.bukkit import Warning
from org.bukkit.Warning import WarningState
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import EventHandler
from org.bukkit.event import Listener
from org.bukkit.event.server import PluginDisableEvent
from org.bukkit.event.server import PluginEnableEvent
from org.bukkit.plugin import AuthorNagException
from org.bukkit.plugin import EventExecutor
from org.bukkit.plugin import InvalidDescriptionException
from org.bukkit.plugin import InvalidPluginException
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.plugin import PluginLoader
from org.bukkit.plugin import RegisteredListener
from org.bukkit.plugin import SimplePluginManager
from org.bukkit.plugin import TimedRegisteredListener
from org.bukkit.plugin import UnknownDependencyException
from org.bukkit.plugin.java import *
from org.spigotmc import CustomTimingsHandler
from org.yaml.snakeyaml.error import YAMLException
from typing import Any, Callable, Iterable, Tuple


class JavaPluginLoader(PluginLoader):
    """
    Represents a Java plugin loader, allowing plugins in the form of .jar
    """

    pluginParentTimer = CustomTimingsHandler("** Plugins")


    def __init__(self, instance: "Server"):
        """
        This class was not meant to be constructed explicitly

        Arguments
        - instance: the server instance
        """
        ...


    def loadPlugin(self, file: "File") -> "Plugin":
        ...


    def getPluginDescription(self, file: "File") -> "PluginDescriptionFile":
        ...


    def getPluginFileFilters(self) -> list["Pattern"]:
        ...


    def createRegisteredListeners(self, listener: "Listener", plugin: "Plugin") -> dict[type["Event"], set["RegisteredListener"]]:
        ...


    def enablePlugin(self, plugin: "Plugin") -> None:
        ...


    def disablePlugin(self, plugin: "Plugin") -> None:
        ...
