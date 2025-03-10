"""
Python module generated from Java source file org.bukkit.scheduler.BukkitRunnable

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import *
from typing import Any, Callable, Iterable, Tuple


class BukkitRunnable(Runnable):
    """
    This class is provided as an easy way to handle scheduling tasks.
    """

    def isCancelled(self) -> bool:
        """
        Returns True if this task has been cancelled.

        Returns
        - True if the task has been cancelled

        Raises
        - IllegalStateException: if task was not scheduled yet
        """
        ...


    def cancel(self) -> None:
        """
        Attempts to cancel this task.

        Raises
        - IllegalStateException: if task was not scheduled yet
        """
        ...


    def runTask(self, plugin: "Plugin") -> "BukkitTask":
        """
        Schedules this in the Bukkit scheduler to run on next tick.

        Arguments
        - plugin: the reference to the plugin scheduling task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTask(Plugin, Runnable)
        """
        ...


    def runTaskAsynchronously(self, plugin: "Plugin") -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit. Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules this in the Bukkit scheduler to run asynchronously.

        Arguments
        - plugin: the reference to the plugin scheduling task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTaskAsynchronously(Plugin, Runnable)
        """
        ...


    def runTaskLater(self, plugin: "Plugin", delay: int) -> "BukkitTask":
        """
        Schedules this to run after the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTaskLater(Plugin, Runnable, long)
        """
        ...


    def runTaskLaterAsynchronously(self, plugin: "Plugin", delay: int) -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit. Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules this to run asynchronously after the specified number of
        server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTaskLaterAsynchronously(Plugin, Runnable, long)
        """
        ...


    def runTaskTimer(self, plugin: "Plugin", delay: int, period: int) -> "BukkitTask":
        """
        Schedules this to repeatedly run until cancelled, starting after the
        specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - delay: the ticks to wait before running the task
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTaskTimer(Plugin, Runnable, long, long)
        """
        ...


    def runTaskTimerAsynchronously(self, plugin: "Plugin", delay: int, period: int) -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit. Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules this to repeatedly run asynchronously until cancelled,
        starting after the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - delay: the ticks to wait before running the task for the first
            time
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalStateException: if this was already scheduled

        See
        - BukkitScheduler.runTaskTimerAsynchronously(Plugin, Runnable, long,
            long)
        """
        ...


    def getTaskId(self) -> int:
        """
        Gets the task id for this runnable.

        Returns
        - the task id that this runnable was scheduled as

        Raises
        - IllegalStateException: if task was not scheduled yet
        """
        ...
