"""
Python module generated from Java source file org.bukkit.packs.ResourcePack

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit.packs import *
from typing import Any, Callable, Iterable, Tuple


class ResourcePack:
    """
    Represents a resource pack.

    See
    - <a href="https://minecraft.wiki/w/Resource_pack">Minecraft wiki</a>
    """

    def getId(self) -> "UUID":
        """
        Gets the id of the resource pack.

        Returns
        - the id
        """
        ...


    def getUrl(self) -> str:
        """
        Gets the url of the resource pack.

        Returns
        - the url
        """
        ...


    def getHash(self) -> str:
        """
        Gets the hash of the resource pack.

        Returns
        - the hash
        """
        ...


    def getPrompt(self) -> str:
        """
        Gets the prompt to show of the resource pack.

        Returns
        - the prompt
        """
        ...


    def isRequired(self) -> bool:
        """
        Gets if the resource pack is required by the server.

        Returns
        - True if is required
        """
        ...
