"""
Python module generated from Java source file org.bukkit.event.entity.SpawnerSpawnEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import CreatureSpawner
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class SpawnerSpawnEvent(EntitySpawnEvent):
    """
    Called when an entity is spawned into a world by a spawner.
    
    If a Spawner Spawn event is cancelled, the entity will not spawn.
    """

    def __init__(self, spawnee: "Entity", spawner: "CreatureSpawner"):
        ...


    def getSpawner(self) -> "CreatureSpawner":
        ...
