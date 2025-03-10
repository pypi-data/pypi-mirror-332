"""
Python module generated from Java source file java.text.NumberFormat

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.math import BigInteger
from java.math import RoundingMode
from java.text import *
from java.text.spi import NumberFormatProvider
from java.util import Currency
from java.util import Locale
from java.util import Objects
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicLong
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import LocaleServiceProviderPool
from typing import Any, Callable, Iterable, Tuple


class NumberFormat(Format):
    """
    `NumberFormat` is the abstract base class for all number
    formats. This class provides the interface for formatting and parsing
    numbers. `NumberFormat` also provides methods for determining
    which locales have number formats, and what their names are.
    
    
    `NumberFormat` helps you to format and parse numbers for any locale.
    Your code can be completely independent of the locale conventions for
    decimal points, thousands-separators, or even the particular decimal
    digits used, or whether the number format is even decimal.
    
    
    To format a number for the current Locale, use one of the factory
    class methods:
    <blockquote>
    ````myString = NumberFormat.getInstance().format(myNumber);````
    </blockquote>
    If you are formatting multiple numbers, it is
    more efficient to get the format and use it multiple times so that
    the system doesn't have to fetch the information about the local
    language and country conventions multiple times.
    <blockquote>
    ````NumberFormat nf = NumberFormat.getInstance();
    for (int i = 0; i < myNumber.length; ++i) {
        output.println(nf.format(myNumber[i]) + "; ");`
    }```
    </blockquote>
    To format a number for a different Locale, specify it in the
    call to `getInstance`.
    <blockquote>
    ````NumberFormat nf = NumberFormat.getInstance(Locale.FRENCH);````
    </blockquote>
    
    If the locale contains "nu" (numbers) and/or "rg" (region override)
    <a href="../util/Locale.html#def_locale_extension">Unicode extensions</a>,
    the decimal digits, and/or the country used for formatting are overridden.
    If both "nu" and "rg" are specified, the decimal digits from the "nu"
    extension supersedes the implicit one from the "rg" extension.
    
    You can also use a `NumberFormat` to parse numbers:
    <blockquote>
    ````myNumber = nf.parse(myString);````
    </blockquote>
    Use `getInstance` or `getNumberInstance` to get the
    normal number format. Use `getIntegerInstance` to get an
    integer number format. Use `getCurrencyInstance` to get the
    currency number format. Use `getCompactNumberInstance` to get the
    compact number format to format a number in shorter form. For example,
    `2000` can be formatted as `"2K"` in
    java.util.Locale.US US locale. Use `getPercentInstance`
    to get a format for displaying percentages. With this format, a fraction
    like 0.53 is displayed as 53%.
    
    
    You can also control the display of numbers with such methods as
    `setMinimumFractionDigits`.
    If you want even more control over the format or parsing,
    or want to give your users more control,
    you can try casting the `NumberFormat` you get from the factory methods
    to a `DecimalFormat` or `CompactNumberFormat` depending on
    the factory method used. This will work for the vast majority of locales;
    just remember to put it in a `try` block in case you encounter
    an unusual one.
    
    
    NumberFormat and DecimalFormat are designed such that some controls
    work for formatting and others work for parsing.  The following is
    the detailed description for each these control methods,
    
    setParseIntegerOnly : only affects parsing, e.g.
    if True,  "3456.78" &rarr; 3456 (and leaves the parse position just after index 6)
    if False, "3456.78" &rarr; 3456.78 (and leaves the parse position just after index 8)
    This is independent of formatting.  If you want to not show a decimal point
    where there might be no digits after the decimal point, use
    setDecimalSeparatorAlwaysShown.
    
    setDecimalSeparatorAlwaysShown : only affects formatting, and only where
    there might be no digits after the decimal point, such as with a pattern
    like "#,##0.##", e.g.,
    if True,  3456.00 &rarr; "3,456."
    if False, 3456.00 &rarr; "3456"
    This is independent of parsing.  If you want parsing to stop at the decimal
    point, use setParseIntegerOnly.
    
    
    You can also use forms of the `parse` and `format`
    methods with `ParsePosition` and `FieldPosition` to
    allow you to:
    
    -  progressively parse through pieces of a string
    -  align the decimal point and other areas
    
    For example, you can align numbers in two ways:
    <ol>
    -  If you are using a monospaced font with spacing for alignment,
         you can pass the `FieldPosition` in your format call, with
         `field` = `INTEGER_FIELD`. On output,
         `getEndIndex` will be set to the offset between the
         last character of the integer and the decimal. Add
         (desiredSpaceCount - getEndIndex) spaces at the front of the string.
    
    -  If you are using proportional fonts,
         instead of padding with spaces, measure the width
         of the string in pixels from the start to `getEndIndex`.
         Then move the pen by
         (desiredPixelWidth - widthToAlignmentPoint) before drawing the text.
         It also works where there is no decimal, but possibly additional
         characters at the end, e.g., with parentheses in negative
         numbers: "(12)" for -12.
    </ol>
    
    <h2><a id="synchronization">Synchronization</a></h2>
    
    
    Number formats are generally not synchronized.
    It is recommended to create separate format instances for each thread.
    If multiple threads access a format concurrently, it must be synchronized
    externally.

    Author(s)
    - Helena Shih

    See
    - CompactNumberFormat

    Since
    - 1.1

    Unknown Tags
    - The .format(double, StringBuffer, FieldPosition),
    .format(long, StringBuffer, FieldPosition) and
    .parse(String, ParsePosition) methods may throw
    `NullPointerException`, if any of their parameter is `null`.
    The subclass may provide its own implementation and specification about
    `NullPointerException`.
    
    
    The default implementation provides rounding modes defined
    in java.math.RoundingMode for formatting numbers. It
    uses the java.math.RoundingMode.HALF_EVEN
    round half-even algorithm. To change the rounding mode use
    .setRoundingMode(java.math.RoundingMode) setRoundingMode.
    The `NumberFormat` returned by the static factory methods is
    configured to round floating point numbers using half-even
    rounding (see java.math.RoundingMode.HALF_EVEN
    RoundingMode.HALF_EVEN) for formatting.
    """

    INTEGER_FIELD = 0
    """
    Field constant used to construct a FieldPosition object. Signifies that
    the position of the integer part of a formatted number should be returned.

    See
    - java.text.FieldPosition
    """
    FRACTION_FIELD = 1
    """
    Field constant used to construct a FieldPosition object. Signifies that
    the position of the fraction part of a formatted number should be returned.

    See
    - java.text.FieldPosition
    """


    def format(self, number: "Object", toAppendTo: "StringBuffer", pos: "FieldPosition") -> "StringBuffer":
        """
        Formats a number and appends the resulting text to the given string
        buffer.
        The number can be of any subclass of java.lang.Number.
        
        This implementation extracts the number's value using
        java.lang.Number.longValue() for all integral type values that
        can be converted to `long` without loss of information,
        including `BigInteger` values with a
        java.math.BigInteger.bitLength() bit length of less than 64,
        and java.lang.Number.doubleValue() for all other types. It
        then calls
        .format(long,java.lang.StringBuffer,java.text.FieldPosition)
        or .format(double,java.lang.StringBuffer,java.text.FieldPosition).
        This may result in loss of magnitude information and precision for
        `BigInteger` and `BigDecimal` values.

        Arguments
        - number: the number to format
        - toAppendTo: the `StringBuffer` to which the formatted
                          text is to be appended
        - pos: keeps track on the position of the field within the
                          returned string. For example, for formatting a number
                          `1234567.89` in `Locale.US` locale,
                          if the given `fieldPosition` is
                          NumberFormat.INTEGER_FIELD, the begin index
                          and end index of `fieldPosition` will be set
                          to 0 and 9, respectively for the output string
                          `1,234,567.89`.

        Returns
        - the value passed in as `toAppendTo`

        Raises
        - IllegalArgumentException: if `number` is
                          null or not an instance of `Number`.
        - NullPointerException: if `toAppendTo` or
                          `pos` is null
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.FieldPosition
        """
        ...


    def parseObject(self, source: str, pos: "ParsePosition") -> "Object":
        """
        Parses text from a string to produce a `Number`.
        
        The method attempts to parse text starting at the index given by
        `pos`.
        If parsing succeeds, then the index of `pos` is updated
        to the index after the last character used (parsing does not necessarily
        use all characters up to the end of the string), and the parsed
        number is returned. The updated `pos` can be used to
        indicate the starting point for the next call to this method.
        If an error occurs, then the index of `pos` is not
        changed, the error index of `pos` is set to the index of
        the character where the error occurred, and null is returned.
        
        See the .parse(String, ParsePosition) method for more information
        on number parsing.

        Arguments
        - source: A `String`, part of which should be parsed.
        - pos: A `ParsePosition` object with index and error
                   index information as described above.

        Returns
        - A `Number` parsed from the string. In case of
                error, returns null.

        Raises
        - NullPointerException: if `source` or `pos` is null.
        """
        ...


    def format(self, number: float) -> str:
        """
        Specialization of format.

        Arguments
        - number: the double number to format

        Returns
        - the formatted String

        Raises
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.Format.format
        """
        ...


    def format(self, number: int) -> str:
        """
        Specialization of format.

        Arguments
        - number: the long number to format

        Returns
        - the formatted String

        Raises
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.Format.format
        """
        ...


    def format(self, number: float, toAppendTo: "StringBuffer", pos: "FieldPosition") -> "StringBuffer":
        """
        Specialization of format.

        Arguments
        - number: the double number to format
        - toAppendTo: the StringBuffer to which the formatted text is to be
                          appended
        - pos: keeps track on the position of the field within the
                          returned string. For example, for formatting a number
                          `1234567.89` in `Locale.US` locale,
                          if the given `fieldPosition` is
                          NumberFormat.INTEGER_FIELD, the begin index
                          and end index of `fieldPosition` will be set
                          to 0 and 9, respectively for the output string
                          `1,234,567.89`.

        Returns
        - the formatted StringBuffer

        Raises
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.Format.format
        """
        ...


    def format(self, number: int, toAppendTo: "StringBuffer", pos: "FieldPosition") -> "StringBuffer":
        """
        Specialization of format.

        Arguments
        - number: the long number to format
        - toAppendTo: the StringBuffer to which the formatted text is to be
                          appended
        - pos: keeps track on the position of the field within the
                          returned string. For example, for formatting a number
                          `123456789` in `Locale.US` locale,
                          if the given `fieldPosition` is
                          NumberFormat.INTEGER_FIELD, the begin index
                          and end index of `fieldPosition` will be set
                          to 0 and 11, respectively for the output string
                          `123,456,789`.

        Returns
        - the formatted StringBuffer

        Raises
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.Format.format
        """
        ...


    def parse(self, source: str, parsePosition: "ParsePosition") -> "Number":
        """
        Returns a Long if possible (e.g., within the range [Long.MIN_VALUE,
        Long.MAX_VALUE] and with no decimals), otherwise a Double.
        If IntegerOnly is set, will stop at a decimal
        point (or equivalent; e.g., for rational numbers "1 2/3", will stop
        after the 1).
        Does not throw an exception; if no object can be parsed, index is
        unchanged!

        Arguments
        - source: the String to parse
        - parsePosition: the parse position

        Returns
        - the parsed value

        See
        - java.text.Format.parseObject
        """
        ...


    def parse(self, source: str) -> "Number":
        """
        Parses text from the beginning of the given string to produce a number.
        The method may not use the entire text of the given string.
        
        See the .parse(String, ParsePosition) method for more information
        on number parsing.

        Arguments
        - source: A `String` whose beginning should be parsed.

        Returns
        - A `Number` parsed from the string.

        Raises
        - ParseException: if the beginning of the specified string
                   cannot be parsed.
        """
        ...


    def isParseIntegerOnly(self) -> bool:
        """
        Returns True if this format will parse numbers as integers only.
        For example in the English locale, with ParseIntegerOnly True, the
        string "1234." would be parsed as the integer value 1234 and parsing
        would stop at the "." character.  Of course, the exact format accepted
        by the parse operation is locale dependent and determined by sub-classes
        of NumberFormat.

        Returns
        - `True` if numbers should be parsed as integers only;
                `False` otherwise
        """
        ...


    def setParseIntegerOnly(self, value: bool) -> None:
        """
        Sets whether or not numbers should be parsed as integers only.

        Arguments
        - value: `True` if numbers should be parsed as integers only;
                     `False` otherwise

        See
        - .isParseIntegerOnly
        """
        ...


    @staticmethod
    def getInstance() -> "NumberFormat":
        """
        Returns a general-purpose number format for the current default
        java.util.Locale.Category.FORMAT FORMAT locale.
        This is the same as calling
        .getNumberInstance() getNumberInstance().

        Returns
        - the `NumberFormat` instance for general-purpose number
        formatting
        """
        ...


    @staticmethod
    def getInstance(inLocale: "Locale") -> "NumberFormat":
        """
        Returns a general-purpose number format for the specified locale.
        This is the same as calling
        .getNumberInstance(java.util.Locale) getNumberInstance(inLocale).

        Arguments
        - inLocale: the desired locale

        Returns
        - the `NumberFormat` instance for general-purpose number
        formatting
        """
        ...


    @staticmethod
    def getNumberInstance() -> "NumberFormat":
        """
        Returns a general-purpose number format for the current default
        java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getNumberInstance(Locale)
            getNumberInstance(Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - the `NumberFormat` instance for general-purpose number
        formatting

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getNumberInstance(inLocale: "Locale") -> "NumberFormat":
        """
        Returns a general-purpose number format for the specified locale.

        Arguments
        - inLocale: the desired locale

        Returns
        - the `NumberFormat` instance for general-purpose number
        formatting
        """
        ...


    @staticmethod
    def getIntegerInstance() -> "NumberFormat":
        """
        Returns an integer number format for the current default
        java.util.Locale.Category.FORMAT FORMAT locale. The
        returned number format is configured to round floating point numbers
        to the nearest integer using half-even rounding (see java.math.RoundingMode.HALF_EVEN RoundingMode.HALF_EVEN) for formatting,
        and to parse only the integer part of an input string (see .isParseIntegerOnly isParseIntegerOnly).
        This is equivalent to calling
        .getIntegerInstance(Locale)
            getIntegerInstance(Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - a number format for integer values

        See
        - java.util.Locale.Category.FORMAT

        Since
        - 1.4
        """
        ...


    @staticmethod
    def getIntegerInstance(inLocale: "Locale") -> "NumberFormat":
        """
        Returns an integer number format for the specified locale. The
        returned number format is configured to round floating point numbers
        to the nearest integer using half-even rounding (see java.math.RoundingMode.HALF_EVEN RoundingMode.HALF_EVEN) for formatting,
        and to parse only the integer part of an input string (see .isParseIntegerOnly isParseIntegerOnly).

        Arguments
        - inLocale: the desired locale

        Returns
        - a number format for integer values

        See
        - .getRoundingMode()

        Since
        - 1.4
        """
        ...


    @staticmethod
    def getCurrencyInstance() -> "NumberFormat":
        """
        Returns a currency format for the current default
        java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getCurrencyInstance(Locale)
            getCurrencyInstance(Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - the `NumberFormat` instance for currency formatting

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getCurrencyInstance(inLocale: "Locale") -> "NumberFormat":
        """
        Returns a currency format for the specified locale.
        
        If the specified locale contains the "`cf`" (
        <a href="https://www.unicode.org/reports/tr35/tr35.html#UnicodeCurrencyFormatIdentifier">
        currency format style</a>)
        <a href="../util/Locale.html#def_locale_extension">Unicode extension</a>,
        the returned currency format uses the style if it is available.
        Otherwise, the style uses the default "`standard`" currency format.
        For example, if the style designates "`account`", negative
        currency amounts use a pair of parentheses in some locales.

        Arguments
        - inLocale: the desired locale

        Returns
        - the `NumberFormat` instance for currency formatting
        """
        ...


    @staticmethod
    def getPercentInstance() -> "NumberFormat":
        """
        Returns a percentage format for the current default
        java.util.Locale.Category.FORMAT FORMAT locale.
        This is equivalent to calling
        .getPercentInstance(Locale)
            getPercentInstance(Locale.getDefault(Locale.Category.FORMAT)).

        Returns
        - the `NumberFormat` instance for percentage formatting

        See
        - java.util.Locale.Category.FORMAT
        """
        ...


    @staticmethod
    def getPercentInstance(inLocale: "Locale") -> "NumberFormat":
        """
        Returns a percentage format for the specified locale.

        Arguments
        - inLocale: the desired locale

        Returns
        - the `NumberFormat` instance for percentage formatting
        """
        ...


    @staticmethod
    def getCompactNumberInstance() -> "NumberFormat":
        """
        Returns a compact number format for the default
        java.util.Locale.Category.FORMAT FORMAT locale with
        NumberFormat.Style.SHORT "SHORT" format style.

        Returns
        - A `NumberFormat` instance for compact number
                formatting

        See
        - java.util.Locale.Category.FORMAT

        Since
        - 12
        """
        ...


    @staticmethod
    def getCompactNumberInstance(locale: "Locale", formatStyle: "NumberFormat.Style") -> "NumberFormat":
        """
        Returns a compact number format for the specified java.util.Locale locale
        and NumberFormat.Style formatStyle.

        Arguments
        - locale: the desired locale
        - formatStyle: the style for formatting a number

        Returns
        - A `NumberFormat` instance for compact number
                formatting

        Raises
        - NullPointerException: if `locale` or `formatStyle`
                                     is `null`

        See
        - java.util.Locale

        Since
        - 12
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
        java.text.spi.NumberFormatProvider NumberFormatProvider implementations.
        It must contain at least a `Locale` instance equal to
        java.util.Locale.US Locale.US.

        Returns
        - An array of locales for which localized
                `NumberFormat` instances are available.
        """
        ...


    def hashCode(self) -> int:
        """
        Overrides hashCode.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Overrides equals.
        """
        ...


    def clone(self) -> "Object":
        """
        Overrides Cloneable.
        """
        ...


    def isGroupingUsed(self) -> bool:
        """
        Returns True if grouping is used in this format. For example, in the
        English locale, with grouping on, the number 1234567 might be formatted
        as "1,234,567". The grouping separator as well as the size of each group
        is locale dependent and is determined by sub-classes of NumberFormat.

        Returns
        - `True` if grouping is used;
                `False` otherwise

        See
        - .setGroupingUsed
        """
        ...


    def setGroupingUsed(self, newValue: bool) -> None:
        """
        Set whether or not grouping will be used in this format.

        Arguments
        - newValue: `True` if grouping is used;
                        `False` otherwise

        See
        - .isGroupingUsed
        """
        ...


    def getMaximumIntegerDigits(self) -> int:
        """
        Returns the maximum number of digits allowed in the integer portion of a
        number.

        Returns
        - the maximum number of digits

        See
        - .setMaximumIntegerDigits
        """
        ...


    def setMaximumIntegerDigits(self, newValue: int) -> None:
        """
        Sets the maximum number of digits allowed in the integer portion of a
        number. maximumIntegerDigits must be &ge; minimumIntegerDigits.  If the
        new value for maximumIntegerDigits is less than the current value
        of minimumIntegerDigits, then minimumIntegerDigits will also be set to
        the new value.

        Arguments
        - newValue: the maximum number of integer digits to be shown; if
        less than zero, then zero is used. The concrete subclass may enforce an
        upper limit to this value appropriate to the numeric type being formatted.

        See
        - .getMaximumIntegerDigits
        """
        ...


    def getMinimumIntegerDigits(self) -> int:
        """
        Returns the minimum number of digits allowed in the integer portion of a
        number.

        Returns
        - the minimum number of digits

        See
        - .setMinimumIntegerDigits
        """
        ...


    def setMinimumIntegerDigits(self, newValue: int) -> None:
        """
        Sets the minimum number of digits allowed in the integer portion of a
        number. minimumIntegerDigits must be &le; maximumIntegerDigits.  If the
        new value for minimumIntegerDigits exceeds the current value
        of maximumIntegerDigits, then maximumIntegerDigits will also be set to
        the new value

        Arguments
        - newValue: the minimum number of integer digits to be shown; if
        less than zero, then zero is used. The concrete subclass may enforce an
        upper limit to this value appropriate to the numeric type being formatted.

        See
        - .getMinimumIntegerDigits
        """
        ...


    def getMaximumFractionDigits(self) -> int:
        """
        Returns the maximum number of digits allowed in the fraction portion of a
        number.

        Returns
        - the maximum number of digits.

        See
        - .setMaximumFractionDigits
        """
        ...


    def setMaximumFractionDigits(self, newValue: int) -> None:
        """
        Sets the maximum number of digits allowed in the fraction portion of a
        number. maximumFractionDigits must be &ge; minimumFractionDigits.  If the
        new value for maximumFractionDigits is less than the current value
        of minimumFractionDigits, then minimumFractionDigits will also be set to
        the new value.

        Arguments
        - newValue: the maximum number of fraction digits to be shown; if
        less than zero, then zero is used. The concrete subclass may enforce an
        upper limit to this value appropriate to the numeric type being formatted.

        See
        - .getMaximumFractionDigits
        """
        ...


    def getMinimumFractionDigits(self) -> int:
        """
        Returns the minimum number of digits allowed in the fraction portion of a
        number.

        Returns
        - the minimum number of digits

        See
        - .setMinimumFractionDigits
        """
        ...


    def setMinimumFractionDigits(self, newValue: int) -> None:
        """
        Sets the minimum number of digits allowed in the fraction portion of a
        number. minimumFractionDigits must be &le; maximumFractionDigits.  If the
        new value for minimumFractionDigits exceeds the current value
        of maximumFractionDigits, then maximumFractionDigits will also be set to
        the new value

        Arguments
        - newValue: the minimum number of fraction digits to be shown; if
        less than zero, then zero is used. The concrete subclass may enforce an
        upper limit to this value appropriate to the numeric type being formatted.

        See
        - .getMinimumFractionDigits
        """
        ...


    def getCurrency(self) -> "Currency":
        """
        Gets the currency used by this number format when formatting
        currency values. The initial value is derived in a locale dependent
        way. The returned value may be null if no valid
        currency could be determined and no currency has been set using
        .setCurrency(java.util.Currency) setCurrency.
        
        The default implementation throws
        `UnsupportedOperationException`.

        Returns
        - the currency used by this number format, or `null`

        Raises
        - UnsupportedOperationException: if the number format class
        doesn't implement currency formatting

        Since
        - 1.4
        """
        ...


    def setCurrency(self, currency: "Currency") -> None:
        """
        Sets the currency used by this number format when formatting
        currency values. This does not update the minimum or maximum
        number of fraction digits used by the number format.
        
        The default implementation throws
        `UnsupportedOperationException`.

        Arguments
        - currency: the new currency to be used by this number format

        Raises
        - UnsupportedOperationException: if the number format class
        doesn't implement currency formatting
        - NullPointerException: if `currency` is null

        Since
        - 1.4
        """
        ...


    def getRoundingMode(self) -> "RoundingMode":
        """
        Gets the java.math.RoundingMode used in this NumberFormat.
        The default implementation of this method in NumberFormat
        always throws java.lang.UnsupportedOperationException.
        Subclasses which handle different rounding modes should override
        this method.

        Returns
        - The `RoundingMode` used for this NumberFormat.

        Raises
        - UnsupportedOperationException: The default implementation
            always throws this exception

        See
        - .setRoundingMode(RoundingMode)

        Since
        - 1.6
        """
        ...


    def setRoundingMode(self, roundingMode: "RoundingMode") -> None:
        """
        Sets the java.math.RoundingMode used in this NumberFormat.
        The default implementation of this method in NumberFormat always
        throws java.lang.UnsupportedOperationException.
        Subclasses which handle different rounding modes should override
        this method.

        Arguments
        - roundingMode: The `RoundingMode` to be used

        Raises
        - UnsupportedOperationException: The default implementation
            always throws this exception
        - NullPointerException: if `roundingMode` is null

        See
        - .getRoundingMode()

        Since
        - 1.6
        """
        ...


    class Field(Field):
        """
        Defines constants that are used as attribute keys in the
        `AttributedCharacterIterator` returned
        from `NumberFormat.formatToCharacterIterator` and as
        field identifiers in `FieldPosition`.

        Since
        - 1.4
        """

        INTEGER = Field("integer")
        """
        Constant identifying the integer field.
        """
        FRACTION = Field("fraction")
        """
        Constant identifying the fraction field.
        """
        EXPONENT = Field("exponent")
        """
        Constant identifying the exponent field.
        """
        DECIMAL_SEPARATOR = Field("decimal separator")
        """
        Constant identifying the decimal separator field.
        """
        SIGN = Field("sign")
        """
        Constant identifying the sign field.
        """
        GROUPING_SEPARATOR = Field("grouping separator")
        """
        Constant identifying the grouping separator field.
        """
        EXPONENT_SYMBOL = Field("exponent symbol")
        """
        Constant identifying the exponent symbol field.
        """
        PERCENT = Field("percent")
        """
        Constant identifying the percent field.
        """
        PERMILLE = Field("per mille")
        """
        Constant identifying the permille field.
        """
        CURRENCY = Field("currency")
        """
        Constant identifying the currency field.
        """
        EXPONENT_SIGN = Field("exponent sign")
        """
        Constant identifying the exponent sign field.
        """
        PREFIX = Field("prefix")
        """
        Constant identifying the prefix field.

        Since
        - 12
        """
        SUFFIX = Field("suffix")
        """
        Constant identifying the suffix field.

        Since
        - 12
        """


    class Style(Enum):
        """
        A number format style.
        
        `Style` is an enum which represents the style for formatting
        a number within a given `NumberFormat` instance.

        See
        - NumberFormat.getCompactNumberInstance(Locale, Style)

        Since
        - 12
        """

        SHORT = 0
        """
        The `SHORT` number format style.
        """
        LONG = 1
        """
        The `LONG` number format style.
        """
