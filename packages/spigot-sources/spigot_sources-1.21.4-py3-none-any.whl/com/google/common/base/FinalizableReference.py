"""
Python module generated from Java source file com.google.common.base.FinalizableReference

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from com.google.errorprone.annotations import DoNotMock
from typing import Any, Callable, Iterable, Tuple


class FinalizableReference:
    """
    Implemented by references that have code to run after garbage collection of their referents.

    Author(s)
    - Bob Lee

    See
    - FinalizableReferenceQueue

    Since
    - 2.0
    """

    def finalizeReferent(self) -> None:
        """
        Invoked on a background thread after the referent has been garbage collected unless security
        restrictions prevented starting a background thread, in which case this method is invoked when
        new references are created.
        """
        ...
