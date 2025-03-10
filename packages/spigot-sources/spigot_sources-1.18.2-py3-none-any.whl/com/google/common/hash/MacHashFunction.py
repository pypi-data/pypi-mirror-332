"""
Python module generated from Java source file com.google.common.hash.MacHashFunction

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.security import InvalidKeyException
from java.security import Key
from java.security import NoSuchAlgorithmException
from javax.crypto import Mac
from typing import Any, Callable, Iterable, Tuple


class MacHashFunction(AbstractHashFunction):
    """
    HashFunction adapter for Mac instances.

    Author(s)
    - Kurt Alfred Kluever
    """

    def bits(self) -> int:
        ...


    def newHasher(self) -> "Hasher":
        ...


    def toString(self) -> str:
        ...
