"""
Python module generated from Java source file org.bukkit.plugin.java.JavaPlugin

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Charsets
from com.google.common.base import Preconditions
from java.io import File
from java.io import FileOutputStream
from java.io import IOException
from java.io import InputStream
from java.io import InputStreamReader
from java.io import OutputStream
from java.io import Reader
from java.net import URL
from java.net import URLConnection
from org.bukkit import Server
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import PluginCommand
from org.bukkit.configuration.file import FileConfiguration
from org.bukkit.configuration.file import YamlConfiguration
from org.bukkit.generator import BiomeProvider
from org.bukkit.generator import ChunkGenerator
from org.bukkit.plugin import PluginBase
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.plugin import PluginLoader
from org.bukkit.plugin import PluginLogger
from org.bukkit.plugin.java import *
from typing import Any, Callable, Iterable, Tuple


class JavaPlugin(PluginBase):
    """
    Represents a Java plugin and its main class. It contains fundamental methods
    and fields for a plugin to be loaded and work properly. This is an indirect
    implementation of org.bukkit.plugin.Plugin.
    """

    def __init__(self):
        ...


    def getDataFolder(self) -> "File":
        """
        Returns the folder that the plugin data's files are located in. The
        folder may not yet exist.

        Returns
        - The folder.
        """
        ...


    def getPluginLoader(self) -> "PluginLoader":
        """
        Gets the associated PluginLoader responsible for this plugin

        Returns
        - PluginLoader that controls this plugin
        """
        ...


    def getServer(self) -> "Server":
        """
        Returns the Server instance currently running this plugin

        Returns
        - Server running this plugin
        """
        ...


    def isEnabled(self) -> bool:
        """
        Returns a value indicating whether or not this plugin is currently
        enabled

        Returns
        - True if this plugin is enabled, otherwise False
        """
        ...


    def getDescription(self) -> "PluginDescriptionFile":
        """
        Returns the plugin.yaml file containing the details for this plugin

        Returns
        - Contents of the plugin.yaml file
        """
        ...


    def getConfig(self) -> "FileConfiguration":
        ...


    def reloadConfig(self) -> None:
        ...


    def saveConfig(self) -> None:
        ...


    def saveDefaultConfig(self) -> None:
        ...


    def saveResource(self, resourcePath: str, replace: bool) -> None:
        ...


    def getResource(self, filename: str) -> "InputStream":
        ...


    def onCommand(self, sender: "CommandSender", command: "Command", label: str, args: list[str]) -> bool:
        """

        """
        ...


    def onTabComplete(self, sender: "CommandSender", command: "Command", alias: str, args: list[str]) -> list[str]:
        """

        """
        ...


    def getCommand(self, name: str) -> "PluginCommand":
        """
        Gets the command with the given name, specific to this plugin. Commands
        need to be registered in the PluginDescriptionFile.getCommands()
        PluginDescriptionFile to exist at runtime.

        Arguments
        - name: name or alias of the command

        Returns
        - the plugin command if found, otherwise null
        """
        ...


    def onLoad(self) -> None:
        ...


    def onDisable(self) -> None:
        ...


    def onEnable(self) -> None:
        ...


    def getDefaultWorldGenerator(self, worldName: str, id: str) -> "ChunkGenerator":
        ...


    def getDefaultBiomeProvider(self, worldName: str, id: str) -> "BiomeProvider":
        ...


    def isNaggable(self) -> bool:
        ...


    def setNaggable(self, canNag: bool) -> None:
        ...


    def getLogger(self) -> "Logger":
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def getPlugin(clazz: type["T"]) -> "T":
        """
        This method provides fast access to the plugin that has .getProvidingPlugin(Class) provided the given plugin class, which is
        usually the plugin that implemented it.
        
        An exception to this would be if plugin's jar that contained the class
        does not extend the class, where the intended plugin would have
        resided in a different jar / classloader.
        
        Type `<T>`: a class that extends JavaPlugin

        Arguments
        - clazz: the class desired

        Returns
        - the plugin that provides and implements said class

        Raises
        - IllegalArgumentException: if clazz is null
        - IllegalArgumentException: if clazz does not extend JavaPlugin
        - IllegalStateException: if clazz was not provided by a plugin,
            for example, if called with
            `JavaPlugin.getPlugin(JavaPlugin.class)`
        - IllegalStateException: if called from the static initializer for
            given JavaPlugin
        - ClassCastException: if plugin that provided the class does not
            extend the class
        """
        ...


    @staticmethod
    def getProvidingPlugin(clazz: type[Any]) -> "JavaPlugin":
        """
        This method provides fast access to the plugin that has provided the
        given class.

        Arguments
        - clazz: a class belonging to a plugin

        Returns
        - the plugin that provided the class

        Raises
        - IllegalArgumentException: if the class is not provided by a
            JavaPlugin
        - IllegalArgumentException: if class is null
        - IllegalStateException: if called from the static initializer for
            given JavaPlugin
        """
        ...
