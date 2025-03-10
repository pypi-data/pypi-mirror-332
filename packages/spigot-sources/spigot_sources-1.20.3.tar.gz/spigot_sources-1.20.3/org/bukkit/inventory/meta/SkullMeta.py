"""
Python module generated from Java source file org.bukkit.inventory.meta.SkullMeta

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit import OfflinePlayer
from org.bukkit.inventory.meta import *
from org.bukkit.profile import PlayerProfile
from typing import Any, Callable, Iterable, Tuple


class SkullMeta(ItemMeta):
    """
    Represents a skull that can have an owner.
    """

    def getOwner(self) -> str:
        """
        Gets the owner of the skull.

        Returns
        - the owner if the skull

        Deprecated
        - see .getOwningPlayer().
        """
        ...


    def hasOwner(self) -> bool:
        """
        Checks to see if the skull has an owner.

        Returns
        - True if the skull has an owner
        """
        ...


    def setOwner(self, owner: str) -> bool:
        """
        Sets the owner of the skull.

        Arguments
        - owner: the new owner of the skull

        Returns
        - True if the owner was successfully set

        Deprecated
        - see .setOwningPlayer(org.bukkit.OfflinePlayer).
        """
        ...


    def getOwningPlayer(self) -> "OfflinePlayer":
        """
        Gets the owner of the skull.

        Returns
        - the owner if the skull
        """
        ...


    def setOwningPlayer(self, owner: "OfflinePlayer") -> bool:
        """
        Sets the owner of the skull.
        
        Plugins should check that hasOwner() returns True before calling this
        plugin.

        Arguments
        - owner: the new owner of the skull

        Returns
        - True if the owner was successfully set
        """
        ...


    def getOwnerProfile(self) -> "PlayerProfile":
        """
        Gets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.

        Returns
        - the profile of the owning player
        """
        ...


    def setOwnerProfile(self, profile: "PlayerProfile") -> None:
        """
        Sets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.
        
        The profile must contain both a unique id and a skin texture. If either
        of these is missing, the profile must contain a name by which the server
        will then attempt to look up the unique id and skin texture.

        Arguments
        - profile: the profile of the owning player

        Raises
        - IllegalArgumentException: if the profile does not contain the
        necessary information
        """
        ...


    def setNoteBlockSound(self, noteBlockSound: "NamespacedKey") -> None:
        """
        Sets the sound to play if the skull is placed on a note block.
        
        <strong>Note:</strong> This only works for player heads. For other heads,
        see org.bukkit.Instrument.

        Arguments
        - noteBlockSound: the key of the sound to be played, or null
        """
        ...


    def getNoteBlockSound(self) -> "NamespacedKey":
        """
        Gets the sound to play if the skull is placed on a note block.
        
        <strong>Note:</strong> This only works for player heads. For other heads,
        see org.bukkit.Instrument.

        Returns
        - the key of the sound, or null
        """
        ...


    def clone(self) -> "SkullMeta":
        ...
