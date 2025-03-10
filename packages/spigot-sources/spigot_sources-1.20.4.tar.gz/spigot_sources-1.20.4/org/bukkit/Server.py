"""
Python module generated from Java source file org.bukkit.Server

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from java.io import File
from java.io import Serializable
from java.net import InetAddress
from java.util import Collections
from java.util import Iterator
from java.util import UUID
from java.util.function import Consumer
from org.bukkit import *
from org.bukkit.Warning import WarningState
from org.bukkit.advancement import Advancement
from org.bukkit.block.data import BlockData
from org.bukkit.boss import BarColor
from org.bukkit.boss import BarFlag
from org.bukkit.boss import BarStyle
from org.bukkit.boss import BossBar
from org.bukkit.boss import KeyedBossBar
from org.bukkit.command import CommandException
from org.bukkit.command import CommandSender
from org.bukkit.command import ConsoleCommandSender
from org.bukkit.command import PluginCommand
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.entity import SpawnCategory
from org.bukkit.event.inventory import InventoryType
from org.bukkit.event.server import ServerListPingEvent
from org.bukkit.generator import ChunkGenerator
from org.bukkit.help import HelpMap
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import ItemCraftResult
from org.bukkit.inventory import ItemFactory
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import Recipe
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.loot import LootTable
from org.bukkit.map import MapView
from org.bukkit.packs import DataPackManager
from org.bukkit.packs import ResourcePack
from org.bukkit.permissions import Permissible
from org.bukkit.plugin import PluginManager
from org.bukkit.plugin import ServicesManager
from org.bukkit.plugin.messaging import Messenger
from org.bukkit.plugin.messaging import PluginMessageRecipient
from org.bukkit.profile import PlayerProfile
from org.bukkit.scheduler import BukkitScheduler
from org.bukkit.scoreboard import Criteria
from org.bukkit.scoreboard import ScoreboardManager
from org.bukkit.structure import StructureManager
from org.bukkit.util import CachedServerIcon
from typing import Any, Callable, Iterable, Tuple


class Server(PluginMessageRecipient):
    """
    Represents a server implementation.
    """

    BROADCAST_CHANNEL_ADMINISTRATIVE = "bukkit.broadcast.admin"
    """
    Used for all administrative messages, such as an operator using a
    command.
    
    For use in .broadcast(java.lang.String, java.lang.String).
    """
    BROADCAST_CHANNEL_USERS = "bukkit.broadcast.user"
    """
    Used for all announcement messages, such as informing users that a
    player has joined.
    
    For use in .broadcast(java.lang.String, java.lang.String).
    """


    def getName(self) -> str:
        """
        Gets the name of this server implementation.

        Returns
        - name of this server implementation
        """
        ...


    def getVersion(self) -> str:
        """
        Gets the version string of this server implementation.

        Returns
        - version of this server implementation
        """
        ...


    def getBukkitVersion(self) -> str:
        """
        Gets the Bukkit version that this server is running.

        Returns
        - version of Bukkit
        """
        ...


    def getOnlinePlayers(self) -> Iterable["Player"]:
        """
        Gets a view of all currently logged in players. This Collections.unmodifiableCollection(Collection) view is a reused
        object, making some operations like Collection.size()
        zero-allocation.
        
        The collection is a view backed by the internal representation, such
        that, changes to the internal state of the server will be reflected
        immediately. However, the reuse of the returned collection (identity)
        is not strictly guaranteed for future or all implementations. Casting
        the collection, or relying on interface implementations (like Serializable or List), is deprecated.
        
        Iteration behavior is undefined outside of self-contained main-thread
        uses. Normal and immediate iterator use without consequences that
        affect the collection are fully supported. The effects following
        (non-exhaustive) Entity.teleport(Location) teleportation,
        Player.setHealth(double) death, and Player.kickPlayer(
        String) kicking are undefined. Any use of this collection from
        asynchronous threads is unsafe.
        
        For safe consequential iteration or mimicking the old array behavior,
        using Collection.toArray(Object[]) is recommended. For making
        snapshots, ImmutableList.copyOf(Collection) is recommended.

        Returns
        - a view of currently online players.
        """
        ...


    def getMaxPlayers(self) -> int:
        """
        Get the maximum amount of players which can login to this server.

        Returns
        - the amount of players this server allows
        """
        ...


    def setMaxPlayers(self, maxPlayers: int) -> None:
        """
        Set the maximum amount of players allowed to be logged in at once.

        Arguments
        - maxPlayers: The maximum amount of concurrent players
        """
        ...


    def getPort(self) -> int:
        """
        Get the game port that the server runs on.

        Returns
        - the port number of this server
        """
        ...


    def getViewDistance(self) -> int:
        """
        Get the view distance from this server.

        Returns
        - the view distance from this server.
        """
        ...


    def getSimulationDistance(self) -> int:
        """
        Get the simulation distance from this server.

        Returns
        - the simulation distance from this server.
        """
        ...


    def getIp(self) -> str:
        """
        Get the IP that this server is bound to, or empty string if not
        specified.

        Returns
        - the IP string that this server is bound to, otherwise empty
            string
        """
        ...


    def getWorldType(self) -> str:
        """
        Get world type (level-type setting) for default world.

        Returns
        - the value of level-type (e.g. DEFAULT, FLAT, DEFAULT_1_1)
        """
        ...


    def getGenerateStructures(self) -> bool:
        """
        Get generate-structures setting.

        Returns
        - True if structure generation is enabled, False otherwise
        """
        ...


    def getMaxWorldSize(self) -> int:
        """
        Get max world size.

        Returns
        - the maximum world size as specified for the server
        """
        ...


    def getAllowEnd(self) -> bool:
        """
        Gets whether this server allows the End or not.

        Returns
        - whether this server allows the End or not
        """
        ...


    def getAllowNether(self) -> bool:
        """
        Gets whether this server allows the Nether or not.

        Returns
        - whether this server allows the Nether or not
        """
        ...


    def isLoggingIPs(self) -> bool:
        """
        Gets whether the server is logging the IP addresses of players.

        Returns
        - whether the server is logging the IP addresses of players
        """
        ...


    def getInitialEnabledPacks(self) -> list[str]:
        """
        Gets a list of packs to be enabled.

        Returns
        - a list of packs names
        """
        ...


    def getInitialDisabledPacks(self) -> list[str]:
        """
        Gets a list of packs that will not be enabled automatically.

        Returns
        - a list of packs names
        """
        ...


    def getDataPackManager(self) -> "DataPackManager":
        """
        Get the DataPack Manager.

        Returns
        - the manager
        """
        ...


    def getServerTickManager(self) -> "ServerTickManager":
        """
        Get the ServerTick Manager.

        Returns
        - the manager
        """
        ...


    def getServerResourcePack(self) -> "ResourcePack":
        """
        Gets the resource pack configured to be sent to clients by the server.

        Returns
        - the resource pack
        """
        ...


    def getResourcePack(self) -> str:
        """
        Gets the server resource pack uri, or empty string if not specified.

        Returns
        - the server resource pack uri, otherwise empty string
        """
        ...


    def getResourcePackHash(self) -> str:
        """
        Gets the SHA-1 digest of the server resource pack, or empty string if
        not specified.

        Returns
        - the SHA-1 digest of the server resource pack, otherwise empty
            string
        """
        ...


    def getResourcePackPrompt(self) -> str:
        """
        Gets the custom prompt message to be shown when the server resource
        pack is required, or empty string if not specified.

        Returns
        - the custom prompt message to be shown when the server resource,
            otherwise empty string
        """
        ...


    def isResourcePackRequired(self) -> bool:
        """
        Gets whether the server resource pack is enforced.

        Returns
        - whether the server resource pack is enforced
        """
        ...


    def hasWhitelist(self) -> bool:
        """
        Gets whether this server has a whitelist or not.

        Returns
        - whether this server has a whitelist or not
        """
        ...


    def setWhitelist(self, value: bool) -> None:
        """
        Sets if the server is whitelisted.

        Arguments
        - value: True for whitelist on, False for off
        """
        ...


    def isWhitelistEnforced(self) -> bool:
        """
        Gets whether the server whitelist is enforced.
        
        If the whitelist is enforced, non-whitelisted players will be
        disconnected when the server whitelist is reloaded.

        Returns
        - whether the server whitelist is enforced
        """
        ...


    def setWhitelistEnforced(self, value: bool) -> None:
        """
        Sets if the server whitelist is enforced.
        
        If the whitelist is enforced, non-whitelisted players will be
        disconnected when the server whitelist is reloaded.

        Arguments
        - value: True for enforced, False for not
        """
        ...


    def getWhitelistedPlayers(self) -> set["OfflinePlayer"]:
        """
        Gets a list of whitelisted players.

        Returns
        - a set containing all whitelisted players
        """
        ...


    def reloadWhitelist(self) -> None:
        """
        Reloads the whitelist from disk.
        """
        ...


    def broadcastMessage(self, message: str) -> int:
        """
        Broadcast a message to all players.
        
        This is the same as calling .broadcast(java.lang.String,
        java.lang.String) to .BROADCAST_CHANNEL_USERS

        Arguments
        - message: the message

        Returns
        - the number of players
        """
        ...


    def getUpdateFolder(self) -> str:
        """
        Gets the name of the update folder. The update folder is used to safely
        update plugins at the right moment on a plugin load.
        
        The update folder name is relative to the plugins folder.

        Returns
        - the name of the update folder
        """
        ...


    def getUpdateFolderFile(self) -> "File":
        """
        Gets the update folder. The update folder is used to safely update
        plugins at the right moment on a plugin load.

        Returns
        - the update folder
        """
        ...


    def getConnectionThrottle(self) -> int:
        """
        Gets the value of the connection throttle setting.

        Returns
        - the value of the connection throttle setting
        """
        ...


    def getTicksPerAnimalSpawns(self) -> int:
        """
        Gets default ticks per animal spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn monsters
            every tick.
        - A value of 400 will mean the server will attempt to spawn monsters
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, animal spawning will be disabled. We
        recommend using spawn-animals to control this instead.
        
        Minecraft default: 400.

        Returns
        - the default ticks per animal spawns value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerMonsterSpawns(self) -> int:
        """
        Gets the default ticks per monster spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn monsters
            every tick.
        - A value of 400 will mean the server will attempt to spawn monsters
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, monsters spawning will be disabled. We
        recommend using spawn-monsters to control this instead.
        
        Minecraft default: 1.

        Returns
        - the default ticks per monsters spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerWaterSpawns(self) -> int:
        """
        Gets the default ticks per water mob spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water mobs
            every tick.
        - A value of 400 will mean the server will attempt to spawn water mobs
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, water mobs spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per water mobs spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerWaterAmbientSpawns(self) -> int:
        """
        Gets the default ticks per water ambient mob spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water ambient mobs
            every tick.
        - A value of 400 will mean the server will attempt to spawn water ambient mobs
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, ambient mobs spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per water ambient mobs spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerWaterUndergroundCreatureSpawns(self) -> int:
        """
        Gets the default ticks per water underground creature spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water underground creature
            every tick.
        - A value of 400 will mean the server will attempt to spawn water underground creature
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, water underground creature spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per water underground creature spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerAmbientSpawns(self) -> int:
        """
        Gets the default ticks per ambient mob spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn ambient mobs
            every tick.
        - A value of 400 will mean the server will attempt to spawn ambient mobs
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, ambient mobs spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per ambient mobs spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def getTicksPerSpawns(self, spawnCategory: "SpawnCategory") -> int:
        """
        Gets the default ticks per SpawnCategory spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn SpawnCategory mobs
            every tick.
        - A value of 400 will mean the server will attempt to spawn SpawnCategory mobs
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, SpawnCategory mobs spawning will be disabled.
        
        Minecraft default: 1.
        
        **Note: ** the SpawnCategory.MISC are not consider.

        Arguments
        - spawnCategory: the category of spawn

        Returns
        - the default ticks per SpawnCategory mobs spawn value
        """
        ...


    def getPlayer(self, name: str) -> "Player":
        """
        Gets a player object by the given username.
        
        This method may not return objects for offline players.

        Arguments
        - name: the name to look up

        Returns
        - a player if one was found, null otherwise
        """
        ...


    def getPlayerExact(self, name: str) -> "Player":
        """
        Gets the player with the exact given name, case insensitive.

        Arguments
        - name: Exact name of the player to retrieve

        Returns
        - a player object if one was found, null otherwise
        """
        ...


    def matchPlayer(self, name: str) -> list["Player"]:
        """
        Attempts to match any players with the given name, and returns a list
        of all possibly matches.
        
        This list is not sorted in any particular order. If an exact match is
        found, the returned list will only contain a single result.

        Arguments
        - name: the (partial) name to match

        Returns
        - list of all possible players
        """
        ...


    def getPlayer(self, id: "UUID") -> "Player":
        """
        Gets the player with the given UUID.

        Arguments
        - id: UUID of the player to retrieve

        Returns
        - a player object if one was found, null otherwise
        """
        ...


    def getPluginManager(self) -> "PluginManager":
        """
        Gets the plugin manager for interfacing with plugins.

        Returns
        - a plugin manager for this Server instance
        """
        ...


    def getScheduler(self) -> "BukkitScheduler":
        """
        Gets the scheduler for managing scheduled events.

        Returns
        - a scheduling service for this server
        """
        ...


    def getServicesManager(self) -> "ServicesManager":
        """
        Gets a services manager.

        Returns
        - s services manager
        """
        ...


    def getWorlds(self) -> list["World"]:
        """
        Gets a list of all worlds on this server.

        Returns
        - a list of worlds
        """
        ...


    def createWorld(self, creator: "WorldCreator") -> "World":
        """
        Creates or loads a world with the given name using the specified
        options.
        
        If the world is already loaded, it will just return the equivalent of
        getWorld(creator.name()).

        Arguments
        - creator: the options to use when creating the world

        Returns
        - newly created or loaded world
        """
        ...


    def unloadWorld(self, name: str, save: bool) -> bool:
        """
        Unloads a world with the given name.

        Arguments
        - name: Name of the world to unload
        - save: whether to save the chunks before unloading

        Returns
        - True if successful, False otherwise
        """
        ...


    def unloadWorld(self, world: "World", save: bool) -> bool:
        """
        Unloads the given world.

        Arguments
        - world: the world to unload
        - save: whether to save the chunks before unloading

        Returns
        - True if successful, False otherwise
        """
        ...


    def getWorld(self, name: str) -> "World":
        """
        Gets the world with the given name.

        Arguments
        - name: the name of the world to retrieve

        Returns
        - a world with the given name, or null if none exists
        """
        ...


    def getWorld(self, uid: "UUID") -> "World":
        """
        Gets the world from the given Unique ID.

        Arguments
        - uid: a unique-id of the world to retrieve

        Returns
        - a world with the given Unique ID, or null if none exists
        """
        ...


    def createWorldBorder(self) -> "WorldBorder":
        """
        Create a new virtual WorldBorder.
        
        Note that world borders created by the server will not respect any world
        scaling effects (i.e. coordinates are not divided by 8 in the nether).

        Returns
        - the created world border instance

        See
        - Player.setWorldBorder(WorldBorder)
        """
        ...


    def getMap(self, id: int) -> "MapView":
        """
        Gets the map from the given item ID.

        Arguments
        - id: the id of the map to get

        Returns
        - a map view if it exists, or null otherwise

        Deprecated
        - Magic value
        """
        ...


    def createMap(self, world: "World") -> "MapView":
        """
        Create a new map with an automatically assigned ID.

        Arguments
        - world: the world the map will belong to

        Returns
        - a newly created map view
        """
        ...


    def createExplorerMap(self, world: "World", location: "Location", structureType: "StructureType") -> "ItemStack":
        """
        Create a new explorer map targeting the closest nearby structure of a
        given StructureType.
        
        This method uses implementation default values for radius and
        findUnexplored (usually 100, True).

        Arguments
        - world: the world the map will belong to
        - location: the origin location to find the nearest structure
        - structureType: the type of structure to find

        Returns
        - a newly created item stack

        See
        - World.locateNearestStructure(org.bukkit.Location,
             org.bukkit.StructureType, int, boolean)
        """
        ...


    def createExplorerMap(self, world: "World", location: "Location", structureType: "StructureType", radius: int, findUnexplored: bool) -> "ItemStack":
        """
        Create a new explorer map targeting the closest nearby structure of a
        given StructureType.
        
        This method uses implementation default values for radius and
        findUnexplored (usually 100, True).

        Arguments
        - world: the world the map will belong to
        - location: the origin location to find the nearest structure
        - structureType: the type of structure to find
        - radius: radius to search, see World#locateNearestStructure for more
                      information
        - findUnexplored: whether to find unexplored structures

        Returns
        - the newly created item stack

        See
        - World.locateNearestStructure(org.bukkit.Location,
             org.bukkit.StructureType, int, boolean)
        """
        ...


    def reload(self) -> None:
        """
        Reloads the server, refreshing settings and plugin information.
        """
        ...


    def reloadData(self) -> None:
        """
        Reload only the Minecraft data for the server. This includes custom
        advancements and loot tables.
        """
        ...


    def getLogger(self) -> "Logger":
        """
        Returns the primary logger associated with this server instance.

        Returns
        - Logger associated with this server
        """
        ...


    def getPluginCommand(self, name: str) -> "PluginCommand":
        """
        Gets a PluginCommand with the given name or alias.

        Arguments
        - name: the name of the command to retrieve

        Returns
        - a plugin command if found, null otherwise
        """
        ...


    def savePlayers(self) -> None:
        """
        Writes loaded players to disk.
        """
        ...


    def dispatchCommand(self, sender: "CommandSender", commandLine: str) -> bool:
        """
        Dispatches a command on this server, and executes it if found.

        Arguments
        - sender: the apparent sender of the command
        - commandLine: the command + arguments. Example: `test abc
            123`

        Returns
        - returns False if no target is found

        Raises
        - CommandException: thrown when the executor for the given command
            fails with an unhandled exception
        """
        ...


    def addRecipe(self, recipe: "Recipe") -> bool:
        """
        Adds a recipe to the crafting manager.

        Arguments
        - recipe: the recipe to add

        Returns
        - True if the recipe was added, False if it wasn't for some
            reason
        """
        ...


    def getRecipesFor(self, result: "ItemStack") -> list["Recipe"]:
        """
        Get a list of all recipes for a given item. The stack size is ignored
        in comparisons. If the durability is -1, it will match any data value.

        Arguments
        - result: the item to match against recipe results

        Returns
        - a list of recipes with the given result
        """
        ...


    def getRecipe(self, recipeKey: "NamespacedKey") -> "Recipe":
        """
        Get the Recipe for the given key.

        Arguments
        - recipeKey: the key of the recipe to return

        Returns
        - the recipe for the given key or null.
        """
        ...


    def getCraftingRecipe(self, craftingMatrix: list["ItemStack"], world: "World") -> "Recipe":
        """
        Get the Recipe for the list of ItemStacks provided.
        
        The list is formatted as a crafting matrix where the index follow
        the pattern below:
        
        ```
        [ 0 1 2 ]
        [ 3 4 5 ]
        [ 6 7 8 ]
        ```
        
        NOTE: This method will not modify the provided ItemStack array, for that, use
        .craftItem(ItemStack[], World, Player).

        Arguments
        - craftingMatrix: list of items to be crafted from.
                              Must not contain more than 9 items.
        - world: The world the crafting takes place in.

        Returns
        - the Recipe resulting from the given crafting matrix.
        """
        ...


    def craftItem(self, craftingMatrix: list["ItemStack"], world: "World", player: "Player") -> "ItemStack":
        """
        Get the crafted item using the list of ItemStack provided.
        
        The list is formatted as a crafting matrix where the index follow
        the pattern below:
        
        ```
        [ 0 1 2 ]
        [ 3 4 5 ]
        [ 6 7 8 ]
        ```
        
        The World and Player arguments are required to fulfill the Bukkit Crafting
        events.
        
        Calls org.bukkit.event.inventory.PrepareItemCraftEvent to imitate the Player
        initiating the crafting event.

        Arguments
        - craftingMatrix: list of items to be crafted from.
                              Must not contain more than 9 items.
        - world: The world the crafting takes place in.
        - player: The player to imitate the crafting event on.

        Returns
        - the ItemStack resulting from the given crafting matrix, if no recipe is found
        an ItemStack of Material.AIR is returned.
        """
        ...


    def craftItem(self, craftingMatrix: list["ItemStack"], world: "World") -> "ItemStack":
        """
        Get the crafted item using the list of ItemStack provided.
        
        The list is formatted as a crafting matrix where the index follow
        the pattern below:
        
        ```
        [ 0 1 2 ]
        [ 3 4 5 ]
        [ 6 7 8 ]
        ```

        Arguments
        - craftingMatrix: list of items to be crafted from.
                              Must not contain more than 9 items.
        - world: The world the crafting takes place in.

        Returns
        - the ItemStack resulting from the given crafting matrix, if no recipe is found
        an ItemStack of Material.AIR is returned.
        """
        ...


    def craftItemResult(self, craftingMatrix: list["ItemStack"], world: "World", player: "Player") -> "ItemCraftResult":
        """
        Get the crafted item using the list of ItemStack provided.
        
        The list is formatted as a crafting matrix where the index follow
        the pattern below:
        
        ```
        [ 0 1 2 ]
        [ 3 4 5 ]
        [ 6 7 8 ]
        ```
        
        The World and Player arguments are required to fulfill the Bukkit Crafting
        events.
        
        Calls org.bukkit.event.inventory.PrepareItemCraftEvent to imitate the Player
        initiating the crafting event.

        Arguments
        - craftingMatrix: list of items to be crafted from.
                              Must not contain more than 9 items.
        - world: The world the crafting takes place in.
        - player: The player to imitate the crafting event on.

        Returns
        - resulting ItemCraftResult containing the resulting item, matrix and any overflow items.
        """
        ...


    def craftItemResult(self, craftingMatrix: list["ItemStack"], world: "World") -> "ItemCraftResult":
        """
        Get the crafted item using the list of ItemStack provided.
        
        The list is formatted as a crafting matrix where the index follow
        the pattern below:
        
        ```
        [ 0 1 2 ]
        [ 3 4 5 ]
        [ 6 7 8 ]
        ```

        Arguments
        - craftingMatrix: list of items to be crafted from.
                              Must not contain more than 9 items.
        - world: The world the crafting takes place in.

        Returns
        - resulting ItemCraftResult containing the resulting item, matrix and any overflow items.
        """
        ...


    def recipeIterator(self) -> Iterator["Recipe"]:
        """
        Get an iterator through the list of crafting recipes.

        Returns
        - an iterator
        """
        ...


    def clearRecipes(self) -> None:
        """
        Clears the list of crafting recipes.
        """
        ...


    def resetRecipes(self) -> None:
        """
        Resets the list of crafting recipes to the default.
        """
        ...


    def removeRecipe(self, key: "NamespacedKey") -> bool:
        """
        Remove a recipe from the server.
        
        **Note that removing a recipe may cause permanent loss of data
        associated with that recipe (eg whether it has been discovered by
        players).**

        Arguments
        - key: NamespacedKey of recipe to remove.

        Returns
        - True if recipe was removed
        """
        ...


    def getCommandAliases(self) -> dict[str, list[str]]:
        """
        Gets a list of command aliases defined in the server properties.

        Returns
        - a map of aliases to command names
        """
        ...


    def getSpawnRadius(self) -> int:
        """
        Gets the radius, in blocks, around each worlds spawn point to protect.

        Returns
        - spawn radius, or 0 if none
        """
        ...


    def setSpawnRadius(self, value: int) -> None:
        """
        Sets the radius, in blocks, around each worlds spawn point to protect.

        Arguments
        - value: new spawn radius, or 0 if none
        """
        ...


    def shouldSendChatPreviews(self) -> bool:
        """
        Gets whether the server should send a preview of the player's chat
        message to the client when the player types a message

        Returns
        - True if the server should send a preview, False otherwise

        Deprecated
        - chat previews have been removed
        """
        ...


    def isEnforcingSecureProfiles(self) -> bool:
        """
        Gets whether the server only allow players with Mojang-signed public key
        to join

        Returns
        - True if only Mojang-signed players can join, False otherwise
        """
        ...


    def getHideOnlinePlayers(self) -> bool:
        """
        Gets whether the Server hide online players in server status.

        Returns
        - True if the server hide online players, False otherwise
        """
        ...


    def getOnlineMode(self) -> bool:
        """
        Gets whether the Server is in online mode or not.

        Returns
        - True if the server authenticates clients, False otherwise
        """
        ...


    def getAllowFlight(self) -> bool:
        """
        Gets whether this server allows flying or not.

        Returns
        - True if the server allows flight, False otherwise
        """
        ...


    def isHardcore(self) -> bool:
        """
        Gets whether the server is in hardcore mode or not.

        Returns
        - True if the server mode is hardcore, False otherwise
        """
        ...


    def shutdown(self) -> None:
        """
        Shutdowns the server, stopping everything.
        """
        ...


    def broadcast(self, message: str, permission: str) -> int:
        """
        Broadcasts the specified message to every user with the given
        permission name.

        Arguments
        - message: message to broadcast
        - permission: the required permission Permissible
            permissibles must have to receive the broadcast

        Returns
        - number of message recipients
        """
        ...


    def getOfflinePlayer(self, name: str) -> "OfflinePlayer":
        """
        Gets the player by the given name, regardless if they are offline or
        online.
        
        This method may involve a blocking web request to get the UUID for the
        given name.
        
        This will return an object even if the player does not exist. To this
        method, all players will exist.

        Arguments
        - name: the name the player to retrieve

        Returns
        - an offline player

        See
        - .getOfflinePlayer(java.util.UUID)

        Deprecated
        - Persistent storage of users should be by UUID as names are no longer
                    unique past a single session.
        """
        ...


    def getOfflinePlayer(self, id: "UUID") -> "OfflinePlayer":
        """
        Gets the player by the given UUID, regardless if they are offline or
        online.
        
        This will return an object even if the player does not exist. To this
        method, all players will exist.

        Arguments
        - id: the UUID of the player to retrieve

        Returns
        - an offline player
        """
        ...


    def createPlayerProfile(self, uniqueId: "UUID", name: str) -> "PlayerProfile":
        """
        Creates a new PlayerProfile.

        Arguments
        - uniqueId: the unique id
        - name: the name

        Returns
        - the new PlayerProfile

        Raises
        - IllegalArgumentException: if both the unique id is
        `null` and the name is `null` or blank
        """
        ...


    def createPlayerProfile(self, uniqueId: "UUID") -> "PlayerProfile":
        """
        Creates a new PlayerProfile.

        Arguments
        - uniqueId: the unique id

        Returns
        - the new PlayerProfile

        Raises
        - IllegalArgumentException: if the unique id is `null`
        """
        ...


    def createPlayerProfile(self, name: str) -> "PlayerProfile":
        """
        Creates a new PlayerProfile.

        Arguments
        - name: the name

        Returns
        - the new PlayerProfile

        Raises
        - IllegalArgumentException: if the name is `null` or
        blank
        """
        ...


    def getIPBans(self) -> set[str]:
        """
        Gets a set containing all current IPs that are banned.

        Returns
        - a set containing banned IP addresses
        """
        ...


    def banIP(self, address: str) -> None:
        """
        Bans the specified address from the server.

        Arguments
        - address: the IP address to ban

        Deprecated
        - see .banIP(InetAddress)
        """
        ...


    def unbanIP(self, address: str) -> None:
        """
        Unbans the specified address from the server.

        Arguments
        - address: the IP address to unban

        Deprecated
        - see .unbanIP(InetAddress)
        """
        ...


    def banIP(self, address: "InetAddress") -> None:
        """
        Bans the specified address from the server.

        Arguments
        - address: the IP address to ban
        """
        ...


    def unbanIP(self, address: "InetAddress") -> None:
        """
        Unbans the specified address from the server.

        Arguments
        - address: the IP address to unban
        """
        ...


    def getBannedPlayers(self) -> set["OfflinePlayer"]:
        """
        Gets a set containing all banned players.

        Returns
        - a set containing banned players
        """
        ...


    def getBanList(self, type: "BanList.Type") -> "T":
        """
        Gets a ban list for the supplied type.
        
        Type `<T>`: The ban target

        Arguments
        - type: the type of list to fetch, cannot be null

        Returns
        - a ban list of the specified type
        """
        ...


    def getOperators(self) -> set["OfflinePlayer"]:
        """
        Gets a set containing all player operators.

        Returns
        - a set containing player operators
        """
        ...


    def getDefaultGameMode(self) -> "GameMode":
        """
        Gets the default GameMode for new players.

        Returns
        - the default game mode
        """
        ...


    def setDefaultGameMode(self, mode: "GameMode") -> None:
        """
        Sets the default GameMode for new players.

        Arguments
        - mode: the new game mode
        """
        ...


    def getConsoleSender(self) -> "ConsoleCommandSender":
        """
        Gets a ConsoleCommandSender that may be used as an input source
        for this server.

        Returns
        - a console command sender
        """
        ...


    def getWorldContainer(self) -> "File":
        """
        Gets the folder that contains all of the various Worlds.

        Returns
        - folder that contains all worlds
        """
        ...


    def getOfflinePlayers(self) -> list["OfflinePlayer"]:
        """
        Gets every player that has ever played on this server.

        Returns
        - an array containing all previous players
        """
        ...


    def getMessenger(self) -> "Messenger":
        """
        Gets the Messenger responsible for this server.

        Returns
        - messenger responsible for this server
        """
        ...


    def getHelpMap(self) -> "HelpMap":
        """
        Gets the HelpMap providing help topics for this server.

        Returns
        - a help map for this server
        """
        ...


    def createInventory(self, owner: "InventoryHolder", type: "InventoryType") -> "Inventory":
        """
        Creates an empty inventory with the specified type. If the type
        is InventoryType.CHEST, the new inventory has a size of 27;
        otherwise the new inventory has the normal size for its type.
        
        InventoryType.WORKBENCH will not process crafting recipes if
        created with this method. Use
        Player.openWorkbench(Location, boolean) instead.
        
        InventoryType.ENCHANTING will not process ItemStacks
        for possible enchanting results. Use
        Player.openEnchanting(Location, boolean) instead.

        Arguments
        - owner: the holder of the inventory, or null to indicate no holder
        - type: the type of inventory to create

        Returns
        - a new inventory

        Raises
        - IllegalArgumentException: if the InventoryType cannot be
        viewed.

        See
        - InventoryType.isCreatable()
        """
        ...


    def createInventory(self, owner: "InventoryHolder", type: "InventoryType", title: str) -> "Inventory":
        """
        Creates an empty inventory with the specified type and title. If the type
        is InventoryType.CHEST, the new inventory has a size of 27;
        otherwise the new inventory has the normal size for its type.
        It should be noted that some inventory types do not support titles and
        may not render with said titles on the Minecraft client.
        
        InventoryType.WORKBENCH will not process crafting recipes if
        created with this method. Use
        Player.openWorkbench(Location, boolean) instead.
        
        InventoryType.ENCHANTING will not process ItemStacks
        for possible enchanting results. Use
        Player.openEnchanting(Location, boolean) instead.

        Arguments
        - owner: The holder of the inventory; can be null if there's no holder.
        - type: The type of inventory to create.
        - title: The title of the inventory, to be displayed when it is viewed.

        Returns
        - The new inventory.

        Raises
        - IllegalArgumentException: if the InventoryType cannot be
        viewed.

        See
        - InventoryType.isCreatable()
        """
        ...


    def createInventory(self, owner: "InventoryHolder", size: int) -> "Inventory":
        """
        Creates an empty inventory of type InventoryType.CHEST with the
        specified size.

        Arguments
        - owner: the holder of the inventory, or null to indicate no holder
        - size: a multiple of 9 as the size of inventory to create

        Returns
        - a new inventory

        Raises
        - IllegalArgumentException: if the size is not a multiple of 9
        """
        ...


    def createInventory(self, owner: "InventoryHolder", size: int, title: str) -> "Inventory":
        """
        Creates an empty inventory of type InventoryType.CHEST with the
        specified size and title.

        Arguments
        - owner: the holder of the inventory, or null to indicate no holder
        - size: a multiple of 9 as the size of inventory to create
        - title: the title of the inventory, displayed when inventory is
            viewed

        Returns
        - a new inventory

        Raises
        - IllegalArgumentException: if the size is not a multiple of 9
        """
        ...


    def createMerchant(self, title: str) -> "Merchant":
        """
        Creates an empty merchant.

        Arguments
        - title: the title of the corresponding merchant inventory, displayed
        when the merchant inventory is viewed

        Returns
        - a new merchant
        """
        ...


    def getMaxChainedNeighborUpdates(self) -> int:
        """
        Gets the amount of consecutive neighbor updates before skipping
        additional ones.

        Returns
        - the amount of consecutive neighbor updates, if the value is
        negative then the limit it's not used
        """
        ...


    def getMonsterSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of monsters that can spawn in a
        chunk.

        Returns
        - the monster spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getAnimalSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of animals that can spawn in a
        chunk.

        Returns
        - the animal spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getWaterAnimalSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of water animals that can spawn in
        a chunk.

        Returns
        - the water animal spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getWaterAmbientSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of water ambient mobs that can spawn
        in a chunk.

        Returns
        - the water ambient spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getWaterUndergroundCreatureSpawnLimit(self) -> int:
        """
        Get user-specified limit for number of water creature underground that can spawn
        in a chunk.

        Returns
        - the water underground creature limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getAmbientSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of ambient mobs that can spawn in
        a chunk.

        Returns
        - the ambient spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getSpawnLimit(self, spawnCategory: "SpawnCategory") -> int:
        """
        Gets user-specified limit for number of SpawnCategory mobs that can spawn in
        a chunk.
        
        **Note: the SpawnCategory.MISC are not consider.**

        Arguments
        - spawnCategory: the category spawn

        Returns
        - the SpawnCategory spawn limit
        """
        ...


    def isPrimaryThread(self) -> bool:
        """
        Checks the current thread against the expected primary thread for the
        server.
        
        **Note:** this method should not be used to indicate the current
        synchronized state of the runtime. A current thread matching the main
        thread indicates that it is synchronized, but a mismatch **does not
        preclude** the same assumption.

        Returns
        - True if the current thread matches the expected primary thread,
            False otherwise
        """
        ...


    def getMotd(self) -> str:
        """
        Gets the message that is displayed on the server list.

        Returns
        - the servers MOTD
        """
        ...


    def setMotd(self, motd: str) -> None:
        """
        Set the message that is displayed on the server list.

        Arguments
        - motd: The message to be displayed
        """
        ...


    def getShutdownMessage(self) -> str:
        """
        Gets the default message that is displayed when the server is stopped.

        Returns
        - the shutdown message
        """
        ...


    def getWarningState(self) -> "WarningState":
        """
        Gets the current warning state for the server.

        Returns
        - the configured warning state
        """
        ...


    def getItemFactory(self) -> "ItemFactory":
        """
        Gets the instance of the item factory (for ItemMeta).

        Returns
        - the item factory

        See
        - ItemFactory
        """
        ...


    def getScoreboardManager(self) -> "ScoreboardManager":
        """
        Gets the instance of the scoreboard manager.
        
        This will only exist after the first world has loaded.

        Returns
        - the scoreboard manager or null if no worlds are loaded.
        """
        ...


    def getScoreboardCriteria(self, name: str) -> "Criteria":
        """
        Get (or create) a new Criteria by its name.

        Arguments
        - name: the criteria name

        Returns
        - the criteria

        See
        - Criteria Criteria for a list of constants
        """
        ...


    def getServerIcon(self) -> "CachedServerIcon":
        """
        Gets an instance of the server's default server-icon.

        Returns
        - the default server-icon; null values may be used by the
            implementation to indicate no defined icon, but this behavior is
            not guaranteed
        """
        ...


    def loadServerIcon(self, file: "File") -> "CachedServerIcon":
        """
        Loads an image from a file, and returns a cached image for the specific
        server-icon.
        
        Size and type are implementation defined. An incompatible file is
        guaranteed to throw an implementation-defined Exception.

        Arguments
        - file: the file to load the from

        Returns
        - a cached server-icon that can be used for a ServerListPingEvent.setServerIcon(CachedServerIcon)

        Raises
        - IllegalArgumentException: if image is null
        - Exception: if the image does not meet current server server-icon
            specifications
        """
        ...


    def loadServerIcon(self, image: "BufferedImage") -> "CachedServerIcon":
        """
        Creates a cached server-icon for the specific image.
        
        Size and type are implementation defined. An incompatible file is
        guaranteed to throw an implementation-defined Exception.

        Arguments
        - image: the image to use

        Returns
        - a cached server-icon that can be used for a ServerListPingEvent.setServerIcon(CachedServerIcon)

        Raises
        - IllegalArgumentException: if image is null
        - Exception: if the image does not meet current server
            server-icon specifications
        """
        ...


    def setIdleTimeout(self, threshold: int) -> None:
        """
        Set the idle kick timeout. Any players idle for the specified amount of
        time will be automatically kicked.
        
        A value of 0 will disable the idle kick timeout.

        Arguments
        - threshold: the idle timeout in minutes
        """
        ...


    def getIdleTimeout(self) -> int:
        """
        Gets the idle kick timeout.

        Returns
        - the idle timeout in minutes
        """
        ...


    def createChunkData(self, world: "World") -> "ChunkGenerator.ChunkData":
        """
        Create a ChunkData for use in a generator.
        
        See ChunkGenerator.generateChunkData(org.bukkit.World, java.util.Random, int, int, org.bukkit.generator.ChunkGenerator.BiomeGrid)

        Arguments
        - world: the world to create the ChunkData for

        Returns
        - a new ChunkData for the world
        """
        ...


    def createBossBar(self, title: str, color: "BarColor", style: "BarStyle", *flags: Tuple["BarFlag", ...]) -> "BossBar":
        """
        Creates a boss bar instance to display to players. The progress
        defaults to 1.0

        Arguments
        - title: the title of the boss bar
        - color: the color of the boss bar
        - style: the style of the boss bar
        - flags: an optional list of flags to set on the boss bar

        Returns
        - the created boss bar
        """
        ...


    def createBossBar(self, key: "NamespacedKey", title: str, color: "BarColor", style: "BarStyle", *flags: Tuple["BarFlag", ...]) -> "KeyedBossBar":
        """
        Creates a boss bar instance to display to players. The progress defaults
        to 1.0.
        
        This instance is added to the persistent storage of the server and will
        be editable by commands and restored after restart.

        Arguments
        - key: the key of the boss bar that is used to access the boss bar
        - title: the title of the boss bar
        - color: the color of the boss bar
        - style: the style of the boss bar
        - flags: an optional list of flags to set on the boss bar

        Returns
        - the created boss bar
        """
        ...


    def getBossBars(self) -> Iterator["KeyedBossBar"]:
        """
        Gets an unmodifiable iterator through all persistent bossbars.
        
          - **not** bound to a org.bukkit.entity.Boss
          - 
            **not** created using
            .createBossBar(String, BarColor, BarStyle, BarFlag...)
          
        
        
        e.g. bossbars created using the bossbar command

        Returns
        - a bossbar iterator
        """
        ...


    def getBossBar(self, key: "NamespacedKey") -> "KeyedBossBar":
        """
        Gets the KeyedBossBar specified by this key.
        
          - **not** bound to a org.bukkit.entity.Boss
          - 
            **not** created using
            .createBossBar(String, BarColor, BarStyle, BarFlag...)
          
        
        
        e.g. bossbars created using the bossbar command

        Arguments
        - key: unique bossbar key

        Returns
        - bossbar or null if not exists
        """
        ...


    def removeBossBar(self, key: "NamespacedKey") -> bool:
        """
        Removes a KeyedBossBar specified by this key.
        
          - **not** bound to a org.bukkit.entity.Boss
          - 
            **not** created using
            .createBossBar(String, BarColor, BarStyle, BarFlag...)
          
        
        
        e.g. bossbars created using the bossbar command

        Arguments
        - key: unique bossbar key

        Returns
        - True if removal succeeded or False
        """
        ...


    def getEntity(self, uuid: "UUID") -> "Entity":
        """
        Gets an entity on the server by its UUID

        Arguments
        - uuid: the UUID of the entity

        Returns
        - the entity with the given UUID, or null if it isn't found
        """
        ...


    def getAdvancement(self, key: "NamespacedKey") -> "Advancement":
        """
        Get the advancement specified by this key.

        Arguments
        - key: unique advancement key

        Returns
        - advancement or null if not exists
        """
        ...


    def advancementIterator(self) -> Iterator["Advancement"]:
        """
        Get an iterator through all advancements. Advancements cannot be removed
        from this iterator,

        Returns
        - an advancement iterator
        """
        ...


    def createBlockData(self, material: "Material") -> "BlockData":
        """
        Creates a new BlockData instance for the specified Material, with
        all properties initialized to unspecified defaults.

        Arguments
        - material: the material

        Returns
        - new data instance
        """
        ...


    def createBlockData(self, material: "Material", consumer: "Consumer"["BlockData"]) -> "BlockData":
        """
        Creates a new BlockData instance for the specified Material, with
        all properties initialized to unspecified defaults.

        Arguments
        - material: the material
        - consumer: consumer to run on new instance before returning

        Returns
        - new data instance
        """
        ...


    def createBlockData(self, data: str) -> "BlockData":
        """
        Creates a new BlockData instance with material and properties
        parsed from provided data.

        Arguments
        - data: data string

        Returns
        - new data instance

        Raises
        - IllegalArgumentException: if the specified data is not valid
        """
        ...


    def createBlockData(self, material: "Material", data: str) -> "BlockData":
        """
        Creates a new BlockData instance for the specified Material, with
        all properties initialized to unspecified defaults, except for those
        provided in data.
        
        If `material` is specified, then the data string must not also
        contain the material.

        Arguments
        - material: the material
        - data: data string

        Returns
        - new data instance

        Raises
        - IllegalArgumentException: if the specified data is not valid
        """
        ...


    def getTag(self, registry: str, tag: "NamespacedKey", clazz: type["T"]) -> "Tag"["T"]:
        """
        Gets a tag which has already been defined within the server. Plugins are
        suggested to use the concrete tags in Tag rather than this method
        which makes no guarantees about which tags are available, and may also be
        less performant due to lack of caching.
        
        Tags will be searched for in an implementation specific manner, but a
        path consisting of namespace/tags/registry/key is expected.
        
        Server implementations are allowed to handle only the registries
        indicated in Tag.
        
        Type `<T>`: type of the tag

        Arguments
        - registry: the tag registry to look at
        - tag: the name of the tag
        - clazz: the class of the tag entries

        Returns
        - the tag or null
        """
        ...


    def getTags(self, registry: str, clazz: type["T"]) -> Iterable["Tag"["T"]]:
        """
        Gets a all tags which have been defined within the server.
        
        Server implementations are allowed to handle only the registries
        indicated in Tag.
        
        No guarantees are made about the mutability of the returned iterator.
        
        Type `<T>`: type of the tag

        Arguments
        - registry: the tag registry to look at
        - clazz: the class of the tag entries

        Returns
        - all defined tags
        """
        ...


    def getLootTable(self, key: "NamespacedKey") -> "LootTable":
        """
        Gets the specified LootTable.

        Arguments
        - key: the name of the LootTable

        Returns
        - the LootTable, or null if no LootTable is found with that name
        """
        ...


    def selectEntities(self, sender: "CommandSender", selector: str) -> list["Entity"]:
        """
        Selects entities using the given Vanilla selector.
        
        No guarantees are made about the selector format, other than they match
        the Vanilla format for the active Minecraft version.
        
        Usually a selector will start with '@', unless selecting a Player in
        which case it may simply be the Player's name or UUID.
        
        Note that in Vanilla, elevated permissions are usually required to use
        '@' selectors, but this method should not check such permissions from the
        sender.

        Arguments
        - sender: the sender to execute as, must be provided
        - selector: the selection string

        Returns
        - a list of the selected entities. The list will not be null, but
        no further guarantees are made.

        Raises
        - IllegalArgumentException: if the selector is malformed in any way
        or a parameter is null
        """
        ...


    def getStructureManager(self) -> "StructureManager":
        """
        Gets the structure manager for loading and saving structures.

        Returns
        - the structure manager
        """
        ...


    def getRegistry(self, tClass: type["T"]) -> "Registry"["T"]:
        """
        Returns the registry for the given class.
        
        If no registry is present for the given class null will be returned.
        
        Depending on the implementation not every registry present in
        Registry will be returned by this method.
        
        Type `<T>`: type of the registry

        Arguments
        - tClass: of the registry to get

        Returns
        - the corresponding registry or null if not present
        """
        ...


    def getUnsafe(self) -> "UnsafeValues":
        """
        Returns
        - the unsafe values instance

        See
        - UnsafeValues
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot:

        def getConfig(self) -> "org.bukkit.configuration.file.YamlConfiguration":
            ...


        def broadcast(self, component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            """
            Sends the component to the player

            Arguments
            - component: the components to send
            """
            ...


        def broadcast(self, *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            """
            Sends an array of components as a single message to the player

            Arguments
            - components: the components to send
            """
            ...


        def restart(self) -> None:
            """
            Restart the server. If the server administrator has not configured restarting, the server will stop.
            """
            ...
