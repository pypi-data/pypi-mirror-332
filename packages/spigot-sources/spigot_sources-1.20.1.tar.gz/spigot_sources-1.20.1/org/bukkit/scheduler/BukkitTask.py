"""
Python module generated from Java source file org.bukkit.scheduler.BukkitTask

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import *
from typing import Any, Callable, Iterable, Tuple


class BukkitTask:
    """
    Represents a task being executed by the scheduler
    """

    def getTaskId(self) -> int:
        """
        Returns the taskId for the task.

        Returns
        - Task id number
        """
        ...


    def getOwner(self) -> "Plugin":
        """
        Returns the Plugin that owns this task.

        Returns
        - The Plugin that owns the task
        """
        ...


    def isSync(self) -> bool:
        """
        Returns True if the Task is a sync task.

        Returns
        - True if the task is run by main thread
        """
        ...


    def isCancelled(self) -> bool:
        """
        Returns True if this task has been cancelled.

        Returns
        - True if the task has been cancelled
        """
        ...


    def cancel(self) -> None:
        """
        Will attempt to cancel this task.
        """
        ...
