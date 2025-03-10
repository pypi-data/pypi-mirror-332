"""
Python module generated from Java source file com.google.common.util.concurrent.SmoothRateLimiter

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.math import LongMath
from com.google.common.util.concurrent import *
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class SmoothRateLimiter(RateLimiter):


