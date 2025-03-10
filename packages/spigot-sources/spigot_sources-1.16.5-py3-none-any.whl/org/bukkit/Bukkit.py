"""
Python module generated from Java source file org.bukkit.Bukkit

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from java.io import File
from java.io import Serializable
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
from org.bukkit.event.inventory import InventoryType
from org.bukkit.event.server import ServerListPingEvent
from org.bukkit.generator import ChunkGenerator
from org.bukkit.help import HelpMap
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import ItemFactory
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import Recipe
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.loot import LootTable
from org.bukkit.map import MapView
from org.bukkit.permissions import Permissible
from org.bukkit.plugin import PluginManager
from org.bukkit.plugin import ServicesManager
from org.bukkit.plugin.messaging import Messenger
from org.bukkit.scheduler import BukkitScheduler
from org.bukkit.scoreboard import ScoreboardManager
from org.bukkit.util import CachedServerIcon
from typing import Any, Callable, Iterable, Tuple


class Bukkit:
    """
    Represents the Bukkit core, for version and Server singleton handling
    """

    @staticmethod
    def getServer() -> "Server":
        """
        Gets the current Server singleton

        Returns
        - Server instance being ran
        """
        ...


    @staticmethod
    def setServer(server: "Server") -> None:
        """
        Attempts to set the Server singleton.
        
        This cannot be done if the Server is already set.

        Arguments
        - server: Server instance
        """
        ...


    @staticmethod
    def getName() -> str:
        """
        Gets the name of this server implementation.

        Returns
        - name of this server implementation
        """
        ...


    @staticmethod
    def getVersion() -> str:
        """
        Gets the version string of this server implementation.

        Returns
        - version of this server implementation
        """
        ...


    @staticmethod
    def getBukkitVersion() -> str:
        """
        Gets the Bukkit version that this server is running.

        Returns
        - version of Bukkit
        """
        ...


    @staticmethod
    def getOnlinePlayers() -> Iterable["Player"]:
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


    @staticmethod
    def getMaxPlayers() -> int:
        """
        Get the maximum amount of players which can login to this server.

        Returns
        - the amount of players this server allows
        """
        ...


    @staticmethod
    def getPort() -> int:
        """
        Get the game port that the server runs on.

        Returns
        - the port number of this server
        """
        ...


    @staticmethod
    def getViewDistance() -> int:
        """
        Get the view distance from this server.

        Returns
        - the view distance from this server.
        """
        ...


    @staticmethod
    def getIp() -> str:
        """
        Get the IP that this server is bound to, or empty string if not
        specified.

        Returns
        - the IP string that this server is bound to, otherwise empty
            string
        """
        ...


    @staticmethod
    def getWorldType() -> str:
        """
        Get world type (level-type setting) for default world.

        Returns
        - the value of level-type (e.g. DEFAULT, FLAT, DEFAULT_1_1)
        """
        ...


    @staticmethod
    def getGenerateStructures() -> bool:
        """
        Get generate-structures setting.

        Returns
        - True if structure generation is enabled, False otherwise
        """
        ...


    @staticmethod
    def getMaxWorldSize() -> int:
        """
        Get max world size.

        Returns
        - the maximum world size as specified for the server
        """
        ...


    @staticmethod
    def getAllowEnd() -> bool:
        """
        Gets whether this server allows the End or not.

        Returns
        - whether this server allows the End or not
        """
        ...


    @staticmethod
    def getAllowNether() -> bool:
        """
        Gets whether this server allows the Nether or not.

        Returns
        - whether this server allows the Nether or not
        """
        ...


    @staticmethod
    def hasWhitelist() -> bool:
        """
        Gets whether this server has a whitelist or not.

        Returns
        - whether this server has a whitelist or not
        """
        ...


    @staticmethod
    def setWhitelist(value: bool) -> None:
        """
        Sets if the server is whitelisted.

        Arguments
        - value: True for whitelist on, False for off
        """
        ...


    @staticmethod
    def getWhitelistedPlayers() -> set["OfflinePlayer"]:
        """
        Gets a list of whitelisted players.

        Returns
        - a set containing all whitelisted players
        """
        ...


    @staticmethod
    def reloadWhitelist() -> None:
        """
        Reloads the whitelist from disk.
        """
        ...


    @staticmethod
    def broadcastMessage(message: str) -> int:
        """
        Broadcast a message to all players.
        
        This is the same as calling .broadcast(java.lang.String,
        java.lang.String) to Server.BROADCAST_CHANNEL_USERS

        Arguments
        - message: the message

        Returns
        - the number of players
        """
        ...


    @staticmethod
    def getUpdateFolder() -> str:
        """
        Gets the name of the update folder. The update folder is used to safely
        update plugins at the right moment on a plugin load.
        
        The update folder name is relative to the plugins folder.

        Returns
        - the name of the update folder
        """
        ...


    @staticmethod
    def getUpdateFolderFile() -> "File":
        """
        Gets the update folder. The update folder is used to safely update
        plugins at the right moment on a plugin load.

        Returns
        - the update folder
        """
        ...


    @staticmethod
    def getConnectionThrottle() -> int:
        """
        Gets the value of the connection throttle setting.

        Returns
        - the value of the connection throttle setting
        """
        ...


    @staticmethod
    def getTicksPerAnimalSpawns() -> int:
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
        """
        ...


    @staticmethod
    def getTicksPerMonsterSpawns() -> int:
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
        """
        ...


    @staticmethod
    def getTicksPerWaterSpawns() -> int:
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
        """
        ...


    @staticmethod
    def getTicksPerAmbientSpawns() -> int:
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
        """
        ...


    @staticmethod
    def getTicksPerWaterAmbientSpawns() -> int:
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
        """
        ...


    @staticmethod
    def getPlayer(name: str) -> "Player":
        """
        Gets a player object by the given username.
        
        This method may not return objects for offline players.

        Arguments
        - name: the name to look up

        Returns
        - a player if one was found, null otherwise
        """
        ...


    @staticmethod
    def getPlayerExact(name: str) -> "Player":
        """
        Gets the player with the exact given name, case insensitive.

        Arguments
        - name: Exact name of the player to retrieve

        Returns
        - a player object if one was found, null otherwise
        """
        ...


    @staticmethod
    def matchPlayer(name: str) -> list["Player"]:
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


    @staticmethod
    def getPlayer(id: "UUID") -> "Player":
        """
        Gets the player with the given UUID.

        Arguments
        - id: UUID of the player to retrieve

        Returns
        - a player object if one was found, null otherwise
        """
        ...


    @staticmethod
    def getPluginManager() -> "PluginManager":
        """
        Gets the plugin manager for interfacing with plugins.

        Returns
        - a plugin manager for this Server instance
        """
        ...


    @staticmethod
    def getScheduler() -> "BukkitScheduler":
        """
        Gets the scheduler for managing scheduled events.

        Returns
        - a scheduling service for this server
        """
        ...


    @staticmethod
    def getServicesManager() -> "ServicesManager":
        """
        Gets a services manager.

        Returns
        - s services manager
        """
        ...


    @staticmethod
    def getWorlds() -> list["World"]:
        """
        Gets a list of all worlds on this server.

        Returns
        - a list of worlds
        """
        ...


    @staticmethod
    def createWorld(creator: "WorldCreator") -> "World":
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


    @staticmethod
    def unloadWorld(name: str, save: bool) -> bool:
        """
        Unloads a world with the given name.

        Arguments
        - name: Name of the world to unload
        - save: whether to save the chunks before unloading

        Returns
        - True if successful, False otherwise
        """
        ...


    @staticmethod
    def unloadWorld(world: "World", save: bool) -> bool:
        """
        Unloads the given world.

        Arguments
        - world: the world to unload
        - save: whether to save the chunks before unloading

        Returns
        - True if successful, False otherwise
        """
        ...


    @staticmethod
    def getWorld(name: str) -> "World":
        """
        Gets the world with the given name.

        Arguments
        - name: the name of the world to retrieve

        Returns
        - a world with the given name, or null if none exists
        """
        ...


    @staticmethod
    def getWorld(uid: "UUID") -> "World":
        """
        Gets the world from the given Unique ID.

        Arguments
        - uid: a unique-id of the world to retrieve

        Returns
        - a world with the given Unique ID, or null if none exists
        """
        ...


    @staticmethod
    def getMap(id: int) -> "MapView":
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


    @staticmethod
    def createMap(world: "World") -> "MapView":
        """
        Create a new map with an automatically assigned ID.

        Arguments
        - world: the world the map will belong to

        Returns
        - a newly created map view
        """
        ...


    @staticmethod
    def createExplorerMap(world: "World", location: "Location", structureType: "StructureType") -> "ItemStack":
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


    @staticmethod
    def createExplorerMap(world: "World", location: "Location", structureType: "StructureType", radius: int, findUnexplored: bool) -> "ItemStack":
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


    @staticmethod
    def reload() -> None:
        """
        Reloads the server, refreshing settings and plugin information.
        """
        ...


    @staticmethod
    def reloadData() -> None:
        """
        Reload only the Minecraft data for the server. This includes custom
        advancements and loot tables.
        """
        ...


    @staticmethod
    def getLogger() -> "Logger":
        """
        Returns the primary logger associated with this server instance.

        Returns
        - Logger associated with this server
        """
        ...


    @staticmethod
    def getPluginCommand(name: str) -> "PluginCommand":
        """
        Gets a PluginCommand with the given name or alias.

        Arguments
        - name: the name of the command to retrieve

        Returns
        - a plugin command if found, null otherwise
        """
        ...


    @staticmethod
    def savePlayers() -> None:
        """
        Writes loaded players to disk.
        """
        ...


    @staticmethod
    def dispatchCommand(sender: "CommandSender", commandLine: str) -> bool:
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


    @staticmethod
    def addRecipe(recipe: "Recipe") -> bool:
        """
        Adds a recipe to the crafting manager.

        Arguments
        - recipe: the recipe to add

        Returns
        - True if the recipe was added, False if it wasn't for some
            reason
        """
        ...


    @staticmethod
    def getRecipesFor(result: "ItemStack") -> list["Recipe"]:
        """
        Get a list of all recipes for a given item. The stack size is ignored
        in comparisons. If the durability is -1, it will match any data value.

        Arguments
        - result: the item to match against recipe results

        Returns
        - a list of recipes with the given result
        """
        ...


    @staticmethod
    def getRecipe(recipeKey: "NamespacedKey") -> "Recipe":
        """
        Get the Recipe for the given key.

        Arguments
        - recipeKey: the key of the recipe to return

        Returns
        - the recipe for the given key or null.
        """
        ...


    @staticmethod
    def recipeIterator() -> Iterator["Recipe"]:
        """
        Get an iterator through the list of crafting recipes.

        Returns
        - an iterator
        """
        ...


    @staticmethod
    def clearRecipes() -> None:
        """
        Clears the list of crafting recipes.
        """
        ...


    @staticmethod
    def resetRecipes() -> None:
        """
        Resets the list of crafting recipes to the default.
        """
        ...


    @staticmethod
    def removeRecipe(key: "NamespacedKey") -> bool:
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


    @staticmethod
    def getCommandAliases() -> dict[str, list[str]]:
        """
        Gets a list of command aliases defined in the server properties.

        Returns
        - a map of aliases to command names
        """
        ...


    @staticmethod
    def getSpawnRadius() -> int:
        """
        Gets the radius, in blocks, around each worlds spawn point to protect.

        Returns
        - spawn radius, or 0 if none
        """
        ...


    @staticmethod
    def setSpawnRadius(value: int) -> None:
        """
        Sets the radius, in blocks, around each worlds spawn point to protect.

        Arguments
        - value: new spawn radius, or 0 if none
        """
        ...


    @staticmethod
    def getOnlineMode() -> bool:
        """
        Gets whether the Server is in online mode or not.

        Returns
        - True if the server authenticates clients, False otherwise
        """
        ...


    @staticmethod
    def getAllowFlight() -> bool:
        """
        Gets whether this server allows flying or not.

        Returns
        - True if the server allows flight, False otherwise
        """
        ...


    @staticmethod
    def isHardcore() -> bool:
        """
        Gets whether the server is in hardcore mode or not.

        Returns
        - True if the server mode is hardcore, False otherwise
        """
        ...


    @staticmethod
    def shutdown() -> None:
        """
        Shutdowns the server, stopping everything.
        """
        ...


    @staticmethod
    def broadcast(message: str, permission: str) -> int:
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


    @staticmethod
    def getOfflinePlayer(name: str) -> "OfflinePlayer":
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


    @staticmethod
    def getOfflinePlayer(id: "UUID") -> "OfflinePlayer":
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


    @staticmethod
    def getIPBans() -> set[str]:
        """
        Gets a set containing all current IPs that are banned.

        Returns
        - a set containing banned IP addresses
        """
        ...


    @staticmethod
    def banIP(address: str) -> None:
        """
        Bans the specified address from the server.

        Arguments
        - address: the IP address to ban
        """
        ...


    @staticmethod
    def unbanIP(address: str) -> None:
        """
        Unbans the specified address from the server.

        Arguments
        - address: the IP address to unban
        """
        ...


    @staticmethod
    def getBannedPlayers() -> set["OfflinePlayer"]:
        """
        Gets a set containing all banned players.

        Returns
        - a set containing banned players
        """
        ...


    @staticmethod
    def getBanList(type: "BanList.Type") -> "BanList":
        """
        Gets a ban list for the supplied type.
        
        Bans by name are no longer supported and this method will return
        null when trying to request them. The replacement is bans by UUID.

        Arguments
        - type: the type of list to fetch, cannot be null

        Returns
        - a ban list of the specified type
        """
        ...


    @staticmethod
    def getOperators() -> set["OfflinePlayer"]:
        """
        Gets a set containing all player operators.

        Returns
        - a set containing player operators
        """
        ...


    @staticmethod
    def getDefaultGameMode() -> "GameMode":
        """
        Gets the default GameMode for new players.

        Returns
        - the default game mode
        """
        ...


    @staticmethod
    def setDefaultGameMode(mode: "GameMode") -> None:
        """
        Sets the default GameMode for new players.

        Arguments
        - mode: the new game mode
        """
        ...


    @staticmethod
    def getConsoleSender() -> "ConsoleCommandSender":
        """
        Gets a ConsoleCommandSender that may be used as an input source
        for this server.

        Returns
        - a console command sender
        """
        ...


    @staticmethod
    def getWorldContainer() -> "File":
        """
        Gets the folder that contains all of the various Worlds.

        Returns
        - folder that contains all worlds
        """
        ...


    @staticmethod
    def getOfflinePlayers() -> list["OfflinePlayer"]:
        """
        Gets every player that has ever played on this server.

        Returns
        - an array containing all previous players
        """
        ...


    @staticmethod
    def getMessenger() -> "Messenger":
        """
        Gets the Messenger responsible for this server.

        Returns
        - messenger responsible for this server
        """
        ...


    @staticmethod
    def getHelpMap() -> "HelpMap":
        """
        Gets the HelpMap providing help topics for this server.

        Returns
        - a help map for this server
        """
        ...


    @staticmethod
    def createInventory(owner: "InventoryHolder", type: "InventoryType") -> "Inventory":
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


    @staticmethod
    def createInventory(owner: "InventoryHolder", type: "InventoryType", title: str) -> "Inventory":
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


    @staticmethod
    def createInventory(owner: "InventoryHolder", size: int) -> "Inventory":
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


    @staticmethod
    def createInventory(owner: "InventoryHolder", size: int, title: str) -> "Inventory":
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


    @staticmethod
    def createMerchant(title: str) -> "Merchant":
        """
        Creates an empty merchant.

        Arguments
        - title: the title of the corresponding merchant inventory, displayed
        when the merchant inventory is viewed

        Returns
        - a new merchant
        """
        ...


    @staticmethod
    def getMonsterSpawnLimit() -> int:
        """
        Gets user-specified limit for number of monsters that can spawn in a
        chunk.

        Returns
        - the monster spawn limit
        """
        ...


    @staticmethod
    def getAnimalSpawnLimit() -> int:
        """
        Gets user-specified limit for number of animals that can spawn in a
        chunk.

        Returns
        - the animal spawn limit
        """
        ...


    @staticmethod
    def getWaterAnimalSpawnLimit() -> int:
        """
        Gets user-specified limit for number of water animals that can spawn in
        a chunk.

        Returns
        - the water animal spawn limit
        """
        ...


    @staticmethod
    def getWaterAmbientSpawnLimit() -> int:
        """
        Gets user-specified limit for number of water ambient mobs that can spawn
        in a chunk.

        Returns
        - the water ambient spawn limit
        """
        ...


    @staticmethod
    def getAmbientSpawnLimit() -> int:
        """
        Gets user-specified limit for number of ambient mobs that can spawn in
        a chunk.

        Returns
        - the ambient spawn limit
        """
        ...


    @staticmethod
    def isPrimaryThread() -> bool:
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


    @staticmethod
    def getMotd() -> str:
        """
        Gets the message that is displayed on the server list.

        Returns
        - the servers MOTD
        """
        ...


    @staticmethod
    def getShutdownMessage() -> str:
        """
        Gets the default message that is displayed when the server is stopped.

        Returns
        - the shutdown message
        """
        ...


    @staticmethod
    def getWarningState() -> "WarningState":
        """
        Gets the current warning state for the server.

        Returns
        - the configured warning state
        """
        ...


    @staticmethod
    def getItemFactory() -> "ItemFactory":
        """
        Gets the instance of the item factory (for ItemMeta).

        Returns
        - the item factory

        See
        - ItemFactory
        """
        ...


    @staticmethod
    def getScoreboardManager() -> "ScoreboardManager":
        """
        Gets the instance of the scoreboard manager.
        
        This will only exist after the first world has loaded.

        Returns
        - the scoreboard manager or null if no worlds are loaded.
        """
        ...


    @staticmethod
    def getServerIcon() -> "CachedServerIcon":
        """
        Gets an instance of the server's default server-icon.

        Returns
        - the default server-icon; null values may be used by the
            implementation to indicate no defined icon, but this behavior is
            not guaranteed
        """
        ...


    @staticmethod
    def loadServerIcon(file: "File") -> "CachedServerIcon":
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


    @staticmethod
    def loadServerIcon(image: "BufferedImage") -> "CachedServerIcon":
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


    @staticmethod
    def setIdleTimeout(threshold: int) -> None:
        """
        Set the idle kick timeout. Any players idle for the specified amount of
        time will be automatically kicked.
        
        A value of 0 will disable the idle kick timeout.

        Arguments
        - threshold: the idle timeout in minutes
        """
        ...


    @staticmethod
    def getIdleTimeout() -> int:
        """
        Gets the idle kick timeout.

        Returns
        - the idle timeout in minutes
        """
        ...


    @staticmethod
    def createChunkData(world: "World") -> "ChunkGenerator.ChunkData":
        """
        Create a ChunkData for use in a generator.
        
        See ChunkGenerator.generateChunkData(org.bukkit.World, java.util.Random, int, int, org.bukkit.generator.ChunkGenerator.BiomeGrid)

        Arguments
        - world: the world to create the ChunkData for

        Returns
        - a new ChunkData for the world
        """
        ...


    @staticmethod
    def createBossBar(title: str, color: "BarColor", style: "BarStyle", *flags: Tuple["BarFlag", ...]) -> "BossBar":
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


    @staticmethod
    def createBossBar(key: "NamespacedKey", title: str, color: "BarColor", style: "BarStyle", *flags: Tuple["BarFlag", ...]) -> "KeyedBossBar":
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


    @staticmethod
    def getBossBars() -> Iterator["KeyedBossBar"]:
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


    @staticmethod
    def getBossBar(key: "NamespacedKey") -> "KeyedBossBar":
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


    @staticmethod
    def removeBossBar(key: "NamespacedKey") -> bool:
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


    @staticmethod
    def getEntity(uuid: "UUID") -> "Entity":
        """
        Gets an entity on the server by its UUID

        Arguments
        - uuid: the UUID of the entity

        Returns
        - the entity with the given UUID, or null if it isn't found
        """
        ...


    @staticmethod
    def getAdvancement(key: "NamespacedKey") -> "Advancement":
        """
        Get the advancement specified by this key.

        Arguments
        - key: unique advancement key

        Returns
        - advancement or null if not exists
        """
        ...


    @staticmethod
    def advancementIterator() -> Iterator["Advancement"]:
        """
        Get an iterator through all advancements. Advancements cannot be removed
        from this iterator,

        Returns
        - an advancement iterator
        """
        ...


    @staticmethod
    def createBlockData(material: "Material") -> "BlockData":
        """
        Creates a new BlockData instance for the specified Material, with
        all properties initialized to unspecified defaults.

        Arguments
        - material: the material

        Returns
        - new data instance
        """
        ...


    @staticmethod
    def createBlockData(material: "Material", consumer: "Consumer"["BlockData"]) -> "BlockData":
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


    @staticmethod
    def createBlockData(data: str) -> "BlockData":
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


    @staticmethod
    def createBlockData(material: "Material", data: str) -> "BlockData":
        """
        Creates a new BlockData instance for the specified Material, with
        all properties initialized to unspecified defaults, except for those
        provided in data.

        Arguments
        - material: the material
        - data: data string

        Returns
        - new data instance

        Raises
        - IllegalArgumentException: if the specified data is not valid
        """
        ...


    @staticmethod
    def getTag(registry: str, tag: "NamespacedKey", clazz: type["T"]) -> "Tag"["T"]:
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


    @staticmethod
    def getTags(registry: str, clazz: type["T"]) -> Iterable["Tag"["T"]]:
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


    @staticmethod
    def getLootTable(key: "NamespacedKey") -> "LootTable":
        """
        Gets the specified LootTable.

        Arguments
        - key: the name of the LootTable

        Returns
        - the LootTable, or null if no LootTable is found with that name
        """
        ...


    @staticmethod
    def selectEntities(sender: "CommandSender", selector: str) -> list["Entity"]:
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


    @staticmethod
    def getUnsafe() -> "UnsafeValues":
        """
        Returns
        - the unsafe values instance

        See
        - UnsafeValues
        """
        ...


    @staticmethod
    def spigot() -> "Server.Spigot":
        ...
