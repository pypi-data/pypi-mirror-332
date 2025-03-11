"""
Python module generated from Java source file org.bukkit.ServerTickManager

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.entity import Entity
from typing import Any, Callable, Iterable, Tuple


class ServerTickManager:
    """
    Manages ticking within a server.
    
    To learn more about the features surrounding this interface.

    See
    - <a href="https://minecraft.wiki/w/Commands/tick">Tick Command</a>
    """

    def isRunningNormally(self) -> bool:
        """
        Checks if the server is running normally.
        
        When the server is running normally it indicates that the server is not
        currently frozen.

        Returns
        - True if the server is running normally, otherwise False
        """
        ...


    def isStepping(self) -> bool:
        """
        Checks if the server is currently stepping.

        Returns
        - True if stepping, otherwise False
        """
        ...


    def isSprinting(self) -> bool:
        """
        Checks if the server is currently sprinting.

        Returns
        - True if sprinting, otherwise False
        """
        ...


    def isFrozen(self) -> bool:
        """
        Checks if the server is currently frozen.

        Returns
        - True if the server is frozen, otherwise False
        """
        ...


    def getTickRate(self) -> float:
        """
        Gets the current tick rate of the server.

        Returns
        - the current tick rate of the server
        """
        ...


    def setTickRate(self, tick: float) -> None:
        """
        Sets the tick rate of the server.
        
        The normal tick rate of the server is 20. No tick rate below 1.0F or
        above 10,000 can be applied to the server.

        Arguments
        - tick: the tick rate to set the server to

        Raises
        - IllegalArgumentException: if tick rate is too low or too high for
        the server to handle
        """
        ...


    def setFrozen(self, frozen: bool) -> None:
        """
        Sets the server to a frozen state that does not tick most things.

        Arguments
        - frozen: True to freeze the server, otherwise False
        """
        ...


    def stepGameIfFrozen(self, ticks: int) -> bool:
        """
        Steps the game a certain amount of ticks if the server is currently
        frozen.
        
        Steps occur when the server is in a frozen state which can be started by
        either using the in game /tick freeze command or the
        .setFrozen(boolean) method.

        Arguments
        - ticks: the amount of ticks to step the game for

        Returns
        - True if the game is now stepping. False if the game is not frozen
        so the request could not be fulfilled.
        """
        ...


    def stopStepping(self) -> bool:
        """
        Stops the current stepping if stepping is occurring.

        Returns
        - True if the game is no-longer stepping. False if the server was
        not stepping or was already done stepping.
        """
        ...


    def requestGameToSprint(self, ticks: int) -> bool:
        """
        Attempts to initiate a sprint, which executes all server ticks at a
        faster rate then normal.

        Arguments
        - ticks: the amount of ticks to sprint for

        Returns
        - True if a sprint was already initiated and was stopped, otherwise
        False
        """
        ...


    def stopSprinting(self) -> bool:
        """
        Stops the current sprint if one is currently happening.

        Returns
        - True if the game is no-longer sprinting, False if the server was
        not sprinting or was already done sprinting
        """
        ...


    def isFrozen(self, entity: "Entity") -> bool:
        """
        Checks if a given entity is frozen.

        Arguments
        - entity: the entity to check if frozen.

        Returns
        - True if the entity is currently frozen otherwise False.
        """
        ...


    def getFrozenTicksToRun(self) -> int:
        """
        Gets the amount of frozen ticks left to run.

        Returns
        - the amount of frozen ticks left to run
        """
        ...
