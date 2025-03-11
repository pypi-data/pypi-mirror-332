"""
Python module generated from Java source file java.math.BigDecimal

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectStreamException
from java.io import StreamCorruptedException
from java.math import *
from java.util import Arrays
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class BigDecimal(Number, Comparable):
    """
    Immutable, arbitrary-precision signed decimal numbers.  A `BigDecimal` consists of an arbitrary precision integer
    *unscaledValue() unscaled value* and a 32-bit
    integer *scale() scale*.  If zero or positive,
    the scale is the number of digits to the right of the decimal
    point.  If negative, the unscaled value of the number is multiplied
    by ten to the power of the negation of the scale.  The value of the
    number represented by the `BigDecimal` is therefore
    `(unscaledValue &times; 10<sup>-scale</sup>)`.
    
    The `BigDecimal` class provides operations for
    arithmetic, scale manipulation, rounding, comparison, hashing, and
    format conversion.  The .toString method provides a
    canonical representation of a `BigDecimal`.
    
    The `BigDecimal` class gives its user complete control
    over rounding behavior.  If no rounding mode is specified and the
    exact result cannot be represented, an `ArithmeticException`
    is thrown; otherwise, calculations can be carried out to a chosen
    precision and rounding mode by supplying an appropriate MathContext object to the operation.  In either case, eight
    *rounding modes* are provided for the control of rounding.
    Using the integer fields in this class (such as .ROUND_HALF_UP) to represent rounding mode is deprecated; the
    enumeration values of the `RoundingMode` `enum`, (such
    as RoundingMode.HALF_UP) should be used instead.
    
    When a `MathContext` object is supplied with a precision
    setting of 0 (for example, MathContext.UNLIMITED),
    arithmetic operations are exact, as are the arithmetic methods
    which take no `MathContext` object. As a corollary of
    computing the exact result, the rounding mode setting of a `MathContext` object with a precision setting of 0 is not used and
    thus irrelevant.  In the case of divide, the exact quotient could
    have an infinitely long decimal expansion; for example, 1 divided
    by 3.  If the quotient has a nonterminating decimal expansion and
    the operation is specified to return an exact result, an `ArithmeticException` is thrown.  Otherwise, the exact result of the
    division is returned, as done for other operations.
    
    When the precision setting is not 0, the rules of `BigDecimal` arithmetic are broadly compatible with selected modes
    of operation of the arithmetic defined in ANSI X3.274-1996 and ANSI
    X3.274-1996/AM 1-2000 (section 7.4).  Unlike those standards,
    `BigDecimal` includes many rounding modes.  Any conflicts
    between these ANSI standards and the `BigDecimal`
    specification are resolved in favor of `BigDecimal`.
    
    Since the same numerical value can have different
    representations (with different scales), the rules of arithmetic
    and rounding must specify both the numerical result and the scale
    used in the result's representation.
    
    The different representations of the same numerical value are
    called members of the same *cohort*. The compareTo(BigDecimal) natural order of `BigDecimal`
    considers members of the same cohort to be equal to each other. In
    contrast, the equals equals method requires both the
    numerical value and representation to be the same for equality to
    hold. The results of methods like scale and unscaledValue will differ for numerically equal values with
    different representations.
    
    In general the rounding modes and precision setting determine
    how operations return results with a limited number of digits when
    the exact result has more digits (perhaps infinitely many in the
    case of division and square root) than the number of digits returned.
    
    First, the total number of digits to return is specified by the
    `MathContext`'s `precision` setting; this determines
    the result's *precision*.  The digit count starts from the
    leftmost nonzero digit of the exact result.  The rounding mode
    determines how any discarded trailing digits affect the returned
    result.
    
    For all arithmetic operators, the operation is carried out as
    though an exact intermediate result were first calculated and then
    rounded to the number of digits specified by the precision setting
    (if necessary), using the selected rounding mode.  If the exact
    result is not returned, some digit positions of the exact result
    are discarded.  When rounding increases the magnitude of the
    returned result, it is possible for a new digit position to be
    created by a carry propagating to a leading "9" digit.
    For example, rounding the value 999.9 to three digits rounding up
    would be numerically equal to one thousand, represented as
    100&times;10<sup>1</sup>.  In such cases, the new "1" is
    the leading digit position of the returned result.
    
    For methods and constructors with a `MathContext`
    parameter, if the result is inexact but the rounding mode is RoundingMode.UNNECESSARY UNNECESSARY, an `ArithmeticException` will be thrown.
    
    Besides a logical exact result, each arithmetic operation has a
    preferred scale for representing a result.  The preferred
    scale for each operation is listed in the table below.
    
    <table class="striped" style="text-align:left">
    <caption>Preferred Scales for Results of Arithmetic Operations
    </caption>
    <thead>
    <tr><th scope="col">Operation</th><th scope="col">Preferred Scale of Result</th></tr>
    </thead>
    <tbody>
    <tr><th scope="row">Add</th><td>max(addend.scale(), augend.scale())</td>
    <tr><th scope="row">Subtract</th><td>max(minuend.scale(), subtrahend.scale())</td>
    <tr><th scope="row">Multiply</th><td>multiplier.scale() + multiplicand.scale()</td>
    <tr><th scope="row">Divide</th><td>dividend.scale() - divisor.scale()</td>
    <tr><th scope="row">Square root</th><td>radicand.scale()/2</td>
    </tbody>
    </table>
    
    These scales are the ones used by the methods which return exact
    arithmetic results; except that an exact divide may have to use a
    larger scale since the exact result may have more digits.  For
    example, `1/32` is `0.03125`.
    
    Before rounding, the scale of the logical exact intermediate
    result is the preferred scale for that operation.  If the exact
    numerical result cannot be represented in `precision`
    digits, rounding selects the set of digits to return and the scale
    of the result is reduced from the scale of the intermediate result
    to the least scale which can represent the `precision`
    digits actually returned.  If the exact result can be represented
    with at most `precision` digits, the representation
    of the result with the scale closest to the preferred scale is
    returned.  In particular, an exactly representable quotient may be
    represented in fewer than `precision` digits by removing
    trailing zeros and decreasing the scale.  For example, rounding to
    three digits using the RoundingMode.FLOOR floor
    rounding mode, 
    
    `19/100 = 0.19   // integer=19,  scale=2` 
    
    but
    
    `21/110 = 0.190  // integer=190, scale=3` 
    
    Note that for add, subtract, and multiply, the reduction in
    scale will equal the number of digit positions of the exact result
    which are discarded. If the rounding causes a carry propagation to
    create a new high-order digit position, an additional digit of the
    result is discarded than when no new digit position is created.
    
    Other methods may have slightly different rounding semantics.
    For example, the result of the `pow` method using the
    .pow(int, MathContext) specified algorithm can
    occasionally differ from the rounded mathematical result by more
    than one unit in the last place, one *.ulp() ulp*.
    
    Two types of operations are provided for manipulating the scale
    of a `BigDecimal`: scaling/rounding operations and decimal
    point motion operations.  Scaling/rounding operations (.setScale setScale and .round round) return a
    `BigDecimal` whose value is approximately (or exactly) equal
    to that of the operand, but whose scale or precision is the
    specified value; that is, they increase or decrease the precision
    of the stored number with minimal effect on its value.  Decimal
    point motion operations (.movePointLeft movePointLeft and
    .movePointRight movePointRight) return a
    `BigDecimal` created from the operand by moving the decimal
    point a specified distance in the specified direction.
    
    As a 32-bit integer, the set of values for the scale is large,
    but bounded. If the scale of a result would exceed the range of a
    32-bit integer, either by overflow or underflow, the operation may
    throw an `ArithmeticException`.
    
    For the sake of brevity and clarity, pseudo-code is used
    throughout the descriptions of `BigDecimal` methods.  The
    pseudo-code expression `(i + j)` is shorthand for "a
    `BigDecimal` whose value is that of the `BigDecimal`
    `i` added to that of the `BigDecimal`
    `j`." The pseudo-code expression `(i == j)` is
    shorthand for "`True` if and only if the
    `BigDecimal` `i` represents the same value as the
    `BigDecimal` `j`." Other pseudo-code expressions
    are interpreted similarly.  Square brackets are used to represent
    the particular `BigInteger` and scale pair defining a
    `BigDecimal` value; for example [19, 2] is the
    `BigDecimal` numerically equal to 0.19 having a scale of 2.
    
    All methods and constructors for this class throw
    `NullPointerException` when passed a `null` object
    reference for any input parameter.

    Author(s)
    - Sergey V. Kuksenko

    See
    - java.util.SortedSet

    Since
    - 1.1

    Unknown Tags
    - Care should be exercised if `BigDecimal` objects are
    used as keys in a java.util.SortedMap SortedMap or elements
    in a java.util.SortedSet SortedSet since `BigDecimal`'s *compareTo(BigDecimal) natural
    ordering* is *inconsistent with equals*.  See Comparable, java.util.SortedMap or java.util.SortedSet for more information.
    
    <h2>Relation to IEEE 754 Decimal Arithmetic</h2>
    
    Starting with its 2008 revision, the <cite>IEEE 754 Standard for
    Floating-point Arithmetic</cite> has covered decimal formats and
    operations. While there are broad similarities in the decimal
    arithmetic defined by IEEE 754 and by this class, there are notable
    differences as well. The fundamental similarity shared by `BigDecimal` and IEEE 754 decimal arithmetic is the conceptual
    operation of computing the mathematical infinitely precise real
    number value of an operation and then mapping that real number to a
    representable decimal floating-point value under a *rounding
    policy*. The rounding policy is called a RoundingMode rounding mode for `BigDecimal` and called a
    rounding-direction attribute in IEEE 754-2019. When the exact value
    is not representable, the rounding policy determines which of the
    two representable decimal values bracketing the exact value is
    selected as the computed result. The notion of a *preferred
    scale/preferred exponent* is also shared by both systems.
    
    For differences, IEEE 754 includes several kinds of values not
    modeled by `BigDecimal` including negative zero, signed
    infinities, and NaN (not-a-number). IEEE 754 defines formats, which
    are parameterized by base (binary or decimal), number of digits of
    precision, and exponent range. A format determines the set of
    representable values. Most operations accept as input one or more
    values of a given format and produce a result in the same format.
    A `BigDecimal`'s scale() scale is equivalent to
    negating an IEEE 754 value's exponent. `BigDecimal` values do
    not have a format in the same sense; all values have the same
    possible range of scale/exponent and the unscaledValue() unscaled value has arbitrary precision. Instead,
    for the `BigDecimal` operations taking a `MathContext`
    parameter, if the `MathContext` has a nonzero precision, the
    set of possible representable values for the result is determined
    by the precision of the `MathContext` argument. For example
    in `BigDecimal`, if a nonzero three-digit number and a
    nonzero four-digit number are multiplied together in the context of
    a `MathContext` object having a precision of three, the
    result will have three digits (assuming no overflow or underflow,
    etc.).
    
    The rounding policies implemented by `BigDecimal`
    operations indicated by RoundingMode rounding modes
    are a proper superset of the IEEE 754 rounding-direction
    attributes.
    
    `BigDecimal` arithmetic will most resemble IEEE 754
    decimal arithmetic if a `MathContext` corresponding to an
    IEEE 754 decimal format, such as MathContext.DECIMAL64
    decimal64 or MathContext.DECIMAL128 decimal128 is
    used to round all starting values and intermediate operations. The
    numerical values computed can differ if the exponent range of the
    IEEE 754 format being approximated is exceeded since a `MathContext` does not constrain the scale of `BigDecimal`
    results. Operations that would generate a NaN or exact infinity,
    such as dividing by zero, throw an `ArithmeticException` in
    `BigDecimal` arithmetic.
    """

    ZERO = ZERO_THROUGH_TEN[0]
    """
    The value 0, with a scale of 0.

    Since
    - 1.5
    """
    ONE = ZERO_THROUGH_TEN[1]
    """
    The value 1, with a scale of 0.

    Since
    - 1.5
    """
    TEN = ZERO_THROUGH_TEN[10]
    """
    The value 10, with a scale of 0.

    Since
    - 1.5
    """
    ROUND_UP = 0
    """
    Rounding mode to round away from zero.  Always increments the
    digit prior to a nonzero discarded fraction.  Note that this rounding
    mode never decreases the magnitude of the calculated value.

    Deprecated
    - Use RoundingMode.UP instead.
    """
    ROUND_DOWN = 1
    """
    Rounding mode to round towards zero.  Never increments the digit
    prior to a discarded fraction (i.e., truncates).  Note that this
    rounding mode never increases the magnitude of the calculated value.

    Deprecated
    - Use RoundingMode.DOWN instead.
    """
    ROUND_CEILING = 2
    """
    Rounding mode to round towards positive infinity.  If the
    `BigDecimal` is positive, behaves as for
    `ROUND_UP`; if negative, behaves as for
    `ROUND_DOWN`.  Note that this rounding mode never
    decreases the calculated value.

    Deprecated
    - Use RoundingMode.CEILING instead.
    """
    ROUND_FLOOR = 3
    """
    Rounding mode to round towards negative infinity.  If the
    `BigDecimal` is positive, behave as for
    `ROUND_DOWN`; if negative, behave as for
    `ROUND_UP`.  Note that this rounding mode never
    increases the calculated value.

    Deprecated
    - Use RoundingMode.FLOOR instead.
    """
    ROUND_HALF_UP = 4
    """
    Rounding mode to round towards "nearest neighbor"
    unless both neighbors are equidistant, in which case round up.
    Behaves as for `ROUND_UP` if the discarded fraction is
    &ge; 0.5; otherwise, behaves as for `ROUND_DOWN`.  Note
    that this is the rounding mode that most of us were taught in
    grade school.

    Deprecated
    - Use RoundingMode.HALF_UP instead.
    """
    ROUND_HALF_DOWN = 5
    """
    Rounding mode to round towards "nearest neighbor"
    unless both neighbors are equidistant, in which case round
    down.  Behaves as for `ROUND_UP` if the discarded
    fraction is > 0.5; otherwise, behaves as for
    `ROUND_DOWN`.

    Deprecated
    - Use RoundingMode.HALF_DOWN instead.
    """
    ROUND_HALF_EVEN = 6
    """
    Rounding mode to round towards the "nearest neighbor"
    unless both neighbors are equidistant, in which case, round
    towards the even neighbor.  Behaves as for
    `ROUND_HALF_UP` if the digit to the left of the
    discarded fraction is odd; behaves as for
    `ROUND_HALF_DOWN` if it's even.  Note that this is the
    rounding mode that minimizes cumulative error when applied
    repeatedly over a sequence of calculations.

    Deprecated
    - Use RoundingMode.HALF_EVEN instead.
    """
    ROUND_UNNECESSARY = 7
    """
    Rounding mode to assert that the requested operation has an exact
    result, hence no rounding is necessary.  If this rounding mode is
    specified on an operation that yields an inexact result, an
    `ArithmeticException` is thrown.

    Deprecated
    - Use RoundingMode.UNNECESSARY instead.
    """


    def __init__(self, in: list[str], offset: int, len: int):
        """
        Translates a character array representation of a
        `BigDecimal` into a `BigDecimal`, accepting the
        same sequence of characters as the .BigDecimal(String)
        constructor, while allowing a sub-array to be specified.

        Arguments
        - in: `char` array that is the source of characters.
        - offset: first character in the array to inspect.
        - len: number of characters to consider.

        Raises
        - NumberFormatException: if `in` is not a valid
                representation of a `BigDecimal` or the defined subarray
                is not wholly within `in`.

        Since
        - 1.5

        Unknown Tags
        - If the sequence of characters is already available
        within a character array, using this constructor is faster than
        converting the `char` array to string and using the
        `BigDecimal(String)` constructor.
        """
        ...


    def __init__(self, in: list[str], offset: int, len: int, mc: "MathContext"):
        """
        Translates a character array representation of a
        `BigDecimal` into a `BigDecimal`, accepting the
        same sequence of characters as the .BigDecimal(String)
        constructor, while allowing a sub-array to be specified and
        with rounding according to the context settings.

        Arguments
        - in: `char` array that is the source of characters.
        - offset: first character in the array to inspect.
        - len: number of characters to consider.
        - mc: the context to use.

        Raises
        - NumberFormatException: if `in` is not a valid
                representation of a `BigDecimal` or the defined subarray
                is not wholly within `in`.

        Since
        - 1.5

        Unknown Tags
        - If the sequence of characters is already available
        within a character array, using this constructor is faster than
        converting the `char` array to string and using the
        `BigDecimal(String)` constructor.
        """
        ...


    def __init__(self, in: list[str]):
        """
        Translates a character array representation of a
        `BigDecimal` into a `BigDecimal`, accepting the
        same sequence of characters as the .BigDecimal(String)
        constructor.

        Arguments
        - in: `char` array that is the source of characters.

        Raises
        - NumberFormatException: if `in` is not a valid
                representation of a `BigDecimal`.

        Since
        - 1.5

        Unknown Tags
        - If the sequence of characters is already available
        as a character array, using this constructor is faster than
        converting the `char` array to string and using the
        `BigDecimal(String)` constructor.
        """
        ...


    def __init__(self, in: list[str], mc: "MathContext"):
        """
        Translates a character array representation of a
        `BigDecimal` into a `BigDecimal`, accepting the
        same sequence of characters as the .BigDecimal(String)
        constructor and with rounding according to the context
        settings.

        Arguments
        - in: `char` array that is the source of characters.
        - mc: the context to use.

        Raises
        - NumberFormatException: if `in` is not a valid
                representation of a `BigDecimal`.

        Since
        - 1.5

        Unknown Tags
        - If the sequence of characters is already available
        as a character array, using this constructor is faster than
        converting the `char` array to string and using the
        `BigDecimal(String)` constructor.
        """
        ...


    def __init__(self, val: str):
        """
        Translates the string representation of a `BigDecimal`
        into a `BigDecimal`.  The string representation consists
        of an optional sign, `'+'` (` '&#92;u002B'`) or
        `'-'` (`'&#92;u002D'`), followed by a sequence of
        zero or more decimal digits ("the integer"), optionally
        followed by a fraction, optionally followed by an exponent.
        
        The fraction consists of a decimal point followed by zero
        or more decimal digits.  The string must contain at least one
        digit in either the integer or the fraction.  The number formed
        by the sign, the integer and the fraction is referred to as the
        *significand*.
        
        The exponent consists of the character `'e'`
        (`'&#92;u0065'`) or `'E'` (`'&#92;u0045'`)
        followed by one or more decimal digits.  The value of the
        exponent must lie between -Integer.MAX_VALUE (Integer.MIN_VALUE+1) and Integer.MAX_VALUE, inclusive.
        
        More formally, the strings this constructor accepts are
        described by the following grammar:
        <blockquote>
        <dl>
        <dt>*BigDecimalString:*
        <dd>*Sign<sub>opt</sub> Significand Exponent<sub>opt</sub>*
        <dt>*Sign:*
        <dd>`+`
        <dd>`-`
        <dt>*Significand:*
        <dd>*IntegerPart* `.` *FractionPart<sub>opt</sub>*
        <dd>`.` *FractionPart*
        <dd>*IntegerPart*
        <dt>*IntegerPart:*
        <dd>*Digits*
        <dt>*FractionPart:*
        <dd>*Digits*
        <dt>*Exponent:*
        <dd>*ExponentIndicator SignedInteger*
        <dt>*ExponentIndicator:*
        <dd>`e`
        <dd>`E`
        <dt>*SignedInteger:*
        <dd>*Sign<sub>opt</sub> Digits*
        <dt>*Digits:*
        <dd>*Digit*
        <dd>*Digits Digit*
        <dt>*Digit:*
        <dd>any character for which Character.isDigit
        returns `True`, including 0, 1, 2 ...
        </dl>
        </blockquote>
        
        The scale of the returned `BigDecimal` will be the
        number of digits in the fraction, or zero if the string
        contains no decimal point, subject to adjustment for any
        exponent; if the string contains an exponent, the exponent is
        subtracted from the scale.  The value of the resulting scale
        must lie between `Integer.MIN_VALUE` and
        `Integer.MAX_VALUE`, inclusive.
        
        The character-to-digit mapping is provided by java.lang.Character.digit set to convert to radix 10.  The
        String may not contain any extraneous characters (whitespace,
        for example).
        
        **Examples:**
        The value of the returned `BigDecimal` is equal to
        *significand* &times; 10<sup>&nbsp;*exponent*</sup>.
        For each string on the left, the resulting representation
        [`BigInteger`, `scale`] is shown on the right.
        ```
        "0"            [0,0]
        "0.00"         [0,2]
        "123"          [123,0]
        "-123"         [-123,0]
        "1.23E3"       [123,-1]
        "1.23E+3"      [123,-1]
        "12.3E+7"      [123,-6]
        "12.0"         [120,1]
        "12.3"         [123,1]
        "0.00123"      [123,5]
        "-1.23E-12"    [-123,14]
        "1234.5E-4"    [12345,5]
        "0E+7"         [0,-7]
        "-0"           [0,0]
        ```

        Arguments
        - val: String representation of `BigDecimal`.

        Raises
        - NumberFormatException: if `val` is not a valid
                representation of a `BigDecimal`.

        Unknown Tags
        - For values other than `float` and
        `double` NaN and &plusmn;Infinity, this constructor is
        compatible with the values returned by Float.toString
        and Double.toString.  This is generally the preferred
        way to convert a `float` or `double` into a
        BigDecimal, as it doesn't suffer from the unpredictability of
        the .BigDecimal(double) constructor.
        """
        ...


    def __init__(self, val: str, mc: "MathContext"):
        """
        Translates the string representation of a `BigDecimal`
        into a `BigDecimal`, accepting the same strings as the
        .BigDecimal(String) constructor, with rounding
        according to the context settings.

        Arguments
        - val: string representation of a `BigDecimal`.
        - mc: the context to use.

        Raises
        - NumberFormatException: if `val` is not a valid
                representation of a BigDecimal.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: float):
        """
        Translates a `double` into a `BigDecimal` which
        is the exact decimal representation of the `double`'s
        binary floating-point value.  The scale of the returned
        `BigDecimal` is the smallest value such that
        `(10<sup>scale</sup> &times; val)` is an integer.
        
        **Notes:**
        <ol>
        - 
        The results of this constructor can be somewhat unpredictable.
        One might assume that writing `new BigDecimal(0.1)` in
        Java creates a `BigDecimal` which is exactly equal to
        0.1 (an unscaled value of 1, with a scale of 1), but it is
        actually equal to
        0.1000000000000000055511151231257827021181583404541015625.
        This is because 0.1 cannot be represented exactly as a
        `double` (or, for that matter, as a binary fraction of
        any finite length).  Thus, the value that is being passed
        *in* to the constructor is not exactly equal to 0.1,
        appearances notwithstanding.
        
        - 
        The `String` constructor, on the other hand, is
        perfectly predictable: writing `new BigDecimal("0.1")`
        creates a `BigDecimal` which is *exactly* equal to
        0.1, as one would expect.  Therefore, it is generally
        recommended that the .BigDecimal(String)
        String constructor be used in preference to this one.
        
        - 
        When a `double` must be used as a source for a
        `BigDecimal`, note that this constructor provides an
        exact conversion; it does not give the same result as
        converting the `double` to a `String` using the
        Double.toString(double) method and then using the
        .BigDecimal(String) constructor.  To get that result,
        use the `static` .valueOf(double) method.
        </ol>

        Arguments
        - val: `double` value to be converted to
               `BigDecimal`.

        Raises
        - NumberFormatException: if `val` is infinite or NaN.
        """
        ...


    def __init__(self, val: float, mc: "MathContext"):
        """
        Translates a `double` into a `BigDecimal`, with
        rounding according to the context settings.  The scale of the
        `BigDecimal` is the smallest value such that
        `(10<sup>scale</sup> &times; val)` is an integer.
        
        The results of this constructor can be somewhat unpredictable
        and its use is generally not recommended; see the notes under
        the .BigDecimal(double) constructor.

        Arguments
        - val: `double` value to be converted to
                `BigDecimal`.
        - mc: the context to use.

        Raises
        - NumberFormatException: if `val` is infinite or NaN.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: "BigInteger"):
        """
        Translates a `BigInteger` into a `BigDecimal`.
        The scale of the `BigDecimal` is zero.

        Arguments
        - val: `BigInteger` value to be converted to
                   `BigDecimal`.
        """
        ...


    def __init__(self, val: "BigInteger", mc: "MathContext"):
        """
        Translates a `BigInteger` into a `BigDecimal`
        rounding according to the context settings.  The scale of the
        `BigDecimal` is zero.

        Arguments
        - val: `BigInteger` value to be converted to
                   `BigDecimal`.
        - mc: the context to use.

        Since
        - 1.5
        """
        ...


    def __init__(self, unscaledVal: "BigInteger", scale: int):
        """
        Translates a `BigInteger` unscaled value and an
        `int` scale into a `BigDecimal`.  The value of
        the `BigDecimal` is
        `(unscaledVal &times; 10<sup>-scale</sup>)`.

        Arguments
        - unscaledVal: unscaled value of the `BigDecimal`.
        - scale: scale of the `BigDecimal`.
        """
        ...


    def __init__(self, unscaledVal: "BigInteger", scale: int, mc: "MathContext"):
        """
        Translates a `BigInteger` unscaled value and an
        `int` scale into a `BigDecimal`, with rounding
        according to the context settings.  The value of the
        `BigDecimal` is `(unscaledVal &times;
        10<sup>-scale</sup>)`, rounded according to the
        `precision` and rounding mode settings.

        Arguments
        - unscaledVal: unscaled value of the `BigDecimal`.
        - scale: scale of the `BigDecimal`.
        - mc: the context to use.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: int):
        """
        Translates an `int` into a `BigDecimal`.  The
        scale of the `BigDecimal` is zero.

        Arguments
        - val: `int` value to be converted to
                   `BigDecimal`.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: int, mc: "MathContext"):
        """
        Translates an `int` into a `BigDecimal`, with
        rounding according to the context settings.  The scale of the
        `BigDecimal`, before any rounding, is zero.

        Arguments
        - val: `int` value to be converted to `BigDecimal`.
        - mc: the context to use.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: int):
        """
        Translates a `long` into a `BigDecimal`.  The
        scale of the `BigDecimal` is zero.

        Arguments
        - val: `long` value to be converted to `BigDecimal`.

        Since
        - 1.5
        """
        ...


    def __init__(self, val: int, mc: "MathContext"):
        """
        Translates a `long` into a `BigDecimal`, with
        rounding according to the context settings.  The scale of the
        `BigDecimal`, before any rounding, is zero.

        Arguments
        - val: `long` value to be converted to `BigDecimal`.
        - mc: the context to use.

        Since
        - 1.5
        """
        ...


    @staticmethod
    def valueOf(unscaledVal: int, scale: int) -> "BigDecimal":
        """
        Translates a `long` unscaled value and an
        `int` scale into a `BigDecimal`.

        Arguments
        - unscaledVal: unscaled value of the `BigDecimal`.
        - scale: scale of the `BigDecimal`.

        Returns
        - a `BigDecimal` whose value is
                `(unscaledVal &times; 10<sup>-scale</sup>)`.

        Unknown Tags
        - This static factory method is provided in preference
        to a (`long`, `int`) constructor because it allows
        for reuse of frequently used `BigDecimal` values.
        """
        ...


    @staticmethod
    def valueOf(val: int) -> "BigDecimal":
        """
        Translates a `long` value into a `BigDecimal`
        with a scale of zero.

        Arguments
        - val: value of the `BigDecimal`.

        Returns
        - a `BigDecimal` whose value is `val`.

        Unknown Tags
        - This static factory method is provided in preference
        to a (`long`) constructor because it allows for reuse of
        frequently used `BigDecimal` values.
        """
        ...


    @staticmethod
    def valueOf(val: float) -> "BigDecimal":
        """
        Translates a `double` into a `BigDecimal`, using
        the `double`'s canonical string representation provided
        by the Double.toString(double) method.

        Arguments
        - val: `double` to convert to a `BigDecimal`.

        Returns
        - a `BigDecimal` whose value is equal to or approximately
                equal to the value of `val`.

        Raises
        - NumberFormatException: if `val` is infinite or NaN.

        Since
        - 1.5

        Unknown Tags
        - This is generally the preferred way to convert a
        `double` (or `float`) into a `BigDecimal`, as
        the value returned is equal to that resulting from constructing
        a `BigDecimal` from the result of using Double.toString(double).
        """
        ...


    def add(self, augend: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this +
        augend)`, and whose scale is `max(this.scale(),
        augend.scale())`.

        Arguments
        - augend: value to be added to this `BigDecimal`.

        Returns
        - `this + augend`
        """
        ...


    def add(self, augend: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this + augend)`,
        with rounding according to the context settings.
        
        If either number is zero and the precision setting is nonzero then
        the other number, rounded if necessary, is used as the result.

        Arguments
        - augend: value to be added to this `BigDecimal`.
        - mc: the context to use.

        Returns
        - `this + augend`, rounded as necessary.

        Since
        - 1.5
        """
        ...


    def subtract(self, subtrahend: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this -
        subtrahend)`, and whose scale is `max(this.scale(),
        subtrahend.scale())`.

        Arguments
        - subtrahend: value to be subtracted from this `BigDecimal`.

        Returns
        - `this - subtrahend`
        """
        ...


    def subtract(self, subtrahend: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this - subtrahend)`,
        with rounding according to the context settings.
        
        If `subtrahend` is zero then this, rounded if necessary, is used as the
        result.  If this is zero then the result is `subtrahend.negate(mc)`.

        Arguments
        - subtrahend: value to be subtracted from this `BigDecimal`.
        - mc: the context to use.

        Returns
        - `this - subtrahend`, rounded as necessary.

        Since
        - 1.5
        """
        ...


    def multiply(self, multiplicand: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this &times;
        multiplicand)`, and whose scale is `(this.scale() +
        multiplicand.scale())`.

        Arguments
        - multiplicand: value to be multiplied by this `BigDecimal`.

        Returns
        - `this * multiplicand`
        """
        ...


    def multiply(self, multiplicand: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this &times;
        multiplicand)`, with rounding according to the context settings.

        Arguments
        - multiplicand: value to be multiplied by this `BigDecimal`.
        - mc: the context to use.

        Returns
        - `this * multiplicand`, rounded as necessary.

        Since
        - 1.5
        """
        ...


    def divide(self, divisor: "BigDecimal", scale: int, roundingMode: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, and whose scale is as specified.  If rounding must
        be performed to generate a result with the specified scale, the
        specified rounding mode is applied.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - scale: scale of the `BigDecimal` quotient to be returned.
        - roundingMode: rounding mode to apply.

        Returns
        - `this / divisor`

        Raises
        - ArithmeticException: if `divisor` is zero,
                `roundingMode==ROUND_UNNECESSARY` and
                the specified scale is insufficient to represent the result
                of the division exactly.
        - IllegalArgumentException: if `roundingMode` does not
                represent a valid rounding mode.

        See
        - .ROUND_UNNECESSARY

        Deprecated
        - The method .divide(BigDecimal, int, RoundingMode)
        should be used in preference to this legacy method.
        """
        ...


    def divide(self, divisor: "BigDecimal", scale: int, roundingMode: "RoundingMode") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, and whose scale is as specified.  If rounding must
        be performed to generate a result with the specified scale, the
        specified rounding mode is applied.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - scale: scale of the `BigDecimal` quotient to be returned.
        - roundingMode: rounding mode to apply.

        Returns
        - `this / divisor`

        Raises
        - ArithmeticException: if `divisor` is zero,
                `roundingMode==RoundingMode.UNNECESSARY` and
                the specified scale is insufficient to represent the result
                of the division exactly.

        Since
        - 1.5
        """
        ...


    def divide(self, divisor: "BigDecimal", roundingMode: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, and whose scale is `this.scale()`.  If
        rounding must be performed to generate a result with the given
        scale, the specified rounding mode is applied.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - roundingMode: rounding mode to apply.

        Returns
        - `this / divisor`

        Raises
        - ArithmeticException: if `divisor==0`, or
                `roundingMode==ROUND_UNNECESSARY` and
                `this.scale()` is insufficient to represent the result
                of the division exactly.
        - IllegalArgumentException: if `roundingMode` does not
                represent a valid rounding mode.

        See
        - .ROUND_UNNECESSARY

        Deprecated
        - The method .divide(BigDecimal, RoundingMode)
        should be used in preference to this legacy method.
        """
        ...


    def divide(self, divisor: "BigDecimal", roundingMode: "RoundingMode") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, and whose scale is `this.scale()`.  If
        rounding must be performed to generate a result with the given
        scale, the specified rounding mode is applied.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - roundingMode: rounding mode to apply.

        Returns
        - `this / divisor`

        Raises
        - ArithmeticException: if `divisor==0`, or
                `roundingMode==RoundingMode.UNNECESSARY` and
                `this.scale()` is insufficient to represent the result
                of the division exactly.

        Since
        - 1.5
        """
        ...


    def divide(self, divisor: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, and whose preferred scale is `(this.scale() -
        divisor.scale())`; if the exact quotient cannot be
        represented (because it has a non-terminating decimal
        expansion) an `ArithmeticException` is thrown.

    Author(s)
        - Joseph D. Darcy

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.

        Returns
        - `this / divisor`

        Raises
        - ArithmeticException: if the exact quotient does not have a
                terminating decimal expansion, including dividing by zero

        Since
        - 1.5
        """
        ...


    def divide(self, divisor: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this /
        divisor)`, with rounding according to the context settings.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - mc: the context to use.

        Returns
        - `this / divisor`, rounded as necessary.

        Raises
        - ArithmeticException: if the result is inexact but the
                rounding mode is `UNNECESSARY` or
                `mc.precision == 0` and the quotient has a
                non-terminating decimal expansion,including dividing by zero

        Since
        - 1.5
        """
        ...


    def divideToIntegralValue(self, divisor: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is the integer part
        of the quotient `(this / divisor)` rounded down.  The
        preferred scale of the result is `(this.scale() -
        divisor.scale())`.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.

        Returns
        - The integer part of `this / divisor`.

        Raises
        - ArithmeticException: if `divisor==0`

        Since
        - 1.5
        """
        ...


    def divideToIntegralValue(self, divisor: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is the integer part
        of `(this / divisor)`.  Since the integer part of the
        exact quotient does not depend on the rounding mode, the
        rounding mode does not affect the values returned by this
        method.  The preferred scale of the result is
        `(this.scale() - divisor.scale())`.  An
        `ArithmeticException` is thrown if the integer part of
        the exact quotient needs more than `mc.precision`
        digits.

    Author(s)
        - Joseph D. Darcy

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - mc: the context to use.

        Returns
        - The integer part of `this / divisor`.

        Raises
        - ArithmeticException: if `divisor==0`
        - ArithmeticException: if `mc.precision` > 0 and the result
                requires a precision of more than `mc.precision` digits.

        Since
        - 1.5
        """
        ...


    def remainder(self, divisor: "BigDecimal") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this % divisor)`.
        
        The remainder is given by
        `this.subtract(this.divideToIntegralValue(divisor).multiply(divisor))`.
        Note that this is *not* the modulo operation (the result can be
        negative).

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.

        Returns
        - `this % divisor`.

        Raises
        - ArithmeticException: if `divisor==0`

        Since
        - 1.5
        """
        ...


    def remainder(self, divisor: "BigDecimal", mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(this %
        divisor)`, with rounding according to the context settings.
        The `MathContext` settings affect the implicit divide
        used to compute the remainder.  The remainder computation
        itself is by definition exact.  Therefore, the remainder may
        contain more than `mc.getPrecision()` digits.
        
        The remainder is given by
        `this.subtract(this.divideToIntegralValue(divisor,
        mc).multiply(divisor))`.  Note that this is not the modulo
        operation (the result can be negative).

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided.
        - mc: the context to use.

        Returns
        - `this % divisor`, rounded as necessary.

        Raises
        - ArithmeticException: if `divisor==0`
        - ArithmeticException: if the result is inexact but the
                rounding mode is `UNNECESSARY`, or `mc.precision`
                > 0 and the result of `this.divideToIntegralValue(divisor)` would
                require a precision of more than `mc.precision` digits.

        See
        - .divideToIntegralValue(java.math.BigDecimal, java.math.MathContext)

        Since
        - 1.5
        """
        ...


    def divideAndRemainder(self, divisor: "BigDecimal") -> list["BigDecimal"]:
        """
        Returns a two-element `BigDecimal` array containing the
        result of `divideToIntegralValue` followed by the result of
        `remainder` on the two operands.
        
        Note that if both the integer quotient and remainder are
        needed, this method is faster than using the
        `divideToIntegralValue` and `remainder` methods
        separately because the division need only be carried out once.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided,
                and the remainder computed.

        Returns
        - a two element `BigDecimal` array: the quotient
                (the result of `divideToIntegralValue`) is the initial element
                and the remainder is the final element.

        Raises
        - ArithmeticException: if `divisor==0`

        See
        - .remainder(java.math.BigDecimal, java.math.MathContext)

        Since
        - 1.5
        """
        ...


    def divideAndRemainder(self, divisor: "BigDecimal", mc: "MathContext") -> list["BigDecimal"]:
        """
        Returns a two-element `BigDecimal` array containing the
        result of `divideToIntegralValue` followed by the result of
        `remainder` on the two operands calculated with rounding
        according to the context settings.
        
        Note that if both the integer quotient and remainder are
        needed, this method is faster than using the
        `divideToIntegralValue` and `remainder` methods
        separately because the division need only be carried out once.

        Arguments
        - divisor: value by which this `BigDecimal` is to be divided,
                and the remainder computed.
        - mc: the context to use.

        Returns
        - a two element `BigDecimal` array: the quotient
                (the result of `divideToIntegralValue`) is the
                initial element and the remainder is the final element.

        Raises
        - ArithmeticException: if `divisor==0`
        - ArithmeticException: if the result is inexact but the
                rounding mode is `UNNECESSARY`, or `mc.precision`
                > 0 and the result of `this.divideToIntegralValue(divisor)` would
                require a precision of more than `mc.precision` digits.

        See
        - .remainder(java.math.BigDecimal, java.math.MathContext)

        Since
        - 1.5
        """
        ...


    def sqrt(self, mc: "MathContext") -> "BigDecimal":
        """
        Returns an approximation to the square root of `this`
        with rounding according to the context settings.
        
        The preferred scale of the returned result is equal to
        `this.scale()/2`. The value of the returned result is
        always within one ulp of the exact decimal value for the
        precision in question.  If the rounding mode is RoundingMode.HALF_UP HALF_UP, RoundingMode.HALF_DOWN
        HALF_DOWN, or RoundingMode.HALF_EVEN HALF_EVEN, the
        result is within one half an ulp of the exact decimal value.
        
        Special case:
        
        -  The square root of a number numerically equal to `ZERO` is numerically equal to `ZERO` with a preferred
        scale according to the general rule above. In particular, for
        `ZERO`, `ZERO.sqrt(mc).equals(ZERO)` is True with
        any `MathContext` as an argument.

        Arguments
        - mc: the context to use.

        Returns
        - the square root of `this`.

        Raises
        - ArithmeticException: if `this` is less than zero.
        - ArithmeticException: if an exact result is requested
        (`mc.getPrecision()==0`) and there is no finite decimal
        expansion of the exact result
        - ArithmeticException: if
        `(mc.getRoundingMode()==RoundingMode.UNNECESSARY`) and
        the exact result cannot fit in `mc.getPrecision()`
        digits.

        See
        - BigInteger.sqrt()

        Since
        - 9
        """
        ...


    def pow(self, n: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is
        `(this<sup>n</sup>)`, The power is computed exactly, to
        unlimited precision.
        
        The parameter `n` must be in the range 0 through
        999999999, inclusive.  `ZERO.pow(0)` returns .ONE.
        
        Note that future releases may expand the allowable exponent
        range of this method.

        Arguments
        - n: power to raise this `BigDecimal` to.

        Returns
        - `this<sup>n</sup>`

        Raises
        - ArithmeticException: if `n` is out of range.

        Since
        - 1.5
        """
        ...


    def pow(self, n: int, mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is
        `(this<sup>n</sup>)`.  The current implementation uses
        the core algorithm defined in ANSI standard X3.274-1996 with
        rounding according to the context settings.  In general, the
        returned numerical value is within two ulps of the exact
        numerical value for the chosen precision.  Note that future
        releases may use a different algorithm with a decreased
        allowable error bound and increased allowable exponent range.
        
        The X3.274-1996 algorithm is:
        
        
        -  An `ArithmeticException` exception is thrown if
         
           - `abs(n) > 999999999`
           - `mc.precision == 0` and `n < 0`
           - `mc.precision > 0` and `n` has more than
           `mc.precision` decimal digits
         
        
        -  if `n` is zero, .ONE is returned even if
        `this` is zero, otherwise
        
          -  if `n` is positive, the result is calculated via
          the repeated squaring technique into a single accumulator.
          The individual multiplications with the accumulator use the
          same math context settings as in `mc` except for a
          precision increased to `mc.precision + elength + 1`
          where `elength` is the number of decimal digits in
          `n`.
        
          -  if `n` is negative, the result is calculated as if
          `n` were positive; this value is then divided into one
          using the working precision specified above.
        
          -  The final value from either the positive or negative case
          is then rounded to the destination precision.
          

        Arguments
        - n: power to raise this `BigDecimal` to.
        - mc: the context to use.

        Returns
        - `this<sup>n</sup>` using the ANSI standard X3.274-1996
                algorithm

        Raises
        - ArithmeticException: if the result is inexact but the
                rounding mode is `UNNECESSARY`, or `n` is out
                of range.

        Since
        - 1.5
        """
        ...


    def abs(self) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is the absolute value
        of this `BigDecimal`, and whose scale is
        `this.scale()`.

        Returns
        - `abs(this)`
        """
        ...


    def abs(self, mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is the absolute value
        of this `BigDecimal`, with rounding according to the
        context settings.

        Arguments
        - mc: the context to use.

        Returns
        - `abs(this)`, rounded as necessary.

        Since
        - 1.5
        """
        ...


    def negate(self) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(-this)`,
        and whose scale is `this.scale()`.

        Returns
        - `-this`.
        """
        ...


    def negate(self, mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(-this)`,
        with rounding according to the context settings.

        Arguments
        - mc: the context to use.

        Returns
        - `-this`, rounded as necessary.

        Since
        - 1.5
        """
        ...


    def plus(self) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(+this)`, and whose
        scale is `this.scale()`.
        
        This method, which simply returns this `BigDecimal`
        is included for symmetry with the unary minus method .negate().

        Returns
        - `this`.

        See
        - .negate()

        Since
        - 1.5
        """
        ...


    def plus(self, mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose value is `(+this)`,
        with rounding according to the context settings.
        
        The effect of this method is identical to that of the .round(MathContext) method.

        Arguments
        - mc: the context to use.

        Returns
        - `this`, rounded as necessary.  A zero result will
                have a scale of 0.

        See
        - .round(MathContext)

        Since
        - 1.5
        """
        ...


    def signum(self) -> int:
        """
        Returns the signum function of this `BigDecimal`.

        Returns
        - -1, 0, or 1 as the value of this `BigDecimal`
                is negative, zero, or positive.
        """
        ...


    def scale(self) -> int:
        """
        Returns the *scale* of this `BigDecimal`.  If zero
        or positive, the scale is the number of digits to the right of
        the decimal point.  If negative, the unscaled value of the
        number is multiplied by ten to the power of the negation of the
        scale.  For example, a scale of `-3` means the unscaled
        value is multiplied by 1000.

        Returns
        - the scale of this `BigDecimal`.
        """
        ...


    def precision(self) -> int:
        """
        Returns the *precision* of this `BigDecimal`.  (The
        precision is the number of digits in the unscaled value.)
        
        The precision of a zero value is 1.

        Returns
        - the precision of this `BigDecimal`.

        Since
        - 1.5
        """
        ...


    def unscaledValue(self) -> "BigInteger":
        """
        Returns a `BigInteger` whose value is the *unscaled
        value* of this `BigDecimal`.  (Computes `(this *
        10<sup>this.scale()</sup>)`.)

        Returns
        - the unscaled value of this `BigDecimal`.

        Since
        - 1.2
        """
        ...


    def round(self, mc: "MathContext") -> "BigDecimal":
        """
        Returns a `BigDecimal` rounded according to the
        `MathContext` settings.  If the precision setting is 0 then
        no rounding takes place.
        
        The effect of this method is identical to that of the
        .plus(MathContext) method.

        Arguments
        - mc: the context to use.

        Returns
        - a `BigDecimal` rounded according to the
                `MathContext` settings.

        See
        - .plus(MathContext)

        Since
        - 1.5
        """
        ...


    def setScale(self, newScale: int, roundingMode: "RoundingMode") -> "BigDecimal":
        """
        Returns a `BigDecimal` whose scale is the specified
        value, and whose unscaled value is determined by multiplying or
        dividing this `BigDecimal`'s unscaled value by the
        appropriate power of ten to maintain its overall value.  If the
        scale is reduced by the operation, the unscaled value must be
        divided (rather than multiplied), and the value may be changed;
        in this case, the specified rounding mode is applied to the
        division.

        Arguments
        - newScale: scale of the `BigDecimal` value to be returned.
        - roundingMode: The rounding mode to apply.

        Returns
        - a `BigDecimal` whose scale is the specified value,
                and whose unscaled value is determined by multiplying or
                dividing this `BigDecimal`'s unscaled value by the
                appropriate power of ten to maintain its overall value.

        Raises
        - ArithmeticException: if `roundingMode==UNNECESSARY`
                and the specified scaling operation would require
                rounding.

        See
        - RoundingMode

        Since
        - 1.5

        Unknown Tags
        - Since BigDecimal objects are immutable, calls of
        this method do *not* result in the original object being
        modified, contrary to the usual convention of having methods
        named `set*X*` mutate field *`X`*.
        Instead, `setScale` returns an object with the proper
        scale; the returned object may or may not be newly allocated.
        """
        ...


    def setScale(self, newScale: int, roundingMode: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose scale is the specified
        value, and whose unscaled value is determined by multiplying or
        dividing this `BigDecimal`'s unscaled value by the
        appropriate power of ten to maintain its overall value.  If the
        scale is reduced by the operation, the unscaled value must be
        divided (rather than multiplied), and the value may be changed;
        in this case, the specified rounding mode is applied to the
        division.

        Arguments
        - newScale: scale of the `BigDecimal` value to be returned.
        - roundingMode: The rounding mode to apply.

        Returns
        - a `BigDecimal` whose scale is the specified value,
                and whose unscaled value is determined by multiplying or
                dividing this `BigDecimal`'s unscaled value by the
                appropriate power of ten to maintain its overall value.

        Raises
        - ArithmeticException: if `roundingMode==ROUND_UNNECESSARY`
                and the specified scaling operation would require
                rounding.
        - IllegalArgumentException: if `roundingMode` does not
                represent a valid rounding mode.

        See
        - .ROUND_UNNECESSARY

        Deprecated
        - The method .setScale(int, RoundingMode) should
        be used in preference to this legacy method.

        Unknown Tags
        - Since BigDecimal objects are immutable, calls of
        this method do *not* result in the original object being
        modified, contrary to the usual convention of having methods
        named `set*X*` mutate field *`X`*.
        Instead, `setScale` returns an object with the proper
        scale; the returned object may or may not be newly allocated.
        """
        ...


    def setScale(self, newScale: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` whose scale is the specified
        value, and whose value is numerically equal to this
        `BigDecimal`'s.  Throws an `ArithmeticException`
        if this is not possible.
        
        This call is typically used to increase the scale, in which
        case it is guaranteed that there exists a `BigDecimal`
        of the specified scale and the correct value.  The call can
        also be used to reduce the scale if the caller knows that the
        `BigDecimal` has sufficiently many zeros at the end of
        its fractional part (i.e., factors of ten in its integer value)
        to allow for the rescaling without changing its value.
        
        This method returns the same result as the two-argument
        versions of `setScale`, but saves the caller the trouble
        of specifying a rounding mode in cases where it is irrelevant.

        Arguments
        - newScale: scale of the `BigDecimal` value to be returned.

        Returns
        - a `BigDecimal` whose scale is the specified value, and
                whose unscaled value is determined by multiplying or dividing
                this `BigDecimal`'s unscaled value by the appropriate
                power of ten to maintain its overall value.

        Raises
        - ArithmeticException: if the specified scaling operation would
                require rounding.

        See
        - .setScale(int, RoundingMode)

        Unknown Tags
        - Since `BigDecimal` objects are immutable,
        calls of this method do *not* result in the original
        object being modified, contrary to the usual convention of
        having methods named `set*X*` mutate field
        *`X`*.  Instead, `setScale` returns an
        object with the proper scale; the returned object may or may
        not be newly allocated.
        """
        ...


    def movePointLeft(self, n: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` which is equivalent to this one
        with the decimal point moved `n` places to the left.  If
        `n` is non-negative, the call merely adds `n` to
        the scale.  If `n` is negative, the call is equivalent
        to `movePointRight(-n)`.  The `BigDecimal`
        returned by this call has value `(this &times;
        10<sup>-n</sup>)` and scale `max(this.scale()+n,
        0)`.

        Arguments
        - n: number of places to move the decimal point to the left.

        Returns
        - a `BigDecimal` which is equivalent to this one with the
                decimal point moved `n` places to the left.

        Raises
        - ArithmeticException: if scale overflows.
        """
        ...


    def movePointRight(self, n: int) -> "BigDecimal":
        """
        Returns a `BigDecimal` which is equivalent to this one
        with the decimal point moved `n` places to the right.
        If `n` is non-negative, the call merely subtracts
        `n` from the scale.  If `n` is negative, the call
        is equivalent to `movePointLeft(-n)`.  The
        `BigDecimal` returned by this call has value `(this
        &times; 10<sup>n</sup>)` and scale `max(this.scale()-n,
        0)`.

        Arguments
        - n: number of places to move the decimal point to the right.

        Returns
        - a `BigDecimal` which is equivalent to this one
                with the decimal point moved `n` places to the right.

        Raises
        - ArithmeticException: if scale overflows.
        """
        ...


    def scaleByPowerOfTen(self, n: int) -> "BigDecimal":
        """
        Returns a BigDecimal whose numerical value is equal to
        (`this` * 10<sup>n</sup>).  The scale of
        the result is `(this.scale() - n)`.

        Arguments
        - n: the exponent power of ten to scale by

        Returns
        - a BigDecimal whose numerical value is equal to
        (`this` * 10<sup>n</sup>)

        Raises
        - ArithmeticException: if the scale would be
                outside the range of a 32-bit integer.

        Since
        - 1.5
        """
        ...


    def stripTrailingZeros(self) -> "BigDecimal":
        """
        Returns a `BigDecimal` which is numerically equal to
        this one but with any trailing zeros removed from the
        representation.  For example, stripping the trailing zeros from
        the `BigDecimal` value `600.0`, which has
        [`BigInteger`, `scale`] components equal to
        [6000, 1], yields `6E2` with [`BigInteger`,
        `scale`] components equal to [6, -2].  If
        this BigDecimal is numerically equal to zero, then
        `BigDecimal.ZERO` is returned.

        Returns
        - a numerically equal `BigDecimal` with any
        trailing zeros removed.

        Raises
        - ArithmeticException: if scale overflows.

        Since
        - 1.5
        """
        ...


    def compareTo(self, val: "BigDecimal") -> int:
        """
        Compares this `BigDecimal` numerically with the specified
        `BigDecimal`.  Two `BigDecimal` objects that are
        equal in value but have a different scale (like 2.0 and 2.00)
        are considered equal by this method. Such values are in the
        same *cohort*.
        
        This method is provided in preference to individual methods for
        each of the six boolean comparison operators (<, ==,
        >, >=, !=, <=).  The suggested
        idiom for performing these comparisons is: `(x.compareTo(y)` &lt;*op*&gt; `0)`, where
        &lt;*op*&gt; is one of the six comparison operators.

        Arguments
        - val: `BigDecimal` to which this `BigDecimal` is
                to be compared.

        Returns
        - -1, 0, or 1 as this `BigDecimal` is numerically
                 less than, equal to, or greater than `val`.

        Unknown Tags
        - Note: this class has a natural ordering that is inconsistent with equals.
        """
        ...


    def equals(self, x: "Object") -> bool:
        """
        Compares this `BigDecimal` with the specified `Object` for equality.  Unlike .compareTo(BigDecimal)
        compareTo, this method considers two `BigDecimal`
        objects equal only if they are equal in value and
        scale. Therefore 2.0 is not equal to 2.00 when compared by this
        method since the former has [`BigInteger`, `scale`]
        components equal to [20, 1] while the latter has components
        equal to [200, 2].

        Arguments
        - x: `Object` to which this `BigDecimal` is
                to be compared.

        Returns
        - `True` if and only if the specified `Object` is a
                `BigDecimal` whose value and scale are equal to this
                `BigDecimal`'s.

        See
        - .hashCode

        Unknown Tags
        - One example that shows how 2.0 and 2.00 are *not*
        substitutable for each other under some arithmetic operations
        are the two expressions:
        `new BigDecimal("2.0" ).divide(BigDecimal.valueOf(3),
        HALF_UP)` which evaluates to 0.7 and 
        `new BigDecimal("2.00").divide(BigDecimal.valueOf(3),
        HALF_UP)` which evaluates to 0.67.
        """
        ...


    def min(self, val: "BigDecimal") -> "BigDecimal":
        """
        Returns the minimum of this `BigDecimal` and
        `val`.

        Arguments
        - val: value with which the minimum is to be computed.

        Returns
        - the `BigDecimal` whose value is the lesser of this
                `BigDecimal` and `val`.  If they are equal,
                as defined by the .compareTo(BigDecimal) compareTo
                method, `this` is returned.

        See
        - .compareTo(java.math.BigDecimal)
        """
        ...


    def max(self, val: "BigDecimal") -> "BigDecimal":
        """
        Returns the maximum of this `BigDecimal` and `val`.

        Arguments
        - val: value with which the maximum is to be computed.

        Returns
        - the `BigDecimal` whose value is the greater of this
                `BigDecimal` and `val`.  If they are equal,
                as defined by the .compareTo(BigDecimal) compareTo
                method, `this` is returned.

        See
        - .compareTo(java.math.BigDecimal)
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this `BigDecimal`.
        The hash code is computed as a function of the unscaledValue() unscaled value and the scale()
        scale of this `BigDecimal`.

        Returns
        - hash code for this `BigDecimal`.

        See
        - .equals(Object)

        Unknown Tags
        - Two `BigDecimal` objects that are numerically equal but
        differ in scale (like 2.0 and 2.00) will generally *not*
        have the same hash code.
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this `BigDecimal`,
        using scientific notation if an exponent is needed.
        
        A standard canonical string form of the `BigDecimal`
        is created as though by the following steps: first, the
        absolute value of the unscaled value of the `BigDecimal`
        is converted to a string in base ten using the characters
        `'0'` through `'9'` with no leading zeros (except
        if its value is zero, in which case a single `'0'`
        character is used).
        
        Next, an *adjusted exponent* is calculated; this is the
        negated scale, plus the number of characters in the converted
        unscaled value, less one.  That is,
        `-scale+(ulength-1)`, where `ulength` is the
        length of the absolute value of the unscaled value in decimal
        digits (its *precision*).
        
        If the scale is greater than or equal to zero and the
        adjusted exponent is greater than or equal to `-6`, the
        number will be converted to a character form without using
        exponential notation.  In this case, if the scale is zero then
        no decimal point is added and if the scale is positive a
        decimal point will be inserted with the scale specifying the
        number of characters to the right of the decimal point.
        `'0'` characters are added to the left of the converted
        unscaled value as necessary.  If no character precedes the
        decimal point after this insertion then a conventional
        `'0'` character is prefixed.
        
        Otherwise (that is, if the scale is negative, or the
        adjusted exponent is less than `-6`), the number will be
        converted to a character form using exponential notation.  In
        this case, if the converted `BigInteger` has more than
        one digit a decimal point is inserted after the first digit.
        An exponent in character form is then suffixed to the converted
        unscaled value (perhaps with inserted decimal point); this
        comprises the letter `'E'` followed immediately by the
        adjusted exponent converted to a character form.  The latter is
        in base ten, using the characters `'0'` through
        `'9'` with no leading zeros, and is always prefixed by a
        sign character `'-'` (`'&#92;u002D'`) if the
        adjusted exponent is negative, `'+'`
        (`'&#92;u002B'`) otherwise).
        
        Finally, the entire string is prefixed by a minus sign
        character `'-'` (`'&#92;u002D'`) if the unscaled
        value is less than zero.  No sign character is prefixed if the
        unscaled value is zero or positive.
        
        **Examples:**
        For each representation [*unscaled value*, *scale*]
        on the left, the resulting string is shown on the right.
        ```
        [123,0]      "123"
        [-123,0]     "-123"
        [123,-1]     "1.23E+3"
        [123,-3]     "1.23E+5"
        [123,1]      "12.3"
        [123,5]      "0.00123"
        [123,10]     "1.23E-8"
        [-123,12]    "-1.23E-10"
        ```
        
        **Notes:**
        <ol>
        
        - There is a one-to-one mapping between the distinguishable
        `BigDecimal` values and the result of this conversion.
        That is, every distinguishable `BigDecimal` value
        (unscaled value and scale) has a unique string representation
        as a result of using `toString`.  If that string
        representation is converted back to a `BigDecimal` using
        the .BigDecimal(String) constructor, then the original
        value will be recovered.
        
        - The string produced for a given number is always the same;
        it is not affected by locale.  This means that it can be used
        as a canonical string representation for exchanging decimal
        data, or as a key for a Hashtable, etc.  Locale-sensitive
        number formatting and parsing is handled by the java.text.NumberFormat class and its subclasses.
        
        - The .toEngineeringString method may be used for
        presenting numbers with exponents in engineering notation, and the
        .setScale(int,RoundingMode) setScale method may be used for
        rounding a `BigDecimal` so it has a known number of digits after
        the decimal point.
        
        - The digit-to-character mapping provided by
        `Character.forDigit` is used.
        
        </ol>

        Returns
        - string representation of this `BigDecimal`.

        See
        - .BigDecimal(java.lang.String)
        """
        ...


    def toEngineeringString(self) -> str:
        """
        Returns a string representation of this `BigDecimal`,
        using engineering notation if an exponent is needed.
        
        Returns a string that represents the `BigDecimal` as
        described in the .toString() method, except that if
        exponential notation is used, the power of ten is adjusted to
        be a multiple of three (engineering notation) such that the
        integer part of nonzero values will be in the range 1 through
        999.  If exponential notation is used for zero values, a
        decimal point and one or two fractional zero digits are used so
        that the scale of the zero value is preserved.  Note that
        unlike the output of .toString(), the output of this
        method is *not* guaranteed to recover the same [integer,
        scale] pair of this `BigDecimal` if the output string is
        converting back to a `BigDecimal` using the .BigDecimal(String) string constructor.  The result of this method meets
        the weaker constraint of always producing a numerically equal
        result from applying the string constructor to the method's output.

        Returns
        - string representation of this `BigDecimal`, using
                engineering notation if an exponent is needed.

        Since
        - 1.5
        """
        ...


    def toPlainString(self) -> str:
        """
        Returns a string representation of this `BigDecimal`
        without an exponent field.  For values with a positive scale,
        the number of digits to the right of the decimal point is used
        to indicate scale.  For values with a zero or negative scale,
        the resulting string is generated as if the value were
        converted to a numerically equal value with zero scale and as
        if all the trailing zeros of the zero scale value were present
        in the result.
        
        The entire string is prefixed by a minus sign character '-'
        (`'&#92;u002D'`) if the unscaled value is less than
        zero. No sign character is prefixed if the unscaled value is
        zero or positive.
        
        Note that if the result of this method is passed to the
        .BigDecimal(String) string constructor, only the
        numerical value of this `BigDecimal` will necessarily be
        recovered; the representation of the new `BigDecimal`
        may have a different scale.  In particular, if this
        `BigDecimal` has a negative scale, the string resulting
        from this method will have a scale of zero when processed by
        the string constructor.
        
        (This method behaves analogously to the `toString`
        method in 1.4 and earlier releases.)

        Returns
        - a string representation of this `BigDecimal`
        without an exponent field.

        See
        - .toEngineeringString()

        Since
        - 1.5
        """
        ...


    def toBigInteger(self) -> "BigInteger":
        """
        Converts this `BigDecimal` to a `BigInteger`.
        This conversion is analogous to the
        *narrowing primitive conversion* from `double` to
        `long` as defined in
        <cite>The Java Language Specification</cite>:
        any fractional part of this
        `BigDecimal` will be discarded.  Note that this
        conversion can lose information about the precision of the
        `BigDecimal` value.
        
        To have an exception thrown if the conversion is inexact (in
        other words if a nonzero fractional part is discarded), use the
        .toBigIntegerExact() method.

        Returns
        - this `BigDecimal` converted to a `BigInteger`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def toBigIntegerExact(self) -> "BigInteger":
        """
        Converts this `BigDecimal` to a `BigInteger`,
        checking for lost information.  An exception is thrown if this
        `BigDecimal` has a nonzero fractional part.

        Returns
        - this `BigDecimal` converted to a `BigInteger`.

        Raises
        - ArithmeticException: if `this` has a nonzero
                fractional part.

        Since
        - 1.5
        """
        ...


    def longValue(self) -> int:
        """
        Converts this `BigDecimal` to a `long`.
        This conversion is analogous to the
        *narrowing primitive conversion* from `double` to
        `short` as defined in
        <cite>The Java Language Specification</cite>:
        any fractional part of this
        `BigDecimal` will be discarded, and if the resulting
        "`BigInteger`" is too big to fit in a
        `long`, only the low-order 64 bits are returned.
        Note that this conversion can lose information about the
        overall magnitude and precision of this `BigDecimal` value as well
        as return a result with the opposite sign.

        Returns
        - this `BigDecimal` converted to a `long`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def longValueExact(self) -> int:
        """
        Converts this `BigDecimal` to a `long`, checking
        for lost information.  If this `BigDecimal` has a
        nonzero fractional part or is out of the possible range for a
        `long` result then an `ArithmeticException` is
        thrown.

        Returns
        - this `BigDecimal` converted to a `long`.

        Raises
        - ArithmeticException: if `this` has a nonzero
                fractional part, or will not fit in a `long`.

        Since
        - 1.5
        """
        ...


    def intValue(self) -> int:
        """
        Converts this `BigDecimal` to an `int`.
        This conversion is analogous to the
        *narrowing primitive conversion* from `double` to
        `short` as defined in
        <cite>The Java Language Specification</cite>:
        any fractional part of this
        `BigDecimal` will be discarded, and if the resulting
        "`BigInteger`" is too big to fit in an
        `int`, only the low-order 32 bits are returned.
        Note that this conversion can lose information about the
        overall magnitude and precision of this `BigDecimal`
        value as well as return a result with the opposite sign.

        Returns
        - this `BigDecimal` converted to an `int`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def intValueExact(self) -> int:
        """
        Converts this `BigDecimal` to an `int`, checking
        for lost information.  If this `BigDecimal` has a
        nonzero fractional part or is out of the possible range for an
        `int` result then an `ArithmeticException` is
        thrown.

        Returns
        - this `BigDecimal` converted to an `int`.

        Raises
        - ArithmeticException: if `this` has a nonzero
                fractional part, or will not fit in an `int`.

        Since
        - 1.5
        """
        ...


    def shortValueExact(self) -> int:
        """
        Converts this `BigDecimal` to a `short`, checking
        for lost information.  If this `BigDecimal` has a
        nonzero fractional part or is out of the possible range for a
        `short` result then an `ArithmeticException` is
        thrown.

        Returns
        - this `BigDecimal` converted to a `short`.

        Raises
        - ArithmeticException: if `this` has a nonzero
                fractional part, or will not fit in a `short`.

        Since
        - 1.5
        """
        ...


    def byteValueExact(self) -> int:
        """
        Converts this `BigDecimal` to a `byte`, checking
        for lost information.  If this `BigDecimal` has a
        nonzero fractional part or is out of the possible range for a
        `byte` result then an `ArithmeticException` is
        thrown.

        Returns
        - this `BigDecimal` converted to a `byte`.

        Raises
        - ArithmeticException: if `this` has a nonzero
                fractional part, or will not fit in a `byte`.

        Since
        - 1.5
        """
        ...


    def floatValue(self) -> float:
        """
        Converts this `BigDecimal` to a `float`.
        This conversion is similar to the
        *narrowing primitive conversion* from `double` to
        `float` as defined in
        <cite>The Java Language Specification</cite>:
        if this `BigDecimal` has too great a
        magnitude to represent as a `float`, it will be
        converted to Float.NEGATIVE_INFINITY or Float.POSITIVE_INFINITY as appropriate.  Note that even when
        the return value is finite, this conversion can lose
        information about the precision of the `BigDecimal`
        value.

        Returns
        - this `BigDecimal` converted to a `float`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def doubleValue(self) -> float:
        """
        Converts this `BigDecimal` to a `double`.
        This conversion is similar to the
        *narrowing primitive conversion* from `double` to
        `float` as defined in
        <cite>The Java Language Specification</cite>:
        if this `BigDecimal` has too great a
        magnitude represent as a `double`, it will be
        converted to Double.NEGATIVE_INFINITY or Double.POSITIVE_INFINITY as appropriate.  Note that even when
        the return value is finite, this conversion can lose
        information about the precision of the `BigDecimal`
        value.

        Returns
        - this `BigDecimal` converted to a `double`.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def ulp(self) -> "BigDecimal":
        """
        Returns the size of an ulp, a unit in the last place, of this
        `BigDecimal`.  An ulp of a nonzero `BigDecimal`
        value is the positive distance between this value and the
        `BigDecimal` value next larger in magnitude with the
        same number of digits.  An ulp of a zero value is numerically
        equal to 1 with the scale of `this`.  The result is
        stored with the same scale as `this` so the result
        for zero and nonzero values is equal to `[1,
        this.scale()]`.

        Returns
        - the size of an ulp of `this`

        Since
        - 1.5
        """
        ...
