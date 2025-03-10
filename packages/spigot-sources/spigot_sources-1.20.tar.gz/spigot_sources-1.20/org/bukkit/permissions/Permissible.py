"""
Python module generated from Java source file org.bukkit.permissions.Permissible

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.permissions import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class Permissible(ServerOperator):
    """
    Represents an object that may be assigned permissions
    """

    def isPermissionSet(self, name: str) -> bool:
        """
        Checks if this object contains an override for the specified
        permission, by fully qualified name

        Arguments
        - name: Name of the permission

        Returns
        - True if the permission is set, otherwise False
        """
        ...


    def isPermissionSet(self, perm: "Permission") -> bool:
        """
        Checks if this object contains an override for the specified Permission

        Arguments
        - perm: Permission to check

        Returns
        - True if the permission is set, otherwise False
        """
        ...


    def hasPermission(self, name: str) -> bool:
        """
        Gets the value of the specified permission, if set.
        
        If a permission override is not set on this object, the default value
        of the permission will be returned.

        Arguments
        - name: Name of the permission

        Returns
        - Value of the permission
        """
        ...


    def hasPermission(self, perm: "Permission") -> bool:
        """
        Gets the value of the specified permission, if set.
        
        If a permission override is not set on this object, the default value
        of the permission will be returned

        Arguments
        - perm: Permission to get

        Returns
        - Value of the permission
        """
        ...


    def addAttachment(self, plugin: "Plugin", name: str, value: bool) -> "PermissionAttachment":
        """
        Adds a new PermissionAttachment with a single permission by
        name and value

        Arguments
        - plugin: Plugin responsible for this attachment, may not be null
            or disabled
        - name: Name of the permission to attach
        - value: Value of the permission

        Returns
        - The PermissionAttachment that was just created
        """
        ...


    def addAttachment(self, plugin: "Plugin") -> "PermissionAttachment":
        """
        Adds a new empty PermissionAttachment to this object

        Arguments
        - plugin: Plugin responsible for this attachment, may not be null
            or disabled

        Returns
        - The PermissionAttachment that was just created
        """
        ...


    def addAttachment(self, plugin: "Plugin", name: str, value: bool, ticks: int) -> "PermissionAttachment":
        """
        Temporarily adds a new PermissionAttachment with a single
        permission by name and value

        Arguments
        - plugin: Plugin responsible for this attachment, may not be null
            or disabled
        - name: Name of the permission to attach
        - value: Value of the permission
        - ticks: Amount of ticks to automatically remove this attachment
            after

        Returns
        - The PermissionAttachment that was just created
        """
        ...


    def addAttachment(self, plugin: "Plugin", ticks: int) -> "PermissionAttachment":
        """
        Temporarily adds a new empty PermissionAttachment to this
        object

        Arguments
        - plugin: Plugin responsible for this attachment, may not be null
            or disabled
        - ticks: Amount of ticks to automatically remove this attachment
            after

        Returns
        - The PermissionAttachment that was just created
        """
        ...


    def removeAttachment(self, attachment: "PermissionAttachment") -> None:
        """
        Removes the given PermissionAttachment from this object

        Arguments
        - attachment: Attachment to remove

        Raises
        - IllegalArgumentException: Thrown when the specified attachment
            isn't part of this object
        """
        ...


    def recalculatePermissions(self) -> None:
        """
        Recalculates the permissions for this object, if the attachments have
        changed values.
        
        This should very rarely need to be called from a plugin.
        """
        ...


    def getEffectivePermissions(self) -> set["PermissionAttachmentInfo"]:
        """
        Gets a set containing all of the permissions currently in effect by
        this object

        Returns
        - Set of currently effective permissions
        """
        ...
