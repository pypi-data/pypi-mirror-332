"""
Python module generated from Java source file com.google.common.hash.Crc32cHashFunction

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from typing import Any, Callable, Iterable, Tuple


class Crc32cHashFunction(AbstractStreamingHashFunction):
    """
    This class generates a CRC32C checksum, defined by RFC 3720, Section 12.1. The generator
    polynomial for this checksum is `0x11EDC6F41`.

    Author(s)
    - Kurt Alfred Kluever
    """

    def bits(self) -> int:
        ...


    def newHasher(self) -> "Hasher":
        ...


    def toString(self) -> str:
        ...
