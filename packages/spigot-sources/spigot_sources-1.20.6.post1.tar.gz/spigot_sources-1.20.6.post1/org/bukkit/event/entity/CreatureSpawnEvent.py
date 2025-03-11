"""
Python module generated from Java source file org.bukkit.event.entity.CreatureSpawnEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Chunk
from org.bukkit.entity import LivingEntity
from org.bukkit.event.entity import *
from org.bukkit.event.world import ChunkLoadEvent
from typing import Any, Callable, Iterable, Tuple


class CreatureSpawnEvent(EntitySpawnEvent):
    """
    Called when a creature is spawned into a world.
    
    If a Creature Spawn event is cancelled, the creature will not spawn.
    """

    def __init__(self, spawnee: "LivingEntity", spawnReason: "SpawnReason"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getSpawnReason(self) -> "SpawnReason":
        """
        Gets the reason for why the creature is being spawned.

        Returns
        - A SpawnReason value detailing the reason for the creature being
            spawned
        """
        ...


    class SpawnReason(Enum):
        """
        An enum to specify the type of spawning
        """

        NATURAL = 0
        """
        When something spawns from natural means
        """
        JOCKEY = 1
        """
        When an entity spawns as a jockey of another entity (mostly spider
        jockeys)
        """
        CHUNK_GEN = 2
        """
        When a creature spawns due to chunk generation

        Deprecated
        - no longer called, chunks are generated with entities
        already existing. Consider using ChunkLoadEvent,
        ChunkLoadEvent.isNewChunk() and Chunk.getEntities()
        for similar effect.
        """
        SPAWNER = 3
        """
        When a creature spawns from a spawner
        """
        EGG = 4
        """
        When a creature spawns from an egg
        """
        SPAWNER_EGG = 5
        """
        When a creature spawns from a Spawner Egg
        """
        LIGHTNING = 6
        """
        When a creature spawns because of a lightning strike
        """
        BUILD_SNOWMAN = 7
        """
        When a snowman is spawned by being built
        """
        BUILD_IRONGOLEM = 8
        """
        When an iron golem is spawned by being built
        """
        BUILD_WITHER = 9
        """
        When a wither boss is spawned by being built
        """
        VILLAGE_DEFENSE = 10
        """
        When an iron golem is spawned to defend a village
        """
        VILLAGE_INVASION = 11
        """
        When a zombie is spawned to invade a village
        """
        BREEDING = 12
        """
        When an entity breeds to create a child, this also include Shulker and Allay
        """
        SLIME_SPLIT = 13
        """
        When a slime splits
        """
        REINFORCEMENTS = 14
        """
        When an entity calls for reinforcements
        """
        NETHER_PORTAL = 15
        """
        When a creature is spawned by nether portal
        """
        DISPENSE_EGG = 16
        """
        When a creature is spawned by a dispenser dispensing an egg
        """
        INFECTION = 17
        """
        When a zombie infects a villager
        """
        CURED = 18
        """
        When a villager is cured from infection
        """
        OCELOT_BABY = 19
        """
        When an ocelot has a baby spawned along with them
        """
        SILVERFISH_BLOCK = 20
        """
        When a silverfish spawns from a block
        """
        MOUNT = 21
        """
        When an entity spawns as a mount of another entity (mostly chicken
        jockeys)
        """
        TRAP = 22
        """
        When an entity spawns as a trap for players approaching
        """
        ENDER_PEARL = 23
        """
        When an entity is spawned as a result of ender pearl usage
        """
        SHOULDER_ENTITY = 24
        """
        When an entity is spawned as a result of the entity it is being
        perched on jumping or being damaged
        """
        DROWNED = 25
        """
        When a creature is spawned by another entity drowning
        """
        SHEARED = 26
        """
        When an cow is spawned by shearing a mushroom cow
        """
        EXPLOSION = 27
        """
        When eg an effect cloud is spawned as a result of a creeper exploding
        """
        RAID = 28
        """
        When an entity is spawned as part of a raid
        """
        PATROL = 29
        """
        When an entity is spawned as part of a patrol
        """
        BEEHIVE = 30
        """
        When a bee is released from a beehive/bee nest
        """
        PIGLIN_ZOMBIFIED = 31
        """
        When a piglin is converted to a zombified piglin.
        """
        SPELL = 32
        """
        When an entity is created by a cast spell.
        """
        FROZEN = 33
        """
        When an entity is shaking in Powder Snow and a new entity spawns.
        """
        METAMORPHOSIS = 34
        """
        When a tadpole converts to a frog
        """
        DUPLICATION = 35
        """
        When an Allay duplicate itself
        """
        COMMAND = 36
        """
        When a creature is spawned by the "/summon" command
        """
        CUSTOM = 37
        """
        When a creature is spawned by plugins
        """
        DEFAULT = 38
        """
        When an entity is missing a SpawnReason
        """
