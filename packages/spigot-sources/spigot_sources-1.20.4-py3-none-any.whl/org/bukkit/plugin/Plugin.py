"""
Python module generated from Java source file org.bukkit.plugin.Plugin

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import InputStream
from org.bukkit import Server
from org.bukkit.command import TabExecutor
from org.bukkit.configuration.file import FileConfiguration
from org.bukkit.generator import BiomeProvider
from org.bukkit.generator import ChunkGenerator
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class Plugin(TabExecutor):
    """
    Represents a Plugin
    
    The use of PluginBase is recommended for actual Implementation
    """

    def getDataFolder(self) -> "File":
        """
        Returns the folder that the plugin data's files are located in. The
        folder may not yet exist.

        Returns
        - The folder
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
        """
        Gets a FileConfiguration for this plugin, read through
        "config.yml"
        
        If there is a default config.yml embedded in this plugin, it will be
        provided as a default for this Configuration.

        Returns
        - Plugin configuration
        """
        ...


    def getResource(self, filename: str) -> "InputStream":
        """
        Gets an embedded resource in this plugin

        Arguments
        - filename: Filename of the resource

        Returns
        - File if found, otherwise null
        """
        ...


    def saveConfig(self) -> None:
        """
        Saves the FileConfiguration retrievable by .getConfig().
        """
        ...


    def saveDefaultConfig(self) -> None:
        """
        Saves the raw contents of the default config.yml file to the location
        retrievable by .getConfig().
        
        This should fail silently if the config.yml already exists.
        """
        ...


    def saveResource(self, resourcePath: str, replace: bool) -> None:
        """
        Saves the raw contents of any resource embedded with a plugin's .jar
        file assuming it can be found using .getResource(String).
        
        The resource is saved into the plugin's data folder using the same
        hierarchy as the .jar file (subdirectories are preserved).

        Arguments
        - resourcePath: the embedded resource path to look for within the
            plugin's .jar file. (No preceding slash).
        - replace: if True, the embedded resource will overwrite the
            contents of an existing file.

        Raises
        - IllegalArgumentException: if the resource path is null, empty,
            or points to a nonexistent resource.
        """
        ...


    def reloadConfig(self) -> None:
        """
        Discards any data in .getConfig() and reloads from disk.
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


    def onDisable(self) -> None:
        """
        Called when this plugin is disabled
        """
        ...


    def onLoad(self) -> None:
        """
        Called after a plugin is loaded but before it has been enabled.
        
        When multiple plugins are loaded, the onLoad() for all plugins is
        called before any onEnable() is called.
        """
        ...


    def onEnable(self) -> None:
        """
        Called when this plugin is enabled
        """
        ...


    def isNaggable(self) -> bool:
        """
        Simple boolean if we can still nag to the logs about things

        Returns
        - boolean whether we can nag
        """
        ...


    def setNaggable(self, canNag: bool) -> None:
        """
        Set naggable state

        Arguments
        - canNag: is this plugin still naggable?
        """
        ...


    def getDefaultWorldGenerator(self, worldName: str, id: str) -> "ChunkGenerator":
        """
        Gets a ChunkGenerator for use in a default world, as specified
        in the server configuration

        Arguments
        - worldName: Name of the world that this will be applied to
        - id: Unique ID, if any, that was specified to indicate which
            generator was requested

        Returns
        - ChunkGenerator for use in the default world generation
        """
        ...


    def getDefaultBiomeProvider(self, worldName: str, id: str) -> "BiomeProvider":
        """
        Gets a BiomeProvider for use in a default world, as specified
        in the server configuration

        Arguments
        - worldName: Name of the world that this will be applied to
        - id: Unique ID, if any, that was specified to indicate which
            biome provider was requested

        Returns
        - BiomeProvider for use in the default world generation
        """
        ...


    def getLogger(self) -> "Logger":
        """
        Returns the plugin logger associated with this server's logger. The
        returned logger automatically tags all log messages with the plugin's
        name.

        Returns
        - Logger associated with this plugin
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of the plugin.
        
        This should return the bare name of the plugin and should be used for
        comparison.

        Returns
        - name of the plugin
        """
        ...
