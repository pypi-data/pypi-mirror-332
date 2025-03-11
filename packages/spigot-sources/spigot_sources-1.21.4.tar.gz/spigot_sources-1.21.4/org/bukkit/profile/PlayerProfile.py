"""
Python module generated from Java source file org.bukkit.profile.PlayerProfile

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from java.util.concurrent import CompletableFuture
from org.bukkit import Server
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.profile import *
from typing import Any, Callable, Iterable, Tuple


class PlayerProfile(Cloneable, ConfigurationSerializable):
    """
    A player profile.
    
    A player profile always provides a unique id, a non-empty name, or both. Its
    unique id and name are immutable, but other properties (such as its textures)
    can be altered.
    
    New profiles can be created via
    Server.createPlayerProfile(UUID, String).
    """

    def getUniqueId(self) -> "UUID":
        """
        Gets the player's unique id.

        Returns
        - the player's unique id, or `null` if not available
        """
        ...


    def getName(self) -> str:
        """
        Gets the player name.

        Returns
        - the player name, or `null` if not available
        """
        ...


    def getTextures(self) -> "PlayerTextures":
        """
        Gets the PlayerTextures of this profile.

        Returns
        - the textures, not `null`
        """
        ...


    def setTextures(self, textures: "PlayerTextures") -> None:
        """
        Copies the given textures.

        Arguments
        - textures: the textures to copy, or `null` to clear the
        textures
        """
        ...


    def isComplete(self) -> bool:
        """
        Checks whether this profile is complete.
        
        A profile is currently considered complete if it has a name, a unique id,
        and textures.

        Returns
        - `True` if this profile is complete
        """
        ...


    def update(self) -> "CompletableFuture"["PlayerProfile"]:
        """
        Produces an updated player profile based on this profile.
        
        This tries to produce a completed profile by filling in missing
        properties (name, unique id, textures, etc.), and updates existing
        properties (e.g. name, textures, etc.) to their official and up-to-date
        values. This operation does not alter the current profile, but produces a
        new updated PlayerProfile.
        
        If no player exists for the unique id or name of this profile, this
        operation yields a profile that is equal to the current profile, which
        might not be complete.
        
        This is an asynchronous operation: Updating the profile can result in an
        outgoing connection in another thread in order to fetch the latest
        profile properties. The returned CompletableFuture will be
        completed once the updated profile is available. In order to not block
        the server's main thread, you should not wait for the result of the
        returned CompletableFuture on the server's main thread. Instead, if you
        want to do something with the updated player profile on the server's main
        thread once it is available, you could do something like this:
        ```
        profile.update().thenAcceptAsync(updatedProfile -> {
            // Do something with the updated profile:
            // ...
        }, runnable -> Bukkit.getScheduler().runTask(plugin, runnable));
        ```

        Returns
        - a completable future that gets completed with the updated
        PlayerProfile once it is available
        """
        ...


    def clone(self) -> "PlayerProfile":
        ...
