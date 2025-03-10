"""
Python module generated from Java source file com.google.common.collect.Streams

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.math import LongMath
from java.util import ArrayDeque
from java.util import Deque
from java.util import Iterator
from java.util import OptionalDouble
from java.util import OptionalInt
from java.util import OptionalLong
from java.util import PrimitiveIterator
from java.util import Spliterator
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import DoubleConsumer
from java.util.function import IntConsumer
from java.util.function import LongConsumer
from java.util.stream import DoubleStream
from java.util.stream import IntStream
from java.util.stream import LongStream
from java.util.stream import Stream
from java.util.stream import StreamSupport
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Streams:
    """
    Static utility methods related to `Stream` instances.

    Since
    - 21.0
    """

    @staticmethod
    def stream(iterable: Iterable["T"]) -> "Stream"["T"]:
        """
        Returns a sequential Stream of the contents of `iterable`, delegating to Collection.stream if possible.
        """
        ...


    @staticmethod
    def stream(collection: Iterable["T"]) -> "Stream"["T"]:
        """
        Returns Collection.stream.

        Deprecated
        - There is no reason to use this; just invoke `collection.stream()` directly.
        """
        ...


    @staticmethod
    def stream(iterator: Iterator["T"]) -> "Stream"["T"]:
        """
        Returns a sequential Stream of the remaining contents of `iterator`. Do not use
        `iterator` directly after passing it to this method.
        """
        ...


    @staticmethod
    def stream(optional: "com.google.common.base.Optional"["T"]) -> "Stream"["T"]:
        """
        If a value is present in `optional`, returns a stream containing only that element,
        otherwise returns an empty stream.
        """
        ...


    @staticmethod
    def stream(optional: "java.util.Optional"["T"]) -> "Stream"["T"]:
        """
        If a value is present in `optional`, returns a stream containing only that element,
        otherwise returns an empty stream.
        
        **Java 9 users:** use `optional.stream()` instead.
        """
        ...


    @staticmethod
    def concat(*streams: Tuple["Stream"["T"], ...]) -> "Stream"["T"]:
        """
        Returns a Stream containing the elements of the first stream, followed by the elements
        of the second stream, and so on.
        
        This is equivalent to `Stream.of(streams).flatMap(stream -> stream)`, but the returned
        stream may perform better.

        See
        - Stream.concat(Stream, Stream)
        """
        ...


    @staticmethod
    def concat(*streams: Tuple["IntStream", ...]) -> "IntStream":
        """
        Returns an IntStream containing the elements of the first stream, followed by the
        elements of the second stream, and so on.
        
        This is equivalent to `Stream.of(streams).flatMapToInt(stream -> stream)`, but the
        returned stream may perform better.

        See
        - IntStream.concat(IntStream, IntStream)
        """
        ...


    @staticmethod
    def concat(*streams: Tuple["LongStream", ...]) -> "LongStream":
        """
        Returns a LongStream containing the elements of the first stream, followed by the
        elements of the second stream, and so on.
        
        This is equivalent to `Stream.of(streams).flatMapToLong(stream -> stream)`, but the
        returned stream may perform better.

        See
        - LongStream.concat(LongStream, LongStream)
        """
        ...


    @staticmethod
    def concat(*streams: Tuple["DoubleStream", ...]) -> "DoubleStream":
        """
        Returns a DoubleStream containing the elements of the first stream, followed by the
        elements of the second stream, and so on.
        
        This is equivalent to `Stream.of(streams).flatMapToDouble(stream -> stream)`, but the
        returned stream may perform better.

        See
        - DoubleStream.concat(DoubleStream, DoubleStream)
        """
        ...


    @staticmethod
    def stream(optional: "OptionalInt") -> "IntStream":
        """
        If a value is present in `optional`, returns a stream containing only that element,
        otherwise returns an empty stream.
        
        **Java 9 users:** use `optional.stream()` instead.
        """
        ...


    @staticmethod
    def stream(optional: "OptionalLong") -> "LongStream":
        """
        If a value is present in `optional`, returns a stream containing only that element,
        otherwise returns an empty stream.
        
        **Java 9 users:** use `optional.stream()` instead.
        """
        ...


    @staticmethod
    def stream(optional: "OptionalDouble") -> "DoubleStream":
        """
        If a value is present in `optional`, returns a stream containing only that element,
        otherwise returns an empty stream.
        
        **Java 9 users:** use `optional.stream()` instead.
        """
        ...


    @staticmethod
    def findLast(stream: "Stream"["T"]) -> "java.util.Optional"["T"]:
        """
        Returns the last element of the specified stream, or java.util.Optional.empty if the
        stream is empty.
        
        Equivalent to `stream.reduce((a, b) -> b)`, but may perform significantly better. This
        method's runtime will be between O(log n) and O(n), performing better on <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        streams.
        
        If the stream has nondeterministic order, this has equivalent semantics to Stream.findAny (which you might as well use).

        Raises
        - NullPointerException: if the last element of the stream is null

        See
        - Stream.findFirst()
        """
        ...


    @staticmethod
    def findLast(stream: "IntStream") -> "OptionalInt":
        """
        Returns the last element of the specified stream, or OptionalInt.empty if the stream is
        empty.
        
        Equivalent to `stream.reduce((a, b) -> b)`, but may perform significantly better. This
        method's runtime will be between O(log n) and O(n), performing better on <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        streams.

        Raises
        - NullPointerException: if the last element of the stream is null

        See
        - IntStream.findFirst()
        """
        ...


    @staticmethod
    def findLast(stream: "LongStream") -> "OptionalLong":
        """
        Returns the last element of the specified stream, or OptionalLong.empty if the stream
        is empty.
        
        Equivalent to `stream.reduce((a, b) -> b)`, but may perform significantly better. This
        method's runtime will be between O(log n) and O(n), performing better on <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        streams.

        Raises
        - NullPointerException: if the last element of the stream is null

        See
        - LongStream.findFirst()
        """
        ...


    @staticmethod
    def findLast(stream: "DoubleStream") -> "OptionalDouble":
        """
        Returns the last element of the specified stream, or OptionalDouble.empty if the stream
        is empty.
        
        Equivalent to `stream.reduce((a, b) -> b)`, but may perform significantly better. This
        method's runtime will be between O(log n) and O(n), performing better on <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        streams.

        Raises
        - NullPointerException: if the last element of the stream is null

        See
        - DoubleStream.findFirst()
        """
        ...


    @staticmethod
    def zip(streamA: "Stream"["A"], streamB: "Stream"["B"], function: "BiFunction"["A", "B", "R"]) -> "Stream"["R"]:
        """
        Returns a stream in which each element is the result of passing the corresponding element of
        each of `streamA` and `streamB` to `function`.
        
        For example:
        
        ````Streams.zip(
          Stream.of("foo1", "foo2", "foo3"),
          Stream.of("bar1", "bar2"),
          (arg1, arg2) -> arg1 + ":" + arg2)````
        
        will return `Stream.of("foo1:bar1", "foo2:bar2")`.
        
        The resulting stream will only be as long as the shorter of the two input streams; if one
        stream is longer, its extra elements will be ignored.
        
        The resulting stream is not <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>.
        This may harm parallel performance.
        """
        ...


    @staticmethod
    def mapWithIndex(stream: "Stream"["T"], function: "FunctionWithIndex"["T", "R"]) -> "Stream"["R"]:
        """
        Returns a stream consisting of the results of applying the given function to the elements of
        `stream` and their indices in the stream. For example,
        
        ````mapWithIndex(
            Stream.of("a", "b", "c"),
            (str, index) -> str + ":" + index)````
        
        would return `Stream.of("a:0", "b:1", "c:2")`.
        
        The resulting stream is <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        if and only if `stream` was efficiently splittable and its underlying spliterator
        reported Spliterator.SUBSIZED. This is generally the case if the underlying stream
        comes from a data structure supporting efficient indexed random access, typically an array or
        list.
        
        The order of the resulting stream is defined if and only if the order of the original stream
        was defined.
        """
        ...


    @staticmethod
    def mapWithIndex(stream: "IntStream", function: "IntFunctionWithIndex"["R"]) -> "Stream"["R"]:
        """
        Returns a stream consisting of the results of applying the given function to the elements of
        `stream` and their indexes in the stream. For example,
        
        ````mapWithIndex(
            IntStream.of(0, 1, 2),
            (i, index) -> i + ":" + index)````
        
        ...would return `Stream.of("0:0", "1:1", "2:2")`.
        
        The resulting stream is <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        if and only if `stream` was efficiently splittable and its underlying spliterator
        reported Spliterator.SUBSIZED. This is generally the case if the underlying stream
        comes from a data structure supporting efficient indexed random access, typically an array or
        list.
        
        The order of the resulting stream is defined if and only if the order of the original stream
        was defined.
        """
        ...


    @staticmethod
    def mapWithIndex(stream: "LongStream", function: "LongFunctionWithIndex"["R"]) -> "Stream"["R"]:
        """
        Returns a stream consisting of the results of applying the given function to the elements of
        `stream` and their indexes in the stream. For example,
        
        ````mapWithIndex(
            LongStream.of(0, 1, 2),
            (i, index) -> i + ":" + index)````
        
        ...would return `Stream.of("0:0", "1:1", "2:2")`.
        
        The resulting stream is <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        if and only if `stream` was efficiently splittable and its underlying spliterator
        reported Spliterator.SUBSIZED. This is generally the case if the underlying stream
        comes from a data structure supporting efficient indexed random access, typically an array or
        list.
        
        The order of the resulting stream is defined if and only if the order of the original stream
        was defined.
        """
        ...


    @staticmethod
    def mapWithIndex(stream: "DoubleStream", function: "DoubleFunctionWithIndex"["R"]) -> "Stream"["R"]:
        """
        Returns a stream consisting of the results of applying the given function to the elements of
        `stream` and their indexes in the stream. For example,
        
        ````mapWithIndex(
            DoubleStream.of(0, 1, 2),
            (x, index) -> x + ":" + index)````
        
        ...would return `Stream.of("0.0:0", "1.0:1", "2.0:2")`.
        
        The resulting stream is <a
        href="http://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html">efficiently splittable</a>
        if and only if `stream` was efficiently splittable and its underlying spliterator
        reported Spliterator.SUBSIZED. This is generally the case if the underlying stream
        comes from a data structure supporting efficient indexed random access, typically an array or
        list.
        
        The order of the resulting stream is defined if and only if the order of the original stream
        was defined.
        """
        ...


    class FunctionWithIndex:
        """
        An analogue of java.util.function.Function also accepting an index.
        
        This interface is only intended for use by callers of .mapWithIndex(Stream,
        FunctionWithIndex).

        Since
        - 21.0
        """

        def apply(self, from: "T", index: int) -> "R":
            """
            Applies this function to the given argument and its index within a stream.
            """
            ...


    class IntFunctionWithIndex:
        """
        An analogue of java.util.function.IntFunction also accepting an index.
        
        This interface is only intended for use by callers of .mapWithIndex(IntStream,
        IntFunctionWithIndex).

        Since
        - 21.0
        """

        def apply(self, from: int, index: int) -> "R":
            """
            Applies this function to the given argument and its index within a stream.
            """
            ...


    class LongFunctionWithIndex:
        """
        An analogue of java.util.function.LongFunction also accepting an index.
        
        This interface is only intended for use by callers of .mapWithIndex(LongStream,
        LongFunctionWithIndex).

        Since
        - 21.0
        """

        def apply(self, from: int, index: int) -> "R":
            """
            Applies this function to the given argument and its index within a stream.
            """
            ...


    class DoubleFunctionWithIndex:
        """
        An analogue of java.util.function.DoubleFunction also accepting an index.
        
        This interface is only intended for use by callers of .mapWithIndex(DoubleStream,
        DoubleFunctionWithIndex).

        Since
        - 21.0
        """

        def apply(self, from: float, index: int) -> "R":
            """
            Applies this function to the given argument and its index within a stream.
            """
            ...
