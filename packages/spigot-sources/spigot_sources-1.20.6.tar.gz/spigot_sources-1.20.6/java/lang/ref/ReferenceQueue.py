"""
Python module generated from Java source file java.lang.ref.ReferenceQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import *
from java.util.function import Consumer
from jdk.internal.misc import VM
from typing import Any, Callable, Iterable, Tuple


class ReferenceQueue:

    def __init__(self):
        """
        Constructs a new reference-object queue.
        """
        ...


    def poll(self) -> "Reference"["T"]:
        """
        Polls this queue to see if a reference object is available.  If one is
        available without further delay then it is removed from the queue and
        returned.  Otherwise this method immediately returns `null`.

        Returns
        - A reference object, if one was immediately available,
                 otherwise `null`
        """
        ...


    def remove(self, timeout: int) -> "Reference"["T"]:
        """
        Removes the next reference object in this queue, blocking until either
        one becomes available or the given timeout period expires.
        
         This method does not offer real-time guarantees: It schedules the
        timeout as if by invoking the Object.wait(long) method.

        Arguments
        - timeout: If positive, block for up to `timeout`
                         milliseconds while waiting for a reference to be
                         added to this queue.  If zero, block indefinitely.

        Returns
        - A reference object, if one was available within the specified
                 timeout period, otherwise `null`

        Raises
        - IllegalArgumentException: If the value of the timeout argument is negative
        - InterruptedException: If the timeout wait is interrupted
        """
        ...


    def remove(self) -> "Reference"["T"]:
        """
        Removes the next reference object in this queue, blocking until one
        becomes available.

        Returns
        - A reference object, blocking until one becomes available

        Raises
        - InterruptedException: If the wait is interrupted
        """
        ...
