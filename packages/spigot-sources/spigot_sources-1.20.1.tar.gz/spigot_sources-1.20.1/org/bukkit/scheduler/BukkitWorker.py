"""
Python module generated from Java source file org.bukkit.scheduler.BukkitWorker

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import *
from typing import Any, Callable, Iterable, Tuple


class BukkitWorker:
    """
    Represents a worker thread for the scheduler. This gives information about
    the Thread object for the task, owner of the task and the taskId.
    
    Workers are used to execute async tasks.
    """

    def getTaskId(self) -> int:
        """
        Returns the taskId for the task being executed by this worker.

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


    def getThread(self) -> "Thread":
        """
        Returns the thread for the worker.

        Returns
        - The Thread object for the worker
        """
        ...
