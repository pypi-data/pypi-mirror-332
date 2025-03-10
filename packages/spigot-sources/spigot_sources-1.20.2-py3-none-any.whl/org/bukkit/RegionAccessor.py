"""
Python module generated from Java source file org.bukkit.RegionAccessor

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from java.util.function import Consumer
from java.util.function import Predicate
from org.bukkit import *
from org.bukkit.block import Biome
from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Entity
from org.bukkit.entity import EntityType
from org.bukkit.entity import LivingEntity
from typing import Any, Callable, Iterable, Tuple


class RegionAccessor:
    """
    A RegionAccessor gives access to getting, modifying and spawning Biome, BlockState and Entity,
    as well as generating some basic structures.
    """

    def getBiome(self, location: "Location") -> "Biome":
        """
        Gets the Biome at the given Location.

        Arguments
        - location: the location of the biome

        Returns
        - Biome at the given location
        """
        ...


    def getBiome(self, x: int, y: int, z: int) -> "Biome":
        """
        Gets the Biome at the given coordinates.

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block

        Returns
        - Biome at the given coordinates
        """
        ...


    def setBiome(self, location: "Location", biome: "Biome") -> None:
        """
        Sets the Biome at the given Location.

        Arguments
        - location: the location of the biome
        - biome: New Biome type for this block
        """
        ...


    def setBiome(self, x: int, y: int, z: int, biome: "Biome") -> None:
        """
        Sets the Biome for the given block coordinates

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block
        - biome: New Biome type for this block
        """
        ...


    def getBlockState(self, location: "Location") -> "BlockState":
        """
        Gets the BlockState at the given Location.

        Arguments
        - location: The location of the block state

        Returns
        - Block state at the given location
        """
        ...


    def getBlockState(self, x: int, y: int, z: int) -> "BlockState":
        """
        Gets the BlockState at the given coordinates.

        Arguments
        - x: X-coordinate of the block state
        - y: Y-coordinate of the block state
        - z: Z-coordinate of the block state

        Returns
        - Block state at the given coordinates
        """
        ...


    def getBlockData(self, location: "Location") -> "BlockData":
        """
        Gets the BlockData at the given Location.

        Arguments
        - location: The location of the block data

        Returns
        - Block data at the given location
        """
        ...


    def getBlockData(self, x: int, y: int, z: int) -> "BlockData":
        """
        Gets the BlockData at the given coordinates.

        Arguments
        - x: X-coordinate of the block data
        - y: Y-coordinate of the block data
        - z: Z-coordinate of the block data

        Returns
        - Block data at the given coordinates
        """
        ...


    def getType(self, location: "Location") -> "Material":
        """
        Gets the type of the block at the given Location.

        Arguments
        - location: The location of the block

        Returns
        - Material at the given coordinates
        """
        ...


    def getType(self, x: int, y: int, z: int) -> "Material":
        """
        Gets the type of the block at the given coordinates.

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block

        Returns
        - Material at the given coordinates
        """
        ...


    def setBlockData(self, location: "Location", blockData: "BlockData") -> None:
        """
        Sets the BlockData at the given Location.

        Arguments
        - location: The location of the block
        - blockData: The block data to set the block to
        """
        ...


    def setBlockData(self, x: int, y: int, z: int, blockData: "BlockData") -> None:
        """
        Sets the BlockData at the given coordinates.

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block
        - blockData: The block data to set the block to
        """
        ...


    def setType(self, location: "Location", material: "Material") -> None:
        """
        Sets the Material at the given Location.

        Arguments
        - location: The location of the block
        - material: The type to set the block to
        """
        ...


    def setType(self, x: int, y: int, z: int, material: "Material") -> None:
        """
        Sets the Material at the given coordinates.

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block
        - material: The type to set the block to
        """
        ...


    def generateTree(self, location: "Location", random: "Random", type: "TreeType") -> bool:
        """
        Creates a tree at the given Location

        Arguments
        - location: Location to spawn the tree
        - random: Random to use to generated the tree
        - type: Type of the tree to create

        Returns
        - True if the tree was created successfully, otherwise False
        """
        ...


    def generateTree(self, location: "Location", random: "Random", type: "TreeType", stateConsumer: "Consumer"["BlockState"]) -> bool:
        """
        Creates a tree at the given Location
        
        The provided consumer gets called for every block which gets changed
        as a result of the tree generation. When the consumer gets called no
        modifications to the world are done yet. Which means, that calling
        .getBlockState(Location) in the consumer while return the state
        of the block before the generation.
        
        Modifications done to the BlockState in the consumer are respected,
        which means that it is not necessary to call BlockState.update()

        Arguments
        - location: Location to spawn the tree
        - random: Random to use to generated the tree
        - type: Type of the tree to create
        - stateConsumer: The consumer which should get called for every block which gets changed

        Returns
        - True if the tree was created successfully, otherwise False
        """
        ...


    def generateTree(self, location: "Location", random: "Random", type: "TreeType", statePredicate: "Predicate"["BlockState"]) -> bool:
        """
        Creates a tree at the given Location
        
        The provided predicate gets called for every block which gets changed
        as a result of the tree generation. When the predicate gets called no
        modifications to the world are done yet. Which means, that calling
        .getBlockState(Location) in the predicate will return the state
        of the block before the generation.
        
        If the predicate returns `True` the block gets set in the world.
        If it returns `False` the block won't get set in the world.

        Arguments
        - location: Location to spawn the tree
        - random: Random to use to generated the tree
        - type: Type of the tree to create
        - statePredicate: The predicate which should get used to test if a block should be set or not.

        Returns
        - True if the tree was created successfully, otherwise False
        """
        ...


    def spawnEntity(self, location: "Location", type: "EntityType") -> "Entity":
        """
        Creates a entity at the given Location

        Arguments
        - location: The location to spawn the entity
        - type: The entity to spawn

        Returns
        - Resulting Entity of this method
        """
        ...


    def spawnEntity(self, loc: "Location", type: "EntityType", randomizeData: bool) -> "Entity":
        """
        Creates a new entity at the given Location.

        Arguments
        - loc: the location at which the entity will be spawned.
        - type: the entity type that determines the entity to spawn.
        - randomizeData: whether or not the entity's data should be randomised
                             before spawning. By default entities are randomised
                             before spawning in regards to their equipment, age,
                             attributes, etc.
                             An example of this randomization would be the color of
                             a sheep, random enchantments on the equipment of mobs
                             or even a zombie becoming a chicken jockey.
                             If set to False, the entity will not be randomised
                             before spawning, meaning all their data will remain
                             in their default state and not further modifications
                             to the entity will be made.
                             Notably only entities that extend the
                             org.bukkit.entity.Mob interface provide
                             randomisation logic for their spawn.
                             This parameter is hence useless for any other type
                             of entity.

        Returns
        - the spawned entity instance.
        """
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Get a list of all entities in this RegionAccessor

        Returns
        - A List of all Entities currently residing in this world accessor
        """
        ...


    def getLivingEntities(self) -> list["LivingEntity"]:
        """
        Get a list of all living entities in this RegionAccessor

        Returns
        - A List of all LivingEntities currently residing in this world accessor
        """
        ...


    def getEntitiesByClass(self, cls: type["T"]) -> Iterable["T"]:
        """
        Get a collection of all entities in this RegionAccessor matching the given
        class/interface
        
        Type `<T>`: an entity subclass

        Arguments
        - cls: The class representing the type of entity to match

        Returns
        - A List of all Entities currently residing in this world accessor
            that match the given class/interface
        """
        ...


    def getEntitiesByClasses(self, *classes: Tuple[type[Any], ...]) -> Iterable["Entity"]:
        """
        Get a collection of all entities in this RegionAccessor matching any of the
        given classes/interfaces

        Arguments
        - classes: The classes representing the types of entity to match

        Returns
        - A List of all Entities currently residing in this world accessor
            that match one or more of the given classes/interfaces
        """
        ...


    def createEntity(self, location: "Location", clazz: type["T"]) -> "T":
        """
        Creates an entity of a specific class at the given Location but
        does not spawn it in the world.
        
        **Note:** The created entity keeps a reference to the world it was
        created in, care should be taken that the entity does not outlive the
        world instance as this will lead to memory leaks.
        
        Type `<T>`: the class of the Entity to create

        Arguments
        - location: the Location to create the entity at
        - clazz: the class of the Entity to spawn

        Returns
        - an instance of the created Entity

        See
        - Entity.createSnapshot()
        """
        ...


    def spawn(self, location: "Location", clazz: type["T"]) -> "T":
        """
        Spawn an entity of a specific class at the given Location
        
        Type `<T>`: the class of the Entity to spawn

        Arguments
        - location: the Location to spawn the entity at
        - clazz: the class of the Entity to spawn

        Returns
        - an instance of the spawned Entity

        Raises
        - IllegalArgumentException: if either parameter is null or the
            Entity requested cannot be spawned
        """
        ...


    def spawn(self, location: "Location", clazz: type["T"], function: "Consumer"["T"]) -> "T":
        """
        Spawn an entity of a specific class at the given Location, with
        the supplied function run before the entity is added to the world.
        
        Note that when the function is run, the entity will not be actually in
        the world. Any operation involving such as teleporting the entity is undefined
        until after this function returns.
        
        Type `<T>`: the class of the Entity to spawn

        Arguments
        - location: the Location to spawn the entity at
        - clazz: the class of the Entity to spawn
        - function: the function to be run before the entity is spawned.

        Returns
        - an instance of the spawned Entity

        Raises
        - IllegalArgumentException: if either parameter is null or the
            Entity requested cannot be spawned
        """
        ...


    def spawn(self, location: "Location", clazz: type["T"], randomizeData: bool, function: "Consumer"["T"]) -> "T":
        """
        Creates a new entity at the given Location with the supplied
        function run before the entity is added to the world.
        
        Note that when the function is run, the entity will not be actually in
        the world. Any operation involving such as teleporting the entity is undefined
        until after this function returns.
        The passed function however is run after the potential entity's spawn
        randomization and hence already allows access to the values of the mob,
        whether or not those were randomized, such as attributes or the entity
        equipment.
        
        Type `<T>`: the generic type of the entity that is being created.

        Arguments
        - location: the location at which the entity will be spawned.
        - clazz: the class of the Entity that is to be spawned.
        - randomizeData: whether or not the entity's data should be randomised
                             before spawning. By default entities are randomised
                             before spawning in regards to their equipment, age,
                             attributes, etc.
                             An example of this randomization would be the color of
                             a sheep, random enchantments on the equipment of mobs
                             or even a zombie becoming a chicken jockey.
                             If set to False, the entity will not be randomised
                             before spawning, meaning all their data will remain
                             in their default state and not further modifications
                             to the entity will be made.
                             Notably only entities that extend the
                             org.bukkit.entity.Mob interface provide
                             randomisation logic for their spawn.
                             This parameter is hence useless for any other type
                             of entity.
        - function: the function to be run before the entity is spawned.

        Returns
        - the spawned entity instance.

        Raises
        - IllegalArgumentException: if either the world or clazz parameter are null.
        """
        ...


    def getHighestBlockYAt(self, x: int, z: int) -> int:
        """
        Gets the highest non-empty (impassable) coordinate at the given
        coordinates.

        Arguments
        - x: X-coordinate of the blocks
        - z: Z-coordinate of the blocks

        Returns
        - Y-coordinate of the highest non-empty block
        """
        ...


    def getHighestBlockYAt(self, location: "Location") -> int:
        """
        Gets the highest non-empty (impassable) coordinate at the given
        Location.

        Arguments
        - location: Location of the blocks

        Returns
        - Y-coordinate of the highest non-empty block
        """
        ...


    def getHighestBlockYAt(self, x: int, z: int, heightMap: "HeightMap") -> int:
        """
        Gets the highest coordinate corresponding to the HeightMap at the
        given coordinates.

        Arguments
        - x: X-coordinate of the blocks
        - z: Z-coordinate of the blocks
        - heightMap: the heightMap that is used to determine the highest
        point

        Returns
        - Y-coordinate of the highest block corresponding to the
        HeightMap
        """
        ...


    def getHighestBlockYAt(self, location: "Location", heightMap: "HeightMap") -> int:
        """
        Gets the highest coordinate corresponding to the HeightMap at the
        given Location.

        Arguments
        - location: Location of the blocks
        - heightMap: the heightMap that is used to determine the highest
        point

        Returns
        - Y-coordinate of the highest block corresponding to the
        HeightMap
        """
        ...


    def addEntity(self, entity: "T") -> "T":
        """
        Spawns a previously created entity in the world. 
        The provided entity must not have already been spawned in a world.
        
        Type `<T>`: the generic type of the entity that is being added.

        Arguments
        - entity: the entity to add

        Returns
        - the entity now in the world
        """
        ...
