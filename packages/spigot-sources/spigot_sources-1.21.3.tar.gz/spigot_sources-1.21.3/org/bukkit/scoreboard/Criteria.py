"""
Python module generated from Java source file org.bukkit.scoreboard.Criteria

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit import Statistic
from org.bukkit.Statistic import Type
from org.bukkit.entity import EntityType
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class Criteria:
    """
    Represents a scoreboard criteria, either custom or built-in to the Minecraft server, used to
    keep track of and manually or automatically change scores on a scoreboard.
    
    While this class outlines constants for standard criteria, see .statistic(Statistic)
    (and its overloads) to create instances for statistically-backed criteria.
    """

    DUMMY = Bukkit.getScoreboardCriteria("dummy")
    """
    The dummy criteria. Not changed by the server.
    """
    TRIGGER = Bukkit.getScoreboardCriteria("trigger")
    """
    The trigger criteria. Changed when a player runs the /trigger command for an objective.
    """
    DEATH_COUNT = Bukkit.getScoreboardCriteria("deathCount")
    """
    Increments automatically when a player dies.
    """
    PLAYER_KILL_COUNT = Bukkit.getScoreboardCriteria("playerKillCount")
    """
    Increments automatically when a player kills another player.
    """
    TOTAL_KILL_COUNT = Bukkit.getScoreboardCriteria("totalKillCount")
    """
    Increments automatically when a player kills another living entity.
    """
    HEALTH = Bukkit.getScoreboardCriteria("health")
    """
    Mirrors the player's health points (0 for no health, 20 for maximum default health).
    """
    FOOD = Bukkit.getScoreboardCriteria("food")
    """
    Mirrors the player's food points (0 for no food, 20 for maximum food).
    """
    AIR = Bukkit.getScoreboardCriteria("air")
    """
    Mirrors the player's air supply (0 for no air, 300 for maximum air).
    """
    ARMOR = Bukkit.getScoreboardCriteria("armor")
    """
    Mirrors the player's armor points (0 for no armor, 20 for maximum armor).
    """
    XP = Bukkit.getScoreboardCriteria("xp")
    """
    Mirrors the player's experience points.
    """
    LEVEL = Bukkit.getScoreboardCriteria("level")
    """
    Mirrors the player's experience level.
    """
    TEAM_KILL_BLACK = Bukkit.getScoreboardCriteria("teamkill.black")
    """
    Increments automatically when a player kills another player on the black team.
    """
    TEAM_KILL_DARK_BLUE = Bukkit.getScoreboardCriteria("teamkill.dark_blue")
    """
    Increments automatically when a player kills another player on the dark blue team.
    """
    TEAM_KILL_DARK_GREEN = Bukkit.getScoreboardCriteria("teamkill.dark_green")
    """
    Increments automatically when a player kills another player on the dark green team.
    """
    TEAM_KILL_DARK_AQUA = Bukkit.getScoreboardCriteria("teamkill.dark_aqua")
    """
    Increments automatically when a player kills another player on the dark aqua team.
    """
    TEAM_KILL_DARK_RED = Bukkit.getScoreboardCriteria("teamkill.dark_red")
    """
    Increments automatically when a player kills another player on the dark red team.
    """
    TEAM_KILL_DARK_PURPLE = Bukkit.getScoreboardCriteria("teamkill.dark_purple")
    """
    Increments automatically when a player kills another player on the dark purple team.
    """
    TEAM_KILL_GOLD = Bukkit.getScoreboardCriteria("teamkill.gold")
    """
    Increments automatically when a player kills another player on the gold team.
    """
    TEAM_KILL_GRAY = Bukkit.getScoreboardCriteria("teamkill.gray")
    """
    Increments automatically when a player kills another player on the gray team.
    """
    TEAM_KILL_DARK_GRAY = Bukkit.getScoreboardCriteria("teamkill.dark_gray")
    """
    Increments automatically when a player kills another player on the dark gray team.
    """
    TEAM_KILL_BLUE = Bukkit.getScoreboardCriteria("teamkill.blue")
    """
    Increments automatically when a player kills another player on the blue team.
    """
    TEAM_KILL_GREEN = Bukkit.getScoreboardCriteria("teamkill.green")
    """
    Increments automatically when a player kills another player on the green team.
    """
    TEAM_KILL_AQUA = Bukkit.getScoreboardCriteria("teamkill.aqua")
    """
    Increments automatically when a player kills another player on the aqua team.
    """
    TEAM_KILL_RED = Bukkit.getScoreboardCriteria("teamkill.red")
    """
    Increments automatically when a player kills another player on the red team.
    """
    TEAM_KILL_LIGHT_PURPLE = Bukkit.getScoreboardCriteria("teamkill.light_purple")
    """
    Increments automatically when a player kills another player on the light purple team.
    """
    TEAM_KILL_YELLOW = Bukkit.getScoreboardCriteria("teamkill.yellow")
    """
    Increments automatically when a player kills another player on the yellow team.
    """
    TEAM_KILL_WHITE = Bukkit.getScoreboardCriteria("teamkill.white")
    """
    Increments automatically when a player kills another player on the white team.
    """
    KILLED_BY_TEAM_BLACK = Bukkit.getScoreboardCriteria("killedByTeam.black")
    """
    Increments automatically when a player is killed by a player on the black team.
    """
    KILLED_BY_TEAM_DARK_BLUE = Bukkit.getScoreboardCriteria("killedByTeam.dark_blue")
    """
    Increments automatically when a player is killed by a player on the dark blue team.
    """
    KILLED_BY_TEAM_DARK_GREEN = Bukkit.getScoreboardCriteria("killedByTeam.dark_green")
    """
    Increments automatically when a player is killed by a player on the dark green team.
    """
    KILLED_BY_TEAM_DARK_AQUA = Bukkit.getScoreboardCriteria("killedByTeam.dark_aqua")
    """
    Increments automatically when a player is killed by a player on the dark aqua team.
    """
    KILLED_BY_TEAM_DARK_RED = Bukkit.getScoreboardCriteria("killedByTeam.dark_red")
    """
    Increments automatically when a player is killed by a player on the dark red team.
    """
    KILLED_BY_TEAM_DARK_PURPLE = Bukkit.getScoreboardCriteria("killedByTeam.dark_purple")
    """
    Increments automatically when a player is killed by a player on the dark purple team.
    """
    KILLED_BY_TEAM_GOLD = Bukkit.getScoreboardCriteria("killedByTeam.gold")
    """
    Increments automatically when a player is killed by a player on the gold team.
    """
    KILLED_BY_TEAM_GRAY = Bukkit.getScoreboardCriteria("killedByTeam.gray")
    """
    Increments automatically when a player is killed by a player on the gray team.
    """
    KILLED_BY_TEAM_DARK_GRAY = Bukkit.getScoreboardCriteria("killedByTeam.dark_gray")
    """
    Increments automatically when a player is killed by a player on the dark gray team.
    """
    KILLED_BY_TEAM_BLUE = Bukkit.getScoreboardCriteria("killedByTeam.blue")
    """
    Increments automatically when a player is killed by a player on the blue team.
    """
    KILLED_BY_TEAM_GREEN = Bukkit.getScoreboardCriteria("killedByTeam.green")
    """
    Increments automatically when a player is killed by a player on the green team.
    """
    KILLED_BY_TEAM_AQUA = Bukkit.getScoreboardCriteria("killedByTeam.aqua")
    """
    Increments automatically when a player is killed by a player on the aqua team.
    """
    KILLED_BY_TEAM_RED = Bukkit.getScoreboardCriteria("killedByTeam.red")
    """
    Increments automatically when a player is killed by a player on the red team.
    """
    KILLED_BY_TEAM_LIGHT_PURPLE = Bukkit.getScoreboardCriteria("killedByTeam.light_purple")
    """
    Increments automatically when a player is killed by a player on the light purple team.
    """
    KILLED_BY_TEAM_YELLOW = Bukkit.getScoreboardCriteria("killedByTeam.yellow")
    """
    Increments automatically when a player is killed by a player on the yellow team.
    """
    KILLED_BY_TEAM_WHITE = Bukkit.getScoreboardCriteria("killedByTeam.white")
    """
    Increments automatically when a player is killed by a player on the white team.
    """


    def getName(self) -> str:
        """
        Get the name of this criteria (its unique id).

        Returns
        - the name
        """
        ...


    def isReadOnly(self) -> bool:
        """
        Get whether or not this criteria is read only. If read only, scoreboards with this criteria
        cannot have their scores changed.

        Returns
        - True if read only, False otherwise
        """
        ...


    def getDefaultRenderType(self) -> "RenderType":
        """
        Get the RenderType used by default for this criteria.

        Returns
        - the default render type
        """
        ...


    @staticmethod
    def statistic(statistic: "Statistic", material: "Material") -> "Criteria":
        """
        Get a Criteria for the specified statistic pertaining to blocks or items.
        
        This method expects a Statistic of Type.BLOCK or Type.ITEM and the
        Material matching said type (e.g. BLOCK statistics require materials where
        Material.isBlock() is True). This acts as a convenience to create more complex
        compound criteria such as those that increment on block breaks, or item uses. An example
        would be `Criteria.statistic(Statistic.CRAFT_ITEM, Material.STICK)`, returning a
        Criteria representing "minecraft.crafted:minecraft.stick" which will increment when the
        player crafts a stick.
        
        If the provided statistic does not require additional data, .statistic(Statistic)
        is called and returned instead.
        
        This method provides no guarantee that any given criteria exists on the vanilla server.

        Arguments
        - statistic: the statistic for which to get a criteria
        - material: the relevant material

        Returns
        - the criteria

        Raises
        - IllegalArgumentException: if Statistic.getType() is anything other than
        Type.BLOCK or Type.ITEM
        - IllegalArgumentException: if Statistic.getType() is Type.BLOCK, but
        Material.isBlock() is False
        - IllegalArgumentException: if Statistic.getType() is Type.ITEM, but
        Material.isItem() is False
        """
        ...


    @staticmethod
    def statistic(statistic: "Statistic", entityType: "EntityType") -> "Criteria":
        """
        Get a Criteria for the specified statistic pertaining to an entity type.
        
        This method expects a Statistic of Type.ENTITY. This acts as a convenience
        to create more complex compound criteria such as being killed by a specific entity type.
        An example would be `Criteria.statistic(Statistic.KILL_ENTITY, EntityType.CREEPER)`,
        returning a Criteria representing "minecraft.killed:minecraft.creeper" which will increment
        when the player kills a creepers.
        
        If the provided statistic does not require additional data, .statistic(Statistic)
        is called and returned instead.
        
        This method provides no guarantee that any given criteria exists on the vanilla server.

        Arguments
        - statistic: the statistic for which to get a criteria
        - entityType: the relevant entity type

        Returns
        - the criteria

        Raises
        - IllegalArgumentException: if Statistic.getType() is not Type.ENTITY
        """
        ...


    @staticmethod
    def statistic(statistic: "Statistic") -> "Criteria":
        """
        Get a Criteria for the specified statistic.
        
        An example would be `Criteria.statistic(Statistic.FLY_ONE_CM)`, returning a Criteria
        representing "minecraft.custom:minecraft.aviate_one_cm" which will increment when the player
        flies with an elytra.
        
        This method provides no guarantee that any given criteria exists on the vanilla server. All
        statistics are accepted, however some may not operate as expected if additional data is
        required. For block/item-related statistics, see .statistic(Statistic, Material),
        and for entity-related statistics, see .statistic(Statistic, EntityType)

        Arguments
        - statistic: the statistic for which to get a criteria

        Returns
        - the criteria
        """
        ...


    @staticmethod
    def create(name: str) -> "Criteria":
        """
        Get (or create) a new Criteria by its name.

        Arguments
        - name: the criteria name

        Returns
        - the created criteria
        """
        ...
