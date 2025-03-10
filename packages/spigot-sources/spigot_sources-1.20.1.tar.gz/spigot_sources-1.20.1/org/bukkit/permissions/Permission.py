"""
Python module generated from Java source file org.bukkit.permissions.Permission

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Bukkit
from org.bukkit.permissions import *
from org.bukkit.plugin import PluginManager
from typing import Any, Callable, Iterable, Tuple


class Permission:
    """
    Represents a unique permission that may be attached to a Permissible
    """

    DEFAULT_PERMISSION = PermissionDefault.OP


    def __init__(self, name: str):
        ...


    def __init__(self, name: str, description: str):
        ...


    def __init__(self, name: str, defaultValue: "PermissionDefault"):
        ...


    def __init__(self, name: str, description: str, defaultValue: "PermissionDefault"):
        ...


    def __init__(self, name: str, children: dict[str, "Boolean"]):
        ...


    def __init__(self, name: str, description: str, children: dict[str, "Boolean"]):
        ...


    def __init__(self, name: str, defaultValue: "PermissionDefault", children: dict[str, "Boolean"]):
        ...


    def __init__(self, name: str, description: str, defaultValue: "PermissionDefault", children: dict[str, "Boolean"]):
        ...


    def getName(self) -> str:
        """
        Returns the unique fully qualified name of this Permission

        Returns
        - Fully qualified name
        """
        ...


    def getChildren(self) -> dict[str, "Boolean"]:
        """
        Gets the children of this permission.
        
        If you change this map in any form, you must call .recalculatePermissibles() to recalculate all Permissibles

        Returns
        - Permission children
        """
        ...


    def getDefault(self) -> "PermissionDefault":
        """
        Gets the default value of this permission.

        Returns
        - Default value of this permission.
        """
        ...


    def setDefault(self, value: "PermissionDefault") -> None:
        """
        Sets the default value of this permission.
        
        This will not be saved to disk, and is a temporary operation until the
        server reloads permissions. Changing this default will cause all Permissibles that contain this permission to recalculate their
        permissions

        Arguments
        - value: The new default to set
        """
        ...


    def getDescription(self) -> str:
        """
        Gets a brief description of this permission, may be empty

        Returns
        - Brief description of this permission
        """
        ...


    def setDescription(self, value: str) -> None:
        """
        Sets the description of this permission.
        
        This will not be saved to disk, and is a temporary operation until the
        server reloads permissions.

        Arguments
        - value: The new description to set
        """
        ...


    def getPermissibles(self) -> set["Permissible"]:
        """
        Gets a set containing every Permissible that has this
        permission.
        
        This set cannot be modified.

        Returns
        - Set containing permissibles with this permission
        """
        ...


    def recalculatePermissibles(self) -> None:
        """
        Recalculates all Permissibles that contain this permission.
        
        This should be called after modifying the children, and is
        automatically called after modifying the default value
        """
        ...


    def addParent(self, name: str, value: bool) -> "Permission":
        """
        Adds this permission to the specified parent permission.
        
        If the parent permission does not exist, it will be created and
        registered.

        Arguments
        - name: Name of the parent permission
        - value: The value to set this permission to

        Returns
        - Parent permission it created or loaded
        """
        ...


    def addParent(self, perm: "Permission", value: bool) -> None:
        """
        Adds this permission to the specified parent permission.

        Arguments
        - perm: Parent permission to register with
        - value: The value to set this permission to
        """
        ...


    @staticmethod
    def loadPermissions(data: dict[Any, Any], error: str, def: "PermissionDefault") -> list["Permission"]:
        """
        Loads a list of Permissions from a map of data, usually used from
        retrieval from a yaml file.
        
        The data may contain a list of name:data, where the data contains the
        following keys:
        
        - default: Boolean True or False. If not specified, False.
        - children: `Map<String, Boolean>` of child permissions. If not
            specified, empty list.
        - description: Short string containing a very small description of
            this description. If not specified, empty string.

        Arguments
        - data: Map of permissions
        - error: An error message to show if a permission is invalid. May contain "%s" format tag, which will be replaced with the name of invalid permission.
        - def: Default permission value to use if missing

        Returns
        - Permission object
        """
        ...


    @staticmethod
    def loadPermission(name: str, data: dict[str, "Object"]) -> "Permission":
        """
        Loads a Permission from a map of data, usually used from retrieval from
        a yaml file.
        
        The data may contain the following keys:
        
        - default: Boolean True or False. If not specified, False.
        - children: `Map<String, Boolean>` of child permissions. If not
            specified, empty list.
        - description: Short string containing a very small description of
            this description. If not specified, empty string.

        Arguments
        - name: Name of the permission
        - data: Map of keys

        Returns
        - Permission object
        """
        ...


    @staticmethod
    def loadPermission(name: str, data: dict[Any, Any], def: "PermissionDefault", output: list["Permission"]) -> "Permission":
        """
        Loads a Permission from a map of data, usually used from retrieval from
        a yaml file.
        
        The data may contain the following keys:
        
        - default: Boolean True or False. If not specified, False.
        - children: `Map<String, Boolean>` of child permissions. If not
            specified, empty list.
        - description: Short string containing a very small description of
            this description. If not specified, empty string.

        Arguments
        - name: Name of the permission
        - data: Map of keys
        - def: Default permission value to use if not set
        - output: A list to append any created child-Permissions to, may be null

        Returns
        - Permission object
        """
        ...
