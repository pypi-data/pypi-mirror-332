"""
Python module generated from Java source file org.bukkit.event.entity.TrialSpawnerSpawnEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import TrialSpawner
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class TrialSpawnerSpawnEvent(EntitySpawnEvent):
    """
    Called when an entity is spawned into a world by a trial spawner.
    
    If a Trial Spawner Spawn event is cancelled, the entity will not spawn.
    """

    def __init__(self, spawnee: "Entity", spawner: "TrialSpawner"):
        ...


    def getTrialSpawner(self) -> "TrialSpawner":
        ...
