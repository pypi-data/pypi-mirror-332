"""
Python module generated from Java source file com.google.common.util.concurrent.ThreadFactoryBuilder

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Locale
from java.util.concurrent import Executors
from java.util.concurrent import ThreadFactory
from java.util.concurrent.atomic import AtomicLong
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ThreadFactoryBuilder:
    """
    A ThreadFactory builder, providing any combination of these features:
    
    
      - whether threads should be marked as Thread.setDaemon daemon threads
      - a ThreadFactoryBuilder.setNameFormat naming format
      - a Thread.setPriority thread priority
      - an Thread.setUncaughtExceptionHandler uncaught exception handler
      - a ThreadFactory.newThread backing thread factory
    
    
    If no backing thread factory is provided, a default backing thread factory is used as if by
    calling `setThreadFactory(`Executors.defaultThreadFactory()`)`.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 4.0
    """

    def __init__(self):
        """
        Creates a new ThreadFactory builder.
        """
        ...


    def setNameFormat(self, nameFormat: str) -> "ThreadFactoryBuilder":
        """
        Sets the naming format to use when naming threads (Thread.setName) which are created
        with this ThreadFactory.

        Arguments
        - nameFormat: a String.format(String, Object...)-compatible format String, to which
            a unique integer (0, 1, etc.) will be supplied as the single parameter. This integer will
            be unique to the built instance of the ThreadFactory and will be assigned sequentially. For
            example, `"rpc-pool-%d"` will generate thread names like `"rpc-pool-0"`, `"rpc-pool-1"`, `"rpc-pool-2"`, etc.

        Returns
        - this for the builder pattern
        """
        ...


    def setDaemon(self, daemon: bool) -> "ThreadFactoryBuilder":
        """
        Sets daemon or not for new threads created with this ThreadFactory.

        Arguments
        - daemon: whether or not new Threads created with this ThreadFactory will be daemon threads

        Returns
        - this for the builder pattern
        """
        ...


    def setPriority(self, priority: int) -> "ThreadFactoryBuilder":
        """
        Sets the priority for new threads created with this ThreadFactory.
        
        **Warning:** relying on the thread scheduler is <a
        href="http://errorprone.info/bugpattern/ThreadPriorityCheck">discouraged</a>.

        Arguments
        - priority: the priority for new Threads created with this ThreadFactory

        Returns
        - this for the builder pattern
        """
        ...


    def setUncaughtExceptionHandler(self, uncaughtExceptionHandler: "UncaughtExceptionHandler") -> "ThreadFactoryBuilder":
        """
        Sets the UncaughtExceptionHandler for new threads created with this ThreadFactory.

        Arguments
        - uncaughtExceptionHandler: the uncaught exception handler for new Threads created with
            this ThreadFactory

        Returns
        - this for the builder pattern
        """
        ...


    def setThreadFactory(self, backingThreadFactory: "ThreadFactory") -> "ThreadFactoryBuilder":
        """
        Sets the backing ThreadFactory for new threads created with this ThreadFactory. Threads
        will be created by invoking #newThread(Runnable) on this backing ThreadFactory.

        Arguments
        - backingThreadFactory: the backing ThreadFactory which will be delegated to during
            thread creation.

        Returns
        - this for the builder pattern

        See
        - MoreExecutors
        """
        ...


    def build(self) -> "ThreadFactory":
        """
        Returns a new thread factory using the options supplied during the building process. After
        building, it is still possible to change the options used to build the ThreadFactory and/or
        build again. State is not shared amongst built instances.

        Returns
        - the fully constructed ThreadFactory
        """
        ...
