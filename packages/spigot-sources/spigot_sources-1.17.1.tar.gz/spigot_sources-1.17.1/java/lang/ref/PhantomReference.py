"""
Python module generated from Java source file java.lang.ref.PhantomReference

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import *
from jdk.internal.vm.annotation import IntrinsicCandidate
from typing import Any, Callable, Iterable, Tuple


class PhantomReference(Reference):

    def __init__(self, referent: "T", q: "ReferenceQueue"["T"]):
        """
        Creates a new phantom reference that refers to the given object and
        is registered with the given queue.
        
         It is possible to create a phantom reference with a `null`
        queue.  Such a reference will never be enqueued.

        Arguments
        - referent: the object the new phantom reference will refer to
        - q: the queue with which the reference is to be registered,
                 or `null` if registration is not required
        """
        ...


    def get(self) -> "T":
        """
        Returns this reference object's referent.  Because the referent of a
        phantom reference is always inaccessible, this method always returns
        `null`.

        Returns
        - `null`
        """
        ...
