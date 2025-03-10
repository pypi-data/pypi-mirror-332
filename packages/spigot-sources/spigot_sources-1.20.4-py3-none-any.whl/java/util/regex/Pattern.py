"""
Python module generated from Java source file java.util.regex.Pattern

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import Normalizer
from java.text.Normalizer import Form
from java.util import Arrays
from java.util import Iterator
from java.util import LinkedHashSet
from java.util import Locale
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.function import Predicate
from java.util.regex import *
from java.util.stream import Stream
from java.util.stream import StreamSupport
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class Pattern(Serializable):

    UNIX_LINES = 0x01
    """
    Enables Unix lines mode.
    
     In this mode, only the `'\n'` line terminator is recognized
    in the behavior of `.`, `^`, and `$`.
    
     Unix lines mode can also be enabled via the embedded flag
    expression&nbsp;`(?d)`.
    """
    CASE_INSENSITIVE = 0x02
    """
    Enables case-insensitive matching.
    
     By default, case-insensitive matching assumes that only characters
    in the US-ASCII charset are being matched.  Unicode-aware
    case-insensitive matching can be enabled by specifying the .UNICODE_CASE flag in conjunction with this flag.
    
     Case-insensitive matching can also be enabled via the embedded flag
    expression&nbsp;`(?i)`.
    
     Specifying this flag may impose a slight performance penalty.  
    """
    COMMENTS = 0x04
    """
    Permits whitespace and comments in pattern.
    
     In this mode, whitespace is ignored, and embedded comments starting
    with `.` are ignored until the end of a line.
    
     Comments mode can also be enabled via the embedded flag
    expression&nbsp;`(?x)`.
    """
    MULTILINE = 0x08
    """
    Enables multiline mode.
    
     In multiline mode the expressions `^` and `$` match
    just after or just before, respectively, a line terminator or the end of
    the input sequence.  By default these expressions only match at the
    beginning and the end of the entire input sequence.
    
     Multiline mode can also be enabled via the embedded flag
    expression&nbsp;`(?m)`.  
    """
    LITERAL = 0x10
    """
    Enables literal parsing of the pattern.
    
     When this flag is specified then the input string that specifies
    the pattern is treated as a sequence of literal characters.
    Metacharacters or escape sequences in the input sequence will be
    given no special meaning.
    
    The flags CASE_INSENSITIVE and UNICODE_CASE retain their impact on
    matching when used in conjunction with this flag. The other flags
    become superfluous.
    
     There is no embedded flag character for enabling literal parsing.

    Since
    - 1.5
    """
    DOTALL = 0x20
    """
    Enables dotall mode.
    
     In dotall mode, the expression `.` matches any character,
    including a line terminator.  By default this expression does not match
    line terminators.
    
     Dotall mode can also be enabled via the embedded flag
    expression&nbsp;`(?s)`.  (The `s` is a mnemonic for
    "single-line" mode, which is what this is called in Perl.)  
    """
    UNICODE_CASE = 0x40
    """
    Enables Unicode-aware case folding.
    
     When this flag is specified then case-insensitive matching, when
    enabled by the .CASE_INSENSITIVE flag, is done in a manner
    consistent with the Unicode Standard.  By default, case-insensitive
    matching assumes that only characters in the US-ASCII charset are being
    matched.
    
     Unicode-aware case folding can also be enabled via the embedded flag
    expression&nbsp;`(?u)`.
    
     Specifying this flag may impose a performance penalty.  
    """
    CANON_EQ = 0x80
    """
    Enables canonical equivalence.
    
     When this flag is specified then two characters will be considered
    to match if, and only if, their full canonical decompositions match.
    The expression `"a&#92;u030A"`, for example, will match the
    string `"&#92;u00E5"` when this flag is specified.  By default,
    matching does not take canonical equivalence into account.
    
     There is no embedded flag character for enabling canonical
    equivalence.
    
     Specifying this flag may impose a performance penalty.  
    """
    UNICODE_CHARACTER_CLASS = 0x100
    """
    Enables the Unicode version of *Predefined character classes* and
    *POSIX character classes*.
    
     When this flag is specified then the (US-ASCII only)
    *Predefined character classes* and *POSIX character classes*
    are in conformance with
    <a href="http://www.unicode.org/reports/tr18/">*Unicode Technical
    Standard #18: Unicode Regular Expressions*</a>
    *Annex C: Compatibility Properties*.
    
    The UNICODE_CHARACTER_CLASS mode can also be enabled via the embedded
    flag expression&nbsp;`(?U)`.
    
    The flag implies UNICODE_CASE, that is, it enables Unicode-aware case
    folding.
    
    Specifying this flag may impose a performance penalty.  

    Since
    - 1.7
    """


    @staticmethod
    def compile(regex: str) -> "Pattern":
        """
        Compiles the given regular expression into a pattern.

        Arguments
        - regex: The expression to be compiled

        Returns
        - the given regular expression compiled into a pattern

        Raises
        - PatternSyntaxException: If the expression's syntax is invalid
        """
        ...


    @staticmethod
    def compile(regex: str, flags: int) -> "Pattern":
        """
        Compiles the given regular expression into a pattern with the given
        flags.

        Arguments
        - regex: The expression to be compiled
        - flags: Match flags, a bit mask that may include
                .CASE_INSENSITIVE, .MULTILINE, .DOTALL,
                .UNICODE_CASE, .CANON_EQ, .UNIX_LINES,
                .LITERAL, .UNICODE_CHARACTER_CLASS
                and .COMMENTS

        Returns
        - the given regular expression compiled into a pattern with the given flags

        Raises
        - IllegalArgumentException: If bit values other than those corresponding to the defined
                 match flags are set in `flags`
        - PatternSyntaxException: If the expression's syntax is invalid
        """
        ...


    def pattern(self) -> str:
        """
        Returns the regular expression from which this pattern was compiled.

        Returns
        - The source of this pattern
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this pattern. This
        is the regular expression from which this pattern was
        compiled.

        Returns
        - The string representation of this pattern

        Since
        - 1.5
        """
        ...


    def matcher(self, input: "CharSequence") -> "Matcher":
        """
        Creates a matcher that will match the given input against this pattern.

        Arguments
        - input: The character sequence to be matched

        Returns
        - A new matcher for this pattern
        """
        ...


    def flags(self) -> int:
        """
        Returns this pattern's match flags.

        Returns
        - The match flags specified when this pattern was compiled
        """
        ...


    @staticmethod
    def matches(regex: str, input: "CharSequence") -> bool:
        """
        Compiles the given regular expression and attempts to match the given
        input against it.
        
         An invocation of this convenience method of the form
        
        <blockquote>```
        Pattern.matches(regex, input);```</blockquote>
        
        behaves in exactly the same way as the expression
        
        <blockquote>```
        Pattern.compile(regex).matcher(input).matches()```</blockquote>
        
         If a pattern is to be used multiple times, compiling it once and reusing
        it will be more efficient than invoking this method each time.  

        Arguments
        - regex: The expression to be compiled
        - input: The character sequence to be matched

        Returns
        - whether or not the regular expression matches on the input

        Raises
        - PatternSyntaxException: If the expression's syntax is invalid
        """
        ...


    def split(self, input: "CharSequence", limit: int) -> list[str]:
        """
        Splits the given input sequence around matches of this pattern.
        
         The array returned by this method contains each substring of the
        input sequence that is terminated by another subsequence that matches
        this pattern or is terminated by the end of the input sequence.  The
        substrings in the array are in the order in which they occur in the
        input. If this pattern does not match any subsequence of the input then
        the resulting array has just one element, namely the input sequence in
        string form.
        
         When there is a positive-width match at the beginning of the input
        sequence then an empty leading substring is included at the beginning
        of the resulting array. A zero-width match at the beginning however
        never produces such empty leading substring.
        
         The `limit` parameter controls the number of times the
        pattern is applied and therefore affects the length of the resulting
        array.
        
           - 
           If the *limit* is positive then the pattern will be applied
           at most *limit*&nbsp;-&nbsp;1 times, the array's length will be
           no greater than *limit*, and the array's last entry will contain
           all input beyond the last matched delimiter.
        
           - 
           If the *limit* is zero then the pattern will be applied as
           many times as possible, the array can have any length, and trailing
           empty strings will be discarded.
        
           - 
           If the *limit* is negative then the pattern will be applied
           as many times as possible and the array can have any length.
        
        
         The input `"boo:and:foo"`, for example, yields the following
        results with these parameters:
        
        <table class="plain" style="margin-left:2em;">
        <caption style="display:none">Split example showing regex, limit, and result</caption>
        <thead>
        <tr>
            <th scope="col">Regex</th>
            <th scope="col">Limit</th>
            <th scope="col">Result</th>
        </tr>
        </thead>
        <tbody>
        <tr><th scope="row" rowspan="3" style="font-weight:normal">:</th>
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">2</th>
            <td>`{ "boo", "and:foo"`}</td></tr>
        <tr><!-- : -->
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
            <td>`{ "boo", "and", "foo"`}</td></tr>
        <tr><!-- : -->
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-2</th>
            <td>`{ "boo", "and", "foo"`}</td></tr>
        <tr><th scope="row" rowspan="3" style="font-weight:normal">o</th>
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
            <td>`{ "b", "", ":and:f", "", ""`}</td></tr>
        <tr><!-- o -->
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-2</th>
            <td>`{ "b", "", ":and:f", "", ""`}</td></tr>
        <tr><!-- o -->
            <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">0</th>
            <td>`{ "b", "", ":and:f"`}</td></tr>
        </tbody>
        </table>

        Arguments
        - input: The character sequence to be split
        - limit: The result threshold, as described above

        Returns
        - The array of strings computed by splitting the input
                 around matches of this pattern
        """
        ...


    def split(self, input: "CharSequence") -> list[str]:
        """
        Splits the given input sequence around matches of this pattern.
        
         This method works as if by invoking the two-argument .split(java.lang.CharSequence, int) split method with the given input
        sequence and a limit argument of zero.  Trailing empty strings are
        therefore not included in the resulting array. 
        
         The input `"boo:and:foo"`, for example, yields the following
        results with these expressions:
        
        <table class="plain" style="margin-left:2em">
        <caption style="display:none">Split examples showing regex and result</caption>
        <thead>
        <tr>
         <th scope="col">Regex</th>
         <th scope="col">Result</th>
        </tr>
        </thead>
        <tbody>
        <tr><th scope="row" style="text-weight:normal">:</th>
            <td>`{ "boo", "and", "foo"`}</td></tr>
        <tr><th scope="row" style="text-weight:normal">o</th>
            <td>`{ "b", "", ":and:f"`}</td></tr>
        </tbody>
        </table>

        Arguments
        - input: The character sequence to be split

        Returns
        - The array of strings computed by splitting the input
                 around matches of this pattern
        """
        ...


    @staticmethod
    def quote(s: str) -> str:
        """
        Returns a literal pattern `String` for the specified
        `String`.
        
        This method produces a `String` that can be used to
        create a `Pattern` that would match the string
        `s` as if it were a literal pattern. Metacharacters
        or escape sequences in the input sequence will be given no special
        meaning.

        Arguments
        - s: The string to be literalized

        Returns
        - A literal string replacement

        Since
        - 1.5
        """
        ...


    def asPredicate(self) -> "Predicate"[str]:
        """
        Creates a predicate that tests if this pattern is found in a given input
        string.

        Returns
        - The predicate which can be used for finding a match on a
                 subsequence of a string

        See
        - Matcher.find

        Since
        - 1.8

        Unknown Tags
        - This method creates a predicate that behaves as if it creates a matcher
        from the input sequence and then calls `find`, for example a
        predicate of the form:
        ````s -> matcher(s).find();````
        """
        ...


    def asMatchPredicate(self) -> "Predicate"[str]:
        """
        Creates a predicate that tests if this pattern matches a given input string.

        Returns
        - The predicate which can be used for matching an input string
                 against this pattern.

        See
        - Matcher.matches

        Since
        - 11

        Unknown Tags
        - This method creates a predicate that behaves as if it creates a matcher
        from the input sequence and then calls `matches`, for example a
        predicate of the form:
        ````s -> matcher(s).matches();````
        """
        ...


    def splitAsStream(self, input: "CharSequence") -> "Stream"[str]:
        """
        Creates a stream from the given input sequence around matches of this
        pattern.
        
         The stream returned by this method contains each substring of the
        input sequence that is terminated by another subsequence that matches
        this pattern or is terminated by the end of the input sequence.  The
        substrings in the stream are in the order in which they occur in the
        input. Trailing empty strings will be discarded and not encountered in
        the stream.
        
         If this pattern does not match any subsequence of the input then
        the resulting stream has just one element, namely the input sequence in
        string form.
        
         When there is a positive-width match at the beginning of the input
        sequence then an empty leading substring is included at the beginning
        of the stream. A zero-width match at the beginning however never produces
        such empty leading substring.
        
         If the input sequence is mutable, it must remain constant during the
        execution of the terminal stream operation.  Otherwise, the result of the
        terminal stream operation is undefined.

        Arguments
        - input: The character sequence to be split

        Returns
        - The stream of strings computed by splitting the input
                 around matches of this pattern

        See
        - .split(CharSequence)

        Since
        - 1.8
        """
        ...
