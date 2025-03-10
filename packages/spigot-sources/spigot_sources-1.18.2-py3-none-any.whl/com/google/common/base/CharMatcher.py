"""
Python module generated from Java source file com.google.common.base.CharMatcher

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from java.util import Arrays
from java.util import BitSet
from typing import Any, Callable, Iterable, Tuple


class CharMatcher(Predicate):
    """
    Determines a True or False value for any Java `char` value, just as Predicate does
    for any Object. Also offers basic text processing methods based on this function.
    Implementations are strongly encouraged to be side-effect-free and immutable.
    
    Throughout the documentation of this class, the phrase "matching character" is used to mean
    "any `char` value `c` for which `this.matches(c)` returns `True`".
    
    **Warning:** This class deals only with `char` values, that is, <a
    href="http://www.unicode.org/glossary/#BMP_character">BMP characters</a>. It does not understand
    <a href="http://www.unicode.org/glossary/#supplementary_code_point">supplementary Unicode code
    points</a> in the range `0x10000` to `0x10FFFF` which includes the majority of
    assigned characters, including important CJK characters and emoji.
    
    Supplementary characters are <a
    href="https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#supplementary">encoded
    into a `String` using surrogate pairs</a>, and a `CharMatcher` treats these just as
    two separate characters. .countIn counts each supplementary character as 2 `char`s.
    
    For up-to-date Unicode character properties (digit, letter, etc.) and support for
    supplementary code points, use ICU4J UCharacter and UnicodeSet (freeze() after building). For
    basic text processing based on UnicodeSet use the ICU4J UnicodeSetSpanner.
    
    Example usages:
    
    ```
      String trimmed = .whitespace() whitespace()..trimFrom trimFrom(userInput);
      if (.ascii() ascii()..matchesAllOf matchesAllOf(s)) { ... }```
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/StringsExplained#charmatcher">`CharMatcher`
    </a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    @staticmethod
    def any() -> "CharMatcher":
        """
        Matches any character.

        Since
        - 19.0 (since 1.0 as constant `ANY`)
        """
        ...


    @staticmethod
    def none() -> "CharMatcher":
        """
        Matches no characters.

        Since
        - 19.0 (since 1.0 as constant `NONE`)
        """
        ...


    @staticmethod
    def whitespace() -> "CharMatcher":
        """
        Determines whether a character is whitespace according to the latest Unicode standard, as
        illustrated <a
        href="http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5Cp%7Bwhitespace%7D">here</a>.
        This is not the same definition used by other Java APIs. (See a <a
        href="https://goo.gl/Y6SLWx">comparison of several definitions of "whitespace"</a>.)
        
        All Unicode White_Space characters are on the BMP and thus supported by this API.
        
        **Note:** as the Unicode definition evolves, we will modify this matcher to keep it up to
        date.

        Since
        - 19.0 (since 1.0 as constant `WHITESPACE`)
        """
        ...


    @staticmethod
    def breakingWhitespace() -> "CharMatcher":
        """
        Determines whether a character is a breaking whitespace (that is, a whitespace which can be
        interpreted as a break between words for formatting purposes). See .whitespace() for a
        discussion of that term.

        Since
        - 19.0 (since 2.0 as constant `BREAKING_WHITESPACE`)
        """
        ...


    @staticmethod
    def ascii() -> "CharMatcher":
        """
        Determines whether a character is ASCII, meaning that its code point is less than 128.

        Since
        - 19.0 (since 1.0 as constant `ASCII`)
        """
        ...


    @staticmethod
    def digit() -> "CharMatcher":
        """
        Determines whether a character is a BMP digit according to <a
        href="http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5Cp%7Bdigit%7D">Unicode</a>. If
        you only care to match ASCII digits, you can use `inRange('0', '9')`.

        Since
        - 19.0 (since 1.0 as constant `DIGIT`)

        Deprecated
        - Many digits are supplementary characters; see the class documentation.
        """
        ...


    @staticmethod
    def javaDigit() -> "CharMatcher":
        """
        Determines whether a character is a BMP digit according to Character.isDigit(char)
        Java's definition. If you only care to match ASCII digits, you can use `inRange('0',
        '9')`.

        Since
        - 19.0 (since 1.0 as constant `JAVA_DIGIT`)

        Deprecated
        - Many digits are supplementary characters; see the class documentation.
        """
        ...


    @staticmethod
    def javaLetter() -> "CharMatcher":
        """
        Determines whether a character is a BMP letter according to Character.isLetter(char) Java's definition. If you only care to match letters of the Latin
        alphabet, you can use `inRange('a', 'z').or(inRange('A', 'Z'))`.

        Since
        - 19.0 (since 1.0 as constant `JAVA_LETTER`)

        Deprecated
        - Most letters are supplementary characters; see the class documentation.
        """
        ...


    @staticmethod
    def javaLetterOrDigit() -> "CharMatcher":
        """
        Determines whether a character is a BMP letter or digit according to Character.isLetterOrDigit(char) Java's definition.

        Since
        - 19.0 (since 1.0 as constant `JAVA_LETTER_OR_DIGIT`).

        Deprecated
        - Most letters and digits are supplementary characters; see the class documentation.
        """
        ...


    @staticmethod
    def javaUpperCase() -> "CharMatcher":
        """
        Determines whether a BMP character is upper case according to Character.isUpperCase(char) Java's definition.

        Since
        - 19.0 (since 1.0 as constant `JAVA_UPPER_CASE`)

        Deprecated
        - Some uppercase characters are supplementary characters; see the class
            documentation.
        """
        ...


    @staticmethod
    def javaLowerCase() -> "CharMatcher":
        """
        Determines whether a BMP character is lower case according to Character.isLowerCase(char) Java's definition.

        Since
        - 19.0 (since 1.0 as constant `JAVA_LOWER_CASE`)

        Deprecated
        - Some lowercase characters are supplementary characters; see the class
            documentation.
        """
        ...


    @staticmethod
    def javaIsoControl() -> "CharMatcher":
        """
        Determines whether a character is an ISO control character as specified by Character.isISOControl(char).
        
        All ISO control codes are on the BMP and thus supported by this API.

        Since
        - 19.0 (since 1.0 as constant `JAVA_ISO_CONTROL`)
        """
        ...


    @staticmethod
    def invisible() -> "CharMatcher":
        """
        Determines whether a character is invisible; that is, if its Unicode category is any of
        SPACE_SEPARATOR, LINE_SEPARATOR, PARAGRAPH_SEPARATOR, CONTROL, FORMAT, SURROGATE, and
        PRIVATE_USE according to ICU4J.
        
        See also the Unicode Default_Ignorable_Code_Point property (available via ICU).

        Since
        - 19.0 (since 1.0 as constant `INVISIBLE`)

        Deprecated
        - Most invisible characters are supplementary characters; see the class
            documentation.
        """
        ...


    @staticmethod
    def singleWidth() -> "CharMatcher":
        """
        Determines whether a character is single-width (not double-width). When in doubt, this matcher
        errs on the side of returning `False` (that is, it tends to assume a character is
        double-width).
        
        **Note:** as the reference file evolves, we will modify this matcher to keep it up to
        date.
        
        See also <a href="http://www.unicode.org/reports/tr11/">UAX #11 East Asian Width</a>.

        Since
        - 19.0 (since 1.0 as constant `SINGLE_WIDTH`)

        Deprecated
        - Many such characters are supplementary characters; see the class documentation.
        """
        ...


    @staticmethod
    def is(match: str) -> "CharMatcher":
        """
        Returns a `char` matcher that matches only one specified BMP character.
        """
        ...


    @staticmethod
    def isNot(match: str) -> "CharMatcher":
        """
        Returns a `char` matcher that matches any character except the BMP character specified.
        
        To negate another `CharMatcher`, use .negate().
        """
        ...


    @staticmethod
    def anyOf(sequence: "CharSequence") -> "CharMatcher":
        """
        Returns a `char` matcher that matches any BMP character present in the given character
        sequence. Returns a bogus matcher if the sequence contains supplementary characters.
        """
        ...


    @staticmethod
    def noneOf(sequence: "CharSequence") -> "CharMatcher":
        """
        Returns a `char` matcher that matches any BMP character not present in the given
        character sequence. Returns a bogus matcher if the sequence contains supplementary characters.
        """
        ...


    @staticmethod
    def inRange(startInclusive: str, endInclusive: str) -> "CharMatcher":
        """
        Returns a `char` matcher that matches any character in a given BMP range (both endpoints
        are inclusive). For example, to match any lowercase letter of the English alphabet, use `CharMatcher.inRange('a', 'z')`.

        Raises
        - IllegalArgumentException: if `endInclusive < startInclusive`
        """
        ...


    @staticmethod
    def forPredicate(predicate: "Predicate"["Character"]) -> "CharMatcher":
        """
        Returns a matcher with identical behavior to the given Character-based predicate, but
        which operates on primitive `char` instances instead.
        """
        ...


    def matches(self, c: str) -> bool:
        """
        Determines a True or False value for the given character.
        """
        ...


    def negate(self) -> "CharMatcher":
        ...


    def and(self, other: "CharMatcher") -> "CharMatcher":
        """
        Returns a matcher that matches any character matched by both this matcher and `other`.
        """
        ...


    def or(self, other: "CharMatcher") -> "CharMatcher":
        """
        Returns a matcher that matches any character matched by either this matcher or `other`.
        """
        ...


    def precomputed(self) -> "CharMatcher":
        """
        Returns a `char` matcher functionally equivalent to this one, but which may be faster to
        query than the original; your mileage may vary. Precomputation takes time and is likely to be
        worthwhile only if the precomputed matcher is queried many thousands of times.
        
        This method has no effect (returns `this`) when called in GWT: it's unclear whether a
        precomputed matcher is faster, but it certainly consumes more memory, which doesn't seem like a
        worthwhile tradeoff in a browser.
        """
        ...


    def matchesAnyOf(self, sequence: "CharSequence") -> bool:
        """
        Returns `True` if a character sequence contains at least one matching BMP character.
        Equivalent to `!matchesNoneOf(sequence)`.
        
        The default implementation iterates over the sequence, invoking .matches for each
        character, until this returns `True` or the end is reached.

        Arguments
        - sequence: the character sequence to examine, possibly empty

        Returns
        - `True` if this matcher matches at least one character in the sequence

        Since
        - 8.0
        """
        ...


    def matchesAllOf(self, sequence: "CharSequence") -> bool:
        """
        Returns `True` if a character sequence contains only matching BMP characters.
        
        The default implementation iterates over the sequence, invoking .matches for each
        character, until this returns `False` or the end is reached.

        Arguments
        - sequence: the character sequence to examine, possibly empty

        Returns
        - `True` if this matcher matches every character in the sequence, including when
            the sequence is empty
        """
        ...


    def matchesNoneOf(self, sequence: "CharSequence") -> bool:
        """
        Returns `True` if a character sequence contains no matching BMP characters. Equivalent to
        `!matchesAnyOf(sequence)`.
        
        The default implementation iterates over the sequence, invoking .matches for each
        character, until this returns `True` or the end is reached.

        Arguments
        - sequence: the character sequence to examine, possibly empty

        Returns
        - `True` if this matcher matches no characters in the sequence, including when the
            sequence is empty
        """
        ...


    def indexIn(self, sequence: "CharSequence") -> int:
        """
        Returns the index of the first matching BMP character in a character sequence, or `-1` if
        no matching character is present.
        
        The default implementation iterates over the sequence in forward order calling .matches for each character.

        Arguments
        - sequence: the character sequence to examine from the beginning

        Returns
        - an index, or `-1` if no character matches
        """
        ...


    def indexIn(self, sequence: "CharSequence", start: int) -> int:
        """
        Returns the index of the first matching BMP character in a character sequence, starting from a
        given position, or `-1` if no character matches after that position.
        
        The default implementation iterates over the sequence in forward order, beginning at `start`, calling .matches for each character.

        Arguments
        - sequence: the character sequence to examine
        - start: the first index to examine; must be nonnegative and no greater than `sequence.length()`

        Returns
        - the index of the first matching character, guaranteed to be no less than `start`,
            or `-1` if no character matches

        Raises
        - IndexOutOfBoundsException: if start is negative or greater than `sequence.length()`
        """
        ...


    def lastIndexIn(self, sequence: "CharSequence") -> int:
        """
        Returns the index of the last matching BMP character in a character sequence, or `-1` if
        no matching character is present.
        
        The default implementation iterates over the sequence in reverse order calling .matches for each character.

        Arguments
        - sequence: the character sequence to examine from the end

        Returns
        - an index, or `-1` if no character matches
        """
        ...


    def countIn(self, sequence: "CharSequence") -> int:
        """
        Returns the number of matching `char`s found in a character sequence.
        
        Counts 2 per supplementary character, such as for .whitespace()..negate().
        """
        ...


    def removeFrom(self, sequence: "CharSequence") -> str:
        """
        Returns a string containing all non-matching characters of a character sequence, in order. For
        example:
        
        ````CharMatcher.is('a').removeFrom("bazaar")````
        
        ... returns `"bzr"`.
        """
        ...


    def retainFrom(self, sequence: "CharSequence") -> str:
        """
        Returns a string containing all matching BMP characters of a character sequence, in order. For
        example:
        
        ````CharMatcher.is('a').retainFrom("bazaar")````
        
        ... returns `"aaa"`.
        """
        ...


    def replaceFrom(self, sequence: "CharSequence", replacement: str) -> str:
        """
        Returns a string copy of the input character sequence, with each matching BMP character
        replaced by a given replacement character. For example:
        
        ````CharMatcher.is('a').replaceFrom("radar", 'o')````
        
        ... returns `"rodor"`.
        
        The default implementation uses .indexIn(CharSequence) to find the first matching
        character, then iterates the remainder of the sequence calling .matches(char) for each
        character.

        Arguments
        - sequence: the character sequence to replace matching characters in
        - replacement: the character to append to the result string in place of each matching
            character in `sequence`

        Returns
        - the new string
        """
        ...


    def replaceFrom(self, sequence: "CharSequence", replacement: "CharSequence") -> str:
        """
        Returns a string copy of the input character sequence, with each matching BMP character
        replaced by a given replacement sequence. For example:
        
        ````CharMatcher.is('a').replaceFrom("yaha", "oo")````
        
        ... returns `"yoohoo"`.
        
        **Note:** If the replacement is a fixed string with only one character, you are better
        off calling .replaceFrom(CharSequence, char) directly.

        Arguments
        - sequence: the character sequence to replace matching characters in
        - replacement: the characters to append to the result string in place of each matching
            character in `sequence`

        Returns
        - the new string
        """
        ...


    def trimFrom(self, sequence: "CharSequence") -> str:
        """
        Returns a substring of the input character sequence that omits all matching BMP characters from
        the beginning and from the end of the string. For example:
        
        ````CharMatcher.anyOf("ab").trimFrom("abacatbab")````
        
        ... returns `"cat"`.
        
        Note that:
        
        ````CharMatcher.inRange('\0', ' ').trimFrom(str)````
        
        ... is equivalent to String.trim().
        """
        ...


    def trimLeadingFrom(self, sequence: "CharSequence") -> str:
        """
        Returns a substring of the input character sequence that omits all matching BMP characters from
        the beginning of the string. For example:
        
        ````CharMatcher.anyOf("ab").trimLeadingFrom("abacatbab")````
        
        ... returns `"catbab"`.
        """
        ...


    def trimTrailingFrom(self, sequence: "CharSequence") -> str:
        """
        Returns a substring of the input character sequence that omits all matching BMP characters from
        the end of the string. For example:
        
        ````CharMatcher.anyOf("ab").trimTrailingFrom("abacatbab")````
        
        ... returns `"abacat"`.
        """
        ...


    def collapseFrom(self, sequence: "CharSequence", replacement: str) -> str:
        """
        Returns a string copy of the input character sequence, with each group of consecutive matching
        BMP characters replaced by a single replacement character. For example:
        
        ````CharMatcher.anyOf("eko").collapseFrom("bookkeeper", '-')````
        
        ... returns `"b-p-r"`.
        
        The default implementation uses .indexIn(CharSequence) to find the first matching
        character, then iterates the remainder of the sequence calling .matches(char) for each
        character.

        Arguments
        - sequence: the character sequence to replace matching groups of characters in
        - replacement: the character to append to the result string in place of each group of
            matching characters in `sequence`

        Returns
        - the new string
        """
        ...


    def trimAndCollapseFrom(self, sequence: "CharSequence", replacement: str) -> str:
        """
        Collapses groups of matching characters exactly as .collapseFrom does, except that
        groups of matching BMP characters at the start or end of the sequence are removed without
        replacement.
        """
        ...


    def apply(self, character: "Character") -> bool:
        """
        Deprecated
        - Provided only to satisfy the Predicate interface; use .matches
            instead.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this `CharMatcher`, such as `CharMatcher.or(WHITESPACE, JAVA_DIGIT)`.
        """
        ...
