"""
Python module generated from Java source file com.google.common.hash.MessageDigestHashFunction

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.security import MessageDigest
from java.security import NoSuchAlgorithmException
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class MessageDigestHashFunction(AbstractHashFunction, Serializable):
    """
    HashFunction adapter for MessageDigest instances.

    Author(s)
    - Dimitris Andreou
    """

    def bits(self) -> int:
        ...


    def toString(self) -> str:
        ...


    def newHasher(self) -> "Hasher":
        ...
