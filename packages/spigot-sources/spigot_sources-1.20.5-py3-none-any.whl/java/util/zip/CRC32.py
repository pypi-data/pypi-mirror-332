"""
Python module generated from Java source file java.util.zip.CRC32

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import Reference
from java.util import Objects
from java.util.zip import *
from jdk.internal.vm.annotation import IntrinsicCandidate
from sun.nio.ch import DirectBuffer
from typing import Any, Callable, Iterable, Tuple


class CRC32(Checksum):
    """
    A class that can be used to compute the CRC-32 of a data stream.
    
     Passing a `null` argument to a method in this class will cause
    a NullPointerException to be thrown.

    Author(s)
    - David Connelly

    Since
    - 1.1
    """

    def __init__(self):
        """
        Creates a new CRC32 object.
        """
        ...


    def update(self, b: int) -> None:
        """
        Updates the CRC-32 checksum with the specified byte (the low
        eight bits of the argument b).
        """
        ...


    def update(self, b: list[int], off: int, len: int) -> None:
        """
        Updates the CRC-32 checksum with the specified array of bytes.

        Raises
        - ArrayIndexOutOfBoundsException: if `off` is negative, or `len` is negative, or
                `off+len` is negative or greater than the length of
                the array `b`.
        """
        ...


    def update(self, buffer: "ByteBuffer") -> None:
        """
        Updates the CRC-32 checksum with the bytes from the specified buffer.
        
        The checksum is updated with the remaining bytes in the buffer, starting
        at the buffer's position. Upon return, the buffer's position will be
        updated to its limit; its limit will not have been changed.

        Since
        - 1.8
        """
        ...


    def reset(self) -> None:
        """
        Resets CRC-32 to initial value.
        """
        ...


    def getValue(self) -> int:
        """
        Returns CRC-32 value.
        """
        ...
