"""
Python module generated from Java source file org.bukkit.scheduler.BukkitScheduler

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import Callable
from java.util.concurrent import Future
from java.util.function import Consumer
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import *
from typing import Any, Callable, Iterable, Tuple


class BukkitScheduler:

    def scheduleSyncDelayedTask(self, plugin: "Plugin", task: "Runnable", delay: int) -> int:
        """
        Schedules a once off task to occur after a delay.
        
        This task will be executed by the main server thread.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing task

        Returns
        - Task id number (-1 if scheduling failed)
        """
        ...


    def scheduleSyncDelayedTask(self, plugin: "Plugin", task: "BukkitRunnable", delay: int) -> int:
        """
        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing task

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - Use BukkitRunnable.runTaskLater(Plugin, long)
        """
        ...


    def scheduleSyncDelayedTask(self, plugin: "Plugin", task: "Runnable") -> int:
        """
        Schedules a once off task to occur as soon as possible.
        
        This task will be executed by the main server thread.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed

        Returns
        - Task id number (-1 if scheduling failed)
        """
        ...


    def scheduleSyncDelayedTask(self, plugin: "Plugin", task: "BukkitRunnable") -> int:
        """
        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - Use BukkitRunnable.runTask(Plugin)
        """
        ...


    def scheduleSyncRepeatingTask(self, plugin: "Plugin", task: "Runnable", delay: int, period: int) -> int:
        """
        Schedules a repeating task.
        
        This task will be executed by the main server thread.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing first repeat
        - period: Period in server ticks of the task

        Returns
        - Task id number (-1 if scheduling failed)
        """
        ...


    def scheduleSyncRepeatingTask(self, plugin: "Plugin", task: "BukkitRunnable", delay: int, period: int) -> int:
        """
        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing first repeat
        - period: Period in server ticks of the task

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - Use BukkitRunnable.runTaskTimer(Plugin, long, long)
        """
        ...


    def scheduleAsyncDelayedTask(self, plugin: "Plugin", task: "Runnable", delay: int) -> int:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules a once off task to occur after a delay. This task will be
        executed by a thread managed by the scheduler.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing task

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - This name is misleading, as it does not schedule "a sync"
            task, but rather, "an async" task
        """
        ...


    def scheduleAsyncDelayedTask(self, plugin: "Plugin", task: "Runnable") -> int:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules a once off task to occur as soon as possible. This task will
        be executed by a thread managed by the scheduler.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - This name is misleading, as it does not schedule "a sync"
            task, but rather, "an async" task
        """
        ...


    def scheduleAsyncRepeatingTask(self, plugin: "Plugin", task: "Runnable", delay: int, period: int) -> int:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Schedules a repeating task. This task will be executed by a thread
        managed by the scheduler.

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed
        - delay: Delay in server ticks before executing first repeat
        - period: Period in server ticks of the task

        Returns
        - Task id number (-1 if scheduling failed)

        Deprecated
        - This name is misleading, as it does not schedule "a sync"
            task, but rather, "an async" task
        """
        ...


    def callSyncMethod(self, plugin: "Plugin", task: "Callable"["T"]) -> "Future"["T"]:
        """
        Calls a method on the main thread and returns a Future object. This
        task will be executed by the main server thread.
        
        - Note: The Future.get() methods must NOT be called from the main
            thread.
        - Note2: There is at least an average of 10ms latency until the
            isDone() method returns True.
        
        
        Type `<T>`: The callable's return type

        Arguments
        - plugin: Plugin that owns the task
        - task: Task to be executed

        Returns
        - Future Future object related to the task
        """
        ...


    def cancelTask(self, taskId: int) -> None:
        """
        Removes task from scheduler.

        Arguments
        - taskId: Id number of task to be removed
        """
        ...


    def cancelTasks(self, plugin: "Plugin") -> None:
        """
        Removes all tasks associated with a particular plugin from the
        scheduler.

        Arguments
        - plugin: Owner of tasks to be removed
        """
        ...


    def isCurrentlyRunning(self, taskId: int) -> bool:
        """
        Check if the task currently running.
        
        A repeating task might not be running currently, but will be running in
        the future. A task that has finished, and does not repeat, will not be
        running ever again.
        
        Explicitly, a task is running if there exists a thread for it, and that
        thread is alive.

        Arguments
        - taskId: The task to check.

        Returns
        - If the task is currently running.
        """
        ...


    def isQueued(self, taskId: int) -> bool:
        """
        Check if the task queued to be run later.
        
        If a repeating task is currently running, it might not be queued now
        but could be in the future. A task that is not queued, and not running,
        will not be queued again.

        Arguments
        - taskId: The task to check.

        Returns
        - If the task is queued to be run.
        """
        ...


    def getActiveWorkers(self) -> list["BukkitWorker"]:
        """
        Returns a list of all active workers.
        
        This list contains asynch tasks that are being executed by separate
        threads.

        Returns
        - Active workers
        """
        ...


    def getPendingTasks(self) -> list["BukkitTask"]:
        """
        Returns a list of all pending tasks. The ordering of the tasks is not
        related to their order of execution.

        Returns
        - Active workers
        """
        ...


    def runTask(self, plugin: "Plugin", task: "Runnable") -> "BukkitTask":
        """
        Returns a task that will run on the next server tick.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTask(self, plugin: "Plugin", task: "Consumer"["BukkitTask"]) -> None:
        """
        Returns a task that will run on the next server tick.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTask(self, plugin: "Plugin", task: "BukkitRunnable") -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTask(Plugin)
        """
        ...


    def runTaskAsynchronously(self, plugin: "Plugin", task: "Runnable") -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will run asynchronously.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskAsynchronously(self, plugin: "Plugin", task: "Consumer"["BukkitTask"]) -> None:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will run asynchronously.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskAsynchronously(self, plugin: "Plugin", task: "BukkitRunnable") -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTaskAsynchronously(Plugin)
        """
        ...


    def runTaskLater(self, plugin: "Plugin", task: "Runnable", delay: int) -> "BukkitTask":
        """
        Returns a task that will run after the specified number of server
        ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskLater(self, plugin: "Plugin", task: "Consumer"["BukkitTask"], delay: int) -> None:
        """
        Returns a task that will run after the specified number of server
        ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskLater(self, plugin: "Plugin", task: "BukkitRunnable", delay: int) -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTaskLater(Plugin, long)
        """
        ...


    def runTaskLaterAsynchronously(self, plugin: "Plugin", task: "Runnable", delay: int) -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will run asynchronously after the specified number
        of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskLaterAsynchronously(self, plugin: "Plugin", task: "Consumer"["BukkitTask"], delay: int) -> None:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will run asynchronously after the specified number
        of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskLaterAsynchronously(self, plugin: "Plugin", task: "BukkitRunnable", delay: int) -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTaskLaterAsynchronously(Plugin, long)
        """
        ...


    def runTaskTimer(self, plugin: "Plugin", task: "Runnable", delay: int, period: int) -> "BukkitTask":
        """
        Returns a task that will repeatedly run until cancelled, starting after
        the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskTimer(self, plugin: "Plugin", task: "Consumer"["BukkitTask"], delay: int, period: int) -> None:
        """
        Returns a task that will repeatedly run until cancelled, starting after
        the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task
        - period: the ticks to wait between runs

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskTimer(self, plugin: "Plugin", task: "BukkitRunnable", delay: int, period: int) -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTaskTimer(Plugin, long, long)
        """
        ...


    def runTaskTimerAsynchronously(self, plugin: "Plugin", task: "Runnable", delay: int, period: int) -> "BukkitTask":
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will repeatedly run asynchronously until cancelled,
        starting after the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task for the first
            time
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskTimerAsynchronously(self, plugin: "Plugin", task: "Consumer"["BukkitTask"], delay: int, period: int) -> None:
        """
        **Asynchronous tasks should never access any API in Bukkit.** **Great care
        should be taken to assure the thread-safety of asynchronous tasks.**
        
        Returns a task that will repeatedly run asynchronously until cancelled,
        starting after the specified number of server ticks.

        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task for the first
            time
        - period: the ticks to wait between runs

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null
        """
        ...


    def runTaskTimerAsynchronously(self, plugin: "Plugin", task: "BukkitRunnable", delay: int, period: int) -> "BukkitTask":
        """
        Arguments
        - plugin: the reference to the plugin scheduling task
        - task: the task to be run
        - delay: the ticks to wait before running the task for the first
            time
        - period: the ticks to wait between runs

        Returns
        - a BukkitTask that contains the id number

        Raises
        - IllegalArgumentException: if plugin is null
        - IllegalArgumentException: if task is null

        Deprecated
        - Use BukkitRunnable.runTaskTimerAsynchronously(Plugin, long, long)
        """
        ...
