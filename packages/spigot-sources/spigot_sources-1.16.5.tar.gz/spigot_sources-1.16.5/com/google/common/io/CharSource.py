"""
Python module generated from Java source file com.google.common.io.CharSource

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Ascii
from com.google.common.base import Optional
from com.google.common.base import Splitter
from com.google.common.collect import AbstractIterator
from com.google.common.collect import ImmutableList
from com.google.common.collect import Lists
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import BufferedReader
from java.io import IOException
from java.io import InputStream
from java.io import Reader
from java.io import Writer
from java.nio.charset import Charset
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class CharSource:
    """
    A readable source of characters, such as a text file. Unlike a Reader, a
    `CharSource` is not an open, stateful stream of characters that can be read and closed.
    Instead, it is an immutable *supplier* of `Reader` instances.
    
    `CharSource` provides two kinds of methods:
    
    - **Methods that return a reader:** These methods should return a *new*, independent
        instance each time they are called. The caller is responsible for ensuring that the returned
        reader is closed.
    - **Convenience methods:** These are implementations of common operations that are typically
        implemented by opening a reader using one of the methods in the first category, doing
        something and finally closing the reader that was opened.
    
    
    Several methods in this class, such as .readLines(), break the contents of the source
    into lines. Like BufferedReader, these methods break lines on any of `\n`,
    `\r` or `\r\n`, do not include the line separator in each line and do not consider
    there to be an empty line at the end if the contents are terminated with a line separator.
    
    Any ByteSource containing text encoded with a specific Charset character
    encoding may be viewed as a `CharSource` using ByteSource.asCharSource(Charset).

    Author(s)
    - Colin Decker

    Since
    - 14.0
    """

    def asByteSource(self, charset: "Charset") -> "ByteSource":
        """
        Returns a ByteSource view of this char source that encodes chars read from this source
        as bytes using the given Charset.
        
        If ByteSource.asCharSource is called on the returned source with the same charset,
        the default implementation of this method will ensure that the original `CharSource` is
        returned, rather than round-trip encoding. Subclasses that override this method should behave
        the same way.

        Since
        - 20.0
        """
        ...


    def openStream(self) -> "Reader":
        """
        Opens a new Reader for reading from this source. This method should return a new,
        independent reader each time it is called.
        
        The caller is responsible for ensuring that the returned reader is closed.

        Raises
        - IOException: if an I/O error occurs in the process of opening the reader
        """
        ...


    def openBufferedStream(self) -> "BufferedReader":
        """
        Opens a new BufferedReader for reading from this source. This method should return a
        new, independent reader each time it is called.
        
        The caller is responsible for ensuring that the returned reader is closed.

        Raises
        - IOException: if an I/O error occurs in the process of opening the reader
        """
        ...


    def lengthIfKnown(self) -> "Optional"["Long"]:
        """
        Returns the size of this source in chars, if the size can be easily determined without actually
        opening the data stream.
        
        The default implementation returns Optional.absent. Some sources, such as a
        `CharSequence`, may return a non-absent value. Note that in such cases, it is
        *possible* that this method will return a different number of chars than would be returned
        by reading all of the chars.
        
        Additionally, for mutable sources such as `StringBuilder`s, a subsequent read may
        return a different number of chars if the contents are changed.

        Since
        - 19.0
        """
        ...


    def length(self) -> int:
        """
        Returns the length of this source in chars, even if doing so requires opening and traversing an
        entire stream. To avoid a potentially expensive operation, see .lengthIfKnown.
        
        The default implementation calls .lengthIfKnown and returns the value if present. If
        absent, it will fall back to a heavyweight operation that will open a stream,
        Reader.skip(long) skip to the end of the stream, and return the total number of chars
        that were skipped.
        
        Note that for sources that implement .lengthIfKnown to provide a more efficient
        implementation, it is *possible* that this method will return a different number of chars
        than would be returned by reading all of the chars.
        
        In either case, for mutable sources such as files, a subsequent read may return a different
        number of chars if the contents are changed.

        Raises
        - IOException: if an I/O error occurs in the process of reading the length of this source

        Since
        - 19.0
        """
        ...


    def copyTo(self, appendable: "Appendable") -> int:
        """
        Appends the contents of this source to the given Appendable (such as a Writer).
        Does not close `appendable` if it is `Closeable`.

        Returns
        - the number of characters copied

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source or
            writing to `appendable`
        """
        ...


    def copyTo(self, sink: "CharSink") -> int:
        """
        Copies the contents of this source to the given sink.

        Returns
        - the number of characters copied

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source or
            writing to `sink`
        """
        ...


    def read(self) -> str:
        """
        Reads the contents of this source as a string.

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source
        """
        ...


    def readFirstLine(self) -> str:
        """
        Reads the first line of this source as a string. Returns `null` if this source is empty.
        
        Like BufferedReader, this method breaks lines on any of `\n`, `\r` or
        `\r\n`, does not include the line separator in the returned line and does not consider
        there to be an extra empty line at the end if the content is terminated with a line separator.

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source
        """
        ...


    def readLines(self) -> "ImmutableList"[str]:
        """
        Reads all the lines of this source as a list of strings. The returned list will be empty if
        this source is empty.
        
        Like BufferedReader, this method breaks lines on any of `\n`, `\r` or
        `\r\n`, does not include the line separator in the returned lines and does not consider
        there to be an extra empty line at the end if the content is terminated with a line separator.

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source
        """
        ...


    def readLines(self, processor: "LineProcessor"["T"]) -> "T":
        """
        Reads lines of text from this source, processing each line as it is read using the given
        LineProcessor processor. Stops when all lines have been processed or the processor
        returns `False` and returns the result produced by the processor.
        
        Like BufferedReader, this method breaks lines on any of `\n`, `\r` or
        `\r\n`, does not include the line separator in the lines passed to the `processor`
        and does not consider there to be an extra empty line at the end if the content is terminated
        with a line separator.

        Raises
        - IOException: if an I/O error occurs in the process of reading from this source or if
            `processor` throws an `IOException`

        Since
        - 16.0
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns whether the source has zero chars. The default implementation returns True if
        .lengthIfKnown returns zero, falling back to opening a stream and checking for EOF if
        the length is not known.
        
        Note that, in cases where `lengthIfKnown` returns zero, it is *possible* that
        chars are actually available for reading. This means that a source may return `True` from
        `isEmpty()` despite having readable content.

        Raises
        - IOException: if an I/O error occurs

        Since
        - 15.0
        """
        ...


    @staticmethod
    def concat(sources: Iterable["CharSource"]) -> "CharSource":
        """
        Concatenates multiple CharSource instances into a single source. Streams returned from
        the source will contain the concatenated data from the streams of the underlying sources.
        
        Only one underlying stream will be open at a time. Closing the concatenated stream will
        close the open underlying stream.

        Arguments
        - sources: the sources to concatenate

        Returns
        - a `CharSource` containing the concatenated data

        Since
        - 15.0
        """
        ...


    @staticmethod
    def concat(sources: Iterator["CharSource"]) -> "CharSource":
        """
        Concatenates multiple CharSource instances into a single source. Streams returned from
        the source will contain the concatenated data from the streams of the underlying sources.
        
        Only one underlying stream will be open at a time. Closing the concatenated stream will
        close the open underlying stream.
        
        Note: The input `Iterator` will be copied to an `ImmutableList` when this method
        is called. This will fail if the iterator is infinite and may cause problems if the iterator
        eagerly fetches data for each source when iterated (rather than producing sources that only
        load data through their streams). Prefer using the .concat(Iterable) overload if
        possible.

        Arguments
        - sources: the sources to concatenate

        Returns
        - a `CharSource` containing the concatenated data

        Raises
        - NullPointerException: if any of `sources` is `null`

        Since
        - 15.0
        """
        ...


    @staticmethod
    def concat(*sources: Tuple["CharSource", ...]) -> "CharSource":
        """
        Concatenates multiple CharSource instances into a single source. Streams returned from
        the source will contain the concatenated data from the streams of the underlying sources.
        
        Only one underlying stream will be open at a time. Closing the concatenated stream will
        close the open underlying stream.

        Arguments
        - sources: the sources to concatenate

        Returns
        - a `CharSource` containing the concatenated data

        Raises
        - NullPointerException: if any of `sources` is `null`

        Since
        - 15.0
        """
        ...


    @staticmethod
    def wrap(charSequence: "CharSequence") -> "CharSource":
        """
        Returns a view of the given character sequence as a CharSource. The behavior of the
        returned `CharSource` and any `Reader` instances created by it is unspecified if
        the `charSequence` is mutated while it is being read, so don't do that.

        Since
        - 15.0 (since 14.0 as `CharStreams.asCharSource(String)`)
        """
        ...


    @staticmethod
    def empty() -> "CharSource":
        """
        Returns an immutable CharSource that contains no characters.

        Since
        - 15.0
        """
        ...
