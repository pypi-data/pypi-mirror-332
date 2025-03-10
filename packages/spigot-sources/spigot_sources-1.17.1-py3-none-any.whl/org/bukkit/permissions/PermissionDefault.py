"""
Python module generated from Java source file org.bukkit.permissions.PermissionDefault

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.permissions import *
from typing import Any, Callable, Iterable, Tuple


class PermissionDefault(Enum):
    """
    Represents the possible default values for permissions
    """

    TRUE = ("true")
    FALSE = ("false")
    OP = ("op", "isop", "operator", "isoperator", "admin", "isadmin")
    NOT_OP = ("!op", "notop", "!operator", "notoperator", "!admin", "notadmin")


    def getValue(self, op: bool) -> bool:
        """
        Calculates the value of this PermissionDefault for the given operator
        value

        Arguments
        - op: If the target is op

        Returns
        - True if the default should be True, or False
        """
        ...


    @staticmethod
    def getByName(name: str) -> "PermissionDefault":
        """
        Looks up a PermissionDefault by name

        Arguments
        - name: Name of the default

        Returns
        - Specified value, or null if not found
        """
        ...


    def toString(self) -> str:
        ...
