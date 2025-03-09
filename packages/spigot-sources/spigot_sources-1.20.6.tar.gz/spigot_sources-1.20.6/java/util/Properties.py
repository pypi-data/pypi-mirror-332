"""
Python module generated from Java source file java.util.Properties

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import BufferedWriter
from java.io import IOException
from java.io import InputStream
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import OutputStream
from java.io import OutputStreamWriter
from java.io import PrintStream
from java.io import PrintWriter
from java.io import Reader
from java.io import StreamCorruptedException
from java.io import UnsupportedEncodingException
from java.io import Writer
from java.nio.charset import Charset
from java.nio.charset import IllegalCharsetNameException
from java.nio.charset import UnsupportedCharsetException
from java.util import *
from java.util.concurrent import ConcurrentHashMap
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Function
from jdk.internal.access import SharedSecrets
from jdk.internal.misc import Unsafe
from jdk.internal.util import ArraysSupport
from jdk.internal.util.xml import PropertiesDefaultHandler
from sun.nio.cs import ISO_8859_1
from sun.nio.cs import UTF_8
from typing import Any, Callable, Iterable, Tuple


class Properties(Hashtable):
    """
    The `Properties` class represents a persistent set of
    properties. The `Properties` can be saved to a stream
    or loaded from a stream. Each key and its corresponding value in
    the property list is a string.
    
    A property list can contain another property list as its
    "defaults"; this second property list is searched if
    the property key is not found in the original property list.
    
    Because `Properties` inherits from `Hashtable`, the
    `put` and `putAll` methods can be applied to a
    `Properties` object.  Their use is strongly discouraged as they
    allow the caller to insert entries whose keys or values are not
    `Strings`.  The `setProperty` method should be used
    instead.  If the `store` or `save` method is called
    on a "compromised" `Properties` object that contains a
    non-`String` key or value, the call will fail. Similarly,
    the call to the `propertyNames` or `list` method
    will fail if it is called on a "compromised" `Properties`
    object that contains a non-`String` key.
    
    
    The iterators returned by the `iterator` method of this class's
    "collection views" (that is, `entrySet()`, `keySet()`, and
    `values()`) may not fail-fast (unlike the Hashtable implementation).
    These iterators are guaranteed to traverse elements as they existed upon
    construction exactly once, and may (but are not guaranteed to) reflect any
    modifications subsequent to construction.
    
    The .load(java.io.Reader) load(Reader) `/`
    .store(java.io.Writer, java.lang.String) store(Writer, String)
    methods load and store properties from and to a character based stream
    in a simple line-oriented format specified below.
    
    The .load(java.io.InputStream) load(InputStream) `/`
    .store(java.io.OutputStream, java.lang.String) store(OutputStream, String)
    methods work the same way as the load(Reader)/store(Writer, String) pair, except
    the input/output stream is encoded in ISO 8859-1 character encoding.
    Characters that cannot be directly represented in this encoding can be written using
    Unicode escapes as defined in section 3.3 of
    <cite>The Java Language Specification</cite>;
    only a single 'u' character is allowed in an escape
    sequence.
    
     The .loadFromXML(InputStream) and .storeToXML(OutputStream, String, String) methods load and store properties
    in a simple XML format.  By default the UTF-8 character encoding is used,
    however a specific encoding may be specified if required. Implementations
    are required to support UTF-8 and UTF-16 and may support other encodings.
    An XML properties document has the following DOCTYPE declaration:
    
    ```
    &lt;!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd"&gt;
    ```
    Note that the system URI (http://java.sun.com/dtd/properties.dtd) is
    *not* accessed when exporting or importing properties; it merely
    serves as a string to uniquely identify the DTD, which is:
    ```
       &lt;?xml version="1.0" encoding="UTF-8"?&gt;
    
       &lt;!-- DTD for properties --&gt;
    
       &lt;!ELEMENT properties ( comment?, entry* ) &gt;
    
       &lt;!ATTLIST properties version CDATA #FIXED "1.0"&gt;
    
       &lt;!ELEMENT comment (#PCDATA) &gt;
    
       &lt;!ELEMENT entry (#PCDATA) &gt;
    
       &lt;!ATTLIST entry key CDATA #REQUIRED&gt;
    ```
    
    This class is thread-safe: multiple threads can share a single
    `Properties` object without the need for external synchronization.

    Author(s)
    - Xueming Shen

    Since
    - 1.0

    Unknown Tags
    - The `Properties` class does not inherit the concept of a load factor
    from its superclass, `Hashtable`.
    """

    def __init__(self):
        """
        Creates an empty property list with no default values.

        Unknown Tags
        - The initial capacity of a `Properties` object created
        with this constructor is unspecified.
        """
        ...


    def __init__(self, initialCapacity: int):
        """
        Creates an empty property list with no default values, and with an
        initial size accommodating the specified number of elements without the
        need to dynamically resize.

        Arguments
        - initialCapacity: the `Properties` will be sized to
                accommodate this many elements

        Raises
        - IllegalArgumentException: if the initial capacity is less than
                zero.
        """
        ...


    def __init__(self, defaults: "Properties"):
        """
        Creates an empty property list with the specified defaults.

        Arguments
        - defaults: the defaults.

        Unknown Tags
        - The initial capacity of a `Properties` object created
        with this constructor is unspecified.
        """
        ...


    def setProperty(self, key: str, value: str) -> "Object":
        """
        Calls the `Hashtable` method `put`. Provided for
        parallelism with the `getProperty` method. Enforces use of
        strings for property keys and values. The value returned is the
        result of the `Hashtable` call to `put`.

        Arguments
        - key: the key to be placed into this property list.
        - value: the value corresponding to `key`.

        Returns
        - the previous value of the specified key in this property
                    list, or `null` if it did not have one.

        See
        - .getProperty

        Since
        - 1.2
        """
        ...


    def load(self, reader: "Reader") -> None:
        """
        Reads a property list (key and element pairs) from the input
        character stream in a simple line-oriented format.
        
        Properties are processed in terms of lines. There are two
        kinds of line, *natural lines* and *logical lines*.
        A natural line is defined as a line of
        characters that is terminated either by a set of line terminator
        characters (`\n` or `\r` or `\r\n`)
        or by the end of the stream. A natural line may be either a blank line,
        a comment line, or hold all or some of a key-element pair. A logical
        line holds all the data of a key-element pair, which may be spread
        out across several adjacent natural lines by escaping
        the line terminator sequence with a backslash character
        `\`.  Note that a comment line cannot be extended
        in this manner; every natural line that is a comment must have
        its own comment indicator, as described below. Lines are read from
        input until the end of the stream is reached.
        
        
        A natural line that contains only white space characters is
        considered blank and is ignored.  A comment line has an ASCII
        `'.'` or `'!'` as its first non-white
        space character; comment lines are also ignored and do not
        encode key-element information.  In addition to line
        terminators, this format considers the characters space
        (`' '`, `'\u005Cu0020'`), tab
        (`'\t'`, `'\u005Cu0009'`), and form feed
        (`'\f'`, `'\u005Cu000C'`) to be white
        space.
        
        
        If a logical line is spread across several natural lines, the
        backslash escaping the line terminator sequence, the line
        terminator sequence, and any white space at the start of the
        following line have no affect on the key or element values.
        The remainder of the discussion of key and element parsing
        (when loading) will assume all the characters constituting
        the key and element appear on a single natural line after
        line continuation characters have been removed.  Note that
        it is *not* sufficient to only examine the character
        preceding a line terminator sequence to decide if the line
        terminator is escaped; there must be an odd number of
        contiguous backslashes for the line terminator to be escaped.
        Since the input is processed from left to right, a
        non-zero even number of 2*n* contiguous backslashes
        before a line terminator (or elsewhere) encodes *n*
        backslashes after escape processing.
        
        
        The key contains all of the characters in the line starting
        with the first non-white space character and up to, but not
        including, the first unescaped `'='`,
        `':'`, or white space character other than a line
        terminator. All of these key termination characters may be
        included in the key by escaping them with a preceding backslash
        character; for example,
        
        `\:\=`
        
        would be the two-character key `":="`.  Line
        terminator characters can be included using `\r` and
        `\n` escape sequences.  Any white space after the
        key is skipped; if the first non-white space character after
        the key is `'='` or `':'`, then it is
        ignored and any white space characters after it are also
        skipped.  All remaining characters on the line become part of
        the associated element string; if there are no remaining
        characters, the element is the empty string
        `""`.  Once the raw character sequences
        constituting the key and element are identified, escape
        processing is performed as described above.
        
        
        As an example, each of the following three lines specifies the key
        `"Truth"` and the associated element value
        `"Beauty"`:
        ```
        Truth = Beauty
         Truth:Beauty
        Truth                    :Beauty
        ```
        As another example, the following three lines specify a single
        property:
        ```
        fruits                           apple, banana, pear, \
                                         cantaloupe, watermelon, \
                                         kiwi, mango
        ```
        The key is `"fruits"` and the associated element is:
        ```"apple, banana, pear, cantaloupe, watermelon, kiwi, mango"```
        Note that a space appears before each `\` so that a space
        will appear after each comma in the final result; the `\`,
        line terminator, and leading white space on the continuation line are
        merely discarded and are *not* replaced by one or more other
        characters.
        
        As a third example, the line:
        ```cheeses
        ```
        specifies that the key is `"cheeses"` and the associated
        element is the empty string `""`.
        
        <a id="unicodeescapes"></a>
        Characters in keys and elements can be represented in escape
        sequences similar to those used for character and string literals
        (see sections 3.3 and 3.10.6 of
        <cite>The Java Language Specification</cite>).
        
        The differences from the character escape sequences and Unicode
        escapes used for characters and strings are:
        
        
        -  Octal escapes are not recognized.
        
        -  The character sequence `\b` does *not*
        represent a backspace character.
        
        -  The method does not treat a backslash character,
        `\`, before a non-valid escape character as an
        error; the backslash is silently dropped.  For example, in a
        Java string the sequence `"\z"` would cause a
        compile time error.  In contrast, this method silently drops
        the backslash.  Therefore, this method treats the two character
        sequence `"\b"` as equivalent to the single
        character `'b'`.
        
        -  Escapes are not necessary for single and double quotes;
        however, by the rule above, single and double quote characters
        preceded by a backslash still yield single and double quote
        characters, respectively.
        
        -  Only a single 'u' character is allowed in a Unicode escape
        sequence.
        
        
        
        The specified stream remains open after this method returns.

        Arguments
        - reader: the input character stream.

        Raises
        - IOException: if an error occurred when reading from the
                 input stream.
        - IllegalArgumentException: if a malformed Unicode escape
                 appears in the input.
        - NullPointerException: if `reader` is null.

        Since
        - 1.6
        """
        ...


    def load(self, inStream: "InputStream") -> None:
        """
        Reads a property list (key and element pairs) from the input
        byte stream. The input stream is in a simple line-oriented
        format as specified in
        .load(java.io.Reader) load(Reader) and is assumed to use
        the ISO 8859-1 character encoding; that is each byte is one Latin1
        character. Characters not in Latin1, and certain special characters,
        are represented in keys and elements using Unicode escapes as defined in
        section 3.3 of
        <cite>The Java Language Specification</cite>.
        
        The specified stream remains open after this method returns.

        Arguments
        - inStream: the input stream.

        Raises
        - IOException: if an error occurred when reading from the
                    input stream.
        - IllegalArgumentException: if the input stream contains a
                    malformed Unicode escape sequence.
        - NullPointerException: if `inStream` is null.

        Since
        - 1.2
        """
        ...


    def save(self, out: "OutputStream", comments: str) -> None:
        """
        Calls the `store(OutputStream out, String comments)` method
        and suppresses IOExceptions that were thrown.

        Arguments
        - out: an output stream.
        - comments: a description of the property list.

        Raises
        - ClassCastException: if this `Properties` object
                    contains any keys or values that are not
                    `Strings`.

        Deprecated
        - This method does not throw an IOException if an I/O error
        occurs while saving the property list.  The preferred way to save a
        properties list is via the `store(OutputStream out,
        String comments)` method or the
        `storeToXML(OutputStream os, String comment)` method.
        """
        ...


    def store(self, writer: "Writer", comments: str) -> None:
        """
        Writes this property list (key and element pairs) in this
        `Properties` table to the output character stream in a
        format suitable for using the .load(java.io.Reader) load(Reader)
        method.
        
        Properties from the defaults table of this `Properties`
        table (if any) are *not* written out by this method.
        
        If the comments argument is not null, then an ASCII `.`
        character, the comments string, and a line separator are first written
        to the output stream. Thus, the `comments` can serve as an
        identifying comment. Any one of a line feed ('\n'), a carriage
        return ('\r'), or a carriage return followed immediately by a line feed
        in comments is replaced by a line separator generated by the `Writer`
        and if the next character in comments is not character `.` or
        character `!` then an ASCII `.` is written out
        after that line separator.
        
        Next, a comment line is always written, consisting of an ASCII
        `.` character, the current date and time (as if produced
        by the `toString` method of `Date` for the
        current time), and a line separator as generated by the `Writer`.
        
        Then every entry in this `Properties` table is
        written out, one per line. For each entry the key string is
        written, then an ASCII `=`, then the associated
        element string. For the key, all space characters are
        written with a preceding `\` character.  For the
        element, leading space characters, but not embedded or trailing
        space characters, are written with a preceding `\`
        character. The key and element characters `.`,
        `!`, `=`, and `:` are written
        with a preceding backslash to ensure that they are properly loaded.
        
        After the entries have been written, the output stream is flushed.
        The output stream remains open after this method returns.

        Arguments
        - writer: an output character stream writer.
        - comments: a description of the property list.

        Raises
        - IOException: if writing this property list to the specified
                    output stream throws an `IOException`.
        - ClassCastException: if this `Properties` object
                    contains any keys or values that are not `Strings`.
        - NullPointerException: if `writer` is null.

        Since
        - 1.6
        """
        ...


    def store(self, out: "OutputStream", comments: str) -> None:
        """
        Writes this property list (key and element pairs) in this
        `Properties` table to the output stream in a format suitable
        for loading into a `Properties` table using the
        .load(InputStream) load(InputStream) method.
        
        Properties from the defaults table of this `Properties`
        table (if any) are *not* written out by this method.
        
        This method outputs the comments, properties keys and values in
        the same format as specified in
        .store(java.io.Writer, java.lang.String) store(Writer),
        with the following differences:
        
        - The stream is written using the ISO 8859-1 character encoding.
        
        - Characters not in Latin-1 in the comments are written as
        `\u005Cu`*xxxx* for their appropriate unicode
        hexadecimal value *xxxx*.
        
        - Characters less than `\u005Cu0020` and characters greater
        than `\u005Cu007E` in property keys or values are written
        as `\u005Cu`*xxxx* for the appropriate hexadecimal
        value *xxxx*.
        
        
        After the entries have been written, the output stream is flushed.
        The output stream remains open after this method returns.

        Arguments
        - out: an output stream.
        - comments: a description of the property list.

        Raises
        - IOException: if writing this property list to the specified
                    output stream throws an `IOException`.
        - ClassCastException: if this `Properties` object
                    contains any keys or values that are not `Strings`.
        - NullPointerException: if `out` is null.

        Since
        - 1.2
        """
        ...


    def loadFromXML(self, in: "InputStream") -> None:
        """
        Loads all of the properties represented by the XML document on the
        specified input stream into this properties table.
        
        The XML document must have the following DOCTYPE declaration:
        ```
        &lt;!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd"&gt;
        ```
        Furthermore, the document must satisfy the properties DTD described
        above.
        
         An implementation is required to read XML documents that use the
        "`UTF-8`" or "`UTF-16`" encoding. An implementation may
        support additional encodings.
        
        The specified stream is closed after this method returns.

        Arguments
        - in: the input stream from which to read the XML document.

        Raises
        - IOException: if reading from the specified input stream
                results in an `IOException`.
        - java.io.UnsupportedEncodingException: if the document's encoding
                declaration can be read and it specifies an encoding that is not
                supported
        - InvalidPropertiesFormatException: Data on input stream does not
                constitute a valid XML document with the mandated document type.
        - NullPointerException: if `in` is null.

        See
        - <a href="http://www.w3.org/TR/REC-xml/.charencoding">Character
                Encoding in Entities</a>

        Since
        - 1.5
        """
        ...


    def storeToXML(self, os: "OutputStream", comment: str) -> None:
        """
        Emits an XML document representing all of the properties contained
        in this table.
        
         An invocation of this method of the form `props.storeToXML(os,
        comment)` behaves in exactly the same way as the invocation
        `props.storeToXML(os, comment, "UTF-8");`.

        Arguments
        - os: the output stream on which to emit the XML document.
        - comment: a description of the property list, or `null`
               if no comment is desired.

        Raises
        - IOException: if writing to the specified output stream
                results in an `IOException`.
        - NullPointerException: if `os` is null.
        - ClassCastException: if this `Properties` object
                contains any keys or values that are not
                `Strings`.

        See
        - .loadFromXML(InputStream)

        Since
        - 1.5
        """
        ...


    def storeToXML(self, os: "OutputStream", comment: str, encoding: str) -> None:
        """
        Emits an XML document representing all of the properties contained
        in this table, using the specified encoding.
        
        The XML document will have the following DOCTYPE declaration:
        ```
        &lt;!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd"&gt;
        ```
        
        If the specified comment is `null` then no comment
        will be stored in the document.
        
         An implementation is required to support writing of XML documents
        that use the "`UTF-8`" or "`UTF-16`" encoding. An
        implementation may support additional encodings.
        
        The specified stream remains open after this method returns.
        
        This method behaves the same as
        .storeToXML(OutputStream os, String comment, Charset charset)
        except that it will java.nio.charset.Charset.forName look up the charset
        using the given encoding name.

        Arguments
        - os: the output stream on which to emit the XML document.
        - comment: a description of the property list, or `null`
                         if no comment is desired.
        - encoding: the name of a supported
                         <a href="../lang/package-summary.html#charenc">
                         character encoding</a>

        Raises
        - IOException: if writing to the specified output stream
                results in an `IOException`.
        - java.io.UnsupportedEncodingException: if the encoding is not
                supported by the implementation.
        - NullPointerException: if `os` is `null`,
                or if `encoding` is `null`.
        - ClassCastException: if this `Properties` object
                contains any keys or values that are not `Strings`.

        See
        - <a href="http://www.w3.org/TR/REC-xml/.charencoding">Character
                Encoding in Entities</a>

        Since
        - 1.5
        """
        ...


    def storeToXML(self, os: "OutputStream", comment: str, charset: "Charset") -> None:
        """
        Emits an XML document representing all of the properties contained
        in this table, using the specified encoding.
        
        The XML document will have the following DOCTYPE declaration:
        ```
        &lt;!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd"&gt;
        ```
        
        If the specified comment is `null` then no comment
        will be stored in the document.
        
         An implementation is required to support writing of XML documents
        that use the "`UTF-8`" or "`UTF-16`" encoding. An
        implementation may support additional encodings.
        
         Unmappable characters for the specified charset will be encoded as
        numeric character references.
        
        The specified stream remains open after this method returns.

        Arguments
        - os: the output stream on which to emit the XML document.
        - comment: a description of the property list, or `null`
                         if no comment is desired.
        - charset: the charset

        Raises
        - IOException: if writing to the specified output stream
                results in an `IOException`.
        - NullPointerException: if `os` or `charset` is `null`.
        - ClassCastException: if this `Properties` object
                contains any keys or values that are not `Strings`.

        See
        - <a href="http://www.w3.org/TR/REC-xml/.charencoding">Character
                Encoding in Entities</a>

        Since
        - 10
        """
        ...


    def getProperty(self, key: str) -> str:
        """
        Searches for the property with the specified key in this property list.
        If the key is not found in this property list, the default property list,
        and its defaults, recursively, are then checked. The method returns
        `null` if the property is not found.

        Arguments
        - key: the property key.

        Returns
        - the value in this property list with the specified key value.

        See
        - .defaults
        """
        ...


    def getProperty(self, key: str, defaultValue: str) -> str:
        """
        Searches for the property with the specified key in this property list.
        If the key is not found in this property list, the default property list,
        and its defaults, recursively, are then checked. The method returns the
        default value argument if the property is not found.

        Arguments
        - key: the hashtable key.
        - defaultValue: a default value.

        Returns
        - the value in this property list with the specified key value.

        See
        - .defaults
        """
        ...


    def propertyNames(self) -> "Enumeration"[Any]:
        """
        Returns an enumeration of all the keys in this property list,
        including distinct keys in the default property list if a key
        of the same name has not already been found from the main
        properties list.

        Returns
        - an enumeration of all the keys in this property list, including
                 the keys in the default property list.

        Raises
        - ClassCastException: if any key in this property list
                 is not a string.

        See
        - .stringPropertyNames
        """
        ...


    def stringPropertyNames(self) -> set[str]:
        """
        Returns an unmodifiable set of keys from this property list
        where the key and its corresponding value are strings,
        including distinct keys in the default property list if a key
        of the same name has not already been found from the main
        properties list.  Properties whose key or value is not
        of type `String` are omitted.
        
        The returned set is not backed by this `Properties` object.
        Changes to this `Properties` object are not reflected in the
        returned set.

        Returns
        - an unmodifiable set of keys in this property list where
                 the key and its corresponding value are strings,
                 including the keys in the default property list.

        See
        - java.util.Properties.defaults

        Since
        - 1.6
        """
        ...


    def list(self, out: "PrintStream") -> None:
        """
        Prints this property list out to the specified output stream.
        This method is useful for debugging.

        Arguments
        - out: an output stream.

        Raises
        - ClassCastException: if any key in this property list
                 is not a string.
        """
        ...


    def list(self, out: "PrintWriter") -> None:
        ...


    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        ...


    def keys(self) -> "Enumeration"["Object"]:
        ...


    def elements(self) -> "Enumeration"["Object"]:
        ...


    def contains(self, value: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def get(self, key: "Object") -> "Object":
        ...


    def put(self, key: "Object", value: "Object") -> "Object":
        ...


    def remove(self, key: "Object") -> "Object":
        ...


    def putAll(self, t: dict[Any, Any]) -> None:
        ...


    def clear(self) -> None:
        ...


    def toString(self) -> str:
        ...


    def keySet(self) -> set["Object"]:
        ...


    def values(self) -> Iterable["Object"]:
        ...


    def entrySet(self) -> set["Map.Entry"["Object", "Object"]]:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def getOrDefault(self, key: "Object", defaultValue: "Object") -> "Object":
        ...


    def forEach(self, action: "BiConsumer"["Object", "Object"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["Object", "Object", Any]) -> None:
        ...


    def putIfAbsent(self, key: "Object", value: "Object") -> "Object":
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        ...


    def replace(self, key: "Object", oldValue: "Object", newValue: "Object") -> bool:
        ...


    def replace(self, key: "Object", value: "Object") -> "Object":
        ...


    def computeIfAbsent(self, key: "Object", mappingFunction: "Function"["Object", Any]) -> "Object":
        ...


    def computeIfPresent(self, key: "Object", remappingFunction: "BiFunction"["Object", "Object", Any]) -> "Object":
        ...


    def compute(self, key: "Object", remappingFunction: "BiFunction"["Object", "Object", Any]) -> "Object":
        ...


    def merge(self, key: "Object", value: "Object", remappingFunction: "BiFunction"["Object", "Object", Any]) -> "Object":
        ...


    def clone(self) -> "Object":
        ...
