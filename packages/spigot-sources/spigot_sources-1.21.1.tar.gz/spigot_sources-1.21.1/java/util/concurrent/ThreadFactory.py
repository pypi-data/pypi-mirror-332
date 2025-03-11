"""
Python module generated from Java source file java.util.concurrent.ThreadFactory

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class ThreadFactory:
    """
    An object that creates new threads on demand.  Using thread factories
    removes hardwiring of calls to Thread.Thread(Runnable) new Thread,
    enabling applications to use special thread subclasses, priorities, etc.
    
    
    The simplest implementation of this interface is just:
    ``` `class SimpleThreadFactory implements ThreadFactory {
      public Thread newThread(Runnable r) {
        return new Thread(r);`
    }}```
    
    The Executors.defaultThreadFactory method provides a more
    useful simple implementation, that sets the created thread context
    to known values before returning it.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def newThread(self, r: "Runnable") -> "Thread":
        """
        Constructs a new `Thread`.  Implementations may also initialize
        priority, name, daemon status, `ThreadGroup`, etc.

        Arguments
        - r: a runnable to be executed by new thread instance

        Returns
        - constructed thread, or `null` if the request to
                create a thread is rejected
        """
        ...
