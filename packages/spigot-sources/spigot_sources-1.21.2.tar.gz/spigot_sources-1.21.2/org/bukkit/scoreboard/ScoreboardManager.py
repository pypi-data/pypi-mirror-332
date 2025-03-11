"""
Python module generated from Java source file org.bukkit.scoreboard.ScoreboardManager

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import WeakReference
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class ScoreboardManager:
    """
    Manager of Scoreboards
    """

    def getMainScoreboard(self) -> "Scoreboard":
        """
        Gets the primary Scoreboard controlled by the server.
        
        This Scoreboard is saved by the server, is affected by the /scoreboard
        command, and is the scoreboard shown by default to players.

        Returns
        - the default server scoreboard
        """
        ...


    def getNewScoreboard(self) -> "Scoreboard":
        """
        Gets a new Scoreboard to be tracked by the server. This scoreboard will
        be tracked as long as a reference is kept, either by a player or by a
        plugin.

        Returns
        - the registered Scoreboard

        See
        - WeakReference
        """
        ...
