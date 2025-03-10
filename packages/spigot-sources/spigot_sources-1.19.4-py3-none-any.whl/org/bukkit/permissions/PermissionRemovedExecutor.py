"""
Python module generated from Java source file org.bukkit.permissions.PermissionRemovedExecutor

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.permissions import *
from typing import Any, Callable, Iterable, Tuple


class PermissionRemovedExecutor:
    """
    Represents a class which is to be notified when a PermissionAttachment is removed from a Permissible
    """

    def attachmentRemoved(self, attachment: "PermissionAttachment") -> None:
        """
        Called when a PermissionAttachment is removed from a Permissible

        Arguments
        - attachment: Attachment which was removed
        """
        ...
