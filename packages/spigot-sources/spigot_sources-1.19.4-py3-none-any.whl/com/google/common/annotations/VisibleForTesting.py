"""
Python module generated from Java source file com.google.common.annotations.VisibleForTesting

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import *
from typing import Any, Callable, Iterable, Tuple


class VisibleForTesting:
    """
    Annotates a program element that exists, or is more widely visible than otherwise necessary, only
    for use in test code.
    
    **Do not use this interface** for public or protected declarations: it is a fig leaf for
    bad design, and it does not prevent anyone from using the declaration---and experience has shown
    that they will. If the method breaks the encapsulation of its class, then its internal
    representation will be hard to change. Instead, use <a
    href="http://errorprone.info/bugpattern/RestrictedApiChecker">RestrictedApiChecker</a>, which
    enforces fine-grained visibility policies.

    Author(s)
    - Johannes Henkel
    """


