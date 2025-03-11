"""
Python module generated from Java source file org.bukkit.event.entity.CreatureSpawnEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

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
        TRIAL_SPAWNER = 4
        """
        When a creature spawns from a trial spawner
        """
        EGG = 5
        """
        When a creature spawns from an egg
        """
        SPAWNER_EGG = 6
        """
        When a creature spawns from a Spawner Egg
        """
        LIGHTNING = 7
        """
        When a creature spawns because of a lightning strike
        """
        BUILD_SNOWMAN = 8
        """
        When a snowman is spawned by being built
        """
        BUILD_IRONGOLEM = 9
        """
        When an iron golem is spawned by being built
        """
        BUILD_WITHER = 10
        """
        When a wither boss is spawned by being built
        """
        VILLAGE_DEFENSE = 11
        """
        When an iron golem is spawned to defend a village
        """
        VILLAGE_INVASION = 12
        """
        When a zombie is spawned to invade a village
        """
        BREEDING = 13
        """
        When an entity breeds to create a child, this also include Shulker and Allay
        """
        SLIME_SPLIT = 14
        """
        When a slime splits
        """
        REINFORCEMENTS = 15
        """
        When an entity calls for reinforcements
        """
        NETHER_PORTAL = 16
        """
        When a creature is spawned by nether portal
        """
        DISPENSE_EGG = 17
        """
        When a creature is spawned by a dispenser dispensing an egg
        """
        INFECTION = 18
        """
        When a zombie infects a villager
        """
        CURED = 19
        """
        When a villager is cured from infection
        """
        OCELOT_BABY = 20
        """
        When an ocelot has a baby spawned along with them
        """
        SILVERFISH_BLOCK = 21
        """
        When a silverfish spawns from a block
        """
        MOUNT = 22
        """
        When an entity spawns as a mount of another entity (mostly chicken
        jockeys)
        """
        TRAP = 23
        """
        When an entity spawns as a trap for players approaching
        """
        ENDER_PEARL = 24
        """
        When an entity is spawned as a result of ender pearl usage
        """
        SHOULDER_ENTITY = 25
        """
        When an entity is spawned as a result of the entity it is being
        perched on jumping or being damaged
        """
        DROWNED = 26
        """
        When a creature is spawned by another entity drowning
        """
        SHEARED = 27
        """
        When an cow is spawned by shearing a mushroom cow
        """
        EXPLOSION = 28
        """
        When eg an effect cloud is spawned as a result of a creeper exploding
        """
        RAID = 29
        """
        When an entity is spawned as part of a raid
        """
        PATROL = 30
        """
        When an entity is spawned as part of a patrol
        """
        BEEHIVE = 31
        """
        When a bee is released from a beehive/bee nest
        """
        PIGLIN_ZOMBIFIED = 32
        """
        When a piglin is converted to a zombified piglin.
        """
        SPELL = 33
        """
        When an entity is created by a cast spell.
        """
        FROZEN = 34
        """
        When an entity is shaking in Powder Snow and a new entity spawns.
        """
        METAMORPHOSIS = 35
        """
        When a tadpole converts to a frog
        """
        DUPLICATION = 36
        """
        When an Allay duplicate itself
        """
        COMMAND = 37
        """
        When a creature is spawned by the "/summon" command
        """
        ENCHANTMENT = 38
        """
        When a creature is spawned by an enchantment
        """
        POTION_EFFECT = 39
        """
        When a creature is spawned by a potion effect, for example:
        org.bukkit.potion.PotionType.OOZING, org.bukkit.potion.PotionType.INFESTED
        """
        CUSTOM = 40
        """
        When a creature is spawned by plugins
        """
        DEFAULT = 41
        """
        When an entity is missing a SpawnReason
        """
