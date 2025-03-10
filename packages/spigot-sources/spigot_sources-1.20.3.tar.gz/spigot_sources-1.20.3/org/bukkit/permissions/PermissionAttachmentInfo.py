"""
Python module generated from Java source file org.bukkit.permissions.PermissionAttachmentInfo

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.permissions import *
from typing import Any, Callable, Iterable, Tuple


class PermissionAttachmentInfo:
    """
    Holds information on a permission and which PermissionAttachment
    provides it
    """

    def __init__(self, permissible: "Permissible", permission: str, attachment: "PermissionAttachment", value: bool):
        ...


    def getPermissible(self) -> "Permissible":
        """
        Gets the permissible this is attached to

        Returns
        - Permissible this permission is for
        """
        ...


    def getPermission(self) -> str:
        """
        Gets the permission being set

        Returns
        - Name of the permission
        """
        ...


    def getAttachment(self) -> "PermissionAttachment":
        """
        Gets the attachment providing this permission. This may be null for
        default permissions (usually parent permissions).

        Returns
        - Attachment
        """
        ...


    def getValue(self) -> bool:
        """
        Gets the value of this permission

        Returns
        - Value of the permission
        """
        ...
