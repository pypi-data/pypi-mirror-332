"""
Python module generated from Java source file java.util.zip.Checksum

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.zip import *
from typing import Any, Callable, Iterable, Tuple


class Checksum:
    """
    An interface representing a data checksum.

    Author(s)
    - David Connelly

    Since
    - 1.1
    """

    def update(self, b: int) -> None:
        """
        Updates the current checksum with the specified byte.

        Arguments
        - b: the byte to update the checksum with
        """
        ...


    def update(self, b: list[int]) -> None:
        """
        Updates the current checksum with the specified array of bytes.

        Arguments
        - b: the array of bytes to update the checksum with

        Raises
        - NullPointerException: if `b` is `null`

        Since
        - 9

        Unknown Tags
        - This default implementation is equal to calling
        `update(b, 0, b.length)`.
        """
        ...


    def update(self, b: list[int], off: int, len: int) -> None:
        """
        Updates the current checksum with the specified array of bytes.

        Arguments
        - b: the byte array to update the checksum with
        - off: the start offset of the data
        - len: the number of bytes to use for the update
        """
        ...


    def update(self, buffer: "ByteBuffer") -> None:
        """
        Updates the current checksum with the bytes from the specified buffer.
        
        The checksum is updated with the remaining bytes in the buffer, starting
        at the buffer's position. Upon return, the buffer's position will be
        updated to its limit; its limit will not have been changed.

        Arguments
        - buffer: the ByteBuffer to update the checksum with

        Raises
        - NullPointerException: if `buffer` is `null`

        Since
        - 9

        Unknown Tags
        - For best performance with DirectByteBuffer and other ByteBuffer
        implementations without a backing array implementers of this interface
        should override this method.
        - The default implementation has the following behavior.
        For ByteBuffers backed by an accessible byte array.
        ````update(buffer.array(),
               buffer.position() + buffer.arrayOffset(),
               buffer.remaining());````
        For ByteBuffers not backed by an accessible byte array.
        ````byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
        while (buffer.hasRemaining()) {
            int length = Math.min(buffer.remaining(), b.length);
            buffer.get(b, 0, length);
            update(b, 0, length);`
        }```
        """
        ...


    def getValue(self) -> int:
        """
        Returns the current checksum value.

        Returns
        - the current checksum value
        """
        ...


    def reset(self) -> None:
        """
        Resets the checksum to its initial value.
        """
        ...
