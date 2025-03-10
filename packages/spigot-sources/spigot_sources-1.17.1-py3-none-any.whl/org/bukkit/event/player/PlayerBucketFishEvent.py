"""
Python module generated from Java source file org.bukkit.event.player.PlayerBucketFishEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import Warning
from org.bukkit.entity import Fish
from org.bukkit.entity import Player
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerBucketFishEvent(PlayerBucketEntityEvent):
    """
    This event is called whenever a player attempts to put a fish in a bucket.

    Deprecated
    - Use the more generic PlayerBucketEntityEvent
    """

    def __init__(self, player: "Player", fish: "Fish", waterBucket: "ItemStack", fishBucket: "ItemStack"):
        ...


    def getEntity(self) -> "Fish":
        """
        Gets the fish involved with this event.

        Returns
        - The fish involved with this event
        """
        ...


    def getWaterBucket(self) -> "ItemStack":
        """
        Gets the bucket used.
        
        This refers to the bucket clicked with, ie Material.WATER_BUCKET.

        Returns
        - The used bucket

        Deprecated
        - Use .getOriginalBucket()
        """
        ...


    def getFishBucket(self) -> "ItemStack":
        """
        Gets the bucket that the fish will be put into.
        
        This refers to the bucket with the fish, ie
        Material.PUFFERFISH_BUCKET.

        Returns
        - The bucket that the fish will be put into

        Deprecated
        - Use .getEntityBucket()
        """
        ...
