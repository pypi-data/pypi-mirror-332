"""
Python module generated from Java source file java.util.stream.BaseStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import Charset
from java.nio.file import Files
from java.nio.file import Path
from java.util import Iterator
from java.util import Spliterator
from java.util.concurrent import ConcurrentHashMap
from java.util.function import IntConsumer
from java.util.function import Predicate
from java.util.stream import *
from typing import Any, Callable, Iterable, Tuple


class BaseStream(AutoCloseable):
    """
    Base interface for streams, which are sequences of elements supporting
    sequential and parallel aggregate operations.  The following example
    illustrates an aggregate operation using the stream types Stream
    and IntStream, computing the sum of the weights of the red widgets:
    
    ````int sum = widgets.stream()
                         .filter(w -> w.getColor() == RED)
                         .mapToInt(w -> w.getWeight())
                         .sum();````
    
    See the class documentation for Stream and the package documentation
    for <a href="package-summary.html">java.util.stream</a> for additional
    specification of streams, stream operations, stream pipelines, and
    parallelism, which governs the behavior of all stream types.
    
    Type `<T>`: the type of the stream elements
    
    Type `<S>`: the type of the stream implementing `BaseStream`

    See
    - <a href="package-summary.html">java.util.stream</a>

    Since
    - 1.8
    """

    def iterator(self) -> Iterator["T"]:
        """
        Returns an iterator for the elements of this stream.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - the element iterator for this stream
        """
        ...


    def spliterator(self) -> "Spliterator"["T"]:
        """
        Returns a spliterator for the elements of this stream.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.
        
        
        The returned spliterator should report the set of characteristics derived
        from the stream pipeline (namely the characteristics derived from the
        stream source spliterator and the intermediate operations).
        Implementations may report a sub-set of those characteristics.  For
        example, it may be too expensive to compute the entire set for some or
        all possible stream pipelines.

        Returns
        - the element spliterator for this stream
        """
        ...


    def isParallel(self) -> bool:
        """
        Returns whether this stream, if a terminal operation were to be executed,
        would execute in parallel.  Calling this method after invoking an
        terminal stream operation method may yield unpredictable results.

        Returns
        - `True` if this stream would execute in parallel if executed
        """
        ...


    def sequential(self) -> "S":
        """
        Returns an equivalent stream that is sequential.  May return
        itself, either because the stream was already sequential, or because
        the underlying stream state was modified to be sequential.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Returns
        - a sequential stream
        """
        ...


    def parallel(self) -> "S":
        """
        Returns an equivalent stream that is parallel.  May return
        itself, either because the stream was already parallel, or because
        the underlying stream state was modified to be parallel.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Returns
        - a parallel stream
        """
        ...


    def unordered(self) -> "S":
        """
        Returns an equivalent stream that is
        <a href="package-summary.html#Ordering">unordered</a>.  May return
        itself, either because the stream was already unordered, or because
        the underlying stream state was modified to be unordered.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Returns
        - an unordered stream
        """
        ...


    def onClose(self, closeHandler: "Runnable") -> "S":
        """
        Returns an equivalent stream with an additional close handler.  Close
        handlers are run when the .close() method
        is called on the stream, and are executed in the order they were
        added.  All close handlers are run, even if earlier close handlers throw
        exceptions.  If any close handler throws an exception, the first
        exception thrown will be relayed to the caller of `close()`, with
        any remaining exceptions added to that exception as suppressed exceptions
        (unless one of the remaining exceptions is the same exception as the
        first exception, since an exception cannot suppress itself.)  May
        return itself.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - closeHandler: A task to execute when the stream is closed

        Returns
        - a stream with a handler that is run if the stream is closed
        """
        ...


    def close(self) -> None:
        """
        Closes this stream, causing all close handlers for this stream pipeline
        to be called.

        See
        - AutoCloseable.close()
        """
        ...
