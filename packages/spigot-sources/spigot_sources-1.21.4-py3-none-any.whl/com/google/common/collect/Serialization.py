"""
Python module generated from Java source file com.google.common.collect.Serialization

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.lang.reflect import Field
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Serialization:
    """
    Provides static methods for serializing collection classes.
    
    This class assists the implementation of collection classes. Do not use this class to
    serialize collections that are defined elsewhere.

    Author(s)
    - Jared Levy
    """


