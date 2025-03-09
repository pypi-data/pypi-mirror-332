"""
Python module generated from Java source file java.util.Locale

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamField
from java.io import Serializable
from java.text import MessageFormat
from java.util import *
from java.util.concurrent import ConcurrentHashMap
from java.util.spi import LocaleNameProvider
from java.util.stream import Collectors
from sun.security.action import GetPropertyAction
from sun.util.locale import BaseLocale
from sun.util.locale import InternalLocaleBuilder
from sun.util.locale import LanguageTag
from sun.util.locale import LocaleExtensions
from sun.util.locale import LocaleMatcher
from sun.util.locale import LocaleObjectCache
from sun.util.locale import LocaleSyntaxException
from sun.util.locale import LocaleUtils
from sun.util.locale import ParseStatus
from sun.util.locale.provider import LocaleProviderAdapter
from sun.util.locale.provider import LocaleResources
from sun.util.locale.provider import LocaleServiceProviderPool
from sun.util.locale.provider import TimeZoneNameUtility
from typing import Any, Callable, Iterable, Tuple


class Locale(Cloneable, Serializable):
    """
    A `Locale` object represents a specific geographical, political,
    or cultural region. An operation that requires a `Locale` to perform
    its task is called *locale-sensitive* and uses the `Locale`
    to tailor information for the user. For example, displaying a number
    is a locale-sensitive operation&mdash; the number should be formatted
    according to the customs and conventions of the user's native country,
    region, or culture.
    
     The `Locale` class implements IETF BCP 47 which is composed of
    <a href="http://tools.ietf.org/html/rfc4647">RFC 4647 "Matching of Language
    Tags"</a> and <a href="http://tools.ietf.org/html/rfc5646">RFC 5646 "Tags
    for Identifying Languages"</a> with support for the LDML (UTS#35, "Unicode
    Locale Data Markup Language") BCP 47-compatible extensions for locale data
    exchange.
    
     A `Locale` object logically consists of the fields
    described below.
    
    <dl>
      <dt><a id="def_language">**language**</a></dt>
    
      <dd>ISO 639 alpha-2 or alpha-3 language code, or registered
      language subtags up to 8 alpha letters (for future enhancements).
      When a language has both an alpha-2 code and an alpha-3 code, the
      alpha-2 code must be used.  You can find a full list of valid
      language codes in the IANA Language Subtag Registry (search for
      "Type: language").  The language field is case insensitive, but
      `Locale` always canonicalizes to lower case.</dd>
    
      <dd>Well-formed language values have the form
      `[a-zA-Z]{2,8}`.  Note that this is not the full
      BCP47 language production, since it excludes extlang.  They are
      not needed since modern three-letter language codes replace
      them.</dd>
    
      <dd>Example: "en" (English), "ja" (Japanese), "kok" (Konkani)</dd>
    
      <dt><a id="def_script">**script**</a></dt>
    
      <dd>ISO 15924 alpha-4 script code.  You can find a full list of
      valid script codes in the IANA Language Subtag Registry (search
      for "Type: script").  The script field is case insensitive, but
      `Locale` always canonicalizes to title case (the first
      letter is upper case and the rest of the letters are lower
      case).</dd>
    
      <dd>Well-formed script values have the form
      `[a-zA-Z]{4}`</dd>
    
      <dd>Example: "Latn" (Latin), "Cyrl" (Cyrillic)</dd>
    
      <dt><a id="def_region">**country (region)**</a></dt>
    
      <dd>ISO 3166 alpha-2 country code or UN M.49 numeric-3 area code.
      You can find a full list of valid country and region codes in the
      IANA Language Subtag Registry (search for "Type: region").  The
      country (region) field is case insensitive, but
      `Locale` always canonicalizes to upper case.</dd>
    
      <dd>Well-formed country/region values have
      the form `[a-zA-Z]{2} | [0-9]{3}`</dd>
    
      <dd>Example: "US" (United States), "FR" (France), "029"
      (Caribbean)</dd>
    
      <dt><a id="def_variant">**variant**</a></dt>
    
      <dd>Any arbitrary value used to indicate a variation of a
      `Locale`.  Where there are two or more variant values
      each indicating its own semantics, these values should be ordered
      by importance, with most important first, separated by
      underscore('_').  The variant field is case sensitive.</dd>
    
      <dd>Note: IETF BCP 47 places syntactic restrictions on variant
      subtags.  Also BCP 47 subtags are strictly used to indicate
      additional variations that define a language or its dialects that
      are not covered by any combinations of language, script and
      region subtags.  You can find a full list of valid variant codes
      in the IANA Language Subtag Registry (search for "Type: variant").
    
      However, the variant field in `Locale` has
      historically been used for any kind of variation, not just
      language variations.  For example, some supported variants
      available in Java SE Runtime Environments indicate alternative
      cultural behaviors such as calendar type or number script.  In
      BCP 47 this kind of information, which does not identify the
      language, is supported by extension subtags or private use
      subtags.</dd>
    
      <dd>Well-formed variant values have the form `SUBTAG
      (('_'|'-') SUBTAG)*` where `SUBTAG =
      [0-9][0-9a-zA-Z]{3} | [0-9a-zA-Z]{5,8}`. (Note: BCP 47 only
      uses hyphen ('-') as a delimiter, this is more lenient).</dd>
    
      <dd>Example: "polyton" (Polytonic Greek), "POSIX"</dd>
    
      <dt><a id="def_extensions">**extensions**</a></dt>
    
      <dd>A map from single character keys to string values, indicating
      extensions apart from language identification.  The extensions in
      `Locale` implement the semantics and syntax of BCP 47
      extension subtags and private use subtags. The extensions are
      case insensitive, but `Locale` canonicalizes all
      extension keys and values to lower case. Note that extensions
      cannot have empty values.</dd>
    
      <dd>Well-formed keys are single characters from the set
      `[0-9a-zA-Z]`.  Well-formed values have the form
      `SUBTAG ('-' SUBTAG)*` where for the key 'x'
      `SUBTAG = [0-9a-zA-Z]{1,8}` and for other keys
      `SUBTAG = [0-9a-zA-Z]{2,8}` (that is, 'x' allows
      single-character subtags).</dd>
    
      <dd>Example: key="u"/value="ca-japanese" (Japanese Calendar),
      key="x"/value="java-1-7"</dd>
    </dl>
    
    **Note:** Although BCP 47 requires field values to be registered
    in the IANA Language Subtag Registry, the `Locale` class
    does not provide any validation features.  The `Builder`
    only checks if an individual field satisfies the syntactic
    requirement (is well-formed), but does not validate the value
    itself.  See Builder for details.
    
    <h2><a id="def_locale_extension">Unicode locale/language extension</a></h2>
    
    UTS#35, "Unicode Locale Data Markup Language" defines optional
    attributes and keywords to override or refine the default behavior
    associated with a locale.  A keyword is represented by a pair of
    key and type.  For example, "nu-thai" indicates that Thai local
    digits (value:"thai") should be used for formatting numbers
    (key:"nu").
    
    The keywords are mapped to a BCP 47 extension value using the
    extension key 'u' (.UNICODE_LOCALE_EXTENSION).  The above
    example, "nu-thai", becomes the extension "u-nu-thai".
    
    Thus, when a `Locale` object contains Unicode locale
    attributes and keywords,
    `getExtension(UNICODE_LOCALE_EXTENSION)` will return a
    String representing this information, for example, "nu-thai".  The
    `Locale` class also provides .getUnicodeLocaleAttributes, .getUnicodeLocaleKeys, and
    .getUnicodeLocaleType which allow you to access Unicode
    locale attributes and key/type pairs directly.  When represented as
    a string, the Unicode Locale Extension lists attributes
    alphabetically, followed by key/type sequences with keys listed
    alphabetically (the order of subtags comprising a key's type is
    fixed when the type is defined)
    
    A well-formed locale key has the form
    `[0-9a-zA-Z]{2}`.  A well-formed locale type has the
    form `"" | [0-9a-zA-Z]{3,8} ('-' [0-9a-zA-Z]{3,8})*` (it
    can be empty, or a series of subtags 3-8 alphanums in length).  A
    well-formed locale attribute has the form
    `[0-9a-zA-Z]{3,8}` (it is a single subtag with the same
    form as a locale type subtag).
    
    The Unicode locale extension specifies optional behavior in
    locale-sensitive services.  Although the LDML specification defines
    various keys and values, actual locale-sensitive service
    implementations in a Java Runtime Environment might not support any
    particular Unicode locale attributes or key/type pairs.
    
    <h3>Creating a Locale</h3>
    
    There are several different ways to create a `Locale`
    object.
    
    <h4>Builder</h4>
    
    Using Builder you can construct a `Locale` object
    that conforms to BCP 47 syntax.
    
    <h4>Constructors</h4>
    
    The `Locale` class provides three constructors:
    <blockquote>
    ```
        .Locale(String language)
        .Locale(String language, String country)
        .Locale(String language, String country, String variant)
    ```
    </blockquote>
    These constructors allow you to create a `Locale` object
    with language, country and variant, but you cannot specify
    script or extensions.
    
    <h4>Factory Methods</h4>
    
    The method .forLanguageTag creates a `Locale`
    object for a well-formed BCP 47 language tag.
    
    <h4>Locale Constants</h4>
    
    The `Locale` class provides a number of convenient constants
    that you can use to create `Locale` objects for commonly used
    locales. For example, the following creates a `Locale` object
    for the United States:
    <blockquote>
    ```
        Locale.US
    ```
    </blockquote>
    
    <h3><a id="LocaleMatching">Locale Matching</a></h3>
    
    If an application or a system is internationalized and provides localized
    resources for multiple locales, it sometimes needs to find one or more
    locales (or language tags) which meet each user's specific preferences. Note
    that a term "language tag" is used interchangeably with "locale" in this
    locale matching documentation.
    
    In order to do matching a user's preferred locales to a set of language
    tags, <a href="http://tools.ietf.org/html/rfc4647">RFC 4647 Matching of
    Language Tags</a> defines two mechanisms: filtering and lookup.
    *Filtering* is used to get all matching locales, whereas
    *lookup* is to choose the best matching locale.
    Matching is done case-insensitively. These matching mechanisms are described
    in the following sections.
    
    A user's preference is called a *Language Priority List* and is
    expressed as a list of language ranges. There are syntactically two types of
    language ranges: basic and extended. See
    Locale.LanguageRange Locale.LanguageRange for details.
    
    <h4>Filtering</h4>
    
    The filtering operation returns all matching language tags. It is defined
    in RFC 4647 as follows:
    "In filtering, each language range represents the least specific language
    tag (that is, the language tag with fewest number of subtags) that is an
    acceptable match. All of the language tags in the matching set of tags will
    have an equal or greater number of subtags than the language range. Every
    non-wildcard subtag in the language range will appear in every one of the
    matching language tags."
    
    There are two types of filtering: filtering for basic language ranges
    (called "basic filtering") and filtering for extended language ranges
    (called "extended filtering"). They may return different results by what
    kind of language ranges are included in the given Language Priority List.
    Locale.FilteringMode is a parameter to specify how filtering should
    be done.
    
    <h4>Lookup</h4>
    
    The lookup operation returns the best matching language tags. It is
    defined in RFC 4647 as follows:
    "By contrast with filtering, each language range represents the most
    specific tag that is an acceptable match.  The first matching tag found,
    according to the user's priority, is considered the closest match and is the
    item returned."
    
    For example, if a Language Priority List consists of two language ranges,
    `"zh-Hant-TW"` and `"en-US"`, in prioritized order, lookup
    method progressively searches the language tags below in order to find the
    best matching language tag.
    <blockquote>
    ```
       1. zh-Hant-TW
       2. zh-Hant
       3. zh
       4. en-US
       5. en
    ```
    </blockquote>
    If there is a language tag which matches completely to a language range
    above, the language tag is returned.
    
    `"*"` is the special language range, and it is ignored in lookup.
    
    If multiple language tags match as a result of the subtag `'*'`
    included in a language range, the first matching language tag returned by
    an Iterator over a Collection of language tags is treated as
    the best matching one.
    
    <h3>Use of Locale</h3>
    
    Once you've created a `Locale` you can query it for information
    about itself. Use `getCountry` to get the country (or region)
    code and `getLanguage` to get the language code.
    You can use `getDisplayCountry` to get the
    name of the country suitable for displaying to the user. Similarly,
    you can use `getDisplayLanguage` to get the name of
    the language suitable for displaying to the user. Interestingly,
    the `getDisplayXXX` methods are themselves locale-sensitive
    and have two versions: one that uses the default
    Locale.Category.DISPLAY DISPLAY locale and one
    that uses the locale specified as an argument.
    
    The Java Platform provides a number of classes that perform locale-sensitive
    operations. For example, the `NumberFormat` class formats
    numbers, currency, and percentages in a locale-sensitive manner. Classes
    such as `NumberFormat` have several convenience methods
    for creating a default object of that type. For example, the
    `NumberFormat` class provides these three convenience methods
    for creating a default `NumberFormat` object:
    <blockquote>
    ```
        NumberFormat.getInstance()
        NumberFormat.getCurrencyInstance()
        NumberFormat.getPercentInstance()
    ```
    </blockquote>
    Each of these methods has two variants; one with an explicit locale
    and one without; the latter uses the default
    Locale.Category.FORMAT FORMAT locale:
    <blockquote>
    ```
        NumberFormat.getInstance(myLocale)
        NumberFormat.getCurrencyInstance(myLocale)
        NumberFormat.getPercentInstance(myLocale)
    ```
    </blockquote>
    A `Locale` is the mechanism for identifying the kind of object
    (`NumberFormat`) that you would like to get. The locale is
    <STRONG>just</STRONG> a mechanism for identifying objects,
    <STRONG>not</STRONG> a container for the objects themselves.
    
    <h3>Compatibility</h3>
    
    In order to maintain compatibility with existing usage, Locale's
    constructors retain their behavior prior to the Java Runtime
    Environment version 1.7.  The same is largely True for the
    `toString` method. Thus Locale objects can continue to
    be used as they were. In particular, clients who parse the output
    of toString into language, country, and variant fields can continue
    to do so (although this is strongly discouraged), although the
    variant field will have additional information in it if script or
    extensions are present.
    
    In addition, BCP 47 imposes syntax restrictions that are not
    imposed by Locale's constructors. This means that conversions
    between some Locales and BCP 47 language tags cannot be made without
    losing information. Thus `toLanguageTag` cannot
    represent the state of locales whose language, country, or variant
    do not conform to BCP 47.
    
    Because of these issues, it is recommended that clients migrate
    away from constructing non-conforming locales and use the
    `forLanguageTag` and `Locale.Builder` APIs instead.
    Clients desiring a string representation of the complete locale can
    then always rely on `toLanguageTag` for this purpose.
    
    <h4><a id="special_cases_constructor">Special cases</a></h4>
    
    For compatibility reasons, two
    non-conforming locales are treated as special cases.  These are
    **`ja_JP_JP`** and **`th_TH_TH`**. These are ill-formed
    in BCP 47 since the variants are too short. To ease migration to BCP 47,
    these are treated specially during construction.  These two cases (and only
    these) cause a constructor to generate an extension, all other values behave
    exactly as they did prior to Java 7.
    
    Java has used `ja_JP_JP` to represent Japanese as used in
    Japan together with the Japanese Imperial calendar. This is now
    representable using a Unicode locale extension, by specifying the
    Unicode locale key `ca` (for "calendar") and type
    `japanese`. When the Locale constructor is called with the
    arguments "ja", "JP", "JP", the extension "u-ca-japanese" is
    automatically added.
    
    Java has used `th_TH_TH` to represent Thai as used in
    Thailand together with Thai digits. This is also now representable using
    a Unicode locale extension, by specifying the Unicode locale key
    `nu` (for "number") and value `thai`. When the Locale
    constructor is called with the arguments "th", "TH", "TH", the
    extension "u-nu-thai" is automatically added.
    
    <h4>Serialization</h4>
    
    During serialization, writeObject writes all fields to the output
    stream, including extensions.
    
    During deserialization, readResolve adds extensions as described
    in <a href="#special_cases_constructor">Special Cases</a>, only
    for the two cases th_TH_TH and ja_JP_JP.
    
    <h4><a id="legacy_language_codes">Legacy language codes</a></h4>
    
    Locale's constructor has always converted three language codes to
    their earlier, obsoleted forms: `he` maps to `iw`,
    `yi` maps to `ji`, and `id` maps to
    `in`. Since Java SE 17, this is no longer the case. Each
    language maps to its new form; `iw` maps to `he`, `ji`
    maps to `yi`, and `in` maps to `id`.
    
    For the backward compatible behavior, the system property
    java.locale.useOldISOCodes reverts the behavior
    back to that of before Java SE 17. If the system property is set to
    `True`, those three current language codes are mapped to their
    backward compatible forms. The property is only read at Java runtime
    startup and subsequent calls to `System.setProperty()` will
    have no effect.
    
    The APIs added in 1.7 map between the old and new language codes,
    maintaining the mapped codes internal to Locale (so that
    `getLanguage` and `toString` reflect the mapped
    code, which depends on the `java.locale.useOldISOCodes` system
    property), but using the new codes in the BCP 47 language tag APIs (so
    that `toLanguageTag` reflects the new one). This
    preserves the equivalence between Locales no matter which code or
    API is used to construct them. Java's default resource bundle
    lookup mechanism also implements this mapping, so that resources
    can be named using either convention, see ResourceBundle.Control.
    
    <h4>Three-letter language/country(region) codes</h4>
    
    The Locale constructors have always specified that the language
    and the country param be two characters in length, although in
    practice they have accepted any length.  The specification has now
    been relaxed to allow language codes of two to eight characters and
    country (region) codes of two to three characters, and in
    particular, three-letter language codes and three-digit region
    codes as specified in the IANA Language Subtag Registry.  For
    compatibility, the implementation still does not impose a length
    constraint.

    Author(s)
    - Mark Davis

    See
    - java.text.Collator

    Since
    - 1.1
    """

    ENGLISH = None
    """
    Useful constant for language.
    """
    FRENCH = None
    """
    Useful constant for language.
    """
    GERMAN = None
    """
    Useful constant for language.
    """
    ITALIAN = None
    """
    Useful constant for language.
    """
    JAPANESE = None
    """
    Useful constant for language.
    """
    KOREAN = None
    """
    Useful constant for language.
    """
    CHINESE = None
    """
    Useful constant for language.
    """
    SIMPLIFIED_CHINESE = None
    """
    Useful constant for language.
    """
    TRADITIONAL_CHINESE = None
    """
    Useful constant for language.
    """
    FRANCE = None
    """
    Useful constant for country.
    """
    GERMANY = None
    """
    Useful constant for country.
    """
    ITALY = None
    """
    Useful constant for country.
    """
    JAPAN = None
    """
    Useful constant for country.
    """
    KOREA = None
    """
    Useful constant for country.
    """
    UK = None
    """
    Useful constant for country.
    """
    US = None
    """
    Useful constant for country.
    """
    CANADA = None
    """
    Useful constant for country.
    """
    CANADA_FRENCH = None
    """
    Useful constant for country.
    """
    ROOT = None
    """
    Useful constant for the root locale.  The root locale is the locale whose
    language, country, and variant are empty ("") strings.  This is regarded
    as the base locale of all locales, and is used as the language/country
    neutral locale for the locale sensitive operations.

    Since
    - 1.6
    """
    CHINA = SIMPLIFIED_CHINESE
    """
    Useful constant for country.
    """
    PRC = SIMPLIFIED_CHINESE
    """
    Useful constant for country.
    """
    TAIWAN = TRADITIONAL_CHINESE
    """
    Useful constant for country.
    """
    PRIVATE_USE_EXTENSION = 'x'
    """
    The key for the private use extension ('x').

    See
    - Builder.setExtension(char, String)

    Since
    - 1.7
    """
    UNICODE_LOCALE_EXTENSION = 'u'
    """
    The key for Unicode locale extension ('u').

    See
    - Builder.setExtension(char, String)

    Since
    - 1.7
    """


    def __init__(self, language: str, country: str, variant: str):
        """
        Construct a locale from language, country and variant.
        This constructor normalizes the language value to lowercase and
        the country value to uppercase.

        Arguments
        - language: An ISO 639 alpha-2 or alpha-3 language code, or a language subtag
        up to 8 characters in length.  See the `Locale` class description about
        valid language values.
        - country: An ISO 3166 alpha-2 country code or a UN M.49 numeric-3 area code.
        See the `Locale` class description about valid country values.
        - variant: Any arbitrary value used to indicate a variation of a `Locale`.
        See the `Locale` class description for the details.

        Raises
        - NullPointerException: thrown if any argument is null.

        Unknown Tags
        - 
        - Obsolete ISO 639 codes ("iw", "ji", and "in") are mapped to
        their current forms. See <a href="#legacy_language_codes">Legacy language
        codes</a> for more information.
        - For backward compatibility reasons, this constructor does not make
        any syntactic checks on the input.
        - The two cases ("ja", "JP", "JP") and ("th", "TH", "TH") are handled specially,
        see <a href="#special_cases_constructor">Special Cases</a> for more information.
        """
        ...


    def __init__(self, language: str, country: str):
        """
        Construct a locale from language and country.
        This constructor normalizes the language value to lowercase and
        the country value to uppercase.

        Arguments
        - language: An ISO 639 alpha-2 or alpha-3 language code, or a language subtag
        up to 8 characters in length.  See the `Locale` class description about
        valid language values.
        - country: An ISO 3166 alpha-2 country code or a UN M.49 numeric-3 area code.
        See the `Locale` class description about valid country values.

        Raises
        - NullPointerException: thrown if either argument is null.

        Unknown Tags
        - 
        - Obsolete ISO 639 codes ("iw", "ji", and "in") are mapped to
        their current forms. See <a href="#legacy_language_codes">Legacy language
        codes</a> for more information.
        - For backward compatibility reasons, this constructor does not make
        any syntactic checks on the input.
        """
        ...


    def __init__(self, language: str):
        """
        Construct a locale from a language code.
        This constructor normalizes the language value to lowercase.

        Arguments
        - language: An ISO 639 alpha-2 or alpha-3 language code, or a language subtag
        up to 8 characters in length.  See the `Locale` class description about
        valid language values.

        Raises
        - NullPointerException: thrown if argument is null.

        Since
        - 1.4

        Unknown Tags
        - 
        - Obsolete ISO 639 codes ("iw", "ji", and "in") are mapped to
        their current forms. See <a href="#legacy_language_codes">Legacy language
        codes</a> for more information.
        - For backward compatibility reasons, this constructor does not make
        any syntactic checks on the input.
        """
        ...


    @staticmethod
    def getDefault() -> "Locale":
        """
        Gets the current value of the default locale for this instance
        of the Java Virtual Machine.
        
        The Java Virtual Machine sets the default locale during startup
        based on the host environment. It is used by many locale-sensitive
        methods if no locale is explicitly specified.
        It can be changed using the
        .setDefault(java.util.Locale) setDefault method.

        Returns
        - the default locale for this instance of the Java Virtual Machine
        """
        ...


    @staticmethod
    def getDefault(category: "Locale.Category") -> "Locale":
        """
        Gets the current value of the default locale for the specified Category
        for this instance of the Java Virtual Machine.
        
        The Java Virtual Machine sets the default locale during startup based
        on the host environment. It is used by many locale-sensitive methods
        if no locale is explicitly specified. It can be changed using the
        setDefault(Locale.Category, Locale) method.

        Arguments
        - category: the specified category to get the default locale

        Returns
        - the default locale for the specified Category for this instance
            of the Java Virtual Machine

        Raises
        - NullPointerException: if category is null

        See
        - .setDefault(Locale.Category, Locale)

        Since
        - 1.7
        """
        ...


    @staticmethod
    def setDefault(newLocale: "Locale") -> None:
        """
        Sets the default locale for this instance of the Java Virtual Machine.
        This does not affect the host locale.
        
        If there is a security manager, its `checkPermission`
        method is called with a `PropertyPermission("user.language", "write")`
        permission before the default locale is changed.
        
        The Java Virtual Machine sets the default locale during startup
        based on the host environment. It is used by many locale-sensitive
        methods if no locale is explicitly specified.
        
        Since changing the default locale may affect many different areas
        of functionality, this method should only be used if the caller
        is prepared to reinitialize locale-sensitive code running
        within the same Java Virtual Machine.
        
        By setting the default locale with this method, all of the default
        locales for each Category are also set to the specified default locale.

        Arguments
        - newLocale: the new default locale

        Raises
        - SecurityException: if a security manager exists and its
               `checkPermission` method doesn't allow the operation.
        - NullPointerException: if `newLocale` is null

        See
        - java.util.PropertyPermission
        """
        ...


    @staticmethod
    def setDefault(category: "Locale.Category", newLocale: "Locale") -> None:
        """
        Sets the default locale for the specified Category for this instance
        of the Java Virtual Machine. This does not affect the host locale.
        
        If there is a security manager, its checkPermission method is called
        with a PropertyPermission("user.language", "write") permission before
        the default locale is changed.
        
        The Java Virtual Machine sets the default locale during startup based
        on the host environment. It is used by many locale-sensitive methods
        if no locale is explicitly specified.
        
        Since changing the default locale may affect many different areas of
        functionality, this method should only be used if the caller is
        prepared to reinitialize locale-sensitive code running within the
        same Java Virtual Machine.

        Arguments
        - category: the specified category to set the default locale
        - newLocale: the new default locale

        Raises
        - SecurityException: if a security manager exists and its
            checkPermission method doesn't allow the operation.
        - NullPointerException: if category and/or newLocale is null

        See
        - .getDefault(Locale.Category)

        Since
        - 1.7
        """
        ...


    @staticmethod
    def getAvailableLocales() -> list["Locale"]:
        """
        Returns an array of all installed locales.
        The returned array represents the union of locales supported
        by the Java runtime environment and by installed
        java.util.spi.LocaleServiceProvider LocaleServiceProvider
        implementations.  It must contain at least a `Locale`
        instance equal to java.util.Locale.US Locale.US.

        Returns
        - An array of installed locales.
        """
        ...


    @staticmethod
    def getISOCountries() -> list[str]:
        """
        Returns a list of all 2-letter country codes defined in ISO 3166.
        Can be used to create Locales.
        This method is equivalent to .getISOCountries(Locale.IsoCountryCode type)
        with `type`  IsoCountryCode.PART1_ALPHA2.
        
        **Note:** The `Locale` class also supports other codes for
        country (region), such as 3-letter numeric UN M.49 area codes.
        Therefore, the list returned by this method does not contain ALL valid
        codes that can be used to create Locales.
        
        Note that this method does not return obsolete 2-letter country codes.
        ISO3166-3 codes which designate country codes for those obsolete codes,
        can be retrieved from .getISOCountries(Locale.IsoCountryCode type) with
        `type`  IsoCountryCode.PART3.

        Returns
        - An array of ISO 3166 two-letter country codes.
        """
        ...


    @staticmethod
    def getISOCountries(type: "IsoCountryCode") -> set[str]:
        """
        Returns a `Set` of ISO3166 country codes for the specified type.

        Arguments
        - type: Locale.IsoCountryCode specified ISO code type.

        Returns
        - a `Set` of ISO country codes for the specified type.

        Raises
        - NullPointerException: if type is null

        See
        - java.util.Locale.IsoCountryCode

        Since
        - 9
        """
        ...


    @staticmethod
    def getISOLanguages() -> list[str]:
        """
        Returns a list of all 2-letter language codes defined in ISO 639.
        Can be used to create Locales.
        
        **Note:**
        
        - ISO 639 is not a stable standard&mdash; some languages' codes have changed.
        The list this function returns includes both the new and the old codes for the
        languages whose codes have changed.
        - The `Locale` class also supports language codes up to
        8 characters in length.  Therefore, the list returned by this method does
        not contain ALL valid codes that can be used to create Locales.

        Returns
        - An array of ISO 639 two-letter language codes.
        """
        ...


    def getLanguage(self) -> str:
        """
        Returns the language code of this Locale.

        Returns
        - The language code, or the empty string if none is defined.

        See
        - .getDisplayLanguage

        Unknown Tags
        - This method returns the new forms for the obsolete ISO 639
        codes ("iw", "ji", and "in"). See <a href="#legacy_language_codes">
        Legacy language codes</a> for more information.
        """
        ...


    def getScript(self) -> str:
        """
        Returns the script for this locale, which should
        either be the empty string or an ISO 15924 4-letter script
        code. The first letter is uppercase and the rest are
        lowercase, for example, 'Latn', 'Cyrl'.

        Returns
        - The script code, or the empty string if none is defined.

        See
        - .getDisplayScript

        Since
        - 1.7
        """
        ...


    def getCountry(self) -> str:
        """
        Returns the country/region code for this locale, which should
        either be the empty string, an uppercase ISO 3166 2-letter code,
        or a UN M.49 3-digit code.

        Returns
        - The country/region code, or the empty string if none is defined.

        See
        - .getDisplayCountry
        """
        ...


    def getVariant(self) -> str:
        """
        Returns the variant code for this locale.

        Returns
        - The variant code, or the empty string if none is defined.

        See
        - .getDisplayVariant
        """
        ...


    def hasExtensions(self) -> bool:
        """
        Returns `True` if this `Locale` has any <a href="#def_extensions">
        extensions</a>.

        Returns
        - `True` if this `Locale` has any extensions

        Since
        - 1.8
        """
        ...


    def stripExtensions(self) -> "Locale":
        """
        Returns a copy of this `Locale` with no <a href="#def_extensions">
        extensions</a>. If this `Locale` has no extensions, this `Locale`
        is returned.

        Returns
        - a copy of this `Locale` with no extensions, or `this`
                if `this` has no extensions

        Since
        - 1.8
        """
        ...


    def getExtension(self, key: str) -> str:
        """
        Returns the extension (or private use) value associated with
        the specified key, or null if there is no extension
        associated with the key. To be well-formed, the key must be one
        of `[0-9A-Za-z]`. Keys are case-insensitive, so
        for example 'z' and 'Z' represent the same extension.

        Arguments
        - key: the extension key

        Returns
        - The extension, or null if this locale defines no
        extension for the specified key.

        Raises
        - IllegalArgumentException: if key is not well-formed

        See
        - .UNICODE_LOCALE_EXTENSION

        Since
        - 1.7
        """
        ...


    def getExtensionKeys(self) -> set["Character"]:
        """
        Returns the set of extension keys associated with this locale, or the
        empty set if it has no extensions. The returned set is unmodifiable.
        The keys will all be lower-case.

        Returns
        - The set of extension keys, or the empty set if this locale has
        no extensions.

        Since
        - 1.7
        """
        ...


    def getUnicodeLocaleAttributes(self) -> set[str]:
        """
        Returns the set of unicode locale attributes associated with
        this locale, or the empty set if it has no attributes. The
        returned set is unmodifiable.

        Returns
        - The set of attributes.

        Since
        - 1.7
        """
        ...


    def getUnicodeLocaleType(self, key: str) -> str:
        """
        Returns the Unicode locale type associated with the specified Unicode locale key
        for this locale. Returns the empty string for keys that are defined with no type.
        Returns null if the key is not defined. Keys are case-insensitive. The key must
        be two alphanumeric characters ([0-9a-zA-Z]), or an IllegalArgumentException is
        thrown.

        Arguments
        - key: the Unicode locale key

        Returns
        - The Unicode locale type associated with the key, or null if the
        locale does not define the key.

        Raises
        - IllegalArgumentException: if the key is not well-formed
        - NullPointerException: if `key` is null

        Since
        - 1.7
        """
        ...


    def getUnicodeLocaleKeys(self) -> set[str]:
        """
        Returns the set of Unicode locale keys defined by this locale, or the empty set if
        this locale has none.  The returned set is immutable.  Keys are all lower case.

        Returns
        - The set of Unicode locale keys, or the empty set if this locale has
        no Unicode locale keywords.

        Since
        - 1.7
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this `Locale`
        object, consisting of language, country, variant, script,
        and extensions as below:
        <blockquote>
        language + "_" + country + "_" + (variant + "_#" | "#") + script + "_" + extensions
        </blockquote>
        
        Language is always lower case, country is always upper case, script is always title
        case, and extensions are always lower case.  Extensions and private use subtags
        will be in canonical order as explained in .toLanguageTag.
        
        When the locale has neither script nor extensions, the result is the same as in
        Java 6 and prior.
        
        If both the language and country fields are missing, this function will return
        the empty string, even if the variant, script, or extensions field is present (you
        can't have a locale with just a variant, the variant must accompany a well-formed
        language or country code).
        
        If script or extensions are present and variant is missing, no underscore is
        added before the "#".
        
        This behavior is designed to support debugging and to be compatible with
        previous uses of `toString` that expected language, country, and variant
        fields only.  To represent a Locale as a String for interchange purposes, use
        .toLanguageTag.
        
        Examples: 
        - `en`
        - `de_DE`
        - `_GB`
        - `en_US_WIN`
        - `de__POSIX`
        - `zh_CN_.Hans`
        - `zh_TW_.Hant_x-java`
        - `th_TH_TH_.u-nu-thai`

        Returns
        - A string representation of the Locale, for debugging.

        See
        - .toLanguageTag
        """
        ...


    def toLanguageTag(self) -> str:
        """
        Returns a well-formed IETF BCP 47 language tag representing
        this locale.
        
        If this `Locale` has a language, country, or
        variant that does not satisfy the IETF BCP 47 language tag
        syntax requirements, this method handles these fields as
        described below:
        
        **Language:** If language is empty, or not <a
        href="#def_language" >well-formed</a> (for example "a" or
        "e2"), it will be emitted as "und" (Undetermined).
        
        **Country:** If country is not <a
        href="#def_region">well-formed</a> (for example "12" or "USA"),
        it will be omitted.
        
        **Variant:** If variant **is** <a
        href="#def_variant">well-formed</a>, each sub-segment
        (delimited by '-' or '_') is emitted as a subtag.  Otherwise:
        
        
        - if all sub-segments match `[0-9a-zA-Z]{1,8}`
        (for example "WIN" or "Oracle_JDK_Standard_Edition"), the first
        ill-formed sub-segment and all following will be appended to
        the private use subtag.  The first appended subtag will be
        "lvariant", followed by the sub-segments in order, separated by
        hyphen. For example, "x-lvariant-WIN",
        "Oracle-x-lvariant-JDK-Standard-Edition".
        
        - if any sub-segment does not match
        `[0-9a-zA-Z]{1,8}`, the variant will be truncated
        and the problematic sub-segment and all following sub-segments
        will be omitted.  If the remainder is non-empty, it will be
        emitted as a private use subtag as above (even if the remainder
        turns out to be well-formed).  For example,
        "Solaris_isjustthecoolestthing" is emitted as
        "x-lvariant-Solaris", not as "solaris".
        
        **Special Conversions:** Java supports some old locale
        representations, including deprecated ISO language codes,
        for compatibility. This method performs the following
        conversions:
        
        
        - Deprecated ISO language codes "iw", "ji", and "in" are
        converted to "he", "yi", and "id", respectively.
        
        - A locale with language "no", country "NO", and variant
        "NY", representing Norwegian Nynorsk (Norway), is converted
        to a language tag "nn-NO".
        
        **Note:** Although the language tag created by this
        method is well-formed (satisfies the syntax requirements
        defined by the IETF BCP 47 specification), it is not
        necessarily a valid BCP 47 language tag.  For example,
        ```
          new Locale("xx", "YY").toLanguageTag();```
        
        will return "xx-YY", but the language subtag "xx" and the
        region subtag "YY" are invalid because they are not registered
        in the IANA Language Subtag Registry.

        Returns
        - a BCP47 language tag representing the locale

        See
        - .forLanguageTag(String)

        Since
        - 1.7
        """
        ...


    @staticmethod
    def forLanguageTag(languageTag: str) -> "Locale":
        """
        Returns a locale for the specified IETF BCP 47 language tag string.
        
        If the specified language tag contains any ill-formed subtags,
        the first such subtag and all following subtags are ignored.  Compare
        to Locale.Builder.setLanguageTag which throws an exception
        in this case.
        
        The following **conversions** are performed:
        
        - The language code "und" is mapped to language "".
        
        - The language codes "iw", "ji", and "in" are mapped to "he",
        "yi", and "id" respectively. (This is the same canonicalization
        that's done in Locale's constructors.) See
        <a href="#legacy_language_codes">Legacy language codes</a>
        for more information.
        
        - The portion of a private use subtag prefixed by "lvariant",
        if any, is removed and appended to the variant field in the
        result locale (without case normalization).  If it is then
        empty, the private use subtag is discarded:
        
        ```
            Locale loc;
            loc = Locale.forLanguageTag("en-US-x-lvariant-POSIX");
            loc.getVariant(); // returns "POSIX"
            loc.getExtension('x'); // returns null
        
            loc = Locale.forLanguageTag("de-POSIX-x-URP-lvariant-Abc-Def");
            loc.getVariant(); // returns "POSIX_Abc_Def"
            loc.getExtension('x'); // returns "urp"
        ```
        
        - When the languageTag argument contains an extlang subtag,
        the first such subtag is used as the language, and the primary
        language subtag and other extlang subtags are ignored:
        
        ```
            Locale.forLanguageTag("ar-aao").getLanguage(); // returns "aao"
            Locale.forLanguageTag("en-abc-def-us").toString(); // returns "abc_US"
        ```
        
        - Case is normalized except for variant tags, which are left
        unchanged.  Language is normalized to lower case, script to
        title case, country to upper case, and extensions to lower
        case.
        
        - If, after processing, the locale would exactly match either
        ja_JP_JP or th_TH_TH with no extensions, the appropriate
        extensions are added as though the constructor had been called:
        
        ```
           Locale.forLanguageTag("ja-JP-x-lvariant-JP").toLanguageTag();
           // returns "ja-JP-u-ca-japanese-x-lvariant-JP"
           Locale.forLanguageTag("th-TH-x-lvariant-TH").toLanguageTag();
           // returns "th-TH-u-nu-thai-x-lvariant-TH"
        ```
        
        This implements the 'Language-Tag' production of BCP47, and
        so supports legacy (regular and irregular, referred to as
        "Type: grandfathered" in BCP47) as well as
        private use language tags.  Stand alone private use tags are
        represented as empty language and extension 'x-whatever',
        and legacy tags are converted to their canonical replacements
        where they exist.
        
        Legacy tags with canonical replacements are as follows:
        
        <table class="striped">
        <caption style="display:none">Legacy tags with canonical replacements</caption>
        <thead style="text-align:center">
        <tr><th scope="col" style="padding: 0 2px">legacy tag</th><th scope="col" style="padding: 0 2px">modern replacement</th></tr>
        </thead>
        <tbody style="text-align:center">
        <tr><th scope="row">art-lojban</th><td>jbo</td></tr>
        <tr><th scope="row">i-ami</th><td>ami</td></tr>
        <tr><th scope="row">i-bnn</th><td>bnn</td></tr>
        <tr><th scope="row">i-hak</th><td>hak</td></tr>
        <tr><th scope="row">i-klingon</th><td>tlh</td></tr>
        <tr><th scope="row">i-lux</th><td>lb</td></tr>
        <tr><th scope="row">i-navajo</th><td>nv</td></tr>
        <tr><th scope="row">i-pwn</th><td>pwn</td></tr>
        <tr><th scope="row">i-tao</th><td>tao</td></tr>
        <tr><th scope="row">i-tay</th><td>tay</td></tr>
        <tr><th scope="row">i-tsu</th><td>tsu</td></tr>
        <tr><th scope="row">no-bok</th><td>nb</td></tr>
        <tr><th scope="row">no-nyn</th><td>nn</td></tr>
        <tr><th scope="row">sgn-BE-FR</th><td>sfb</td></tr>
        <tr><th scope="row">sgn-BE-NL</th><td>vgt</td></tr>
        <tr><th scope="row">sgn-CH-DE</th><td>sgg</td></tr>
        <tr><th scope="row">zh-guoyu</th><td>cmn</td></tr>
        <tr><th scope="row">zh-hakka</th><td>hak</td></tr>
        <tr><th scope="row">zh-min-nan</th><td>nan</td></tr>
        <tr><th scope="row">zh-xiang</th><td>hsn</td></tr>
        </tbody>
        </table>
        
        Legacy tags with no modern replacement will be
        converted as follows:
        
        <table class="striped">
        <caption style="display:none">Legacy tags with no modern replacement</caption>
        <thead style="text-align:center">
        <tr><th scope="col" style="padding: 0 2px">legacy tag</th><th scope="col" style="padding: 0 2px">converts to</th></tr>
        </thead>
        <tbody style="text-align:center">
        <tr><th scope="row">cel-gaulish</th><td>xtg-x-cel-gaulish</td></tr>
        <tr><th scope="row">en-GB-oed</th><td>en-GB-x-oed</td></tr>
        <tr><th scope="row">i-default</th><td>en-x-i-default</td></tr>
        <tr><th scope="row">i-enochian</th><td>und-x-i-enochian</td></tr>
        <tr><th scope="row">i-mingo</th><td>see-x-i-mingo</td></tr>
        <tr><th scope="row">zh-min</th><td>nan-x-zh-min</td></tr>
        </tbody>
        </table>
        
        For a list of all legacy tags, see the
        IANA Language Subtag Registry (search for "Type: grandfathered").
        
        **Note**: there is no guarantee that `toLanguageTag`
        and `forLanguageTag` will round-trip.

        Arguments
        - languageTag: the language tag

        Returns
        - The locale that best represents the language tag.

        Raises
        - NullPointerException: if `languageTag` is `null`

        See
        - java.util.Locale.Builder.setLanguageTag(String)

        Since
        - 1.7
        """
        ...


    def getISO3Language(self) -> str:
        """
        Returns a three-letter abbreviation of this locale's language.
        If the language matches an ISO 639-1 two-letter code, the
        corresponding ISO 639-2/T three-letter lowercase code is
        returned.  The ISO 639-2 language codes can be found on-line,
        see "Codes for the Representation of Names of Languages Part 2:
        Alpha-3 Code".  If the locale specifies a three-letter
        language, the language is returned as is.  If the locale does
        not specify a language the empty string is returned.

        Returns
        - A three-letter abbreviation of this locale's language.

        Raises
        - MissingResourceException: Throws MissingResourceException if
        three-letter language abbreviation is not available for this locale.
        """
        ...


    def getISO3Country(self) -> str:
        """
        Returns a three-letter abbreviation for this locale's country.
        If the country matches an ISO 3166-1 alpha-2 code, the
        corresponding ISO 3166-1 alpha-3 uppercase code is returned.
        If the locale doesn't specify a country, this will be the empty
        string.
        
        The ISO 3166-1 codes can be found on-line.

        Returns
        - A three-letter abbreviation of this locale's country.

        Raises
        - MissingResourceException: Throws MissingResourceException if the
        three-letter country abbreviation is not available for this locale.
        """
        ...


    def getDisplayLanguage(self) -> str:
        """
        Returns a name for the locale's language that is appropriate for display to the
        user.
        If possible, the name returned will be localized for the default
        Locale.Category.DISPLAY DISPLAY locale.
        For example, if the locale is fr_FR and the default
        Locale.Category.DISPLAY DISPLAY locale
        is en_US, getDisplayLanguage() will return "French"; if the locale is en_US and
        the default Locale.Category.DISPLAY DISPLAY locale is fr_FR,
        getDisplayLanguage() will return "anglais".
        If the name returned cannot be localized for the default
        Locale.Category.DISPLAY DISPLAY locale,
        (say, we don't have a Japanese name for Croatian),
        this function falls back on the English name, and uses the ISO code as a last-resort
        value.  If the locale doesn't specify a language, this function returns the empty string.

        Returns
        - The name of the display language.
        """
        ...


    def getDisplayLanguage(self, inLocale: "Locale") -> str:
        """
        Returns a name for the locale's language that is appropriate for display to the
        user.
        If possible, the name returned will be localized according to inLocale.
        For example, if the locale is fr_FR and inLocale
        is en_US, getDisplayLanguage() will return "French"; if the locale is en_US and
        inLocale is fr_FR, getDisplayLanguage() will return "anglais".
        If the name returned cannot be localized according to inLocale,
        (say, we don't have a Japanese name for Croatian),
        this function falls back on the English name, and finally
        on the ISO code as a last-resort value.  If the locale doesn't specify a language,
        this function returns the empty string.

        Arguments
        - inLocale: The locale for which to retrieve the display language.

        Returns
        - The name of the display language appropriate to the given locale.

        Raises
        - NullPointerException: if `inLocale` is `null`
        """
        ...


    def getDisplayScript(self) -> str:
        """
        Returns a name for the locale's script that is appropriate for display to
        the user. If possible, the name will be localized for the default
        Locale.Category.DISPLAY DISPLAY locale.  Returns
        the empty string if this locale doesn't specify a script code.

        Returns
        - the display name of the script code for the current default
            Locale.Category.DISPLAY DISPLAY locale

        Since
        - 1.7
        """
        ...


    def getDisplayScript(self, inLocale: "Locale") -> str:
        """
        Returns a name for the locale's script that is appropriate
        for display to the user. If possible, the name will be
        localized for the given locale. Returns the empty string if
        this locale doesn't specify a script code.

        Arguments
        - inLocale: The locale for which to retrieve the display script.

        Returns
        - the display name of the script code for the current default
        Locale.Category.DISPLAY DISPLAY locale

        Raises
        - NullPointerException: if `inLocale` is `null`

        Since
        - 1.7
        """
        ...


    def getDisplayCountry(self) -> str:
        """
        Returns a name for the locale's country that is appropriate for display to the
        user.
        If possible, the name returned will be localized for the default
        Locale.Category.DISPLAY DISPLAY locale.
        For example, if the locale is fr_FR and the default
        Locale.Category.DISPLAY DISPLAY locale
        is en_US, getDisplayCountry() will return "France"; if the locale is en_US and
        the default Locale.Category.DISPLAY DISPLAY locale is fr_FR,
        getDisplayCountry() will return "Etats-Unis".
        If the name returned cannot be localized for the default
        Locale.Category.DISPLAY DISPLAY locale,
        (say, we don't have a Japanese name for Croatia),
        this function falls back on the English name, and uses the ISO code as a last-resort
        value.  If the locale doesn't specify a country, this function returns the empty string.

        Returns
        - The name of the country appropriate to the locale.
        """
        ...


    def getDisplayCountry(self, inLocale: "Locale") -> str:
        """
        Returns a name for the locale's country that is appropriate for display to the
        user.
        If possible, the name returned will be localized according to inLocale.
        For example, if the locale is fr_FR and inLocale
        is en_US, getDisplayCountry() will return "France"; if the locale is en_US and
        inLocale is fr_FR, getDisplayCountry() will return "Etats-Unis".
        If the name returned cannot be localized according to inLocale.
        (say, we don't have a Japanese name for Croatia),
        this function falls back on the English name, and finally
        on the ISO code as a last-resort value.  If the locale doesn't specify a country,
        this function returns the empty string.

        Arguments
        - inLocale: The locale for which to retrieve the display country.

        Returns
        - The name of the country appropriate to the given locale.

        Raises
        - NullPointerException: if `inLocale` is `null`
        """
        ...


    def getDisplayVariant(self) -> str:
        """
        Returns a name for the locale's variant code that is appropriate for display to the
        user.  If possible, the name will be localized for the default
        Locale.Category.DISPLAY DISPLAY locale.  If the locale
        doesn't specify a variant code, this function returns the empty string.

        Returns
        - The name of the display variant code appropriate to the locale.
        """
        ...


    def getDisplayVariant(self, inLocale: "Locale") -> str:
        """
        Returns a name for the locale's variant code that is appropriate for display to the
        user.  If possible, the name will be localized for inLocale.  If the locale
        doesn't specify a variant code, this function returns the empty string.

        Arguments
        - inLocale: The locale for which to retrieve the display variant code.

        Returns
        - The name of the display variant code appropriate to the given locale.

        Raises
        - NullPointerException: if `inLocale` is `null`
        """
        ...


    def getDisplayName(self) -> str:
        """
        Returns a name for the locale that is appropriate for display to the
        user. This will be the values returned by getDisplayLanguage(),
        getDisplayScript(), getDisplayCountry(), getDisplayVariant() and
        optional <a href="./Locale.html#def_locale_extension">Unicode extensions</a>
        assembled into a single string. The non-empty values are used in order, with
        the second and subsequent names in parentheses.  For example:
        <blockquote>
        language (script, country, variant(, extension)*)
        language (country(, extension)*)
        language (variant(, extension)*)
        script (country(, extension)*)
        country (extension)*
        </blockquote>
        depending on which fields are specified in the locale. The field
        separator in the above parentheses, denoted as a comma character, may
        be localized depending on the locale. If the language, script, country,
        and variant fields are all empty, this function returns the empty string.

        Returns
        - The name of the locale appropriate to display.
        """
        ...


    def getDisplayName(self, inLocale: "Locale") -> str:
        """
        Returns a name for the locale that is appropriate for display
        to the user.  This will be the values returned by
        getDisplayLanguage(), getDisplayScript(),getDisplayCountry()
        getDisplayVariant(), and optional <a href="./Locale.html#def_locale_extension">
        Unicode extensions</a> assembled into a single string. The non-empty
        values are used in order, with the second and subsequent names in
        parentheses.  For example:
        <blockquote>
        language (script, country, variant(, extension)*)
        language (country(, extension)*)
        language (variant(, extension)*)
        script (country(, extension)*)
        country (extension)*
        </blockquote>
        depending on which fields are specified in the locale. The field
        separator in the above parentheses, denoted as a comma character, may
        be localized depending on the locale. If the language, script, country,
        and variant fields are all empty, this function returns the empty string.

        Arguments
        - inLocale: The locale for which to retrieve the display name.

        Returns
        - The name of the locale appropriate to display.

        Raises
        - NullPointerException: if `inLocale` is `null`
        """
        ...


    def clone(self) -> "Object":
        """
        Overrides Cloneable.
        """
        ...


    def hashCode(self) -> int:
        """
        Override hashCode.
        Since Locales are often used in hashtables, caches the value
        for speed.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Returns True if this Locale is equal to another object.  A Locale is
        deemed equal to another Locale with identical language, script, country,
        variant and extensions, and unequal to all other objects.

        Returns
        - True if this Locale is equal to the specified object.
        """
        ...


    @staticmethod
    def filter(priorityList: list["LanguageRange"], locales: Iterable["Locale"], mode: "FilteringMode") -> list["Locale"]:
        """
        Returns a list of matching `Locale` instances using the filtering
        mechanism defined in RFC 4647.
        
        This filter operation on the given `locales` ensures that only
        unique matching locale(s) are returned.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - locales: `Locale` instances used for matching
        - mode: filtering mode

        Returns
        - a list of `Locale` instances for matching language tags
            sorted in descending order based on priority or weight, or an empty
            list if nothing matches. The list is modifiable.

        Raises
        - NullPointerException: if `priorityList` or `locales`
            is `null`
        - IllegalArgumentException: if one or more extended language ranges
            are included in the given list when
            FilteringMode.REJECT_EXTENDED_RANGES is specified

        Since
        - 1.8
        """
        ...


    @staticmethod
    def filter(priorityList: list["LanguageRange"], locales: Iterable["Locale"]) -> list["Locale"]:
        """
        Returns a list of matching `Locale` instances using the filtering
        mechanism defined in RFC 4647. This is equivalent to
        .filter(List, Collection, FilteringMode) when `mode` is
        FilteringMode.AUTOSELECT_FILTERING.
        
        This filter operation on the given `locales` ensures that only
        unique matching locale(s) are returned.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - locales: `Locale` instances used for matching

        Returns
        - a list of `Locale` instances for matching language tags
            sorted in descending order based on priority or weight, or an empty
            list if nothing matches. The list is modifiable.

        Raises
        - NullPointerException: if `priorityList` or `locales`
            is `null`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def filterTags(priorityList: list["LanguageRange"], tags: Iterable[str], mode: "FilteringMode") -> list[str]:
        """
        Returns a list of matching languages tags using the basic filtering
        mechanism defined in RFC 4647.
        
        This filter operation on the given `tags` ensures that only
        unique matching tag(s) are returned with preserved case. In case of
        duplicate matching tags with the case difference, the first matching
        tag with preserved case is returned.
        For example, "de-ch" is returned out of the duplicate matching tags
        "de-ch" and "de-CH", if "de-ch" is checked first for matching in the
        given `tags`. Note that if the given `tags` is an unordered
        `Collection`, the returned matching tag out of duplicate tags is
        subject to change, depending on the implementation of the
        `Collection`.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - tags: language tags
        - mode: filtering mode

        Returns
        - a list of matching language tags sorted in descending order
            based on priority or weight, or an empty list if nothing matches.
            The list is modifiable.

        Raises
        - NullPointerException: if `priorityList` or `tags` is
            `null`
        - IllegalArgumentException: if one or more extended language ranges
            are included in the given list when
            FilteringMode.REJECT_EXTENDED_RANGES is specified

        Since
        - 1.8
        """
        ...


    @staticmethod
    def filterTags(priorityList: list["LanguageRange"], tags: Iterable[str]) -> list[str]:
        """
        Returns a list of matching languages tags using the basic filtering
        mechanism defined in RFC 4647. This is equivalent to
        .filterTags(List, Collection, FilteringMode) when `mode`
        is FilteringMode.AUTOSELECT_FILTERING.
        
        This filter operation on the given `tags` ensures that only
        unique matching tag(s) are returned with preserved case. In case of
        duplicate matching tags with the case difference, the first matching
        tag with preserved case is returned.
        For example, "de-ch" is returned out of the duplicate matching tags
        "de-ch" and "de-CH", if "de-ch" is checked first for matching in the
        given `tags`. Note that if the given `tags` is an unordered
        `Collection`, the returned matching tag out of duplicate tags is
        subject to change, depending on the implementation of the
        `Collection`.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - tags: language tags

        Returns
        - a list of matching language tags sorted in descending order
            based on priority or weight, or an empty list if nothing matches.
            The list is modifiable.

        Raises
        - NullPointerException: if `priorityList` or `tags` is
            `null`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def lookup(priorityList: list["LanguageRange"], locales: Iterable["Locale"]) -> "Locale":
        """
        Returns a `Locale` instance for the best-matching language
        tag using the lookup mechanism defined in RFC 4647.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - locales: `Locale` instances used for matching

        Returns
        - the best matching `Locale` instance chosen based on
            priority or weight, or `null` if nothing matches.

        Raises
        - NullPointerException: if `priorityList` or `tags` is
            `null`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def lookupTag(priorityList: list["LanguageRange"], tags: Iterable[str]) -> str:
        """
        Returns the best-matching language tag using the lookup mechanism
        defined in RFC 4647.
        
        This lookup operation on the given `tags` ensures that the
        first matching tag with preserved case is returned.

        Arguments
        - priorityList: user's Language Priority List in which each language
            tag is sorted in descending order based on priority or weight
        - tags: language tangs used for matching

        Returns
        - the best matching language tag chosen based on priority or
            weight, or `null` if nothing matches.

        Raises
        - NullPointerException: if `priorityList` or `tags` is
            `null`

        Since
        - 1.8
        """
        ...


    class Builder:
        """
        `Builder` is used to build instances of `Locale`
        from values configured by the setters.  Unlike the `Locale`
        constructors, the `Builder` checks if a value configured by a
        setter satisfies the syntax requirements defined by the `Locale`
        class.  A `Locale` object created by a `Builder` is
        well-formed and can be transformed to a well-formed IETF BCP 47 language tag
        without losing information.
        
        **Note:** The `Locale` class does not provide any
        syntactic restrictions on variant, while BCP 47 requires each variant
        subtag to be 5 to 8 alphanumerics or a single numeric followed by 3
        alphanumerics.  The method `setVariant` throws
        `IllformedLocaleException` for a variant that does not satisfy
        this restriction. If it is necessary to support such a variant, use a
        Locale constructor.  However, keep in mind that a `Locale`
        object created this way might lose the variant information when
        transformed to a BCP 47 language tag.
        
        The following example shows how to create a `Locale` object
        with the `Builder`.
        <blockquote>
        ```
            Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
        ```
        </blockquote>
        
        Builders can be reused; `clear()` resets all
        fields to their default values.

        See
        - Locale.forLanguageTag

        Since
        - 1.7
        """

        def __init__(self):
            """
            Constructs an empty Builder. The default value of all
            fields, extensions, and private use information is the
            empty string.
            """
            ...


        def setLocale(self, locale: "Locale") -> "Builder":
            """
            Resets the `Builder` to match the provided
            `locale`.  Existing state is discarded.
            
            All fields of the locale must be well-formed, see Locale.
            
            Locales with any ill-formed fields cause
            `IllformedLocaleException` to be thrown, except for the
            following three cases which are accepted for compatibility
            reasons:
            - Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"
            - Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"
            - Locale("no", "NO", "NY") is treated as "nn-NO"

            Arguments
            - locale: the locale

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `locale` has
            any ill-formed fields.
            - NullPointerException: if `locale` is null.
            """
            ...


        def setLanguageTag(self, languageTag: str) -> "Builder":
            """
            Resets the Builder to match the provided IETF BCP 47
            language tag.  Discards the existing state.  Null and the
            empty string cause the builder to be reset, like .clear.  Legacy tags (see Locale.forLanguageTag) are converted to their canonical
            form before being processed.  Otherwise, the language tag
            must be well-formed (see Locale) or an exception is
            thrown (unlike `Locale.forLanguageTag`, which
            just discards ill-formed and following portions of the
            tag).

            Arguments
            - languageTag: the language tag

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `languageTag` is ill-formed

            See
            - Locale.forLanguageTag(String)
            """
            ...


        def setLanguage(self, language: str) -> "Builder":
            """
            Sets the language.  If `language` is the empty string or
            null, the language in this `Builder` is removed.  Otherwise,
            the language must be <a href="./Locale.html#def_language">well-formed</a>
            or an exception is thrown.
            
            The typical language value is a two or three-letter language
            code as defined in ISO639.

            Arguments
            - language: the language

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `language` is ill-formed
            """
            ...


        def setScript(self, script: str) -> "Builder":
            """
            Sets the script. If `script` is null or the empty string,
            the script in this `Builder` is removed.
            Otherwise, the script must be <a href="./Locale.html#def_script">well-formed</a> or an
            exception is thrown.
            
            The typical script value is a four-letter script code as defined by ISO 15924.

            Arguments
            - script: the script

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `script` is ill-formed
            """
            ...


        def setRegion(self, region: str) -> "Builder":
            """
            Sets the region.  If region is null or the empty string, the region
            in this `Builder` is removed.  Otherwise,
            the region must be <a href="./Locale.html#def_region">well-formed</a> or an
            exception is thrown.
            
            The typical region value is a two-letter ISO 3166 code or a
            three-digit UN M.49 area code.
            
            The country value in the `Locale` created by the
            `Builder` is always normalized to upper case.

            Arguments
            - region: the region

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `region` is ill-formed
            """
            ...


        def setVariant(self, variant: str) -> "Builder":
            """
            Sets the variant.  If variant is null or the empty string, the
            variant in this `Builder` is removed.  Otherwise, it
            must consist of one or more <a href="./Locale.html#def_variant">well-formed</a>
            subtags, or an exception is thrown.
            
            **Note:** This method checks if `variant`
            satisfies the IETF BCP 47 variant subtag's syntax requirements,
            and normalizes the value to lowercase letters.  However,
            the `Locale` class does not impose any syntactic
            restriction on variant, and the variant value in
            `Locale` is case sensitive.  To set such a variant,
            use a Locale constructor.

            Arguments
            - variant: the variant

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `variant` is ill-formed
            """
            ...


        def setExtension(self, key: str, value: str) -> "Builder":
            """
            Sets the extension for the given key. If the value is null or the
            empty string, the extension is removed.  Otherwise, the extension
            must be <a href="./Locale.html#def_extensions">well-formed</a> or an exception
            is thrown.
            
            **Note:** The key Locale.UNICODE_LOCALE_EXTENSION
            UNICODE_LOCALE_EXTENSION ('u') is used for the Unicode locale extension.
            Setting a value for this key replaces any existing Unicode locale key/type
            pairs with those defined in the extension.
            
            **Note:** The key Locale.PRIVATE_USE_EXTENSION
            PRIVATE_USE_EXTENSION ('x') is used for the private use code. To be
            well-formed, the value for this key needs only to have subtags of one to
            eight alphanumeric characters, not two to eight as in the general case.

            Arguments
            - key: the extension key
            - value: the extension value

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `key` is illegal
            or `value` is ill-formed

            See
            - .setUnicodeLocaleKeyword(String, String)
            """
            ...


        def setUnicodeLocaleKeyword(self, key: str, type: str) -> "Builder":
            """
            Sets the Unicode locale keyword type for the given key.  If the type
            is null, the Unicode keyword is removed.  Otherwise, the key must be
            non-null and both key and type must be <a
            href="./Locale.html#def_locale_extension">well-formed</a> or an exception
            is thrown.
            
            Keys and types are converted to lower case.
            
            **Note**:Setting the 'u' extension via .setExtension
            replaces all Unicode locale keywords with those defined in the
            extension.

            Arguments
            - key: the Unicode locale key
            - type: the Unicode locale type

            Returns
            - This builder.

            Raises
            - IllformedLocaleException: if `key` or `type`
            is ill-formed
            - NullPointerException: if `key` is null

            See
            - .setExtension(char, String)
            """
            ...


        def addUnicodeLocaleAttribute(self, attribute: str) -> "Builder":
            """
            Adds a unicode locale attribute, if not already present, otherwise
            has no effect.  The attribute must not be null and must be <a
            href="./Locale.html#def_locale_extension">well-formed</a> or an exception
            is thrown.

            Arguments
            - attribute: the attribute

            Returns
            - This builder.

            Raises
            - NullPointerException: if `attribute` is null
            - IllformedLocaleException: if `attribute` is ill-formed

            See
            - .setExtension(char, String)
            """
            ...


        def removeUnicodeLocaleAttribute(self, attribute: str) -> "Builder":
            """
            Removes a unicode locale attribute, if present, otherwise has no
            effect.  The attribute must not be null and must be <a
            href="./Locale.html#def_locale_extension">well-formed</a> or an exception
            is thrown.
            
            Attribute comparison for removal is case-insensitive.

            Arguments
            - attribute: the attribute

            Returns
            - This builder.

            Raises
            - NullPointerException: if `attribute` is null
            - IllformedLocaleException: if `attribute` is ill-formed

            See
            - .setExtension(char, String)
            """
            ...


        def clear(self) -> "Builder":
            """
            Resets the builder to its initial, empty state.

            Returns
            - This builder.
            """
            ...


        def clearExtensions(self) -> "Builder":
            """
            Resets the extensions to their initial, empty state.
            Language, script, region and variant are unchanged.

            Returns
            - This builder.

            See
            - .setExtension(char, String)
            """
            ...


        def build(self) -> "Locale":
            """
            Returns an instance of `Locale` created from the fields set
            on this builder.
            
            This applies the conversions listed in Locale.forLanguageTag
            when constructing a Locale. (Legacy tags are handled in
            .setLanguageTag.)

            Returns
            - A Locale.
            """
            ...


    class LanguageRange:
        """
        This class expresses a *Language Range* defined in
        <a href="http://tools.ietf.org/html/rfc4647">RFC 4647 Matching of
        Language Tags</a>. A language range is an identifier which is used to
        select language tag(s) meeting specific requirements by using the
        mechanisms described in <a href="Locale.html#LocaleMatching">Locale
        Matching</a>. A list which represents a user's preferences and consists
        of language ranges is called a *Language Priority List*.
        
        There are two types of language ranges: basic and extended. In RFC
        4647, the syntax of language ranges is expressed in
        <a href="http://tools.ietf.org/html/rfc4234">ABNF</a> as follows:
        <blockquote>
        ```
            basic-language-range    = (1*8ALPHA *("-" 1*8alphanum)) / "*"
            extended-language-range = (1*8ALPHA / "*")
                                      *("-" (1*8alphanum / "*"))
            alphanum                = ALPHA / DIGIT
        ```
        </blockquote>
        For example, `"en"` (English), `"ja-JP"` (Japanese, Japan),
        `"*"` (special language range which matches any language tag) are
        basic language ranges, whereas `"*-CH"` (any languages,
        Switzerland), `"es-*"` (Spanish, any regions), and
        `"zh-Hant-*"` (Traditional Chinese, any regions) are extended
        language ranges.

        See
        - .lookupTag

        Since
        - 1.8
        """

        MAX_WEIGHT = 1.0
        """
        A constant holding the maximum value of weight, 1.0, which indicates
        that the language range is a good fit for the user.
        """
        MIN_WEIGHT = 0.0
        """
        A constant holding the minimum value of weight, 0.0, which indicates
        that the language range is not a good fit for the user.
        """


        def __init__(self, range: str):
            """
            Constructs a `LanguageRange` using the given `range`.
            Note that no validation is done against the IANA Language Subtag
            Registry at time of construction.
            
            This is equivalent to `LanguageRange(range, MAX_WEIGHT)`.

            Arguments
            - range: a language range

            Raises
            - NullPointerException: if the given `range` is
                `null`
            - IllegalArgumentException: if the given `range` does not
            comply with the syntax of the language range mentioned in RFC 4647
            """
            ...


        def __init__(self, range: str, weight: float):
            """
            Constructs a `LanguageRange` using the given `range` and
            `weight`. Note that no validation is done against the IANA
            Language Subtag Registry at time of construction.

            Arguments
            - range: a language range
            - weight: a weight value between `MIN_WEIGHT` and
                `MAX_WEIGHT`

            Raises
            - NullPointerException: if the given `range` is
                `null`
            - IllegalArgumentException: if the given `range` does not
            comply with the syntax of the language range mentioned in RFC 4647
            or if the given `weight` is less than `MIN_WEIGHT`
            or greater than `MAX_WEIGHT`
            """
            ...


        def getRange(self) -> str:
            """
            Returns the language range of this `LanguageRange`.

            Returns
            - the language range.
            """
            ...


        def getWeight(self) -> float:
            """
            Returns the weight of this `LanguageRange`.

            Returns
            - the weight value.
            """
            ...


        @staticmethod
        def parse(ranges: str) -> list["LanguageRange"]:
            """
            Parses the given `ranges` to generate a Language Priority List.
            
            This method performs a syntactic check for each language range in
            the given `ranges` but doesn't do validation using the IANA
            Language Subtag Registry.
            
            The `ranges` to be given can take one of the following
            forms:
            
            ```
              "Accept-Language: ja,en;q=0.4"  (weighted list with Accept-Language prefix)
              "ja,en;q=0.4"                   (weighted list)
              "ja,en"                         (prioritized list)
            ```
            
            In a weighted list, each language range is given a weight value.
            The weight value is identical to the "quality value" in
            <a href="http://tools.ietf.org/html/rfc2616">RFC 2616</a>, and it
            expresses how much the user prefers  the language. A weight value is
            specified after a corresponding language range followed by
            `";q="`, and the default weight value is `MAX_WEIGHT`
            when it is omitted.
            
            Unlike a weighted list, language ranges in a prioritized list
            are sorted in the descending order based on its priority. The first
            language range has the highest priority and meets the user's
            preference most.
            
            In either case, language ranges are sorted in descending order in
            the Language Priority List based on priority or weight. If a
            language range appears in the given `ranges` more than once,
            only the first one is included on the Language Priority List.
            
            The returned list consists of language ranges from the given
            `ranges` and their equivalents found in the IANA Language
            Subtag Registry. For example, if the given `ranges` is
            `"Accept-Language: iw,en-us;q=0.7,en;q=0.3"`, the elements in
            the list to be returned are:
            
            ```
             **Range**                                   **Weight**
               "iw" (older tag for Hebrew)             1.0
               "he" (new preferred code for Hebrew)    1.0
               "en-us" (English, United States)        0.7
               "en" (English)                          0.3
            ```
            
            Two language ranges, `"iw"` and `"he"`, have the same
            highest priority in the list. By adding `"he"` to the user's
            Language Priority List, locale-matching method can find Hebrew as a
            matching locale (or language tag) even if the application or system
            offers only `"he"` as a supported locale (or language tag).

            Arguments
            - ranges: a list of comma-separated language ranges or a list of
                language ranges in the form of the "Accept-Language" header
                defined in <a href="http://tools.ietf.org/html/rfc2616">RFC
                2616</a>

            Returns
            - a Language Priority List consisting of language ranges
                included in the given `ranges` and their equivalent
                language ranges if available. The list is modifiable.

            Raises
            - NullPointerException: if `ranges` is null
            - IllegalArgumentException: if a language range or a weight
                found in the given `ranges` is ill-formed
            """
            ...


        @staticmethod
        def parse(ranges: str, map: dict[str, list[str]]) -> list["LanguageRange"]:
            """
            Parses the given `ranges` to generate a Language Priority
            List, and then customizes the list using the given `map`.
            This method is equivalent to
            `mapEquivalents(parse(ranges), map)`.

            Arguments
            - ranges: a list of comma-separated language ranges or a list
                of language ranges in the form of the "Accept-Language" header
                defined in <a href="http://tools.ietf.org/html/rfc2616">RFC
                2616</a>
            - map: a map containing information to customize language ranges

            Returns
            - a Language Priority List with customization. The list is
                modifiable.

            Raises
            - NullPointerException: if `ranges` is null
            - IllegalArgumentException: if a language range or a weight
                found in the given `ranges` is ill-formed

            See
            - .mapEquivalents
            """
            ...


        @staticmethod
        def mapEquivalents(priorityList: list["LanguageRange"], map: dict[str, list[str]]) -> list["LanguageRange"]:
            """
            Generates a new customized Language Priority List using the given
            `priorityList` and `map`. If the given `map` is
            empty, this method returns a copy of the given `priorityList`.
            
            In the map, a key represents a language range whereas a value is
            a list of equivalents of it. `'*'` cannot be used in the map.
            Each equivalent language range has the same weight value as its
            original language range.
            
            ```
             An example of map:
               **Key**                            **Value**
                 "zh" (Chinese)                 "zh",
                                                "zh-Hans"(Simplified Chinese)
                 "zh-HK" (Chinese, Hong Kong)   "zh-HK"
                 "zh-TW" (Chinese, Taiwan)      "zh-TW"
            ```
            
            The customization is performed after modification using the IANA
            Language Subtag Registry.
            
            For example, if a user's Language Priority List consists of five
            language ranges (`"zh"`, `"zh-CN"`, `"en"`,
            `"zh-TW"`, and `"zh-HK"`), the newly generated Language
            Priority List which is customized using the above map example will
            consists of `"zh"`, `"zh-Hans"`, `"zh-CN"`,
            `"zh-Hans-CN"`, `"en"`, `"zh-TW"`, and
            `"zh-HK"`.
            
            `"zh-HK"` and `"zh-TW"` aren't converted to
            `"zh-Hans-HK"` nor `"zh-Hans-TW"` even if they are
            included in the Language Priority List. In this example, mapping
            is used to clearly distinguish Simplified Chinese and Traditional
            Chinese.
            
            If the `"zh"`-to-`"zh"` mapping isn't included in the
            map, a simple replacement will be performed and the customized list
            won't include `"zh"` and `"zh-CN"`.

            Arguments
            - priorityList: user's Language Priority List
            - map: a map containing information to customize language ranges

            Returns
            - a new Language Priority List with customization. The list is
                modifiable.

            Raises
            - NullPointerException: if `priorityList` is `null`

            See
            - .parse(String, Map)
            """
            ...


        def hashCode(self) -> int:
            """
            Returns a hash code value for the object.

            Returns
            - a hash code value for this object.
            """
            ...


        def equals(self, obj: "Object") -> bool:
            """
            Compares this object to the specified object. The result is True if
            and only if the argument is not `null` and is a
            `LanguageRange` object that contains the same `range`
            and `weight` values as this object.

            Arguments
            - obj: the object to compare with

            Returns
            - `True` if this object's `range` and
                `weight` are the same as the `obj`'s; `False`
                otherwise.
            """
            ...


        def toString(self) -> str:
            """
            Returns an informative string representation of this `LanguageRange`
            object, consisting of language range and weight if the range is
            weighted and the weight is less than the max weight.

            Returns
            - a string representation of this `LanguageRange` object.
            """
            ...


    class IsoCountryCode(Enum):
        """
        Enum for specifying the type defined in ISO 3166. This enum is used to
        retrieve the two-letter ISO3166-1 alpha-2, three-letter ISO3166-1
        alpha-3, four-letter ISO3166-3 country codes.

        See
        - .getISOCountries(Locale.IsoCountryCode)

        Since
        - 9
        """

        PART1_ALPHA2 = 0
        """
        PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
        country codes.
        """
        PART1_ALPHA3 = 1
        """
        PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
        country codes.
        """
        PART3 = 2
        """
        PART3 is used to represent the ISO3166-3 four letter country codes.
        """


    class Category(Enum):
        """
        Enum for locale categories.  These locale categories are used to get/set
        the default locale for the specific functionality represented by the
        category.

        See
        - .setDefault(Locale.Category, Locale)

        Since
        - 1.7
        """

        DISPLAY = ("user.language.display", "user.script.display", "user.country.display", "user.variant.display", "user.extensions.display")
        """
        Category used to represent the default locale for
        displaying user interfaces.
        """
        FORMAT = ("user.language.format", "user.script.format", "user.country.format", "user.variant.format", "user.extensions.format")
        """
        Category used to represent the default locale for
        formatting dates, numbers, and/or currencies.
        """


    class FilteringMode(Enum):
        """
        This enum provides constants to select a filtering mode for locale
        matching. Refer to <a href="http://tools.ietf.org/html/rfc4647">RFC 4647
        Matching of Language Tags</a> for details.
        
        As an example, think of two Language Priority Lists each of which
        includes only one language range and a set of following language tags:
        
        ```
           de (German)
           de-DE (German, Germany)
           de-Deva (German, in Devanagari script)
           de-Deva-DE (German, in Devanagari script, Germany)
           de-DE-1996 (German, Germany, orthography of 1996)
           de-Latn-DE (German, in Latin script, Germany)
           de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
        ```
        
        The filtering method will behave as follows:
        
        <table class="striped">
        <caption>Filtering method behavior</caption>
        <thead>
        <tr>
        <th scope="col">Filtering Mode</th>
        <th scope="col">Language Priority List: `"de-DE"`</th>
        <th scope="col">Language Priority List: `"de-*-DE"`</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th scope="row" style="vertical-align:top">
        FilteringMode.AUTOSELECT_FILTERING AUTOSELECT_FILTERING
        </th>
        <td style="vertical-align:top">
        Performs *basic* filtering and returns `"de-DE"` and
        `"de-DE-1996"`.
        </td>
        <td style="vertical-align:top">
        Performs *extended* filtering and returns `"de-DE"`,
        `"de-Deva-DE"`, `"de-DE-1996"`, `"de-Latn-DE"`, and
        `"de-Latn-DE-1996"`.
        </td>
        </tr>
        <tr>
        <th scope="row" style="vertical-align:top">
        FilteringMode.EXTENDED_FILTERING EXTENDED_FILTERING
        </th>
        <td style="vertical-align:top">
        Performs *extended* filtering and returns `"de-DE"`,
        `"de-Deva-DE"`, `"de-DE-1996"`, `"de-Latn-DE"`, and
        `"de-Latn-DE-1996"`.
        </td>
        <td style="vertical-align:top">Same as above.</td>
        </tr>
        <tr>
        <th scope="row" style="vertical-align:top">
        FilteringMode.IGNORE_EXTENDED_RANGES IGNORE_EXTENDED_RANGES
        </th>
        <td style="vertical-align:top">
        Performs *basic* filtering and returns `"de-DE"` and
        `"de-DE-1996"`.
        </td>
        <td style="vertical-align:top">
        Performs *basic* filtering and returns `null` because
        nothing matches.
        </td>
        </tr>
        <tr>
        <th scope="row" style="vertical-align:top">
        FilteringMode.MAP_EXTENDED_RANGES MAP_EXTENDED_RANGES
        </th>
        <td style="vertical-align:top">Same as above.</td>
        <td style="vertical-align:top">
        Performs *basic* filtering and returns `"de-DE"` and
        `"de-DE-1996"` because `"de-*-DE"` is mapped to
        `"de-DE"`.
        </td>
        </tr>
        <tr>
        <th scope="row" style="vertical-align:top">
        FilteringMode.REJECT_EXTENDED_RANGES REJECT_EXTENDED_RANGES
        </th>
        <td style="vertical-align:top">Same as above.</td>
        <td style="vertical-align:top">
        Throws IllegalArgumentException because `"de-*-DE"` is
        not a valid basic language range.
        </td>
        </tr>
        </tbody>
        </table>

        See
        - .filterTags(List, Collection, FilteringMode)

        Since
        - 1.8
        """

        AUTOSELECT_FILTERING = 0
        """
        Specifies automatic filtering mode based on the given Language
        Priority List consisting of language ranges. If all of the ranges
        are basic, basic filtering is selected. Otherwise, extended
        filtering is selected.
        """
        EXTENDED_FILTERING = 1
        """
        Specifies extended filtering.
        """
        IGNORE_EXTENDED_RANGES = 2
        """
        Specifies basic filtering: Note that any extended language ranges
        included in the given Language Priority List are ignored.
        """
        MAP_EXTENDED_RANGES = 3
        """
        Specifies basic filtering: If any extended language ranges are
        included in the given Language Priority List, they are mapped to the
        basic language range. Specifically, a language range starting with a
        subtag `"*"` is treated as a language range `"*"`. For
        example, `"*-US"` is treated as `"*"`. If `"*"` is
        not the first subtag, `"*"` and extra `"-"` are removed.
        For example, `"ja-*-JP"` is mapped to `"ja-JP"`.
        """
        REJECT_EXTENDED_RANGES = 4
        """
        Specifies basic filtering: If any extended language ranges are
        included in the given Language Priority List, the list is rejected
        and the filtering method throws IllegalArgumentException.
        """
