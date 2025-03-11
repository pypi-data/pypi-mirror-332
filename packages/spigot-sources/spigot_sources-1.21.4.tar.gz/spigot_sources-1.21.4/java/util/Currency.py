"""
Python module generated from Java source file java.util.Currency

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import BufferedInputStream
from java.io import DataInputStream
from java.io import File
from java.io import FileReader
from java.io import IOException
from java.io import InputStream
from java.io import Serializable
from java.security import AccessController
from java.security import PrivilegedAction
from java.text import ParseException
from java.text import SimpleDateFormat
from java.util import *
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.regex import Matcher
from java.util.regex import Pattern
from java.util.spi import CurrencyNameProvider
from java.util.stream import Collectors
from jdk.internal.util import StaticProperty
from sun.util.locale.provider import CalendarDataUtility
from sun.util.locale.provider import LocaleServiceProviderPool
from sun.util.logging import PlatformLogger
from typing import Any, Callable, Iterable, Tuple


class Currency(Serializable):
    """
    Represents a currency. Currencies are identified by their ISO 4217 currency
    codes. Visit the <a href="http://www.iso.org/iso/home/standards/currency_codes.htm">
    ISO web site</a> for more information.
    
    The class is designed so that there's never more than one
    `Currency` instance for any given currency. Therefore, there's
    no public constructor. You obtain a `Currency` instance using
    the `getInstance` methods.
    
    Users can supersede the Java runtime currency data by means of the system
    property java.util.currency.data. If this system property is
    defined then its value is the location of a properties file, the contents of
    which are key/value pairs of the ISO 3166 country codes and the ISO 4217
    currency data respectively.  The value part consists of three ISO 4217 values
    of a currency, i.e., an alphabetic code, a numeric code, and a minor unit.
    Those three ISO 4217 values are separated by commas.
    The lines which start with '#'s are considered comment lines. An optional UTC
    timestamp may be specified per currency entry if users need to specify a
    cutover date indicating when the new data comes into effect. The timestamp is
    appended to the end of the currency properties and uses a comma as a separator.
    If a UTC datestamp is present and valid, the JRE will only use the new currency
    properties if the current UTC date is later than the date specified at class
    loading time. The format of the timestamp must be of ISO 8601 format :
    `'yyyy-MM-dd'T'HH:mm:ss'`. For example,
    
    `
    #Sample currency properties
    JP=JPZ,999,0
    `
    
    will supersede the currency data for Japan. If JPZ is one of the existing
    ISO 4217 currency code referred by other countries, the existing
    JPZ currency data is updated with the given numeric code and minor
    unit value.
    
    
    `
    #Sample currency properties with cutover date
    JP=JPZ,999,0,2014-01-01T00:00:00
    `
    
    will supersede the currency data for Japan if `Currency` class is loaded after
    1st January 2014 00:00:00 GMT.
    
    Where syntactically malformed entries are encountered, the entry is ignored
    and the remainder of entries in file are processed. For instances where duplicate
    country code entries exist, the behavior of the Currency information for that
    `Currency` is undefined and the remainder of entries in file are processed.
    
    If multiple property entries with same currency code but different numeric code
    and/or minor unit are encountered, those entries are ignored and the remainder
    of entries in file are processed.
    
    
    It is recommended to use java.math.BigDecimal class while dealing
    with `Currency` or monetary values as it provides better handling of floating
    point numbers and their operations.

    See
    - java.math.BigDecimal

    Since
    - 1.4
    """

    @staticmethod
    def getInstance(currencyCode: str) -> "Currency":
        """
        Returns the `Currency` instance for the given currency code.

        Arguments
        - currencyCode: the ISO 4217 code of the currency

        Returns
        - the `Currency` instance for the given currency code

        Raises
        - NullPointerException: if `currencyCode` is null
        - IllegalArgumentException: if `currencyCode` is not
        a supported ISO 4217 code.
        """
        ...


    @staticmethod
    def getInstance(locale: "Locale") -> "Currency":
        """
        Returns the `Currency` instance for the country of the
        given locale. The language and variant components of the locale
        are ignored. The result may vary over time, as countries change their
        currencies. For example, for the original member countries of the
        European Monetary Union, the method returns the old national currencies
        until December 31, 2001, and the Euro from January 1, 2002, local time
        of the respective countries.
        
        If the specified `locale` contains "cu" and/or "rg"
        <a href="./Locale.html#def_locale_extension">Unicode extensions</a>,
        the instance returned from this method reflects
        the values specified with those extensions. If both "cu" and "rg" are
        specified, the currency from the "cu" extension supersedes the implicit one
        from the "rg" extension.
        
        The method returns `null` for territories that don't
        have a currency, such as Antarctica.

        Arguments
        - locale: the locale for whose country a `Currency`
        instance is needed

        Returns
        - the `Currency` instance for the country of the given
        locale, or `null`

        Raises
        - NullPointerException: if `locale`
        is `null`
        - IllegalArgumentException: if the country of the given `locale`
        is not a supported ISO 3166 country code.
        """
        ...


    @staticmethod
    def getAvailableCurrencies() -> set["Currency"]:
        """
        Gets the set of available currencies.  The returned set of currencies
        contains all of the available currencies, which may include currencies
        that represent obsolete ISO 4217 codes.  The set can be modified
        without affecting the available currencies in the runtime.

        Returns
        - the set of available currencies.  If there is no currency
           available in the runtime, the returned set is empty.

        Since
        - 1.7
        """
        ...


    def getCurrencyCode(self) -> str:
        """
        Gets the ISO 4217 currency code of this currency.

        Returns
        - the ISO 4217 currency code of this currency.
        """
        ...


    def getSymbol(self) -> str:
        """
        Gets the symbol of this currency for the default
        Locale.Category.DISPLAY DISPLAY locale.
        For example, for the US Dollar, the symbol is "$" if the default
        locale is the US, while for other locales it may be "US$". If no
        symbol can be determined, the ISO 4217 currency code is returned.
        
        If the default Locale.Category.DISPLAY DISPLAY locale
        contains "rg" (region override)
        <a href="./Locale.html#def_locale_extension">Unicode extension</a>,
        the symbol returned from this method reflects
        the value specified with that extension.
        
        This is equivalent to calling
        .getSymbol(Locale)
            getSymbol(Locale.getDefault(Locale.Category.DISPLAY)).

        Returns
        - the symbol of this currency for the default
            Locale.Category.DISPLAY DISPLAY locale
        """
        ...


    def getSymbol(self, locale: "Locale") -> str:
        """
        Gets the symbol of this currency for the specified locale.
        For example, for the US Dollar, the symbol is "$" if the specified
        locale is the US, while for other locales it may be "US$". If no
        symbol can be determined, the ISO 4217 currency code is returned.
        
        If the specified `locale` contains "rg" (region override)
        <a href="./Locale.html#def_locale_extension">Unicode extension</a>,
        the symbol returned from this method reflects
        the value specified with that extension.

        Arguments
        - locale: the locale for which a display name for this currency is
        needed

        Returns
        - the symbol of this currency for the specified locale

        Raises
        - NullPointerException: if `locale` is null
        """
        ...


    def getDefaultFractionDigits(self) -> int:
        """
        Gets the default number of fraction digits used with this currency.
        Note that the number of fraction digits is the same as ISO 4217's
        minor unit for the currency.
        For example, the default number of fraction digits for the Euro is 2,
        while for the Japanese Yen it's 0.
        In the case of pseudo-currencies, such as IMF Special Drawing Rights,
        -1 is returned.

        Returns
        - the default number of fraction digits used with this currency
        """
        ...


    def getNumericCode(self) -> int:
        """
        Returns the ISO 4217 numeric code of this currency.

        Returns
        - the ISO 4217 numeric code of this currency

        Since
        - 1.7
        """
        ...


    def getNumericCodeAsString(self) -> str:
        """
        Returns the 3 digit ISO 4217 numeric code of this currency as a `String`.
        Unlike .getNumericCode(), which returns the numeric code as `int`,
        this method always returns the numeric code as a 3 digit string.
        e.g. a numeric value of 32 would be returned as "032",
        and a numeric value of 6 would be returned as "006".

        Returns
        - the 3 digit ISO 4217 numeric code of this currency as a `String`

        Since
        - 9
        """
        ...


    def getDisplayName(self) -> str:
        """
        Gets the name that is suitable for displaying this currency for
        the default Locale.Category.DISPLAY DISPLAY locale.
        If there is no suitable display name found
        for the default locale, the ISO 4217 currency code is returned.
        
        This is equivalent to calling
        .getDisplayName(Locale)
            getDisplayName(Locale.getDefault(Locale.Category.DISPLAY)).

        Returns
        - the display name of this currency for the default
            Locale.Category.DISPLAY DISPLAY locale

        Since
        - 1.7
        """
        ...


    def getDisplayName(self, locale: "Locale") -> str:
        """
        Gets the name that is suitable for displaying this currency for
        the specified locale.  If there is no suitable display name found
        for the specified locale, the ISO 4217 currency code is returned.

        Arguments
        - locale: the locale for which a display name for this currency is
        needed

        Returns
        - the display name of this currency for the specified locale

        Raises
        - NullPointerException: if `locale` is null

        Since
        - 1.7
        """
        ...


    def toString(self) -> str:
        """
        Returns the ISO 4217 currency code of this currency.

        Returns
        - the ISO 4217 currency code of this currency
        """
        ...
