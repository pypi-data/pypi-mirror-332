"""
Python module generated from Java source file java.math.RoundingMode

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.math import *
from typing import Any, Callable, Iterable, Tuple


class RoundingMode(Enum):
    """
    Specifies a *rounding policy* for numerical operations capable
    of discarding precision. Each rounding mode indicates how the least
    significant returned digit of a rounded result is to be calculated.
    If fewer digits are returned than the digits needed to represent
    the exact numerical result, the discarded digits will be referred
    to as the *discarded fraction* regardless the digits'
    contribution to the value of the number.  In other words,
    considered as a numerical value, the discarded fraction could have
    an absolute value greater than one.
    
    Each rounding mode description includes a table listing how
    different two-digit decimal values would round to a one digit
    decimal value under the rounding mode in question.  The result
    column in the tables could be gotten by creating a
    `BigDecimal` number with the specified value, forming a
    MathContext object with the proper settings
    (`precision` set to `1`, and the
    `roundingMode` set to the rounding mode in question), and
    calling BigDecimal.round round on this number with the
    proper `MathContext`.  A summary table showing the results
    of these rounding operations for all rounding modes appears below.
    
    <table class="striped">
    <caption>**Summary of Rounding Operations Under Different Rounding Modes**</caption>
    <thead>
    <tr><th scope="col" rowspan="2">Input Number</th><th scope="col"colspan=8>Result of rounding input to one digit with the given
                              rounding mode</th>
    <tr style="vertical-align:top">
                                  <th>`UP`</th>
                                              <th>`DOWN`</th>
                                                           <th>`CEILING`</th>
                                                                          <th>`FLOOR`</th>
                                                                                       <th>`HALF_UP`</th>
                                                                                                      <th>`HALF_DOWN`</th>
                                                                                                                       <th>`HALF_EVEN`</th>
                                                                                                                                        <th>`UNNECESSARY`</th>
    </thead>
    <tbody style="text-align:right">
    
    <tr><th scope="row">5.5</th>  <td>6</td>  <td>5</td>    <td>6</td>    <td>5</td>  <td>6</td>      <td>5</td>       <td>6</td>       <td>throw `ArithmeticException`</td>
    <tr><th scope="row">2.5</th>  <td>3</td>  <td>2</td>    <td>3</td>    <td>2</td>  <td>3</td>      <td>2</td>       <td>2</td>       <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.6</th>  <td>2</td>  <td>1</td>    <td>2</td>    <td>1</td>  <td>2</td>      <td>2</td>       <td>2</td>       <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.1</th>  <td>2</td>  <td>1</td>    <td>2</td>    <td>1</td>  <td>1</td>      <td>1</td>       <td>1</td>       <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.0</th>  <td>1</td>  <td>1</td>    <td>1</td>    <td>1</td>  <td>1</td>      <td>1</td>       <td>1</td>       <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td> <td>-1</td>   <td>-1</td>   <td>-1</td> <td>-1</td>     <td>-1</td>      <td>-1</td>      <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-2</td> <td>-1</td>   <td>-1</td>   <td>-2</td> <td>-1</td>     <td>-1</td>      <td>-1</td>      <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-1.6</th> <td>-2</td> <td>-1</td>   <td>-1</td>   <td>-2</td> <td>-2</td>     <td>-2</td>      <td>-2</td>      <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-2.5</th> <td>-3</td> <td>-2</td>   <td>-2</td>   <td>-3</td> <td>-3</td>     <td>-2</td>      <td>-2</td>      <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-5.5</th> <td>-6</td> <td>-5</td>   <td>-5</td>   <td>-6</td> <td>-6</td>     <td>-5</td>      <td>-6</td>      <td>throw `ArithmeticException`</td>
    </tbody>
    </table>
    
    
    This `enum` is intended to replace the integer-based
    enumeration of rounding mode constants in BigDecimal
    (BigDecimal.ROUND_UP, BigDecimal.ROUND_DOWN,
    etc. ).

    Author(s)
    - Joseph D. Darcy

    See
    - MathContext

    Since
    - 1.5

    Unknown Tags
    - Five of the rounding modes declared in this class correspond to
    rounding-direction attributes defined in the <cite>IEEE Standard
    for Floating-Point Arithmetic</cite>, IEEE 754-2019. Where present,
    this correspondence will be noted in the documentation of the
    particular constant.
    """

    UP = (BigDecimal.ROUND_UP)
    """
    Rounding mode to round away from zero.  Always increments the
    digit prior to a non-zero discarded fraction.  Note that this
    rounding mode never decreases the magnitude of the calculated
    value.
    
    Example:
    <table class="striped">
    <caption>Rounding mode UP Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `UP` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>6</td>
    <tr><th scope="row">2.5</th>  <td>3</td>
    <tr><th scope="row">1.6</th>  <td>2</td>
    <tr><th scope="row">1.1</th>  <td>2</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-2</td>
    <tr><th scope="row">-1.6</th> <td>-2</td>
    <tr><th scope="row">-2.5</th> <td>-3</td>
    <tr><th scope="row">-5.5</th> <td>-6</td>
    </tbody>
    </table>
    """
    DOWN = (BigDecimal.ROUND_DOWN)
    """
    Rounding mode to round towards zero.  Never increments the digit
    prior to a discarded fraction (i.e., truncates).  Note that this
    rounding mode never increases the magnitude of the calculated value.
    This mode corresponds to the IEEE 754-2019 rounding-direction
    attribute roundTowardZero.
    
    Example:
    <table class="striped">
    <caption>Rounding mode DOWN Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `DOWN` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>5</td>
    <tr><th scope="row">2.5</th>  <td>2</td>
    <tr><th scope="row">1.6</th>  <td>1</td>
    <tr><th scope="row">1.1</th>  <td>1</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-1</td>
    <tr><th scope="row">-1.6</th> <td>-1</td>
    <tr><th scope="row">-2.5</th> <td>-2</td>
    <tr><th scope="row">-5.5</th> <td>-5</td>
    </tbody>
    </table>
    """
    CEILING = (BigDecimal.ROUND_CEILING)
    """
    Rounding mode to round towards positive infinity.  If the
    result is positive, behaves as for `RoundingMode.UP`;
    if negative, behaves as for `RoundingMode.DOWN`.  Note
    that this rounding mode never decreases the calculated value.
    This mode corresponds to the IEEE 754-2019 rounding-direction
    attribute roundTowardPositive.
    
    Example:
    <table class="striped">
    <caption>Rounding mode CEILING Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th>Input Number</th>
       <th>Input rounded to one digit with `CEILING` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>6</td>
    <tr><th scope="row">2.5</th>  <td>3</td>
    <tr><th scope="row">1.6</th>  <td>2</td>
    <tr><th scope="row">1.1</th>  <td>2</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-1</td>
    <tr><th scope="row">-1.6</th> <td>-1</td>
    <tr><th scope="row">-2.5</th> <td>-2</td>
    <tr><th scope="row">-5.5</th> <td>-5</td>
    </tbody>
    </table>
    """
    FLOOR = (BigDecimal.ROUND_FLOOR)
    """
    Rounding mode to round towards negative infinity.  If the
    result is positive, behave as for `RoundingMode.DOWN`;
    if negative, behave as for `RoundingMode.UP`.  Note that
    this rounding mode never increases the calculated value.
    This mode corresponds to the IEEE 754-2019 rounding-direction
    attribute roundTowardNegative.
    
    Example:
    <table class="striped">
    <caption>Rounding mode FLOOR Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `FLOOR` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>5</td>
    <tr><th scope="row">2.5</th>  <td>2</td>
    <tr><th scope="row">1.6</th>  <td>1</td>
    <tr><th scope="row">1.1</th>  <td>1</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-2</td>
    <tr><th scope="row">-1.6</th> <td>-2</td>
    <tr><th scope="row">-2.5</th> <td>-3</td>
    <tr><th scope="row">-5.5</th> <td>-6</td>
    </tbody>
    </table>
    """
    HALF_UP = (BigDecimal.ROUND_HALF_UP)
    """
    Rounding mode to round towards "nearest neighbor"
    unless both neighbors are equidistant, in which case round up.
    Behaves as for `RoundingMode.UP` if the discarded
    fraction is &ge; 0.5; otherwise, behaves as for
    `RoundingMode.DOWN`.  Note that this is the rounding
    mode commonly taught at school.
    This mode corresponds to the IEEE 754-2019 rounding-direction
    attribute roundTiesToAway.
    
    Example:
    <table class="striped">
    <caption>Rounding mode HALF_UP Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `HALF_UP` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>6</td>
    <tr><th scope="row">2.5</th>  <td>3</td>
    <tr><th scope="row">1.6</th>  <td>2</td>
    <tr><th scope="row">1.1</th>  <td>1</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-1</td>
    <tr><th scope="row">-1.6</th> <td>-2</td>
    <tr><th scope="row">-2.5</th> <td>-3</td>
    <tr><th scope="row">-5.5</th> <td>-6</td>
    </tbody>
    </table>
    """
    HALF_DOWN = (BigDecimal.ROUND_HALF_DOWN)
    """
    Rounding mode to round towards "nearest neighbor"
    unless both neighbors are equidistant, in which case round
    down.  Behaves as for `RoundingMode.UP` if the discarded
    fraction is &gt; 0.5; otherwise, behaves as for
    `RoundingMode.DOWN`.
    
    Example:
    <table class="striped">
    <caption>Rounding mode HALF_DOWN Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `HALF_DOWN` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>5</td>
    <tr><th scope="row">2.5</th>  <td>2</td>
    <tr><th scope="row">1.6</th>  <td>2</td>
    <tr><th scope="row">1.1</th>  <td>1</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-1</td>
    <tr><th scope="row">-1.6</th> <td>-2</td>
    <tr><th scope="row">-2.5</th> <td>-2</td>
    <tr><th scope="row">-5.5</th> <td>-5</td>
    </tbody>
    </table>
    """
    HALF_EVEN = (BigDecimal.ROUND_HALF_EVEN)
    """
    Rounding mode to round towards the "nearest neighbor"
    unless both neighbors are equidistant, in which case, round
    towards the even neighbor.  Behaves as for
    `RoundingMode.HALF_UP` if the digit to the left of the
    discarded fraction is odd; behaves as for
    `RoundingMode.HALF_DOWN` if it's even.  Note that this
    is the rounding mode that statistically minimizes cumulative
    error when applied repeatedly over a sequence of calculations.
    It is sometimes known as "Banker's rounding," and is
    chiefly used in the USA.  This rounding mode is analogous to
    the rounding policy used for `float` and `double`
    arithmetic in Java.
    This mode corresponds to the IEEE 754-2019 rounding-direction
    attribute roundTiesToEven.
    
    Example:
    <table class="striped">
    <caption>Rounding mode HALF_EVEN Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `HALF_EVEN` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>6</td>
    <tr><th scope="row">2.5</th>  <td>2</td>
    <tr><th scope="row">1.6</th>  <td>2</td>
    <tr><th scope="row">1.1</th>  <td>1</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>-1</td>
    <tr><th scope="row">-1.6</th> <td>-2</td>
    <tr><th scope="row">-2.5</th> <td>-2</td>
    <tr><th scope="row">-5.5</th> <td>-6</td>
    </tbody>
    </table>
    """
    UNNECESSARY = (BigDecimal.ROUND_UNNECESSARY)
    """
    Rounding mode to assert that the requested operation has an exact
    result, hence no rounding is necessary.  If this rounding mode is
    specified on an operation that yields an inexact result, an
    `ArithmeticException` is thrown.
    Example:
    <table class="striped">
    <caption>Rounding mode UNNECESSARY Examples</caption>
    <thead>
    <tr style="vertical-align:top"><th scope="col">Input Number</th>
       <th scope="col">Input rounded to one digit with `UNNECESSARY` rounding
    </thead>
    <tbody style="text-align:right">
    <tr><th scope="row">5.5</th>  <td>throw `ArithmeticException`</td>
    <tr><th scope="row">2.5</th>  <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.6</th>  <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.1</th>  <td>throw `ArithmeticException`</td>
    <tr><th scope="row">1.0</th>  <td>1</td>
    <tr><th scope="row">-1.0</th> <td>-1</td>
    <tr><th scope="row">-1.1</th> <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-1.6</th> <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-2.5</th> <td>throw `ArithmeticException`</td>
    <tr><th scope="row">-5.5</th> <td>throw `ArithmeticException`</td>
    </tbody>
    </table>
    """


    @staticmethod
    def valueOf(rm: int) -> "RoundingMode":
        """
        Returns the `RoundingMode` object corresponding to a
        legacy integer rounding mode constant in BigDecimal.

        Arguments
        - rm: legacy integer rounding mode to convert

        Returns
        - `RoundingMode` corresponding to the given integer.

        Raises
        - IllegalArgumentException: integer is out of range
        """
        ...
