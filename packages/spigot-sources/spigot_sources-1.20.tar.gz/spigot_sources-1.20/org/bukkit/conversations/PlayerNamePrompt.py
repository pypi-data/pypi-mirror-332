"""
Python module generated from Java source file org.bukkit.conversations.PlayerNamePrompt

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PlayerNamePrompt(ValidatingPrompt):
    """
    PlayerNamePrompt is the base class for any prompt that requires the player
    to enter another player's name.
    """

    def __init__(self, plugin: "Plugin"):
        ...
