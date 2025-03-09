"""
Python module generated from Java source file java.util.regex.Matcher

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import Spliterator
from java.util.function import Consumer
from java.util.function import Function
from java.util.regex import *
from java.util.stream import Stream
from java.util.stream import StreamSupport
from typing import Any, Callable, Iterable, Tuple


class Matcher(MatchResult):

    def pattern(self) -> "Pattern":
        """
        Returns the pattern that is interpreted by this matcher.

        Returns
        - The pattern for which this matcher was created
        """
        ...


    def toMatchResult(self) -> "MatchResult":
        """
        Returns the match state of this matcher as a MatchResult.
        The result is unaffected by subsequent operations performed upon this
        matcher.

        Returns
        - a `MatchResult` with the state of this matcher

        Since
        - 1.5
        """
        ...


    def usePattern(self, newPattern: "Pattern") -> "Matcher":
        """
        Changes the `Pattern` that this `Matcher` uses to
        find matches with.
        
         This method causes this matcher to lose information
        about the groups of the last match that occurred. The
        matcher's position in the input is maintained and its
        last append position is unaffected.

        Arguments
        - newPattern: The new pattern used by this matcher

        Returns
        - This matcher

        Raises
        - IllegalArgumentException: If newPattern is `null`

        Since
        - 1.5
        """
        ...


    def reset(self) -> "Matcher":
        """
        Resets this matcher.
        
         Resetting a matcher discards all of its explicit state information
        and sets its append position to zero. The matcher's region is set to the
        default region, which is its entire character sequence. The anchoring
        and transparency of this matcher's region boundaries are unaffected.

        Returns
        - This matcher
        """
        ...


    def reset(self, input: "CharSequence") -> "Matcher":
        """
        Resets this matcher with a new input sequence.
        
         Resetting a matcher discards all of its explicit state information
        and sets its append position to zero.  The matcher's region is set to
        the default region, which is its entire character sequence.  The
        anchoring and transparency of this matcher's region boundaries are
        unaffected.

        Arguments
        - input: The new input character sequence

        Returns
        - This matcher
        """
        ...


    def start(self) -> int:
        """
        Returns the start index of the previous match.

        Returns
        - The index of the first character matched

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        """
        ...


    def start(self, group: int) -> int:
        """
        Returns the start index of the subsequence captured by the given group
        during the previous match operation.
        
         <a href="Pattern.html#cg">Capturing groups</a> are indexed from left
        to right, starting at one.  Group zero denotes the entire pattern, so
        the expression *m.*`start(0)` is equivalent to
        *m.*`start()`.  

        Arguments
        - group: The index of a capturing group in this matcher's pattern

        Returns
        - The index of the first character captured by the group,
                 or `-1` if the match was successful but the group
                 itself did not match anything

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IndexOutOfBoundsException: If there is no capturing group in the pattern
                 with the given index
        """
        ...


    def start(self, name: str) -> int:
        """
        Returns the start index of the subsequence captured by the given
        <a href="Pattern.html#groupname">named-capturing group</a> during the
        previous match operation.

        Arguments
        - name: The name of a named-capturing group in this matcher's pattern

        Returns
        - The index of the first character captured by the group,
                 or `-1` if the match was successful but the group
                 itself did not match anything

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IllegalArgumentException: If there is no capturing group in the pattern
                 with the given name

        Since
        - 1.8
        """
        ...


    def end(self) -> int:
        """
        Returns the offset after the last character matched.

        Returns
        - The offset after the last character matched

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        """
        ...


    def end(self, group: int) -> int:
        """
        Returns the offset after the last character of the subsequence
        captured by the given group during the previous match operation.
        
         <a href="Pattern.html#cg">Capturing groups</a> are indexed from left
        to right, starting at one.  Group zero denotes the entire pattern, so
        the expression *m.*`end(0)` is equivalent to
        *m.*`end()`.  

        Arguments
        - group: The index of a capturing group in this matcher's pattern

        Returns
        - The offset after the last character captured by the group,
                 or `-1` if the match was successful
                 but the group itself did not match anything

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IndexOutOfBoundsException: If there is no capturing group in the pattern
                 with the given index
        """
        ...


    def end(self, name: str) -> int:
        """
        Returns the offset after the last character of the subsequence
        captured by the given <a href="Pattern.html#groupname">named-capturing
        group</a> during the previous match operation.

        Arguments
        - name: The name of a named-capturing group in this matcher's pattern

        Returns
        - The offset after the last character captured by the group,
                 or `-1` if the match was successful
                 but the group itself did not match anything

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IllegalArgumentException: If there is no capturing group in the pattern
                 with the given name

        Since
        - 1.8
        """
        ...


    def group(self) -> str:
        """
        Returns the input subsequence matched by the previous match.
        
         For a matcher *m* with input sequence *s*,
        the expressions *m.*`group()` and
        *s.*`substring(`*m.*`start(),`&nbsp;*m.*
        `end())` are equivalent.  
        
         Note that some patterns, for example `a*`, match the empty
        string.  This method will return the empty string when the pattern
        successfully matches the empty string in the input.  

        Returns
        - The (possibly empty) subsequence matched by the previous match,
                in string form

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        """
        ...


    def group(self, group: int) -> str:
        """
        Returns the input subsequence captured by the given group during the
        previous match operation.
        
         For a matcher *m*, input sequence *s*, and group index
        *g*, the expressions *m.*`group(`*g*`)` and
        *s.*`substring(`*m.*`start(`*g*`),`&nbsp;*m.*`end(`*g*`))`
        are equivalent.  
        
         <a href="Pattern.html#cg">Capturing groups</a> are indexed from left
        to right, starting at one.  Group zero denotes the entire pattern, so
        the expression `m.group(0)` is equivalent to `m.group()`.
        
        
         If the match was successful but the group specified failed to match
        any part of the input sequence, then `null` is returned. Note
        that some groups, for example `(a*)`, match the empty string.
        This method will return the empty string when such a group successfully
        matches the empty string in the input.  

        Arguments
        - group: The index of a capturing group in this matcher's pattern

        Returns
        - The (possibly empty) subsequence captured by the group
                 during the previous match, or `null` if the group
                 failed to match part of the input

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IndexOutOfBoundsException: If there is no capturing group in the pattern
                 with the given index
        """
        ...


    def group(self, name: str) -> str:
        """
        Returns the input subsequence captured by the given
        <a href="Pattern.html#groupname">named-capturing group</a> during the
        previous match operation.
        
         If the match was successful but the group specified failed to match
        any part of the input sequence, then `null` is returned. Note
        that some groups, for example `(a*)`, match the empty string.
        This method will return the empty string when such a group successfully
        matches the empty string in the input.  

        Arguments
        - name: The name of a named-capturing group in this matcher's pattern

        Returns
        - The (possibly empty) subsequence captured by the named group
                 during the previous match, or `null` if the group
                 failed to match part of the input

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IllegalArgumentException: If there is no capturing group in the pattern
                 with the given name

        Since
        - 1.7
        """
        ...


    def groupCount(self) -> int:
        """
        Returns the number of capturing groups in this matcher's pattern.
        
         Group zero denotes the entire pattern by convention. It is not
        included in this count.
        
         Any non-negative integer smaller than or equal to the value
        returned by this method is guaranteed to be a valid group index for
        this matcher.  

        Returns
        - The number of capturing groups in this matcher's pattern
        """
        ...


    def matches(self) -> bool:
        """
        Attempts to match the entire region against the pattern.
        
         If the match succeeds then more information can be obtained via the
        `start`, `end`, and `group` methods.  

        Returns
        - `True` if, and only if, the entire region sequence
                 matches this matcher's pattern
        """
        ...


    def find(self) -> bool:
        """
        Attempts to find the next subsequence of the input sequence that matches
        the pattern.
        
         This method starts at the beginning of this matcher's region, or, if
        a previous invocation of the method was successful and the matcher has
        not since been reset, at the first character not matched by the previous
        match.
        
         If the match succeeds then more information can be obtained via the
        `start`, `end`, and `group` methods.  

        Returns
        - `True` if, and only if, a subsequence of the input
                 sequence matches this matcher's pattern
        """
        ...


    def find(self, start: int) -> bool:
        """
        Resets this matcher and then attempts to find the next subsequence of
        the input sequence that matches the pattern, starting at the specified
        index.
        
         If the match succeeds then more information can be obtained via the
        `start`, `end`, and `group` methods, and subsequent
        invocations of the .find() method will start at the first
        character not matched by this match.  

        Arguments
        - start: the index to start searching for a match

        Returns
        - `True` if, and only if, a subsequence of the input
                 sequence starting at the given index matches this matcher's
                 pattern

        Raises
        - IndexOutOfBoundsException: If start is less than zero or if start is greater than the
                 length of the input sequence.
        """
        ...


    def lookingAt(self) -> bool:
        """
        Attempts to match the input sequence, starting at the beginning of the
        region, against the pattern.
        
         Like the .matches matches method, this method always starts
        at the beginning of the region; unlike that method, it does not
        require that the entire region be matched.
        
         If the match succeeds then more information can be obtained via the
        `start`, `end`, and `group` methods.  

        Returns
        - `True` if, and only if, a prefix of the input
                 sequence matches this matcher's pattern
        """
        ...


    @staticmethod
    def quoteReplacement(s: str) -> str:
        """
        Returns a literal replacement `String` for the specified
        `String`.
        
        This method produces a `String` that will work
        as a literal replacement `s` in the
        `appendReplacement` method of the Matcher class.
        The `String` produced will match the sequence of characters
        in `s` treated as a literal sequence. Slashes ('\') and
        dollar signs ('$') will be given no special meaning.

        Arguments
        - s: The string to be literalized

        Returns
        - A literal string replacement

        Since
        - 1.5
        """
        ...


    def appendReplacement(self, sb: "StringBuffer", replacement: str) -> "Matcher":
        """
        Implements a non-terminal append-and-replace step.
        
         This method performs the following actions: 
        
        <ol>
        
          -  It reads characters from the input sequence, starting at the
          append position, and appends them to the given string buffer.  It
          stops after reading the last character preceding the previous match,
          that is, the character at index .start()&nbsp;`-`&nbsp;`1`.  
        
          -  It appends the given replacement string to the string buffer.
          
        
          -  It sets the append position of this matcher to the index of
          the last character matched, plus one, that is, to .end().
          
        
        </ol>
        
         The replacement string may contain references to subsequences
        captured during the previous match: Each occurrence of
        `${`*name*`}` or `$`*g*
        will be replaced by the result of evaluating the corresponding
        .group(String) group(name) or .group(int) group(g)
        respectively. For `$`*g*,
        the first number after the `$` is always treated as part of
        the group reference. Subsequent numbers are incorporated into g if
        they would form a legal group reference. Only the numerals '0'
        through '9' are considered as potential components of the group
        reference. If the second group matched the string `"foo"`, for
        example, then passing the replacement string `"$2bar"` would
        cause `"foobar"` to be appended to the string buffer. A dollar
        sign (`$`) may be included as a literal in the replacement
        string by preceding it with a backslash (`\$`).
        
         Note that backslashes (`\`) and dollar signs (`$`) in
        the replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         This method is intended to be used in a loop together with the
        .appendTail(StringBuffer) appendTail and .find() find
        methods.  The following code, for example, writes `one dog two dogs
        in the yard` to the standard-output stream: 
        
        <blockquote>```
        Pattern p = Pattern.compile("cat");
        Matcher m = p.matcher("one cat two cats in the yard");
        StringBuffer sb = new StringBuffer();
        while (m.find()) {
            m.appendReplacement(sb, "dog");
        }
        m.appendTail(sb);
        System.out.println(sb.toString());```</blockquote>

        Arguments
        - sb: The target string buffer
        - replacement: The replacement string

        Returns
        - This matcher

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IllegalArgumentException: If the replacement string refers to a named-capturing
                 group that does not exist in the pattern
        - IndexOutOfBoundsException: If the replacement string refers to a capturing group
                 that does not exist in the pattern
        """
        ...


    def appendReplacement(self, sb: "StringBuilder", replacement: str) -> "Matcher":
        """
        Implements a non-terminal append-and-replace step.
        
         This method performs the following actions: 
        
        <ol>
        
          -  It reads characters from the input sequence, starting at the
          append position, and appends them to the given string builder.  It
          stops after reading the last character preceding the previous match,
          that is, the character at index .start()&nbsp;`-`&nbsp;`1`.  
        
          -  It appends the given replacement string to the string builder.
          
        
          -  It sets the append position of this matcher to the index of
          the last character matched, plus one, that is, to .end().
          
        
        </ol>
        
         The replacement string may contain references to subsequences
        captured during the previous match: Each occurrence of
        `$`*g* will be replaced by the result of
        evaluating .group(int) group`(`*g*`)`.
        The first number after the `$` is always treated as part of
        the group reference. Subsequent numbers are incorporated into g if
        they would form a legal group reference. Only the numerals '0'
        through '9' are considered as potential components of the group
        reference. If the second group matched the string `"foo"`, for
        example, then passing the replacement string `"$2bar"` would
        cause `"foobar"` to be appended to the string builder. A dollar
        sign (`$`) may be included as a literal in the replacement
        string by preceding it with a backslash (`\$`).
        
         Note that backslashes (`\`) and dollar signs (`$`) in
        the replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         This method is intended to be used in a loop together with the
        .appendTail(StringBuilder) appendTail and
        .find() find methods. The following code, for example, writes
        `one dog two dogs in the yard` to the standard-output stream: 
        
        <blockquote>```
        Pattern p = Pattern.compile("cat");
        Matcher m = p.matcher("one cat two cats in the yard");
        StringBuilder sb = new StringBuilder();
        while (m.find()) {
            m.appendReplacement(sb, "dog");
        }
        m.appendTail(sb);
        System.out.println(sb.toString());```</blockquote>

        Arguments
        - sb: The target string builder
        - replacement: The replacement string

        Returns
        - This matcher

        Raises
        - IllegalStateException: If no match has yet been attempted,
                 or if the previous match operation failed
        - IllegalArgumentException: If the replacement string refers to a named-capturing
                 group that does not exist in the pattern
        - IndexOutOfBoundsException: If the replacement string refers to a capturing group
                 that does not exist in the pattern

        Since
        - 9
        """
        ...


    def appendTail(self, sb: "StringBuffer") -> "StringBuffer":
        """
        Implements a terminal append-and-replace step.
        
         This method reads characters from the input sequence, starting at
        the append position, and appends them to the given string buffer.  It is
        intended to be invoked after one or more invocations of the .appendReplacement(StringBuffer, String) appendReplacement method in
        order to copy the remainder of the input sequence.  

        Arguments
        - sb: The target string buffer

        Returns
        - The target string buffer
        """
        ...


    def appendTail(self, sb: "StringBuilder") -> "StringBuilder":
        """
        Implements a terminal append-and-replace step.
        
         This method reads characters from the input sequence, starting at
        the append position, and appends them to the given string builder.  It is
        intended to be invoked after one or more invocations of the .appendReplacement(StringBuilder, String)
        appendReplacement method in order to copy the remainder of the input
        sequence.  

        Arguments
        - sb: The target string builder

        Returns
        - The target string builder

        Since
        - 9
        """
        ...


    def replaceAll(self, replacement: str) -> str:
        """
        Replaces every subsequence of the input sequence that matches the
        pattern with the given replacement string.
        
         This method first resets this matcher.  It then scans the input
        sequence looking for matches of the pattern.  Characters that are not
        part of any match are appended directly to the result string; each match
        is replaced in the result by the replacement string.  The replacement
        string may contain references to captured subsequences as in the .appendReplacement appendReplacement method.
        
         Note that backslashes (`\`) and dollar signs (`$`) in
        the replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         Given the regular expression `a*b`, the input
        `"aabfooaabfooabfoob"`, and the replacement string
        `"-"`, an invocation of this method on a matcher for that
        expression would yield the string `"-foo-foo-foo-"`.
        
         Invoking this method changes this matcher's state.  If the matcher
        is to be used in further matching operations then it should first be
        reset.  

        Arguments
        - replacement: The replacement string

        Returns
        - The string constructed by replacing each matching subsequence
                 by the replacement string, substituting captured subsequences
                 as needed
        """
        ...


    def replaceAll(self, replacer: "Function"["MatchResult", str]) -> str:
        """
        Replaces every subsequence of the input sequence that matches the
        pattern with the result of applying the given replacer function to the
        match result of this matcher corresponding to that subsequence.
        Exceptions thrown by the function are relayed to the caller.
        
         This method first resets this matcher.  It then scans the input
        sequence looking for matches of the pattern.  Characters that are not
        part of any match are appended directly to the result string; each match
        is replaced in the result by the applying the replacer function that
        returns a replacement string.  Each replacement string may contain
        references to captured subsequences as in the .appendReplacement
        appendReplacement method.
        
         Note that backslashes (`\`) and dollar signs (`$`) in
        a replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         Given the regular expression `dog`, the input
        `"zzzdogzzzdogzzz"`, and the function
        `mr -> mr.group().toUpperCase()`, an invocation of this method on
        a matcher for that expression would yield the string
        `"zzzDOGzzzDOGzzz"`.
        
         Invoking this method changes this matcher's state.  If the matcher
        is to be used in further matching operations then it should first be
        reset.  
        
         The replacer function should not modify this matcher's state during
        replacement.  This method will, on a best-effort basis, throw a
        java.util.ConcurrentModificationException if such modification is
        detected.
        
         The state of each match result passed to the replacer function is
        guaranteed to be constant only for the duration of the replacer function
        call and only if the replacer function does not modify this matcher's
        state.

        Arguments
        - replacer: The function to be applied to the match result of this matcher
                that returns a replacement string.

        Returns
        - The string constructed by replacing each matching subsequence
                 with the result of applying the replacer function to that
                 matched subsequence, substituting captured subsequences as
                 needed.

        Raises
        - NullPointerException: if the replacer function is null
        - ConcurrentModificationException: if it is detected, on a
                best-effort basis, that the replacer function modified this
                matcher's state

        Since
        - 9

        Unknown Tags
        - This implementation applies the replacer function to this matcher, which
        is an instance of `MatchResult`.
        """
        ...


    def results(self) -> "Stream"["MatchResult"]:
        """
        Returns a stream of match results for each subsequence of the input
        sequence that matches the pattern.  The match results occur in the
        same order as the matching subsequences in the input sequence.
        
         Each match result is produced as if by .toMatchResult().
        
         This method does not reset this matcher.  Matching starts on
        initiation of the terminal stream operation either at the beginning of
        this matcher's region, or, if the matcher has not since been reset, at
        the first character not matched by a previous match.
        
         If the matcher is to be used for further matching operations after
        the terminal stream operation completes then it should be first reset.
        
         This matcher's state should not be modified during execution of the
        returned stream's pipeline.  The returned stream's source
        `Spliterator` is *fail-fast* and will, on a best-effort
        basis, throw a java.util.ConcurrentModificationException if such
        modification is detected.

        Returns
        - a sequential stream of match results.

        Since
        - 9
        """
        ...


    def replaceFirst(self, replacement: str) -> str:
        """
        Replaces the first subsequence of the input sequence that matches the
        pattern with the given replacement string.
        
         This method first resets this matcher.  It then scans the input
        sequence looking for a match of the pattern.  Characters that are not
        part of the match are appended directly to the result string; the match
        is replaced in the result by the replacement string.  The replacement
        string may contain references to captured subsequences as in the .appendReplacement appendReplacement method.
        
        Note that backslashes (`\`) and dollar signs (`$`) in
        the replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         Given the regular expression `dog`, the input
        `"zzzdogzzzdogzzz"`, and the replacement string
        `"cat"`, an invocation of this method on a matcher for that
        expression would yield the string `"zzzcatzzzdogzzz"`.  
        
         Invoking this method changes this matcher's state.  If the matcher
        is to be used in further matching operations then it should first be
        reset.  

        Arguments
        - replacement: The replacement string

        Returns
        - The string constructed by replacing the first matching
                 subsequence by the replacement string, substituting captured
                 subsequences as needed
        """
        ...


    def replaceFirst(self, replacer: "Function"["MatchResult", str]) -> str:
        """
        Replaces the first subsequence of the input sequence that matches the
        pattern with the result of applying the given replacer function to the
        match result of this matcher corresponding to that subsequence.
        Exceptions thrown by the replace function are relayed to the caller.
        
         This method first resets this matcher.  It then scans the input
        sequence looking for a match of the pattern.  Characters that are not
        part of the match are appended directly to the result string; the match
        is replaced in the result by the applying the replacer function that
        returns a replacement string.  The replacement string may contain
        references to captured subsequences as in the .appendReplacement
        appendReplacement method.
        
        Note that backslashes (`\`) and dollar signs (`$`) in
        the replacement string may cause the results to be different than if it
        were being treated as a literal replacement string. Dollar signs may be
        treated as references to captured subsequences as described above, and
        backslashes are used to escape literal characters in the replacement
        string.
        
         Given the regular expression `dog`, the input
        `"zzzdogzzzdogzzz"`, and the function
        `mr -> mr.group().toUpperCase()`, an invocation of this method on
        a matcher for that expression would yield the string
        `"zzzDOGzzzdogzzz"`.
        
         Invoking this method changes this matcher's state.  If the matcher
        is to be used in further matching operations then it should first be
        reset.
        
         The replacer function should not modify this matcher's state during
        replacement.  This method will, on a best-effort basis, throw a
        java.util.ConcurrentModificationException if such modification is
        detected.
        
         The state of the match result passed to the replacer function is
        guaranteed to be constant only for the duration of the replacer function
        call and only if the replacer function does not modify this matcher's
        state.

        Arguments
        - replacer: The function to be applied to the match result of this matcher
                that returns a replacement string.

        Returns
        - The string constructed by replacing the first matching
                 subsequence with the result of applying the replacer function to
                 the matched subsequence, substituting captured subsequences as
                 needed.

        Raises
        - NullPointerException: if the replacer function is null
        - ConcurrentModificationException: if it is detected, on a
                best-effort basis, that the replacer function modified this
                matcher's state

        Since
        - 9

        Unknown Tags
        - This implementation applies the replacer function to this matcher, which
        is an instance of `MatchResult`.
        """
        ...


    def region(self, start: int, end: int) -> "Matcher":
        """
        Sets the limits of this matcher's region. The region is the part of the
        input sequence that will be searched to find a match. Invoking this
        method resets the matcher, and then sets the region to start at the
        index specified by the `start` parameter and end at the
        index specified by the `end` parameter.
        
        Depending on the transparency and anchoring being used (see
        .useTransparentBounds(boolean) useTransparentBounds and
        .useAnchoringBounds(boolean) useAnchoringBounds), certain
        constructs such as anchors may behave differently at or around the
        boundaries of the region.

        Arguments
        - start: The index to start searching at (inclusive)
        - end: The index to end searching at (exclusive)

        Returns
        - this matcher

        Raises
        - IndexOutOfBoundsException: If start or end is less than zero, if
                 start is greater than the length of the input sequence, if
                 end is greater than the length of the input sequence, or if
                 start is greater than end.

        Since
        - 1.5
        """
        ...


    def regionStart(self) -> int:
        """
        Reports the start index of this matcher's region. The
        searches this matcher conducts are limited to finding matches
        within .regionStart() regionStart (inclusive) and
        .regionEnd() regionEnd (exclusive).

        Returns
        - The starting point of this matcher's region

        Since
        - 1.5
        """
        ...


    def regionEnd(self) -> int:
        """
        Reports the end index (exclusive) of this matcher's region.
        The searches this matcher conducts are limited to finding matches
        within .regionStart() regionStart (inclusive) and
        .regionEnd() regionEnd (exclusive).

        Returns
        - the ending point of this matcher's region

        Since
        - 1.5
        """
        ...


    def hasTransparentBounds(self) -> bool:
        """
        Queries the transparency of region bounds for this matcher.
        
         This method returns `True` if this matcher uses
        *transparent* bounds, `False` if it uses *opaque*
        bounds.
        
         See .useTransparentBounds(boolean) useTransparentBounds for a
        description of transparent and opaque bounds.
        
         By default, a matcher uses opaque region boundaries.

        Returns
        - `True` iff this matcher is using transparent bounds,
                `False` otherwise.

        See
        - java.util.regex.Matcher.useTransparentBounds(boolean)

        Since
        - 1.5
        """
        ...


    def useTransparentBounds(self, b: bool) -> "Matcher":
        """
        Sets the transparency of region bounds for this matcher.
        
         Invoking this method with an argument of `True` will set this
        matcher to use *transparent* bounds. If the boolean
        argument is `False`, then *opaque* bounds will be used.
        
         Using transparent bounds, the boundaries of this
        matcher's region are transparent to lookahead, lookbehind,
        and boundary matching constructs. Those constructs can see beyond the
        boundaries of the region to see if a match is appropriate.
        
         Using opaque bounds, the boundaries of this matcher's
        region are opaque to lookahead, lookbehind, and boundary matching
        constructs that may try to see beyond them. Those constructs cannot
        look past the boundaries so they will fail to match anything outside
        of the region.
        
         By default, a matcher uses opaque bounds.

        Arguments
        - b: a boolean indicating whether to use opaque or transparent
                regions

        Returns
        - this matcher

        See
        - java.util.regex.Matcher.hasTransparentBounds

        Since
        - 1.5
        """
        ...


    def hasAnchoringBounds(self) -> bool:
        """
        Queries the anchoring of region bounds for this matcher.
        
         This method returns `True` if this matcher uses
        *anchoring* bounds, `False` otherwise.
        
         See .useAnchoringBounds(boolean) useAnchoringBounds for a
        description of anchoring bounds.
        
         By default, a matcher uses anchoring region boundaries.

        Returns
        - `True` iff this matcher is using anchoring bounds,
                `False` otherwise.

        See
        - java.util.regex.Matcher.useAnchoringBounds(boolean)

        Since
        - 1.5
        """
        ...


    def useAnchoringBounds(self, b: bool) -> "Matcher":
        """
        Sets the anchoring of region bounds for this matcher.
        
         Invoking this method with an argument of `True` will set this
        matcher to use *anchoring* bounds. If the boolean
        argument is `False`, then *non-anchoring* bounds will be
        used.
        
         Using anchoring bounds, the boundaries of this
        matcher's region match anchors such as ^ and $.
        
         Without anchoring bounds, the boundaries of this
        matcher's region will not match anchors such as ^ and $.
        
         By default, a matcher uses anchoring region boundaries.

        Arguments
        - b: a boolean indicating whether or not to use anchoring bounds.

        Returns
        - this matcher

        See
        - java.util.regex.Matcher.hasAnchoringBounds

        Since
        - 1.5
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this matcher. The
        string representation of a `Matcher` contains information
        that may be useful for debugging. The exact format is unspecified.

        Returns
        - The string representation of this matcher

        Since
        - 1.5
        """
        ...


    def hitEnd(self) -> bool:
        """
        Returns True if the end of input was hit by the search engine in
        the last match operation performed by this matcher.
        
        When this method returns True, then it is possible that more input
        would have changed the result of the last search.

        Returns
        - True iff the end of input was hit in the last match; False
                 otherwise

        Since
        - 1.5
        """
        ...


    def requireEnd(self) -> bool:
        """
        Returns True if more input could change a positive match into a
        negative one.
        
        If this method returns True, and a match was found, then more
        input could cause the match to be lost. If this method returns False
        and a match was found, then more input might change the match but the
        match won't be lost. If a match was not found, then requireEnd has no
        meaning.

        Returns
        - True iff more input could change a positive match into a
                 negative one.

        Since
        - 1.5
        """
        ...
