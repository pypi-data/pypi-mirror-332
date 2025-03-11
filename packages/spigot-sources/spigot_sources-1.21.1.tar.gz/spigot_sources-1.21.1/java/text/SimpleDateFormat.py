"""
Python module generated from Java source file java.text.SimpleDateFormat

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.text import *
from java.util import Calendar
from java.util import Date
from java.util import GregorianCalendar
from java.util import Locale
from java.util import SimpleTimeZone
from java.util import SortedMap
from java.util import TimeZone
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from sun.util.calendar import CalendarUtils
from sun.util.calendar import ZoneInfoFile
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import TimeZoneNameUtility
from typing import Any, Callable, Iterable, Tuple


class SimpleDateFormat(DateFormat):
    """
    `SimpleDateFormat` is a concrete class for formatting and
    parsing dates in a locale-sensitive manner. It allows for formatting
    (date &rarr; text), parsing (text &rarr; date), and normalization.
    
    
    `SimpleDateFormat` allows you to start by choosing
    any user-defined patterns for date-time formatting. However, you
    are encouraged to create a date-time formatter with either
    `getTimeInstance`, `getDateInstance`, or
    `getDateTimeInstance` in `DateFormat`. Each
    of these class methods can return a date/time formatter initialized
    with a default format pattern. You may modify the format pattern
    using the `applyPattern` methods as desired.
    For more information on using these methods, see
    DateFormat.
    
    <h2>Date and Time Patterns</h2>
    
    Date and time formats are specified by *date and time pattern*
    strings.
    Within date and time pattern strings, unquoted letters from
    `'A'` to `'Z'` and from `'a'` to
    `'z'` are interpreted as pattern letters representing the
    components of a date or time string.
    Text can be quoted using single quotes (`'`) to avoid
    interpretation.
    `"''"` represents a single quote.
    All other characters are not interpreted; they're simply copied into the
    output string during formatting or matched against the input string
    during parsing.
    
    The following pattern letters are defined (all other characters from
    `'A'` to `'Z'` and from `'a'` to
    `'z'` are reserved):
    <blockquote>
    <table class="striped">
    <caption style="display:none">Chart shows pattern letters, date/time component, presentation, and examples.</caption>
    <thead>
        <tr>
            <th scope="col" style="text-align:left">Letter
            <th scope="col" style="text-align:left">Date or Time Component
            <th scope="col" style="text-align:left">Presentation
            <th scope="col" style="text-align:left">Examples
    </thead>
    <tbody>
        <tr>
            <th scope="row">`G`
            <td>Era designator
            <td><a href="#text">Text</a>
            <td>`AD`
        <tr>
            <th scope="row">`y`
            <td>Year
            <td><a href="#year">Year</a>
            <td>`1996`; `96`
        <tr>
            <th scope="row">`Y`
            <td>Week year
            <td><a href="#year">Year</a>
            <td>`2009`; `09`
        <tr>
            <th scope="row">`M`
            <td>Month in year (context sensitive)
            <td><a href="#month">Month</a>
            <td>`July`; `Jul`; `07`
        <tr>
            <th scope="row">`L`
            <td>Month in year (standalone form)
            <td><a href="#month">Month</a>
            <td>`July`; `Jul`; `07`
        <tr>
            <th scope="row">`w`
            <td>Week in year
            <td><a href="#number">Number</a>
            <td>`27`
        <tr>
            <th scope="row">`W`
            <td>Week in month
            <td><a href="#number">Number</a>
            <td>`2`
        <tr>
            <th scope="row">`D`
            <td>Day in year
            <td><a href="#number">Number</a>
            <td>`189`
        <tr>
            <th scope="row">`d`
            <td>Day in month
            <td><a href="#number">Number</a>
            <td>`10`
        <tr>
            <th scope="row">`F`
            <td>Day of week in month
            <td><a href="#number">Number</a>
            <td>`2`
        <tr>
            <th scope="row">`E`
            <td>Day name in week
            <td><a href="#text">Text</a>
            <td>`Tuesday`; `Tue`
        <tr>
            <th scope="row">`u`
            <td>Day number of week (1 = Monday, ..., 7 = Sunday)
            <td><a href="#number">Number</a>
            <td>`1`
        <tr>
            <th scope="row">`a`
            <td>Am/pm marker
            <td><a href="#text">Text</a>
            <td>`PM`
        <tr>
            <th scope="row">`H`
            <td>Hour in day (0-23)
            <td><a href="#number">Number</a>
            <td>`0`
        <tr>
            <th scope="row">`k`
            <td>Hour in day (1-24)
            <td><a href="#number">Number</a>
            <td>`24`
        <tr>
            <th scope="row">`K`
            <td>Hour in am/pm (0-11)
            <td><a href="#number">Number</a>
            <td>`0`
        <tr>
            <th scope="row">`h`
            <td>Hour in am/pm (1-12)
            <td><a href="#number">Number</a>
            <td>`12`
        <tr>
            <th scope="row">`m`
            <td>Minute in hour
            <td><a href="#number">Number</a>
            <td>`30`
        <tr>
            <th scope="row">`s`
            <td>Second in minute
            <td><a href="#number">Number</a>
            <td>`55`
        <tr>
            <th scope="row">`S`
            <td>Millisecond
            <td><a href="#number">Number</a>
            <td>`978`
        <tr>
            <th scope="row">`z`
            <td>Time zone
            <td><a href="#timezone">General time zone</a>
            <td>`Pacific Standard Time`; `PST`; `GMT-08:00`
        <tr>
            <th scope="row">`Z`
            <td>Time zone
            <td><a href="#rfc822timezone">RFC 822 time zone</a>
            <td>`-0800`
        <tr>
            <th scope="row">`X`
            <td>Time zone
            <td><a href="#iso8601timezone">ISO 8601 time zone</a>
            <td>`-08`; `-0800`;  `-08:00`
    </tbody>
    </table>
    </blockquote>
    Pattern letters are usually repeated, as their number determines the
    exact presentation:
    
    - <strong><a id="text">Text:</a></strong>
        For formatting, if the number of pattern letters is 4 or more,
        the full form is used; otherwise a short or abbreviated form
        is used if available.
        For parsing, both forms are accepted, independent of the number
        of pattern letters.
    - <strong><a id="number">Number:</a></strong>
        For formatting, the number of pattern letters is the minimum
        number of digits, and shorter numbers are zero-padded to this amount.
        For parsing, the number of pattern letters is ignored unless
        it's needed to separate two adjacent fields.
    - <strong><a id="year">Year:</a></strong>
        If the formatter's .getCalendar() Calendar is the Gregorian
        calendar, the following rules are applied.
        
        - For formatting, if the number of pattern letters is 2, the year
            is truncated to 2 digits; otherwise it is interpreted as a
            <a href="#number">number</a>.
        - For parsing, if the number of pattern letters is more than 2,
            the year is interpreted literally, regardless of the number of
            digits. So using the pattern "MM/dd/yyyy", "01/11/12" parses to
            Jan 11, 12 A.D.
        - For parsing with the abbreviated year pattern ("y" or "yy"),
            `SimpleDateFormat` must interpret the abbreviated year
            relative to some century.  It does this by adjusting dates to be
            within 80 years before and 20 years after the time the `SimpleDateFormat`
            instance is created. For example, using a pattern of "MM/dd/yy" and a
            `SimpleDateFormat` instance created on Jan 1, 1997,  the string
            "01/11/12" would be interpreted as Jan 11, 2012 while the string "05/04/64"
            would be interpreted as May 4, 1964.
            During parsing, only strings consisting of exactly two digits, as defined by
            Character.isDigit(char), will be parsed into the default century.
            Any other numeric string, such as a one digit string, a three or more digit
            string, or a two digit string that isn't all digits (for example, "-1"), is
            interpreted literally.  So "01/02/3" or "01/02/003" are parsed, using the
            same pattern, as Jan 2, 3 AD.  Likewise, "01/02/-3" is parsed as Jan 2, 4 BC.
        
        Otherwise, calendar system specific forms are applied.
        For both formatting and parsing, if the number of pattern
        letters is 4 or more, a calendar specific Calendar.LONG long form is used. Otherwise, a calendar
        specific Calendar.SHORT short or abbreviated form
        is used.
        
        If week year `'Y'` is specified and the .getCalendar() calendar doesn't support any <a
        href="../util/GregorianCalendar.html#week_year"> week
        years</a>, the calendar year (`'y'`) is used instead. The
        support of week years can be tested with a call to DateFormat.getCalendar() getCalendar().java.util.Calendar.isWeekDateSupported()
        isWeekDateSupported().
    - <strong><a id="month">Month:</a></strong>
        If the number of pattern letters is 3 or more, the month is
        interpreted as <a href="#text">text</a>; otherwise,
        it is interpreted as a <a href="#number">number</a>.
        
        - Letter *M* produces context-sensitive month names, such as the
            embedded form of names. Letter *M* is context-sensitive in the
            sense that when it is used in the standalone pattern, for example,
            "MMMM", it gives the standalone form of a month name and when it is
            used in the pattern containing other field(s), for example, "d MMMM",
            it gives the format form of a month name. For example, January in the
            Catalan language is "de gener" in the format form while it is "gener"
            in the standalone form. In this case, "MMMM" will produce "gener" and
            the month part of the "d MMMM" will produce "de gener". If a
            `DateFormatSymbols` has been set explicitly with constructor
            .SimpleDateFormat(String,DateFormatSymbols) or method .setDateFormatSymbols(DateFormatSymbols), the month names given by
            the `DateFormatSymbols` are used.
        - Letter *L* produces the standalone form of month names.
        
        
    - <strong><a id="timezone">General time zone:</a></strong>
        Time zones are interpreted as <a href="#text">text</a> if they have
        names. For time zones representing a GMT offset value, the
        following syntax is used:
        ```
        <a id="GMTOffsetTimeZone">*GMTOffsetTimeZone:*</a>
                `GMT` *Sign* *Hours* `:` *Minutes*
        *Sign:* one of
                `+ -`
        *Hours:*
                *Digit*
                *Digit* *Digit*
        *Minutes:*
                *Digit* *Digit*
        *Digit:* one of
                `0 1 2 3 4 5 6 7 8 9````
        *Hours* must be between 0 and 23, and *Minutes* must be between
        00 and 59. The format is locale independent and digits must be taken
        from the Basic Latin block of the Unicode standard.
        For parsing, <a href="#rfc822timezone">RFC 822 time zones</a> are also
        accepted.
    - <strong><a id="rfc822timezone">RFC 822 time zone:</a></strong>
        For formatting, the RFC 822 4-digit time zone format is used:
    
        ```
        *RFC822TimeZone:*
                *Sign* *TwoDigitHours* *Minutes*
        *TwoDigitHours:*
                *Digit Digit*```
        *TwoDigitHours* must be between 00 and 23. Other definitions
        are as for <a href="#timezone">general time zones</a>.
    
        For parsing, <a href="#timezone">general time zones</a> are also
        accepted.
    - <strong><a id="iso8601timezone">ISO 8601 Time zone:</a></strong>
        The number of pattern letters designates the format for both formatting
        and parsing as follows:
        ```
        *ISO8601TimeZone:*
                *OneLetterISO8601TimeZone*
                *TwoLetterISO8601TimeZone*
                *ThreeLetterISO8601TimeZone*
        *OneLetterISO8601TimeZone:*
                *Sign* *TwoDigitHours*
                `Z`
        *TwoLetterISO8601TimeZone:*
                *Sign* *TwoDigitHours* *Minutes*
                `Z`
        *ThreeLetterISO8601TimeZone:*
                *Sign* *TwoDigitHours* `:` *Minutes*
                `Z````
        Other definitions are as for <a href="#timezone">general time zones</a> or
        <a href="#rfc822timezone">RFC 822 time zones</a>.
    
        For formatting, if the offset value from GMT is 0, `"Z"` is
        produced. If the number of pattern letters is 1, any fraction of an hour
        is ignored. For example, if the pattern is `"X"` and the time zone is
        `"GMT+05:30"`, `"+05"` is produced.
    
        For parsing, `"Z"` is parsed as the UTC time zone designator.
        <a href="#timezone">General time zones</a> are *not* accepted.
    
        If the number of pattern letters is 4 or more, IllegalArgumentException is thrown when constructing a `SimpleDateFormat` or .applyPattern(String) applying a
        pattern.
    
    `SimpleDateFormat` also supports *localized date and time
    pattern* strings. In these strings, the pattern letters described above
    may be replaced with other, locale dependent, pattern letters.
    `SimpleDateFormat` does not deal with the localization of text
    other than the pattern letters; that's up to the client of the class.
    
    <h3>Examples</h3>
    
    The following examples show how date and time patterns are interpreted in
    the U.S. locale. The given date and time are 2001-07-04 12:08:56 local time
    in the U.S. Pacific Time time zone.
    <blockquote>
    <table class="striped">
    <caption style="display:none">Examples of date and time patterns interpreted in the U.S. locale</caption>
    <thead>
        <tr>
            <th scope="col" style="text-align:left">Date and Time Pattern
            <th scope="col" style="text-align:left">Result
    </thead>
    <tbody>
        <tr>
            <th scope="row">`"yyyy.MM.dd G 'at' HH:mm:ss z"`
            <td>`2001.07.04 AD at 12:08:56 PDT`
        <tr>
            <th scope="row">`"EEE, MMM d, ''yy"`
            <td>`Wed, Jul 4, '01`
        <tr>
            <th scope="row">`"h:mm a"`
            <td>`12:08 PM`
        <tr>
            <th scope="row">`"hh 'o''clock' a, zzzz"`
            <td>`12 o'clock PM, Pacific Daylight Time`
        <tr>
            <th scope="row">`"K:mm a, z"`
            <td>`0:08 PM, PDT`
        <tr>
            <th scope="row">`"yyyyy.MMMMM.dd GGG hh:mm aaa"`
            <td>`02001.July.04 AD 12:08 PM`
        <tr>
            <th scope="row">`"EEE, d MMM yyyy HH:mm:ss Z"`
            <td>`Wed, 4 Jul 2001 12:08:56 -0700`
        <tr>
            <th scope="row">`"yyMMddHHmmssZ"`
            <td>`010704120856-0700`
        <tr>
            <th scope="row">`"yyyy-MM-dd'T'HH:mm:ss.SSSZ"`
            <td>`2001-07-04T12:08:56.235-0700`
        <tr>
            <th scope="row">`"yyyy-MM-dd'T'HH:mm:ss.SSSXXX"`
            <td>`2001-07-04T12:08:56.235-07:00`
        <tr>
            <th scope="row">`"YYYY-'W'ww-u"`
            <td>`2001-W27-3`
    </tbody>
    </table>
    </blockquote>
    
    <h3><a id="synchronization">Synchronization</a></h3>
    
    
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
    """

    def __init__(self):
        """
        Constructs a `SimpleDateFormat` using the default pattern and
        date format symbols for the default
        java.util.Locale.Category.FORMAT FORMAT locale.
        **Note:** This constructor may not support all locales.
        For full coverage, use the factory methods in the DateFormat
        class.
        """
        ...


    def __init__(self, pattern: str):
        """
        Constructs a `SimpleDateFormat` using the given pattern and
        the default date format symbols for the default
        java.util.Locale.Category.FORMAT FORMAT locale.
        **Note:** This constructor may not support all locales.
        For full coverage, use the factory methods in the DateFormat
        class.
        This is equivalent to calling
        .SimpleDateFormat(String, Locale)
            SimpleDateFormat(pattern, Locale.getDefault(Locale.Category.FORMAT)).

        Arguments
        - pattern: the pattern describing the date and time format

        Raises
        - NullPointerException: if the given pattern is null
        - IllegalArgumentException: if the given pattern is invalid

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    def __init__(self, pattern: str, locale: "Locale"):
        """
        Constructs a `SimpleDateFormat` using the given pattern and
        the default date format symbols for the given locale.
        **Note:** This constructor may not support all locales.
        For full coverage, use the factory methods in the DateFormat
        class.

        Arguments
        - pattern: the pattern describing the date and time format
        - locale: the locale whose date format symbols should be used

        Raises
        - NullPointerException: if the given pattern or locale is null
        - IllegalArgumentException: if the given pattern is invalid
        """
        ...


    def __init__(self, pattern: str, formatSymbols: "DateFormatSymbols"):
        """
        Constructs a `SimpleDateFormat` using the given pattern and
        date format symbols.

        Arguments
        - pattern: the pattern describing the date and time format
        - formatSymbols: the date format symbols to be used for formatting

        Raises
        - NullPointerException: if the given pattern or formatSymbols is null
        - IllegalArgumentException: if the given pattern is invalid
        """
        ...


    def set2DigitYearStart(self, startDate: "Date") -> None:
        """
        Sets the 100-year period 2-digit years will be interpreted as being in
        to begin on the date the user specifies.

        Arguments
        - startDate: During parsing, two digit years will be placed in the range
        `startDate` to `startDate + 100 years`.

        Raises
        - NullPointerException: if `startDate` is `null`.

        See
        - .get2DigitYearStart

        Since
        - 1.2
        """
        ...


    def get2DigitYearStart(self) -> "Date":
        """
        Returns the beginning date of the 100-year period 2-digit years are interpreted
        as being within.

        Returns
        - the start of the 100-year period into which two digit years are
        parsed

        See
        - .set2DigitYearStart

        Since
        - 1.2
        """
        ...


    def format(self, date: "Date", toAppendTo: "StringBuffer", pos: "FieldPosition") -> "StringBuffer":
        """
        Formats the given `Date` into a date/time string and appends
        the result to the given `StringBuffer`.

        Arguments
        - date: the date-time value to be formatted into a date-time string.
        - toAppendTo: where the new date-time text is to be appended.
        - pos: keeps track on the position of the field within
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
        - the formatted date-time string.

        Raises
        - NullPointerException: if any of the parameters is `null`.
        """
        ...


    def formatToCharacterIterator(self, obj: "Object") -> "AttributedCharacterIterator":
        """
        Formats an Object producing an `AttributedCharacterIterator`.
        You can use the returned `AttributedCharacterIterator`
        to build the resulting String, as well as to determine information
        about the resulting String.
        
        Each attribute key of the AttributedCharacterIterator will be of type
        `DateFormat.Field`, with the corresponding attribute value
        being the same as the attribute key.

        Arguments
        - obj: The object to format

        Returns
        - AttributedCharacterIterator describing the formatted value.

        Raises
        - NullPointerException: if obj is null.
        - IllegalArgumentException: if the Format cannot format the
                   given object, or if the Format's pattern string is invalid.

        Since
        - 1.4
        """
        ...


    def parse(self, text: str, pos: "ParsePosition") -> "Date":
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
        
        This parsing operation uses the DateFormat.calendar
        calendar to produce a `Date`. All of the `calendar`'s date-time fields are Calendar.clear()
        cleared before parsing, and the `calendar`'s default
        values of the date-time fields are used for any missing
        date-time information. For example, the year value of the
        parsed `Date` is 1970 with GregorianCalendar if
        no year value is given from the parsing operation.  The `TimeZone` value may be overwritten, depending on the given
        pattern and the time zone value in `text`. Any `TimeZone` value that has previously been set by a call to
        .setTimeZone(java.util.TimeZone) setTimeZone may need
        to be restored for further operations.

        Arguments
        - text: A `String`, part of which should be parsed.
        - pos: A `ParsePosition` object with index and error
                     index information as described above.

        Returns
        - A `Date` parsed from the string. In case of
                error, returns null.

        Raises
        - NullPointerException: if `text` or `pos` is null.
        """
        ...


    def toPattern(self) -> str:
        """
        Returns a pattern string describing this date format.

        Returns
        - a pattern string describing this date format.
        """
        ...


    def toLocalizedPattern(self) -> str:
        """
        Returns a localized pattern string describing this date format.

        Returns
        - a localized pattern string describing this date format.
        """
        ...


    def applyPattern(self, pattern: str) -> None:
        """
        Applies the given pattern string to this date format.

        Arguments
        - pattern: the new date and time pattern for this date format

        Raises
        - NullPointerException: if the given pattern is null
        - IllegalArgumentException: if the given pattern is invalid
        """
        ...


    def applyLocalizedPattern(self, pattern: str) -> None:
        """
        Applies the given localized pattern string to this date format.

        Arguments
        - pattern: a String to be mapped to the new date and time format
               pattern for this format

        Raises
        - NullPointerException: if the given pattern is null
        - IllegalArgumentException: if the given pattern is invalid
        """
        ...


    def getDateFormatSymbols(self) -> "DateFormatSymbols":
        """
        Gets a copy of the date and time format symbols of this date format.

        Returns
        - the date and time format symbols of this date format

        See
        - .setDateFormatSymbols
        """
        ...


    def setDateFormatSymbols(self, newFormatSymbols: "DateFormatSymbols") -> None:
        """
        Sets the date and time format symbols of this date format.

        Arguments
        - newFormatSymbols: the new date and time format symbols

        Raises
        - NullPointerException: if the given newFormatSymbols is null

        See
        - .getDateFormatSymbols
        """
        ...


    def clone(self) -> "Object":
        """
        Creates a copy of this `SimpleDateFormat`. This also
        clones the format's date format symbols.

        Returns
        - a clone of this `SimpleDateFormat`
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this `SimpleDateFormat` object.

        Returns
        - the hash code value for this `SimpleDateFormat` object.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares the given object with this `SimpleDateFormat` for
        equality.

        Returns
        - True if the given object is equal to this
        `SimpleDateFormat`
        """
        ...
