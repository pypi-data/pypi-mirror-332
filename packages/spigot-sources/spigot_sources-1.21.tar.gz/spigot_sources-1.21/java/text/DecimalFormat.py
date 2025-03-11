"""
Python module generated from Java source file java.text.DecimalFormat

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.math import BigDecimal
from java.math import BigInteger
from java.math import RoundingMode
from java.text import *
from java.text.spi import NumberFormatProvider
from java.util import Currency
from java.util import Locale
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicLong
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import ResourceBundleBasedAdapter
from typing import Any, Callable, Iterable, Tuple


class DecimalFormat(NumberFormat):
    """
    `DecimalFormat` is a concrete subclass of
    `NumberFormat` that formats decimal numbers. It has a variety of
    features designed to make it possible to parse and format numbers in any
    locale, including support for Western, Arabic, and Indic digits.  It also
    supports different kinds of numbers, including integers (123), fixed-point
    numbers (123.4), scientific notation (1.23E4), percentages (12%), and
    currency amounts ($123).  All of these can be localized.
    
    To obtain a `NumberFormat` for a specific locale, including the
    default locale, call one of `NumberFormat`'s factory methods, such
    as `getInstance()`.  In general, do not call the
    `DecimalFormat` constructors directly, since the
    `NumberFormat` factory methods may return subclasses other than
    `DecimalFormat`. If you need to customize the format object, do
    something like this:
    
    <blockquote>```
    NumberFormat f = NumberFormat.getInstance(loc);
    if (f instanceof DecimalFormat) {
        ((DecimalFormat) f).setDecimalSeparatorAlwaysShown(True);
    }
    ```</blockquote>
    
    A `DecimalFormat` comprises a *pattern* and a set of
    *symbols*.  The pattern may be set directly using
    `applyPattern()`, or indirectly using the API methods.  The
    symbols are stored in a `DecimalFormatSymbols` object.  When using
    the `NumberFormat` factory methods, the pattern and symbols are
    read from localized `ResourceBundle`s.
    
    <h2>Patterns</h2>
    
    `DecimalFormat` patterns have the following syntax:
    <blockquote>```
    *Pattern:*
            *PositivePattern*
            *PositivePattern* ; *NegativePattern*
    *PositivePattern:*
            *Prefix<sub>opt</sub>* *Number* *Suffix<sub>opt</sub>*
    *NegativePattern:*
            *Prefix<sub>opt</sub>* *Number* *Suffix<sub>opt</sub>*
    *Prefix:*
            any Unicode characters except &#92;uFFFE, &#92;uFFFF, and special characters
    *Suffix:*
            any Unicode characters except &#92;uFFFE, &#92;uFFFF, and special characters
    *Number:*
            *Integer* *Exponent<sub>opt</sub>*
            *Integer* . *Fraction* *Exponent<sub>opt</sub>*
    *Integer:*
            *MinimumInteger*
            #
            # *Integer*
            # , *Integer*
    *MinimumInteger:*
            0
            0 *MinimumInteger*
            0 , *MinimumInteger*
    *Fraction:*
            *MinimumFraction<sub>opt</sub>* *OptionalFraction<sub>opt</sub>*
    *MinimumFraction:*
            0 *MinimumFraction<sub>opt</sub>*
    *OptionalFraction:*
            # *OptionalFraction<sub>opt</sub>*
    *Exponent:*
            E *MinimumExponent*
    *MinimumExponent:*
            0 *MinimumExponent<sub>opt</sub>*
    ```</blockquote>
    
    A `DecimalFormat` pattern contains a positive and negative
    subpattern, for example, `".,..0.00;(.,..0.00)"`.  Each
    subpattern has a prefix, numeric part, and suffix. The negative subpattern
    is optional; if absent, then the positive subpattern prefixed with the
    minus sign (`'-' U+002D HYPHEN-MINUS`) is used as the
    negative subpattern. That is, `"0.00"` alone is equivalent to
    `"0.00;-0.00"`.  If there is an explicit negative subpattern, it
    serves only to specify the negative prefix and suffix; the number of digits,
    minimal digits, and other characteristics are all the same as the positive
    pattern. That means that `".,..0.0.;(.)"` produces precisely
    the same behavior as `".,..0.0.;(.,..0.0.)"`.
    
    The prefixes, suffixes, and various symbols used for infinity, digits,
    grouping separators, decimal separators, etc. may be set to arbitrary
    values, and they will appear properly during formatting.  However, care must
    be taken that the symbols and strings do not conflict, or parsing will be
    unreliable.  For example, either the positive and negative prefixes or the
    suffixes must be distinct for `DecimalFormat.parse()` to be able
    to distinguish positive from negative values.  (If they are identical, then
    `DecimalFormat` will behave as if no negative subpattern was
    specified.)  Another example is that the decimal separator and grouping
    separator should be distinct characters, or parsing will be impossible.
    
    The grouping separator is commonly used for thousands, but in some
    countries it separates ten-thousands. The grouping size is a constant number
    of digits between the grouping characters, such as 3 for 100,000,000 or 4 for
    1,0000,0000.  If you supply a pattern with multiple grouping characters, the
    interval between the last one and the end of the integer is the one that is
    used. So `".,..,...,...."` == `"......,...."` ==
    `"..,....,...."`.
    
    <h3><a id="special_pattern_character">Special Pattern Characters</a></h3>
    
    Many characters in a pattern are taken literally; they are matched during
    parsing and output unchanged during formatting.  Special characters, on the
    other hand, stand for other characters, strings, or classes of characters.
    They must be quoted, unless noted otherwise, if they are to appear in the
    prefix or suffix as literals.
    
    The characters listed here are used in non-localized patterns.  Localized
    patterns use the corresponding characters taken from this formatter's
    `DecimalFormatSymbols` object instead, and these characters lose
    their special status.  Two exceptions are the currency sign and quote, which
    are not localized.
    
    <blockquote>
    <table class="striped">
    <caption style="display:none">Chart showing symbol, location, localized, and meaning.</caption>
    <thead>
        <tr>
             <th scope="col" style="text-align:left">Symbol
             <th scope="col" style="text-align:left">Location
             <th scope="col" style="text-align:left">Localized?
             <th scope="col" style="text-align:left">Meaning
    </thead>
    <tbody>
        <tr style="vertical-align:top">
             <th scope="row">`0`
             <td>Number
             <td>Yes
             <td>Digit
        <tr style="vertical-align: top">
             <th scope="row">`.`
             <td>Number
             <td>Yes
             <td>Digit, zero shows as absent
        <tr style="vertical-align:top">
             <th scope="row">`.`
             <td>Number
             <td>Yes
             <td>Decimal separator or monetary decimal separator
        <tr style="vertical-align: top">
             <th scope="row">`-`
             <td>Number
             <td>Yes
             <td>Minus sign
        <tr style="vertical-align:top">
             <th scope="row">`,`
             <td>Number
             <td>Yes
             <td>Grouping separator or monetary grouping separator
        <tr style="vertical-align: top">
             <th scope="row">`E`
             <td>Number
             <td>Yes
             <td>Separates mantissa and exponent in scientific notation.
                 *Need not be quoted in prefix or suffix.*
        <tr style="vertical-align:top">
             <th scope="row">`;`
             <td>Subpattern boundary
             <td>Yes
             <td>Separates positive and negative subpatterns
        <tr style="vertical-align: top">
             <th scope="row">`%`
             <td>Prefix or suffix
             <td>Yes
             <td>Multiply by 100 and show as percentage
        <tr style="vertical-align:top">
             <th scope="row">`&.92;u2030`
             <td>Prefix or suffix
             <td>Yes
             <td>Multiply by 1000 and show as per mille value
        <tr style="vertical-align: top">
             <th scope="row">`&.164;` (`&.92;u00A4`)
             <td>Prefix or suffix
             <td>No
             <td>Currency sign, replaced by currency symbol.  If
                 doubled, replaced by international currency symbol.
                 If present in a pattern, the monetary decimal/grouping separators
                 are used instead of the decimal/grouping separators.
        <tr style="vertical-align:top">
             <th scope="row">`'`
             <td>Prefix or suffix
             <td>No
             <td>Used to quote special characters in a prefix or suffix,
                 for example, `"'.'."` formats 123 to
                 `".123"`.  To create a single quote
                 itself, use two in a row: `". o''clock"`.
    </tbody>
    </table>
    </blockquote>
    
    <h3>Scientific Notation</h3>
    
    Numbers in scientific notation are expressed as the product of a mantissa
    and a power of ten, for example, 1234 can be expressed as 1.234 x 10^3.  The
    mantissa is often in the range 1.0 &le; x < 10.0, but it need not
    be.
    `DecimalFormat` can be instructed to format and parse scientific
    notation *only via a pattern*; there is currently no factory method
    that creates a scientific notation format.  In a pattern, the exponent
    character immediately followed by one or more digit characters indicates
    scientific notation.  Example: `"0....E0"` formats the number
    1234 as `"1.234E3"`.
    
    
    - The number of digit characters after the exponent character gives the
    minimum exponent digit count.  There is no maximum.  Negative exponents are
    formatted using the localized minus sign, *not* the prefix and suffix
    from the pattern.  This allows patterns such as `"0....E0 m/s"`.
    
    - The minimum and maximum number of integer digits are interpreted
    together:
    
    
    - If the maximum number of integer digits is greater than their minimum number
    and greater than 1, it forces the exponent to be a multiple of the maximum
    number of integer digits, and the minimum number of integer digits to be
    interpreted as 1.  The most common use of this is to generate
    *engineering notation*, in which the exponent is a multiple of three,
    e.g., `"..0......E0"`. Using this pattern, the number 12345
    formats to `"12.345E3"`, and 123456 formats to
    `"123.456E3"`.
    
    - Otherwise, the minimum number of integer digits is achieved by adjusting the
    exponent.  Example: 0.00123 formatted with `"00....E0"` yields
    `"12.3E-4"`.
    
    
    - The number of significant digits in the mantissa is the sum of the
    *minimum integer* and *maximum fraction* digits, and is
    unaffected by the maximum integer digits.  For example, 12345 formatted with
    `"..0...E0"` is `"12.3E3"`. To show all digits, set
    the significant digits count to zero.  The number of significant digits
    does not affect parsing.
    
    - Exponential patterns may not contain grouping separators.
    
    
    <h3>Rounding</h3>
    
    `DecimalFormat` provides rounding modes defined in
    java.math.RoundingMode for formatting.  By default, it uses
    java.math.RoundingMode.HALF_EVEN RoundingMode.HALF_EVEN.
    
    <h3>Digits</h3>
    
    For formatting, `DecimalFormat` uses the ten consecutive
    characters starting with the localized zero digit defined in the
    `DecimalFormatSymbols` object as digits. For parsing, these
    digits as well as all Unicode decimal digits, as defined by
    Character.digit Character.digit, are recognized.
    
    <h4>Special Values</h4>
    
    `NaN` is formatted as a string, which typically has a single character
    `&.92;uFFFD`.  This string is determined by the
    `DecimalFormatSymbols` object.  This is the only value for which
    the prefixes and suffixes are not used.
    
    Infinity is formatted as a string, which typically has a single character
    `&.92;u221E`, with the positive or negative prefixes and suffixes
    applied.  The infinity string is determined by the
    `DecimalFormatSymbols` object.
    
    Negative zero (`"-0"`) parses to
    
    - `BigDecimal(0)` if `isParseBigDecimal()` is
    True,
    - `Long(0)` if `isParseBigDecimal()` is False
        and `isParseIntegerOnly()` is True,
    - `Double(-0.0)` if both `isParseBigDecimal()`
    and `isParseIntegerOnly()` are False.
    
    
    <h3><a id="synchronization">Synchronization</a></h3>
    
    
    Decimal formats are generally not synchronized.
    It is recommended to create separate format instances for each thread.
    If multiple threads access a format concurrently, it must be synchronized
    externally.
    
    <h3>Example</h3>
    
    <blockquote>```<strong>`// Print out a number using the localized number, integer, currency,
    // and percent format for each locale`</strong>`Locale[] locales = NumberFormat.getAvailableLocales();
    double myNumber = -1234.56;
    NumberFormat form;
    for (int j = 0; j < 4; ++j) {
        System.out.println("FORMAT");
        for (int i = 0; i < locales.length; ++i) {
            if (locales[i].getCountry().length() == 0) {
               continue; // Skip language-only locales`
            System.out.print(locales[i].getDisplayName());
            switch (j) {
            case 0:
                form = NumberFormat.getInstance(locales[i]); break;
            case 1:
                form = NumberFormat.getIntegerInstance(locales[i]); break;
            case 2:
                form = NumberFormat.getCurrencyInstance(locales[i]); break;
            default:
                form = NumberFormat.getPercentInstance(locales[i]); break;
            }
            if (form instanceof DecimalFormat) {
                System.out.print(": " + ((DecimalFormat) form).toPattern());
            }
            System.out.print(" -> " + form.format(myNumber));
            try {
                System.out.println(" -> " + form.parse(form.format(myNumber)));
            } catch (ParseException e) {}
        }
    }
    }```</blockquote>

    Author(s)
    - Alan Liu

    See
    - ParsePosition

    Since
    - 1.1
    """

    def __init__(self):
        """
        Creates a DecimalFormat using the default pattern and symbols
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is a convenient way to obtain a
        DecimalFormat when internationalization is not the main concern.
        
        To obtain standard formats for a given locale, use the factory methods
        on NumberFormat such as getNumberInstance. These factories will
        return the most appropriate sub-class of NumberFormat for a given
        locale.

        See
        - java.text.NumberFormat.getPercentInstance
        """
        ...


    def __init__(self, pattern: str):
        """
        Creates a DecimalFormat using the given pattern and the symbols
        for the default java.util.Locale.Category.FORMAT FORMAT locale.
        This is a convenient way to obtain a
        DecimalFormat when internationalization is not the main concern.
        
        To obtain standard formats for a given locale, use the factory methods
        on NumberFormat such as getNumberInstance. These factories will
        return the most appropriate sub-class of NumberFormat for a given
        locale.

        Arguments
        - pattern: a non-localized pattern string.

        Raises
        - NullPointerException: if `pattern` is null
        - IllegalArgumentException: if the given pattern is invalid.

        See
        - java.text.NumberFormat.getPercentInstance
        """
        ...


    def __init__(self, pattern: str, symbols: "DecimalFormatSymbols"):
        """
        Creates a DecimalFormat using the given pattern and symbols.
        Use this constructor when you need to completely customize the
        behavior of the format.
        
        To obtain standard formats for a given
        locale, use the factory methods on NumberFormat such as
        getInstance or getCurrencyInstance. If you need only minor adjustments
        to a standard format, you can modify the format returned by
        a NumberFormat factory method.

        Arguments
        - pattern: a non-localized pattern string
        - symbols: the set of symbols to be used

        Raises
        - NullPointerException: if any of the given arguments is null
        - IllegalArgumentException: if the given pattern is invalid

        See
        - java.text.DecimalFormatSymbols
        """
        ...


    def format(self, number: "Object", toAppendTo: "StringBuffer", pos: "FieldPosition") -> "StringBuffer":
        """
        Formats a number and appends the resulting text to the given string
        buffer.
        The number can be of any subclass of java.lang.Number.
        
        This implementation uses the maximum precision permitted.

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


    def format(self, number: float, result: "StringBuffer", fieldPosition: "FieldPosition") -> "StringBuffer":
        """
        Formats a double to produce a string.

        Arguments
        - number: The double to format
        - result: where the text is to be appended
        - fieldPosition: keeps track on the position of the field within
                                the returned string. For example, for formatting
                                a number `1234567.89` in `Locale.US`
                                locale, if the given `fieldPosition` is
                                NumberFormat.INTEGER_FIELD, the begin index
                                and end index of `fieldPosition` will be set
                                to 0 and 9, respectively for the output string
                                `1,234,567.89`.

        Returns
        - The formatted number string

        Raises
        - NullPointerException: if `result` or
                   `fieldPosition` is `null`
        - ArithmeticException: if rounding is needed with rounding
                   mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.FieldPosition
        """
        ...


    def format(self, number: int, result: "StringBuffer", fieldPosition: "FieldPosition") -> "StringBuffer":
        """
        Format a long to produce a string.

        Arguments
        - number: The long to format
        - result: where the text is to be appended
        - fieldPosition: keeps track on the position of the field within
                                the returned string. For example, for formatting
                                a number `123456789` in `Locale.US`
                                locale, if the given `fieldPosition` is
                                NumberFormat.INTEGER_FIELD, the begin index
                                and end index of `fieldPosition` will be set
                                to 0 and 11, respectively for the output string
                                `123,456,789`.

        Returns
        - The formatted number string

        Raises
        - NullPointerException: if `result` or
                         `fieldPosition` is `null`
        - ArithmeticException: if rounding is needed with rounding
                         mode being set to RoundingMode.UNNECESSARY

        See
        - java.text.FieldPosition
        """
        ...


    def formatToCharacterIterator(self, obj: "Object") -> "AttributedCharacterIterator":
        """
        Formats an Object producing an `AttributedCharacterIterator`.
        You can use the returned `AttributedCharacterIterator`
        to build the resulting String, as well as to determine information
        about the resulting String.
        
        Each attribute key of the AttributedCharacterIterator will be of type
        `NumberFormat.Field`, with the attribute value being the
        same as the attribute key.

        Arguments
        - obj: The object to format

        Returns
        - AttributedCharacterIterator describing the formatted value.

        Raises
        - NullPointerException: if obj is null.
        - IllegalArgumentException: when the Format cannot format the
                   given object.
        - ArithmeticException: if rounding is needed with rounding
                          mode being set to RoundingMode.UNNECESSARY

        Since
        - 1.4
        """
        ...


    def parse(self, text: str, pos: "ParsePosition") -> "Number":
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
        
        The subclass returned depends on the value of .isParseBigDecimal
        as well as on the string being parsed.
        
          - If `isParseBigDecimal()` is False (the default),
              most integer values are returned as `Long`
              objects, no matter how they are written: `"17"` and
              `"17.000"` both parse to `Long(17)`.
              Values that cannot fit into a `Long` are returned as
              `Double`s. This includes values with a fractional part,
              infinite values, `NaN`, and the value -0.0.
              `DecimalFormat` does *not* decide whether to
              return a `Double` or a `Long` based on the
              presence of a decimal separator in the source string. Doing so
              would prevent integers that overflow the mantissa of a double,
              such as `"-9,223,372,036,854,775,808.00"`, from being
              parsed accurately.
              
              Callers may use the `Number` methods
              `doubleValue`, `longValue`, etc., to obtain
              the type they want.
          - If `isParseBigDecimal()` is True, values are returned
              as `BigDecimal` objects. The values are the ones
              constructed by java.math.BigDecimal.BigDecimal(String)
              for corresponding strings in locale-independent format. The
              special cases negative and positive infinity and NaN are returned
              as `Double` instances holding the values of the
              corresponding `Double` constants.
        
        
        `DecimalFormat` parses all Unicode characters that represent
        decimal digits, as defined by `Character.digit()`. In
        addition, `DecimalFormat` also recognizes as digits the ten
        consecutive characters starting with the localized zero digit defined in
        the `DecimalFormatSymbols` object.

        Arguments
        - text: the string to be parsed
        - pos: A `ParsePosition` object with index and error
                    index information as described above.

        Returns
        - the parsed value, or `null` if the parse fails

        Raises
        - NullPointerException: if `text` or
                    `pos` is null.
        """
        ...


    def getDecimalFormatSymbols(self) -> "DecimalFormatSymbols":
        """
        Returns a copy of the decimal format symbols, which is generally not
        changed by the programmer or user.

        Returns
        - a copy of the desired DecimalFormatSymbols

        See
        - java.text.DecimalFormatSymbols
        """
        ...


    def setDecimalFormatSymbols(self, newSymbols: "DecimalFormatSymbols") -> None:
        """
        Sets the decimal format symbols, which is generally not changed
        by the programmer or user.

        Arguments
        - newSymbols: desired DecimalFormatSymbols

        See
        - java.text.DecimalFormatSymbols
        """
        ...


    def getPositivePrefix(self) -> str:
        """
        Get the positive prefix.
        <P>Examples: +123, $123, sFr123

        Returns
        - the positive prefix
        """
        ...


    def setPositivePrefix(self, newValue: str) -> None:
        """
        Set the positive prefix.
        <P>Examples: +123, $123, sFr123

        Arguments
        - newValue: the new positive prefix
        """
        ...


    def getNegativePrefix(self) -> str:
        """
        Get the negative prefix.
        <P>Examples: -123, ($123) (with negative suffix), sFr-123

        Returns
        - the negative prefix
        """
        ...


    def setNegativePrefix(self, newValue: str) -> None:
        """
        Set the negative prefix.
        <P>Examples: -123, ($123) (with negative suffix), sFr-123

        Arguments
        - newValue: the new negative prefix
        """
        ...


    def getPositiveSuffix(self) -> str:
        """
        Get the positive suffix.
        <P>Example: 123%

        Returns
        - the positive suffix
        """
        ...


    def setPositiveSuffix(self, newValue: str) -> None:
        """
        Set the positive suffix.
        <P>Example: 123%

        Arguments
        - newValue: the new positive suffix
        """
        ...


    def getNegativeSuffix(self) -> str:
        """
        Get the negative suffix.
        <P>Examples: -123%, ($123) (with positive suffixes)

        Returns
        - the negative suffix
        """
        ...


    def setNegativeSuffix(self, newValue: str) -> None:
        """
        Set the negative suffix.
        <P>Examples: 123%

        Arguments
        - newValue: the new negative suffix
        """
        ...


    def getMultiplier(self) -> int:
        """
        Gets the multiplier for use in percent, per mille, and similar
        formats.

        Returns
        - the multiplier

        See
        - .setMultiplier(int)
        """
        ...


    def setMultiplier(self, newValue: int) -> None:
        """
        Sets the multiplier for use in percent, per mille, and similar
        formats.
        For a percent format, set the multiplier to 100 and the suffixes to
        have '%' (for Arabic, use the Arabic percent sign).
        For a per mille format, set the multiplier to 1000 and the suffixes to
        have '&#92;u2030'.
        
        <P>Example: with multiplier 100, 1.23 is formatted as "123", and
        "123" is parsed into 1.23.

        Arguments
        - newValue: the new multiplier

        See
        - .getMultiplier
        """
        ...


    def setGroupingUsed(self, newValue: bool) -> None:
        """

        """
        ...


    def getGroupingSize(self) -> int:
        """
        Return the grouping size. Grouping size is the number of digits between
        grouping separators in the integer portion of a number.  For example,
        in the number "123,456.78", the grouping size is 3. Grouping size of
        zero designates that grouping is not used, which provides the same
        formatting as if calling .setGroupingUsed(boolean)
        setGroupingUsed(False).

        Returns
        - the grouping size

        See
        - java.text.DecimalFormatSymbols.getGroupingSeparator
        """
        ...


    def setGroupingSize(self, newValue: int) -> None:
        """
        Set the grouping size. Grouping size is the number of digits between
        grouping separators in the integer portion of a number.  For example,
        in the number "123,456.78", the grouping size is 3. Grouping size of
        zero designates that grouping is not used, which provides the same
        formatting as if calling .setGroupingUsed(boolean)
        setGroupingUsed(False).
        
        The value passed in is converted to a byte, which may lose information.
        Values that are negative or greater than
        java.lang.Byte.MAX_VALUE Byte.MAX_VALUE, will throw an
        `IllegalArgumentException`.

        Arguments
        - newValue: the new grouping size

        Raises
        - IllegalArgumentException: if `newValue` is negative or
                 greater than java.lang.Byte.MAX_VALUE Byte.MAX_VALUE

        See
        - java.text.DecimalFormatSymbols.setGroupingSeparator
        """
        ...


    def isDecimalSeparatorAlwaysShown(self) -> bool:
        """
        Allows you to get the behavior of the decimal separator with integers.
        (The decimal separator will always appear with decimals.)
        <P>Example: Decimal ON: 12345 &rarr; 12345.; OFF: 12345 &rarr; 12345

        Returns
        - `True` if the decimal separator is always shown;
                `False` otherwise
        """
        ...


    def setDecimalSeparatorAlwaysShown(self, newValue: bool) -> None:
        """
        Allows you to set the behavior of the decimal separator with integers.
        (The decimal separator will always appear with decimals.)
        <P>Example: Decimal ON: 12345 &rarr; 12345.; OFF: 12345 &rarr; 12345

        Arguments
        - newValue: `True` if the decimal separator is always shown;
                        `False` otherwise
        """
        ...


    def isParseBigDecimal(self) -> bool:
        """
        Returns whether the .parse(java.lang.String, java.text.ParsePosition)
        method returns `BigDecimal`. The default value is False.

        Returns
        - `True` if the parse method returns BigDecimal;
                `False` otherwise

        See
        - .setParseBigDecimal

        Since
        - 1.5
        """
        ...


    def setParseBigDecimal(self, newValue: bool) -> None:
        """
        Sets whether the .parse(java.lang.String, java.text.ParsePosition)
        method returns `BigDecimal`.

        Arguments
        - newValue: `True` if the parse method returns BigDecimal;
                        `False` otherwise

        See
        - .isParseBigDecimal

        Since
        - 1.5
        """
        ...


    def clone(self) -> "Object":
        """
        Standard override; no change in semantics.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Overrides equals
        """
        ...


    def hashCode(self) -> int:
        """
        Overrides hashCode
        """
        ...


    def toPattern(self) -> str:
        """
        Synthesizes a pattern string that represents the current state
        of this Format object.

        Returns
        - a pattern string

        See
        - .applyPattern
        """
        ...


    def toLocalizedPattern(self) -> str:
        """
        Synthesizes a localized pattern string that represents the current
        state of this Format object.

        Returns
        - a localized pattern string

        See
        - .applyPattern
        """
        ...


    def applyPattern(self, pattern: str) -> None:
        """
        Apply the given pattern to this Format object.  A pattern is a
        short-hand specification for the various formatting properties.
        These properties can also be changed individually through the
        various setter methods.
        
        There is no limit to integer digits set
        by this routine, since that is the typical end-user desire;
        use setMaximumInteger if you want to set a real value.
        For negative numbers, use a second pattern, separated by a semicolon
        <P>Example `".,.00.0."` &rarr; 1,234.56
        <P>This means a minimum of 2 integer digits, 1 fraction digit, and
        a maximum of 2 fraction digits.
        Example: `".,.00.0.;(.,.00.0.)"` for negatives in
        parentheses.
        In negative patterns, the minimum and maximum counts are ignored;
        these are presumed to be set in the positive pattern.

        Arguments
        - pattern: a new pattern

        Raises
        - NullPointerException: if `pattern` is null
        - IllegalArgumentException: if the given pattern is invalid.
        """
        ...


    def applyLocalizedPattern(self, pattern: str) -> None:
        """
        Apply the given pattern to this Format object.  The pattern
        is assumed to be in a localized notation. A pattern is a
        short-hand specification for the various formatting properties.
        These properties can also be changed individually through the
        various setter methods.
        
        There is no limit to integer digits set
        by this routine, since that is the typical end-user desire;
        use setMaximumInteger if you want to set a real value.
        For negative numbers, use a second pattern, separated by a semicolon
        <P>Example `".,.00.0."` &rarr; 1,234.56
        <P>This means a minimum of 2 integer digits, 1 fraction digit, and
        a maximum of 2 fraction digits.
        Example: `".,.00.0.;(.,.00.0.)"` for negatives in
        parentheses.
        In negative patterns, the minimum and maximum counts are ignored;
        these are presumed to be set in the positive pattern.

        Arguments
        - pattern: a new pattern

        Raises
        - NullPointerException: if `pattern` is null
        - IllegalArgumentException: if the given pattern is invalid.
        """
        ...


    def setMaximumIntegerDigits(self, newValue: int) -> None:
        """
        Sets the maximum number of digits allowed in the integer portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of `newValue` and
        309 is used. Negative input values are replaced with 0.

        See
        - NumberFormat.setMaximumIntegerDigits
        """
        ...


    def setMinimumIntegerDigits(self, newValue: int) -> None:
        """
        Sets the minimum number of digits allowed in the integer portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of `newValue` and
        309 is used. Negative input values are replaced with 0.

        See
        - NumberFormat.setMinimumIntegerDigits
        """
        ...


    def setMaximumFractionDigits(self, newValue: int) -> None:
        """
        Sets the maximum number of digits allowed in the fraction portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of `newValue` and
        340 is used. Negative input values are replaced with 0.

        See
        - NumberFormat.setMaximumFractionDigits
        """
        ...


    def setMinimumFractionDigits(self, newValue: int) -> None:
        """
        Sets the minimum number of digits allowed in the fraction portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of `newValue` and
        340 is used. Negative input values are replaced with 0.

        See
        - NumberFormat.setMinimumFractionDigits
        """
        ...


    def getMaximumIntegerDigits(self) -> int:
        """
        Gets the maximum number of digits allowed in the integer portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of the return value and
        309 is used.

        See
        - .setMaximumIntegerDigits
        """
        ...


    def getMinimumIntegerDigits(self) -> int:
        """
        Gets the minimum number of digits allowed in the integer portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of the return value and
        309 is used.

        See
        - .setMinimumIntegerDigits
        """
        ...


    def getMaximumFractionDigits(self) -> int:
        """
        Gets the maximum number of digits allowed in the fraction portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of the return value and
        340 is used.

        See
        - .setMaximumFractionDigits
        """
        ...


    def getMinimumFractionDigits(self) -> int:
        """
        Gets the minimum number of digits allowed in the fraction portion of a
        number.
        For formatting numbers other than `BigInteger` and
        `BigDecimal` objects, the lower of the return value and
        340 is used.

        See
        - .setMinimumFractionDigits
        """
        ...


    def getCurrency(self) -> "Currency":
        """
        Gets the currency used by this decimal format when formatting
        currency values.
        The currency is obtained by calling
        DecimalFormatSymbols.getCurrency DecimalFormatSymbols.getCurrency
        on this number format's symbols.

        Returns
        - the currency used by this decimal format, or `null`

        Since
        - 1.4
        """
        ...


    def setCurrency(self, currency: "Currency") -> None:
        """
        Sets the currency used by this number format when formatting
        currency values. This does not update the minimum or maximum
        number of fraction digits used by the number format.
        The currency is set by calling
        DecimalFormatSymbols.setCurrency DecimalFormatSymbols.setCurrency
        on this number format's symbols.

        Arguments
        - currency: the new currency to be used by this decimal format

        Raises
        - NullPointerException: if `currency` is null

        Since
        - 1.4
        """
        ...


    def getRoundingMode(self) -> "RoundingMode":
        """
        Gets the java.math.RoundingMode used in this DecimalFormat.

        Returns
        - The `RoundingMode` used for this DecimalFormat.

        See
        - .setRoundingMode(RoundingMode)

        Since
        - 1.6
        """
        ...


    def setRoundingMode(self, roundingMode: "RoundingMode") -> None:
        """
        Sets the java.math.RoundingMode used in this DecimalFormat.

        Arguments
        - roundingMode: The `RoundingMode` to be used

        Raises
        - NullPointerException: if `roundingMode` is null.

        See
        - .getRoundingMode()

        Since
        - 1.6
        """
        ...
