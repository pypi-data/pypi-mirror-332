"""
Python module generated from Java source file com.google.common.annotations.Beta

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import *
from typing import Any, Callable, Iterable, Tuple


class Beta:
    """
    Signifies that a public API (public class, method or field) is subject to incompatible changes,
    or even removal, in a future release. An API bearing this annotation is exempt from any
    compatibility guarantees made by its containing library. Note that the presence of this
    annotation implies nothing about the quality or performance of the API in question, only the fact
    that it is not "API-frozen."
    
    It is generally safe for *applications* to depend on beta APIs, at the cost of some extra
    work during upgrades. However it is generally inadvisable for *libraries* (which get
    included on users' CLASSPATHs, outside the library developers' control) to do so.

    Author(s)
    - Kevin Bourrillion
    """


