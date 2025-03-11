"""
Python module generated from Java source file org.bukkit.registry.RegistryAware

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import *
from typing import Any, Callable, Iterable, Tuple


class RegistryAware:
    """
    Indicates that instances of a class may be registered to the server and have a key associated with them.

    See
    - Registry
    """

    def getKeyOrThrow(self) -> "NamespacedKey":
        """
        Gets the key of this instance if it is registered otherwise throws an error.
        
        This is a convenience method and plugins should always check .isRegistered() before using this method.

        Returns
        - the key with which this instance is registered.

        Raises
        - IllegalStateException: if this instance is not registered.

        See
        - Registry
        """
        ...


    def getKeyOrNull(self) -> "NamespacedKey":
        """
        Gets the key of this instance if it is registered otherwise returns `null`.

        Returns
        - the key with which this instance is registered or `null` if not registered.

        See
        - Registry
        """
        ...


    def isRegistered(self) -> bool:
        """
        Returns whether this instance is register in a registry and therefore has a key or not.

        Returns
        - True, if this instance is registered. Otherwise, False.

        See
        - Registry
        """
        ...
