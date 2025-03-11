"""
Python module generated from Java source file java.math.BigInteger

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamException
from java.io import ObjectStreamField
from java.math import *
from java.util import Arrays
from java.util import Objects
from java.util import Random
from java.util.concurrent import ThreadLocalRandom
from jdk.internal.math import DoubleConsts
from jdk.internal.math import FloatConsts
from jdk.internal.vm.annotation import ForceInline
from jdk.internal.vm.annotation import IntrinsicCandidate
from jdk.internal.vm.annotation import Stable
from typing import Any, Callable, Iterable, Tuple


class BigInteger(Number, Comparable):

    ZERO = BigInteger(int[0], 0)
    """
    The BigInteger constant zero.

    Since
    - 1.2
    """
    ONE = valueOf(1)
    """
    The BigInteger constant one.

    Since
    - 1.2
    """
    TWO = valueOf(2)
    """
    The BigInteger constant two.

    Since
    - 9
    """
    TEN = valueOf(10)
    """
    The BigInteger constant ten.

    Since
    - 1.5
    """


    def __init__(self, val: list[int], off: int, len: int):
        """
        Translates a byte sub-array containing the two's-complement binary
        representation of a BigInteger into a BigInteger.  The sub-array is
        specified via an offset into the array and a length.  The sub-array is
        assumed to be in *big-endian* byte-order: the most significant
        byte is the element at index `off`.  The `val` array is
        assumed to be unchanged for the duration of the constructor call.
        
        An `IndexOutOfBoundsException` is thrown if the length of the array
        `val` is non-zero and either `off` is negative, `len`
        is negative, or `off+len` is greater than the length of
        `val`.

        Arguments
        - val: byte array containing a sub-array which is the big-endian
                two's-complement binary representation of a BigInteger.
        - off: the start offset of the binary representation.
        - len: the number of bytes to use.

        Raises
        - NumberFormatException: `val` is zero bytes long.
        - IndexOutOfBoundsException: if the provided array offset and
                length would cause an index into the byte array to be
                negative or greater than or equal to the array length.

        Since
        - 9
        """
        ...


    def __init__(self, val: list[int]):
        """
        Translates a byte array containing the two's-complement binary
        representation of a BigInteger into a BigInteger.  The input array is
        assumed to be in *big-endian* byte-order: the most significant
        byte is in the zeroth element.  The `val` array is assumed to be
        unchanged for the duration of the constructor call.

        Arguments
        - val: big-endian two's-complement binary representation of a
                BigInteger.

        Raises
        - NumberFormatException: `val` is zero bytes long.
        """
        ...


    def __init__(self, signum: int, magnitude: list[int], off: int, len: int):
        """
        Translates the sign-magnitude representation of a BigInteger into a
        BigInteger.  The sign is represented as an integer signum value: -1 for
        negative, 0 for zero, or 1 for positive.  The magnitude is a sub-array of
        a byte array in *big-endian* byte-order: the most significant byte
        is the element at index `off`.  A zero value of the length
        `len` is permissible, and will result in a BigInteger value of 0,
        whether signum is -1, 0 or 1.  The `magnitude` array is assumed to
        be unchanged for the duration of the constructor call.
        
        An `IndexOutOfBoundsException` is thrown if the length of the array
        `magnitude` is non-zero and either `off` is negative,
        `len` is negative, or `off+len` is greater than the length of
        `magnitude`.

        Arguments
        - signum: signum of the number (-1 for negative, 0 for zero, 1
                for positive).
        - magnitude: big-endian binary representation of the magnitude of
                the number.
        - off: the start offset of the binary representation.
        - len: the number of bytes to use.

        Raises
        - NumberFormatException: `signum` is not one of the three
                legal values (-1, 0, and 1), or `signum` is 0 and
                `magnitude` contains one or more non-zero bytes.
        - IndexOutOfBoundsException: if the provided array offset and
                length would cause an index into the byte array to be
                negative or greater than or equal to the array length.

        Since
        - 9
        """
        ...


    def __init__(self, signum: int, magnitude: list[int]):
        """
        Translates the sign-magnitude representation of a BigInteger into a
        BigInteger.  The sign is represented as an integer signum value: -1 for
        negative, 0 for zero, or 1 for positive.  The magnitude is a byte array
        in *big-endian* byte-order: the most significant byte is the
        zeroth element.  A zero-length magnitude array is permissible, and will
        result in a BigInteger value of 0, whether signum is -1, 0 or 1.  The
        `magnitude` array is assumed to be unchanged for the duration of
        the constructor call.

        Arguments
        - signum: signum of the number (-1 for negative, 0 for zero, 1
                for positive).
        - magnitude: big-endian binary representation of the magnitude of
                the number.

        Raises
        - NumberFormatException: `signum` is not one of the three
                legal values (-1, 0, and 1), or `signum` is 0 and
                `magnitude` contains one or more non-zero bytes.
        """
        ...


    def __init__(self, val: str, radix: int):
        """
        Translates the String representation of a BigInteger in the
        specified radix into a BigInteger.  The String representation
        consists of an optional minus or plus sign followed by a
        sequence of one or more digits in the specified radix.  The
        character-to-digit mapping is provided by Character.digit(char, int) Character.digit.  The String may
        not contain any extraneous characters (whitespace, for
        example).

        Arguments
        - val: String representation of BigInteger.
        - radix: radix to be used in interpreting `val`.

        Raises
        - NumberFormatException: `val` is not a valid representation
                of a BigInteger in the specified radix, or `radix` is
                outside the range from Character.MIN_RADIX to
                Character.MAX_RADIX, inclusive.
        """
        ...


    def __init__(self, val: str):
        """
        Translates the decimal String representation of a BigInteger
        into a BigInteger.  The String representation consists of an
        optional minus or plus sign followed by a sequence of one or
        more decimal digits.  The character-to-digit mapping is
        provided by Character.digit(char, int)
        Character.digit.  The String may not contain any extraneous
        characters (whitespace, for example).

        Arguments
        - val: decimal String representation of BigInteger.

        Raises
        - NumberFormatException: `val` is not a valid representation
                of a BigInteger.
        """
        ...


    def __init__(self, numBits: int, rnd: "Random"):
        """
        Constructs a randomly generated BigInteger, uniformly distributed over
        the range 0 to (2<sup>`numBits`</sup> - 1), inclusive.
        The uniformity of the distribution assumes that a fair source of random
        bits is provided in `rnd`.  Note that this constructor always
        constructs a non-negative BigInteger.

        Arguments
        - numBits: maximum bitLength of the new BigInteger.
        - rnd: source of randomness to be used in computing the new
                BigInteger.

        Raises
        - IllegalArgumentException: `numBits` is negative.

        See
        - .bitLength()
        """
        ...


    def __init__(self, bitLength: int, certainty: int, rnd: "Random"):
        """
        Constructs a randomly generated positive BigInteger that is probably
        prime, with the specified bitLength.

        Arguments
        - bitLength: bitLength of the returned BigInteger.
        - certainty: a measure of the uncertainty that the caller is
                willing to tolerate.  The probability that the new BigInteger
                represents a prime number will exceed
                (1 - 1/2<sup>`certainty`</sup>).  The execution time of
                this constructor is proportional to the value of this parameter.
        - rnd: source of random bits used to select candidates to be
                tested for primality.

        Raises
        - ArithmeticException: `bitLength < 2` or `bitLength` is too large.

        See
        - .bitLength()

        Unknown Tags
        - It is recommended that the .probablePrime probablePrime
        method be used in preference to this constructor unless there
        is a compelling need to specify a certainty.
        """
        ...


    @staticmethod
    def probablePrime(bitLength: int, rnd: "Random") -> "BigInteger":
        """
        Returns a positive BigInteger that is probably prime, with the
        specified bitLength. The probability that a BigInteger returned
        by this method is composite does not exceed 2<sup>-100</sup>.

        Arguments
        - bitLength: bitLength of the returned BigInteger.
        - rnd: source of random bits used to select candidates to be
                tested for primality.

        Returns
        - a BigInteger of `bitLength` bits that is probably prime

        Raises
        - ArithmeticException: `bitLength < 2` or `bitLength` is too large.

        See
        - .bitLength()

        Since
        - 1.4
        """
        ...


    def nextProbablePrime(self) -> "BigInteger":
        """
        Returns the first integer greater than this `BigInteger` that
        is probably prime.  The probability that the number returned by this
        method is composite does not exceed 2<sup>-100</sup>. This method will
        never skip over a prime when searching: if it returns `p`, there
        is no prime `q` such that `this < q < p`.

        Returns
        - the first integer greater than this `BigInteger` that
                is probably prime.

        Raises
        - ArithmeticException: `this < 0` or `this` is too large.

        Since
        - 1.5
        """
        ...


    @staticmethod
    def valueOf(val: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is equal to that of the
        specified `long`.

        Arguments
        - val: value of the BigInteger to return.

        Returns
        - a BigInteger with the specified value.

        Unknown Tags
        - This static factory method is provided in preference
        to a (`long`) constructor because it allows for reuse of
        frequently used BigIntegers.
        """
        ...


    def add(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this + val)`.

        Arguments
        - val: value to be added to this BigInteger.

        Returns
        - `this + val`
        """
        ...


    def subtract(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this - val)`.

        Arguments
        - val: value to be subtracted from this BigInteger.

        Returns
        - `this - val`
        """
        ...


    def multiply(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this * val)`.

        Arguments
        - val: value to be multiplied by this BigInteger.

        Returns
        - `this * val`

        Unknown Tags
        - An implementation may offer better algorithmic
        performance when `val == this`.
        """
        ...


    def divide(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this / val)`.

        Arguments
        - val: value by which this BigInteger is to be divided.

        Returns
        - `this / val`

        Raises
        - ArithmeticException: if `val` is zero.
        """
        ...


    def divideAndRemainder(self, val: "BigInteger") -> list["BigInteger"]:
        """
        Returns an array of two BigIntegers containing `(this / val)`
        followed by `(this % val)`.

        Arguments
        - val: value by which this BigInteger is to be divided, and the
                remainder computed.

        Returns
        - an array of two BigIntegers: the quotient `(this / val)`
                is the initial element, and the remainder `(this % val)`
                is the final element.

        Raises
        - ArithmeticException: if `val` is zero.
        """
        ...


    def remainder(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this % val)`.

        Arguments
        - val: value by which this BigInteger is to be divided, and the
                remainder computed.

        Returns
        - `this % val`

        Raises
        - ArithmeticException: if `val` is zero.
        """
        ...


    def pow(self, exponent: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this<sup>exponent</sup>)`.
        Note that `exponent` is an integer rather than a BigInteger.

        Arguments
        - exponent: exponent to which this BigInteger is to be raised.

        Returns
        - `this<sup>exponent</sup>`

        Raises
        - ArithmeticException: `exponent` is negative.  (This would
                cause the operation to yield a non-integer value.)
        """
        ...


    def sqrt(self) -> "BigInteger":
        """
        Returns the integer square root of this BigInteger.  The integer square
        root of the corresponding mathematical integer `n` is the largest
        mathematical integer `s` such that `s*s <= n`.  It is equal
        to the value of `floor(sqrt(n))`, where `sqrt(n)` denotes the
        real square root of `n` treated as a real.  Note that the integer
        square root will be less than the real square root if the latter is not
        representable as an integral value.

        Returns
        - the integer square root of `this`

        Raises
        - ArithmeticException: if `this` is negative.  (The square
                root of a negative integer `val` is
                `(i * sqrt(-val))` where *i* is the
                *imaginary unit* and is equal to
                `sqrt(-1)`.)

        Since
        - 9
        """
        ...


    def sqrtAndRemainder(self) -> list["BigInteger"]:
        """
        Returns an array of two BigIntegers containing the integer square root
        `s` of `this` and its remainder `this - s*s`,
        respectively.

        Returns
        - an array of two BigIntegers with the integer square root at
                offset 0 and the remainder at offset 1

        Raises
        - ArithmeticException: if `this` is negative.  (The square
                root of a negative integer `val` is
                `(i * sqrt(-val))` where *i* is the
                *imaginary unit* and is equal to
                `sqrt(-1)`.)

        See
        - .sqrt()

        Since
        - 9
        """
        ...


    def gcd(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is the greatest common divisor of
        `abs(this)` and `abs(val)`.  Returns 0 if
        `this == 0 && val == 0`.

        Arguments
        - val: value with which the GCD is to be computed.

        Returns
        - `GCD(abs(this), abs(val))`
        """
        ...


    def abs(self) -> "BigInteger":
        """
        Returns a BigInteger whose value is the absolute value of this
        BigInteger.

        Returns
        - `abs(this)`
        """
        ...


    def negate(self) -> "BigInteger":
        """
        Returns a BigInteger whose value is `(-this)`.

        Returns
        - `-this`
        """
        ...


    def signum(self) -> int:
        """
        Returns the signum function of this BigInteger.

        Returns
        - -1, 0 or 1 as the value of this BigInteger is negative, zero or
                positive.
        """
        ...


    def mod(self, m: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this mod m`).  This method
        differs from `remainder` in that it always returns a
        *non-negative* BigInteger.

        Arguments
        - m: the modulus.

        Returns
        - `this mod m`

        Raises
        - ArithmeticException: `m` &le; 0

        See
        - .remainder
        """
        ...


    def modPow(self, exponent: "BigInteger", m: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is
        `(this<sup>exponent</sup> mod m)`.  (Unlike `pow`, this
        method permits negative exponents.)

        Arguments
        - exponent: the exponent.
        - m: the modulus.

        Returns
        - `this<sup>exponent</sup> mod m`

        Raises
        - ArithmeticException: `m` &le; 0 or the exponent is
                negative and this BigInteger is not *relatively
                prime* to `m`.

        See
        - .modInverse
        """
        ...


    def modInverse(self, m: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this`<sup>-1</sup> `mod m)`.

        Arguments
        - m: the modulus.

        Returns
        - `this`<sup>-1</sup> `mod m`.

        Raises
        - ArithmeticException: `m` &le; 0, or this BigInteger
                has no multiplicative inverse mod m (that is, this BigInteger
                is not *relatively prime* to m).
        """
        ...


    def shiftLeft(self, n: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this << n)`.
        The shift distance, `n`, may be negative, in which case
        this method performs a right shift.
        (Computes `floor(this * 2<sup>n</sup>)`.)

        Arguments
        - n: shift distance, in bits.

        Returns
        - `this << n`

        See
        - .shiftRight
        """
        ...


    def shiftRight(self, n: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this >> n)`.  Sign
        extension is performed.  The shift distance, `n`, may be
        negative, in which case this method performs a left shift.
        (Computes `floor(this / 2<sup>n</sup>)`.)

        Arguments
        - n: shift distance, in bits.

        Returns
        - `this >> n`

        See
        - .shiftLeft
        """
        ...


    def and(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this & val)`.  (This
        method returns a negative BigInteger if and only if this and val are
        both negative.)

        Arguments
        - val: value to be AND'ed with this BigInteger.

        Returns
        - `this & val`
        """
        ...


    def or(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this | val)`.  (This method
        returns a negative BigInteger if and only if either this or val is
        negative.)

        Arguments
        - val: value to be OR'ed with this BigInteger.

        Returns
        - `this | val`
        """
        ...


    def xor(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this ^ val)`.  (This method
        returns a negative BigInteger if and only if exactly one of this and
        val are negative.)

        Arguments
        - val: value to be XOR'ed with this BigInteger.

        Returns
        - `this ^ val`
        """
        ...


    def not(self) -> "BigInteger":
        """
        Returns a BigInteger whose value is `(~this)`.  (This method
        returns a negative value if and only if this BigInteger is
        non-negative.)

        Returns
        - `~this`
        """
        ...


    def andNot(self, val: "BigInteger") -> "BigInteger":
        """
        Returns a BigInteger whose value is `(this & ~val)`.  This
        method, which is equivalent to `and(val.not())`, is provided as
        a convenience for masking operations.  (This method returns a negative
        BigInteger if and only if `this` is negative and `val` is
        positive.)

        Arguments
        - val: value to be complemented and AND'ed with this BigInteger.

        Returns
        - `this & ~val`
        """
        ...


    def testBit(self, n: int) -> bool:
        """
        Returns `True` if and only if the designated bit is set.
        (Computes `((this & (1<<n)) != 0)`.)

        Arguments
        - n: index of bit to test.

        Returns
        - `True` if and only if the designated bit is set.

        Raises
        - ArithmeticException: `n` is negative.
        """
        ...


    def setBit(self, n: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is equivalent to this BigInteger
        with the designated bit set.  (Computes `(this | (1<<n))`.)

        Arguments
        - n: index of bit to set.

        Returns
        - `this | (1<<n)`

        Raises
        - ArithmeticException: `n` is negative.
        """
        ...


    def clearBit(self, n: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is equivalent to this BigInteger
        with the designated bit cleared.
        (Computes `(this & ~(1<<n))`.)

        Arguments
        - n: index of bit to clear.

        Returns
        - `this & ~(1<<n)`

        Raises
        - ArithmeticException: `n` is negative.
        """
        ...


    def flipBit(self, n: int) -> "BigInteger":
        """
        Returns a BigInteger whose value is equivalent to this BigInteger
        with the designated bit flipped.
        (Computes `(this ^ (1<<n))`.)

        Arguments
        - n: index of bit to flip.

        Returns
        - `this ^ (1<<n)`

        Raises
        - ArithmeticException: `n` is negative.
        """
        ...


    def getLowestSetBit(self) -> int:
        """
        Returns the index of the rightmost (lowest-order) one bit in this
        BigInteger (the number of zero bits to the right of the rightmost
        one bit).  Returns -1 if this BigInteger contains no one bits.
        (Computes `(this == 0? -1 : log2(this & -this))`.)

        Returns
        - index of the rightmost one bit in this BigInteger.
        """
        ...


    def bitLength(self) -> int:
        """
        Returns the number of bits in the minimal two's-complement
        representation of this BigInteger, *excluding* a sign bit.
        For positive BigIntegers, this is equivalent to the number of bits in
        the ordinary binary representation.  For zero this method returns
        `0`.  (Computes `(ceil(log2(this < 0 ? -this : this+1)))`.)

        Returns
        - number of bits in the minimal two's-complement
                representation of this BigInteger, *excluding* a sign bit.
        """
        ...


    def bitCount(self) -> int:
        """
        Returns the number of bits in the two's complement representation
        of this BigInteger that differ from its sign bit.  This method is
        useful when implementing bit-vector style sets atop BigIntegers.

        Returns
        - number of bits in the two's complement representation
                of this BigInteger that differ from its sign bit.
        """
        ...


    def isProbablePrime(self, certainty: int) -> bool:
        """
        Returns `True` if this BigInteger is probably prime,
        `False` if it's definitely composite.  If
        `certainty` is &le; 0, `True` is
        returned.

        Arguments
        - certainty: a measure of the uncertainty that the caller is
                willing to tolerate: if the call returns `True`
                the probability that this BigInteger is prime exceeds
                (1 - 1/2<sup>`certainty`</sup>).  The execution time of
                this method is proportional to the value of this parameter.

        Returns
        - `True` if this BigInteger is probably prime,
                `False` if it's definitely composite.
        """
        ...


    def compareTo(self, val: "BigInteger") -> int:
        """
        Compares this BigInteger with the specified BigInteger.  This
        method is provided in preference to individual methods for each
        of the six boolean comparison operators (<, ==,
        >, >=, !=, <=).  The suggested
        idiom for performing these comparisons is: `(x.compareTo(y)` &lt;*op*&gt; `0)`, where
        &lt;*op*&gt; is one of the six comparison operators.

        Arguments
        - val: BigInteger to which this BigInteger is to be compared.

        Returns
        - -1, 0 or 1 as this BigInteger is numerically less than, equal
                to, or greater than `val`.
        """
        ...


    def equals(self, x: "Object") -> bool:
        """
        Compares this BigInteger with the specified Object for equality.

        Arguments
        - x: Object to which this BigInteger is to be compared.

        Returns
        - `True` if and only if the specified Object is a
                BigInteger whose value is numerically equal to this BigInteger.
        """
        ...


    def min(self, val: "BigInteger") -> "BigInteger":
        """
        Returns the minimum of this BigInteger and `val`.

        Arguments
        - val: value with which the minimum is to be computed.

        Returns
        - the BigInteger whose value is the lesser of this BigInteger and
                `val`.  If they are equal, either may be returned.
        """
        ...


    def max(self, val: "BigInteger") -> "BigInteger":
        """
        Returns the maximum of this BigInteger and `val`.

        Arguments
        - val: value with which the maximum is to be computed.

        Returns
        - the BigInteger whose value is the greater of this and
                `val`.  If they are equal, either may be returned.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this BigInteger.

        Returns
        - hash code for this BigInteger.
        """
        ...


    def toString(self, radix: int) -> str:
        """
        Returns the String representation of this BigInteger in the
        given radix.  If the radix is outside the range from Character.MIN_RADIX to Character.MAX_RADIX inclusive,
        it will default to 10 (as is the case for
        `Integer.toString`).  The digit-to-character mapping
        provided by `Character.forDigit` is used, and a minus
        sign is prepended if appropriate.  (This representation is
        compatible with the .BigInteger(String, int) (String,
        int) constructor.)

        Arguments
        - radix: radix of the String representation.

        Returns
        - String representation of this BigInteger in the given radix.

        See
        - .BigInteger(java.lang.String, int)
        """
        ...


    def toString(self) -> str:
        """
        Returns the decimal String representation of this BigInteger.
        The digit-to-character mapping provided by
        `Character.forDigit` is used, and a minus sign is
        prepended if appropriate.  (This representation is compatible
        with the .BigInteger(String) (String) constructor, and
        allows for String concatenation with Java's + operator.)

        Returns
        - decimal String representation of this BigInteger.

        See
        - .BigInteger(java.lang.String)
        """
        ...


    def toByteArray(self) -> list[int]:
        """
        Returns a byte array containing the two's-complement
        representation of this BigInteger.  The byte array will be in
        *big-endian* byte-order: the most significant byte is in
        the zeroth element.  The array will contain the minimum number
        of bytes required to represent this BigInteger, including at
        least one sign bit, which is `(ceil((this.bitLength() +
        1)/8))`.  (This representation is compatible with the
        .BigInteger(byte[]) (byte[]) constructor.)

        Returns
        - a byte array containing the two's-complement representation of
                this BigInteger.

        See
        - .BigInteger(byte[])
        """
        ...


    def intValue(self) -> int:
        """
        Converts this BigInteger to an `int`.  This
        conversion is analogous to a
        *narrowing primitive conversion* from `long` to
        `int` as defined in
        <cite>The Java Language Specification</cite>:
        if this BigInteger is too big to fit in an
        `int`, only the low-order 32 bits are returned.
        Note that this conversion can lose information about the
        overall magnitude of the BigInteger value as well as return a
        result with the opposite sign.

        Returns
        - this BigInteger converted to an `int`.

        See
        - .intValueExact()

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def longValue(self) -> int:
        """
        Converts this BigInteger to a `long`.  This
        conversion is analogous to a
        *narrowing primitive conversion* from `long` to
        `int` as defined in
        <cite>The Java Language Specification</cite>:
        if this BigInteger is too big to fit in a
        `long`, only the low-order 64 bits are returned.
        Note that this conversion can lose information about the
        overall magnitude of the BigInteger value as well as return a
        result with the opposite sign.

        Returns
        - this BigInteger converted to a `long`.

        See
        - .longValueExact()

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def floatValue(self) -> float:
        """
        Converts this BigInteger to a `float`.  This
        conversion is similar to the
        *narrowing primitive conversion* from `double` to
        `float` as defined in
        <cite>The Java Language Specification</cite>:
        if this BigInteger has too great a magnitude
        to represent as a `float`, it will be converted to
        Float.NEGATIVE_INFINITY or Float.POSITIVE_INFINITY as appropriate.  Note that even when
        the return value is finite, this conversion can lose
        information about the precision of the BigInteger value.

        Returns
        - this BigInteger converted to a `float`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def doubleValue(self) -> float:
        """
        Converts this BigInteger to a `double`.  This
        conversion is similar to the
        *narrowing primitive conversion* from `double` to
        `float` as defined in
        <cite>The Java Language Specification</cite>:
        if this BigInteger has too great a magnitude
        to represent as a `double`, it will be converted to
        Double.NEGATIVE_INFINITY or Double.POSITIVE_INFINITY as appropriate.  Note that even when
        the return value is finite, this conversion can lose
        information about the precision of the BigInteger value.

        Returns
        - this BigInteger converted to a `double`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def longValueExact(self) -> int:
        """
        Converts this `BigInteger` to a `long`, checking
        for lost information.  If the value of this `BigInteger`
        is out of the range of the `long` type, then an
        `ArithmeticException` is thrown.

        Returns
        - this `BigInteger` converted to a `long`.

        Raises
        - ArithmeticException: if the value of `this` will
        not exactly fit in a `long`.

        See
        - BigInteger.longValue

        Since
        - 1.8
        """
        ...


    def intValueExact(self) -> int:
        """
        Converts this `BigInteger` to an `int`, checking
        for lost information.  If the value of this `BigInteger`
        is out of the range of the `int` type, then an
        `ArithmeticException` is thrown.

        Returns
        - this `BigInteger` converted to an `int`.

        Raises
        - ArithmeticException: if the value of `this` will
        not exactly fit in an `int`.

        See
        - BigInteger.intValue

        Since
        - 1.8
        """
        ...


    def shortValueExact(self) -> int:
        """
        Converts this `BigInteger` to a `short`, checking
        for lost information.  If the value of this `BigInteger`
        is out of the range of the `short` type, then an
        `ArithmeticException` is thrown.

        Returns
        - this `BigInteger` converted to a `short`.

        Raises
        - ArithmeticException: if the value of `this` will
        not exactly fit in a `short`.

        See
        - BigInteger.shortValue

        Since
        - 1.8
        """
        ...


    def byteValueExact(self) -> int:
        """
        Converts this `BigInteger` to a `byte`, checking
        for lost information.  If the value of this `BigInteger`
        is out of the range of the `byte` type, then an
        `ArithmeticException` is thrown.

        Returns
        - this `BigInteger` converted to a `byte`.

        Raises
        - ArithmeticException: if the value of `this` will
        not exactly fit in a `byte`.

        See
        - BigInteger.byteValue

        Since
        - 1.8
        """
        ...
