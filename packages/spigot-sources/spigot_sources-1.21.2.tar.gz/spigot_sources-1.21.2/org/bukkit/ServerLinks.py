"""
Python module generated from Java source file org.bukkit.ServerLinks

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.net import URI
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class ServerLinks:
    """
    Represents a collections of links which may be sent to a client.
    """

    def getLink(self, type: "Type") -> "ServerLink":
        """
        Gets the link of a given type, if it exists.

        Arguments
        - type: link type

        Returns
        - link or null
        """
        ...


    def getLinks(self) -> list["ServerLink"]:
        """
        Gets an immutable list of all links.

        Returns
        - immutable list
        """
        ...


    def setLink(self, type: "Type", url: "URI") -> "ServerLink":
        """
        Adds the given link, overwriting the first link of the same type if
        already set.

        Arguments
        - type: link type
        - url: link url

        Returns
        - the added link
        """
        ...


    def addLink(self, type: "Type", url: "URI") -> "ServerLink":
        """
        Adds the given link to the list of links.

        Arguments
        - type: link type
        - url: link url

        Returns
        - the added link
        """
        ...


    def addLink(self, displayName: str, url: "URI") -> "ServerLink":
        """
        Adds the given link to the list of links.

        Arguments
        - displayName: link name / display text
        - url: link url

        Returns
        - the added link
        """
        ...


    def removeLink(self, link: "ServerLink") -> bool:
        """
        Removes the given link.

        Arguments
        - link: the link to remove

        Returns
        - if the link existed and was removed
        """
        ...


    def copy(self) -> "ServerLinks":
        """
        Returns a copy of this link collection, unassociated from the server.

        Returns
        - copied links
        """
        ...


    class ServerLink:
        """
        Represents a server link.
        """

        def getType(self) -> "Type":
            """
            Gets the type of this link if it is a known special type.

            Returns
            - type or null
            """
            ...


        def getDisplayName(self) -> str:
            """
            Gets the display name/text of this link.

            Returns
            - display name
            """
            ...


        def getUrl(self) -> "URI":
            """
            Gets the url of this link.

            Returns
            - link url
            """
            ...


    class Type(Enum):
        """
        Represents a known type of link which will be translated by the client
        and may have special functionality.
        """

        REPORT_BUG = 0
        """
        Bug report links which may appear on disconnect/crash screens.
        """
        COMMUNITY_GUIDELINES = 1
        SUPPORT = 2
        STATUS = 3
        FEEDBACK = 4
        COMMUNITY = 5
        WEBSITE = 6
        FORUMS = 7
        NEWS = 8
        ANNOUNCEMENTS = 9
