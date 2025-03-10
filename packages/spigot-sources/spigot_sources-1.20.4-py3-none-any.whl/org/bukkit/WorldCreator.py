"""
Python module generated from Java source file org.bukkit.WorldCreator

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Random
from org.bukkit import *
from org.bukkit.command import CommandSender
from org.bukkit.generator import BiomeProvider
from org.bukkit.generator import ChunkGenerator
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class WorldCreator:
    """
    Represents various types of options that may be used to create a world.
    """

    def __init__(self, name: str):
        """
        Creates an empty WorldCreationOptions for the given world name

        Arguments
        - name: Name of the world that will be created
        """
        ...


    def copy(self, world: "World") -> "WorldCreator":
        """
        Copies the options from the specified world

        Arguments
        - world: World to copy options from

        Returns
        - This object, for chaining
        """
        ...


    def copy(self, creator: "WorldCreator") -> "WorldCreator":
        """
        Copies the options from the specified WorldCreator

        Arguments
        - creator: World creator to copy options from

        Returns
        - This object, for chaining
        """
        ...


    def name(self) -> str:
        """
        Gets the name of the world that is to be loaded or created.

        Returns
        - World name
        """
        ...


    def seed(self) -> int:
        """
        Gets the seed that will be used to create this world

        Returns
        - World seed
        """
        ...


    def seed(self, seed: int) -> "WorldCreator":
        """
        Sets the seed that will be used to create this world

        Arguments
        - seed: World seed

        Returns
        - This object, for chaining
        """
        ...


    def environment(self) -> "World.Environment":
        """
        Gets the environment that will be used to create or load the world

        Returns
        - World environment
        """
        ...


    def environment(self, env: "World.Environment") -> "WorldCreator":
        """
        Sets the environment that will be used to create or load the world

        Arguments
        - env: World environment

        Returns
        - This object, for chaining
        """
        ...


    def type(self) -> "WorldType":
        """
        Gets the type of the world that will be created or loaded

        Returns
        - World type
        """
        ...


    def type(self, type: "WorldType") -> "WorldCreator":
        """
        Sets the type of the world that will be created or loaded

        Arguments
        - type: World type

        Returns
        - This object, for chaining
        """
        ...


    def generator(self) -> "ChunkGenerator":
        """
        Gets the generator that will be used to create or load the world.
        
        This may be null, in which case the "natural" generator for this
        environment will be used.

        Returns
        - Chunk generator
        """
        ...


    def generator(self, generator: "ChunkGenerator") -> "WorldCreator":
        """
        Sets the generator that will be used to create or load the world.
        
        This may be null, in which case the "natural" generator for this
        environment will be used.

        Arguments
        - generator: Chunk generator

        Returns
        - This object, for chaining
        """
        ...


    def generator(self, generator: str) -> "WorldCreator":
        """
        Sets the generator that will be used to create or load the world.
        
        This may be null, in which case the "natural" generator for this
        environment will be used.
        
        If the generator cannot be found for the given name, the natural
        environment generator will be used instead and a warning will be
        printed to the console.

        Arguments
        - generator: Name of the generator to use, in "plugin:id" notation

        Returns
        - This object, for chaining
        """
        ...


    def generator(self, generator: str, output: "CommandSender") -> "WorldCreator":
        """
        Sets the generator that will be used to create or load the world.
        
        This may be null, in which case the "natural" generator for this
        environment will be used.
        
        If the generator cannot be found for the given name, the natural
        environment generator will be used instead and a warning will be
        printed to the specified output

        Arguments
        - generator: Name of the generator to use, in "plugin:id" notation
        - output: CommandSender that will receive any error
            messages

        Returns
        - This object, for chaining
        """
        ...


    def biomeProvider(self) -> "BiomeProvider":
        """
        Gets the biome provider that will be used to create or load the world.
        
        This may be null, in which case the biome provider from the ChunkGenerator
        will be used. If no ChunkGenerator is specific the "natural" biome provider
        for this environment will be used.

        Returns
        - Biome provider
        """
        ...


    def biomeProvider(self, biomeProvider: "BiomeProvider") -> "WorldCreator":
        """
        Sets the biome provider that will be used to create or load the world.
        
        This may be null, in which case the biome provider from the
        ChunkGenerator will be used. If no ChunkGenerator is
        specific the "natural" biome provider for this environment will be used.

        Arguments
        - biomeProvider: Biome provider

        Returns
        - This object, for chaining
        """
        ...


    def biomeProvider(self, biomeProvider: str) -> "WorldCreator":
        """
        Sets the biome provider that will be used to create or load the world.
        
        This may be null, in which case the biome provider from the
        ChunkGenerator will be used. If no ChunkGenerator is
        specific the "natural" biome provider for this environment will be used.
        
        If the biome provider cannot be found for the given name and no
        ChunkGenerator is specific, the natural environment biome
        provider will be used instead and a warning will be printed to the
        specified output

        Arguments
        - biomeProvider: Name of the biome provider to use, in "plugin:id"
        notation

        Returns
        - This object, for chaining
        """
        ...


    def biomeProvider(self, biomeProvider: str, output: "CommandSender") -> "WorldCreator":
        """
        Sets the biome provider that will be used to create or load the world.
        
        This may be null, in which case the biome provider from the
        ChunkGenerator will be used. If no ChunkGenerator is
        specific the "natural" biome provider for this environment will be used.
        
        If the biome provider cannot be found for the given name and no
        ChunkGenerator is specific, the natural environment biome
        provider will be used instead and a warning will be printed to the
        specified output

        Arguments
        - biomeProvider: Name of the biome provider to use, in "plugin:id"
        notation
        - output: CommandSender that will receive any error messages

        Returns
        - This object, for chaining
        """
        ...


    def generatorSettings(self, generatorSettings: str) -> "WorldCreator":
        """
        Sets the generator settings of the world that will be created or loaded.
        
        Currently only WorldType.FLAT uses these settings, and expects
        them to be in JSON format with a valid biome (1.18.2 and
        above) defined. An example valid configuration is as follows:
        `{"layers": [{"block": "stone", "height": 1}, {"block": "grass_block", "height": 1}], "biome":"plains"}`

        Arguments
        - generatorSettings: The settings that should be used by the
        generator

        Returns
        - This object, for chaining

        See
        - <a href="https://minecraft.wiki/w/Custom_dimension">Custom
        dimension</a> (scroll to "When the generator ID type is
        `minecraft:flat`)"
        """
        ...


    def generatorSettings(self) -> str:
        """
        Gets the generator settings of the world that will be created or loaded.

        Returns
        - The settings that should be used by the generator

        See
        - .generatorSettings(java.lang.String)
        """
        ...


    def generateStructures(self, generate: bool) -> "WorldCreator":
        """
        Sets whether or not worlds created or loaded with this creator will
        have structures.

        Arguments
        - generate: Whether to generate structures

        Returns
        - This object, for chaining
        """
        ...


    def generateStructures(self) -> bool:
        """
        Gets whether or not structures will be generated in the world.

        Returns
        - True if structures will be generated
        """
        ...


    def hardcore(self, hardcore: bool) -> "WorldCreator":
        """
        Sets whether the world will be hardcore or not.
        
        In a hardcore world the difficulty will be locked to hard.

        Arguments
        - hardcore: Whether the world will be hardcore

        Returns
        - This object, for chaining
        """
        ...


    def hardcore(self) -> bool:
        """
        Gets whether the world will be hardcore or not.
        
        In a hardcore world the difficulty will be locked to hard.

        Returns
        - hardcore status
        """
        ...


    def keepSpawnInMemory(self, keepSpawnInMemory: bool) -> "WorldCreator":
        """
        Sets whether the spawn chunks will be kept loaded. 
        Setting this to False will also stop the spawn chunks from being generated
        when creating a new world.
        
        Has little performance benefit unless paired with a ChunkGenerator
        that overrides ChunkGenerator.getFixedSpawnLocation(World, Random).

        Arguments
        - keepSpawnInMemory: Whether the spawn chunks will be kept loaded

        Returns
        - This object, for chaining
        """
        ...


    def keepSpawnInMemory(self) -> bool:
        """
        Gets whether or not the spawn chunks will be kept loaded.

        Returns
        - True if the spawn chunks will be kept loaded
        """
        ...


    def createWorld(self) -> "World":
        """
        Creates a world with the specified options.
        
        If the world already exists, it will be loaded from disk and some
        options may be ignored.

        Returns
        - Newly created or loaded world
        """
        ...


    @staticmethod
    def name(name: str) -> "WorldCreator":
        """
        Creates a new WorldCreator for the given world name

        Arguments
        - name: Name of the world to load or create

        Returns
        - Resulting WorldCreator
        """
        ...


    @staticmethod
    def getGeneratorForName(world: str, name: str, output: "CommandSender") -> "ChunkGenerator":
        """
        Attempts to get the ChunkGenerator with the given name.
        
        If the generator is not found, null will be returned and a message will
        be printed to the specified CommandSender explaining why.
        
        The name must be in the "plugin:id" notation, or optionally just
        "plugin", where "plugin" is the safe-name of a plugin and "id" is an
        optional unique identifier for the generator you wish to request from
        the plugin.

        Arguments
        - world: Name of the world this will be used for
        - name: Name of the generator to retrieve
        - output: Where to output if errors are present

        Returns
        - Resulting generator, or null
        """
        ...


    @staticmethod
    def getBiomeProviderForName(world: str, name: str, output: "CommandSender") -> "BiomeProvider":
        """
        Attempts to get the BiomeProvider with the given name.
        
        If the biome provider is not found, null will be returned and a message
        will be printed to the specified CommandSender explaining why.
        
        The name must be in the "plugin:id" notation, or optionally just
        "plugin", where "plugin" is the safe-name of a plugin and "id" is an
        optional unique identifier for the biome provider you wish to request
        from the plugin.

        Arguments
        - world: Name of the world this will be used for
        - name: Name of the biome provider to retrieve
        - output: Where to output if errors are present

        Returns
        - Resulting biome provider, or null
        """
        ...
