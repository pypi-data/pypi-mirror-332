"""
Python module generated from Java source file java.nio.charset.CoderResult

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import *
from java.util.concurrent import ConcurrentHashMap
from typing import Any, Callable, Iterable, Tuple


class CoderResult:

    UNDERFLOW = CoderResult(CR_UNDERFLOW, 0)
    """
    Result object indicating underflow, meaning that either the input buffer
    has been completely consumed or, if the input buffer is not yet empty,
    that additional input is required.
    """
    OVERFLOW = CoderResult(CR_OVERFLOW, 0)
    """
    Result object indicating overflow, meaning that there is insufficient
    room in the output buffer.
    """


    def toString(self) -> str:
        """
        Returns a string describing this coder result.

        Returns
        - A descriptive string
        """
        ...


    def isUnderflow(self) -> bool:
        """
        Tells whether or not this object describes an underflow condition.

        Returns
        - `True` if, and only if, this object denotes underflow
        """
        ...


    def isOverflow(self) -> bool:
        """
        Tells whether or not this object describes an overflow condition.

        Returns
        - `True` if, and only if, this object denotes overflow
        """
        ...


    def isError(self) -> bool:
        """
        Tells whether or not this object describes an error condition.

        Returns
        - `True` if, and only if, this object denotes either a
                 malformed-input error or an unmappable-character error
        """
        ...


    def isMalformed(self) -> bool:
        """
        Tells whether or not this object describes a malformed-input error.

        Returns
        - `True` if, and only if, this object denotes a
                 malformed-input error
        """
        ...


    def isUnmappable(self) -> bool:
        """
        Tells whether or not this object describes an unmappable-character
        error.

        Returns
        - `True` if, and only if, this object denotes an
                 unmappable-character error
        """
        ...


    def length(self) -> int:
        """
        Returns the length of the erroneous input described by this
        object&nbsp;&nbsp;*(optional operation)*.

        Returns
        - The length of the erroneous input, a positive integer

        Raises
        - UnsupportedOperationException: If this object does not describe an error condition, that is,
                 if the .isError() isError does not return `True`
        """
        ...


    @staticmethod
    def malformedForLength(length: int) -> "CoderResult":
        """
        Static factory method that returns the unique object describing a
        malformed-input error of the given length.

        Arguments
        - length: The given length

        Returns
        - The requested coder-result object
        """
        ...


    @staticmethod
    def unmappableForLength(length: int) -> "CoderResult":
        """
        Static factory method that returns the unique result object describing
        an unmappable-character error of the given length.

        Arguments
        - length: The given length

        Returns
        - The requested coder-result object
        """
        ...


    def throwException(self) -> None:
        """
        Throws an exception appropriate to the result described by this object.

        Raises
        - BufferUnderflowException: If this object is .UNDERFLOW
        - BufferOverflowException: If this object is .OVERFLOW
        - MalformedInputException: If this object represents a malformed-input error; the
                 exception's length value will be that of this object
        - UnmappableCharacterException: If this object represents an unmappable-character error; the
                 exceptions length value will be that of this object
        """
        ...
