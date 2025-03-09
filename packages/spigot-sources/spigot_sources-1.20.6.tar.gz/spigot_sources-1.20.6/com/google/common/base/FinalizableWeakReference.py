"""
Python module generated from Java source file com.google.common.base.FinalizableWeakReference

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class FinalizableWeakReference(WeakReference, FinalizableReference):
    """
    Weak reference with a `finalizeReferent()` method which a background thread invokes after
    the garbage collector reclaims the referent. This is a simpler alternative to using a ReferenceQueue.

    Author(s)
    - Bob Lee

    Since
    - 2.0
    """


