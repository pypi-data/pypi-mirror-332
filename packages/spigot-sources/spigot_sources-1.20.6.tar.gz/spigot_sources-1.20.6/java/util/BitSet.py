"""
Python module generated from Java source file java.util.BitSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import *
from java.util.function import IntConsumer
from java.util.stream import IntStream
from java.util.stream import StreamSupport
from typing import Any, Callable, Iterable, Tuple


class BitSet(Cloneable, Serializable):
    """
    This class implements a vector of bits that grows as needed. Each
    component of the bit set has a `boolean` value. The
    bits of a `BitSet` are indexed by nonnegative integers.
    Individual indexed bits can be examined, set, or cleared. One
    `BitSet` may be used to modify the contents of another
    `BitSet` through logical AND, logical inclusive OR, and
    logical exclusive OR operations.
    
    By default, all bits in the set initially have the value
    `False`.
    
    Every bit set has a current size, which is the number of bits
    of space currently in use by the bit set. Note that the size is
    related to the implementation of a bit set, so it may change with
    implementation. The length of a bit set relates to logical length
    of a bit set and is defined independently of implementation.
    
    Unless otherwise noted, passing a null parameter to any of the
    methods in a `BitSet` will result in a
    `NullPointerException`.
    
    A `BitSet` is not safe for multithreaded use without
    external synchronization.

    Author(s)
    - Martin Buchholz

    Since
    - 1.0
    """

    def __init__(self):
        """
        Creates a new bit set. All bits are initially `False`.
        """
        ...


    def __init__(self, nbits: int):
        """
        Creates a bit set whose initial size is large enough to explicitly
        represent bits with indices in the range `0` through
        `nbits-1`. All bits are initially `False`.

        Arguments
        - nbits: the initial size of the bit set

        Raises
        - NegativeArraySizeException: if the specified initial size
                is negative
        """
        ...


    @staticmethod
    def valueOf(longs: list[int]) -> "BitSet":
        """
        Returns a new bit set containing all the bits in the given long array.
        
        More precisely,
        `BitSet.valueOf(longs).get(n) == ((longs[n/64] & (1L<<(n%64))) != 0)`
        for all `n < 64 * longs.length`.
        
        This method is equivalent to
        `BitSet.valueOf(LongBuffer.wrap(longs))`.

        Arguments
        - longs: a long array containing a little-endian representation
               of a sequence of bits to be used as the initial bits of the
               new bit set

        Returns
        - a `BitSet` containing all the bits in the long array

        Since
        - 1.7
        """
        ...


    @staticmethod
    def valueOf(lb: "LongBuffer") -> "BitSet":
        """
        Returns a new bit set containing all the bits in the given long
        buffer between its position and limit.
        
        More precisely,
        `BitSet.valueOf(lb).get(n) == ((lb.get(lb.position()+n/64) & (1L<<(n%64))) != 0)`
        for all `n < 64 * lb.remaining()`.
        
        The long buffer is not modified by this method, and no
        reference to the buffer is retained by the bit set.

        Arguments
        - lb: a long buffer containing a little-endian representation
               of a sequence of bits between its position and limit, to be
               used as the initial bits of the new bit set

        Returns
        - a `BitSet` containing all the bits in the buffer in the
                specified range

        Since
        - 1.7
        """
        ...


    @staticmethod
    def valueOf(bytes: list[int]) -> "BitSet":
        """
        Returns a new bit set containing all the bits in the given byte array.
        
        More precisely,
        `BitSet.valueOf(bytes).get(n) == ((bytes[n/8] & (1<<(n%8))) != 0)`
        for all `n <  8 * bytes.length`.
        
        This method is equivalent to
        `BitSet.valueOf(ByteBuffer.wrap(bytes))`.

        Arguments
        - bytes: a byte array containing a little-endian
               representation of a sequence of bits to be used as the
               initial bits of the new bit set

        Returns
        - a `BitSet` containing all the bits in the byte array

        Since
        - 1.7
        """
        ...


    @staticmethod
    def valueOf(bb: "ByteBuffer") -> "BitSet":
        """
        Returns a new bit set containing all the bits in the given byte
        buffer between its position and limit.
        
        More precisely,
        `BitSet.valueOf(bb).get(n) == ((bb.get(bb.position()+n/8) & (1<<(n%8))) != 0)`
        for all `n < 8 * bb.remaining()`.
        
        The byte buffer is not modified by this method, and no
        reference to the buffer is retained by the bit set.

        Arguments
        - bb: a byte buffer containing a little-endian representation
               of a sequence of bits between its position and limit, to be
               used as the initial bits of the new bit set

        Returns
        - a `BitSet` containing all the bits in the buffer in the
                specified range

        Since
        - 1.7
        """
        ...


    def toByteArray(self) -> list[int]:
        """
        Returns a new byte array containing all the bits in this bit set.
        
        More precisely, if
        `byte[] bytes = s.toByteArray();`
        then `bytes.length == (s.length()+7)/8` and
        `s.get(n) == ((bytes[n/8] & (1<<(n%8))) != 0)`
        for all `n < 8 * bytes.length`.

        Returns
        - a byte array containing a little-endian representation
                of all the bits in this bit set

        Since
        - 1.7
        """
        ...


    def toLongArray(self) -> list[int]:
        """
        Returns a new long array containing all the bits in this bit set.
        
        More precisely, if
        `long[] longs = s.toLongArray();`
        then `longs.length == (s.length()+63)/64` and
        `s.get(n) == ((longs[n/64] & (1L<<(n%64))) != 0)`
        for all `n < 64 * longs.length`.

        Returns
        - a long array containing a little-endian representation
                of all the bits in this bit set

        Since
        - 1.7
        """
        ...


    def flip(self, bitIndex: int) -> None:
        """
        Sets the bit at the specified index to the complement of its
        current value.

        Arguments
        - bitIndex: the index of the bit to flip

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.4
        """
        ...


    def flip(self, fromIndex: int, toIndex: int) -> None:
        """
        Sets each bit from the specified `fromIndex` (inclusive) to the
        specified `toIndex` (exclusive) to the complement of its current
        value.

        Arguments
        - fromIndex: index of the first bit to flip
        - toIndex: index after the last bit to flip

        Raises
        - IndexOutOfBoundsException: if `fromIndex` is negative,
                or `toIndex` is negative, or `fromIndex` is
                larger than `toIndex`

        Since
        - 1.4
        """
        ...


    def set(self, bitIndex: int) -> None:
        """
        Sets the bit at the specified index to `True`.

        Arguments
        - bitIndex: a bit index

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.0
        """
        ...


    def set(self, bitIndex: int, value: bool) -> None:
        """
        Sets the bit at the specified index to the specified value.

        Arguments
        - bitIndex: a bit index
        - value: a boolean value to set

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.4
        """
        ...


    def set(self, fromIndex: int, toIndex: int) -> None:
        """
        Sets the bits from the specified `fromIndex` (inclusive) to the
        specified `toIndex` (exclusive) to `True`.

        Arguments
        - fromIndex: index of the first bit to be set
        - toIndex: index after the last bit to be set

        Raises
        - IndexOutOfBoundsException: if `fromIndex` is negative,
                or `toIndex` is negative, or `fromIndex` is
                larger than `toIndex`

        Since
        - 1.4
        """
        ...


    def set(self, fromIndex: int, toIndex: int, value: bool) -> None:
        """
        Sets the bits from the specified `fromIndex` (inclusive) to the
        specified `toIndex` (exclusive) to the specified value.

        Arguments
        - fromIndex: index of the first bit to be set
        - toIndex: index after the last bit to be set
        - value: value to set the selected bits to

        Raises
        - IndexOutOfBoundsException: if `fromIndex` is negative,
                or `toIndex` is negative, or `fromIndex` is
                larger than `toIndex`

        Since
        - 1.4
        """
        ...


    def clear(self, bitIndex: int) -> None:
        """
        Sets the bit specified by the index to `False`.

        Arguments
        - bitIndex: the index of the bit to be cleared

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.0
        """
        ...


    def clear(self, fromIndex: int, toIndex: int) -> None:
        """
        Sets the bits from the specified `fromIndex` (inclusive) to the
        specified `toIndex` (exclusive) to `False`.

        Arguments
        - fromIndex: index of the first bit to be cleared
        - toIndex: index after the last bit to be cleared

        Raises
        - IndexOutOfBoundsException: if `fromIndex` is negative,
                or `toIndex` is negative, or `fromIndex` is
                larger than `toIndex`

        Since
        - 1.4
        """
        ...


    def clear(self) -> None:
        """
        Sets all of the bits in this BitSet to `False`.

        Since
        - 1.4
        """
        ...


    def get(self, bitIndex: int) -> bool:
        """
        Returns the value of the bit with the specified index. The value
        is `True` if the bit with the index `bitIndex`
        is currently set in this `BitSet`; otherwise, the result
        is `False`.

        Arguments
        - bitIndex: the bit index

        Returns
        - the value of the bit with the specified index

        Raises
        - IndexOutOfBoundsException: if the specified index is negative
        """
        ...


    def get(self, fromIndex: int, toIndex: int) -> "BitSet":
        """
        Returns a new `BitSet` composed of bits from this `BitSet`
        from `fromIndex` (inclusive) to `toIndex` (exclusive).

        Arguments
        - fromIndex: index of the first bit to include
        - toIndex: index after the last bit to include

        Returns
        - a new `BitSet` from a range of this `BitSet`

        Raises
        - IndexOutOfBoundsException: if `fromIndex` is negative,
                or `toIndex` is negative, or `fromIndex` is
                larger than `toIndex`

        Since
        - 1.4
        """
        ...


    def nextSetBit(self, fromIndex: int) -> int:
        """
        Returns the index of the first bit that is set to `True`
        that occurs on or after the specified starting index. If no such
        bit exists then `-1` is returned.
        
        To iterate over the `True` bits in a `BitSet`,
        use the following loop:
        
         ``` `for (int i = bs.nextSetBit(0); i >= 0; i = bs.nextSetBit(i+1)) {
            // operate on index i here
            if (i == Integer.MAX_VALUE) {
                break; // or (i+1) would overflow`
        }}```

        Arguments
        - fromIndex: the index to start checking from (inclusive)

        Returns
        - the index of the next set bit, or `-1` if there
                is no such bit

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.4
        """
        ...


    def nextClearBit(self, fromIndex: int) -> int:
        """
        Returns the index of the first bit that is set to `False`
        that occurs on or after the specified starting index.

        Arguments
        - fromIndex: the index to start checking from (inclusive)

        Returns
        - the index of the next clear bit

        Raises
        - IndexOutOfBoundsException: if the specified index is negative

        Since
        - 1.4
        """
        ...


    def previousSetBit(self, fromIndex: int) -> int:
        """
        Returns the index of the nearest bit that is set to `True`
        that occurs on or before the specified starting index.
        If no such bit exists, or if `-1` is given as the
        starting index, then `-1` is returned.
        
        To iterate over the `True` bits in a `BitSet`,
        use the following loop:
        
         ``` `for (int i = bs.length(); (i = bs.previousSetBit(i-1)) >= 0; ) {
            // operate on index i here`}```

        Arguments
        - fromIndex: the index to start checking from (inclusive)

        Returns
        - the index of the previous set bit, or `-1` if there
                is no such bit

        Raises
        - IndexOutOfBoundsException: if the specified index is less
                than `-1`

        Since
        - 1.7
        """
        ...


    def previousClearBit(self, fromIndex: int) -> int:
        """
        Returns the index of the nearest bit that is set to `False`
        that occurs on or before the specified starting index.
        If no such bit exists, or if `-1` is given as the
        starting index, then `-1` is returned.

        Arguments
        - fromIndex: the index to start checking from (inclusive)

        Returns
        - the index of the previous clear bit, or `-1` if there
                is no such bit

        Raises
        - IndexOutOfBoundsException: if the specified index is less
                than `-1`

        Since
        - 1.7
        """
        ...


    def length(self) -> int:
        """
        Returns the "logical size" of this `BitSet`: the index of
        the highest set bit in the `BitSet` plus one. Returns zero
        if the `BitSet` contains no set bits.

        Returns
        - the logical size of this `BitSet`

        Since
        - 1.2
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns True if this `BitSet` contains no bits that are set
        to `True`.

        Returns
        - boolean indicating whether this `BitSet` is empty

        Since
        - 1.4
        """
        ...


    def intersects(self, set: "BitSet") -> bool:
        """
        Returns True if the specified `BitSet` has any bits set to
        `True` that are also set to `True` in this `BitSet`.

        Arguments
        - set: `BitSet` to intersect with

        Returns
        - boolean indicating whether this `BitSet` intersects
                the specified `BitSet`

        Since
        - 1.4
        """
        ...


    def cardinality(self) -> int:
        """
        Returns the number of bits set to `True` in this `BitSet`.

        Returns
        - the number of bits set to `True` in this `BitSet`

        Since
        - 1.4
        """
        ...


    def and(self, set: "BitSet") -> None:
        """
        Performs a logical **AND** of this target bit set with the
        argument bit set. This bit set is modified so that each bit in it
        has the value `True` if and only if it both initially
        had the value `True` and the corresponding bit in the
        bit set argument also had the value `True`.

        Arguments
        - set: a bit set
        """
        ...


    def or(self, set: "BitSet") -> None:
        """
        Performs a logical **OR** of this bit set with the bit set
        argument. This bit set is modified so that a bit in it has the
        value `True` if and only if it either already had the
        value `True` or the corresponding bit in the bit set
        argument has the value `True`.

        Arguments
        - set: a bit set
        """
        ...


    def xor(self, set: "BitSet") -> None:
        """
        Performs a logical **XOR** of this bit set with the bit set
        argument. This bit set is modified so that a bit in it has the
        value `True` if and only if one of the following
        statements holds:
        
        - The bit initially has the value `True`, and the
            corresponding bit in the argument has the value `False`.
        - The bit initially has the value `False`, and the
            corresponding bit in the argument has the value `True`.

        Arguments
        - set: a bit set
        """
        ...


    def andNot(self, set: "BitSet") -> None:
        """
        Clears all of the bits in this `BitSet` whose corresponding
        bit is set in the specified `BitSet`.

        Arguments
        - set: the `BitSet` with which to mask this
                `BitSet`

        Since
        - 1.2
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this bit set. The hash code depends
        only on which bits are set within this `BitSet`.
        
        The hash code is defined to be the result of the following
        calculation:
         ``` `public int hashCode() {
            long h = 1234;
            long[] words = toLongArray();
            for (int i = words.length; --i >= 0; )
                h ^= words[i] * (i + 1);
            return (int)((h >> 32) ^ h);`}```
        Note that the hash code changes if the set of bits is altered.

        Returns
        - the hash code value for this bit set
        """
        ...


    def size(self) -> int:
        """
        Returns the number of bits of space actually in use by this
        `BitSet` to represent bit values.
        The maximum element in the set is the size - 1st element.

        Returns
        - the number of bits currently in this bit set
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this object against the specified object.
        The result is `True` if and only if the argument is
        not `null` and is a `BitSet` object that has
        exactly the same set of bits set to `True` as this bit
        set. That is, for every nonnegative `int` index `k`,
        ```((BitSet)obj).get(k) == this.get(k)```
        must be True. The current sizes of the two bit sets are not compared.

        Arguments
        - obj: the object to compare with

        Returns
        - `True` if the objects are the same;
                `False` otherwise

        See
        - .size()
        """
        ...


    def clone(self) -> "Object":
        """
        Cloning this `BitSet` produces a new `BitSet`
        that is equal to it.
        The clone of the bit set is another bit set that has exactly the
        same bits set to `True` as this bit set.

        Returns
        - a clone of this bit set

        See
        - .size()
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this bit set. For every index
        for which this `BitSet` contains a bit in the set
        state, the decimal representation of that index is included in
        the result. Such indices are listed in order from lowest to
        highest, separated by ",&nbsp;" (a comma and a space) and
        surrounded by braces, resulting in the usual mathematical
        notation for a set of integers.
        
        Example:
        ```
        BitSet drPepper = new BitSet();```
        Now `drPepper.toString()` returns "`{`}".
        ```
        drPepper.set(2);```
        Now `drPepper.toString()` returns "`{2`}".
        ```
        drPepper.set(4);
        drPepper.set(10);```
        Now `drPepper.toString()` returns "`{2, 4, 10`}".

        Returns
        - a string representation of this bit set
        """
        ...


    def stream(self) -> "IntStream":
        """
        Returns a stream of indices for which this `BitSet`
        contains a bit in the set state. The indices are returned
        in order, from lowest to highest. The size of the stream
        is the number of bits in the set state, equal to the value
        returned by the .cardinality() method.
        
        The stream binds to this bit set when the terminal stream operation
        commences (specifically, the spliterator for the stream is
        <a href="Spliterator.html#binding">*late-binding*</a>).  If the
        bit set is modified during that operation then the result is undefined.

        Returns
        - a stream of integers representing set indices

        Since
        - 1.8
        """
        ...
