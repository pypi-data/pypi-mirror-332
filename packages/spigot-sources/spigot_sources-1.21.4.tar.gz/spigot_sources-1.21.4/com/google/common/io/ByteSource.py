"""
Python module generated from Java source file com.google.common.io.ByteSource

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Ascii
from com.google.common.base import Optional
from com.google.common.collect import ImmutableList
from com.google.common.hash import Funnels
from com.google.common.hash import HashCode
from com.google.common.hash import HashFunction
from com.google.common.hash import Hasher
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import BufferedInputStream
from java.io import ByteArrayInputStream
from java.io import IOException
from java.io import InputStream
from java.io import InputStreamReader
from java.io import OutputStream
from java.io import Reader
from java.nio.charset import Charset
from java.util import Arrays
from java.util import Iterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ByteSource:
    """
    A readable source of bytes, such as a file. Unlike an InputStream, a `ByteSource`
    is not an open, stateful stream for input that can be read and closed. Instead, it is an
    immutable *supplier* of `InputStream` instances.
    
    `ByteSource` provides two kinds of methods:
    
    
      - **Methods that return a stream:** These methods should return a *new*, independent
          instance each time they are called. The caller is responsible for ensuring that the
          returned stream is closed.
      - **Convenience methods:** These are implementations of common operations that are
          typically implemented by opening a stream using one of the methods in the first category,
          doing something and finally closing the stream that was opened.
    
    
    **Note:** In general, `ByteSource` is intended to be used for "file-like" sources
    that provide streams that are:
    
    
      - **Finite:** Many operations, such as .size() and .read(), will either
          block indefinitely or fail if the source creates an infinite stream.
      - **Non-destructive:** A *destructive* stream will consume or otherwise alter the
          bytes of the source as they are read from it. A source that provides such streams will not
          be reusable, and operations that read from the stream (including .size(), in some
          implementations) will prevent further operations from completing as expected.

    Author(s)
    - Colin Decker

    Since
    - 14.0
    """

    def asCharSource(self, charset: "Charset") -> "CharSource":
        """
        Returns a CharSource view of this byte source that decodes bytes read from this source
        as characters using the given Charset.
        
        If CharSource.asByteSource is called on the returned source with the same charset,
        the default implementation of this method will ensure that the original `ByteSource` is
        returned, rather than round-trip encoding. Subclasses that override this method should behave
        the same way.
        """
        ...


    def openStream(self) -> "InputStream":
        """
        Opens a new InputStream for reading from this source. This method returns a new,
        independent stream each time it is called.
        
        The caller is responsible for ensuring that the returned stream is closed.

        Raises
        - IOException: if an I/O error occurs while opening the stream
        """
        ...


    def openBufferedStream(self) -> "InputStream":
        """
        Opens a new buffered InputStream for reading from this source. The returned stream is
        not required to be a BufferedInputStream in order to allow implementations to simply
        delegate to .openStream() when the stream returned by that method does not benefit from
        additional buffering (for example, a `ByteArrayInputStream`). This method returns a new,
        independent stream each time it is called.
        
        The caller is responsible for ensuring that the returned stream is closed.

        Raises
        - IOException: if an I/O error occurs while opening the stream

        Since
        - 15.0 (in 14.0 with return type BufferedInputStream)
        """
        ...


    def slice(self, offset: int, length: int) -> "ByteSource":
        """
        Returns a view of a slice of this byte source that is at most `length` bytes long
        starting at the given `offset`. If `offset` is greater than the size of this
        source, the returned source will be empty. If `offset + length` is greater than the size
        of this source, the returned source will contain the slice starting at `offset` and
        ending at the end of this source.

        Raises
        - IllegalArgumentException: if `offset` or `length` is negative
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns whether the source has zero bytes. The default implementation first checks .sizeIfKnown, returning True if it's known to be zero and False if it's known to be non-zero.
        If the size is not known, it falls back to opening a stream and checking for EOF.
        
        Note that, in cases where `sizeIfKnown` returns zero, it is *possible* that bytes
        are actually available for reading. (For example, some special files may return a size of 0
        despite actually having content when read.) This means that a source may return `True`
        from `isEmpty()` despite having readable content.

        Raises
        - IOException: if an I/O error occurs

        Since
        - 15.0
        """
        ...


    def sizeIfKnown(self) -> "Optional"["Long"]:
        """
        Returns the size of this source in bytes, if the size can be easily determined without actually
        opening the data stream.
        
        The default implementation returns Optional.absent. Some sources, such as a file,
        may return a non-absent value. Note that in such cases, it is *possible* that this method
        will return a different number of bytes than would be returned by reading all of the bytes (for
        example, some special files may return a size of 0 despite actually having content when read).
        
        Additionally, for mutable sources such as files, a subsequent read may return a different
        number of bytes if the contents are changed.

        Since
        - 19.0
        """
        ...


    def size(self) -> int:
        """
        Returns the size of this source in bytes, even if doing so requires opening and traversing an
        entire stream. To avoid a potentially expensive operation, see .sizeIfKnown.
        
        The default implementation calls .sizeIfKnown and returns the value if present. If
        absent, it will fall back to a heavyweight operation that will open a stream, read (or InputStream.skip(long) skip, if possible) to the end of the stream and return the total number
        of bytes that were read.
        
        Note that for some sources that implement .sizeIfKnown to provide a more efficient
        implementation, it is *possible* that this method will return a different number of bytes
        than would be returned by reading all of the bytes (for example, some special files may return
        a size of 0 despite actually having content when read).
        
        In either case, for mutable sources such as files, a subsequent read may return a different
        number of bytes if the contents are changed.

        Raises
        - IOException: if an I/O error occurs while reading the size of this source
        """
        ...


    def copyTo(self, output: "OutputStream") -> int:
        """
        Copies the contents of this byte source to the given `OutputStream`. Does not close
        `output`.

        Returns
        - the number of bytes copied

        Raises
        - IOException: if an I/O error occurs while reading from this source or writing to `output`
        """
        ...


    def copyTo(self, sink: "ByteSink") -> int:
        """
        Copies the contents of this byte source to the given `ByteSink`.

        Returns
        - the number of bytes copied

        Raises
        - IOException: if an I/O error occurs while reading from this source or writing to `sink`
        """
        ...


    def read(self) -> list[int]:
        """
        Reads the full contents of this byte source as a byte array.

        Raises
        - IOException: if an I/O error occurs while reading from this source
        """
        ...


    def read(self, processor: "ByteProcessor"["T"]) -> "T":
        """
        Reads the contents of this byte source using the given `processor` to process bytes as
        they are read. Stops when all bytes have been read or the consumer returns `False`.
        Returns the result produced by the processor.

        Raises
        - IOException: if an I/O error occurs while reading from this source or if `processor` throws an `IOException`

        Since
        - 16.0
        """
        ...


    def hash(self, hashFunction: "HashFunction") -> "HashCode":
        """
        Hashes the contents of this byte source using the given hash function.

        Raises
        - IOException: if an I/O error occurs while reading from this source
        """
        ...


    def contentEquals(self, other: "ByteSource") -> bool:
        """
        Checks that the contents of this byte source are equal to the contents of the given byte
        source.

        Raises
        - IOException: if an I/O error occurs while reading from this source or `other`
        """
        ...


    @staticmethod
    def concat(sources: Iterable["ByteSource"]) -> "ByteSource":
        """
        Concatenates multiple ByteSource instances into a single source. Streams returned from
        the source will contain the concatenated data from the streams of the underlying sources.
        
        Only one underlying stream will be open at a time. Closing the concatenated stream will
        close the open underlying stream.

        Arguments
        - sources: the sources to concatenate

        Returns
        - a `ByteSource` containing the concatenated data

        Since
        - 15.0
        """
        ...


    @staticmethod
    def concat(sources: Iterator["ByteSource"]) -> "ByteSource":
        """
        Concatenates multiple ByteSource instances into a single source. Streams returned from
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
        - a `ByteSource` containing the concatenated data

        Raises
        - NullPointerException: if any of `sources` is `null`

        Since
        - 15.0
        """
        ...


    @staticmethod
    def concat(*sources: Tuple["ByteSource", ...]) -> "ByteSource":
        """
        Concatenates multiple ByteSource instances into a single source. Streams returned from
        the source will contain the concatenated data from the streams of the underlying sources.
        
        Only one underlying stream will be open at a time. Closing the concatenated stream will
        close the open underlying stream.

        Arguments
        - sources: the sources to concatenate

        Returns
        - a `ByteSource` containing the concatenated data

        Raises
        - NullPointerException: if any of `sources` is `null`

        Since
        - 15.0
        """
        ...


    @staticmethod
    def wrap(b: list[int]) -> "ByteSource":
        """
        Returns a view of the given byte array as a ByteSource. To view only a specific range
        in the array, use `ByteSource.wrap(b).slice(offset, length)`.
        
        Note that the given byte array may be passed directly to methods on, for example, `OutputStream` (when `copyTo(OutputStream)` is called on the resulting `ByteSource`). This could allow a malicious `OutputStream` implementation to modify the
        contents of the array, but provides better performance in the normal case.

        Since
        - 15.0 (since 14.0 as `ByteStreams.asByteSource(byte[])`).
        """
        ...


    @staticmethod
    def empty() -> "ByteSource":
        """
        Returns an immutable ByteSource that contains no bytes.

        Since
        - 15.0
        """
        ...
