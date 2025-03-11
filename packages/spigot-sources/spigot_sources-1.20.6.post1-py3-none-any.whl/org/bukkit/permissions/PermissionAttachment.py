"""
Python module generated from Java source file org.bukkit.permissions.PermissionAttachment

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Locale
from org.bukkit.permissions import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PermissionAttachment:
    """
    Holds information about a permission attachment on a Permissible
    object
    """

    def __init__(self, plugin: "Plugin", permissible: "Permissible"):
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the plugin responsible for this attachment

        Returns
        - Plugin responsible for this permission attachment
        """
        ...


    def setRemovalCallback(self, ex: "PermissionRemovedExecutor") -> None:
        """
        Sets an object to be called for when this attachment is removed from a
        Permissible. May be null.

        Arguments
        - ex: Object to be called when this is removed
        """
        ...


    def getRemovalCallback(self) -> "PermissionRemovedExecutor":
        """
        Gets the class that was previously set to be called when this
        attachment was removed from a Permissible. May be null.

        Returns
        - Object to be called when this is removed
        """
        ...


    def getPermissible(self) -> "Permissible":
        """
        Gets the Permissible that this is attached to

        Returns
        - Permissible containing this attachment
        """
        ...


    def getPermissions(self) -> dict[str, "Boolean"]:
        """
        Gets a copy of all set permissions and values contained within this
        attachment.
        
        This map may be modified but will not affect the attachment, as it is a
        copy.

        Returns
        - Copy of all permissions and values expressed by this attachment
        """
        ...


    def setPermission(self, name: str, value: bool) -> None:
        """
        Sets a permission to the given value, by its fully qualified name

        Arguments
        - name: Name of the permission
        - value: New value of the permission
        """
        ...


    def setPermission(self, perm: "Permission", value: bool) -> None:
        """
        Sets a permission to the given value

        Arguments
        - perm: Permission to set
        - value: New value of the permission
        """
        ...


    def unsetPermission(self, name: str) -> None:
        """
        Removes the specified permission from this attachment.
        
        If the permission does not exist in this attachment, nothing will
        happen.

        Arguments
        - name: Name of the permission to remove
        """
        ...


    def unsetPermission(self, perm: "Permission") -> None:
        """
        Removes the specified permission from this attachment.
        
        If the permission does not exist in this attachment, nothing will
        happen.

        Arguments
        - perm: Permission to remove
        """
        ...


    def remove(self) -> bool:
        """
        Removes this attachment from its registered Permissible

        Returns
        - True if the permissible was removed successfully, False if it
            did not exist
        """
        ...
