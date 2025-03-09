"""
Python module generated from Java source file java.util.TimeZone

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Serializable
from java.time import ZoneId
from java.util import *
from jdk.internal.util import StaticProperty
from sun.security.action import GetPropertyAction
from sun.util.calendar import ZoneInfo
from sun.util.calendar import ZoneInfoFile
from sun.util.locale.provider import TimeZoneNameUtility
from typing import Any, Callable, Iterable, Tuple


class TimeZone(Serializable, Cloneable):
    """
    `TimeZone` represents a time zone offset, and also figures out daylight
    savings.
    
    
    Typically, you get a `TimeZone` using `getDefault`
    which creates a `TimeZone` based on the time zone where the program
    is running. For example, for a program running in Japan, `getDefault`
    creates a `TimeZone` object based on Japanese Standard Time.
    
    
    You can also get a `TimeZone` using `getTimeZone`
    along with a time zone ID. For instance, the time zone ID for the
    U.S. Pacific Time zone is "America/Los_Angeles". So, you can get a
    U.S. Pacific Time `TimeZone` object with:
    <blockquote>```
    TimeZone tz = TimeZone.getTimeZone("America/Los_Angeles");
    ```</blockquote>
    You can use the `getAvailableIDs` method to iterate through
    all the supported time zone IDs. You can then choose a
    supported ID to get a `TimeZone`.
    If the time zone you want is not represented by one of the
    supported IDs, then a custom time zone ID can be specified to
    produce a TimeZone. The syntax of a custom time zone ID is:
    
    <blockquote>```
    <a id="CustomID">*CustomID:*</a>
            `GMT` *Sign* *Hours* `:` *Minutes*
            `GMT` *Sign* *Hours* *Minutes*
            `GMT` *Sign* *Hours*
    *Sign:* one of
            `+ -`
    *Hours:*
            *Digit*
            *Digit* *Digit*
    *Minutes:*
            *Digit* *Digit*
    *Digit:* one of
            `0 1 2 3 4 5 6 7 8 9`
    ```</blockquote>
    
    *Hours* must be between 0 to 23 and *Minutes* must be
    between 00 to 59.  For example, "GMT+10" and "GMT+0010" mean ten
    hours and ten minutes ahead of GMT, respectively.
    
    The format is locale independent and digits must be taken from the
    Basic Latin block of the Unicode standard. No daylight saving time
    transition schedule can be specified with a custom time zone ID. If
    the specified string doesn't match the syntax, `"GMT"`
    is used.
    
    When creating a `TimeZone`, the specified custom time
    zone ID is normalized in the following syntax:
    <blockquote>```
    <a id="NormalizedCustomID">*NormalizedCustomID:*</a>
            `GMT` *Sign* *TwoDigitHours* `:` *Minutes*
    *Sign:* one of
            `+ -`
    *TwoDigitHours:*
            *Digit* *Digit*
    *Minutes:*
            *Digit* *Digit*
    *Digit:* one of
            `0 1 2 3 4 5 6 7 8 9`
    ```</blockquote>
    For example, TimeZone.getTimeZone("GMT-8").getID() returns "GMT-08:00".
    
    <h2>Three-letter time zone IDs</h2>
    
    For compatibility with JDK 1.1.x, some other three-letter time zone IDs
    (such as "PST", "CTT", "AST") are also supported. However, <strong>their
    use is deprecated</strong> because the same abbreviation is often used
    for multiple time zones (for example, "CST" could be U.S. "Central Standard
    Time" and "China Standard Time"), and the Java platform can then only
    recognize one of them.

    Author(s)
    - Mark Davis, David Goldsmith, Chen-Lieh Huang, Alan Liu

    See
    - SimpleTimeZone

    Since
    - 1.1
    """

    SHORT = 0
    """
    A style specifier for `getDisplayName()` indicating
    a short name, such as "PST."

    See
    - .LONG

    Since
    - 1.2
    """
    LONG = 1
    """
    A style specifier for `getDisplayName()` indicating
    a long name, such as "Pacific Standard Time."

    See
    - .SHORT

    Since
    - 1.2
    """


    def __init__(self):
        """
        Sole constructor.  (For invocation by subclass constructors, typically
        implicit.)
        """
        ...


    def getOffset(self, era: int, year: int, month: int, day: int, dayOfWeek: int, milliseconds: int) -> int:
        """
        Gets the time zone offset, for current date, modified in case of
        daylight savings. This is the offset to add to UTC to get local time.
        
        This method returns a historically correct offset if an
        underlying `TimeZone` implementation subclass
        supports historical Daylight Saving Time schedule and GMT
        offset changes.

        Arguments
        - era: the era of the given date.
        - year: the year in the given date.
        - month: the month in the given date.
        Month is 0-based. e.g., 0 for January.
        - day: the day-in-month of the given date.
        - dayOfWeek: the day-of-week of the given date.
        - milliseconds: the milliseconds in day in *standard*
        local time.

        Returns
        - the offset in milliseconds to add to GMT to get local time.

        See
        - Calendar.DST_OFFSET
        """
        ...


    def getOffset(self, date: int) -> int:
        """
        Returns the offset of this time zone from UTC at the specified
        date. If Daylight Saving Time is in effect at the specified
        date, the offset value is adjusted with the amount of daylight
        saving.
        
        This method returns a historically correct offset value if an
        underlying TimeZone implementation subclass supports historical
        Daylight Saving Time schedule and GMT offset changes.

        Arguments
        - date: the date represented in milliseconds since January 1, 1970 00:00:00 GMT

        Returns
        - the amount of time in milliseconds to add to UTC to get local time.

        See
        - Calendar.DST_OFFSET

        Since
        - 1.4
        """
        ...


    def setRawOffset(self, offsetMillis: int) -> None:
        """
        Sets the base time zone offset to GMT.
        This is the offset to add to UTC to get local time.
        
        If an underlying `TimeZone` implementation subclass
        supports historical GMT offset changes, the specified GMT
        offset is set as the latest GMT offset and the difference from
        the known latest GMT offset value is used to adjust all
        historical GMT offset values.

        Arguments
        - offsetMillis: the given base time zone offset to GMT.
        """
        ...


    def getRawOffset(self) -> int:
        """
        Returns the amount of time in milliseconds to add to UTC to get
        standard time in this time zone. Because this value is not
        affected by daylight saving time, it is called <I>raw
        offset</I>.
        
        If an underlying `TimeZone` implementation subclass
        supports historical GMT offset changes, the method returns the
        raw offset value of the current date. In Honolulu, for example,
        its raw offset changed from GMT-10:30 to GMT-10:00 in 1947, and
        this method always returns -36000000 milliseconds (i.e., -10
        hours).

        Returns
        - the amount of raw offset time in milliseconds to add to UTC.

        See
        - Calendar.ZONE_OFFSET
        """
        ...


    def getID(self) -> str:
        """
        Gets the ID of this time zone.

        Returns
        - the ID of this time zone.
        """
        ...


    def setID(self, ID: str) -> None:
        """
        Sets the time zone ID. This does not change any other data in
        the time zone object.

        Arguments
        - ID: the new time zone ID.
        """
        ...


    def getDisplayName(self) -> str:
        """
        Returns a long standard time name of this `TimeZone` suitable for
        presentation to the user in the default locale.
        
        This method is equivalent to:
        <blockquote>```
        getDisplayName(False, .LONG,
                       Locale.getDefault(Locale.Category.DISPLAY))
        ```</blockquote>

        Returns
        - the human-readable name of this time zone in the default locale.

        See
        - Locale.Category

        Since
        - 1.2
        """
        ...


    def getDisplayName(self, locale: "Locale") -> str:
        """
        Returns a long standard time name of this `TimeZone` suitable for
        presentation to the user in the specified `locale`.
        
        This method is equivalent to:
        <blockquote>```
        getDisplayName(False, .LONG, locale)
        ```</blockquote>

        Arguments
        - locale: the locale in which to supply the display name.

        Returns
        - the human-readable name of this time zone in the given locale.

        Raises
        - NullPointerException: if `locale` is `null`.

        See
        - .getDisplayName(boolean, int, Locale)

        Since
        - 1.2
        """
        ...


    def getDisplayName(self, daylight: bool, style: int) -> str:
        """
        Returns a name in the specified `style` of this `TimeZone`
        suitable for presentation to the user in the default locale. If the
        specified `daylight` is `True`, a Daylight Saving Time name
        is returned (even if this `TimeZone` doesn't observe Daylight Saving
        Time). Otherwise, a Standard Time name is returned.
        
        This method is equivalent to:
        <blockquote>```
        getDisplayName(daylight, style,
                       Locale.getDefault(Locale.Category.DISPLAY))
        ```</blockquote>

        Arguments
        - daylight: `True` specifying a Daylight Saving Time name, or
                        `False` specifying a Standard Time name
        - style: either .LONG or .SHORT

        Returns
        - the human-readable name of this time zone in the default locale.

        Raises
        - IllegalArgumentException: if `style` is invalid.

        See
        - java.text.DateFormatSymbols.getZoneStrings()

        Since
        - 1.2
        """
        ...


    def getDisplayName(self, daylight: bool, style: int, locale: "Locale") -> str:
        """
        Returns a name in the specified `style` of this `TimeZone`
        suitable for presentation to the user in the specified `locale`. If the specified `daylight` is `True`, a Daylight
        Saving Time name is returned (even if this `TimeZone` doesn't
        observe Daylight Saving Time). Otherwise, a Standard Time name is
        returned.
        
        When looking up a time zone name, the ResourceBundle.Control.getCandidateLocales(String,Locale) default
        {@code Locale search path of `ResourceBundle`} derived
        from the specified `locale` is used. (No ResourceBundle.Control.getFallbackLocale(String,Locale) fallback
        {@code Locale} search is performed.) If a time zone name in any
        `Locale` of the search path, including Locale.ROOT, is
        found, the name is returned. Otherwise, a string in the
        <a href="#NormalizedCustomID">normalized custom ID format</a> is returned.

        Arguments
        - daylight: `True` specifying a Daylight Saving Time name, or
                        `False` specifying a Standard Time name
        - style: either .LONG or .SHORT
        - locale: the locale in which to supply the display name.

        Returns
        - the human-readable name of this time zone in the given locale.

        Raises
        - IllegalArgumentException: if `style` is invalid.
        - NullPointerException: if `locale` is `null`.

        See
        - java.text.DateFormatSymbols.getZoneStrings()

        Since
        - 1.2
        """
        ...


    def getDSTSavings(self) -> int:
        """
        Returns the amount of time to be added to local standard time
        to get local wall clock time.
        
        The default implementation returns 3600000 milliseconds
        (i.e., one hour) if a call to .useDaylightTime()
        returns `True`. Otherwise, 0 (zero) is returned.
        
        If an underlying `TimeZone` implementation subclass
        supports historical and future Daylight Saving Time schedule
        changes, this method returns the amount of saving time of the
        last known Daylight Saving Time rule that can be a future
        prediction.
        
        If the amount of saving time at any given time stamp is
        required, construct a Calendar with this `TimeZone` and the time stamp, and call Calendar.get(int)
        Calendar.get`(`Calendar.DST_OFFSET`)`.

        Returns
        - the amount of saving time in milliseconds

        See
        - Calendar.ZONE_OFFSET

        Since
        - 1.4
        """
        ...


    def useDaylightTime(self) -> bool:
        """
        Queries if this `TimeZone` uses Daylight Saving Time.
        
        If an underlying `TimeZone` implementation subclass
        supports historical and future Daylight Saving Time schedule
        changes, this method refers to the last known Daylight Saving Time
        rule that can be a future prediction and may not be the same as
        the current rule. Consider calling .observesDaylightTime()
        if the current rule should also be taken into account.

        Returns
        - `True` if this `TimeZone` uses Daylight Saving Time,
                `False`, otherwise.

        See
        - Calendar.DST_OFFSET
        """
        ...


    def observesDaylightTime(self) -> bool:
        """
        Returns `True` if this `TimeZone` is currently in
        Daylight Saving Time, or if a transition from Standard Time to
        Daylight Saving Time occurs at any future time.
        
        The default implementation returns `True` if
        `useDaylightTime()` or `inDaylightTime(new Date())`
        returns `True`.

        Returns
        - `True` if this `TimeZone` is currently in
        Daylight Saving Time, or if a transition from Standard Time to
        Daylight Saving Time occurs at any future time; `False`
        otherwise.

        See
        - Calendar.DST_OFFSET

        Since
        - 1.7
        """
        ...


    def inDaylightTime(self, date: "Date") -> bool:
        """
        Queries if the given `date` is in Daylight Saving Time in
        this time zone.

        Arguments
        - date: the given Date.

        Returns
        - `True` if the given date is in Daylight Saving Time,
                `False`, otherwise.
        """
        ...


    @staticmethod
    def getTimeZone(ID: str) -> "TimeZone":
        """
        Gets the `TimeZone` for the given ID.

        Arguments
        - ID: the ID for a `TimeZone`, either an abbreviation
        such as "PST", a full name such as "America/Los_Angeles", or a custom
        ID such as "GMT-8:00". Note that the support of abbreviations is
        for JDK 1.1.x compatibility only and full names should be used.

        Returns
        - the specified `TimeZone`, or the GMT zone if the given ID
        cannot be understood.
        """
        ...


    @staticmethod
    def getTimeZone(zoneId: "ZoneId") -> "TimeZone":
        """
        Gets the `TimeZone` for the given `zoneId`.

        Arguments
        - zoneId: a ZoneId from which the time zone ID is obtained

        Returns
        - the specified `TimeZone`, or the GMT zone if the given ID
                cannot be understood.

        Raises
        - NullPointerException: if `zoneId` is `null`

        Since
        - 1.8
        """
        ...


    def toZoneId(self) -> "ZoneId":
        """
        Converts this `TimeZone` object to a `ZoneId`.

        Returns
        - a `ZoneId` representing the same time zone as this
                `TimeZone`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def getAvailableIDs(rawOffset: int) -> list[str]:
        """
        Gets the available IDs according to the given time zone offset in milliseconds.

        Arguments
        - rawOffset: the given time zone GMT offset in milliseconds.

        Returns
        - an array of IDs, where the time zone for that ID has
        the specified GMT offset. For example, "America/Phoenix" and "America/Denver"
        both have GMT-07:00, but differ in daylight saving behavior.

        See
        - .getRawOffset()
        """
        ...


    @staticmethod
    def getAvailableIDs() -> list[str]:
        """
        Gets all the available IDs supported.

        Returns
        - an array of IDs.
        """
        ...


    @staticmethod
    def getDefault() -> "TimeZone":
        """
        Gets the default `TimeZone` of the Java virtual machine. If the
        cached default `TimeZone` is available, its clone is returned.
        Otherwise, the method takes the following steps to determine the default
        time zone.
        
        
        - Use the `user.timezone` property value as the default
        time zone ID if it's available.
        - Detect the platform time zone ID. The source of the
        platform time zone and ID mapping may vary with implementation.
        - Use `GMT` as the last resort if the given or detected
        time zone ID is unknown.
        
        
        The default `TimeZone` created from the ID is cached,
        and its clone is returned. The `user.timezone` property
        value is set to the ID upon return.

        Returns
        - the default `TimeZone`

        See
        - .setDefault(TimeZone)
        """
        ...


    @staticmethod
    def setDefault(zone: "TimeZone") -> None:
        """
        Sets the `TimeZone` that is returned by the `getDefault`
        method. `zone` is cached. If `zone` is null, the cached
        default `TimeZone` is cleared. This method doesn't change the value
        of the `user.timezone` property.

        Arguments
        - zone: the new default `TimeZone`, or null

        Raises
        - SecurityException: if the security manager's `checkPermission`
                                  denies `PropertyPermission("user.timezone",
                                  "write")`

        See
        - PropertyPermission
        """
        ...


    def hasSameRules(self, other: "TimeZone") -> bool:
        """
        Returns True if this zone has the same rule and offset as another zone.
        That is, if this zone differs only in ID, if at all.  Returns False
        if the other zone is null.

        Arguments
        - other: the `TimeZone` object to be compared with

        Returns
        - True if the other zone is not null and is the same as this one,
        with the possible exception of the ID

        Since
        - 1.2
        """
        ...


    def clone(self) -> "Object":
        """
        Creates a copy of this `TimeZone`.

        Returns
        - a clone of this `TimeZone`
        """
        ...
