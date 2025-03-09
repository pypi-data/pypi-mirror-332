"""
Python module generated from Java source file java.nio.file.attribute.FileTime

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.file.attribute import *
from java.time import Instant
from java.time import LocalDateTime
from java.time import ZoneOffset
from java.util import Objects
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class FileTime(Comparable):

    @staticmethod
    def from(value: int, unit: "TimeUnit") -> "FileTime":
        """
        Returns a `FileTime` representing a value at the given unit of
        granularity.

        Arguments
        - value: the value since the epoch (1970-01-01T00:00:00Z); can be
                 negative
        - unit: the unit of granularity to interpret the value

        Returns
        - a `FileTime` representing the given value
        """
        ...


    @staticmethod
    def fromMillis(value: int) -> "FileTime":
        """
        Returns a `FileTime` representing the given value in milliseconds.

        Arguments
        - value: the value, in milliseconds, since the epoch
                 (1970-01-01T00:00:00Z); can be negative

        Returns
        - a `FileTime` representing the given value
        """
        ...


    @staticmethod
    def from(instant: "Instant") -> "FileTime":
        """
        Returns a `FileTime` representing the same point of time value
        on the time-line as the provided `Instant` object.

        Arguments
        - instant: the instant to convert

        Returns
        - a `FileTime` representing the same point on the time-line
                 as the provided instant

        Since
        - 1.8
        """
        ...


    def to(self, unit: "TimeUnit") -> int:
        """
        Returns the value at the given unit of granularity.
        
         Conversion from a coarser granularity that would numerically overflow
        saturate to `Long.MIN_VALUE` if negative or `Long.MAX_VALUE`
        if positive.

        Arguments
        - unit: the unit of granularity for the return value

        Returns
        - value in the given unit of granularity, since the epoch
                 since the epoch (1970-01-01T00:00:00Z); can be negative
        """
        ...


    def toMillis(self) -> int:
        """
        Returns the value in milliseconds.
        
         Conversion from a coarser granularity that would numerically overflow
        saturate to `Long.MIN_VALUE` if negative or `Long.MAX_VALUE`
        if positive.

        Returns
        - the value in milliseconds, since the epoch (1970-01-01T00:00:00Z)
        """
        ...


    def toInstant(self) -> "Instant":
        """
        Converts this `FileTime` object to an `Instant`.
        
         The conversion creates an `Instant` that represents the
        same point on the time-line as this `FileTime`.
        
         `FileTime` can store points on the time-line further in the
        future and further in the past than `Instant`. Conversion
        from such further time points saturates to Instant.MIN if
        earlier than `Instant.MIN` or Instant.MAX if later
        than `Instant.MAX`.

        Returns
        - an instant representing the same point on the time-line as
                 this `FileTime` object

        Since
        - 1.8
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Tests this `FileTime` for equality with the given object.
        
         The result is `True` if and only if the argument is not `null` and is a `FileTime` that represents the same time. This
        method satisfies the general contract of the `Object.equals` method.

        Arguments
        - obj: the object to compare with

        Returns
        - `True` if, and only if, the given object is a `FileTime` that represents the same time
        """
        ...


    def hashCode(self) -> int:
        """
        Computes a hash code for this file time.
        
         The hash code is based upon the value represented, and satisfies the
        general contract of the Object.hashCode method.

        Returns
        - the hash-code value
        """
        ...


    def compareTo(self, other: "FileTime") -> int:
        """
        Compares the value of two `FileTime` objects for order.

        Arguments
        - other: the other `FileTime` to be compared

        Returns
        - `0` if this `FileTime` is equal to `other`, a
                 value less than 0 if this `FileTime` represents a time
                 that is before `other`, and a value greater than 0 if this
                 `FileTime` represents a time that is after `other`
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this `FileTime`. The string
        is returned in the <a
        href="http://www.w3.org/TR/NOTE-datetime">ISO&nbsp;8601</a> format:
        ```
            YYYY-MM-DDThh:mm:ss[.s+]Z
        ```
        where "`[.s+]`" represents a dot followed by one of more digits
        for the decimal fraction of a second. It is only present when the decimal
        fraction of a second is not zero. For example, `FileTime.fromMillis(1234567890000L).toString()` yields `"2009-02-13T23:31:30Z"`, and `FileTime.fromMillis(1234567890123L).toString()`
        yields `"2009-02-13T23:31:30.123Z"`.
        
         A `FileTime` is primarily intended to represent the value of a
        file's time stamp. Where used to represent *extreme values*, where
        the year is less than "`0001`" or greater than "`9999`" then
        this method deviates from ISO 8601 in the same manner as the
        <a href="http://www.w3.org/TR/xmlschema-2/#deviantformats">XML Schema
        language</a>. That is, the year may be expanded to more than four digits
        and may be negative-signed. If more than four digits then leading zeros
        are not present. The year before "`0001`" is "`-0001`".

        Returns
        - the string representation of this file time
        """
        ...
