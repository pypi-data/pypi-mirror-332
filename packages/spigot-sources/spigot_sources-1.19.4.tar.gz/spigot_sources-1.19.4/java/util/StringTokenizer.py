"""
Python module generated from Java source file java.util.StringTokenizer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class StringTokenizer(Enumeration):
    """
    The string tokenizer class allows an application to break a
    string into tokens. The tokenization method is much simpler than
    the one used by the `StreamTokenizer` class. The
    `StringTokenizer` methods do not distinguish among
    identifiers, numbers, and quoted strings, nor do they recognize
    and skip comments.
    
    The set of delimiters (the characters that separate tokens) may
    be specified either at creation time or on a per-token basis.
    
    An instance of `StringTokenizer` behaves in one of two
    ways, depending on whether it was created with the
    `returnDelims` flag having the value `True`
    or `False`:
    
    - If the flag is `False`, delimiter characters serve to
        separate tokens. A token is a maximal sequence of consecutive
        characters that are not delimiters.
    - If the flag is `True`, delimiter characters are themselves
        considered to be tokens. A token is thus either one delimiter
        character, or a maximal sequence of consecutive characters that are
        not delimiters.
    
    A `StringTokenizer` object internally maintains a current
    position within the string to be tokenized. Some operations advance this
    current position past the characters processed.
    A token is returned by taking a substring of the string that was used to
    create the `StringTokenizer` object.
    
    The following is one example of the use of the tokenizer. The code:
    <blockquote>```
        StringTokenizer st = new StringTokenizer("this is a test");
        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
    ```</blockquote>
    
    prints the following output:
    <blockquote>```
        this
        is
        a
        test
    ```</blockquote>
    
    
    `StringTokenizer` is a legacy class that is retained for
    compatibility reasons although its use is discouraged in new code. It is
    recommended that anyone seeking this functionality use the `split`
    method of `String` or the java.util.regex package instead.
    
    The following example illustrates how the `String.split`
    method can be used to break up a string into its basic tokens:
    <blockquote>```
        String[] result = "this is a test".split("\\s");
        for (int x=0; x&lt;result.length; x++)
            System.out.println(result[x]);
    ```</blockquote>
    
    prints the following output:
    <blockquote>```
        this
        is
        a
        test
    ```</blockquote>

    See
    - java.io.StreamTokenizer

    Since
    - 1.0
    """

    def __init__(self, str: str, delim: str, returnDelims: bool):
        """
        Constructs a string tokenizer for the specified string. All
        characters in the `delim` argument are the delimiters
        for separating tokens.
        
        If the `returnDelims` flag is `True`, then
        the delimiter characters are also returned as tokens. Each
        delimiter is returned as a string of length one. If the flag is
        `False`, the delimiter characters are skipped and only
        serve as separators between tokens.
        
        Note that if `delim` is `null`, this constructor does
        not throw an exception. However, trying to invoke other methods on the
        resulting `StringTokenizer` may result in a
        `NullPointerException`.

        Arguments
        - str: a string to be parsed.
        - delim: the delimiters.
        - returnDelims: flag indicating whether to return the delimiters
                                as tokens.

        Raises
        - NullPointerException: if str is `null`
        """
        ...


    def __init__(self, str: str, delim: str):
        """
        Constructs a string tokenizer for the specified string. The
        characters in the `delim` argument are the delimiters
        for separating tokens. Delimiter characters themselves will not
        be treated as tokens.
        
        Note that if `delim` is `null`, this constructor does
        not throw an exception. However, trying to invoke other methods on the
        resulting `StringTokenizer` may result in a
        `NullPointerException`.

        Arguments
        - str: a string to be parsed.
        - delim: the delimiters.

        Raises
        - NullPointerException: if str is `null`
        """
        ...


    def __init__(self, str: str):
        """
        Constructs a string tokenizer for the specified string. The
        tokenizer uses the default delimiter set, which is
        `"&nbsp;&#92;t&#92;n&#92;r&#92;f"`: the space character,
        the tab character, the newline character, the carriage-return character,
        and the form-feed character. Delimiter characters themselves will
        not be treated as tokens.

        Arguments
        - str: a string to be parsed.

        Raises
        - NullPointerException: if str is `null`
        """
        ...


    def hasMoreTokens(self) -> bool:
        """
        Tests if there are more tokens available from this tokenizer's string.
        If this method returns `True`, then a subsequent call to
        `nextToken` with no argument will successfully return a token.

        Returns
        - `True` if and only if there is at least one token
                 in the string after the current position; `False`
                 otherwise.
        """
        ...


    def nextToken(self) -> str:
        """
        Returns the next token from this string tokenizer.

        Returns
        - the next token from this string tokenizer.

        Raises
        - NoSuchElementException: if there are no more tokens in this
                      tokenizer's string.
        """
        ...


    def nextToken(self, delim: str) -> str:
        """
        Returns the next token in this string tokenizer's string. First,
        the set of characters considered to be delimiters by this
        `StringTokenizer` object is changed to be the characters in
        the string `delim`. Then the next token in the string
        after the current position is returned. The current position is
        advanced beyond the recognized token.  The new delimiter set
        remains the default after this call.

        Arguments
        - delim: the new delimiters.

        Returns
        - the next token, after switching to the new delimiter set.

        Raises
        - NoSuchElementException: if there are no more tokens in this
                      tokenizer's string.
        - NullPointerException: if delim is `null`
        """
        ...


    def hasMoreElements(self) -> bool:
        """
        Returns the same value as the `hasMoreTokens`
        method. It exists so that this class can implement the
        `Enumeration` interface.

        Returns
        - `True` if there are more tokens;
                 `False` otherwise.

        See
        - java.util.StringTokenizer.hasMoreTokens()
        """
        ...


    def nextElement(self) -> "Object":
        """
        Returns the same value as the `nextToken` method,
        except that its declared return value is `Object` rather than
        `String`. It exists so that this class can implement the
        `Enumeration` interface.

        Returns
        - the next token in the string.

        Raises
        - NoSuchElementException: if there are no more tokens in this
                      tokenizer's string.

        See
        - java.util.StringTokenizer.nextToken()
        """
        ...


    def countTokens(self) -> int:
        """
        Calculates the number of times that this tokenizer's
        `nextToken` method can be called before it generates an
        exception. The current position is not advanced.

        Returns
        - the number of tokens remaining in the string using the current
                 delimiter set.

        See
        - java.util.StringTokenizer.nextToken()
        """
        ...
