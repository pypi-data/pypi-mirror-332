"""
Python module generated from Java source file com.google.common.base.Splitter

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import *
from java.util import Collections
from java.util import Iterator
from java.util.regex import Pattern
from java.util.stream import Stream
from java.util.stream import StreamSupport
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Splitter:
    """
    Extracts non-overlapping substrings from an input string, typically by recognizing appearances of
    a *separator* sequence. This separator can be specified as a single .on(char)
    character, fixed .on(String) string, .onPattern regular expression or
    .on(CharMatcher) CharMatcher instance. Or, instead of using a separator at all, a
    splitter can extract adjacent substrings of a given .fixedLength fixed length.
    
    For example, this expression:
    
    ````Splitter.on(',').split("foo,bar,qux")````
    
    ... produces an `Iterable` containing `"foo"`, `"bar"` and `"qux"`, in
    that order.
    
    By default, `Splitter`'s behavior is simplistic and unassuming. The following
    expression:
    
    ````Splitter.on(',').split(" foo,,,  bar ,")````
    
    ... yields the substrings `[" foo", "", "", " bar ", ""]`. If this is not the desired
    behavior, use configuration methods to obtain a *new* splitter instance with modified
    behavior:
    
    ````private static final Splitter MY_SPLITTER = Splitter.on(',')
        .trimResults()
        .omitEmptyStrings();````
    
    Now `MY_SPLITTER.split("foo,,, bar ,")` returns just `["foo", "bar"]`. Note that
    the order in which these configuration methods are called is never significant.
    
    **Warning:** Splitter instances are immutable. Invoking a configuration method has no
    effect on the receiving instance; you must store and use the new splitter instance it returns
    instead.
    
    ````// Do NOT do this
    Splitter splitter = Splitter.on('/');
    splitter.trimResults(); // does nothing!
    return splitter.split("wrong / wrong / wrong");````
    
    For separator-based splitters that do not use `omitEmptyStrings`, an input string
    containing `n` occurrences of the separator naturally yields an iterable of size `n +
    1`. So if the separator does not occur anywhere in the input, a single substring is returned
    containing the entire input. Consequently, all splitters split the empty string to `[""]`
    (note: even fixed-length splitters).
    
    Splitter instances are thread-safe immutable, and are therefore safe to store as `static
    final` constants.
    
    The Joiner class provides the inverse operation to splitting, but note that a
    round-trip between the two should be assumed to be lossy.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/StringsExplained#splitter">`Splitter`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 1.0
    """

    @staticmethod
    def on(separator: str) -> "Splitter":
        """
        Returns a splitter that uses the given single-character separator. For example, `Splitter.on(',').split("foo,,bar")` returns an iterable containing `["foo", "", "bar"]`.

        Arguments
        - separator: the character to recognize as a separator

        Returns
        - a splitter, with default settings, that recognizes that separator
        """
        ...


    @staticmethod
    def on(separatorMatcher: "CharMatcher") -> "Splitter":
        """
        Returns a splitter that considers any single character matched by the given `CharMatcher`
        to be a separator. For example, `Splitter.on(CharMatcher.anyOf(";,")).split("foo,;bar,quux")` returns an iterable containing
        `["foo", "", "bar", "quux"]`.

        Arguments
        - separatorMatcher: a CharMatcher that determines whether a character is a
            separator

        Returns
        - a splitter, with default settings, that uses this matcher
        """
        ...


    @staticmethod
    def on(separator: str) -> "Splitter":
        """
        Returns a splitter that uses the given fixed string as a separator. For example, `Splitter.on(", ").split("foo, bar,baz")` returns an iterable containing `["foo",
        "bar,baz"]`.

        Arguments
        - separator: the literal, nonempty string to recognize as a separator

        Returns
        - a splitter, with default settings, that recognizes that separator
        """
        ...


    @staticmethod
    def on(separatorPattern: "Pattern") -> "Splitter":
        """
        Returns a splitter that considers any subsequence matching `pattern` to be a separator.
        For example, `Splitter.on(Pattern.compile("\r?\n")).split(entireFile)` splits a string
        into lines whether it uses DOS-style or UNIX-style line terminators.

        Arguments
        - separatorPattern: the pattern that determines whether a subsequence is a separator. This
            pattern may not match the empty string.

        Returns
        - a splitter, with default settings, that uses this pattern

        Raises
        - IllegalArgumentException: if `separatorPattern` matches the empty string
        """
        ...


    @staticmethod
    def onPattern(separatorPattern: str) -> "Splitter":
        """
        Returns a splitter that considers any subsequence matching a given pattern (regular expression)
        to be a separator. For example, `Splitter.onPattern("\r?\n").split(entireFile)` splits a
        string into lines whether it uses DOS-style or UNIX-style line terminators. This is equivalent
        to `Splitter.on(Pattern.compile(pattern))`.

        Arguments
        - separatorPattern: the pattern that determines whether a subsequence is a separator. This
            pattern may not match the empty string.

        Returns
        - a splitter, with default settings, that uses this pattern

        Raises
        - IllegalArgumentException: if `separatorPattern` matches the empty string or is a
            malformed expression
        """
        ...


    @staticmethod
    def fixedLength(length: int) -> "Splitter":
        """
        Returns a splitter that divides strings into pieces of the given length. For example, `Splitter.fixedLength(2).split("abcde")` returns an iterable containing `["ab", "cd",
        "e"]`. The last piece can be smaller than `length` but will never be empty.
        
        **Note:** if .fixedLength is used in conjunction with .limit, the final
        split piece *may be longer than the specified fixed length*. This is because the splitter
        will *stop splitting when the limit is reached*, and just return the final piece as-is.
        
        **Exception:** for consistency with separator-based splitters, `split("")` does not
        yield an empty iterable, but an iterable containing `""`. This is the only case in which
        `Iterables.size(split(input))` does not equal `IntMath.divide(input.length(),
        length, CEILING)`. To avoid this behavior, use `omitEmptyStrings`.

        Arguments
        - length: the desired length of pieces after splitting, a positive integer

        Returns
        - a splitter, with default settings, that can split into fixed sized pieces

        Raises
        - IllegalArgumentException: if `length` is zero or negative
        """
        ...


    def omitEmptyStrings(self) -> "Splitter":
        """
        Returns a splitter that behaves equivalently to `this` splitter, but automatically omits
        empty strings from the results. For example, `Splitter.on(',').omitEmptyStrings().split(",a,,,b,c,,")` returns an iterable containing only
        `["a", "b", "c"]`.
        
        If either `trimResults` option is also specified when creating a splitter, that
        splitter always trims results first before checking for emptiness. So, for example, `Splitter.on(':').omitEmptyStrings().trimResults().split(": : : ")` returns an empty iterable.
        
        Note that it is ordinarily not possible for .split(CharSequence) to return an empty
        iterable, but when using this option, it can (if the input sequence consists of nothing but
        separators).

        Returns
        - a splitter with the desired configuration
        """
        ...


    def limit(self, maxItems: int) -> "Splitter":
        """
        Returns a splitter that behaves equivalently to `this` splitter but stops splitting after
        it reaches the limit. The limit defines the maximum number of items returned by the iterator,
        or the maximum size of the list returned by .splitToList.
        
        For example, `Splitter.on(',').limit(3).split("a,b,c,d")` returns an iterable
        containing `["a", "b", "c,d"]`. When omitting empty strings, the omitted strings do not
        count. Hence, `Splitter.on(',').limit(3).omitEmptyStrings().split("a,,,b,,,c,d")` returns
        an iterable containing `["a", "b", "c,d"]`. When trim is requested, all entries are
        trimmed, including the last. Hence `Splitter.on(',').limit(3).trimResults().split(" a , b
        , c , d ")` results in `["a", "b", "c , d"]`.

        Arguments
        - maxItems: the maximum number of items returned

        Returns
        - a splitter with the desired configuration

        Since
        - 9.0
        """
        ...


    def trimResults(self) -> "Splitter":
        """
        Returns a splitter that behaves equivalently to `this` splitter, but automatically
        removes leading and trailing CharMatcher.whitespace whitespace from each returned
        substring; equivalent to `trimResults(CharMatcher.whitespace())`. For example, `Splitter.on(',').trimResults().split(" a, b ,c ")` returns an iterable containing `["a",
        "b", "c"]`.

        Returns
        - a splitter with the desired configuration
        """
        ...


    def trimResults(self, trimmer: "CharMatcher") -> "Splitter":
        ...


    def split(self, sequence: "CharSequence") -> Iterable[str]:
        """
        Splits `sequence` into string components and makes them available through an Iterator, which may be lazily evaluated. If you want an eagerly computed List, use
        .splitToList(CharSequence). Java 8+ users may prefer .splitToStream instead.

        Arguments
        - sequence: the sequence of characters to split

        Returns
        - an iteration over the segments split from the parameter
        """
        ...


    def splitToList(self, sequence: "CharSequence") -> list[str]:
        """
        Splits `sequence` into string components and returns them as an immutable list. If you
        want an Iterable which may be lazily evaluated, use .split(CharSequence).

        Arguments
        - sequence: the sequence of characters to split

        Returns
        - an immutable list of the segments split from the parameter

        Since
        - 15.0
        """
        ...


    def splitToStream(self, sequence: "CharSequence") -> "Stream"[str]:
        """
        Splits `sequence` into string components and makes them available through an Stream, which may be lazily evaluated. If you want an eagerly computed List, use
        .splitToList(CharSequence).

        Arguments
        - sequence: the sequence of characters to split

        Returns
        - a stream over the segments split from the parameter

        Since
        - 28.2
        """
        ...


    def withKeyValueSeparator(self, separator: str) -> "MapSplitter":
        """
        Returns a `MapSplitter` which splits entries based on this splitter, and splits entries
        into keys and values using the specified separator.

        Since
        - 10.0
        """
        ...


    def withKeyValueSeparator(self, separator: str) -> "MapSplitter":
        """
        Returns a `MapSplitter` which splits entries based on this splitter, and splits entries
        into keys and values using the specified separator.

        Since
        - 14.0
        """
        ...


    def withKeyValueSeparator(self, keyValueSplitter: "Splitter") -> "MapSplitter":
        """
        Returns a `MapSplitter` which splits entries based on this splitter, and splits entries
        into keys and values using the specified key-value splitter.
        
        Note: Any configuration option configured on this splitter, such as .trimResults,
        does not change the behavior of the `keyValueSplitter`.
        
        Example:
        
        ````String toSplit = " x -> y, z-> a ";
        Splitter outerSplitter = Splitter.on(',').trimResults();
        MapSplitter mapSplitter = outerSplitter.withKeyValueSeparator(Splitter.on("->"));
        Map<String, String> result = mapSplitter.split(toSplit);
        assertThat(result).isEqualTo(ImmutableMap.of("x ", " y", "z", " a"));````

        Since
        - 10.0
        """
        ...


    class MapSplitter:
        """
        An object that splits strings into maps as `Splitter` splits iterables and lists. Like
        `Splitter`, it is thread-safe and immutable. The common way to build instances is by
        providing an additional Splitter.withKeyValueSeparator key-value separator to
        Splitter.

        Since
        - 10.0
        """

        def split(self, sequence: "CharSequence") -> dict[str, str]:
            """
            Splits `sequence` into substrings, splits each substring into an entry, and returns an
            unmodifiable map with each of the entries. For example, `Splitter.on(';').trimResults().withKeyValueSeparator("=>").split("a=>b ; c=>b")` will return
            a mapping from `"a"` to `"b"` and `"c"` to `"b"`.
            
            The returned map preserves the order of the entries from `sequence`.

            Raises
            - IllegalArgumentException: if the specified sequence does not split into valid map
                entries, or if there are duplicate keys
            """
            ...
