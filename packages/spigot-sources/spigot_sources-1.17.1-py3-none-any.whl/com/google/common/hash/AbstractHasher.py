"""
Python module generated from Java source file com.google.common.hash.AbstractHasher

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.nio.charset import Charset
from typing import Any, Callable, Iterable, Tuple


class AbstractHasher(Hasher):
    """
    An abstract hasher, implementing .putBoolean(boolean), .putDouble(double),
    .putFloat(float), .putUnencodedChars(CharSequence), and
    .putString(CharSequence, Charset) as prescribed by Hasher.

    Author(s)
    - Dimitris Andreou
    """

    def putBoolean(self, b: bool) -> "Hasher":
        ...


    def putDouble(self, d: float) -> "Hasher":
        ...


    def putFloat(self, f: float) -> "Hasher":
        ...


    def putUnencodedChars(self, charSequence: "CharSequence") -> "Hasher":
        ...


    def putString(self, charSequence: "CharSequence", charset: "Charset") -> "Hasher":
        ...
