"""
Python module generated from Java source file org.bukkit.permissions.PermissibleBase

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit.permissions import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PermissibleBase(Permissible):
    """
    Base Permissible for use in any Permissible object via proxy or extension
    """

    def __init__(self, opable: "ServerOperator"):
        ...


    def isOp(self) -> bool:
        ...


    def setOp(self, value: bool) -> None:
        ...


    def isPermissionSet(self, name: str) -> bool:
        ...


    def isPermissionSet(self, perm: "Permission") -> bool:
        ...


    def hasPermission(self, inName: str) -> bool:
        ...


    def hasPermission(self, perm: "Permission") -> bool:
        ...


    def addAttachment(self, plugin: "Plugin", name: str, value: bool) -> "PermissionAttachment":
        ...


    def addAttachment(self, plugin: "Plugin") -> "PermissionAttachment":
        ...


    def removeAttachment(self, attachment: "PermissionAttachment") -> None:
        ...


    def recalculatePermissions(self) -> None:
        ...


    def clearPermissions(self) -> None:
        ...


    def addAttachment(self, plugin: "Plugin", name: str, value: bool, ticks: int) -> "PermissionAttachment":
        ...


    def addAttachment(self, plugin: "Plugin", ticks: int) -> "PermissionAttachment":
        ...


    def getEffectivePermissions(self) -> set["PermissionAttachmentInfo"]:
        ...
