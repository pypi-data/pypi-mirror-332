"""
Python module generated from Java source file com.google.common.base.Platform

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from java.lang.ref import WeakReference
from java.util import Locale
from java.util import ServiceConfigurationError
from java.util.regex import Pattern
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Platform:
    """
    Methods factored out so that they can be emulated differently in GWT.

    Author(s)
    - Jesse Wilson
    """


