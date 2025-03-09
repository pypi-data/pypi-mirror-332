"""
Python module generated from Java source file com.google.common.hash.LittleEndianByteArray

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.common.primitives import Longs
from java.lang.reflect import Field
from java.security import AccessController
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from sun.misc import Unsafe
from typing import Any, Callable, Iterable, Tuple


class LittleEndianByteArray:
    """
    Utility functions for loading and storing values from a byte array.

    Author(s)
    - Kyle Maddison
    """


