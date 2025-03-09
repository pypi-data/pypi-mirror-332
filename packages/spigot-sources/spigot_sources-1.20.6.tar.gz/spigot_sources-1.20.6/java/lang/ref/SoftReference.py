"""
Python module generated from Java source file java.lang.ref.SoftReference

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import *
from typing import Any, Callable, Iterable, Tuple


class SoftReference(Reference):

    def __init__(self, referent: "T"):
        """
        Creates a new soft reference that refers to the given object.  The new
        reference is not registered with any queue.

        Arguments
        - referent: object the new soft reference will refer to
        """
        ...


    def __init__(self, referent: "T", q: "ReferenceQueue"["T"]):
        """
        Creates a new soft reference that refers to the given object and is
        registered with the given queue.

        Arguments
        - referent: object the new soft reference will refer to
        - q: the queue with which the reference is to be registered,
                 or `null` if registration is not required
        """
        ...


    def get(self) -> "T":
        """
        Returns this reference object's referent.  If this reference object has
        been cleared, either by the program or by the garbage collector, then
        this method returns `null`.

        Returns
        - The object to which this reference refers, or
                  `null` if this reference object has been cleared
        """
        ...
