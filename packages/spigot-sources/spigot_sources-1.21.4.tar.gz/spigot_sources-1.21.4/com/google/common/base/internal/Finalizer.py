"""
Python module generated from Java source file com.google.common.base.internal.Finalizer

Java source file obtained from artifact guava version 33.3.1-jre

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
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Finalizer(Runnable):

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
