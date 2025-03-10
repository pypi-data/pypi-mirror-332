"""
Python module generated from Java source file com.google.common.util.concurrent.OverflowAvoidingLockSupport

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.util.concurrent import *
from java.util.concurrent.locks import LockSupport
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class OverflowAvoidingLockSupport:
    """
    Works around an android bug, where parking for more than INT_MAX seconds can produce an abort
    signal on 32 bit devices running Android Q.
    """


