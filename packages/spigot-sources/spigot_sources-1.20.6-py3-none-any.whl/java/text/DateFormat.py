"""
Python module generated from Java source file java.text.DateFormat

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import InvalidObjectException
from java.text import *
from java.text.spi import DateFormatProvider
from java.util import Calendar
from java.util import Date
from java.util import GregorianCalendar
from java.util import Locale
from java.util import MissingResourceException
from java.util import ResourceBundle
from java.util import TimeZone
from java.util.spi import LocaleServiceProvider
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import LocaleServiceProviderPool
from typing import Any, Callable, Iterable, Tuple


class DateFormat(Format):
    """
    `DateFormat` is an abstract class for date/time formatting subclasses which
    formats and parses dates or time in a language-independent manner.
    The date/time formatting subclass, such as SimpleDateFormat, allows for
    formatting (i.e., date &rarr; text), parsing (text &rarr; date), and
    normalization.  The date is represented as a `Date` object or
    as the milliseconds since January 1, 1970, 00:00:00 GMT.
    
    `DateFormat` provides many class methods for obtaining default date/time
    formatters based on the default or a given locale and a number of formatting
    styles. The formatting styles include .FULL, .LONG, .MEDIUM, and .SHORT. More
    detail and examples of using these styles are provided in the method
    descriptions.
    
    `DateFormat` helps you to format and parse dates for any locale.
    Your code can be completely independent of the locale conventions for
    months, days of the week, or even the calendar format: lunar vs. solar.
    
    To format a date for the current Locale, use one of the
    static factory methods:
    <blockquote>
    ````myString = DateFormat.getDateInstance().format(myDate);````
    </blockquote>
    If you are formatting multiple dates, it is
    more efficient to get the format and use it multiple times so that
    the system doesn't have to fetch the information about the local
    language and country conventions multiple times.
    <blockquote>
    ````DateFormat df = DateFormat.getDateInstance();
    for (int i = 0; i < myDate.length; ++i) {
        output.println(df.format(myDate[i]) + "; ");`
    }```
    </blockquote>
    To format a date for a different Locale, specify it in the
    call to .getDateInstance(int, Locale) getDateInstance().
    <blockquote>
    ````DateFormat df = DateFormat.getDateInstance(DateFormat.LONG, Locale.FRANCE);````
    </blockquote>
    
    If the specified locale contains "ca" (calendar), "rg" (region override),
    and/or "tz" (timezone) <a href="../util/Locale.html#def_locale_extension">Unicode
    extensions</a>, the calendar, the country and/or the time zone for formatting
    are overridden. If both "ca" and "rg" are specified, the calendar from the "ca"
    extension supersedes the implicit one from the "rg" extension.
    
    You can use a DateFormat to parse also.
    <blockquote>
    ````myDate = df.parse(myString);````
    </blockquote>
    Use `getDateInstance` to get the normal date format for that country.
    There are other static factory methods available.
    Use `getTimeInstance` to get the time format for that country.
    Use `getDateTimeInstance` to get a date and time format. You can pass in
    different options to these factory methods to control the length of the
    result; from .SHORT to .MEDIUM to .LONG to .FULL. The exact result depends
    on the locale, but generally:
    - .SHORT is completely numeric, such as `12.13.52` or `3:30pm`
    - .MEDIUM is longer, such as `Jan 12, 1952`
    - .LONG is longer, such as `January 12, 1952` or `3:30:32pm`
    - .FULL is pretty completely specified, such as
    `Tuesday, April 12, 1952 AD or 3:30:42pm PST`.
    
    
    You can also set the time zone on the format if you wish.
    If you want even more control over the format or parsing,
    (or want to give your users more control),
    you can try casting the `DateFormat` you get from the factory methods
    to a SimpleDateFormat. This will work for the majority
    of countries; just remember to put it in a `try` block in case you
    encounter an unusual one.
    
    You can also use forms of the parse and format methods with
    ParsePosition and FieldPosition to
    allow you to
    - progressively parse through pieces of a string.
    - align any particular field, or find out where it is for selection
    on the screen.
    
    
    <h2><a id="synchronization">Synchronization</a></h2>
    
    
    Date formats are not synchronized.
    It is recommended to create separate format instances for each thread.
    If multiple threads access a format concurrently, it must be synchronized
    externally.

    Author(s)
    - Mark Davis, Chen-Lieh Huang, Alan Liu

    See
    - java.time.format.DateTimeFormatter

    Since
    - 1.1

    Unknown Tags
    - Consider using java.time.format.DateTimeFormatter as an
    immutable and thread-safe alternative.
    - - The .format(Date, StringBuffer, FieldPosition) and
    .parse(String, ParsePosition) methods may throw
    `NullPointerException`, if any of their parameter is `null`.
    The subclass may provide its own implementation and specification about
    `NullPointerException`.
    - The .setCalendar(Calendar), .setNumberFormat(NumberFormat) and .setTimeZone(TimeZone) methods
    do not throw `NullPointerException` when their parameter is
    `null`, but any subsequent operations on the same instance may throw
    `NullPointerException`.
    - The .getCalendar(), .getNumberFormat() and
    getTimeZone() methods may return `null`, if the respective
    values of this instance is set to `null` through the corresponding
    setter methods. For Example: .getTimeZone() may return `null`,
    if the `TimeZone` value of this instance is set as
    .setTimeZone(java.util.TimeZone) setTimeZone(null).
    """

    ERA_FIELD = 0
    """
    Useful constant for ERA field alignment.
    Used in FieldPosition of date/time formatting.
    """
    YEAR_FIELD = 1
    """
    Useful constant for YEAR field alignment.
    Used in FieldPosition of date/time formatting.
    """
    MONTH_FIELD = 2
    """
    Useful constant for MONTH field alignment.
    Used in FieldPosition of date/time formatting.
    """
    DATE_FIELD = 3
    """
    Useful constant for DATE field alignment.
    Used in FieldPosition of date/time formatting.
    """
    HOUR_OF_DAY1_FIELD = 4
    """
    Useful constant for one-based HOUR_OF_DAY field alignment.
    Used in FieldPosition of date/time formatting.
    HOUR_OF_DAY1_FIELD is used for the one-based 24-hour clock.
    For example, 23:59 + 01:00 results in 24:59.
    """
    HOUR_OF_DAY0_FIELD = 5
    """
    Useful constant for zero-based HOUR_OF_DAY field alignment.
    Used in FieldPosition of date/time formatting.
    HOUR_OF_DAY0_FIELD is used for the zero-based 24-hour clock.
    For example, 23:59 + 01:00 results in 00:59.
    """
    MINUTE_FIELD = 6
    """
    Useful constant for MINUTE field alignment.
    Used in FieldPosition of date/time formatting.
    """
    SECOND_FIELD = 7
    """
    Useful constant for SECOND field alignment.
    Used in FieldPosition of date/time formatting.
    """
    MILLISECOND_FIELD = 8
    """
    Useful constant for MILLISECOND field alignment.
    Used in FieldPosition of date/time formatting.
    """
    DAY_OF_WEEK_FIELD = 9
    """
    Useful constant for DAY_OF_WEEK field alignment.
    Used in FieldPosition of date/time formatting.
    """
    DAY_OF_YEAR_FIELD = 10
    """
    Useful constant for DAY_OF_YEAR field alignment.
    Used in FieldPosition of date/time formatting.
    """
    DAY_OF_WEEK_IN_MONTH_FIELD = 11
    """
    Useful constant for DAY_OF_WEEK_IN_MONTH field alignment.
    Used in FieldPosition of date/time formatting.
    """
    WEEK_OF_YEAR_FIELD = 12
    """
    Useful constant for WEEK_OF_YEAR field alignment.
    Used in FieldPosition of date/time formatting.
    """
    WEEK_OF_MONTH_FIELD = 13
    """
    Useful constant for WEEK_OF_MONTH field alignment.
    Used in FieldPosition of date/time formatting.
    """
    AM_PM_FIELD = 14
    """
    Useful constant for AM_PM field alignment.
    Used in FieldPosition of date/time formatting.
    """
    HOUR1_FIELD = 15
    """
    Useful constant for one-based HOUR field alignment.
    Used in FieldPosition of date/time formatting.
    HOUR1_FIELD is used for the one-based 12-hour clock.
    For example, 11:30 PM + 1 hour results in 12:30 AM.
    """
    HOUR0_FIELD = 16
    """
    Useful constant for zero-based HOUR field alignment.
    Used in FieldPosition of date/time formatting.
    HOUR0_FIELD is used for the zero-based 12-hour clock.
    For example, 11:30 PM + 1 hour results in 00:30 AM.
    """
    TIMEZONE_FIELD = 17
    """
    Useful constant for TIMEZONE field alignment.
    Used in FieldPosition of date/time formatting.
    """
    FULL = 0
    """
    Constant for full style pattern.
    """
    LONG = 1
    """
    Constant for long style pattern.
    """
    MEDIUM = 2
    """
    Constant for medium style pattern.
    """
    SHORT = 3
    """
    Constant for short style pattern.
    """
    DEFAULT = MEDIUM
    """
    Constant for default style pattern.  Its value is MEDIUM.
    """


    def format(self, obj: "Object", toAppendTo: "StringBuffer", fieldPosition: "FieldPosition") -> "StringBuffer":
        """
        Formats the given `Object` into a date-time string. The formatted
        string is appended to the given `StringBuffer`.

        Arguments
        - obj: Must be a `Date` or a `Number` representing a
        millisecond offset from the <a href="../util/Calendar.html#Epoch">Epoch</a>.
        - toAppendTo: The string buffer for the returning date-time string.
        - fieldPosition: keeps track on the position of the field within
        the returned string. For example, given a date-time text
        `"1996.07.10 AD at 15:08:56 PDT"`, if the given `fieldPosition`
        is DateFormat.YEAR_FIELD, the begin index and end index of
        `fieldPosition` will be set to 0 and 4, respectively.
        Notice that if the same date-time field appears more than once in a
        pattern, the `fieldPosition` will be set for the first occurrence
        of that date-time field. For instance, formatting a `Date` to the
        date-time string `"1 PM PDT (Pacific Daylight Time)"` using the
        pattern `"h a z (zzzz)"` and the alignment field
        DateFormat.TIMEZONE_FIELD, the begin index and end index of
        `fieldPosition` will be set to 5 and 8, respectively, for the
        first occurrence of the timezone pattern character `'z'`.

        Returns
        - the string buffer passed in as `toAppendTo`,
                with formatted text appended.

        Raises
        - IllegalArgumentException: if the `Format` cannot format
                   the given `obj`.

        See
        - java.text.Format
        """
        ...


    def format(self, date: "Date", toAppendTo: "StringBuffer", fieldPosition: "FieldPosition") -> "StringBuffer":
        """
        Formats a Date into a date-time string. The formatted
        string is appended to the given `StringBuffer`.

        Arguments
        - date: a Date to be formatted into a date-time string.
        - toAppendTo: the string buffer for the returning date-time string.
        - fieldPosition: keeps track on the position of the field within
        the returned string. For example, given a date-time text
        `"1996.07.10 AD at 15:08:56 PDT"`, if the given `fieldPosition`
        is DateFormat.YEAR_FIELD, the begin index and end index of
        `fieldPosition` will be set to 0 and 4, respectively.
        Notice that if the same date-time field appears more than once in a
        pattern, the `fieldPosition` will be set for the first occurrence
        of that date-time field. For instance, formatting a `Date` to the
        date-time string `"1 PM PDT (Pacific Daylight Time)"` using the
        pattern `"h a z (zzzz)"` and the alignment field
        DateFormat.TIMEZONE_FIELD, the begin index and end index of
        `fieldPosition` will be set to 5 and 8, respectively, for the
        first occurrence of the timezone pattern character `'z'`.

        Returns
        - the string buffer passed in as `toAppendTo`, with formatted
        text appended.
        """
        ...


    def format(self, date: "Date") -> str:
        """
        Formats a Date into a date-time string.

        Arguments
        - date: the time value to be formatted into a date-time string.

        Returns
        - the formatted date-time string.
        """
        ...


    def parse(self, source: str) -> "Date":
        """
        Parses text from the beginning of the given string to produce a date.
        The method may not use the entire text of the given string.
        
        See the .parse(String, ParsePosition) method for more information
        on date parsing.

        Arguments
        - source: A `String` whose beginning should be parsed.

        Returns
        - A `Date` parsed from the string.

        Raises
        - ParseException: if the beginning of the specified string
                   cannot be parsed.
        """
        ...


    def parse(self, source: str, pos: "ParsePosition") -> "Date":
        """
        Parse a date/time string according to the given parse position.  For
        example, a time text `"07/10/96 4:5 PM, PDT"` will be parsed into a `Date`
        that is equivalent to `Date(837039900000L)`.
        
         By default, parsing is lenient: If the input is not in the form used
        by this object's format method but can still be parsed as a date, then
        the parse succeeds.  Clients may insist on strict adherence to the
        format by calling .setLenient(boolean) setLenient(False).
        
        This parsing operation uses the .calendar to produce
        a `Date`. As a result, the `calendar`'s date-time
        fields and the `TimeZone` value may have been
        overwritten, depending on subclass implementations. Any `TimeZone` value that has previously been set by a call to
        .setTimeZone(java.util.TimeZone) setTimeZone may need
        to be restored for further operations.

        Arguments
        - source: The date/time string to be parsed
        - pos: On input, the position at which to start parsing; on
                     output, the position at which parsing terminated, or the
                     start position if the parse failed.

        Returns
        - A `Date`, or `null` if the input could not be parsed
        """
        ...


    def parseObject(self, source: str, pos: "ParsePosition") -> "Object":
        """
        Parses text from a string to produce a `Date`.
        
        The method attempts to parse text starting at the index given by
        `pos`.
        If parsing succeeds, then the index of `pos` is updated
        to the index after the last character used (parsing does not necessarily
        use all characters up to the end of the string), and the parsed
        date is returned. The updated `pos` can be used to
        indicate the starting point for the next call to this method.
        If an error occurs, then the index of `pos` is not
        changed, the error index of `pos` is set to the index of
        the character where the error occurred, and null is returned.
        
        See the .parse(String, ParsePosition) method for more information
        on date parsing.

        Arguments
        - source: A `String`, part of which should be parsed.
        - pos: A `ParsePosition` object with index and error
                   index information as described above.

        Returns
        - A `Date` parsed from the string. In case of
                error, returns null.

        Raises
        - NullPointerException: if `source` or `pos` is null.
        """
        ...


    @staticmethod
    def getTimeInstance() -> "DateFormat":
        """
        Gets the time formatter with the default formatting style
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getTimeInstance(int, Locale) getTimeInstance(DEFAULT,
            Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - a time formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getTimeInstance(style: int) -> "DateFormat":
        """
        Gets the time formatter with the given formatting style
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getTimeInstance(int, Locale) getTimeInstance(style,
            Locale.getDefault(Locale.Category.FORMAT)).

        Arguments
        - style: the given formatting style. For example,
        SHORT for "h:mm a" in the US locale.

        Returns
        - a time formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getTimeInstance(style: int, aLocale: "Locale") -> "DateFormat":
        """
        Gets the time formatter with the given formatting style
        for the given locale.

        Arguments
        - style: the given formatting style. For example,
        SHORT for "h:mm a" in the US locale.
        - aLocale: the given locale.

        Returns
        - a time formatter.
        """
        ...


    @staticmethod
    def getDateInstance() -> "DateFormat":
        """
        Gets the date formatter with the default formatting style
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getDateInstance(int, Locale) getDateInstance(DEFAULT,
            Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - a date formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getDateInstance(style: int) -> "DateFormat":
        """
        Gets the date formatter with the given formatting style
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getDateInstance(int, Locale) getDateInstance(style,
            Locale.getDefault(Locale.Category.FORMAT)).

        Arguments
        - style: the given formatting style. For example,
        SHORT for "M/d/yy" in the US locale.

        Returns
        - a date formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getDateInstance(style: int, aLocale: "Locale") -> "DateFormat":
        """
        Gets the date formatter with the given formatting style
        for the given locale.

        Arguments
        - style: the given formatting style. For example,
        SHORT for "M/d/yy" in the US locale.
        - aLocale: the given locale.

        Returns
        - a date formatter.
        """
        ...


    @staticmethod
    def getDateTimeInstance() -> "DateFormat":
        """
        Gets the date/time formatter with the default formatting style
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getDateTimeInstance(int, int, Locale) getDateTimeInstance(DEFAULT,
            DEFAULT, Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - a date/time formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getDateTimeInstance(dateStyle: int, timeStyle: int) -> "DateFormat":
        """
        Gets the date/time formatter with the given date and time
        formatting styles for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getDateTimeInstance(int, int, Locale) getDateTimeInstance(dateStyle,
            timeStyle, Locale.getDefault(Locale.Category.FORMAT)).

        Arguments
        - dateStyle: the given date formatting style. For example,
        SHORT for "M/d/yy" in the US locale.
        - timeStyle: the given time formatting style. For example,
        SHORT for "h:mm a" in the US locale.

        Returns
        - a date/time formatter.

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getDateTimeInstance(dateStyle: int, timeStyle: int, aLocale: "Locale") -> "DateFormat":
        """
        Gets the date/time formatter with the given formatting styles
        for the given locale.

        Arguments
        - dateStyle: the given date formatting style.
        - timeStyle: the given time formatting style.
        - aLocale: the given locale.

        Returns
        - a date/time formatter.
        """
        ...


    @staticmethod
    def getInstance() -> "DateFormat":
        """
        Get a default date/time formatter that uses the SHORT style for both the
        date and the time.

        Returns
        - a date/time formatter
        """
        ...


    @staticmethod
    def getAvailableLocales() -> list["Locale"]:
        """
        Returns an array of all locales for which the
        `get*Instance` methods of this class can return
        localized instances.
        The returned array represents the union of locales supported by the Java
        runtime and by installed
        java.text.spi.DateFormatProvider DateFormatProvider implementations.
        It must contain at least a `Locale` instance equal to
        java.util.Locale.US Locale.US.

        Returns
        - An array of locales for which localized
                `DateFormat` instances are available.
        """
        ...


    def setCalendar(self, newCalendar: "Calendar") -> None:
        """
        Set the calendar to be used by this date format.  Initially, the default
        calendar for the specified or default locale is used.
        
        Any java.util.TimeZone TimeZone and .isLenient() leniency values that have previously been set are
        overwritten by `newCalendar`'s values.

        Arguments
        - newCalendar: the new `Calendar` to be used by the date format
        """
        ...


    def getCalendar(self) -> "Calendar":
        """
        Gets the calendar associated with this date/time formatter.

        Returns
        - the calendar associated with this date/time formatter.
        """
        ...


    def setNumberFormat(self, newNumberFormat: "NumberFormat") -> None:
        """
        Allows you to set the number formatter.

        Arguments
        - newNumberFormat: the given new NumberFormat.
        """
        ...


    def getNumberFormat(self) -> "NumberFormat":
        """
        Gets the number formatter which this date/time formatter uses to
        format and parse a time.

        Returns
        - the number formatter which this date/time formatter uses.
        """
        ...


    def setTimeZone(self, zone: "TimeZone") -> None:
        """
        Sets the time zone for the calendar of this `DateFormat` object.
        This method is equivalent to the following call.
        <blockquote>````getCalendar().setTimeZone(zone)````</blockquote>
        
        The `TimeZone` set by this method is overwritten by a
        .setCalendar(java.util.Calendar) setCalendar call.
        
        The `TimeZone` set by this method may be overwritten as
        a result of a call to the parse method.

        Arguments
        - zone: the given new time zone.
        """
        ...


    def getTimeZone(self) -> "TimeZone":
        """
        Gets the time zone.
        This method is equivalent to the following call.
        <blockquote>````getCalendar().getTimeZone()````</blockquote>

        Returns
        - the time zone associated with the calendar of DateFormat.
        """
        ...


    def setLenient(self, lenient: bool) -> None:
        """
        Specify whether or not date/time parsing is to be lenient.  With
        lenient parsing, the parser may use heuristics to interpret inputs that
        do not precisely match this object's format.  With strict parsing,
        inputs must match this object's format.
        
        This method is equivalent to the following call.
        <blockquote>````getCalendar().setLenient(lenient)````</blockquote>
        
        This leniency value is overwritten by a call to .setCalendar(java.util.Calendar) setCalendar().

        Arguments
        - lenient: when `True`, parsing is lenient

        See
        - java.util.Calendar.setLenient(boolean)
        """
        ...


    def isLenient(self) -> bool:
        """
        Tell whether date/time parsing is to be lenient.
        This method is equivalent to the following call.
        <blockquote>````getCalendar().isLenient()````</blockquote>

        Returns
        - `True` if the .calendar is lenient;
                `False` otherwise.

        See
        - java.util.Calendar.isLenient()
        """
        ...


    def hashCode(self) -> int:
        """
        Overrides hashCode
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Overrides equals
        """
        ...


    def clone(self) -> "Object":
        """
        Overrides Cloneable
        """
        ...


    class Field(Field):
        """
        Defines constants that are used as attribute keys in the
        `AttributedCharacterIterator` returned
        from `DateFormat.formatToCharacterIterator` and as
        field identifiers in `FieldPosition`.
        
        The class also provides two methods to map
        between its constants and the corresponding Calendar constants.

        See
        - java.util.Calendar

        Since
        - 1.4
        """

        ERA = Field("era", Calendar.ERA)
        """
        Constant identifying the era field.
        """
        YEAR = Field("year", Calendar.YEAR)
        """
        Constant identifying the year field.
        """
        MONTH = Field("month", Calendar.MONTH)
        """
        Constant identifying the month field.
        """
        DAY_OF_MONTH = Field("day of month", Calendar.DAY_OF_MONTH)
        """
        Constant identifying the day of month field.
        """
        HOUR_OF_DAY1 = Field("hour of day 1", -1)
        """
        Constant identifying the hour of day field, where the legal values
        are 1 to 24.
        """
        HOUR_OF_DAY0 = Field("hour of day", Calendar.HOUR_OF_DAY)
        """
        Constant identifying the hour of day field, where the legal values
        are 0 to 23.
        """
        MINUTE = Field("minute", Calendar.MINUTE)
        """
        Constant identifying the minute field.
        """
        SECOND = Field("second", Calendar.SECOND)
        """
        Constant identifying the second field.
        """
        MILLISECOND = Field("millisecond", Calendar.MILLISECOND)
        """
        Constant identifying the millisecond field.
        """
        DAY_OF_WEEK = Field("day of week", Calendar.DAY_OF_WEEK)
        """
        Constant identifying the day of week field.
        """
        DAY_OF_YEAR = Field("day of year", Calendar.DAY_OF_YEAR)
        """
        Constant identifying the day of year field.
        """
        DAY_OF_WEEK_IN_MONTH = Field("day of week in month", Calendar.DAY_OF_WEEK_IN_MONTH)
        """
        Constant identifying the day of week field.
        """
        WEEK_OF_YEAR = Field("week of year", Calendar.WEEK_OF_YEAR)
        """
        Constant identifying the week of year field.
        """
        WEEK_OF_MONTH = Field("week of month", Calendar.WEEK_OF_MONTH)
        """
        Constant identifying the week of month field.
        """
        AM_PM = Field("am pm", Calendar.AM_PM)
        """
        Constant identifying the time of day indicator
        (e.g. "a.m." or "p.m.") field.
        """
        HOUR1 = Field("hour 1", -1)
        """
        Constant identifying the hour field, where the legal values are
        1 to 12.
        """
        HOUR0 = Field("hour", Calendar.HOUR)
        """
        Constant identifying the hour field, where the legal values are
        0 to 11.
        """
        TIME_ZONE = Field("time zone", -1)
        """
        Constant identifying the time zone field.
        """


        @staticmethod
        def ofCalendarField(calendarField: int) -> "Field":
            """
            Returns the `Field` constant that corresponds to
            the `Calendar` constant `calendarField`.
            If there is no direct mapping between the `Calendar`
            constant and a `Field`, null is returned.

            Arguments
            - calendarField: Calendar field constant

            Returns
            - Field instance representing calendarField.

            Raises
            - IllegalArgumentException: if `calendarField` is
                    not the value of a `Calendar` field constant.

            See
            - java.util.Calendar
            """
            ...


        def getCalendarField(self) -> int:
            """
            Returns the `Calendar` field associated with this
            attribute. For example, if this represents the hours field of
            a `Calendar`, this would return
            `Calendar.HOUR`. If there is no corresponding
            `Calendar` constant, this will return -1.

            Returns
            - Calendar constant for this field

            See
            - java.util.Calendar
            """
            ...
