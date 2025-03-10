"""
Python module generated from Java source file com.google.common.base.internal.Finalizer

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base.internal import *
from java.lang.ref import PhantomReference
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import Method
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Finalizer(Runnable):
    """
    Thread that finalizes referents. All references should implement `com.google.common.base.FinalizableReference`.
    
    While this class is public, we consider it to be *internal* and not part of our published API.
    It is public so we can access it reflectively across class loaders in secure environments.
    
    This class can't depend on other Guava code. If we were to load this class in the same class
    loader as the rest of Guava, this thread would keep an indirect strong reference to the class
    loader and prevent it from being garbage collected. This poses a problem for environments where
    you want to throw away the class loader. For example, dynamically reloading a web application or
    unloading an OSGi bundle.
    
    `com.google.common.base.FinalizableReferenceQueue` loads this class in its own class
    loader. That way, this class doesn't prevent the main class loader from getting garbage
    collected, and this class can detect when the main class loader has been garbage collected and
    stop itself.
    """

    @staticmethod
    def startFinalizer(finalizableReferenceClass: type[Any], queue: "ReferenceQueue"["Object"], frqReference: "PhantomReference"["Object"]) -> None:
        """
        Starts the Finalizer thread. FinalizableReferenceQueue calls this method reflectively.

        Arguments
        - finalizableReferenceClass: FinalizableReference.class.
        - queue: a reference queue that the thread will poll.
        - frqReference: a phantom reference to the FinalizableReferenceQueue, which will be queued
            either when the FinalizableReferenceQueue is no longer referenced anywhere, or when its
            close() method is called.
        """
        ...


    def run(self) -> None:
        """
        Loops continuously, pulling references off the queue and cleaning them up.
        """
        ...
