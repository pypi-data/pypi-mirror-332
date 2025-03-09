"""
Python module generated from Java source file org.bukkit.help.HelpTopic

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import CommandSender
from org.bukkit.entity import Player
from org.bukkit.help import *
from typing import Any, Callable, Iterable, Tuple


class HelpTopic:
    """
    HelpTopic implementations are displayed to the user when the user uses the
    /help command.
    
    Custom implementations of this class can work at two levels. A simple
    implementation only needs to set the value of `name`, `shortText`, and `fullText` in the constructor. This base class will
    take care of the rest.
    
    Complex implementations can be created by overriding the behavior of all
    the methods in this class.
    """

    def canSee(self, player: "CommandSender") -> bool:
        """
        Determines if a Player is allowed to see this help topic.
        
        HelpTopic implementations should take server administrator wishes into
        account as set by the HelpTopic.amendCanSee(String) function.

        Arguments
        - player: The Player in question.

        Returns
        - True of the Player can see this help topic, False otherwise.
        """
        ...


    def amendCanSee(self, amendedPermission: str) -> None:
        """
        Allows the server administrator to override the permission required to
        see a help topic.
        
        HelpTopic implementations should take this into account when
        determining topic visibility on the HelpTopic.canSee(org.bukkit.command.CommandSender) function.

        Arguments
        - amendedPermission: The permission node the server administrator
            wishes to apply to this topic.
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this help topic.

        Returns
        - The topic name.
        """
        ...


    def getShortText(self) -> str:
        """
        Returns a brief description that will be displayed in the topic index.

        Returns
        - A brief topic description.
        """
        ...


    def getFullText(self, forWho: "CommandSender") -> str:
        """
        Returns the full description of this help topic that is displayed when
        the user requests this topic's details.
        
        The result will be paginated to properly fit the user's client.

        Arguments
        - forWho: The player or console requesting the full text. Useful
            for further security trimming the command's full text based on
            sub-permissions in custom implementations.

        Returns
        - A full topic description.
        """
        ...


    def amendTopic(self, amendedShortText: str, amendedFullText: str) -> None:
        """
        Allows the server admin (or another plugin) to add or replace the
        contents of a help topic.
        
        A null in either parameter will leave that part of the topic unchanged.
        In either amending parameter, the string <text> is replaced
        with the existing contents in the help topic. Use this to append or
        prepend additional content into an automatically generated help topic.

        Arguments
        - amendedShortText: The new topic short text to use, or null to
            leave alone.
        - amendedFullText: The new topic full text to use, or null to leave
            alone.
        """
        ...
