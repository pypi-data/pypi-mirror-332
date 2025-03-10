"""
Python module generated from Java source file org.bukkit.entity.Player

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import InetSocketAddress
from java.util import UUID
from org.bukkit import DyeColor
from org.bukkit import Effect
from org.bukkit import GameMode
from org.bukkit import Instrument
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import Note
from org.bukkit import OfflinePlayer
from org.bukkit import Particle
from org.bukkit import Server
from org.bukkit import Sound
from org.bukkit import SoundCategory
from org.bukkit import WeatherType
from org.bukkit import WorldBorder
from org.bukkit.advancement import Advancement
from org.bukkit.advancement import AdvancementProgress
from org.bukkit.block import Block
from org.bukkit.block import Sign
from org.bukkit.block.data import BlockData
from org.bukkit.conversations import Conversable
from org.bukkit.entity import *
from org.bukkit.event.block import BlockBreakEvent
from org.bukkit.event.block import BlockDropItemEvent
from org.bukkit.event.player import PlayerResourcePackStatusEvent
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.map import MapView
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import PluginMessageRecipient
from org.bukkit.scoreboard import Scoreboard
from typing import Any, Callable, Iterable, Tuple


class Player(HumanEntity, Conversable, OfflinePlayer, PluginMessageRecipient):
    """
    Represents a player, connected or not
    """

    def getDisplayName(self) -> str:
        """
        Gets the "friendly" name to display of this player. This may include
        color.
        
        Note that this name will not be displayed in game, only in chat and
        places defined by plugins.

        Returns
        - the friendly name
        """
        ...


    def setDisplayName(self, name: str) -> None:
        """
        Sets the "friendly" name to display of this player. This may include
        color.
        
        Note that this name will not be displayed in game, only in chat and
        places defined by plugins.

        Arguments
        - name: The new display name.
        """
        ...


    def getPlayerListName(self) -> str:
        """
        Gets the name that is shown on the player list.

        Returns
        - the player list name
        """
        ...


    def setPlayerListName(self, name: str) -> None:
        """
        Sets the name that is shown on the in-game player list.
        
        If the value is null, the name will be identical to .getName().

        Arguments
        - name: new player list name
        """
        ...


    def getPlayerListHeader(self) -> str:
        """
        Gets the currently displayed player list header for this player.

        Returns
        - player list header or null
        """
        ...


    def getPlayerListFooter(self) -> str:
        """
        Gets the currently displayed player list footer for this player.

        Returns
        - player list header or null
        """
        ...


    def setPlayerListHeader(self, header: str) -> None:
        """
        Sets the currently displayed player list header for this player.

        Arguments
        - header: player list header, null for empty
        """
        ...


    def setPlayerListFooter(self, footer: str) -> None:
        """
        Sets the currently displayed player list footer for this player.

        Arguments
        - footer: player list footer, null for empty
        """
        ...


    def setPlayerListHeaderFooter(self, header: str, footer: str) -> None:
        """
        Sets the currently displayed player list header and footer for this
        player.

        Arguments
        - header: player list header, null for empty
        - footer: player list footer, null for empty
        """
        ...


    def setCompassTarget(self, loc: "Location") -> None:
        """
        Set the target of the player's compass.

        Arguments
        - loc: Location to point to
        """
        ...


    def getCompassTarget(self) -> "Location":
        """
        Get the previously set compass target.

        Returns
        - location of the target
        """
        ...


    def getAddress(self) -> "InetSocketAddress":
        """
        Gets the socket address of this player

        Returns
        - the player's address
        """
        ...


    def sendRawMessage(self, message: str) -> None:
        """
        Sends this sender a message raw

        Arguments
        - message: Message to be displayed
        """
        ...


    def kickPlayer(self, message: str) -> None:
        """
        Kicks player with custom kick message.

        Arguments
        - message: kick message
        """
        ...


    def chat(self, msg: str) -> None:
        """
        Says a message (or runs a command).

        Arguments
        - msg: message to print
        """
        ...


    def performCommand(self, command: str) -> bool:
        """
        Makes the player perform the given command

        Arguments
        - command: Command to perform

        Returns
        - True if the command was successful, otherwise False
        """
        ...


    def isOnGround(self) -> bool:
        """
        Returns True if the entity is supported by a block.
        
        This value is a state updated by the client after each movement.

        Returns
        - True if entity is on ground.

        Deprecated
        - This value is controlled only by the client and is therefore
        unreliable and vulnerable to spoofing and/or desync depending on the
        context/time which it is accessed
        """
        ...


    def isSneaking(self) -> bool:
        """
        Returns if the player is in sneak mode

        Returns
        - True if player is in sneak mode
        """
        ...


    def setSneaking(self, sneak: bool) -> None:
        """
        Sets the sneak mode the player

        Arguments
        - sneak: True if player should appear sneaking
        """
        ...


    def isSprinting(self) -> bool:
        """
        Gets whether the player is sprinting or not.

        Returns
        - True if player is sprinting.
        """
        ...


    def setSprinting(self, sprinting: bool) -> None:
        """
        Sets whether the player is sprinting or not.

        Arguments
        - sprinting: True if the player should be sprinting
        """
        ...


    def saveData(self) -> None:
        """
        Saves the players current location, health, inventory, motion, and
        other information into the username.dat file, in the world/player
        folder
        """
        ...


    def loadData(self) -> None:
        """
        Loads the players current location, health, inventory, motion, and
        other information from the username.dat file, in the world/player
        folder.
        
        Note: This will overwrite the players current inventory, health,
        motion, etc, with the state from the saved dat file.
        """
        ...


    def setSleepingIgnored(self, isSleeping: bool) -> None:
        """
        Sets whether the player is ignored as not sleeping. If everyone is
        either sleeping or has this flag set, then time will advance to the
        next day. If everyone has this flag set but no one is actually in bed,
        then nothing will happen.

        Arguments
        - isSleeping: Whether to ignore.
        """
        ...


    def isSleepingIgnored(self) -> bool:
        """
        Returns whether the player is sleeping ignored.

        Returns
        - Whether player is ignoring sleep.
        """
        ...


    def getBedSpawnLocation(self) -> "Location":
        """
        Gets the Location where the player will spawn at their bed, null if
        they have not slept in one or their current bed spawn is invalid.

        Returns
        - Bed Spawn Location if bed exists, otherwise null.
        """
        ...


    def setBedSpawnLocation(self, location: "Location") -> None:
        """
        Sets the Location where the player will spawn at their bed.

        Arguments
        - location: where to set the respawn location
        """
        ...


    def setBedSpawnLocation(self, location: "Location", force: bool) -> None:
        """
        Sets the Location where the player will spawn at their bed.

        Arguments
        - location: where to set the respawn location
        - force: whether to forcefully set the respawn location even if a
            valid bed is not present
        """
        ...


    def playNote(self, loc: "Location", instrument: int, note: int) -> None:
        """
        Play a note for a player at a location. This requires a note block
        at the particular location (as far as the client is concerned). This
        will not work without a note block. This will not work with cake.

        Arguments
        - loc: The location of a note block.
        - instrument: The instrument ID.
        - note: The note ID.

        Deprecated
        - Magic value
        """
        ...


    def playNote(self, loc: "Location", instrument: "Instrument", note: "Note") -> None:
        """
        Play a note for a player at a location. This requires a note block
        at the particular location (as far as the client is concerned). This
        will not work without a note block. This will not work with cake.

        Arguments
        - loc: The location of a note block
        - instrument: The instrument
        - note: The note
        """
        ...


    def playSound(self, location: "Location", sound: "Sound", volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location.
        
        This function will fail silently if Location or Sound are null.

        Arguments
        - location: The location to play the sound
        - sound: The sound to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: str, volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location.
        
        This function will fail silently if Location or Sound are null. No
        sound will be heard by the player if their client does not have the
        respective sound for the value passed.

        Arguments
        - location: the location to play the sound
        - sound: the internal sound name to play
        - volume: the volume of the sound
        - pitch: the pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: "Sound", category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location.
        
        This function will fail silently if Location or Sound are null.

        Arguments
        - location: The location to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: str, category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location.
        
        This function will fail silently if Location or Sound are null. No sound
        will be heard by the player if their client does not have the respective
        sound for the value passed.

        Arguments
        - location: the location to play the sound
        - sound: the internal sound name to play
        - category: The category of the sound
        - volume: the volume of the sound
        - pitch: the pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: "Sound", volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location of the entity.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: "Sound", category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a sound for a player at the location of the entity.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def stopSound(self, sound: "Sound") -> None:
        """
        Stop the specified sound from playing.

        Arguments
        - sound: the sound to stop
        """
        ...


    def stopSound(self, sound: str) -> None:
        """
        Stop the specified sound from playing.

        Arguments
        - sound: the sound to stop
        """
        ...


    def stopSound(self, sound: "Sound", category: "SoundCategory") -> None:
        """
        Stop the specified sound from playing.

        Arguments
        - sound: the sound to stop
        - category: the category of the sound
        """
        ...


    def stopSound(self, sound: str, category: "SoundCategory") -> None:
        """
        Stop the specified sound from playing.

        Arguments
        - sound: the sound to stop
        - category: the category of the sound
        """
        ...


    def stopAllSounds(self) -> None:
        """
        Stop all sounds from playing.
        """
        ...


    def playEffect(self, loc: "Location", effect: "Effect", data: int) -> None:
        """
        Plays an effect to just this player.

        Arguments
        - loc: the location to play the effect at
        - effect: the Effect
        - data: a data bit needed for some effects

        Deprecated
        - Magic value
        """
        ...


    def playEffect(self, loc: "Location", effect: "Effect", data: "T") -> None:
        """
        Plays an effect to just this player.
        
        Type `<T>`: the data based based on the type of the effect

        Arguments
        - loc: the location to play the effect at
        - effect: the Effect
        - data: a data bit needed for some effects
        """
        ...


    def breakBlock(self, block: "Block") -> bool:
        """
        Force this player to break a Block using the item in their main hand.
        
        This method will respect enchantments, handle item durability (if
        applicable) and drop experience and the correct items according to the
        tool/item in the player's hand.
        
        Note that this method will call a BlockBreakEvent, meaning that
        this method may not be successful in breaking the block if the event was
        cancelled by a third party plugin. Care should be taken if running this
        method in a BlockBreakEvent listener as recursion may be possible if it
        is invoked on the same Block being broken in the event.
        
        Additionally, a BlockDropItemEvent is called for the items
        dropped by this method (if successful).
        
        The block must be in the same world as the player.

        Arguments
        - block: the block to break

        Returns
        - True if the block was broken, False if the break failed
        """
        ...


    def sendBlockChange(self, loc: "Location", material: "Material", data: int) -> None:
        """
        Send a block change. This fakes a block change packet for a user at a
        certain location. This will not actually change the world in any way.

        Arguments
        - loc: The location of the changed block
        - material: The new block
        - data: The block data

        Deprecated
        - Magic value
        """
        ...


    def sendBlockChange(self, loc: "Location", block: "BlockData") -> None:
        """
        Send a block change. This fakes a block change packet for a user at a
        certain location. This will not actually change the world in any way.

        Arguments
        - loc: The location of the changed block
        - block: The new block
        """
        ...


    def sendBlockDamage(self, loc: "Location", progress: float) -> None:
        """
        Send block damage. This fakes block break progress for a user at a
        certain location. This will not actually change the block's break
        progress in any way.

        Arguments
        - loc: the location of the damaged block
        - progress: the progress from 0.0 - 1.0 where 0 is no damage and
        1.0 is the most damaged
        """
        ...


    def sendEquipmentChange(self, entity: "LivingEntity", slot: "EquipmentSlot", item: "ItemStack") -> None:
        """
        Send the equipment change of an entity. This fakes the equipment change
        of an entity for a user. This will not actually change the inventory of
        the specified entity in any way.

        Arguments
        - entity: The entity that the player will see the change for
        - slot: The slot of the spoofed equipment change
        - item: The ItemStack to display for the player
        """
        ...


    def sendSignChange(self, loc: "Location", lines: list[str]) -> None:
        """
        Send a sign change. This fakes a sign change packet for a user at
        a certain location. This will not actually change the world in any way.
        This method will use a sign at the location's block or a faked sign
        sent via
        .sendBlockChange(org.bukkit.Location, org.bukkit.Material, byte).
        
        If the client does not have a sign at the given location it will
        display an error message to the user.

        Arguments
        - loc: the location of the sign
        - lines: the new text on the sign or null to clear it

        Raises
        - IllegalArgumentException: if location is null
        - IllegalArgumentException: if lines is non-null and has a length less than 4
        """
        ...


    def sendSignChange(self, loc: "Location", lines: list[str], dyeColor: "DyeColor") -> None:
        """
        Send a sign change. This fakes a sign change packet for a user at
        a certain location. This will not actually change the world in any way.
        This method will use a sign at the location's block or a faked sign
        sent via
        .sendBlockChange(org.bukkit.Location, org.bukkit.Material, byte).
        
        If the client does not have a sign at the given location it will
        display an error message to the user.

        Arguments
        - loc: the location of the sign
        - lines: the new text on the sign or null to clear it
        - dyeColor: the color of the sign

        Raises
        - IllegalArgumentException: if location is null
        - IllegalArgumentException: if dyeColor is null
        - IllegalArgumentException: if lines is non-null and has a length less than 4
        """
        ...


    def sendSignChange(self, loc: "Location", lines: list[str], dyeColor: "DyeColor", hasGlowingText: bool) -> None:
        """
        Send a sign change. This fakes a sign change packet for a user at
        a certain location. This will not actually change the world in any way.
        This method will use a sign at the location's block or a faked sign
        sent via
        .sendBlockChange(org.bukkit.Location, org.bukkit.Material, byte).
        
        If the client does not have a sign at the given location it will
        display an error message to the user.

        Arguments
        - loc: the location of the sign
        - lines: the new text on the sign or null to clear it
        - dyeColor: the color of the sign
        - hasGlowingText: if the sign's text should be glowing

        Raises
        - IllegalArgumentException: if location is null
        - IllegalArgumentException: if dyeColor is null
        - IllegalArgumentException: if lines is non-null and has a length less than 4
        """
        ...


    def sendMap(self, map: "MapView") -> None:
        """
        Render a map and send it to the player in its entirety. This may be
        used when streaming the map in the normal manner is not desirable.

        Arguments
        - map: The map to be sent
        """
        ...


    def updateInventory(self) -> None:
        ...


    def getPreviousGameMode(self) -> "GameMode":
        """
        Gets this player's previous GameMode

        Returns
        - Previous game mode or null
        """
        ...


    def setPlayerTime(self, time: int, relative: bool) -> None:
        """
        Sets the current time on the player's client. When relative is True the
        player's time will be kept synchronized to its world time with the
        specified offset.
        
        When using non relative time the player's time will stay fixed at the
        specified time parameter. It's up to the caller to continue updating
        the player's time. To restore player time to normal use
        resetPlayerTime().

        Arguments
        - time: The current player's perceived time or the player's time
            offset from the server time.
        - relative: When True the player time is kept relative to its world
            time.
        """
        ...


    def getPlayerTime(self) -> int:
        """
        Returns the player's current timestamp.

        Returns
        - The player's time
        """
        ...


    def getPlayerTimeOffset(self) -> int:
        """
        Returns the player's current time offset relative to server time, or
        the current player's fixed time if the player's time is absolute.

        Returns
        - The player's time
        """
        ...


    def isPlayerTimeRelative(self) -> bool:
        """
        Returns True if the player's time is relative to the server time,
        otherwise the player's time is absolute and will not change its current
        time unless done so with setPlayerTime().

        Returns
        - True if the player's time is relative to the server time.
        """
        ...


    def resetPlayerTime(self) -> None:
        """
        Restores the normal condition where the player's time is synchronized
        with the server time.
        
        Equivalent to calling setPlayerTime(0, True).
        """
        ...


    def setPlayerWeather(self, type: "WeatherType") -> None:
        """
        Sets the type of weather the player will see.  When used, the weather
        status of the player is locked until .resetPlayerWeather() is
        used.

        Arguments
        - type: The WeatherType enum type the player should experience
        """
        ...


    def getPlayerWeather(self) -> "WeatherType":
        """
        Returns the type of weather the player is currently experiencing.

        Returns
        - The WeatherType that the player is currently experiencing or
            null if player is seeing server weather.
        """
        ...


    def resetPlayerWeather(self) -> None:
        """
        Restores the normal condition where the player's weather is controlled
        by server conditions.
        """
        ...


    def giveExp(self, amount: int) -> None:
        """
        Gives the player the amount of experience specified.

        Arguments
        - amount: Exp amount to give
        """
        ...


    def giveExpLevels(self, amount: int) -> None:
        """
        Gives the player the amount of experience levels specified. Levels can
        be taken by specifying a negative amount.

        Arguments
        - amount: amount of experience levels to give or take
        """
        ...


    def getExp(self) -> float:
        """
        Gets the players current experience points towards the next level.
        
        This is a percentage value. 0 is "no progress" and 1 is "next level".

        Returns
        - Current experience points
        """
        ...


    def setExp(self, exp: float) -> None:
        """
        Sets the players current experience points towards the next level
        
        This is a percentage value. 0 is "no progress" and 1 is "next level".

        Arguments
        - exp: New experience points
        """
        ...


    def getLevel(self) -> int:
        """
        Gets the players current experience level

        Returns
        - Current experience level
        """
        ...


    def setLevel(self, level: int) -> None:
        """
        Sets the players current experience level

        Arguments
        - level: New experience level
        """
        ...


    def getTotalExperience(self) -> int:
        """
        Gets the players total experience points.
        
        This refers to the total amount of experience the player has collected
        over time and is not currently displayed to the client.

        Returns
        - Current total experience points
        """
        ...


    def setTotalExperience(self, exp: int) -> None:
        """
        Sets the players current experience points.
        
        This refers to the total amount of experience the player has collected
        over time and is not currently displayed to the client.

        Arguments
        - exp: New total experience points
        """
        ...


    def sendExperienceChange(self, progress: float) -> None:
        """
        Send an experience change.
        
        This fakes an experience change packet for a user. This will not actually
        change the experience points in any way.

        Arguments
        - progress: Experience progress percentage (between 0.0 and 1.0)

        See
        - .setExp(float)
        """
        ...


    def sendExperienceChange(self, progress: float, level: int) -> None:
        """
        Send an experience change.
        
        This fakes an experience change packet for a user. This will not actually
        change the experience points in any way.

        Arguments
        - progress: New experience progress percentage (between 0.0 and 1.0)
        - level: New experience level

        See
        - .setLevel(int)
        """
        ...


    def getAllowFlight(self) -> bool:
        """
        Determines if the Player is allowed to fly via jump key double-tap like
        in creative mode.

        Returns
        - True if the player is allowed to fly.
        """
        ...


    def setAllowFlight(self, flight: bool) -> None:
        """
        Sets if the Player is allowed to fly via jump key double-tap like in
        creative mode.

        Arguments
        - flight: If flight should be allowed.
        """
        ...


    def hidePlayer(self, player: "Player") -> None:
        """
        Hides a player from this player

        Arguments
        - player: Player to hide

        Deprecated
        - see .hidePlayer(Plugin, Player)
        """
        ...


    def hidePlayer(self, plugin: "Plugin", player: "Player") -> None:
        """
        Hides a player from this player

        Arguments
        - plugin: Plugin that wants to hide the player
        - player: Player to hide
        """
        ...


    def showPlayer(self, player: "Player") -> None:
        """
        Allows this player to see a player that was previously hidden

        Arguments
        - player: Player to show

        Deprecated
        - see .showPlayer(Plugin, Player)
        """
        ...


    def showPlayer(self, plugin: "Plugin", player: "Player") -> None:
        """
        Allows this player to see a player that was previously hidden. If
        another another plugin had hidden the player too, then the player will
        remain hidden until the other plugin calls this method too.

        Arguments
        - plugin: Plugin that wants to show the player
        - player: Player to show
        """
        ...


    def canSee(self, player: "Player") -> bool:
        """
        Checks to see if a player has been hidden from this player

        Arguments
        - player: Player to check

        Returns
        - True if the provided player is not being hidden from this
            player
        """
        ...


    def hideEntity(self, plugin: "Plugin", entity: "Entity") -> None:
        """
        Visually hides an entity from this player.

        Arguments
        - plugin: Plugin that wants to hide the entity
        - entity: Entity to hide

        Deprecated
        - draft API
        """
        ...


    def showEntity(self, plugin: "Plugin", entity: "Entity") -> None:
        """
        Allows this player to see an entity that was previously hidden. If
        another another plugin had hidden the entity too, then the entity will
        remain hidden until the other plugin calls this method too.

        Arguments
        - plugin: Plugin that wants to show the entity
        - entity: Entity to show

        Deprecated
        - draft API
        """
        ...


    def canSee(self, entity: "Entity") -> bool:
        """
        Checks to see if an entity has been visually hidden from this player.

        Arguments
        - entity: Entity to check

        Returns
        - True if the provided entity is not being hidden from this
            player

        Deprecated
        - draft API
        """
        ...


    def isFlying(self) -> bool:
        """
        Checks to see if this player is currently flying or not.

        Returns
        - True if the player is flying, else False.
        """
        ...


    def setFlying(self, value: bool) -> None:
        """
        Makes this player start or stop flying.

        Arguments
        - value: True to fly.
        """
        ...


    def setFlySpeed(self, value: float) -> None:
        """
        Sets the speed at which a client will fly. Negative values indicate
        reverse directions.

        Arguments
        - value: The new speed, from -1 to 1.

        Raises
        - IllegalArgumentException: If new speed is less than -1 or
            greater than 1
        """
        ...


    def setWalkSpeed(self, value: float) -> None:
        """
        Sets the speed at which a client will walk. Negative values indicate
        reverse directions.

        Arguments
        - value: The new speed, from -1 to 1.

        Raises
        - IllegalArgumentException: If new speed is less than -1 or
            greater than 1
        """
        ...


    def getFlySpeed(self) -> float:
        """
        Gets the current allowed speed that a client can fly.

        Returns
        - The current allowed speed, from -1 to 1
        """
        ...


    def getWalkSpeed(self) -> float:
        """
        Gets the current allowed speed that a client can walk.

        Returns
        - The current allowed speed, from -1 to 1
        """
        ...


    def setTexturePack(self, url: str) -> None:
        """
        Request that the player's client download and switch texture packs.
        
        The player's client will download the new texture pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached the same
        texture pack in the past, it will perform a file size check against
        the response content to determine if the texture pack has changed and
        needs to be downloaded again. When this request is sent for the very
        first time from a given server, the client will first display a
        confirmation GUI to the player before proceeding with the download.
        
        Notes:
        
        - Players can disable server textures on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting texture packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is send with "null" as the hash. This might result
            in newer versions not loading the pack correctly.

        Arguments
        - url: The URL from which the client will download the texture
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long.

        Deprecated
        - Minecraft no longer uses textures packs. Instead you
            should use .setResourcePack(String).
        """
        ...


    def setResourcePack(self, url: str) -> None:
        """
        Request that the player's client download and switch resource packs.
        
        The player's client will download the new resource pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached the same
        resource pack in the past, it will perform a file size check against
        the response content to determine if the resource pack has changed and
        needs to be downloaded again. When this request is sent for the very
        first time from a given server, the client will first display a
        confirmation GUI to the player before proceeding with the download.
        
        Notes:
        
        - Players can disable server resources on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting resource packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is send with empty string as the hash. This might result
            in newer versions not loading the pack correctly.

        Arguments
        - url: The URL from which the client will download the resource
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long. The
            length restriction is an implementation specific arbitrary value.
        """
        ...


    def setResourcePack(self, url: str, hash: list[int]) -> None:
        """
        Request that the player's client download and switch resource packs.
        
        The player's client will download the new resource pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached a
        resource pack with the same hash in the past it will not download but
        directly apply the cached pack. If the hash is null and the client has
        downloaded and cached the same resource pack in the past, it will
        perform a file size check against the response content to determine if
        the resource pack has changed and needs to be downloaded again. When
        this request is sent for the very first time from a given server, the
        client will first display a confirmation GUI to the player before
        proceeding with the download.
        
        Notes:
        
        - Players can disable server resources on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting resource packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is sent with empty string as the hash when the hash is
            not provided. This might result in newer versions not loading the
            pack correctly.

        Arguments
        - url: The URL from which the client will download the resource
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.
        - hash: The sha1 hash sum of the resource pack file which is used
            to apply a cached version of the pack directly without downloading
            if it is available. Hast to be 20 bytes long!

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long. The
            length restriction is an implementation specific arbitrary value.
        - IllegalArgumentException: Thrown if the hash is not 20 bytes
            long.
        """
        ...


    def setResourcePack(self, url: str, hash: list[int], prompt: str) -> None:
        """
        Request that the player's client download and switch resource packs.
        
        The player's client will download the new resource pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached a
        resource pack with the same hash in the past it will not download but
        directly apply the cached pack. If the hash is null and the client has
        downloaded and cached the same resource pack in the past, it will
        perform a file size check against the response content to determine if
        the resource pack has changed and needs to be downloaded again. When
        this request is sent for the very first time from a given server, the
        client will first display a confirmation GUI to the player before
        proceeding with the download.
        
        Notes:
        
        - Players can disable server resources on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting resource packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is sent with empty string as the hash when the hash is
            not provided. This might result in newer versions not loading the
            pack correctly.

        Arguments
        - url: The URL from which the client will download the resource
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.
        - hash: The sha1 hash sum of the resource pack file which is used
            to apply a cached version of the pack directly without downloading
            if it is available. Hast to be 20 bytes long!
        - prompt: The optional custom prompt message to be shown to client.

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long. The
            length restriction is an implementation specific arbitrary value.
        - IllegalArgumentException: Thrown if the hash is not 20 bytes
            long.
        """
        ...


    def setResourcePack(self, url: str, hash: list[int], force: bool) -> None:
        """
        Request that the player's client download and switch resource packs.
        
        The player's client will download the new resource pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached a
        resource pack with the same hash in the past it will not download but
        directly apply the cached pack. If the hash is null and the client has
        downloaded and cached the same resource pack in the past, it will
        perform a file size check against the response content to determine if
        the resource pack has changed and needs to be downloaded again. When
        this request is sent for the very first time from a given server, the
        client will first display a confirmation GUI to the player before
        proceeding with the download.
        
        Notes:
        
        - Players can disable server resources on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting resource packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is sent with empty string as the hash when the hash is
            not provided. This might result in newer versions not loading the
            pack correctly.

        Arguments
        - url: The URL from which the client will download the resource
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.
        - hash: The sha1 hash sum of the resource pack file which is used
            to apply a cached version of the pack directly without downloading
            if it is available. Hast to be 20 bytes long!
        - force: If True, the client will be disconnected from the server
            when it declines to use the resource pack.

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long. The
            length restriction is an implementation specific arbitrary value.
        - IllegalArgumentException: Thrown if the hash is not 20 bytes
            long.
        """
        ...


    def setResourcePack(self, url: str, hash: list[int], prompt: str, force: bool) -> None:
        """
        Request that the player's client download and switch resource packs.
        
        The player's client will download the new resource pack asynchronously
        in the background, and will automatically switch to it once the
        download is complete. If the client has downloaded and cached a
        resource pack with the same hash in the past it will not download but
        directly apply the cached pack. If the hash is null and the client has
        downloaded and cached the same resource pack in the past, it will
        perform a file size check against the response content to determine if
        the resource pack has changed and needs to be downloaded again. When
        this request is sent for the very first time from a given server, the
        client will first display a confirmation GUI to the player before
        proceeding with the download.
        
        Notes:
        
        - Players can disable server resources on their client, in which
            case this method will have no affect on them. Use the
            PlayerResourcePackStatusEvent to figure out whether or not
            the player loaded the pack!
        - There is no concept of resetting resource packs back to default
            within Minecraft, so players will have to relog to do so or you
            have to send an empty pack.
        - The request is sent with empty string as the hash when the hash is
            not provided. This might result in newer versions not loading the
            pack correctly.

        Arguments
        - url: The URL from which the client will download the resource
            pack. The string must contain only US-ASCII characters and should
            be encoded as per RFC 1738.
        - hash: The sha1 hash sum of the resource pack file which is used
            to apply a cached version of the pack directly without downloading
            if it is available. Hast to be 20 bytes long!
        - prompt: The optional custom prompt message to be shown to client.
        - force: If True, the client will be disconnected from the server
            when it declines to use the resource pack.

        Raises
        - IllegalArgumentException: Thrown if the URL is null.
        - IllegalArgumentException: Thrown if the URL is too long. The
            length restriction is an implementation specific arbitrary value.
        - IllegalArgumentException: Thrown if the hash is not 20 bytes
            long.
        """
        ...


    def getScoreboard(self) -> "Scoreboard":
        """
        Gets the Scoreboard displayed to this player

        Returns
        - The current scoreboard seen by this player
        """
        ...


    def setScoreboard(self, scoreboard: "Scoreboard") -> None:
        """
        Sets the player's visible Scoreboard.

        Arguments
        - scoreboard: New Scoreboard for the player

        Raises
        - IllegalArgumentException: if scoreboard is null
        - IllegalArgumentException: if scoreboard was not created by the
            org.bukkit.scoreboard.ScoreboardManager scoreboard manager
        - IllegalStateException: if this is a player that is not logged
            yet or has logged out
        """
        ...


    def getWorldBorder(self) -> "WorldBorder":
        """
        Gets the WorldBorder visible to this Player, or null if viewing
        the world's world border.

        Returns
        - the player's world border
        """
        ...


    def setWorldBorder(self, border: "WorldBorder") -> None:
        """
        Sets the WorldBorder visible to this Player.

        Arguments
        - border: the border to set, or null to set to the world border of
        the player's current world

        Raises
        - UnsupportedOperationException: if setting the border to that of
        a world in which the player is not currently present.

        See
        - Server.createWorldBorder()
        """
        ...


    def isHealthScaled(self) -> bool:
        """
        Gets if the client is displayed a 'scaled' health, that is, health on a
        scale from 0-.getHealthScale().

        Returns
        - if client health display is scaled

        See
        - Player.setHealthScaled(boolean)
        """
        ...


    def setHealthScaled(self, scale: bool) -> None:
        """
        Sets if the client is displayed a 'scaled' health, that is, health on a
        scale from 0-.getHealthScale().
        
        Displayed health follows a simple formula `displayedHealth =
        getHealth() / getMaxHealth() * getHealthScale()`.

        Arguments
        - scale: if the client health display is scaled
        """
        ...


    def setHealthScale(self, scale: float) -> None:
        """
        Sets the number to scale health to for the client; this will also
        .setHealthScaled(boolean) setHealthScaled(True).
        
        Displayed health follows a simple formula `displayedHealth =
        getHealth() / getMaxHealth() * getHealthScale()`.

        Arguments
        - scale: the number to scale health to

        Raises
        - IllegalArgumentException: if scale is &lt;0
        - IllegalArgumentException: if scale is Double.NaN
        - IllegalArgumentException: if scale is too high
        """
        ...


    def getHealthScale(self) -> float:
        """
        Gets the number that health is scaled to for the client.

        Returns
        - the number that health would be scaled to for the client if
            HealthScaling is set to True

        See
        - Player.setHealthScaled(boolean)
        """
        ...


    def getSpectatorTarget(self) -> "Entity":
        """
        Gets the entity which is followed by the camera when in
        GameMode.SPECTATOR.

        Returns
        - the followed entity, or null if not in spectator mode or not
        following a specific entity.
        """
        ...


    def setSpectatorTarget(self, entity: "Entity") -> None:
        """
        Sets the entity which is followed by the camera when in
        GameMode.SPECTATOR.

        Arguments
        - entity: the entity to follow or null to reset

        Raises
        - IllegalStateException: if the player is not in
        GameMode.SPECTATOR
        """
        ...


    def sendTitle(self, title: str, subtitle: str) -> None:
        """
        Sends a title and a subtitle message to the player. If either of these
        values are null, they will not be sent and the display will remain
        unchanged. If they are empty strings, the display will be updated as
        such. If the strings contain a new line, only the first line will be
        sent. The titles will be displayed with the client's default timings.

        Arguments
        - title: Title text
        - subtitle: Subtitle text

        Deprecated
        - API behavior subject to change
        """
        ...


    def sendTitle(self, title: str, subtitle: str, fadeIn: int, stay: int, fadeOut: int) -> None:
        """
        Sends a title and a subtitle message to the player. If either of these
        values are null, they will not be sent and the display will remain
        unchanged. If they are empty strings, the display will be updated as
        such. If the strings contain a new line, only the first line will be
        sent. All timings values may take a value of -1 to indicate that they
        will use the last value sent (or the defaults if no title has been
        displayed).

        Arguments
        - title: Title text
        - subtitle: Subtitle text
        - fadeIn: time in ticks for titles to fade in. Defaults to 10.
        - stay: time in ticks for titles to stay. Defaults to 70.
        - fadeOut: time in ticks for titles to fade out. Defaults to 20.
        """
        ...


    def resetTitle(self) -> None:
        """
        Resets the title displayed to the player. This will clear the displayed
        title / subtitle and reset timings to their default values.
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def getAdvancementProgress(self, advancement: "Advancement") -> "AdvancementProgress":
        """
        Return the player's progression on the specified advancement.

        Arguments
        - advancement: advancement

        Returns
        - object detailing the player's progress
        """
        ...


    def getClientViewDistance(self) -> int:
        """
        Get the player's current client side view distance.
        
        Will default to the server view distance if the client has not yet
        communicated this information,

        Returns
        - client view distance as above
        """
        ...


    def getPing(self) -> int:
        """
        Gets the player's estimated ping in milliseconds.
        
        In Vanilla this value represents a weighted average of the response time
        to application layer ping packets sent. This value does not represent the
        network round trip time and as such may have less granularity and be
        impacted by other sources. For these reasons it **should not** be used
        for anti-cheat purposes. Its recommended use is only as a
        **qualitative** indicator of connection quality (Vanilla uses it for
        this purpose in the tab list).

        Returns
        - player ping
        """
        ...


    def getLocale(self) -> str:
        """
        Gets the player's current locale.
        
        The value of the locale String is not defined properly.
        
        The vanilla Minecraft client will use lowercase language / country pairs
        separated by an underscore, but custom resource packs may use any format
        they wish.

        Returns
        - the player's locale
        """
        ...


    def updateCommands(self) -> None:
        """
        Update the list of commands sent to the client.
        
        Generally useful to ensure the client has a complete list of commands
        after permission changes are done.
        """
        ...


    def openBook(self, book: "ItemStack") -> None:
        """
        Open a Material.WRITTEN_BOOK for a Player

        Arguments
        - book: The book to open for this player
        """
        ...


    def openSign(self, sign: "Sign") -> None:
        """
        Open a Sign for editing by the Player.
        
        The Sign must be placed in the same world as the player.

        Arguments
        - sign: The sign to edit
        """
        ...


    def showDemoScreen(self) -> None:
        """
        Shows the demo screen to the player, this screen is normally only seen in
        the demo version of the game.
        
        Servers can modify the text on this screen using a resource pack.
        """
        ...


    def isAllowingServerListings(self) -> bool:
        """
        Gets whether the player has the "Allow Server Listings" setting enabled.

        Returns
        - whether the player allows server listings
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot(Spigot):

        def getRawAddress(self) -> "InetSocketAddress":
            """
            Gets the connection address of this player, regardless of whether it
            has been spoofed or not.

            Returns
            - the player's connection address
            """
            ...


        def getCollidesWithEntities(self) -> bool:
            """
            Gets whether the player collides with entities

            Returns
            - the player's collision toggle state

            Deprecated
            - see LivingEntity.isCollidable()
            """
            ...


        def setCollidesWithEntities(self, collides: bool) -> None:
            """
            Sets whether the player collides with entities

            Arguments
            - collides: whether the player should collide with entities or
            not.

            Deprecated
            - LivingEntity.setCollidable(boolean)
            """
            ...


        def respawn(self) -> None:
            """
            Respawns the player if dead.
            """
            ...


        def getHiddenPlayers(self) -> "java.util.Set"["Player"]:
            """
            Gets all players hidden with .hidePlayer(org.bukkit.entity.Player).

            Returns
            - a Set with all hidden players
            """
            ...


        def sendMessage(self, component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            ...


        def sendMessage(self, *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            ...


        def sendMessage(self, position: "net.md_5.bungee.api.ChatMessageType", component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            """
            Sends the component to the specified screen position of this player

            Arguments
            - position: the screen position
            - component: the components to send
            """
            ...


        def sendMessage(self, position: "net.md_5.bungee.api.ChatMessageType", *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            """
            Sends an array of components as a single message to the specified screen position of this player

            Arguments
            - position: the screen position
            - components: the components to send
            """
            ...


        def sendMessage(self, position: "net.md_5.bungee.api.ChatMessageType", sender: "UUID", component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            """
            Sends the component to the specified screen position of this player

            Arguments
            - position: the screen position
            - sender: the sender of the message
            - component: the components to send
            """
            ...


        def sendMessage(self, position: "net.md_5.bungee.api.ChatMessageType", sender: "UUID", *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            """
            Sends an array of components as a single message to the specified screen position of this player

            Arguments
            - position: the screen position
            - sender: the sender of the message
            - components: the components to send
            """
            ...
