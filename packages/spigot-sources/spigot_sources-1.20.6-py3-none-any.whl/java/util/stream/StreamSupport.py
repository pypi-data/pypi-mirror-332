"""
Python module generated from Java source file java.util.stream.StreamSupport

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util import Spliterator
from java.util.function import Supplier
from java.util.stream import *
from typing import Any, Callable, Iterable, Tuple


class StreamSupport:
    """
    Low-level utility methods for creating and manipulating streams.
    
    This class is mostly for library writers presenting stream views
    of data structures; most static stream methods intended for end users are in
    the various `Stream` classes.

    Since
    - 1.8
    """

    @staticmethod
    def stream(spliterator: "Spliterator"["T"], parallel: bool) -> "Stream"["T"]:
        """
        Creates a new sequential or parallel `Stream` from a
        `Spliterator`.
        
        The spliterator is only traversed, split, or queried for estimated
        size after the terminal operation of the stream pipeline commences.
        
        It is strongly recommended the spliterator report a characteristic of
        `IMMUTABLE` or `CONCURRENT`, or be
        <a href="../Spliterator.html#binding">late-binding</a>.  Otherwise,
        .stream(java.util.function.Supplier, int, boolean) should be used
        to reduce the scope of potential interference with the source.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.
        
        Type `<T>`: the type of stream elements

        Arguments
        - spliterator: a `Spliterator` describing the stream elements
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `Stream`
        """
        ...


    @staticmethod
    def stream(supplier: "Supplier"["Spliterator"["T"]], characteristics: int, parallel: bool) -> "Stream"["T"]:
        """
        Creates a new sequential or parallel `Stream` from a
        `Supplier` of `Spliterator`.
        
        The Supplier.get() method will be invoked on the supplier no
        more than once, and only after the terminal operation of the stream pipeline
        commences.
        
        For spliterators that report a characteristic of `IMMUTABLE`
        or `CONCURRENT`, or that are
        <a href="../Spliterator.html#binding">late-binding</a>, it is likely
        more efficient to use .stream(java.util.Spliterator, boolean)
        instead.
        The use of a `Supplier` in this form provides a level of
        indirection that reduces the scope of potential interference with the
        source.  Since the supplier is only invoked after the terminal operation
        commences, any modifications to the source up to the start of the
        terminal operation are reflected in the stream result.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.
        
        Type `<T>`: the type of stream elements

        Arguments
        - supplier: a `Supplier` of a `Spliterator`
        - characteristics: Spliterator characteristics of the supplied
               `Spliterator`.  The characteristics must be equal to
               `supplier.get().characteristics()`, otherwise undefined
               behavior may occur when terminal operation commences.
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `Stream`

        See
        - .stream(java.util.Spliterator, boolean)
        """
        ...


    @staticmethod
    def intStream(spliterator: "Spliterator.OfInt", parallel: bool) -> "IntStream":
        """
        Creates a new sequential or parallel `IntStream` from a
        `Spliterator.OfInt`.
        
        The spliterator is only traversed, split, or queried for estimated size
        after the terminal operation of the stream pipeline commences.
        
        It is strongly recommended the spliterator report a characteristic of
        `IMMUTABLE` or `CONCURRENT`, or be
        <a href="../Spliterator.html#binding">late-binding</a>.  Otherwise,
        .intStream(java.util.function.Supplier, int, boolean) should be
        used to reduce the scope of potential interference with the source.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - spliterator: a `Spliterator.OfInt` describing the stream elements
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `IntStream`
        """
        ...


    @staticmethod
    def intStream(supplier: "Supplier"["Spliterator.OfInt"], characteristics: int, parallel: bool) -> "IntStream":
        """
        Creates a new sequential or parallel `IntStream` from a
        `Supplier` of `Spliterator.OfInt`.
        
        The Supplier.get() method will be invoked on the supplier no
        more than once, and only after the terminal operation of the stream pipeline
        commences.
        
        For spliterators that report a characteristic of `IMMUTABLE`
        or `CONCURRENT`, or that are
        <a href="../Spliterator.html#binding">late-binding</a>, it is likely
        more efficient to use .intStream(java.util.Spliterator.OfInt, boolean)
        instead.
        The use of a `Supplier` in this form provides a level of
        indirection that reduces the scope of potential interference with the
        source.  Since the supplier is only invoked after the terminal operation
        commences, any modifications to the source up to the start of the
        terminal operation are reflected in the stream result.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - supplier: a `Supplier` of a `Spliterator.OfInt`
        - characteristics: Spliterator characteristics of the supplied
               `Spliterator.OfInt`.  The characteristics must be equal to
               `supplier.get().characteristics()`, otherwise undefined
               behavior may occur when terminal operation commences.
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `IntStream`

        See
        - .intStream(java.util.Spliterator.OfInt, boolean)
        """
        ...


    @staticmethod
    def longStream(spliterator: "Spliterator.OfLong", parallel: bool) -> "LongStream":
        """
        Creates a new sequential or parallel `LongStream` from a
        `Spliterator.OfLong`.
        
        The spliterator is only traversed, split, or queried for estimated
        size after the terminal operation of the stream pipeline commences.
        
        It is strongly recommended the spliterator report a characteristic of
        `IMMUTABLE` or `CONCURRENT`, or be
        <a href="../Spliterator.html#binding">late-binding</a>.  Otherwise,
        .longStream(java.util.function.Supplier, int, boolean) should be
        used to reduce the scope of potential interference with the source.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - spliterator: a `Spliterator.OfLong` describing the stream elements
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `LongStream`
        """
        ...


    @staticmethod
    def longStream(supplier: "Supplier"["Spliterator.OfLong"], characteristics: int, parallel: bool) -> "LongStream":
        """
        Creates a new sequential or parallel `LongStream` from a
        `Supplier` of `Spliterator.OfLong`.
        
        The Supplier.get() method will be invoked on the supplier no
        more than once, and only after the terminal operation of the stream pipeline
        commences.
        
        For spliterators that report a characteristic of `IMMUTABLE`
        or `CONCURRENT`, or that are
        <a href="../Spliterator.html#binding">late-binding</a>, it is likely
        more efficient to use .longStream(java.util.Spliterator.OfLong, boolean)
        instead.
        The use of a `Supplier` in this form provides a level of
        indirection that reduces the scope of potential interference with the
        source.  Since the supplier is only invoked after the terminal operation
        commences, any modifications to the source up to the start of the
        terminal operation are reflected in the stream result.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - supplier: a `Supplier` of a `Spliterator.OfLong`
        - characteristics: Spliterator characteristics of the supplied
               `Spliterator.OfLong`.  The characteristics must be equal to
               `supplier.get().characteristics()`, otherwise undefined
               behavior may occur when terminal operation commences.
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `LongStream`

        See
        - .longStream(java.util.Spliterator.OfLong, boolean)
        """
        ...


    @staticmethod
    def doubleStream(spliterator: "Spliterator.OfDouble", parallel: bool) -> "DoubleStream":
        """
        Creates a new sequential or parallel `DoubleStream` from a
        `Spliterator.OfDouble`.
        
        The spliterator is only traversed, split, or queried for estimated size
        after the terminal operation of the stream pipeline commences.
        
        It is strongly recommended the spliterator report a characteristic of
        `IMMUTABLE` or `CONCURRENT`, or be
        <a href="../Spliterator.html#binding">late-binding</a>.  Otherwise,
        .doubleStream(java.util.function.Supplier, int, boolean) should
        be used to reduce the scope of potential interference with the source.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - spliterator: A `Spliterator.OfDouble` describing the stream elements
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `DoubleStream`
        """
        ...


    @staticmethod
    def doubleStream(supplier: "Supplier"["Spliterator.OfDouble"], characteristics: int, parallel: bool) -> "DoubleStream":
        """
        Creates a new sequential or parallel `DoubleStream` from a
        `Supplier` of `Spliterator.OfDouble`.
        
        The Supplier.get() method will be invoked on the supplier no
        more than once, and only after the terminal operation of the stream pipeline
        commences.
        
        For spliterators that report a characteristic of `IMMUTABLE`
        or `CONCURRENT`, or that are
        <a href="../Spliterator.html#binding">late-binding</a>, it is likely
        more efficient to use .doubleStream(java.util.Spliterator.OfDouble, boolean)
        instead.
        The use of a `Supplier` in this form provides a level of
        indirection that reduces the scope of potential interference with the
        source.  Since the supplier is only invoked after the terminal operation
        commences, any modifications to the source up to the start of the
        terminal operation are reflected in the stream result.  See
        <a href="package-summary.html#NonInterference">Non-Interference</a> for
        more details.

        Arguments
        - supplier: A `Supplier` of a `Spliterator.OfDouble`
        - characteristics: Spliterator characteristics of the supplied
               `Spliterator.OfDouble`.  The characteristics must be equal to
               `supplier.get().characteristics()`, otherwise undefined
               behavior may occur when terminal operation commences.
        - parallel: if `True` then the returned stream is a parallel
               stream; if `False` the returned stream is a sequential
               stream.

        Returns
        - a new sequential or parallel `DoubleStream`

        See
        - .doubleStream(java.util.Spliterator.OfDouble, boolean)
        """
        ...
