"""
Python module generated from Java source file org.bukkit.util.permissions.DefaultPermissions

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.bukkit.util.permissions import *
from typing import Any, Callable, Iterable, Tuple


class DefaultPermissions:

    @staticmethod
    def registerPermission(perm: "Permission") -> "Permission":
        ...


    @staticmethod
    def registerPermission(perm: "Permission", withLegacy: bool) -> "Permission":
        ...


    @staticmethod
    def registerPermission(perm: "Permission", parent: "Permission") -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str) -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str, parent: "Permission") -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str, def: "PermissionDefault") -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str, def: "PermissionDefault", parent: "Permission") -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str, def: "PermissionDefault", children: dict[str, "Boolean"]) -> "Permission":
        ...


    @staticmethod
    def registerPermission(name: str, desc: str, def: "PermissionDefault", children: dict[str, "Boolean"], parent: "Permission") -> "Permission":
        ...


    @staticmethod
    def registerCorePermissions() -> None:
        ...
