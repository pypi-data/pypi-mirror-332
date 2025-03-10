"""
Python module generated from Java source file java.time.Duration

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import DataInput
from java.io import DataOutput
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.math import BigDecimal
from java.math import BigInteger
from java.math import RoundingMode
from java.time import *
from java.time.format import DateTimeParseException
from java.time.temporal import ChronoField
from java.time.temporal import ChronoUnit
from java.time.temporal import Temporal
from java.time.temporal import TemporalAmount
from java.time.temporal import TemporalUnit
from java.time.temporal import UnsupportedTemporalTypeException
from java.util import Objects
from java.util.regex import Matcher
from java.util.regex import Pattern
from typing import Any, Callable, Iterable, Tuple


class Duration(TemporalAmount, Comparable, Serializable):
    """
    A time-based amount of time, such as '34.5 seconds'.
    
    This class models a quantity or amount of time in terms of seconds and nanoseconds.
    It can be accessed using other duration-based units, such as minutes and hours.
    In addition, the ChronoUnit.DAYS DAYS unit can be used and is treated as
    exactly equal to 24 hours, thus ignoring daylight savings effects.
    See Period for the date-based equivalent to this class.
    
    A physical duration could be of infinite length.
    For practicality, the duration is stored with constraints similar to Instant.
    The duration uses nanosecond resolution with a maximum value of the seconds that can
    be held in a `long`. This is greater than the current estimated age of the universe.
    
    The range of a duration requires the storage of a number larger than a `long`.
    To achieve this, the class stores a `long` representing seconds and an `int`
    representing nanosecond-of-second, which will always be between 0 and 999,999,999.
    The model is of a directed duration, meaning that the duration may be negative.
    
    The duration is measured in "seconds", but these are not necessarily identical to
    the scientific "SI second" definition based on atomic clocks.
    This difference only impacts durations measured near a leap-second and should not affect
    most applications.
    See Instant for a discussion as to the meaning of the second and time-scales.
    
    This is a <a href="/java.base/java/lang/doc-files/ValueBased.html">value-based</a>
    class; programmers should treat instances that are
    .equals(Object) equal as interchangeable and should not
    use instances for synchronization, or unpredictable behavior may
    occur. For example, in a future release, synchronization may fail.
    The `equals` method should be used for comparisons.

    Since
    - 1.8

    Unknown Tags
    - This class is immutable and thread-safe.
    """

    ZERO = Duration(0, 0)
    """
    Constant for a duration of zero.
    """


    @staticmethod
    def ofDays(days: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of standard 24 hour days.
        
        The seconds are calculated based on the standard definition of a day,
        where each day is 86400 seconds which implies a 24 hour day.
        The nanosecond in second field is set to zero.

        Arguments
        - days: the number of days, positive or negative

        Returns
        - a `Duration`, not null

        Raises
        - ArithmeticException: if the input days exceeds the capacity of `Duration`
        """
        ...


    @staticmethod
    def ofHours(hours: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of standard hours.
        
        The seconds are calculated based on the standard definition of an hour,
        where each hour is 3600 seconds.
        The nanosecond in second field is set to zero.

        Arguments
        - hours: the number of hours, positive or negative

        Returns
        - a `Duration`, not null

        Raises
        - ArithmeticException: if the input hours exceeds the capacity of `Duration`
        """
        ...


    @staticmethod
    def ofMinutes(minutes: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of standard minutes.
        
        The seconds are calculated based on the standard definition of a minute,
        where each minute is 60 seconds.
        The nanosecond in second field is set to zero.

        Arguments
        - minutes: the number of minutes, positive or negative

        Returns
        - a `Duration`, not null

        Raises
        - ArithmeticException: if the input minutes exceeds the capacity of `Duration`
        """
        ...


    @staticmethod
    def ofSeconds(seconds: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of seconds.
        
        The nanosecond in second field is set to zero.

        Arguments
        - seconds: the number of seconds, positive or negative

        Returns
        - a `Duration`, not null
        """
        ...


    @staticmethod
    def ofSeconds(seconds: int, nanoAdjustment: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of seconds and an
        adjustment in nanoseconds.
        
        This method allows an arbitrary number of nanoseconds to be passed in.
        The factory will alter the values of the second and nanosecond in order
        to ensure that the stored nanosecond is in the range 0 to 999,999,999.
        For example, the following will result in exactly the same duration:
        ```
         Duration.ofSeconds(3, 1);
         Duration.ofSeconds(4, -999_999_999);
         Duration.ofSeconds(2, 1000_000_001);
        ```

        Arguments
        - seconds: the number of seconds, positive or negative
        - nanoAdjustment: the nanosecond adjustment to the number of seconds, positive or negative

        Returns
        - a `Duration`, not null

        Raises
        - ArithmeticException: if the adjustment causes the seconds to exceed the capacity of `Duration`
        """
        ...


    @staticmethod
    def ofMillis(millis: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of milliseconds.
        
        The seconds and nanoseconds are extracted from the specified milliseconds.

        Arguments
        - millis: the number of milliseconds, positive or negative

        Returns
        - a `Duration`, not null
        """
        ...


    @staticmethod
    def ofNanos(nanos: int) -> "Duration":
        """
        Obtains a `Duration` representing a number of nanoseconds.
        
        The seconds and nanoseconds are extracted from the specified nanoseconds.

        Arguments
        - nanos: the number of nanoseconds, positive or negative

        Returns
        - a `Duration`, not null
        """
        ...


    @staticmethod
    def of(amount: int, unit: "TemporalUnit") -> "Duration":
        """
        Obtains a `Duration` representing an amount in the specified unit.
        
        The parameters represent the two parts of a phrase like '6 Hours'. For example:
        ```
         Duration.of(3, SECONDS);
         Duration.of(465, HOURS);
        ```
        Only a subset of units are accepted by this method.
        The unit must either have an TemporalUnit.isDurationEstimated() exact duration or
        be ChronoUnit.DAYS which is treated as 24 hours. Other units throw an exception.

        Arguments
        - amount: the amount of the duration, measured in terms of the unit, positive or negative
        - unit: the unit that the duration is measured in, must have an exact duration, not null

        Returns
        - a `Duration`, not null

        Raises
        - DateTimeException: if the period unit has an estimated duration
        - ArithmeticException: if a numeric overflow occurs
        """
        ...


    @staticmethod
    def from(amount: "TemporalAmount") -> "Duration":
        """
        Obtains an instance of `Duration` from a temporal amount.
        
        This obtains a duration based on the specified amount.
        A `TemporalAmount` represents an  amount of time, which may be
        date-based or time-based, which this factory extracts to a duration.
        
        The conversion loops around the set of units from the amount and uses
        the TemporalUnit.getDuration() duration of the unit to
        calculate the total `Duration`.
        Only a subset of units are accepted by this method. The unit must either
        have an TemporalUnit.isDurationEstimated() exact duration
        or be ChronoUnit.DAYS which is treated as 24 hours.
        If any other units are found then an exception is thrown.

        Arguments
        - amount: the temporal amount to convert, not null

        Returns
        - the equivalent duration, not null

        Raises
        - DateTimeException: if unable to convert to a `Duration`
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    @staticmethod
    def parse(text: "CharSequence") -> "Duration":
        """
        Obtains a `Duration` from a text string such as `PnDTnHnMn.nS`.
        
        This will parse a textual representation of a duration, including the
        string produced by `toString()`. The formats accepted are based
        on the ISO-8601 duration format `PnDTnHnMn.nS` with days
        considered to be exactly 24 hours.
        
        The string starts with an optional sign, denoted by the ASCII negative
        or positive symbol. If negative, the whole period is negated.
        The ASCII letter "P" is next in upper or lower case.
        There are then four sections, each consisting of a number and a suffix.
        The sections have suffixes in ASCII of "D", "H", "M" and "S" for
        days, hours, minutes and seconds, accepted in upper or lower case.
        The suffixes must occur in order. The ASCII letter "T" must occur before
        the first occurrence, if any, of an hour, minute or second section.
        At least one of the four sections must be present, and if "T" is present
        there must be at least one section after the "T".
        The number part of each section must consist of one or more ASCII digits.
        The number may be prefixed by the ASCII negative or positive symbol.
        The number of days, hours and minutes must parse to a `long`.
        The number of seconds must parse to a `long` with optional fraction.
        The decimal point may be either a dot or a comma.
        The fractional part may have from zero to 9 digits.
        
        The leading plus/minus sign, and negative values for other units are
        not part of the ISO-8601 standard.
        
        Examples:
        ```
           "PT20.345S" -- parses as "20.345 seconds"
           "PT15M"     -- parses as "15 minutes" (where a minute is 60 seconds)
           "PT10H"     -- parses as "10 hours" (where an hour is 3600 seconds)
           "P2D"       -- parses as "2 days" (where a day is 24 hours or 86400 seconds)
           "P2DT3H4M"  -- parses as "2 days, 3 hours and 4 minutes"
           "PT-6H3M"    -- parses as "-6 hours and +3 minutes"
           "-PT6H3M"    -- parses as "-6 hours and -3 minutes"
           "-PT-6H+3M"  -- parses as "+6 hours and -3 minutes"
        ```

        Arguments
        - text: the text to parse, not null

        Returns
        - the parsed duration, not null

        Raises
        - DateTimeParseException: if the text cannot be parsed to a duration
        """
        ...


    @staticmethod
    def between(startInclusive: "Temporal", endExclusive: "Temporal") -> "Duration":
        """
        Obtains a `Duration` representing the duration between two temporal objects.
        
        This calculates the duration between two temporal objects. If the objects
        are of different types, then the duration is calculated based on the type
        of the first object. For example, if the first argument is a `LocalTime`
        then the second argument is converted to a `LocalTime`.
        
        The specified temporal objects must support the ChronoUnit.SECONDS SECONDS unit.
        For full accuracy, either the ChronoUnit.NANOS NANOS unit or the
        ChronoField.NANO_OF_SECOND NANO_OF_SECOND field should be supported.
        
        The result of this method can be a negative period if the end is before the start.
        To guarantee to obtain a positive duration call .abs() on the result.

        Arguments
        - startInclusive: the start instant, inclusive, not null
        - endExclusive: the end instant, exclusive, not null

        Returns
        - a `Duration`, not null

        Raises
        - DateTimeException: if the seconds between the temporals cannot be obtained
        - ArithmeticException: if the calculation exceeds the capacity of `Duration`
        """
        ...


    def get(self, unit: "TemporalUnit") -> int:
        """
        Gets the value of the requested unit.
        
        This returns a value for each of the two supported units,
        ChronoUnit.SECONDS SECONDS and ChronoUnit.NANOS NANOS.
        All other units throw an exception.

        Arguments
        - unit: the `TemporalUnit` for which to return the value

        Returns
        - the long value of the unit

        Raises
        - DateTimeException: if the unit is not supported
        - UnsupportedTemporalTypeException: if the unit is not supported
        """
        ...


    def getUnits(self) -> list["TemporalUnit"]:
        """
        Gets the set of units supported by this duration.
        
        The supported units are ChronoUnit.SECONDS SECONDS,
        and ChronoUnit.NANOS NANOS.
        They are returned in the order seconds, nanos.
        
        This set can be used in conjunction with .get(TemporalUnit)
        to access the entire state of the duration.

        Returns
        - a list containing the seconds and nanos units, not null
        """
        ...


    def isZero(self) -> bool:
        """
        Checks if this duration is zero length.
        
        A `Duration` represents a directed distance between two points on
        the time-line and can therefore be positive, zero or negative.
        This method checks whether the length is zero.

        Returns
        - True if this duration has a total length equal to zero
        """
        ...


    def isNegative(self) -> bool:
        """
        Checks if this duration is negative, excluding zero.
        
        A `Duration` represents a directed distance between two points on
        the time-line and can therefore be positive, zero or negative.
        This method checks whether the length is less than zero.

        Returns
        - True if this duration has a total length less than zero
        """
        ...


    def getSeconds(self) -> int:
        """
        Gets the number of seconds in this duration.
        
        The length of the duration is stored using two fields - seconds and nanoseconds.
        The nanoseconds part is a value from 0 to 999,999,999 that is an adjustment to
        the length in seconds.
        The total duration is defined by calling this method and .getNano().
        
        A `Duration` represents a directed distance between two points on the time-line.
        A negative duration is expressed by the negative sign of the seconds part.
        A duration of -1 nanosecond is stored as -1 seconds plus 999,999,999 nanoseconds.

        Returns
        - the whole seconds part of the length of the duration, positive or negative
        """
        ...


    def getNano(self) -> int:
        """
        Gets the number of nanoseconds within the second in this duration.
        
        The length of the duration is stored using two fields - seconds and nanoseconds.
        The nanoseconds part is a value from 0 to 999,999,999 that is an adjustment to
        the length in seconds.
        The total duration is defined by calling this method and .getSeconds().
        
        A `Duration` represents a directed distance between two points on the time-line.
        A negative duration is expressed by the negative sign of the seconds part.
        A duration of -1 nanosecond is stored as -1 seconds plus 999,999,999 nanoseconds.

        Returns
        - the nanoseconds within the second part of the length of the duration, from 0 to 999,999,999
        """
        ...


    def withSeconds(self, seconds: int) -> "Duration":
        """
        Returns a copy of this duration with the specified amount of seconds.
        
        This returns a duration with the specified seconds, retaining the
        nano-of-second part of this duration.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - seconds: the seconds to represent, may be negative

        Returns
        - a `Duration` based on this period with the requested seconds, not null
        """
        ...


    def withNanos(self, nanoOfSecond: int) -> "Duration":
        """
        Returns a copy of this duration with the specified nano-of-second.
        
        This returns a duration with the specified nano-of-second, retaining the
        seconds part of this duration.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - nanoOfSecond: the nano-of-second to represent, from 0 to 999,999,999

        Returns
        - a `Duration` based on this period with the requested nano-of-second, not null

        Raises
        - DateTimeException: if the nano-of-second is invalid
        """
        ...


    def plus(self, duration: "Duration") -> "Duration":
        """
        Returns a copy of this duration with the specified duration added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - duration: the duration to add, positive or negative, not null

        Returns
        - a `Duration` based on this duration with the specified duration added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plus(self, amountToAdd: int, unit: "TemporalUnit") -> "Duration":
        """
        Returns a copy of this duration with the specified duration added.
        
        The duration amount is measured in terms of the specified unit.
        Only a subset of units are accepted by this method.
        The unit must either have an TemporalUnit.isDurationEstimated() exact duration or
        be ChronoUnit.DAYS which is treated as 24 hours. Other units throw an exception.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - amountToAdd: the amount to add, measured in terms of the unit, positive or negative
        - unit: the unit that the amount is measured in, must have an exact duration, not null

        Returns
        - a `Duration` based on this duration with the specified duration added, not null

        Raises
        - UnsupportedTemporalTypeException: if the unit is not supported
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusDays(self, daysToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in standard 24 hour days added.
        
        The number of days is multiplied by 86400 to obtain the number of seconds to add.
        This is based on the standard definition of a day as 24 hours.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - daysToAdd: the days to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified days added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusHours(self, hoursToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in hours added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - hoursToAdd: the hours to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified hours added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusMinutes(self, minutesToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in minutes added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - minutesToAdd: the minutes to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified minutes added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusSeconds(self, secondsToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in seconds added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - secondsToAdd: the seconds to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified seconds added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusMillis(self, millisToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in milliseconds added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - millisToAdd: the milliseconds to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified milliseconds added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def plusNanos(self, nanosToAdd: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in nanoseconds added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - nanosToAdd: the nanoseconds to add, positive or negative

        Returns
        - a `Duration` based on this duration with the specified nanoseconds added, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minus(self, duration: "Duration") -> "Duration":
        """
        Returns a copy of this duration with the specified duration subtracted.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - duration: the duration to subtract, positive or negative, not null

        Returns
        - a `Duration` based on this duration with the specified duration subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minus(self, amountToSubtract: int, unit: "TemporalUnit") -> "Duration":
        """
        Returns a copy of this duration with the specified duration subtracted.
        
        The duration amount is measured in terms of the specified unit.
        Only a subset of units are accepted by this method.
        The unit must either have an TemporalUnit.isDurationEstimated() exact duration or
        be ChronoUnit.DAYS which is treated as 24 hours. Other units throw an exception.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - amountToSubtract: the amount to subtract, measured in terms of the unit, positive or negative
        - unit: the unit that the amount is measured in, must have an exact duration, not null

        Returns
        - a `Duration` based on this duration with the specified duration subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusDays(self, daysToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in standard 24 hour days subtracted.
        
        The number of days is multiplied by 86400 to obtain the number of seconds to subtract.
        This is based on the standard definition of a day as 24 hours.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - daysToSubtract: the days to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified days subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusHours(self, hoursToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in hours subtracted.
        
        The number of hours is multiplied by 3600 to obtain the number of seconds to subtract.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - hoursToSubtract: the hours to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified hours subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusMinutes(self, minutesToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in minutes subtracted.
        
        The number of hours is multiplied by 60 to obtain the number of seconds to subtract.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - minutesToSubtract: the minutes to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified minutes subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusSeconds(self, secondsToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in seconds subtracted.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - secondsToSubtract: the seconds to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified seconds subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusMillis(self, millisToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in milliseconds subtracted.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - millisToSubtract: the milliseconds to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified milliseconds subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def minusNanos(self, nanosToSubtract: int) -> "Duration":
        """
        Returns a copy of this duration with the specified duration in nanoseconds subtracted.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - nanosToSubtract: the nanoseconds to subtract, positive or negative

        Returns
        - a `Duration` based on this duration with the specified nanoseconds subtracted, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def multipliedBy(self, multiplicand: int) -> "Duration":
        """
        Returns a copy of this duration multiplied by the scalar.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - multiplicand: the value to multiply the duration by, positive or negative

        Returns
        - a `Duration` based on this duration multiplied by the specified scalar, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def dividedBy(self, divisor: int) -> "Duration":
        """
        Returns a copy of this duration divided by the specified value.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - divisor: the value to divide the duration by, positive or negative, not zero

        Returns
        - a `Duration` based on this duration divided by the specified divisor, not null

        Raises
        - ArithmeticException: if the divisor is zero or if numeric overflow occurs
        """
        ...


    def dividedBy(self, divisor: "Duration") -> int:
        """
        Returns number of whole times a specified Duration occurs within this Duration.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - divisor: the value to divide the duration by, positive or negative, not null

        Returns
        - number of whole times, rounded toward zero, a specified
                `Duration` occurs within this Duration, may be negative

        Raises
        - ArithmeticException: if the divisor is zero, or if numeric overflow occurs

        Since
        - 9
        """
        ...


    def negated(self) -> "Duration":
        """
        Returns a copy of this duration with the length negated.
        
        This method swaps the sign of the total length of this duration.
        For example, `PT1.3S` will be returned as `PT-1.3S`.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - a `Duration` based on this duration with the amount negated, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def abs(self) -> "Duration":
        """
        Returns a copy of this duration with a positive length.
        
        This method returns a positive duration by effectively removing the sign from any negative total length.
        For example, `PT-1.3S` will be returned as `PT1.3S`.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - a `Duration` based on this duration with an absolute length, not null

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def addTo(self, temporal: "Temporal") -> "Temporal":
        """
        Adds this duration to the specified temporal object.
        
        This returns a temporal object of the same observable type as the input
        with this duration added.
        
        In most cases, it is clearer to reverse the calling pattern by using
        Temporal.plus(TemporalAmount).
        ```
          // these two lines are equivalent, but the second approach is recommended
          dateTime = thisDuration.addTo(dateTime);
          dateTime = dateTime.plus(thisDuration);
        ```
        
        The calculation will add the seconds, then nanos.
        Only non-zero amounts will be added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - temporal: the temporal object to adjust, not null

        Returns
        - an object of the same type with the adjustment made, not null

        Raises
        - DateTimeException: if unable to add
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def subtractFrom(self, temporal: "Temporal") -> "Temporal":
        """
        Subtracts this duration from the specified temporal object.
        
        This returns a temporal object of the same observable type as the input
        with this duration subtracted.
        
        In most cases, it is clearer to reverse the calling pattern by using
        Temporal.minus(TemporalAmount).
        ```
          // these two lines are equivalent, but the second approach is recommended
          dateTime = thisDuration.subtractFrom(dateTime);
          dateTime = dateTime.minus(thisDuration);
        ```
        
        The calculation will subtract the seconds, then nanos.
        Only non-zero amounts will be added.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - temporal: the temporal object to adjust, not null

        Returns
        - an object of the same type with the adjustment made, not null

        Raises
        - DateTimeException: if unable to subtract
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def toDays(self) -> int:
        """
        Gets the number of days in this duration.
        
        This returns the total number of days in the duration by dividing the
        number of seconds by 86400.
        This is based on the standard definition of a day as 24 hours.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of days in the duration, may be negative
        """
        ...


    def toHours(self) -> int:
        """
        Gets the number of hours in this duration.
        
        This returns the total number of hours in the duration by dividing the
        number of seconds by 3600.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of hours in the duration, may be negative
        """
        ...


    def toMinutes(self) -> int:
        """
        Gets the number of minutes in this duration.
        
        This returns the total number of minutes in the duration by dividing the
        number of seconds by 60.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of minutes in the duration, may be negative
        """
        ...


    def toSeconds(self) -> int:
        """
        Gets the number of seconds in this duration.
        
        This returns the total number of whole seconds in the duration.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the whole seconds part of the length of the duration, positive or negative

        Since
        - 9
        """
        ...


    def toMillis(self) -> int:
        """
        Converts this duration to the total length in milliseconds.
        
        If this duration is too large to fit in a `long` milliseconds, then an
        exception is thrown.
        
        If this duration has greater than millisecond precision, then the conversion
        will drop any excess precision information as though the amount in nanoseconds
        was subject to integer division by one million.

        Returns
        - the total length of the duration in milliseconds

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def toNanos(self) -> int:
        """
        Converts this duration to the total length in nanoseconds expressed as a `long`.
        
        If this duration is too large to fit in a `long` nanoseconds, then an
        exception is thrown.

        Returns
        - the total length of the duration in nanoseconds

        Raises
        - ArithmeticException: if numeric overflow occurs
        """
        ...


    def toDaysPart(self) -> int:
        """
        Extracts the number of days in the duration.
        
        This returns the total number of days in the duration by dividing the
        number of seconds by 86400.
        This is based on the standard definition of a day as 24 hours.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of days in the duration, may be negative

        Since
        - 9
        """
        ...


    def toHoursPart(self) -> int:
        """
        Extracts the number of hours part in the duration.
        
        This returns the number of remaining hours when dividing .toHours
        by hours in a day.
        This is based on the standard definition of a day as 24 hours.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of hours part in the duration, may be negative

        Since
        - 9
        """
        ...


    def toMinutesPart(self) -> int:
        """
        Extracts the number of minutes part in the duration.
        
        This returns the number of remaining minutes when dividing .toMinutes
        by minutes in an hour.
        This is based on the standard definition of an hour as 60 minutes.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of minutes parts in the duration, may be negative

        Since
        - 9
        """
        ...


    def toSecondsPart(self) -> int:
        """
        Extracts the number of seconds part in the duration.
        
        This returns the remaining seconds when dividing .toSeconds
        by seconds in a minute.
        This is based on the standard definition of a minute as 60 seconds.
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of seconds parts in the duration, may be negative

        Since
        - 9
        """
        ...


    def toMillisPart(self) -> int:
        """
        Extracts the number of milliseconds part of the duration.
        
        This returns the milliseconds part by dividing the number of nanoseconds by 1,000,000.
        The length of the duration is stored using two fields - seconds and nanoseconds.
        The nanoseconds part is a value from 0 to 999,999,999 that is an adjustment to
        the length in seconds.
        The total duration is defined by calling .getNano() and .getSeconds().
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the number of milliseconds part of the duration.

        Since
        - 9
        """
        ...


    def toNanosPart(self) -> int:
        """
        Get the nanoseconds part within seconds of the duration.
        
        The length of the duration is stored using two fields - seconds and nanoseconds.
        The nanoseconds part is a value from 0 to 999,999,999 that is an adjustment to
        the length in seconds.
        The total duration is defined by calling .getNano() and .getSeconds().
        
        This instance is immutable and unaffected by this method call.

        Returns
        - the nanoseconds within the second part of the length of the duration, from 0 to 999,999,999

        Since
        - 9
        """
        ...


    def truncatedTo(self, unit: "TemporalUnit") -> "Duration":
        """
        Returns a copy of this `Duration` truncated to the specified unit.
        
        Truncating the duration returns a copy of the original with conceptual fields
        smaller than the specified unit set to zero.
        For example, truncating with the ChronoUnit.MINUTES MINUTES unit will
        round down towards zero to the nearest minute, setting the seconds and
        nanoseconds to zero.
        
        The unit must have a TemporalUnit.getDuration() duration
        that divides into the length of a standard day without remainder.
        This includes all
        ChronoUnit.isTimeBased() time-based units on {@code ChronoUnit}
        and ChronoUnit.DAYS DAYS. Other ChronoUnits throw an exception.
        
        This instance is immutable and unaffected by this method call.

        Arguments
        - unit: the unit to truncate to, not null

        Returns
        - a `Duration` based on this duration with the time truncated, not null

        Raises
        - DateTimeException: if the unit is invalid for truncation
        - UnsupportedTemporalTypeException: if the unit is not supported

        Since
        - 9
        """
        ...


    def compareTo(self, otherDuration: "Duration") -> int:
        """
        Compares this duration to the specified `Duration`.
        
        The comparison is based on the total length of the durations.
        It is "consistent with equals", as defined by Comparable.

        Arguments
        - otherDuration: the other duration to compare to, not null

        Returns
        - the comparator value, negative if less, positive if greater
        """
        ...


    def equals(self, other: "Object") -> bool:
        """
        Checks if this duration is equal to the specified `Duration`.
        
        The comparison is based on the total length of the durations.

        Arguments
        - other: the other duration, null returns False

        Returns
        - True if the other duration is equal to this one
        """
        ...


    def hashCode(self) -> int:
        """
        A hash code for this duration.

        Returns
        - a suitable hash code
        """
        ...


    def toString(self) -> str:
        """
        A string representation of this duration using ISO-8601 seconds
        based representation, such as `PT8H6M12.345S`.
        
        The format of the returned string will be `PTnHnMnS`, where n is
        the relevant hours, minutes or seconds part of the duration.
        Any fractional seconds are placed after a decimal point in the seconds section.
        If a section has a zero value, it is omitted.
        The hours, minutes and seconds will all have the same sign.
        
        Examples:
        ```
           "20.345 seconds"                 -- "PT20.345S
           "15 minutes" (15 * 60 seconds)   -- "PT15M"
           "10 hours" (10 * 3600 seconds)   -- "PT10H"
           "2 days" (2 * 86400 seconds)     -- "PT48H"
        ```
        Note that multiples of 24 hours are not output as days to avoid confusion
        with `Period`.

        Returns
        - an ISO-8601 representation of this duration, not null
        """
        ...
