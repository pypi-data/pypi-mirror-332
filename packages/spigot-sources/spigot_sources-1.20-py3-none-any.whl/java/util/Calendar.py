"""
Python module generated from Java source file java.util.Calendar

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import OptionalDataException
from java.io import Serializable
from java.security import AccessControlContext
from java.security import AccessController
from java.security import PermissionCollection
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.security import ProtectionDomain
from java.text import DateFormat
from java.text import DateFormatSymbols
from java.time import Instant
from java.util import *
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from sun.util import BuddhistCalendar
from sun.util.calendar import ZoneInfo
from sun.util.locale.provider import CalendarDataUtility
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import TimeZoneNameUtility
from sun.util.spi import CalendarProvider
from typing import Any, Callable, Iterable, Tuple


class Calendar(Serializable, Cloneable, Comparable):
    """
    The `Calendar` class is an abstract class that provides methods
    for converting between a specific instant in time and a set of .fields calendar fields such as `YEAR`, `MONTH`,
    `DAY_OF_MONTH`, `HOUR`, and so on, and for
    manipulating the calendar fields, such as getting the date of the next
    week. An instant in time can be represented by a millisecond value that is
    an offset from the <a id="Epoch">*Epoch*</a>, January 1, 1970
    00:00:00.000 GMT (Gregorian).
    
    The class also provides additional fields and methods for
    implementing a concrete calendar system outside the package. Those
    fields and methods are defined as `protected`.
    
    
    Like other locale-sensitive classes, `Calendar` provides a
    class method, `getInstance`, for getting a generally useful
    object of this type. `Calendar`'s `getInstance` method
    returns a `Calendar` object whose
    calendar fields have been initialized with the current date and time:
    <blockquote>
    ```
        Calendar rightNow = Calendar.getInstance();
    ```
    </blockquote>
    
    A `Calendar` object can produce all the calendar field values
    needed to implement the date-time formatting for a particular language and
    calendar style (for example, Japanese-Gregorian, Japanese-Traditional).
    `Calendar` defines the range of values returned by
    certain calendar fields, as well as their meaning.  For example,
    the first month of the calendar system has value `MONTH ==
    JANUARY` for all calendars.  Other values are defined by the
    concrete subclass, such as `ERA`.  See individual field
    documentation and subclass documentation for details.
    
    <h2>Getting and Setting Calendar Field Values</h2>
    
    The calendar field values can be set by calling the `set`
    methods. Any field values set in a `Calendar` will not be
    interpreted until it needs to calculate its time value (milliseconds from
    the Epoch) or values of the calendar fields. Calling the
    `get`, `getTimeInMillis`, `getTime`,
    `add` and `roll` involves such calculation.
    
    <h3>Leniency</h3>
    
    `Calendar` has two modes for interpreting the calendar
    fields, *lenient* and *non-lenient*.  When a
    `Calendar` is in lenient mode, it accepts a wider range of
    calendar field values than it produces.  When a `Calendar`
    recomputes calendar field values for return by `get()`, all of
    the calendar fields are normalized. For example, a lenient
    `GregorianCalendar` interprets `MONTH == JANUARY`,
    `DAY_OF_MONTH == 32` as February 1.
    
    When a `Calendar` is in non-lenient mode, it throws an
    exception if there is any inconsistency in its calendar fields. For
    example, a `GregorianCalendar` always produces
    `DAY_OF_MONTH` values between 1 and the length of the month. A
    non-lenient `GregorianCalendar` throws an exception upon
    calculating its time or calendar field values if any out-of-range field
    value has been set.
    
    <h3><a id="first_week">First Week</a></h3>
    
    `Calendar` defines a locale-specific seven day week using two
    parameters: the first day of the week and the minimal days in first week
    (from 1 to 7).  These numbers are taken from the locale resource data or the
    locale itself when a `Calendar` is constructed. If the designated
    locale contains "fw" and/or "rg" <a href="./Locale.html#def_locale_extension">
    Unicode extensions</a>, the first day of the week will be obtained according to
    those extensions. If both "fw" and "rg" are specified, the value from the "fw"
    extension supersedes the implicit one from the "rg" extension.
    They may also be specified explicitly through the methods for setting their
    values.
    
    When setting or getting the `WEEK_OF_MONTH` or
    `WEEK_OF_YEAR` fields, `Calendar` must determine the
    first week of the month or year as a reference point.  The first week of a
    month or year is defined as the earliest seven day period beginning on
    `getFirstDayOfWeek()` and containing at least
    `getMinimalDaysInFirstWeek()` days of that month or year.  Weeks
    numbered ..., -1, 0 precede the first week; weeks numbered 2, 3,... follow
    it.  Note that the normalized numbering returned by `get()` may be
    different.  For example, a specific `Calendar` subclass may
    designate the week before week 1 of a year as week `*n*` of
    the previous year.
    
    <h3>Calendar Fields Resolution</h3>
    
    When computing a date and time from the calendar fields, there
    may be insufficient information for the computation (such as only
    year and month with no day of month), or there may be inconsistent
    information (such as Tuesday, July 15, 1996 (Gregorian) -- July 15,
    1996 is actually a Monday). `Calendar` will resolve
    calendar field values to determine the date and time in the
    following way.
    
    <a id="resolution">If there is any conflict in calendar field values,
    `Calendar` gives priorities to calendar fields that have been set
    more recently.</a> The following are the default combinations of the
    calendar fields. The most recent combination, as determined by the
    most recently set single field, will be used.
    
    <a id="date_resolution">For the date fields</a>:
    <blockquote>
    ```
    YEAR + MONTH + DAY_OF_MONTH
    YEAR + MONTH + WEEK_OF_MONTH + DAY_OF_WEEK
    YEAR + MONTH + DAY_OF_WEEK_IN_MONTH + DAY_OF_WEEK
    YEAR + DAY_OF_YEAR
    YEAR + DAY_OF_WEEK + WEEK_OF_YEAR
    ```</blockquote>
    
    <a id="time_resolution">For the time of day fields</a>:
    <blockquote>
    ```
    HOUR_OF_DAY
    AM_PM + HOUR
    ```</blockquote>
    
    If there are any calendar fields whose values haven't been set in the selected
    field combination, `Calendar` uses their default values. The default
    value of each field may vary by concrete calendar systems. For example, in
    `GregorianCalendar`, the default of a field is the same as that
    of the start of the Epoch: i.e., `YEAR = 1970`, `MONTH =
    JANUARY`, `DAY_OF_MONTH = 1`, etc.
    
    
    <strong>Note:</strong> There are certain possible ambiguities in
    interpretation of certain singular times, which are resolved in the
    following ways:
    <ol>
        -  23:59 is the last minute of the day and 00:00 is the first
             minute of the next day. Thus, 23:59 on Dec 31, 1999 &lt; 00:00 on
             Jan 1, 2000 &lt; 00:01 on Jan 1, 2000.
    
        -  Although historically not precise, midnight also belongs to "am",
             and noon belongs to "pm", so on the same day,
             12:00 am (midnight) &lt; 12:01 am, and 12:00 pm (noon) &lt; 12:01 pm
    </ol>
    
    
    The date or time format strings are not part of the definition of a
    calendar, as those must be modifiable or overridable by the user at
    runtime. Use DateFormat
    to format dates.
    
    <h3>Field Manipulation</h3>
    
    The calendar fields can be changed using three methods:
    `set()`, `add()`, and `roll()`.
    
    <strong>`set(f, value)`</strong> changes calendar field
    `f` to `value`.  In addition, it sets an
    internal member variable to indicate that calendar field `f` has
    been changed. Although calendar field `f` is changed immediately,
    the calendar's time value in milliseconds is not recomputed until the next call to
    `get()`, `getTime()`, `getTimeInMillis()`,
    `add()`, or `roll()` is made. Thus, multiple calls to
    `set()` do not trigger multiple, unnecessary
    computations. As a result of changing a calendar field using
    `set()`, other calendar fields may also change, depending on the
    calendar field, the calendar field value, and the calendar system. In addition,
    `get(f)` will not necessarily return `value` set by
    the call to the `set` method
    after the calendar fields have been recomputed. The specifics are determined by
    the concrete calendar class.
    
    *Example*: Consider a `GregorianCalendar`
    originally set to August 31, 1999. Calling `set(Calendar.MONTH,
    Calendar.SEPTEMBER)` sets the date to September 31,
    1999. This is a temporary internal representation that resolves to
    October 1, 1999 if `getTime()` is then called. However, a
    call to `set(Calendar.DAY_OF_MONTH, 30)` before the call to
    `getTime()` sets the date to September 30, 1999, since
    no recomputation occurs after `set()` itself.
    
    <strong>`add(f, delta)`</strong> adds `delta`
    to field `f`.  This is equivalent to calling `set(f,
    get(f) + delta)` with two adjustments:
    
    <blockquote>
      <strong>Add rule 1</strong>. The value of field `f`
      after the call minus the value of field `f` before the
      call is `delta`, modulo any overflow that has occurred in
      field `f`. Overflow occurs when a field value exceeds its
      range and, as a result, the next larger field is incremented or
      decremented and the field value is adjusted back into its range.
    
      <strong>Add rule 2</strong>. If a smaller field is expected to be
      invariant, but it is impossible for it to be equal to its
      prior value because of changes in its minimum or maximum after field
      `f` is changed or other constraints, such as time zone
      offset changes, then its value is adjusted to be as close
      as possible to its expected value. A smaller field represents a
      smaller unit of time. `HOUR` is a smaller field than
      `DAY_OF_MONTH`. No adjustment is made to smaller fields
      that are not expected to be invariant. The calendar system
      determines what fields are expected to be invariant.
    </blockquote>
    
    In addition, unlike `set()`, `add()` forces
    an immediate recomputation of the calendar's milliseconds and all
    fields.
    
    *Example*: Consider a `GregorianCalendar`
    originally set to August 31, 1999. Calling `add(Calendar.MONTH,
    13)` sets the calendar to September 30, 2000. <strong>Add rule
    1</strong> sets the `MONTH` field to September, since
    adding 13 months to August gives September of the next year. Since
    `DAY_OF_MONTH` cannot be 31 in September in a
    `GregorianCalendar`, <strong>add rule 2</strong> sets the
    `DAY_OF_MONTH` to 30, the closest possible value. Although
    it is a smaller field, `DAY_OF_WEEK` is not adjusted by
    rule 2, since it is expected to change when the month changes in a
    `GregorianCalendar`.
    
    <strong>`roll(f, delta)`</strong> adds
    `delta` to field `f` without changing larger
    fields. This is equivalent to calling `add(f, delta)` with
    the following adjustment:
    
    <blockquote>
      <strong>Roll rule</strong>. Larger fields are unchanged after the
      call. A larger field represents a larger unit of
      time. `DAY_OF_MONTH` is a larger field than
      `HOUR`.
    </blockquote>
    
    *Example*: See java.util.GregorianCalendar.roll(int, int).
    
    <strong>Usage model</strong>. To motivate the behavior of
    `add()` and `roll()`, consider a user interface
    component with increment and decrement buttons for the month, day, and
    year, and an underlying `GregorianCalendar`. If the
    interface reads January 31, 1999 and the user presses the month
    increment button, what should it read? If the underlying
    implementation uses `set()`, it might read March 3, 1999. A
    better result would be February 28, 1999. Furthermore, if the user
    presses the month increment button again, it should read March 31,
    1999, not March 28, 1999. By saving the original date and using either
    `add()` or `roll()`, depending on whether larger
    fields should be affected, the user interface can behave as most users
    will intuitively expect.

    Author(s)
    - Mark Davis, David Goldsmith, Chen-Lieh Huang, Alan Liu

    See
    - java.text.DateFormat

    Since
    - 1.1
    """

    ERA = 0
    """
    Field number for `get` and `set` indicating the
    era, e.g., AD or BC in the Julian calendar. This is a calendar-specific
    value; see subclass documentation.

    See
    - GregorianCalendar.BC
    """
    YEAR = 1
    """
    Field number for `get` and `set` indicating the
    year. This is a calendar-specific value; see subclass documentation.
    """
    MONTH = 2
    """
    Field number for `get` and `set` indicating the
    month. This is a calendar-specific value. The first month of
    the year in the Gregorian and Julian calendars is
    `JANUARY` which is 0; the last depends on the number
    of months in a year.

    See
    - .UNDECIMBER
    """
    WEEK_OF_YEAR = 3
    """
    Field number for `get` and `set` indicating the
    week number within the current year.  The first week of the year, as
    defined by `getFirstDayOfWeek()` and
    `getMinimalDaysInFirstWeek()`, has value 1.  Subclasses define
    the value of `WEEK_OF_YEAR` for days before the first week of
    the year.

    See
    - .getMinimalDaysInFirstWeek
    """
    WEEK_OF_MONTH = 4
    """
    Field number for `get` and `set` indicating the
    week number within the current month.  The first week of the month, as
    defined by `getFirstDayOfWeek()` and
    `getMinimalDaysInFirstWeek()`, has value 1.  Subclasses define
    the value of `WEEK_OF_MONTH` for days before the first week of
    the month.

    See
    - .getMinimalDaysInFirstWeek
    """
    DATE = 5
    """
    Field number for `get` and `set` indicating the
    day of the month. This is a synonym for `DAY_OF_MONTH`.
    The first day of the month has value 1.

    See
    - .DAY_OF_MONTH
    """
    DAY_OF_MONTH = 5
    """
    Field number for `get` and `set` indicating the
    day of the month. This is a synonym for `DATE`.
    The first day of the month has value 1.

    See
    - .DATE
    """
    DAY_OF_YEAR = 6
    """
    Field number for `get` and `set` indicating the day
    number within the current year.  The first day of the year has value 1.
    """
    DAY_OF_WEEK = 7
    """
    Field number for `get` and `set` indicating the day
    of the week.  This field takes values `SUNDAY`,
    `MONDAY`, `TUESDAY`, `WEDNESDAY`,
    `THURSDAY`, `FRIDAY`, and `SATURDAY`.

    See
    - .SATURDAY
    """
    DAY_OF_WEEK_IN_MONTH = 8
    """
    Field number for `get` and `set` indicating the
    ordinal number of the day of the week within the current month. Together
    with the `DAY_OF_WEEK` field, this uniquely specifies a day
    within a month.  Unlike `WEEK_OF_MONTH` and
    `WEEK_OF_YEAR`, this field's value does *not* depend on
    `getFirstDayOfWeek()` or
    `getMinimalDaysInFirstWeek()`.  `DAY_OF_MONTH 1`
    through `7` always correspond to `DAY_OF_WEEK_IN_MONTH
    1`; `8` through `14` correspond to
    `DAY_OF_WEEK_IN_MONTH 2`, and so on.
    `DAY_OF_WEEK_IN_MONTH 0` indicates the week before
    `DAY_OF_WEEK_IN_MONTH 1`.  Negative values count back from the
    end of the month, so the last Sunday of a month is specified as
    `DAY_OF_WEEK = SUNDAY, DAY_OF_WEEK_IN_MONTH = -1`.  Because
    negative values count backward they will usually be aligned differently
    within the month than positive values.  For example, if a month has 31
    days, `DAY_OF_WEEK_IN_MONTH -1` will overlap
    `DAY_OF_WEEK_IN_MONTH 5` and the end of `4`.

    See
    - .WEEK_OF_MONTH
    """
    AM_PM = 9
    """
    Field number for `get` and `set` indicating
    whether the `HOUR` is before or after noon.
    E.g., at 10:04:15.250 PM the `AM_PM` is `PM`.

    See
    - .HOUR
    """
    HOUR = 10
    """
    Field number for `get` and `set` indicating the
    hour of the morning or afternoon. `HOUR` is used for the
    12-hour clock (0 - 11). Noon and midnight are represented by 0, not by 12.
    E.g., at 10:04:15.250 PM the `HOUR` is 10.

    See
    - .HOUR_OF_DAY
    """
    HOUR_OF_DAY = 11
    """
    Field number for `get` and `set` indicating the
    hour of the day. `HOUR_OF_DAY` is used for the 24-hour clock.
    E.g., at 10:04:15.250 PM the `HOUR_OF_DAY` is 22.

    See
    - .HOUR
    """
    MINUTE = 12
    """
    Field number for `get` and `set` indicating the
    minute within the hour.
    E.g., at 10:04:15.250 PM the `MINUTE` is 4.
    """
    SECOND = 13
    """
    Field number for `get` and `set` indicating the
    second within the minute.
    E.g., at 10:04:15.250 PM the `SECOND` is 15.
    """
    MILLISECOND = 14
    """
    Field number for `get` and `set` indicating the
    millisecond within the second.
    E.g., at 10:04:15.250 PM the `MILLISECOND` is 250.
    """
    ZONE_OFFSET = 15
    """
    Field number for `get` and `set`
    indicating the raw offset from GMT in milliseconds.
    
    This field reflects the correct GMT offset value of the time
    zone of this `Calendar` if the
    `TimeZone` implementation subclass supports
    historical GMT offset changes.
    """
    DST_OFFSET = 16
    """
    Field number for `get` and `set` indicating the
    daylight saving offset in milliseconds.
    
    This field reflects the correct daylight saving offset value of
    the time zone of this `Calendar` if the
    `TimeZone` implementation subclass supports
    historical Daylight Saving Time schedule changes.
    """
    FIELD_COUNT = 17
    """
    The number of distinct fields recognized by `get` and `set`.
    Field numbers range from `0..FIELD_COUNT-1`.
    """
    SUNDAY = 1
    """
    Value of the .DAY_OF_WEEK field indicating
    Sunday.
    """
    MONDAY = 2
    """
    Value of the .DAY_OF_WEEK field indicating
    Monday.
    """
    TUESDAY = 3
    """
    Value of the .DAY_OF_WEEK field indicating
    Tuesday.
    """
    WEDNESDAY = 4
    """
    Value of the .DAY_OF_WEEK field indicating
    Wednesday.
    """
    THURSDAY = 5
    """
    Value of the .DAY_OF_WEEK field indicating
    Thursday.
    """
    FRIDAY = 6
    """
    Value of the .DAY_OF_WEEK field indicating
    Friday.
    """
    SATURDAY = 7
    """
    Value of the .DAY_OF_WEEK field indicating
    Saturday.
    """
    JANUARY = 0
    """
    Value of the .MONTH field indicating the
    first month of the year in the Gregorian and Julian calendars.
    """
    FEBRUARY = 1
    """
    Value of the .MONTH field indicating the
    second month of the year in the Gregorian and Julian calendars.
    """
    MARCH = 2
    """
    Value of the .MONTH field indicating the
    third month of the year in the Gregorian and Julian calendars.
    """
    APRIL = 3
    """
    Value of the .MONTH field indicating the
    fourth month of the year in the Gregorian and Julian calendars.
    """
    MAY = 4
    """
    Value of the .MONTH field indicating the
    fifth month of the year in the Gregorian and Julian calendars.
    """
    JUNE = 5
    """
    Value of the .MONTH field indicating the
    sixth month of the year in the Gregorian and Julian calendars.
    """
    JULY = 6
    """
    Value of the .MONTH field indicating the
    seventh month of the year in the Gregorian and Julian calendars.
    """
    AUGUST = 7
    """
    Value of the .MONTH field indicating the
    eighth month of the year in the Gregorian and Julian calendars.
    """
    SEPTEMBER = 8
    """
    Value of the .MONTH field indicating the
    ninth month of the year in the Gregorian and Julian calendars.
    """
    OCTOBER = 9
    """
    Value of the .MONTH field indicating the
    tenth month of the year in the Gregorian and Julian calendars.
    """
    NOVEMBER = 10
    """
    Value of the .MONTH field indicating the
    eleventh month of the year in the Gregorian and Julian calendars.
    """
    DECEMBER = 11
    """
    Value of the .MONTH field indicating the
    twelfth month of the year in the Gregorian and Julian calendars.
    """
    UNDECIMBER = 12
    """
    Value of the .MONTH field indicating the
    thirteenth month of the year. Although `GregorianCalendar`
    does not use this value, lunar calendars do.
    """
    AM = 0
    """
    Value of the .AM_PM field indicating the
    period of the day from midnight to just before noon.
    """
    PM = 1
    """
    Value of the .AM_PM field indicating the
    period of the day from noon to just before midnight.
    """
    ALL_STYLES = 0
    """
    A style specifier for .getDisplayNames(int, int, Locale)
    getDisplayNames indicating names in all styles, such as
    "January" and "Jan".

    See
    - .LONG

    Since
    - 1.6
    """
    SHORT = 1
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames equivalent to .SHORT_FORMAT.

    See
    - .LONG

    Since
    - 1.6
    """
    LONG = 2
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames equivalent to .LONG_FORMAT.

    See
    - .SHORT

    Since
    - 1.6
    """
    NARROW_FORMAT = 4
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a narrow name used for format. Narrow names
    are typically single character strings, such as "M" for Monday.

    See
    - .LONG_FORMAT

    Since
    - 1.8
    """
    NARROW_STANDALONE = NARROW_FORMAT | STANDALONE_MASK
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a narrow name independently. Narrow names
    are typically single character strings, such as "M" for Monday.

    See
    - .LONG_STANDALONE

    Since
    - 1.8
    """
    SHORT_FORMAT = 1
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a short name used for format.

    See
    - .LONG_STANDALONE

    Since
    - 1.8
    """
    LONG_FORMAT = 2
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a long name used for format.

    See
    - .SHORT_STANDALONE

    Since
    - 1.8
    """
    SHORT_STANDALONE = SHORT | STANDALONE_MASK
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a short name used independently,
    such as a month abbreviation as calendar headers.

    See
    - .LONG_STANDALONE

    Since
    - 1.8
    """
    LONG_STANDALONE = LONG | STANDALONE_MASK
    """
    A style specifier for .getDisplayName(int, int, Locale)
    getDisplayName and .getDisplayNames(int, int, Locale)
    getDisplayNames indicating a long name used independently,
    such as a month name as calendar headers.

    See
    - .SHORT_STANDALONE

    Since
    - 1.8
    """


    @staticmethod
    def getInstance() -> "Calendar":
        """
        Gets a calendar using the default time zone and locale. The
        `Calendar` returned is based on the current time
        in the default time zone with the default
        Locale.Category.FORMAT FORMAT locale.
        
        If the locale contains the time zone with "tz"
        <a href="Locale.html#def_locale_extension">Unicode extension</a>,
        that time zone is used instead.

        Returns
        - a Calendar.
        """
        ...


    @staticmethod
    def getInstance(zone: "TimeZone") -> "Calendar":
        """
        Gets a calendar using the specified time zone and default locale.
        The `Calendar` returned is based on the current time
        in the given time zone with the default
        Locale.Category.FORMAT FORMAT locale.

        Arguments
        - zone: the time zone to use

        Returns
        - a Calendar.
        """
        ...


    @staticmethod
    def getInstance(aLocale: "Locale") -> "Calendar":
        """
        Gets a calendar using the default time zone and specified locale.
        The `Calendar` returned is based on the current time
        in the default time zone with the given locale.
        
        If the locale contains the time zone with "tz"
        <a href="Locale.html#def_locale_extension">Unicode extension</a>,
        that time zone is used instead.

        Arguments
        - aLocale: the locale for the week data

        Returns
        - a Calendar.
        """
        ...


    @staticmethod
    def getInstance(zone: "TimeZone", aLocale: "Locale") -> "Calendar":
        """
        Gets a calendar with the specified time zone and locale.
        The `Calendar` returned is based on the current time
        in the given time zone with the given locale.

        Arguments
        - zone: the time zone to use
        - aLocale: the locale for the week data

        Returns
        - a Calendar.
        """
        ...


    @staticmethod
    def getAvailableLocales() -> list["Locale"]:
        """
        Returns an array of all locales for which the `getInstance`
        methods of this class can return localized instances.
        The array returned must contain at least a `Locale`
        instance equal to java.util.Locale.US Locale.US.

        Returns
        - An array of locales for which localized
                `Calendar` instances are available.
        """
        ...


    def getTime(self) -> "Date":
        """
        Returns a `Date` object representing this
        `Calendar`'s time value (millisecond offset from the <a
        href="#Epoch">Epoch</a>").

        Returns
        - a `Date` representing the time value.

        See
        - .getTimeInMillis()
        """
        ...


    def setTime(self, date: "Date") -> None:
        """
        Sets this Calendar's time with the given `Date`.
        
        Note: Calling `setTime()` with
        `Date(Long.MAX_VALUE)` or `Date(Long.MIN_VALUE)`
        may yield incorrect field values from `get()`.

        Arguments
        - date: the given Date.

        Raises
        - NullPointerException: if `date` is `null`

        See
        - .setTimeInMillis(long)
        """
        ...


    def getTimeInMillis(self) -> int:
        """
        Returns this Calendar's time value in milliseconds.

        Returns
        - the current time as UTC milliseconds from the epoch.

        See
        - .setTimeInMillis(long)
        """
        ...


    def setTimeInMillis(self, millis: int) -> None:
        """
        Sets this Calendar's current time from the given long value.

        Arguments
        - millis: the new time in UTC milliseconds from the epoch.

        See
        - .getTimeInMillis()
        """
        ...


    def get(self, field: int) -> int:
        """
        Returns the value of the given calendar field. In lenient mode,
        all calendar fields are normalized. In non-lenient mode, all
        calendar fields are validated and this method throws an
        exception if any calendar fields have out-of-range values. The
        normalization and validation are handled by the
        .complete() method, which process is calendar
        system dependent.

        Arguments
        - field: the given calendar field.

        Returns
        - the value for the given calendar field.

        Raises
        - ArrayIndexOutOfBoundsException: if the specified field is out of range
                    (`field &lt; 0 || field &gt;= FIELD_COUNT`).

        See
        - .complete()
        """
        ...


    def set(self, field: int, value: int) -> None:
        """
        Sets the given calendar field to the given value. The value is not
        interpreted by this method regardless of the leniency mode.

        Arguments
        - field: the given calendar field.
        - value: the value to be set for the given calendar field.

        Raises
        - ArrayIndexOutOfBoundsException: if the specified field is out of range
                    (`field &lt; 0 || field &gt;= FIELD_COUNT`).
        in non-lenient mode.

        See
        - .get(int)
        """
        ...


    def set(self, year: int, month: int, date: int) -> None:
        """
        Sets the values for the calendar fields `YEAR`,
        `MONTH`, and `DAY_OF_MONTH`.
        Previous values of other calendar fields are retained.  If this is not desired,
        call .clear() first.

        Arguments
        - year: the value used to set the `YEAR` calendar field.
        - month: the value used to set the `MONTH` calendar field.
        Month value is 0-based. e.g., 0 for January.
        - date: the value used to set the `DAY_OF_MONTH` calendar field.

        See
        - .set(int,int,int,int,int,int)
        """
        ...


    def set(self, year: int, month: int, date: int, hourOfDay: int, minute: int) -> None:
        """
        Sets the values for the calendar fields `YEAR`,
        `MONTH`, `DAY_OF_MONTH`,
        `HOUR_OF_DAY`, and `MINUTE`.
        Previous values of other fields are retained.  If this is not desired,
        call .clear() first.

        Arguments
        - year: the value used to set the `YEAR` calendar field.
        - month: the value used to set the `MONTH` calendar field.
        Month value is 0-based. e.g., 0 for January.
        - date: the value used to set the `DAY_OF_MONTH` calendar field.
        - hourOfDay: the value used to set the `HOUR_OF_DAY` calendar field.
        - minute: the value used to set the `MINUTE` calendar field.

        See
        - .set(int,int,int,int,int,int)
        """
        ...


    def set(self, year: int, month: int, date: int, hourOfDay: int, minute: int, second: int) -> None:
        """
        Sets the values for the fields `YEAR`, `MONTH`,
        `DAY_OF_MONTH`, `HOUR_OF_DAY`, `MINUTE`, and
        `SECOND`.
        Previous values of other fields are retained.  If this is not desired,
        call .clear() first.

        Arguments
        - year: the value used to set the `YEAR` calendar field.
        - month: the value used to set the `MONTH` calendar field.
        Month value is 0-based. e.g., 0 for January.
        - date: the value used to set the `DAY_OF_MONTH` calendar field.
        - hourOfDay: the value used to set the `HOUR_OF_DAY` calendar field.
        - minute: the value used to set the `MINUTE` calendar field.
        - second: the value used to set the `SECOND` calendar field.

        See
        - .set(int,int,int,int,int)
        """
        ...


    def clear(self) -> None:
        """
        Sets all the calendar field values and the time value
        (millisecond offset from the <a href="#Epoch">Epoch</a>) of
        this `Calendar` undefined. This means that .isSet(int) isSet() will return `False` for all the
        calendar fields, and the date and time calculations will treat
        the fields as if they had never been set. A
        `Calendar` implementation class may use its specific
        default field values for date/time calculations. For example,
        `GregorianCalendar` uses 1970 if the
        `YEAR` field value is undefined.

        See
        - .clear(int)
        """
        ...


    def clear(self, field: int) -> None:
        """
        Sets the given calendar field value and the time value
        (millisecond offset from the <a href="#Epoch">Epoch</a>) of
        this `Calendar` undefined. This means that .isSet(int) isSet(field) will return `False`, and
        the date and time calculations will treat the field as if it
        had never been set. A `Calendar` implementation
        class may use the field's specific default value for date and
        time calculations.
        
        The .HOUR_OF_DAY, .HOUR and .AM_PM
        fields are handled independently and the <a
        href="#time_resolution">the resolution rule for the time of
        day</a> is applied. Clearing one of the fields doesn't reset
        the hour of day value of this `Calendar`. Use .set(int,int) set(Calendar.HOUR_OF_DAY, 0) to reset the hour
        value.

        Arguments
        - field: the calendar field to be cleared.

        See
        - .clear()
        """
        ...


    def isSet(self, field: int) -> bool:
        """
        Determines if the given calendar field has a value set,
        including cases that the value has been set by internal fields
        calculations triggered by a `get` method call.

        Arguments
        - field: the calendar field to test

        Returns
        - `True` if the given calendar field has a value set;
        `False` otherwise.
        """
        ...


    def getDisplayName(self, field: int, style: int, locale: "Locale") -> str:
        """
        Returns the string representation of the calendar
        `field` value in the given `style` and
        `locale`.  If no string representation is
        applicable, `null` is returned. This method calls
        Calendar.get(int) get(field) to get the calendar
        `field` value if the string representation is
        applicable to the given calendar `field`.
        
        For example, if this `Calendar` is a
        `GregorianCalendar` and its date is 2005-01-01, then
        the string representation of the .MONTH field would be
        "January" in the long style in an English locale or "Jan" in
        the short style. However, no string representation would be
        available for the .DAY_OF_MONTH field, and this method
        would return `null`.
        
        The default implementation supports the calendar fields for
        which a DateFormatSymbols has names in the given
        `locale`.

        Arguments
        - field: the calendar field for which the string representation
               is returned
        - style: the style applied to the string representation; one of .SHORT_FORMAT (.SHORT), .SHORT_STANDALONE,
               .LONG_FORMAT (.LONG), .LONG_STANDALONE,
               .NARROW_FORMAT, or .NARROW_STANDALONE.
        - locale: the locale for the string representation
               (any calendar types specified by `locale` are ignored)

        Returns
        - the string representation of the given
               `field` in the given `style`, or
               `null` if no string representation is
               applicable.

        Raises
        - IllegalArgumentException: if `field` or `style` is invalid,
               or if this `Calendar` is non-lenient and any
               of the calendar fields have invalid values
        - NullPointerException: if `locale` is null

        Since
        - 1.6
        """
        ...


    def getDisplayNames(self, field: int, style: int, locale: "Locale") -> dict[str, "Integer"]:
        """
        Returns a `Map` containing all names of the calendar
        `field` in the given `style` and
        `locale` and their corresponding field values. For
        example, if this `Calendar` is a GregorianCalendar, the returned map would contain "Jan" to
        .JANUARY, "Feb" to .FEBRUARY, and so on, in the
        .SHORT short style in an English locale.
        
        Narrow names may not be unique due to use of single characters,
        such as "S" for Sunday and Saturday. In that case narrow names are not
        included in the returned `Map`.
        
        The values of other calendar fields may be taken into
        account to determine a set of display names. For example, if
        this `Calendar` is a lunisolar calendar system and
        the year value given by the .YEAR field has a leap
        month, this method would return month names containing the leap
        month name, and month names are mapped to their values specific
        for the year.
        
        The default implementation supports display names contained in
        a DateFormatSymbols. For example, if `field`
        is .MONTH and `style` is .ALL_STYLES, this method returns a `Map` containing
        all strings returned by DateFormatSymbols.getShortMonths()
        and DateFormatSymbols.getMonths().

        Arguments
        - field: the calendar field for which the display names are returned
        - style: the style applied to the string representation; one of .SHORT_FORMAT (.SHORT), .SHORT_STANDALONE,
               .LONG_FORMAT (.LONG), .LONG_STANDALONE,
               .NARROW_FORMAT, or .NARROW_STANDALONE
        - locale: the locale for the display names

        Returns
        - a `Map` containing all display names in
               `style` and `locale` and their
               field values, or `null` if no display names
               are defined for `field`

        Raises
        - IllegalArgumentException: if `field` or `style` is invalid,
               or if this `Calendar` is non-lenient and any
               of the calendar fields have invalid values
        - NullPointerException: if `locale` is null

        Since
        - 1.6
        """
        ...


    @staticmethod
    def getAvailableCalendarTypes() -> set[str]:
        """
        Returns an unmodifiable `Set` containing all calendar types
        supported by `Calendar` in the runtime environment. The available
        calendar types can be used for the <a
        href="Locale.html#def_locale_extension">Unicode locale extensions</a>.
        The `Set` returned contains at least `"gregory"`. The
        calendar types don't include aliases, such as `"gregorian"` for
        `"gregory"`.

        Returns
        - an unmodifiable `Set` containing all available calendar types

        See
        - Locale.getUnicodeLocaleType(String)

        Since
        - 1.8
        """
        ...


    def getCalendarType(self) -> str:
        """
        Returns the calendar type of this `Calendar`. Calendar types are
        defined by the *Unicode Locale Data Markup Language (LDML)*
        specification.
        
        The default implementation of this method returns the class name of
        this `Calendar` instance. Any subclasses that implement
        LDML-defined calendar systems should override this method to return
        appropriate calendar types.

        Returns
        - the LDML-defined calendar type or the class name of this
                `Calendar` instance

        See
        - Locale.Builder.setUnicodeLocaleKeyword(String, String)

        Since
        - 1.8
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this `Calendar` to the specified
        `Object`.  The result is `True` if and only if
        the argument is a `Calendar` object of the same calendar
        system that represents the same time value (millisecond offset from the
        <a href="#Epoch">Epoch</a>) under the same
        `Calendar` parameters as this object.
        
        The `Calendar` parameters are the values represented
        by the `isLenient`, `getFirstDayOfWeek`,
        `getMinimalDaysInFirstWeek` and `getTimeZone`
        methods. If there is any difference in those parameters
        between the two `Calendar`s, this method returns
        `False`.
        
        Use the .compareTo(Calendar) compareTo method to
        compare only the time values.

        Arguments
        - obj: the object to compare with.

        Returns
        - `True` if this object is equal to `obj`;
        `False` otherwise.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this calendar.

        Returns
        - a hash code value for this object.

        Since
        - 1.2
        """
        ...


    def before(self, when: "Object") -> bool:
        """
        Returns whether this `Calendar` represents a time
        before the time represented by the specified
        `Object`. This method is equivalent to:
        ````compareTo(when) < 0````
        if and only if `when` is a `Calendar`
        instance. Otherwise, the method returns `False`.

        Arguments
        - when: the `Object` to be compared

        Returns
        - `True` if the time of this
        `Calendar` is before the time represented by
        `when`; `False` otherwise.

        See
        - .compareTo(Calendar)
        """
        ...


    def after(self, when: "Object") -> bool:
        """
        Returns whether this `Calendar` represents a time
        after the time represented by the specified
        `Object`. This method is equivalent to:
        ````compareTo(when) > 0````
        if and only if `when` is a `Calendar`
        instance. Otherwise, the method returns `False`.

        Arguments
        - when: the `Object` to be compared

        Returns
        - `True` if the time of this `Calendar` is
        after the time represented by `when`; `False`
        otherwise.

        See
        - .compareTo(Calendar)
        """
        ...


    def compareTo(self, anotherCalendar: "Calendar") -> int:
        """
        Compares the time values (millisecond offsets from the <a
        href="#Epoch">Epoch</a>) represented by two
        `Calendar` objects.

        Arguments
        - anotherCalendar: the `Calendar` to be compared.

        Returns
        - the value `0` if the time represented by the argument
        is equal to the time represented by this `Calendar`; a value
        less than `0` if the time of this `Calendar` is
        before the time represented by the argument; and a value greater than
        `0` if the time of this `Calendar` is after the
        time represented by the argument.

        Raises
        - NullPointerException: if the specified `Calendar` is
                   `null`.
        - IllegalArgumentException: if the time value of the
        specified `Calendar` object can't be obtained due to
        any invalid calendar values.

        Since
        - 1.5
        """
        ...


    def add(self, field: int, amount: int) -> None:
        """
        Adds or subtracts the specified amount of time to the given calendar field,
        based on the calendar's rules. For example, to subtract 5 days from
        the current time of the calendar, you can achieve it by calling:
        `add(Calendar.DAY_OF_MONTH, -5)`.

        Arguments
        - field: the calendar field.
        - amount: the amount of date or time to be added to the field.

        See
        - .set(int,int)
        """
        ...


    def roll(self, field: int, up: bool) -> None:
        """
        Adds or subtracts (up/down) a single unit of time on the given time
        field without changing larger fields. For example, to roll the current
        date up by one day, you can achieve it by calling:
        roll(Calendar.DATE, True).
        When rolling on the year or Calendar.YEAR field, it will roll the year
        value in the range between 1 and the value returned by calling
        `getMaximum(Calendar.YEAR)`.
        When rolling on the month or Calendar.MONTH field, other fields like
        date might conflict and, need to be changed. For instance,
        rolling the month on the date 01/31/96 will result in 02/29/96.
        When rolling on the hour-in-day or Calendar.HOUR_OF_DAY field, it will
        roll the hour value in the range between 0 and 23, which is zero-based.

        Arguments
        - field: the time field.
        - up: indicates if the value of the specified time field is to be
        rolled up or rolled down. Use True if rolling up, False otherwise.

        See
        - Calendar.set(int,int)
        """
        ...


    def roll(self, field: int, amount: int) -> None:
        """
        Adds the specified (signed) amount to the specified calendar field
        without changing larger fields.  A negative amount means to roll
        down.
        
        NOTE:  This default implementation on `Calendar` just repeatedly calls the
        version of .roll(int,boolean) roll() that rolls by one unit.  This may not
        always do the right thing.  For example, if the `DAY_OF_MONTH` field is 31,
        rolling through February will leave it set to 28.  The `GregorianCalendar`
        version of this function takes care of this problem.  Other subclasses
        should also provide overrides of this function that do the right thing.

        Arguments
        - field: the calendar field.
        - amount: the signed amount to add to the calendar `field`.

        See
        - .set(int,int)

        Since
        - 1.2
        """
        ...


    def setTimeZone(self, value: "TimeZone") -> None:
        """
        Sets the time zone with the given time zone value.

        Arguments
        - value: the given time zone.
        """
        ...


    def getTimeZone(self) -> "TimeZone":
        """
        Gets the time zone.

        Returns
        - the time zone object associated with this calendar.
        """
        ...


    def setLenient(self, lenient: bool) -> None:
        """
        Specifies whether or not date/time interpretation is to be lenient.  With
        lenient interpretation, a date such as "February 942, 1996" will be
        treated as being equivalent to the 941st day after February 1, 1996.
        With strict (non-lenient) interpretation, such dates will cause an exception to be
        thrown. The default is lenient.

        Arguments
        - lenient: `True` if the lenient mode is to be turned
        on; `False` if it is to be turned off.

        See
        - java.text.DateFormat.setLenient
        """
        ...


    def isLenient(self) -> bool:
        """
        Tells whether date/time interpretation is to be lenient.

        Returns
        - `True` if the interpretation mode of this calendar is lenient;
        `False` otherwise.

        See
        - .setLenient(boolean)
        """
        ...


    def setFirstDayOfWeek(self, value: int) -> None:
        """
        Sets what the first day of the week is; e.g., `SUNDAY` in the U.S.,
        `MONDAY` in France.

        Arguments
        - value: the given first day of the week.

        See
        - .getMinimalDaysInFirstWeek()
        """
        ...


    def getFirstDayOfWeek(self) -> int:
        """
        Gets what the first day of the week is; e.g., `SUNDAY` in the U.S.,
        `MONDAY` in France.

        Returns
        - the first day of the week.

        See
        - .getMinimalDaysInFirstWeek()
        """
        ...


    def setMinimalDaysInFirstWeek(self, value: int) -> None:
        """
        Sets what the minimal days required in the first week of the year are;
        For example, if the first week is defined as one that contains the first
        day of the first month of a year, call this method with value 1. If it
        must be a full week, use value 7.

        Arguments
        - value: the given minimal days required in the first week
        of the year.

        See
        - .getMinimalDaysInFirstWeek()
        """
        ...


    def getMinimalDaysInFirstWeek(self) -> int:
        """
        Gets what the minimal days required in the first week of the year are;
        e.g., if the first week is defined as one that contains the first day
        of the first month of a year, this method returns 1. If
        the minimal days required must be a full week, this method
        returns 7.

        Returns
        - the minimal days required in the first week of the year.

        See
        - .setMinimalDaysInFirstWeek(int)
        """
        ...


    def isWeekDateSupported(self) -> bool:
        """
        Returns whether this `Calendar` supports week dates.
        
        The default implementation of this method returns `False`.

        Returns
        - `True` if this `Calendar` supports week dates;
                `False` otherwise.

        See
        - .getWeeksInWeekYear()

        Since
        - 1.7
        """
        ...


    def getWeekYear(self) -> int:
        """
        Returns the week year represented by this `Calendar`. The
        week year is in sync with the week cycle. The .getFirstDayOfWeek() first day of the first week is the first
        day of the week year.
        
        The default implementation of this method throws an
        UnsupportedOperationException.

        Returns
        - the week year of this `Calendar`

        Raises
        - UnsupportedOperationException: if any week year numbering isn't supported
                   in this `Calendar`.

        See
        - .getMinimalDaysInFirstWeek()

        Since
        - 1.7
        """
        ...


    def setWeekDate(self, weekYear: int, weekOfYear: int, dayOfWeek: int) -> None:
        """
        Sets the date of this `Calendar` with the given date
        specifiers - week year, week of year, and day of week.
        
        Unlike the `set` method, all of the calendar fields
        and `time` values are calculated upon return.
        
        If `weekOfYear` is out of the valid week-of-year range
        in `weekYear`, the `weekYear` and `weekOfYear` values are adjusted in lenient mode, or an `IllegalArgumentException` is thrown in non-lenient mode.
        
        The default implementation of this method throws an
        `UnsupportedOperationException`.

        Arguments
        - weekYear: the week year
        - weekOfYear: the week number based on `weekYear`
        - dayOfWeek: the day of week value: one of the constants
                          for the .DAY_OF_WEEK field: .SUNDAY, ..., .SATURDAY.

        Raises
        - IllegalArgumentException: if any of the given date specifiers is invalid
                   or any of the calendar fields are inconsistent
                   with the given date specifiers in non-lenient mode
        - UnsupportedOperationException: if any week year numbering isn't supported in this
                   `Calendar`.

        See
        - .getMinimalDaysInFirstWeek()

        Since
        - 1.7
        """
        ...


    def getWeeksInWeekYear(self) -> int:
        """
        Returns the number of weeks in the week year represented by this
        `Calendar`.
        
        The default implementation of this method throws an
        `UnsupportedOperationException`.

        Returns
        - the number of weeks in the week year.

        Raises
        - UnsupportedOperationException: if any week year numbering isn't supported in this
                   `Calendar`.

        See
        - .getActualMaximum(int)

        Since
        - 1.7
        """
        ...


    def getMinimum(self, field: int) -> int:
        """
        Returns the minimum value for the given calendar field of this
        `Calendar` instance. The minimum value is defined as
        the smallest value returned by the .get(int) get method
        for any possible time value.  The minimum value depends on
        calendar system specific parameters of the instance.

        Arguments
        - field: the calendar field.

        Returns
        - the minimum value for the given calendar field.

        See
        - .getActualMaximum(int)
        """
        ...


    def getMaximum(self, field: int) -> int:
        """
        Returns the maximum value for the given calendar field of this
        `Calendar` instance. The maximum value is defined as
        the largest value returned by the .get(int) get method
        for any possible time value. The maximum value depends on
        calendar system specific parameters of the instance.

        Arguments
        - field: the calendar field.

        Returns
        - the maximum value for the given calendar field.

        See
        - .getActualMaximum(int)
        """
        ...


    def getGreatestMinimum(self, field: int) -> int:
        """
        Returns the highest minimum value for the given calendar field
        of this `Calendar` instance. The highest minimum
        value is defined as the largest value returned by .getActualMinimum(int) for any possible time value. The
        greatest minimum value depends on calendar system specific
        parameters of the instance.

        Arguments
        - field: the calendar field.

        Returns
        - the highest minimum value for the given calendar field.

        See
        - .getActualMaximum(int)
        """
        ...


    def getLeastMaximum(self, field: int) -> int:
        """
        Returns the lowest maximum value for the given calendar field
        of this `Calendar` instance. The lowest maximum
        value is defined as the smallest value returned by .getActualMaximum(int) for any possible time value. The least
        maximum value depends on calendar system specific parameters of
        the instance. For example, a `Calendar` for the
        Gregorian calendar system returns 28 for the
        `DAY_OF_MONTH` field, because the 28th is the last
        day of the shortest month of this calendar, February in a
        common year.

        Arguments
        - field: the calendar field.

        Returns
        - the lowest maximum value for the given calendar field.

        See
        - .getActualMaximum(int)
        """
        ...


    def getActualMinimum(self, field: int) -> int:
        """
        Returns the minimum value that the specified calendar field
        could have, given the time value of this `Calendar`.
        
        The default implementation of this method uses an iterative
        algorithm to determine the actual minimum value for the
        calendar field. Subclasses should, if possible, override this
        with a more efficient implementation - in many cases, they can
        simply return `getMinimum()`.

        Arguments
        - field: the calendar field

        Returns
        - the minimum of the given calendar field for the time
        value of this `Calendar`

        See
        - .getActualMaximum(int)

        Since
        - 1.2
        """
        ...


    def getActualMaximum(self, field: int) -> int:
        """
        Returns the maximum value that the specified calendar field
        could have, given the time value of this
        `Calendar`. For example, the actual maximum value of
        the `MONTH` field is 12 in some years, and 13 in
        other years in the Hebrew calendar system.
        
        The default implementation of this method uses an iterative
        algorithm to determine the actual maximum value for the
        calendar field. Subclasses should, if possible, override this
        with a more efficient implementation.

        Arguments
        - field: the calendar field

        Returns
        - the maximum of the given calendar field for the time
        value of this `Calendar`

        See
        - .getActualMinimum(int)

        Since
        - 1.2
        """
        ...


    def clone(self) -> "Object":
        """
        Creates and returns a copy of this object.

        Returns
        - a copy of this object.
        """
        ...


    def toString(self) -> str:
        """
        Return a string representation of this calendar. This method
        is intended to be used only for debugging purposes, and the
        format of the returned string may vary between implementations.
        The returned string may be empty but may not be `null`.

        Returns
        - a string representation of this calendar.
        """
        ...


    def toInstant(self) -> "Instant":
        """
        Converts this object to an Instant.
        
        The conversion creates an `Instant` that represents the
        same point on the time-line as this `Calendar`.

        Returns
        - the instant representing the same point on the time-line

        Since
        - 1.8
        """
        ...


    class Builder:
        """
        `Calendar.Builder` is used for creating a `Calendar` from
        various date-time parameters.
        
        There are two ways to set a `Calendar` to a date-time value. One
        is to set the instant parameter to a millisecond offset from the <a
        href="Calendar.html#Epoch">Epoch</a>. The other is to set individual
        field parameters, such as Calendar.YEAR YEAR, to their desired
        values. These two ways can't be mixed. Trying to set both the instant and
        individual fields will cause an IllegalStateException to be
        thrown. However, it is permitted to override previous values of the
        instant or field parameters.
        
        If no enough field parameters are given for determining date and/or
        time, calendar specific default values are used when building a
        `Calendar`. For example, if the Calendar.YEAR YEAR value
        isn't given for the Gregorian calendar, 1970 will be used. If there are
        any conflicts among field parameters, the <a
        href="Calendar.html#resolution"> resolution rules</a> are applied.
        Therefore, the order of field setting matters.
        
        In addition to the date-time parameters,
        the .setLocale(Locale) locale,
        .setTimeZone(TimeZone) time zone,
        .setWeekDefinition(int, int) week definition, and
        .setLenient(boolean) leniency mode parameters can be set.
        
        **Examples**
        The following are sample usages. Sample code assumes that the
        `Calendar` constants are statically imported.
        
        The following code produces a `Calendar` with date 2012-12-31
        (Gregorian) because Monday is the first day of a week with the <a
        href="GregorianCalendar.html#iso8601_compatible_setting"> ISO 8601
        compatible week parameters</a>.
        ```
          Calendar cal = new Calendar.Builder().setCalendarType("iso8601")
                               .setWeekDate(2013, 1, MONDAY).build();```
        The following code produces a Japanese `Calendar` with date
        1989-01-08 (Gregorian), assuming that the default Calendar.ERA ERA
        is *Heisei* that started on that day.
        ```
          Calendar cal = new Calendar.Builder().setCalendarType("japanese")
                               .setFields(YEAR, 1, DAY_OF_YEAR, 1).build();```

        See
        - Calendar.fields

        Since
        - 1.8
        """

        def __init__(self):
            """
            Constructs a `Calendar.Builder`.
            """
            ...


        def setInstant(self, instant: int) -> "Builder":
            """
            Sets the instant parameter to the given `instant` value that is
            a millisecond offset from <a href="Calendar.html#Epoch">the
            Epoch</a>.

            Arguments
            - instant: a millisecond offset from the Epoch

            Returns
            - this `Calendar.Builder`

            Raises
            - IllegalStateException: if any of the field parameters have
                                          already been set

            See
            - Calendar.time
            """
            ...


        def setInstant(self, instant: "Date") -> "Builder":
            """
            Sets the instant parameter to the `instant` value given by a
            Date. This method is equivalent to a call to
            .setInstant(long) setInstant(instant.getTime()).

            Arguments
            - instant: a `Date` representing a millisecond offset from
                           the Epoch

            Returns
            - this `Calendar.Builder`

            Raises
            - NullPointerException: if `instant` is `null`
            - IllegalStateException: if any of the field parameters have
                                          already been set

            See
            - Calendar.time
            """
            ...


        def set(self, field: int, value: int) -> "Builder":
            """
            Sets the `field` parameter to the given `value`.
            `field` is an index to the Calendar.fields, such as
            Calendar.DAY_OF_MONTH DAY_OF_MONTH. Field value validation is
            not performed in this method. Any out of range values are either
            normalized in lenient mode or detected as an invalid value in
            non-lenient mode when building a `Calendar`.

            Arguments
            - field: an index to the `Calendar` fields
            - value: the field value

            Returns
            - this `Calendar.Builder`

            Raises
            - IllegalArgumentException: if `field` is invalid
            - IllegalStateException: if the instant value has already been set,
                                 or if fields have been set too many
                                 (approximately Integer.MAX_VALUE) times.

            See
            - Calendar.set(int, int)
            """
            ...


        def setFields(self, *fieldValuePairs: Tuple[int, ...]) -> "Builder":
            """
            Sets field parameters to their values given by
            `fieldValuePairs` that are pairs of a field and its value.
            For example,
            ```
              setFields(Calendar.YEAR, 2013,
                        Calendar.MONTH, Calendar.DECEMBER,
                        Calendar.DAY_OF_MONTH, 23);```
            is equivalent to the sequence of the following
            .set(int, int) set calls:
            ```
              set(Calendar.YEAR, 2013)
              .set(Calendar.MONTH, Calendar.DECEMBER)
              .set(Calendar.DAY_OF_MONTH, 23);```

            Arguments
            - fieldValuePairs: field-value pairs

            Returns
            - this `Calendar.Builder`

            Raises
            - NullPointerException: if `fieldValuePairs` is `null`
            - IllegalArgumentException: if any of fields are invalid,
                        or if `fieldValuePairs.length` is an odd number.
            - IllegalStateException: if the instant value has been set,
                        or if fields have been set too many (approximately
                        Integer.MAX_VALUE) times.
            """
            ...


        def setDate(self, year: int, month: int, dayOfMonth: int) -> "Builder":
            """
            Sets the date field parameters to the values given by `year`,
            `month`, and `dayOfMonth`. This method is equivalent to
            a call to:
            ```
              setFields(Calendar.YEAR, year,
                        Calendar.MONTH, month,
                        Calendar.DAY_OF_MONTH, dayOfMonth);```

            Arguments
            - year: the Calendar.YEAR YEAR value
            - month: the Calendar.MONTH MONTH value
                              (the month numbering is *0-based*).
            - dayOfMonth: the Calendar.DAY_OF_MONTH DAY_OF_MONTH value

            Returns
            - this `Calendar.Builder`
            """
            ...


        def setTimeOfDay(self, hourOfDay: int, minute: int, second: int) -> "Builder":
            """
            Sets the time of day field parameters to the values given by
            `hourOfDay`, `minute`, and `second`. This method is
            equivalent to a call to:
            ```
              setTimeOfDay(hourOfDay, minute, second, 0);```

            Arguments
            - hourOfDay: the Calendar.HOUR_OF_DAY HOUR_OF_DAY value
                             (24-hour clock)
            - minute: the Calendar.MINUTE MINUTE value
            - second: the Calendar.SECOND SECOND value

            Returns
            - this `Calendar.Builder`
            """
            ...


        def setTimeOfDay(self, hourOfDay: int, minute: int, second: int, millis: int) -> "Builder":
            """
            Sets the time of day field parameters to the values given by
            `hourOfDay`, `minute`, `second`, and
            `millis`. This method is equivalent to a call to:
            ```
              setFields(Calendar.HOUR_OF_DAY, hourOfDay,
                        Calendar.MINUTE, minute,
                        Calendar.SECOND, second,
                        Calendar.MILLISECOND, millis);```

            Arguments
            - hourOfDay: the Calendar.HOUR_OF_DAY HOUR_OF_DAY value
                             (24-hour clock)
            - minute: the Calendar.MINUTE MINUTE value
            - second: the Calendar.SECOND SECOND value
            - millis: the Calendar.MILLISECOND MILLISECOND value

            Returns
            - this `Calendar.Builder`
            """
            ...


        def setWeekDate(self, weekYear: int, weekOfYear: int, dayOfWeek: int) -> "Builder":
            """
            Sets the week-based date parameters to the values with the given
            date specifiers - week year, week of year, and day of week.
            
            If the specified calendar doesn't support week dates, the
            .build() build method will throw an IllegalArgumentException.

            Arguments
            - weekYear: the week year
            - weekOfYear: the week number based on `weekYear`
            - dayOfWeek: the day of week value: one of the constants
                for the Calendar.DAY_OF_WEEK DAY_OF_WEEK field:
                Calendar.SUNDAY SUNDAY, ..., Calendar.SATURDAY SATURDAY.

            Returns
            - this `Calendar.Builder`

            See
            - Calendar.isWeekDateSupported()
            """
            ...


        def setTimeZone(self, zone: "TimeZone") -> "Builder":
            """
            Sets the time zone parameter to the given `zone`. If no time
            zone parameter is given to this `Calendar.Builder`, the
            TimeZone.getDefault() default
            {@code TimeZone} will be used in the .build() build
            method.

            Arguments
            - zone: the TimeZone

            Returns
            - this `Calendar.Builder`

            Raises
            - NullPointerException: if `zone` is `null`

            See
            - Calendar.setTimeZone(TimeZone)
            """
            ...


        def setLenient(self, lenient: bool) -> "Builder":
            """
            Sets the lenient mode parameter to the value given by `lenient`.
            If no lenient parameter is given to this `Calendar.Builder`,
            lenient mode will be used in the .build() build method.

            Arguments
            - lenient: `True` for lenient mode;
                           `False` for non-lenient mode

            Returns
            - this `Calendar.Builder`

            See
            - Calendar.setLenient(boolean)
            """
            ...


        def setCalendarType(self, type: str) -> "Builder":
            """
            Sets the calendar type parameter to the given `type`. The
            calendar type given by this method has precedence over any explicit
            or implicit calendar type given by the
            .setLocale(Locale) locale.
            
            In addition to the available calendar types returned by the
            Calendar.getAvailableCalendarTypes() Calendar.getAvailableCalendarTypes
            method, `"gregorian"` and `"iso8601"` as aliases of
            `"gregory"` can be used with this method.

            Arguments
            - type: the calendar type

            Returns
            - this `Calendar.Builder`

            Raises
            - NullPointerException: if `type` is `null`
            - IllegalArgumentException: if `type` is unknown
            - IllegalStateException: if another calendar type has already been set

            See
            - Calendar.getAvailableCalendarTypes()
            """
            ...


        def setLocale(self, locale: "Locale") -> "Builder":
            """
            Sets the locale parameter to the given `locale`. If no locale
            is given to this `Calendar.Builder`, the Locale.getDefault(Locale.Category) default {@code Locale}
            for Locale.Category.FORMAT will be used.
            
            If no calendar type is explicitly given by a call to the
            .setCalendarType(String) setCalendarType method,
            the `Locale` value is used to determine what type of
            `Calendar` to be built.
            
            If no week definition parameters are explicitly given by a call to
            the .setWeekDefinition(int,int) setWeekDefinition method, the
            `Locale`'s default values are used.

            Arguments
            - locale: the Locale

            Returns
            - this `Calendar.Builder`

            Raises
            - NullPointerException: if `locale` is `null`

            See
            - Calendar.getInstance(Locale)
            """
            ...


        def setWeekDefinition(self, firstDayOfWeek: int, minimalDaysInFirstWeek: int) -> "Builder":
            """
            Sets the week definition parameters to the values given by
            `firstDayOfWeek` and `minimalDaysInFirstWeek` that are
            used to determine the <a href="Calendar.html#first_week">first
            week</a> of a year. The parameters given by this method have
            precedence over the default values given by the
            .setLocale(Locale) locale.

            Arguments
            - firstDayOfWeek: the first day of a week; one of
                                  Calendar.SUNDAY to Calendar.SATURDAY
            - minimalDaysInFirstWeek: the minimal number of days in the first
                                          week (1..7)

            Returns
            - this `Calendar.Builder`

            Raises
            - IllegalArgumentException: if `firstDayOfWeek` or
                                             `minimalDaysInFirstWeek` is invalid

            See
            - Calendar.getMinimalDaysInFirstWeek()
            """
            ...


        def build(self) -> "Calendar":
            """
            Returns a `Calendar` built from the parameters set by the
            setter methods. The calendar type given by the .setCalendarType(String)
            setCalendarType method or the .setLocale(Locale) locale is
            used to determine what `Calendar` to be created. If no explicit
            calendar type is given, the locale's default calendar is created.
            
            If the calendar type is `"iso8601"`, the
            GregorianCalendar.setGregorianChange(Date) Gregorian change date
            of a GregorianCalendar is set to `Date(Long.MIN_VALUE)`
            to be the *proleptic* Gregorian calendar. Its week definition
            parameters are also set to be <a
            href="GregorianCalendar.html#iso8601_compatible_setting">compatible
            with the ISO 8601 standard</a>. Note that the
            GregorianCalendar.getCalendarType() getCalendarType method of
            a `GregorianCalendar` created with `"iso8601"` returns
            `"gregory"`.
            
            The default values are used for locale and time zone if these
            parameters haven't been given explicitly.
            
            If the locale contains the time zone with "tz"
            <a href="Locale.html#def_locale_extension">Unicode extension</a>,
            and time zone hasn't been given explicitly, time zone in the locale
            is used.
            
            Any out of range field values are either normalized in lenient
            mode or detected as an invalid value in non-lenient mode.

            Returns
            - a `Calendar` built with parameters of this `Calendar.Builder`

            Raises
            - IllegalArgumentException: if the calendar type is unknown, or
                        if any invalid field values are given in non-lenient mode, or
                        if a week date is given for the calendar type that doesn't
                        support week dates.

            See
            - TimeZone.getDefault()
            """
            ...
