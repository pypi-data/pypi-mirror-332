"""
Python module generated from Java source file com.google.common.base.FinalizableSoftReference

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import *
from java.lang.ref import ReferenceQueue
from java.lang.ref import SoftReference
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class FinalizableSoftReference(SoftReference, FinalizableReference):
    """
    Soft reference with a `finalizeReferent()` method which a background thread invokes after
    the garbage collector reclaims the referent. This is a simpler alternative to using a ReferenceQueue.

    Author(s)
    - Bob Lee

    Since
    - 2.0
    """


