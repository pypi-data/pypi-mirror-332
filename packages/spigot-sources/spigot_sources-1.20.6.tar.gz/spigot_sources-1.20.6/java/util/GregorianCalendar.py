"""
Python module generated from Java source file java.util.GregorianCalendar

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInputStream
from java.time import Instant
from java.time import ZonedDateTime
from java.time.temporal import ChronoField
from java.util import *
from sun.util.calendar import BaseCalendar
from sun.util.calendar import CalendarDate
from sun.util.calendar import CalendarSystem
from sun.util.calendar import CalendarUtils
from sun.util.calendar import Era
from sun.util.calendar import Gregorian
from sun.util.calendar import JulianCalendar
from sun.util.calendar import ZoneInfo
from typing import Any, Callable, Iterable, Tuple


class GregorianCalendar(Calendar):
    """
    `GregorianCalendar` is a concrete subclass of
    `Calendar` and provides the standard calendar system
    used by most of the world.
    
     `GregorianCalendar` is a hybrid calendar that
    supports both the Julian and Gregorian calendar systems with the
    support of a single discontinuity, which corresponds by default to
    the Gregorian date when the Gregorian calendar was instituted
    (October 15, 1582 in some countries, later in others).  The cutover
    date may be changed by the caller by calling .setGregorianChange(Date) setGregorianChange().
    
    
    Historically, in those countries which adopted the Gregorian calendar first,
    October 4, 1582 (Julian) was thus followed by October 15, 1582 (Gregorian). This calendar models
    this correctly.  Before the Gregorian cutover, `GregorianCalendar`
    implements the Julian calendar.  The only difference between the Gregorian
    and the Julian calendar is the leap year rule. The Julian calendar specifies
    leap years every four years, whereas the Gregorian calendar omits century
    years which are not divisible by 400.
    
    
    `GregorianCalendar` implements *proleptic* Gregorian and
    Julian calendars. That is, dates are computed by extrapolating the current
    rules indefinitely far backward and forward in time. As a result,
    `GregorianCalendar` may be used for all years to generate
    meaningful and consistent results. However, dates obtained using
    `GregorianCalendar` are historically accurate only from March 1, 4
    AD onward, when modern Julian calendar rules were adopted.  Before this date,
    leap year rules were applied irregularly, and before 45 BC the Julian
    calendar did not even exist.
    
    
    Prior to the institution of the Gregorian calendar, New Year's Day was
    March 25. To avoid confusion, this calendar always uses January 1. A manual
    adjustment may be made if desired for dates that are prior to the Gregorian
    changeover and which fall between January 1 and March 24.
    
    <h2><a id="week_and_year">Week Of Year and Week Year</a></h2>
    
    Values calculated for the Calendar.WEEK_OF_YEAR
    WEEK_OF_YEAR field range from 1 to 53. The first week of a
    calendar year is the earliest seven day period starting on Calendar.getFirstDayOfWeek() getFirstDayOfWeek() that contains at
    least Calendar.getMinimalDaysInFirstWeek()
    getMinimalDaysInFirstWeek() days from that year. It thus depends
    on the values of `getMinimalDaysInFirstWeek()`, `getFirstDayOfWeek()`, and the day of the week of January 1. Weeks
    between week 1 of one year and week 1 of the following year
    (exclusive) are numbered sequentially from 2 to 52 or 53 (except
    for year(s) involved in the Julian-Gregorian transition).
    
    The `getFirstDayOfWeek()` and `getMinimalDaysInFirstWeek()` values are initialized using
    locale-dependent resources when constructing a `GregorianCalendar`. <a id="iso8601_compatible_setting">The week
    determination is compatible</a> with the ISO 8601 standard when `getFirstDayOfWeek()` is `MONDAY` and `getMinimalDaysInFirstWeek()` is 4, which values are used in locales
    where the standard is preferred. These values can explicitly be set by
    calling Calendar.setFirstDayOfWeek(int) setFirstDayOfWeek() and
    Calendar.setMinimalDaysInFirstWeek(int)
    setMinimalDaysInFirstWeek().
    
    A <a id="week_year">*week year*</a> is in sync with a
    `WEEK_OF_YEAR` cycle. All weeks between the first and last
    weeks (inclusive) have the same *week year* value.
    Therefore, the first and last days of a week year may have
    different calendar year values.
    
    For example, January 1, 1998 is a Thursday. If `getFirstDayOfWeek()` is `MONDAY` and `getMinimalDaysInFirstWeek()` is 4 (ISO 8601 standard compatible
    setting), then week 1 of 1998 starts on December 29, 1997, and ends
    on January 4, 1998. The week year is 1998 for the last three days
    of calendar year 1997. If, however, `getFirstDayOfWeek()` is
    `SUNDAY`, then week 1 of 1998 starts on January 4, 1998, and
    ends on January 10, 1998; the first three days of 1998 then are
    part of week 53 of 1997 and their week year is 1997.
    
    <h3>Week Of Month</h3>
    
    Values calculated for the `WEEK_OF_MONTH` field range from 0
    to 6.  Week 1 of a month (the days with `WEEK_OF_MONTH =
    1`) is the earliest set of at least
    `getMinimalDaysInFirstWeek()` contiguous days in that month,
    ending on the day before `getFirstDayOfWeek()`.  Unlike
    week 1 of a year, week 1 of a month may be shorter than 7 days, need
    not start on `getFirstDayOfWeek()`, and will not include days of
    the previous month.  Days of a month before week 1 have a
    `WEEK_OF_MONTH` of 0.
    
    For example, if `getFirstDayOfWeek()` is `SUNDAY`
    and `getMinimalDaysInFirstWeek()` is 4, then the first week of
    January 1998 is Sunday, January 4 through Saturday, January 10.  These days
    have a `WEEK_OF_MONTH` of 1.  Thursday, January 1 through
    Saturday, January 3 have a `WEEK_OF_MONTH` of 0.  If
    `getMinimalDaysInFirstWeek()` is changed to 3, then January 1
    through January 3 have a `WEEK_OF_MONTH` of 1.
    
    <h3>Default Fields Values</h3>
    
    The `clear` method sets calendar field(s)
    undefined. `GregorianCalendar` uses the following
    default value for each calendar field if its value is undefined.
    
    <table class="striped" style="text-align: left; width: 66%;">
    <caption style="display:none">GregorianCalendar default field values</caption>
      <thead>
        <tr>
          <th scope="col">
             Field
          </th>
          <th scope="col">
             Default Value
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">
                 `ERA`
          </th>
          <td>
                 `AD`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `YEAR`
          </th>
          <td>
                 `1970`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `MONTH`
          </th>
          <td>
                 `JANUARY`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `DAY_OF_MONTH`
          </th>
          <td>
                 `1`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `DAY_OF_WEEK`
          </th>
          <td>
                 `the first day of week`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `WEEK_OF_MONTH`
          </th>
          <td>
                 `0`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `DAY_OF_WEEK_IN_MONTH`
          </th>
          <td>
                 `1`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `AM_PM`
          </th>
          <td>
                 `AM`
          </td>
        </tr>
        <tr>
          <th scope="row">
                 `HOUR, HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND`
          </th>
          <td>
                 `0`
          </td>
        </tr>
      </tbody>
    </table>
    Default values are not applicable for the fields not listed above.
    
    
    <strong>Example:</strong>
    <blockquote>
    ```
    // get the supported ids for GMT-08:00 (Pacific Standard Time)
    String[] ids = TimeZone.getAvailableIDs(-8 * 60 * 60 * 1000);
    // if no ids were returned, something is wrong. get out.
    if (ids.length == 0)
        System.exit(0);
    
     // begin output
    System.out.println("Current Time");
    
    // create a Pacific Standard Time time zone
    SimpleTimeZone pdt = new SimpleTimeZone(-8 * 60 * 60 * 1000, ids[0]);
    
    // set up rules for Daylight Saving Time
    pdt.setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2 * 60 * 60 * 1000);
    pdt.setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2 * 60 * 60 * 1000);
    
    // create a GregorianCalendar with the Pacific Daylight time zone
    // and the current date and time
    Calendar calendar = new GregorianCalendar(pdt);
    Date trialTime = new Date();
    calendar.setTime(trialTime);
    
    // print out a bunch of interesting things
    System.out.println("ERA: " + calendar.get(Calendar.ERA));
    System.out.println("YEAR: " + calendar.get(Calendar.YEAR));
    System.out.println("MONTH: " + calendar.get(Calendar.MONTH));
    System.out.println("WEEK_OF_YEAR: " + calendar.get(Calendar.WEEK_OF_YEAR));
    System.out.println("WEEK_OF_MONTH: " + calendar.get(Calendar.WEEK_OF_MONTH));
    System.out.println("DATE: " + calendar.get(Calendar.DATE));
    System.out.println("DAY_OF_MONTH: " + calendar.get(Calendar.DAY_OF_MONTH));
    System.out.println("DAY_OF_YEAR: " + calendar.get(Calendar.DAY_OF_YEAR));
    System.out.println("DAY_OF_WEEK: " + calendar.get(Calendar.DAY_OF_WEEK));
    System.out.println("DAY_OF_WEEK_IN_MONTH: "
                       + calendar.get(Calendar.DAY_OF_WEEK_IN_MONTH));
    System.out.println("AM_PM: " + calendar.get(Calendar.AM_PM));
    System.out.println("HOUR: " + calendar.get(Calendar.HOUR));
    System.out.println("HOUR_OF_DAY: " + calendar.get(Calendar.HOUR_OF_DAY));
    System.out.println("MINUTE: " + calendar.get(Calendar.MINUTE));
    System.out.println("SECOND: " + calendar.get(Calendar.SECOND));
    System.out.println("MILLISECOND: " + calendar.get(Calendar.MILLISECOND));
    System.out.println("ZONE_OFFSET: "
                       + (calendar.get(Calendar.ZONE_OFFSET)/(60*60*1000)));
    System.out.println("DST_OFFSET: "
                       + (calendar.get(Calendar.DST_OFFSET)/(60*60*1000)));
    System.out.println("Current Time, with hour reset to 3");
    calendar.clear(Calendar.HOUR_OF_DAY); // so doesn't override
    calendar.set(Calendar.HOUR, 3);
    System.out.println("ERA: " + calendar.get(Calendar.ERA));
    System.out.println("YEAR: " + calendar.get(Calendar.YEAR));
    System.out.println("MONTH: " + calendar.get(Calendar.MONTH));
    System.out.println("WEEK_OF_YEAR: " + calendar.get(Calendar.WEEK_OF_YEAR));
    System.out.println("WEEK_OF_MONTH: " + calendar.get(Calendar.WEEK_OF_MONTH));
    System.out.println("DATE: " + calendar.get(Calendar.DATE));
    System.out.println("DAY_OF_MONTH: " + calendar.get(Calendar.DAY_OF_MONTH));
    System.out.println("DAY_OF_YEAR: " + calendar.get(Calendar.DAY_OF_YEAR));
    System.out.println("DAY_OF_WEEK: " + calendar.get(Calendar.DAY_OF_WEEK));
    System.out.println("DAY_OF_WEEK_IN_MONTH: "
                       + calendar.get(Calendar.DAY_OF_WEEK_IN_MONTH));
    System.out.println("AM_PM: " + calendar.get(Calendar.AM_PM));
    System.out.println("HOUR: " + calendar.get(Calendar.HOUR));
    System.out.println("HOUR_OF_DAY: " + calendar.get(Calendar.HOUR_OF_DAY));
    System.out.println("MINUTE: " + calendar.get(Calendar.MINUTE));
    System.out.println("SECOND: " + calendar.get(Calendar.SECOND));
    System.out.println("MILLISECOND: " + calendar.get(Calendar.MILLISECOND));
    System.out.println("ZONE_OFFSET: "
           + (calendar.get(Calendar.ZONE_OFFSET)/(60*60*1000))); // in hours
    System.out.println("DST_OFFSET: "
           + (calendar.get(Calendar.DST_OFFSET)/(60*60*1000))); // in hours
    ```
    </blockquote>

    Author(s)
    - David Goldsmith, Mark Davis, Chen-Lieh Huang, Alan Liu

    See
    - TimeZone

    Since
    - 1.1
    """

    BC = 0
    """
    Value of the `ERA` field indicating
    the period before the common era (before Christ), also known as BCE.
    The sequence of years at the transition from `BC` to `AD` is
    ..., 2 BC, 1 BC, 1 AD, 2 AD,...

    See
    - .ERA
    """
    AD = 1
    """
    Value of the `ERA` field indicating
    the common era (Anno Domini), also known as CE.
    The sequence of years at the transition from `BC` to `AD` is
    ..., 2 BC, 1 BC, 1 AD, 2 AD,...

    See
    - .ERA
    """


    def __init__(self):
        """
        Constructs a default `GregorianCalendar` using the current time
        in the default time zone with the default
        Locale.Category.FORMAT FORMAT locale.
        """
        ...


    def __init__(self, zone: "TimeZone"):
        """
        Constructs a `GregorianCalendar` based on the current time
        in the given time zone with the default
        Locale.Category.FORMAT FORMAT locale.

        Arguments
        - zone: the given time zone.
        """
        ...


    def __init__(self, aLocale: "Locale"):
        """
        Constructs a `GregorianCalendar` based on the current time
        in the default time zone with the given locale.

        Arguments
        - aLocale: the given locale.
        """
        ...


    def __init__(self, zone: "TimeZone", aLocale: "Locale"):
        """
        Constructs a `GregorianCalendar` based on the current time
        in the given time zone with the given locale.

        Arguments
        - zone: the given time zone.
        - aLocale: the given locale.
        """
        ...


    def __init__(self, year: int, month: int, dayOfMonth: int):
        """
        Constructs a `GregorianCalendar` with the given date set
        in the default time zone with the default locale.

        Arguments
        - year: the value used to set the `YEAR` calendar field in the calendar.
        - month: the value used to set the `MONTH` calendar field in the calendar.
        Month value is 0-based. e.g., 0 for January.
        - dayOfMonth: the value used to set the `DAY_OF_MONTH` calendar field in the calendar.
        """
        ...


    def __init__(self, year: int, month: int, dayOfMonth: int, hourOfDay: int, minute: int):
        """
        Constructs a `GregorianCalendar` with the given date
        and time set for the default time zone with the default locale.

        Arguments
        - year: the value used to set the `YEAR` calendar field in the calendar.
        - month: the value used to set the `MONTH` calendar field in the calendar.
        Month value is 0-based. e.g., 0 for January.
        - dayOfMonth: the value used to set the `DAY_OF_MONTH` calendar field in the calendar.
        - hourOfDay: the value used to set the `HOUR_OF_DAY` calendar field
        in the calendar.
        - minute: the value used to set the `MINUTE` calendar field
        in the calendar.
        """
        ...


    def __init__(self, year: int, month: int, dayOfMonth: int, hourOfDay: int, minute: int, second: int):
        """
        Constructs a GregorianCalendar with the given date
        and time set for the default time zone with the default locale.

        Arguments
        - year: the value used to set the `YEAR` calendar field in the calendar.
        - month: the value used to set the `MONTH` calendar field in the calendar.
        Month value is 0-based. e.g., 0 for January.
        - dayOfMonth: the value used to set the `DAY_OF_MONTH` calendar field in the calendar.
        - hourOfDay: the value used to set the `HOUR_OF_DAY` calendar field
        in the calendar.
        - minute: the value used to set the `MINUTE` calendar field
        in the calendar.
        - second: the value used to set the `SECOND` calendar field
        in the calendar.
        """
        ...


    def setGregorianChange(self, date: "Date") -> None:
        """
        Sets the `GregorianCalendar` change date. This is the point when the switch
        from Julian dates to Gregorian dates occurred. Default is October 15,
        1582 (Gregorian). Previous to this, dates will be in the Julian calendar.
        
        To obtain a pure Julian calendar, set the change date to
        `Date(Long.MAX_VALUE)`.  To obtain a pure Gregorian calendar,
        set the change date to `Date(Long.MIN_VALUE)`.

        Arguments
        - date: the given Gregorian cutover date.
        """
        ...


    def getGregorianChange(self) -> "Date":
        """
        Gets the Gregorian Calendar change date.  This is the point when the
        switch from Julian dates to Gregorian dates occurred. Default is
        October 15, 1582 (Gregorian). Previous to this, dates will be in the Julian
        calendar.

        Returns
        - the Gregorian cutover date for this `GregorianCalendar` object.
        """
        ...


    def isLeapYear(self, year: int) -> bool:
        """
        Determines if the given year is a leap year. Returns `True` if
        the given year is a leap year. To specify BC year numbers,
        `1 - year number` must be given. For example, year BC 4 is
        specified as -3.

        Arguments
        - year: the given year.

        Returns
        - `True` if the given year is a leap year; `False` otherwise.
        """
        ...


    def getCalendarType(self) -> str:
        """
        Returns `"gregory"` as the calendar type.

        Returns
        - `"gregory"`

        Since
        - 1.8
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this `GregorianCalendar` to the specified
        `Object`. The result is `True` if and
        only if the argument is a `GregorianCalendar` object
        that represents the same time value (millisecond offset from
        the <a href="Calendar.html#Epoch">Epoch</a>) under the same
        `Calendar` parameters and Gregorian change date as
        this object.

        Arguments
        - obj: the object to compare with.

        Returns
        - `True` if this object is equal to `obj`;
        `False` otherwise.

        See
        - Calendar.compareTo(Calendar)
        """
        ...


    def hashCode(self) -> int:
        """
        Generates the hash code for this `GregorianCalendar` object.
        """
        ...


    def add(self, field: int, amount: int) -> None:
        """
        Adds the specified (signed) amount of time to the given calendar field,
        based on the calendar's rules.
        
        *Add rule 1*. The value of `field`
        after the call minus the value of `field` before the
        call is `amount`, modulo any overflow that has occurred in
        `field`. Overflow occurs when a field value exceeds its
        range and, as a result, the next larger field is incremented or
        decremented and the field value is adjusted back into its range.
        
        *Add rule 2*. If a smaller field is expected to be
        invariant, but it is impossible for it to be equal to its
        prior value because of changes in its minimum or maximum after
        `field` is changed, then its value is adjusted to be as close
        as possible to its expected value. A smaller field represents a
        smaller unit of time. `HOUR` is a smaller field than
        `DAY_OF_MONTH`. No adjustment is made to smaller fields
        that are not expected to be invariant. The calendar system
        determines what fields are expected to be invariant.

        Arguments
        - field: the calendar field.
        - amount: the amount of date or time to be added to the field.

        Raises
        - IllegalArgumentException: if `field` is
        `ZONE_OFFSET`, `DST_OFFSET`, or unknown,
        or if any calendar fields have out-of-range values in
        non-lenient mode.
        """
        ...


    def roll(self, field: int, up: bool) -> None:
        """
        Adds or subtracts (up/down) a single unit of time on the given time
        field without changing larger fields.
        
        *Example*: Consider a `GregorianCalendar`
        originally set to December 31, 1999. Calling .roll(int,boolean) roll(Calendar.MONTH, True)
        sets the calendar to January 31, 1999.  The `YEAR` field is unchanged
        because it is a larger field than `MONTH`.

        Arguments
        - up: indicates if the value of the specified calendar field is to be
        rolled up or rolled down. Use `True` if rolling up, `False` otherwise.

        Raises
        - IllegalArgumentException: if `field` is
        `ZONE_OFFSET`, `DST_OFFSET`, or unknown,
        or if any calendar fields have out-of-range values in
        non-lenient mode.

        See
        - .set(int,int)
        """
        ...


    def roll(self, field: int, amount: int) -> None:
        """
        Adds a signed amount to the specified calendar field without changing larger fields.
        A negative roll amount means to subtract from field without changing
        larger fields. If the specified amount is 0, this method performs nothing.
        
        This method calls .complete() before adding the
        amount so that all the calendar fields are normalized. If there
        is any calendar field having an out-of-range value in non-lenient mode, then an
        `IllegalArgumentException` is thrown.
        
        
        *Example*: Consider a `GregorianCalendar`
        originally set to August 31, 1999. Calling `roll(Calendar.MONTH,
        8)` sets the calendar to April 30, <strong>1999</strong>. Using a
        `GregorianCalendar`, the `DAY_OF_MONTH` field cannot
        be 31 in the month April. `DAY_OF_MONTH` is set to the closest possible
        value, 30. The `YEAR` field maintains the value of 1999 because it
        is a larger field than `MONTH`.
        
        *Example*: Consider a `GregorianCalendar`
        originally set to Sunday June 6, 1999. Calling
        `roll(Calendar.WEEK_OF_MONTH, -1)` sets the calendar to
        Tuesday June 1, 1999, whereas calling
        `add(Calendar.WEEK_OF_MONTH, -1)` sets the calendar to
        Sunday May 30, 1999. This is because the roll rule imposes an
        additional constraint: The `MONTH` must not change when the
        `WEEK_OF_MONTH` is rolled. Taken together with add rule 1,
        the resultant date must be between Tuesday June 1 and Saturday June
        5. According to add rule 2, the `DAY_OF_WEEK`, an invariant
        when changing the `WEEK_OF_MONTH`, is set to Tuesday, the
        closest possible value to Sunday (where Sunday is the first day of the
        week).

        Arguments
        - field: the calendar field.
        - amount: the signed amount to add to `field`.

        Raises
        - IllegalArgumentException: if `field` is
        `ZONE_OFFSET`, `DST_OFFSET`, or unknown,
        or if any calendar fields have out-of-range values in
        non-lenient mode.

        See
        - .set(int,int)

        Since
        - 1.2
        """
        ...


    def getMinimum(self, field: int) -> int:
        """
        Returns the minimum value for the given calendar field of this
        `GregorianCalendar` instance. The minimum value is
        defined as the smallest value returned by the Calendar.get(int) get method for any possible time value,
        taking into consideration the current values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.

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
        `GregorianCalendar` instance. The maximum value is
        defined as the largest value returned by the Calendar.get(int) get method for any possible time value,
        taking into consideration the current values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.

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
        of this `GregorianCalendar` instance. The highest
        minimum value is defined as the largest value returned by
        .getActualMinimum(int) for any possible time value,
        taking into consideration the current values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.

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
        of this `GregorianCalendar` instance. The lowest
        maximum value is defined as the smallest value returned by
        .getActualMaximum(int) for any possible time value,
        taking into consideration the current values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.

        Arguments
        - field: the calendar field

        Returns
        - the lowest maximum value for the given calendar field.

        See
        - .getActualMaximum(int)
        """
        ...


    def getActualMinimum(self, field: int) -> int:
        """
        Returns the minimum value that this calendar field could have,
        taking into consideration the given time value and the current
        values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.
        
        For example, if the Gregorian change date is January 10,
        1970 and the date of this `GregorianCalendar` is
        January 20, 1970, the actual minimum value of the
        `DAY_OF_MONTH` field is 10 because the previous date
        of January 10, 1970 is December 27, 1996 (in the Julian
        calendar). Therefore, December 28, 1969 to January 9, 1970
        don't exist.

        Arguments
        - field: the calendar field

        Returns
        - the minimum of the given field for the time value of
        this `GregorianCalendar`

        See
        - .getActualMaximum(int)

        Since
        - 1.2
        """
        ...


    def getActualMaximum(self, field: int) -> int:
        """
        Returns the maximum value that this calendar field could have,
        taking into consideration the given time value and the current
        values of the
        Calendar.getFirstDayOfWeek() getFirstDayOfWeek,
        Calendar.getMinimalDaysInFirstWeek() getMinimalDaysInFirstWeek,
        .getGregorianChange() getGregorianChange and
        Calendar.getTimeZone() getTimeZone methods.
        For example, if the date of this instance is February 1, 2004,
        the actual maximum value of the `DAY_OF_MONTH` field
        is 29 because 2004 is a leap year, and if the date of this
        instance is February 1, 2005, it's 28.
        
        This method calculates the maximum value of Calendar.WEEK_OF_YEAR WEEK_OF_YEAR based on the Calendar.YEAR YEAR (calendar year) value, not the <a
        href="#week_year">week year</a>. Call .getWeeksInWeekYear() to get the maximum value of `WEEK_OF_YEAR` in the week year of this `GregorianCalendar`.

        Arguments
        - field: the calendar field

        Returns
        - the maximum of the given field for the time value of
        this `GregorianCalendar`

        See
        - .getActualMinimum(int)

        Since
        - 1.2
        """
        ...


    def clone(self) -> "Object":
        ...


    def getTimeZone(self) -> "TimeZone":
        ...


    def setTimeZone(self, zone: "TimeZone") -> None:
        ...


    def isWeekDateSupported(self) -> bool:
        """
        Returns `True` indicating this `GregorianCalendar`
        supports week dates.

        Returns
        - `True` (always)

        See
        - .getWeeksInWeekYear()

        Since
        - 1.7
        """
        ...


    def getWeekYear(self) -> int:
        """
        Returns the <a href="#week_year">week year</a> represented by this
        `GregorianCalendar`. The dates in the weeks between 1 and the
        maximum week number of the week year have the same week year value
        that may be one year before or after the Calendar.YEAR YEAR
        (calendar year) value.
        
        This method calls Calendar.complete() before
        calculating the week year.

        Returns
        - the week year represented by this `GregorianCalendar`.
                If the Calendar.ERA ERA value is .BC, the year is
                represented by 0 or a negative number: BC 1 is 0, BC 2
                is -1, BC 3 is -2, and so on.

        Raises
        - IllegalArgumentException: if any of the calendar fields is invalid in non-lenient mode.

        See
        - Calendar.getMinimalDaysInFirstWeek()

        Since
        - 1.7
        """
        ...


    def setWeekDate(self, weekYear: int, weekOfYear: int, dayOfWeek: int) -> None:
        """
        Sets this `GregorianCalendar` to the date given by the
        date specifiers - <a href="#week_year">`weekYear`</a>,
        `weekOfYear`, and `dayOfWeek`. `weekOfYear`
        follows the <a href="#week_and_year">`WEEK_OF_YEAR`
        numbering</a>.  The `dayOfWeek` value must be one of the
        Calendar.DAY_OF_WEEK DAY_OF_WEEK values: Calendar.SUNDAY SUNDAY to Calendar.SATURDAY SATURDAY.
        
        Note that the numeric day-of-week representation differs from
        the ISO 8601 standard, and that the `weekOfYear`
        numbering is compatible with the standard when `getFirstDayOfWeek()` is `MONDAY` and `getMinimalDaysInFirstWeek()` is 4.
        
        Unlike the `set` method, all of the calendar fields
        and the instant of time value are calculated upon return.
        
        If `weekOfYear` is out of the valid week-of-year
        range in `weekYear`, the `weekYear`
        and `weekOfYear` values are adjusted in lenient
        mode, or an `IllegalArgumentException` is thrown in
        non-lenient mode.

        Arguments
        - weekYear: the week year
        - weekOfYear: the week number based on `weekYear`
        - dayOfWeek: the day of week value: one of the constants
                           for the .DAY_OF_WEEK DAY_OF_WEEK field:
                           Calendar.SUNDAY SUNDAY, ...,
                           Calendar.SATURDAY SATURDAY.

        Raises
        - IllegalArgumentException: if any of the given date specifiers is invalid,
                   or if any of the calendar fields are inconsistent
                   with the given date specifiers in non-lenient mode

        See
        - Calendar.getMinimalDaysInFirstWeek()

        Since
        - 1.7
        """
        ...


    def getWeeksInWeekYear(self) -> int:
        """
        Returns the number of weeks in the <a href="#week_year">week year</a>
        represented by this `GregorianCalendar`.
        
        For example, if this `GregorianCalendar`'s date is
        December 31, 2008 with <a href="#iso8601_compatible_setting">the ISO
        8601 compatible setting</a>, this method will return 53 for the
        period: December 29, 2008 to January 3, 2010 while .getActualMaximum(int) getActualMaximum(WEEK_OF_YEAR) will return
        52 for the period: December 31, 2007 to December 28, 2008.

        Returns
        - the number of weeks in the week year.

        See
        - .getActualMaximum(int)

        Since
        - 1.7
        """
        ...


    def toZonedDateTime(self) -> "ZonedDateTime":
        """
        Converts this object to a `ZonedDateTime` that represents
        the same point on the time-line as this `GregorianCalendar`.
        
        Since this object supports a Julian-Gregorian cutover date and
        `ZonedDateTime` does not, it is possible that the resulting year,
        month and day will have different values.  The result will represent the
        correct date in the ISO calendar system, which will also be the same value
        for Modified Julian Days.

        Returns
        - a zoned date-time representing the same point on the time-line
         as this gregorian calendar

        Since
        - 1.8
        """
        ...


    @staticmethod
    def from(zdt: "ZonedDateTime") -> "GregorianCalendar":
        """
        Obtains an instance of `GregorianCalendar` with the default locale
        from a `ZonedDateTime` object.
        
        Since `ZonedDateTime` does not support a Julian-Gregorian cutover
        date and uses ISO calendar system, the return GregorianCalendar is a pure
        Gregorian calendar and uses ISO 8601 standard for week definitions,
        which has `MONDAY` as the Calendar.getFirstDayOfWeek()
        FirstDayOfWeek and `4` as the value of the
        Calendar.getMinimalDaysInFirstWeek() MinimalDaysInFirstWeek.
        
        `ZoneDateTime` can store points on the time-line further in the
        future and further in the past than `GregorianCalendar`. In this
        scenario, this method will throw an `IllegalArgumentException`
        exception.

        Arguments
        - zdt: the zoned date-time object to convert

        Returns
        - the gregorian calendar representing the same point on the
         time-line as the zoned date-time provided

        Raises
        - NullPointerException: if `zdt` is null
        - IllegalArgumentException: if the zoned date-time is too
        large to represent as a `GregorianCalendar`

        Since
        - 1.8
        """
        ...
