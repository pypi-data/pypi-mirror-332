"""
Python module generated from Java source file org.bukkit.GameRule

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class GameRule:
    """
    GameRules dictate certain behavior within Minecraft itself
    
    For more information please visit the
    <a href="https://minecraft.wiki/w/Commands/gamerule">Minecraft
    Wiki</a>
    
    Type `<T>`: type of rule (Boolean or Integer)
    """

    ANNOUNCE_ADVANCEMENTS = GameRule<>("announceAdvancements", Boolean.class)
    """
    Toggles the announcing of advancements.
    """
    COMMAND_BLOCK_OUTPUT = GameRule<>("commandBlockOutput", Boolean.class)
    """
    Whether command blocks should notify admins when they perform commands.
    """
    DISABLE_PLAYER_MOVEMENT_CHECK = GameRule<>("disablePlayerMovementCheck", Boolean.class)
    """
    Whether the server should skip checking player speed.
    """
    DISABLE_ELYTRA_MOVEMENT_CHECK = GameRule<>("disableElytraMovementCheck", Boolean.class)
    """
    Whether the server should skip checking player speed when the player is
    wearing elytra.
    """
    DO_DAYLIGHT_CYCLE = GameRule<>("doDaylightCycle", Boolean.class)
    """
    Whether time progresses from the current moment.
    """
    DO_ENTITY_DROPS = GameRule<>("doEntityDrops", Boolean.class)
    """
    Whether entities that are not mobs should have drops.
    """
    DO_FIRE_TICK = GameRule<>("doFireTick", Boolean.class)
    """
    Whether fire should spread and naturally extinguish.
    """
    DO_LIMITED_CRAFTING = GameRule<>("doLimitedCrafting", Boolean.class)
    """
    Whether players should only be able to craft recipes they've unlocked
    first.
    """
    DO_MOB_LOOT = GameRule<>("doMobLoot", Boolean.class)
    """
    Whether mobs should drop items.
    """
    PROJECTILES_CAN_BREAK_BLOCKS = GameRule<>("projectilesCanBreakBlocks", Boolean.class)
    """
    Whether projectiles can break blocks.
    """
    DO_MOB_SPAWNING = GameRule<>("doMobSpawning", Boolean.class)
    """
    Whether mobs should naturally spawn.
    """
    DO_TILE_DROPS = GameRule<>("doTileDrops", Boolean.class)
    """
    Whether blocks should have drops.
    """
    DO_WEATHER_CYCLE = GameRule<>("doWeatherCycle", Boolean.class)
    """
    Whether the weather will change from the current moment.
    """
    KEEP_INVENTORY = GameRule<>("keepInventory", Boolean.class)
    """
    Whether the player should keep items in their inventory after death.
    """
    LOG_ADMIN_COMMANDS = GameRule<>("logAdminCommands", Boolean.class)
    """
    Whether to log admin commands to server log.
    """
    MOB_GRIEFING = GameRule<>("mobGriefing", Boolean.class)
    """
    Whether mobs can pick up items or change blocks.
    """
    NATURAL_REGENERATION = GameRule<>("naturalRegeneration", Boolean.class)
    """
    Whether players can regenerate health naturally through their hunger bar.
    """
    REDUCED_DEBUG_INFO = GameRule<>("reducedDebugInfo", Boolean.class)
    """
    Whether the debug screen shows all or reduced information.
    """
    SEND_COMMAND_FEEDBACK = GameRule<>("sendCommandFeedback", Boolean.class)
    """
    Whether the feedback from commands executed by a player should show up in
    chat. Also affects the default behavior of whether command blocks store
    their output text.
    """
    SHOW_DEATH_MESSAGES = GameRule<>("showDeathMessages", Boolean.class)
    """
    Whether a message appears in chat when a player dies.
    """
    SPECTATORS_GENERATE_CHUNKS = GameRule<>("spectatorsGenerateChunks", Boolean.class)
    """
    Whether players in spectator mode can generate chunks.
    """
    DISABLE_RAIDS = GameRule<>("disableRaids", Boolean.class)
    """
    Whether pillager raids are enabled or not.
    """
    DO_INSOMNIA = GameRule<>("doInsomnia", Boolean.class)
    """
    Whether phantoms will appear without sleeping or not.
    """
    DO_IMMEDIATE_RESPAWN = GameRule<>("doImmediateRespawn", Boolean.class)
    """
    Whether clients will respawn immediately after death or not.
    """
    DROWNING_DAMAGE = GameRule<>("drowningDamage", Boolean.class)
    """
    Whether drowning damage is enabled or not.
    """
    FALL_DAMAGE = GameRule<>("fallDamage", Boolean.class)
    """
    Whether fall damage is enabled or not.
    """
    FIRE_DAMAGE = GameRule<>("fireDamage", Boolean.class)
    """
    Whether fire damage is enabled or not.
    """
    FREEZE_DAMAGE = GameRule<>("freezeDamage", Boolean.class)
    """
    Whether freeze damage is enabled or not.
    """
    DO_PATROL_SPAWNING = GameRule<>("doPatrolSpawning", Boolean.class)
    """
    Whether patrols should naturally spawn.
    """
    DO_TRADER_SPAWNING = GameRule<>("doTraderSpawning", Boolean.class)
    """
    Whether traders should naturally spawn.
    """
    DO_WARDEN_SPAWNING = GameRule<>("doWardenSpawning", Boolean.class)
    """
    Whether wardens should naturally spawn.
    """
    FORGIVE_DEAD_PLAYERS = GameRule<>("forgiveDeadPlayers", Boolean.class)
    """
    Whether mobs should cease being angry at a player once they die.
    """
    UNIVERSAL_ANGER = GameRule<>("universalAnger", Boolean.class)
    """
    Whether mobs will target all player entities once angered.
    """
    BLOCK_EXPLOSION_DROP_DECAY = GameRule<>("blockExplosionDropDecay", Boolean.class)
    """
    Whether block explosions will destroy dropped items.
    """
    MOB_EXPLOSION_DROP_DECAY = GameRule<>("mobExplosionDropDecay", Boolean.class)
    """
    * Whether mob explosions will destroy dropped items.
    """
    TNT_EXPLOSION_DROP_DECAY = GameRule<>("tntExplosionDropDecay", Boolean.class)
    """
    Whether tnt explosions will destroy dropped items.
    """
    WATER_SOURCE_CONVERSION = GameRule<>("waterSourceConversion", Boolean.class)
    """
    Whether water blocks can convert into water source blocks.
    """
    LAVA_SOURCE_CONVERSION = GameRule<>("lavaSourceConversion", Boolean.class)
    """
    Whether lava blocks can convert into lava source blocks.
    """
    GLOBAL_SOUND_EVENTS = GameRule<>("globalSoundEvents", Boolean.class)
    """
    Whether global level events such as ender dragon, wither, and completed
    end portal effects will propagate across the entire server.
    """
    DO_VINES_SPREAD = GameRule<>("doVinesSpread", Boolean.class)
    """
    Whether vines will spread.
    """
    ENDER_PEARLS_VANISH_ON_DEATH = GameRule<>("enderPearlsVanishOnDeath", Boolean.class)
    """
    Whether ender pearls will vanish on player death.
    """
    RANDOM_TICK_SPEED = GameRule<>("randomTickSpeed", Integer.class)
    """
    How often a random block tick occurs (such as plant growth, leaf decay,
    etc.) per chunk section per game tick. 0 will disable random ticks,
    higher numbers will increase random ticks.
    """
    SPAWN_RADIUS = GameRule<>("spawnRadius", Integer.class)
    """
    The number of blocks outward from the world spawn coordinates that a
    player will spawn in when first joining a server or when dying without a
    spawnpoint.
    """
    MAX_ENTITY_CRAMMING = GameRule<>("maxEntityCramming", Integer.class)
    """
    The maximum number of other pushable entities a mob or player can push,
    before taking suffocation damage.
    
    Setting to 0 disables this rule.
    """
    MAX_COMMAND_CHAIN_LENGTH = GameRule<>("maxCommandChainLength", Integer.class)
    """
    Determines the number at which the chain of command blocks act as a
    "chain."
    
    This is the maximum amount of command blocks that can be activated in a
    single tick from a single chain.
    """
    MAX_COMMAND_FORK_COUNT = GameRule<>("maxCommandForkCount", Integer.class)
    """
    Determines the number of different commands/functions which execute
    commands can fork into.
    """
    COMMAND_MODIFICATION_BLOCK_LIMIT = GameRule<>("commandModificationBlockLimit", Integer.class)
    """
    Determines the maximum number of blocks which a command can modify.
    """
    PLAYERS_SLEEPING_PERCENTAGE = GameRule<>("playersSleepingPercentage", Integer.class)
    """
    The percentage of online players which must be sleeping for the night to
    advance.
    """
    SNOW_ACCUMULATION_HEIGHT = GameRule<>("snowAccumulationHeight", Integer.class)
    PLAYERS_NETHER_PORTAL_DEFAULT_DELAY = GameRule<>("playersNetherPortalDefaultDelay", Integer.class)
    """
    The amount of time a player must stand in a nether portal before the
    portal activates.
    """
    PLAYERS_NETHER_PORTAL_CREATIVE_DELAY = GameRule<>("playersNetherPortalCreativeDelay", Integer.class)
    """
    The amount of time a player in creative mode must stand in a nether
    portal before the portal activates.
    """
    MINECART_MAX_SPEED = GameRule<>("minecartMaxSpeed", Integer.class)
    """
    The maximum speed of minecarts (when the new movement algorithm is
    enabled).
    """
    SPAWN_CHUNK_RADIUS = GameRule<>("spawnChunkRadius", Integer.class)
    """
    The number of chunks around spawn which will be kept loaded at all times.
    """


    def getName(self) -> str:
        """
        Get the name of this GameRule.

        Returns
        - the name of this GameRule
        """
        ...


    def getType(self) -> type["T"]:
        """
        Get the type of this rule.

        Returns
        - the rule type; Integer or Boolean
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def getByName(rule: str) -> "GameRule"[Any]:
        """
        Get a GameRule by its name.

        Arguments
        - rule: the name of the GameRule

        Returns
        - the GameRule or null if no GameRule matches the given
        name
        """
        ...


    @staticmethod
    def values() -> list["GameRule"[Any]]:
        """
        Get an immutable collection of GameRules.

        Returns
        - an immutable collection containing all registered GameRules.
        """
        ...
