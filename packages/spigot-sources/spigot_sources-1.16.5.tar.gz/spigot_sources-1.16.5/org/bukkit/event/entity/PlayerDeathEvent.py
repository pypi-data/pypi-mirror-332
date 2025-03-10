"""
Python module generated from Java source file org.bukkit.event.entity.PlayerDeathEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerDeathEvent(EntityDeathEvent):
    """
    Thrown whenever a Player dies
    """

    def __init__(self, player: "Player", drops: list["ItemStack"], droppedExp: int, deathMessage: str):
        ...


    def __init__(self, player: "Player", drops: list["ItemStack"], droppedExp: int, newExp: int, deathMessage: str):
        ...


    def __init__(self, player: "Player", drops: list["ItemStack"], droppedExp: int, newExp: int, newTotalExp: int, newLevel: int, deathMessage: str):
        ...


    def getEntity(self) -> "Player":
        ...


    def setDeathMessage(self, deathMessage: str) -> None:
        """
        Set the death message that will appear to everyone on the server.

        Arguments
        - deathMessage: Message to appear to other players on the server.
        """
        ...


    def getDeathMessage(self) -> str:
        """
        Get the death message that will appear to everyone on the server.

        Returns
        - Message to appear to other players on the server.
        """
        ...


    def getNewExp(self) -> int:
        """
        Gets how much EXP the Player should have at respawn.
        
        This does not indicate how much EXP should be dropped, please see
        .getDroppedExp() for that.

        Returns
        - New EXP of the respawned player
        """
        ...


    def setNewExp(self, exp: int) -> None:
        """
        Sets how much EXP the Player should have at respawn.
        
        This does not indicate how much EXP should be dropped, please see
        .setDroppedExp(int) for that.

        Arguments
        - exp: New EXP of the respawned player
        """
        ...


    def getNewLevel(self) -> int:
        """
        Gets the Level the Player should have at respawn.

        Returns
        - New Level of the respawned player
        """
        ...


    def setNewLevel(self, level: int) -> None:
        """
        Sets the Level the Player should have at respawn.

        Arguments
        - level: New Level of the respawned player
        """
        ...


    def getNewTotalExp(self) -> int:
        """
        Gets the Total EXP the Player should have at respawn.

        Returns
        - New Total EXP of the respawned player
        """
        ...


    def setNewTotalExp(self, totalExp: int) -> None:
        """
        Sets the Total EXP the Player should have at respawn.

        Arguments
        - totalExp: New Total EXP of the respawned player
        """
        ...


    def getKeepLevel(self) -> bool:
        """
        Gets if the Player should keep all EXP at respawn.
        
        This flag overrides other EXP settings

        Returns
        - True if Player should keep all pre-death exp
        """
        ...


    def setKeepLevel(self, keepLevel: bool) -> None:
        """
        Sets if the Player should keep all EXP at respawn.
        
        This overrides all other EXP settings
        
        **This doesn't prevent the EXP from dropping.
        .setDroppedExp(int) should be used stop the
        EXP from dropping.**

        Arguments
        - keepLevel: True to keep all current value levels
        """
        ...


    def setKeepInventory(self, keepInventory: bool) -> None:
        """
        Sets if the Player keeps inventory on death.
        
        **This doesn't prevent the items from dropping.
        `getDrops().clear()` should be used stop the
        items from dropping.**

        Arguments
        - keepInventory: True to keep the inventory
        """
        ...


    def getKeepInventory(self) -> bool:
        """
        Gets if the Player keeps inventory on death.

        Returns
        - True if the player keeps inventory on death
        """
        ...
