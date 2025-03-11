"""
Python module generated from Java source file com.google.common.base.FinalizablePhantomReference

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from java.lang.ref import PhantomReference
from java.lang.ref import ReferenceQueue
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class FinalizablePhantomReference(PhantomReference, FinalizableReference):
    """
    Phantom reference with a `finalizeReferent()` method which a background thread invokes
    after the garbage collector reclaims the referent. This is a simpler alternative to using a
    ReferenceQueue.
    
    Unlike a normal phantom reference, this reference will be cleared automatically.

    Author(s)
    - Bob Lee

    Since
    - 2.0
    """


