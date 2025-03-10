"""
Python module generated from Java source file java.util.UUID

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from java.util import *
from jdk.internal.access import JavaLangAccess
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class UUID(Serializable, Comparable):
    """
    A class that represents an immutable universally unique identifier (UUID).
    A UUID represents a 128-bit value.
    
     There exist different variants of these global identifiers.  The methods
    of this class are for manipulating the Leach-Salz variant, although the
    constructors allow the creation of any variant of UUID (described below).
    
     The layout of a variant 2 (Leach-Salz) UUID is as follows:
    
    The most significant long consists of the following unsigned fields:
    ```
    0xFFFFFFFF00000000 time_low
    0x00000000FFFF0000 time_mid
    0x000000000000F000 version
    0x0000000000000FFF time_hi
    ```
    The least significant long consists of the following unsigned fields:
    ```
    0xC000000000000000 variant
    0x3FFF000000000000 clock_seq
    0x0000FFFFFFFFFFFF node
    ```
    
     The variant field contains a value which identifies the layout of the
    `UUID`.  The bit layout described above is valid only for a `UUID` with a variant value of 2, which indicates the Leach-Salz variant.
    
     The version field holds a value that describes the type of this `UUID`.  There are four different basic types of UUIDs: time-based, DCE
    security, name-based, and randomly generated UUIDs.  These types have a
    version value of 1, 2, 3 and 4, respectively.
    
     For more information including algorithms used to create `UUID`s,
    see <a href="http://www.ietf.org/rfc/rfc4122.txt"> *RFC&nbsp;4122: A
    Universally Unique IDentifier (UUID) URN Namespace*</a>, section 4.2
    &quot;Algorithms for Creating a Time-Based UUID&quot;.

    Since
    - 1.5
    """

    def __init__(self, mostSigBits: int, leastSigBits: int):
        """
        Constructs a new `UUID` using the specified data.  `mostSigBits` is used for the most significant 64 bits of the `UUID` and `leastSigBits` becomes the least significant 64 bits of
        the `UUID`.

        Arguments
        - mostSigBits: The most significant bits of the `UUID`
        - leastSigBits: The least significant bits of the `UUID`
        """
        ...


    @staticmethod
    def randomUUID() -> "UUID":
        """
        Static factory to retrieve a type 4 (pseudo randomly generated) UUID.
        
        The `UUID` is generated using a cryptographically strong pseudo
        random number generator.

        Returns
        - A randomly generated `UUID`
        """
        ...


    @staticmethod
    def nameUUIDFromBytes(name: list[int]) -> "UUID":
        """
        Static factory to retrieve a type 3 (name based) `UUID` based on
        the specified byte array.

        Arguments
        - name: A byte array to be used to construct a `UUID`

        Returns
        - A `UUID` generated from the specified array
        """
        ...


    @staticmethod
    def fromString(name: str) -> "UUID":
        """
        Creates a `UUID` from the string standard representation as
        described in the .toString method.

        Arguments
        - name: A string that specifies a `UUID`

        Returns
        - A `UUID` with the specified value

        Raises
        - IllegalArgumentException: If name does not conform to the string representation as
                 described in .toString
        """
        ...


    def getLeastSignificantBits(self) -> int:
        """
        Returns the least significant 64 bits of this UUID's 128 bit value.

        Returns
        - The least significant 64 bits of this UUID's 128 bit value
        """
        ...


    def getMostSignificantBits(self) -> int:
        """
        Returns the most significant 64 bits of this UUID's 128 bit value.

        Returns
        - The most significant 64 bits of this UUID's 128 bit value
        """
        ...


    def version(self) -> int:
        """
        The version number associated with this `UUID`.  The version
        number describes how this `UUID` was generated.
        
        The version number has the following meaning:
        
        - 1    Time-based UUID
        - 2    DCE security UUID
        - 3    Name-based UUID
        - 4    Randomly generated UUID

        Returns
        - The version number of this `UUID`
        """
        ...


    def variant(self) -> int:
        """
        The variant number associated with this `UUID`.  The variant
        number describes the layout of the `UUID`.
        
        The variant number has the following meaning:
        
        - 0    Reserved for NCS backward compatibility
        - 2    <a href="http://www.ietf.org/rfc/rfc4122.txt">IETF&nbsp;RFC&nbsp;4122</a>
        (Leach-Salz), used by this class
        - 6    Reserved, Microsoft Corporation backward compatibility
        - 7    Reserved for future definition

        Returns
        - The variant number of this `UUID`
        """
        ...


    def timestamp(self) -> int:
        """
        The timestamp value associated with this UUID.
        
         The 60 bit timestamp value is constructed from the time_low,
        time_mid, and time_hi fields of this `UUID`.  The resulting
        timestamp is measured in 100-nanosecond units since midnight,
        October 15, 1582 UTC.
        
         The timestamp value is only meaningful in a time-based UUID, which
        has version type 1.  If this `UUID` is not a time-based UUID then
        this method throws UnsupportedOperationException.

        Returns
        - The timestamp of this `UUID`.

        Raises
        - UnsupportedOperationException: If this UUID is not a version 1 UUID
        """
        ...


    def clockSequence(self) -> int:
        """
        The clock sequence value associated with this UUID.
        
         The 14 bit clock sequence value is constructed from the clock
        sequence field of this UUID.  The clock sequence field is used to
        guarantee temporal uniqueness in a time-based UUID.
        
         The `clockSequence` value is only meaningful in a time-based
        UUID, which has version type 1.  If this UUID is not a time-based UUID
        then this method throws UnsupportedOperationException.

        Returns
        - The clock sequence of this `UUID`

        Raises
        - UnsupportedOperationException: If this UUID is not a version 1 UUID
        """
        ...


    def node(self) -> int:
        """
        The node value associated with this UUID.
        
         The 48 bit node value is constructed from the node field of this
        UUID.  This field is intended to hold the IEEE 802 address of the machine
        that generated this UUID to guarantee spatial uniqueness.
        
         The node value is only meaningful in a time-based UUID, which has
        version type 1.  If this UUID is not a time-based UUID then this method
        throws UnsupportedOperationException.

        Returns
        - The node value of this `UUID`

        Raises
        - UnsupportedOperationException: If this UUID is not a version 1 UUID
        """
        ...


    def toString(self) -> str:
        """
        Returns a `String` object representing this `UUID`.
        
         The UUID string representation is as described by this BNF:
        <blockquote>```
        `UUID                   = <time_low> "-" <time_mid> "-"
                                 <time_high_and_version> "-"
                                 <variant_and_sequence> "-"
                                 <node>
        time_low               = 4*<hexOctet>
        time_mid               = 2*<hexOctet>
        time_high_and_version  = 2*<hexOctet>
        variant_and_sequence   = 2*<hexOctet>
        node                   = 6*<hexOctet>
        hexOctet               = <hexDigit><hexDigit>
        hexDigit               =
              "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
              | "a" | "b" | "c" | "d" | "e" | "f"
              | "A" | "B" | "C" | "D" | "E" | "F"````</blockquote>

        Returns
        - A string representation of this `UUID`
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this `UUID`.

        Returns
        - A hash code value for this `UUID`
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this object to the specified object.  The result is `True` if and only if the argument is not `null`, is a `UUID`
        object, has the same variant, and contains the same value, bit for bit,
        as this `UUID`.

        Arguments
        - obj: The object to be compared

        Returns
        - `True` if the objects are the same; `False`
                 otherwise
        """
        ...


    def compareTo(self, val: "UUID") -> int:
        """
        Compares this UUID with the specified UUID.
        
         The first of two UUIDs is greater than the second if the most
        significant field in which the UUIDs differ is greater for the first
        UUID.

        Arguments
        - val: `UUID` to which this `UUID` is to be compared

        Returns
        - -1, 0 or 1 as this `UUID` is less than, equal to, or
                 greater than `val`
        """
        ...
