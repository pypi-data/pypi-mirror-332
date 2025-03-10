"""
Python module generated from Java source file java.util.concurrent.ScheduledExecutorService

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class ScheduledExecutorService(ExecutorService):
    """
    An ExecutorService that can schedule commands to run after a given
    delay, or to execute periodically.
    
    The `schedule` methods create tasks with various delays
    and return a task object that can be used to cancel or check
    execution. The `scheduleAtFixedRate` and
    `scheduleWithFixedDelay` methods create and execute tasks
    that run periodically until cancelled.
    
    Commands submitted using the Executor.execute(Runnable)
    and ExecutorService `submit` methods are scheduled
    with a requested delay of zero. Zero and negative delays (but not
    periods) are also allowed in `schedule` methods, and are
    treated as requests for immediate execution.
    
    All `schedule` methods accept *relative* delays and
    periods as arguments, not absolute times or dates. It is a simple
    matter to transform an absolute time represented as a java.util.Date to the required form. For example, to schedule at
    a certain future `date`, you can use: `schedule(task,
    date.getTime() - System.currentTimeMillis(),
    TimeUnit.MILLISECONDS)`. Beware however that expiration of a
    relative delay need not coincide with the current `Date` at
    which the task is enabled due to network time synchronization
    protocols, clock drift, or other factors.
    
    The Executors class provides convenient factory methods for
    the ScheduledExecutorService implementations provided in this package.
    
    <h2>Usage Example</h2>
    
    Here is a class with a method that sets up a ScheduledExecutorService
    to beep every ten seconds for an hour:
    
    ``` `import static java.util.concurrent.TimeUnit.*;
    class BeeperControl {
      private final ScheduledExecutorService scheduler =
        Executors.newScheduledThreadPool(1);
    
      public void beepForAnHour() {
        Runnable beeper = () -> System.out.println("beep");
        ScheduledFuture<?> beeperHandle =
          scheduler.scheduleAtFixedRate(beeper, 10, 10, SECONDS);
        Runnable canceller = () -> beeperHandle.cancel(False);
        scheduler.schedule(canceller, 1, HOURS);`
    }}```

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def schedule(self, command: "Runnable", delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Submits a one-shot task that becomes enabled after the given delay.

        Arguments
        - command: the task to execute
        - delay: the time from now to delay execution
        - unit: the time unit of the delay parameter

        Returns
        - a ScheduledFuture representing pending completion of
                the task and whose `get()` method will return
                `null` upon completion

        Raises
        - RejectedExecutionException: if the task cannot be
                scheduled for execution
        - NullPointerException: if command or unit is null
        """
        ...


    def schedule(self, callable: "Callable"["V"], delay: int, unit: "TimeUnit") -> "ScheduledFuture"["V"]:
        """
        Submits a value-returning one-shot task that becomes enabled
        after the given delay.
        
        Type `<V>`: the type of the callable's result

        Arguments
        - callable: the function to execute
        - delay: the time from now to delay execution
        - unit: the time unit of the delay parameter

        Returns
        - a ScheduledFuture that can be used to extract result or cancel

        Raises
        - RejectedExecutionException: if the task cannot be
                scheduled for execution
        - NullPointerException: if callable or unit is null
        """
        ...


    def scheduleAtFixedRate(self, command: "Runnable", initialDelay: int, period: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Submits a periodic action that becomes enabled first after the
        given initial delay, and subsequently with the given period;
        that is, executions will commence after
        `initialDelay`, then `initialDelay + period`, then
        `initialDelay + 2 * period`, and so on.
        
        The sequence of task executions continues indefinitely until
        one of the following exceptional completions occur:
        
        - The task is Future.cancel explicitly cancelled
        via the returned future.
        - The executor terminates, also resulting in task cancellation.
        - An execution of the task throws an exception.  In this case
        calling Future.get() get on the returned future will throw
        ExecutionException, holding the exception as its cause.
        
        Subsequent executions are suppressed.  Subsequent calls to
        Future.isDone isDone() on the returned future will
        return `True`.
        
        If any execution of this task takes longer than its period, then
        subsequent executions may start late, but will not concurrently
        execute.

        Arguments
        - command: the task to execute
        - initialDelay: the time to delay first execution
        - period: the period between successive executions
        - unit: the time unit of the initialDelay and period parameters

        Returns
        - a ScheduledFuture representing pending completion of
                the series of repeated tasks.  The future's Future.get() get() method will never return normally,
                and will throw an exception upon task cancellation or
                abnormal termination of a task execution.

        Raises
        - RejectedExecutionException: if the task cannot be
                scheduled for execution
        - NullPointerException: if command or unit is null
        - IllegalArgumentException: if period less than or equal to zero
        """
        ...


    def scheduleWithFixedDelay(self, command: "Runnable", initialDelay: int, delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Submits a periodic action that becomes enabled first after the
        given initial delay, and subsequently with the given delay
        between the termination of one execution and the commencement of
        the next.
        
        The sequence of task executions continues indefinitely until
        one of the following exceptional completions occur:
        
        - The task is Future.cancel explicitly cancelled
        via the returned future.
        - The executor terminates, also resulting in task cancellation.
        - An execution of the task throws an exception.  In this case
        calling Future.get() get on the returned future will throw
        ExecutionException, holding the exception as its cause.
        
        Subsequent executions are suppressed.  Subsequent calls to
        Future.isDone isDone() on the returned future will
        return `True`.

        Arguments
        - command: the task to execute
        - initialDelay: the time to delay first execution
        - delay: the delay between the termination of one
        execution and the commencement of the next
        - unit: the time unit of the initialDelay and delay parameters

        Returns
        - a ScheduledFuture representing pending completion of
                the series of repeated tasks.  The future's Future.get() get() method will never return normally,
                and will throw an exception upon task cancellation or
                abnormal termination of a task execution.

        Raises
        - RejectedExecutionException: if the task cannot be
                scheduled for execution
        - NullPointerException: if command or unit is null
        - IllegalArgumentException: if delay less than or equal to zero
        """
        ...
