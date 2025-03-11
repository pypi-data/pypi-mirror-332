"""
Python module generated from Java source file com.google.common.collect.ImmutableMapEntry

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableMapEntry(ImmutableEntry):
    """
    Implementation of `Entry` for ImmutableMap that adds extra methods to traverse hash
    buckets for the key and the value. This allows reuse in RegularImmutableMap and RegularImmutableBiMap, which don't have to recopy the entries created by their `Builder`
    implementations.
    
    This base implementation has no key or value pointers, so instances of ImmutableMapEntry (but
    not its subclasses) can be reused when copied from one ImmutableMap to another.

    Author(s)
    - Louis Wasserman
    """


