"""
Python module generated from Java source file java.util.stream.DoubleStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util import DoubleSummaryStatistics
from java.util import Objects
from java.util import OptionalDouble
from java.util import PrimitiveIterator
from java.util import Spliterator
from java.util.function import BiConsumer
from java.util.function import DoubleBinaryOperator
from java.util.function import DoubleConsumer
from java.util.function import DoubleFunction
from java.util.function import DoublePredicate
from java.util.function import DoubleSupplier
from java.util.function import DoubleToIntFunction
from java.util.function import DoubleToLongFunction
from java.util.function import DoubleUnaryOperator
from java.util.function import Function
from java.util.function import ObjDoubleConsumer
from java.util.function import Supplier
from java.util.stream import *
from typing import Any, Callable, Iterable, Tuple


class DoubleStream(BaseStream):
    """
    A sequence of primitive double-valued elements supporting sequential and parallel
    aggregate operations.  This is the `double` primitive specialization of
    Stream.
    
    The following example illustrates an aggregate operation using
    Stream and DoubleStream, computing the sum of the weights of the
    red widgets:
    
    ````double sum = widgets.stream()
                            .filter(w -> w.getColor() == RED)
                            .mapToDouble(w -> w.getWeight())
                            .sum();````
    
    See the class documentation for Stream and the package documentation
    for <a href="package-summary.html">java.util.stream</a> for additional
    specification of streams, stream operations, stream pipelines, and
    parallelism.

    See
    - <a href="package-summary.html">java.util.stream</a>

    Since
    - 1.8
    """

    def filter(self, predicate: "DoublePredicate") -> "DoubleStream":
        """
        Returns a stream consisting of the elements of this stream that match
        the given predicate.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to each element to determine if it
                         should be included

        Returns
        - the new stream
        """
        ...


    def map(self, mapper: "DoubleUnaryOperator") -> "DoubleStream":
        """
        Returns a stream consisting of the results of applying the given
        function to the elements of this stream.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function to apply to each element

        Returns
        - the new stream
        """
        ...


    def mapToObj(self, mapper: "DoubleFunction"["U"]) -> "Stream"["U"]:
        """
        Returns an object-valued `Stream` consisting of the results of
        applying the given function to the elements of this stream.
        
        This is an <a href="package-summary.html#StreamOps">
            intermediate operation</a>.
        
        Type `<U>`: the element type of the new stream

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function to apply to each element

        Returns
        - the new stream
        """
        ...


    def mapToInt(self, mapper: "DoubleToIntFunction") -> "IntStream":
        """
        Returns an `IntStream` consisting of the results of applying the
        given function to the elements of this stream.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function to apply to each element

        Returns
        - the new stream
        """
        ...


    def mapToLong(self, mapper: "DoubleToLongFunction") -> "LongStream":
        """
        Returns a `LongStream` consisting of the results of applying the
        given function to the elements of this stream.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function to apply to each element

        Returns
        - the new stream
        """
        ...


    def flatMap(self, mapper: "DoubleFunction"["DoubleStream"]) -> "DoubleStream":
        """
        Returns a stream consisting of the results of replacing each element of
        this stream with the contents of a mapped stream produced by applying
        the provided mapping function to each element.  Each mapped stream is
        java.util.stream.BaseStream.close() closed after its contents
        have been placed into this stream.  (If a mapped stream is `null`
        an empty stream is used, instead.)
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function to apply to each element which produces a
                      `DoubleStream` of new values

        Returns
        - the new stream

        See
        - Stream.flatMap(Function)
        """
        ...


    def mapMulti(self, mapper: "DoubleMapMultiConsumer") -> "DoubleStream":
        """
        Returns a stream consisting of the results of replacing each element of
        this stream with multiple elements, specifically zero or more elements.
        Replacement is performed by applying the provided mapping function to each
        element in conjunction with a DoubleConsumer consumer argument
        that accepts replacement elements. The mapping function calls the consumer
        zero or more times to provide the replacement elements.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.
        
        If the DoubleConsumer consumer argument is used outside the scope of
        its application to the mapping function, the results are undefined.

        Arguments
        - mapper: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                      <a href="package-summary.html#Statelessness">stateless</a>
                      function that generates replacement elements

        Returns
        - the new stream

        See
        - Stream.mapMulti Stream.mapMulti

        Since
        - 16

        Unknown Tags
        - The default implementation invokes .flatMap flatMap on this stream,
        passing a function that behaves as follows. First, it calls the mapper function
        with a `DoubleConsumer` that accumulates replacement elements into a newly created
        internal buffer. When the mapper function returns, it creates a `DoubleStream` from the
        internal buffer. Finally, it returns this stream to `flatMap`.
        """
        ...


    def distinct(self) -> "DoubleStream":
        """
        Returns a stream consisting of the distinct elements of this stream. The
        elements are compared for equality according to
        java.lang.Double.compare(double, double).
        
        This is a <a href="package-summary.html#StreamOps">stateful
        intermediate operation</a>.

        Returns
        - the result stream
        """
        ...


    def sorted(self) -> "DoubleStream":
        """
        Returns a stream consisting of the elements of this stream in sorted
        order. The elements are compared for equality according to
        java.lang.Double.compare(double, double).
        
        This is a <a href="package-summary.html#StreamOps">stateful
        intermediate operation</a>.

        Returns
        - the result stream
        """
        ...


    def peek(self, action: "DoubleConsumer") -> "DoubleStream":
        """
        Returns a stream consisting of the elements of this stream, additionally
        performing the provided action on each element as elements are consumed
        from the resulting stream.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.
        
        For parallel stream pipelines, the action may be called at
        whatever time and in whatever thread the element is made available by the
        upstream operation.  If the action modifies shared state,
        it is responsible for providing the required synchronization.

        Arguments
        - action: a <a href="package-summary.html#NonInterference">
                      non-interfering</a> action to perform on the elements as
                      they are consumed from the stream

        Returns
        - the new stream

        Unknown Tags
        - This method exists mainly to support debugging, where you want
        to see the elements as they flow past a certain point in a pipeline:
        ````DoubleStream.of(1, 2, 3, 4)
                .filter(e -> e > 2)
                .peek(e -> System.out.println("Filtered value: " + e))
                .map(e -> e * e)
                .peek(e -> System.out.println("Mapped value: " + e))
                .sum();````
        
        In cases where the stream implementation is able to optimize away the
        production of some or all the elements (such as with short-circuiting
        operations like `findFirst`, or in the example described in
        .count), the action will not be invoked for those elements.
        """
        ...


    def limit(self, maxSize: int) -> "DoubleStream":
        """
        Returns a stream consisting of the elements of this stream, truncated
        to be no longer than `maxSize` in length.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        stateful intermediate operation</a>.

        Arguments
        - maxSize: the number of elements the stream should be limited to

        Returns
        - the new stream

        Raises
        - IllegalArgumentException: if `maxSize` is negative

        Unknown Tags
        - While `limit()` is generally a cheap operation on sequential
        stream pipelines, it can be quite expensive on ordered parallel pipelines,
        especially for large values of `maxSize`, since `limit(n)`
        is constrained to return not just any *n* elements, but the
        *first n* elements in the encounter order.  Using an unordered
        stream source (such as .generate(DoubleSupplier)) or removing the
        ordering constraint with .unordered() may result in significant
        speedups of `limit()` in parallel pipelines, if the semantics of
        your situation permit.  If consistency with encounter order is required,
        and you are experiencing poor performance or memory utilization with
        `limit()` in parallel pipelines, switching to sequential execution
        with .sequential() may improve performance.
        """
        ...


    def skip(self, n: int) -> "DoubleStream":
        """
        Returns a stream consisting of the remaining elements of this stream
        after discarding the first `n` elements of the stream.
        If this stream contains fewer than `n` elements then an
        empty stream will be returned.
        
        This is a <a href="package-summary.html#StreamOps">stateful
        intermediate operation</a>.

        Arguments
        - n: the number of leading elements to skip

        Returns
        - the new stream

        Raises
        - IllegalArgumentException: if `n` is negative

        Unknown Tags
        - While `skip()` is generally a cheap operation on sequential
        stream pipelines, it can be quite expensive on ordered parallel pipelines,
        especially for large values of `n`, since `skip(n)`
        is constrained to skip not just any *n* elements, but the
        *first n* elements in the encounter order.  Using an unordered
        stream source (such as .generate(DoubleSupplier)) or removing the
        ordering constraint with .unordered() may result in significant
        speedups of `skip()` in parallel pipelines, if the semantics of
        your situation permit.  If consistency with encounter order is required,
        and you are experiencing poor performance or memory utilization with
        `skip()` in parallel pipelines, switching to sequential execution
        with .sequential() may improve performance.
        """
        ...


    def takeWhile(self, predicate: "DoublePredicate") -> "DoubleStream":
        """
        Returns, if this stream is ordered, a stream consisting of the longest
        prefix of elements taken from this stream that match the given predicate.
        Otherwise returns, if this stream is unordered, a stream consisting of a
        subset of elements taken from this stream that match the given predicate.
        
        If this stream is ordered then the longest prefix is a contiguous
        sequence of elements of this stream that match the given predicate.  The
        first element of the sequence is the first element of this stream, and
        the element immediately following the last element of the sequence does
        not match the given predicate.
        
        If this stream is unordered, and some (but not all) elements of this
        stream match the given predicate, then the behavior of this operation is
        nondeterministic; it is free to take any subset of matching elements
        (which includes the empty set).
        
        Independent of whether this stream is ordered or unordered if all
        elements of this stream match the given predicate then this operation
        takes all elements (the result is the same as the input), or if no
        elements of the stream match the given predicate then no elements are
        taken (the result is an empty stream).
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        stateful intermediate operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to elements to determine the longest
                         prefix of elements.

        Returns
        - the new stream

        Since
        - 9

        Unknown Tags
        - The default implementation obtains the .spliterator() spliterator
        of this stream, wraps that spliterator so as to support the semantics
        of this operation on traversal, and returns a new stream associated with
        the wrapped spliterator.  The returned stream preserves the execution
        characteristics of this stream (namely parallel or sequential execution
        as per .isParallel()) but the wrapped spliterator may choose to
        not support splitting.  When the returned stream is closed, the close
        handlers for both the returned and this stream are invoked.
        - While `takeWhile()` is generally a cheap operation on sequential
        stream pipelines, it can be quite expensive on ordered parallel
        pipelines, since the operation is constrained to return not just any
        valid prefix, but the longest prefix of elements in the encounter order.
        Using an unordered stream source (such as
        .generate(DoubleSupplier)) or removing the ordering constraint
        with .unordered() may result in significant speedups of
        `takeWhile()` in parallel pipelines, if the semantics of your
        situation permit.  If consistency with encounter order is required, and
        you are experiencing poor performance or memory utilization with
        `takeWhile()` in parallel pipelines, switching to sequential
        execution with .sequential() may improve performance.
        """
        ...


    def dropWhile(self, predicate: "DoublePredicate") -> "DoubleStream":
        """
        Returns, if this stream is ordered, a stream consisting of the remaining
        elements of this stream after dropping the longest prefix of elements
        that match the given predicate.  Otherwise returns, if this stream is
        unordered, a stream consisting of the remaining elements of this stream
        after dropping a subset of elements that match the given predicate.
        
        If this stream is ordered then the longest prefix is a contiguous
        sequence of elements of this stream that match the given predicate.  The
        first element of the sequence is the first element of this stream, and
        the element immediately following the last element of the sequence does
        not match the given predicate.
        
        If this stream is unordered, and some (but not all) elements of this
        stream match the given predicate, then the behavior of this operation is
        nondeterministic; it is free to drop any subset of matching elements
        (which includes the empty set).
        
        Independent of whether this stream is ordered or unordered if all
        elements of this stream match the given predicate then this operation
        drops all elements (the result is an empty stream), or if no elements of
        the stream match the given predicate then no elements are dropped (the
        result is the same as the input).
        
        This is a <a href="package-summary.html#StreamOps">stateful
        intermediate operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to elements to determine the longest
                         prefix of elements.

        Returns
        - the new stream

        Since
        - 9

        Unknown Tags
        - The default implementation obtains the .spliterator() spliterator
        of this stream, wraps that spliterator so as to support the semantics
        of this operation on traversal, and returns a new stream associated with
        the wrapped spliterator.  The returned stream preserves the execution
        characteristics of this stream (namely parallel or sequential execution
        as per .isParallel()) but the wrapped spliterator may choose to
        not support splitting.  When the returned stream is closed, the close
        handlers for both the returned and this stream are invoked.
        - While `dropWhile()` is generally a cheap operation on sequential
        stream pipelines, it can be quite expensive on ordered parallel
        pipelines, since the operation is constrained to return not just any
        valid prefix, but the longest prefix of elements in the encounter order.
        Using an unordered stream source (such as
        .generate(DoubleSupplier)) or removing the ordering constraint
        with .unordered() may result in significant speedups of
        `dropWhile()` in parallel pipelines, if the semantics of your
        situation permit.  If consistency with encounter order is required, and
        you are experiencing poor performance or memory utilization with
        `dropWhile()` in parallel pipelines, switching to sequential
        execution with .sequential() may improve performance.
        """
        ...


    def forEach(self, action: "DoubleConsumer") -> None:
        """
        Performs an action for each element of this stream.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.
        
        For parallel stream pipelines, this operation does *not*
        guarantee to respect the encounter order of the stream, as doing so
        would sacrifice the benefit of parallelism.  For any given element, the
        action may be performed at whatever time and in whatever thread the
        library chooses.  If the action accesses shared state, it is
        responsible for providing the required synchronization.

        Arguments
        - action: a <a href="package-summary.html#NonInterference">
                      non-interfering</a> action to perform on the elements
        """
        ...


    def forEachOrdered(self, action: "DoubleConsumer") -> None:
        """
        Performs an action for each element of this stream, guaranteeing that
        each element is processed in encounter order for streams that have a
        defined encounter order.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Arguments
        - action: a <a href="package-summary.html#NonInterference">
                      non-interfering</a> action to perform on the elements

        See
        - .forEach(DoubleConsumer)
        """
        ...


    def toArray(self) -> list[float]:
        """
        Returns an array containing the elements of this stream.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - an array containing the elements of this stream
        """
        ...


    def reduce(self, identity: float, op: "DoubleBinaryOperator") -> float:
        """
        Performs a <a href="package-summary.html#Reduction">reduction</a> on the
        elements of this stream, using the provided identity value and an
        <a href="package-summary.html#Associativity">associative</a>
        accumulation function, and returns the reduced value.  This is equivalent
        to:
        ````double result = identity;
            for (double element : this stream)
                result = accumulator.applyAsDouble(result, element)
            return result;````
        
        but is not constrained to execute sequentially.
        
        The `identity` value must be an identity for the accumulator
        function. This means that for all `x`,
        `accumulator.apply(identity, x)` is equal to `x`.
        The `accumulator` function must be an
        <a href="package-summary.html#Associativity">associative</a> function.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Arguments
        - identity: the identity value for the accumulating function
        - op: an <a href="package-summary.html#Associativity">associative</a>,
                  <a href="package-summary.html#NonInterference">non-interfering</a>,
                  <a href="package-summary.html#Statelessness">stateless</a>
                  function for combining two values

        Returns
        - the result of the reduction

        See
        - .average()

        Unknown Tags
        - Sum, min, max, and average are all special cases of reduction.
        Summing a stream of numbers can be expressed as:
        
        ````double sum = numbers.reduce(0, (a, b) -> a+b);````
        
        or more compactly:
        
        ````double sum = numbers.reduce(0, Double::sum);````
        
        While this may seem a more roundabout way to perform an aggregation
        compared to simply mutating a running total in a loop, reduction
        operations parallelize more gracefully, without needing additional
        synchronization and with greatly reduced risk of data races.
        """
        ...


    def reduce(self, op: "DoubleBinaryOperator") -> "OptionalDouble":
        """
        Performs a <a href="package-summary.html#Reduction">reduction</a> on the
        elements of this stream, using an
        <a href="package-summary.html#Associativity">associative</a> accumulation
        function, and returns an `OptionalDouble` describing the reduced
        value, if any. This is equivalent to:
        ````boolean foundAny = False;
            double result = null;
            for (double element : this stream) {
                if (!foundAny) {
                    foundAny = True;
                    result = element;`
                else
                    result = accumulator.applyAsDouble(result, element);
            }
            return foundAny ? OptionalDouble.of(result) : OptionalDouble.empty();
        }```
        
        but is not constrained to execute sequentially.
        
        The `accumulator` function must be an
        <a href="package-summary.html#Associativity">associative</a> function.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Arguments
        - op: an <a href="package-summary.html#Associativity">associative</a>,
                  <a href="package-summary.html#NonInterference">non-interfering</a>,
                  <a href="package-summary.html#Statelessness">stateless</a>
                  function for combining two values

        Returns
        - the result of the reduction

        See
        - .reduce(double, DoubleBinaryOperator)
        """
        ...


    def collect(self, supplier: "Supplier"["R"], accumulator: "ObjDoubleConsumer"["R"], combiner: "BiConsumer"["R", "R"]) -> "R":
        """
        Performs a <a href="package-summary.html#MutableReduction">mutable
        reduction</a> operation on the elements of this stream.  A mutable
        reduction is one in which the reduced value is a mutable result container,
        such as an `ArrayList`, and elements are incorporated by updating
        the state of the result rather than by replacing the result.  This
        produces a result equivalent to:
        ````R result = supplier.get();
            for (double element : this stream)
                accumulator.accept(result, element);
            return result;````
        
        Like .reduce(double, DoubleBinaryOperator), `collect`
        operations can be parallelized without requiring additional
        synchronization.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.
        
        Type `<R>`: the type of the mutable result container

        Arguments
        - supplier: a function that creates a new mutable result container.
                        For a parallel execution, this function may be called
                        multiple times and must return a fresh value each time.
        - accumulator: an <a href="package-summary.html#Associativity">associative</a>,
                           <a href="package-summary.html#NonInterference">non-interfering</a>,
                           <a href="package-summary.html#Statelessness">stateless</a>
                           function that must fold an element into a result
                           container.
        - combiner: an <a href="package-summary.html#Associativity">associative</a>,
                           <a href="package-summary.html#NonInterference">non-interfering</a>,
                           <a href="package-summary.html#Statelessness">stateless</a>
                           function that accepts two partial result containers
                           and merges them, which must be compatible with the
                           accumulator function.  The combiner function must fold
                           the elements from the second result container into the
                           first result container.

        Returns
        - the result of the reduction

        See
        - Stream.collect(Supplier, BiConsumer, BiConsumer)
        """
        ...


    def sum(self) -> float:
        """
        Returns the sum of elements in this stream.
        
        Summation is a special case of a <a
        href="package-summary.html#Reduction">reduction</a>. If
        floating-point summation were exact, this method would be
        equivalent to:
        
        ````return reduce(0, Double::sum);````
        
        However, since floating-point summation is not exact, the above
        code is not necessarily equivalent to the summation computation
        done by this method.
        
        The value of a floating-point sum is a function both
        of the input values as well as the order of addition
        operations. The order of addition operations of this method is
        intentionally not defined to allow for implementation
        flexibility to improve the speed and accuracy of the computed
        result.
        
        In particular, this method may be implemented using compensated
        summation or other technique to reduce the error bound in the
        numerical sum compared to a simple summation of `double`
        values.
        
        Because of the unspecified order of operations and the
        possibility of using differing summation schemes, the output of
        this method may vary on the same input elements.
        
        Various conditions can result in a non-finite sum being
        computed. This can occur even if the all the elements
        being summed are finite. If any element is non-finite,
        the sum will be non-finite:
        
        
        
        - If any element is a NaN, then the final sum will be
        NaN.
        
        - If the elements contain one or more infinities, the
        sum will be infinite or NaN.
        
        
        
        - If the elements contain infinities of opposite sign,
        the sum will be NaN.
        
        - If the elements contain infinities of one sign and
        an intermediate sum overflows to an infinity of the opposite
        sign, the sum may be NaN.
        
        
        
        
        
        It is possible for intermediate sums of finite values to
        overflow into opposite-signed infinities; if that occurs, the
        final sum will be NaN even if the elements are all
        finite.
        
        If all the elements are zero, the sign of zero is
        *not* guaranteed to be preserved in the final sum.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - the sum of elements in this stream

        Unknown Tags
        - Elements sorted by increasing absolute magnitude tend
        to yield more accurate results.
        """
        ...


    def min(self) -> "OptionalDouble":
        """
        Returns an `OptionalDouble` describing the minimum element of this
        stream, or an empty OptionalDouble if this stream is empty.  The minimum
        element will be `Double.NaN` if any stream element was NaN. Unlike
        the numerical comparison operators, this method considers negative zero
        to be strictly smaller than positive zero. This is a special case of a
        <a href="package-summary.html#Reduction">reduction</a> and is
        equivalent to:
        ````return reduce(Double::min);````
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - an `OptionalDouble` containing the minimum element of this
        stream, or an empty optional if the stream is empty
        """
        ...


    def max(self) -> "OptionalDouble":
        """
        Returns an `OptionalDouble` describing the maximum element of this
        stream, or an empty OptionalDouble if this stream is empty.  The maximum
        element will be `Double.NaN` if any stream element was NaN. Unlike
        the numerical comparison operators, this method considers negative zero
        to be strictly smaller than positive zero. This is a
        special case of a
        <a href="package-summary.html#Reduction">reduction</a> and is
        equivalent to:
        ````return reduce(Double::max);````
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - an `OptionalDouble` containing the maximum element of this
        stream, or an empty optional if the stream is empty
        """
        ...


    def count(self) -> int:
        """
        Returns the count of elements in this stream.  This is a special case of
        a <a href="package-summary.html#Reduction">reduction</a> and is
        equivalent to:
        ````return mapToLong(e -> 1L).sum();````
        
        This is a <a href="package-summary.html#StreamOps">terminal operation</a>.

        Returns
        - the count of elements in this stream

        Unknown Tags
        - An implementation may choose to not execute the stream pipeline (either
        sequentially or in parallel) if it is capable of computing the count
        directly from the stream source.  In such cases no source elements will
        be traversed and no intermediate operations will be evaluated.
        Behavioral parameters with side-effects, which are strongly discouraged
        except for harmless cases such as debugging, may be affected.  For
        example, consider the following stream:
        ````DoubleStream s = DoubleStream.of(1, 2, 3, 4);
            long count = s.peek(System.out::println).count();````
        The number of elements covered by the stream source is known and the
        intermediate operation, `peek`, does not inject into or remove
        elements from the stream (as may be the case for `flatMap` or
        `filter` operations).  Thus the count is 4 and there is no need to
        execute the pipeline and, as a side-effect, print out the elements.
        """
        ...


    def average(self) -> "OptionalDouble":
        """
        Returns an `OptionalDouble` describing the arithmetic
        mean of elements of this stream, or an empty optional if this
        stream is empty.
        
        The computed average can vary numerically and have the
        special case behavior as computing the sum; see .sum
        for details.
        
         The average is a special case of a <a
         href="package-summary.html#Reduction">reduction</a>.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - an `OptionalDouble` containing the average element of this
        stream, or an empty optional if the stream is empty

        Unknown Tags
        - Elements sorted by increasing absolute magnitude tend
        to yield more accurate results.
        """
        ...


    def summaryStatistics(self) -> "DoubleSummaryStatistics":
        """
        Returns a `DoubleSummaryStatistics` describing various summary data
        about the elements of this stream.  This is a special
        case of a <a href="package-summary.html#Reduction">reduction</a>.
        
        This is a <a href="package-summary.html#StreamOps">terminal
        operation</a>.

        Returns
        - a `DoubleSummaryStatistics` describing various summary data
        about the elements of this stream
        """
        ...


    def anyMatch(self, predicate: "DoublePredicate") -> bool:
        """
        Returns whether any elements of this stream match the provided
        predicate.  May not evaluate the predicate on all elements if not
        necessary for determining the result.  If the stream is empty then
        `False` is returned and the predicate is not evaluated.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        terminal operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to elements of this stream

        Returns
        - `True` if any elements of the stream match the provided
        predicate, otherwise `False`

        Unknown Tags
        - This method evaluates the *existential quantification* of the
        predicate over the elements of the stream (for some x P(x)).
        """
        ...


    def allMatch(self, predicate: "DoublePredicate") -> bool:
        """
        Returns whether all elements of this stream match the provided predicate.
        May not evaluate the predicate on all elements if not necessary for
        determining the result.  If the stream is empty then `True` is
        returned and the predicate is not evaluated.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        terminal operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to elements of this stream

        Returns
        - `True` if either all elements of the stream match the
        provided predicate or the stream is empty, otherwise `False`

        Unknown Tags
        - This method evaluates the *universal quantification* of the
        predicate over the elements of the stream (for all x P(x)).  If the
        stream is empty, the quantification is said to be *vacuously
        satisfied* and is always `True` (regardless of P(x)).
        """
        ...


    def noneMatch(self, predicate: "DoublePredicate") -> bool:
        """
        Returns whether no elements of this stream match the provided predicate.
        May not evaluate the predicate on all elements if not necessary for
        determining the result.  If the stream is empty then `True` is
        returned and the predicate is not evaluated.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        terminal operation</a>.

        Arguments
        - predicate: a <a href="package-summary.html#NonInterference">non-interfering</a>,
                         <a href="package-summary.html#Statelessness">stateless</a>
                         predicate to apply to elements of this stream

        Returns
        - `True` if either no elements of the stream match the
        provided predicate or the stream is empty, otherwise `False`

        Unknown Tags
        - This method evaluates the *universal quantification* of the
        negated predicate over the elements of the stream (for all x ~P(x)).  If
        the stream is empty, the quantification is said to be vacuously satisfied
        and is always `True`, regardless of P(x).
        """
        ...


    def findFirst(self) -> "OptionalDouble":
        """
        Returns an OptionalDouble describing the first element of this
        stream, or an empty `OptionalDouble` if the stream is empty.  If
        the stream has no encounter order, then any element may be returned.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        terminal operation</a>.

        Returns
        - an `OptionalDouble` describing the first element of this
        stream, or an empty `OptionalDouble` if the stream is empty
        """
        ...


    def findAny(self) -> "OptionalDouble":
        """
        Returns an OptionalDouble describing some element of the stream,
        or an empty `OptionalDouble` if the stream is empty.
        
        This is a <a href="package-summary.html#StreamOps">short-circuiting
        terminal operation</a>.
        
        The behavior of this operation is explicitly nondeterministic; it is
        free to select any element in the stream.  This is to allow for maximal
        performance in parallel operations; the cost is that multiple invocations
        on the same source may not return the same result.  (If a stable result
        is desired, use .findFirst() instead.)

        Returns
        - an `OptionalDouble` describing some element of this stream,
        or an empty `OptionalDouble` if the stream is empty

        See
        - .findFirst()
        """
        ...


    def boxed(self) -> "Stream"["Double"]:
        """
        Returns a `Stream` consisting of the elements of this stream,
        boxed to `Double`.
        
        This is an <a href="package-summary.html#StreamOps">intermediate
        operation</a>.

        Returns
        - a `Stream` consistent of the elements of this stream,
        each boxed to a `Double`
        """
        ...


    def sequential(self) -> "DoubleStream":
        ...


    def parallel(self) -> "DoubleStream":
        ...


    def iterator(self) -> "PrimitiveIterator.OfDouble":
        ...


    def spliterator(self) -> "Spliterator.OfDouble":
        ...


    @staticmethod
    def builder() -> "Builder":
        """
        Returns a builder for a `DoubleStream`.

        Returns
        - a stream builder
        """
        ...


    @staticmethod
    def empty() -> "DoubleStream":
        """
        Returns an empty sequential `DoubleStream`.

        Returns
        - an empty sequential stream
        """
        ...


    @staticmethod
    def of(t: float) -> "DoubleStream":
        """
        Returns a sequential `DoubleStream` containing a single element.

        Arguments
        - t: the single element

        Returns
        - a singleton sequential stream
        """
        ...


    @staticmethod
    def of(*values: Tuple[float, ...]) -> "DoubleStream":
        """
        Returns a sequential ordered stream whose elements are the specified values.

        Arguments
        - values: the elements of the new stream

        Returns
        - the new stream
        """
        ...


    @staticmethod
    def iterate(seed: float, f: "DoubleUnaryOperator") -> "DoubleStream":
        """
        Returns an infinite sequential ordered `DoubleStream` produced by iterative
        application of a function `f` to an initial element `seed`,
        producing a `Stream` consisting of `seed`, `f(seed)`,
        `f(f(seed))`, etc.
        
        The first element (position `0`) in the `DoubleStream`
        will be the provided `seed`.  For `n > 0`, the element at
        position `n`, will be the result of applying the function `f`
         to the element at position `n - 1`.
        
        The action of applying `f` for one element
        <a href="../concurrent/package-summary.html#MemoryVisibility">*happens-before*</a>
        the action of applying `f` for subsequent elements.  For any given
        element the action may be performed in whatever thread the library
        chooses.

        Arguments
        - seed: the initial element
        - f: a function to be applied to the previous element to produce
                 a new element

        Returns
        - a new sequential `DoubleStream`
        """
        ...


    @staticmethod
    def iterate(seed: float, hasNext: "DoublePredicate", next: "DoubleUnaryOperator") -> "DoubleStream":
        """
        Returns a sequential ordered `DoubleStream` produced by iterative
        application of the given `next` function to an initial element,
        conditioned on satisfying the given `hasNext` predicate.  The
        stream terminates as soon as the `hasNext` predicate returns False.
        
        `DoubleStream.iterate` should produce the same sequence of elements as
        produced by the corresponding for-loop:
        ````for (double index=seed; hasNext.test(index); index = next.applyAsDouble(index)) {
                ...`
        }```
        
        The resulting sequence may be empty if the `hasNext` predicate
        does not hold on the seed value.  Otherwise the first element will be the
        supplied `seed` value, the next element (if present) will be the
        result of applying the `next` function to the `seed` value,
        and so on iteratively until the `hasNext` predicate indicates that
        the stream should terminate.
        
        The action of applying the `hasNext` predicate to an element
        <a href="../concurrent/package-summary.html#MemoryVisibility">*happens-before*</a>
        the action of applying the `next` function to that element.  The
        action of applying the `next` function for one element
        *happens-before* the action of applying the `hasNext`
        predicate for subsequent elements.  For any given element an action may
        be performed in whatever thread the library chooses.

        Arguments
        - seed: the initial element
        - hasNext: a predicate to apply to elements to determine when the
                       stream must terminate.
        - next: a function to be applied to the previous element to produce
                    a new element

        Returns
        - a new sequential `DoubleStream`

        Since
        - 9
        """
        ...


    @staticmethod
    def generate(s: "DoubleSupplier") -> "DoubleStream":
        """
        Returns an infinite sequential unordered stream where each element is
        generated by the provided `DoubleSupplier`.  This is suitable for
        generating constant streams, streams of random elements, etc.

        Arguments
        - s: the `DoubleSupplier` for generated elements

        Returns
        - a new infinite sequential unordered `DoubleStream`
        """
        ...


    @staticmethod
    def concat(a: "DoubleStream", b: "DoubleStream") -> "DoubleStream":
        """
        Creates a lazily concatenated stream whose elements are all the
        elements of the first stream followed by all the elements of the
        second stream.  The resulting stream is ordered if both
        of the input streams are ordered, and parallel if either of the input
        streams is parallel.  When the resulting stream is closed, the close
        handlers for both input streams are invoked.
        
        This method operates on the two input streams and binds each stream
        to its source.  As a result subsequent modifications to an input stream
        source may not be reflected in the concatenated stream result.

        Arguments
        - a: the first stream
        - b: the second stream

        Returns
        - the concatenation of the two input streams

        Unknown Tags
        - Use caution when constructing streams from repeated concatenation.
        Accessing an element of a deeply concatenated stream can result in deep
        call chains, or even `StackOverflowError`.
        - To preserve optimization opportunities this method binds each stream to
        its source and accepts only two streams as parameters.  For example, the
        exact size of the concatenated stream source can be computed if the exact
        size of each input stream source is known.
        To concatenate more streams without binding, or without nested calls to
        this method, try creating a stream of streams and flat-mapping with the
        identity function, for example:
        ````DoubleStream concat = Stream.of(s1, s2, s3, s4).flatMapToDouble(s -> s);````
        """
        ...


    class Builder(DoubleConsumer):
        """
        A mutable builder for a `DoubleStream`.
        
        A stream builder has a lifecycle, which starts in a building
        phase, during which elements can be added, and then transitions to a built
        phase, after which elements may not be added.  The built phase
        begins when the .build() method is called, which creates an
        ordered stream whose elements are the elements that were added to the
        stream builder, in the order they were added.

        See
        - DoubleStream.builder()

        Since
        - 1.8
        """

        def accept(self, t: float) -> None:
            """
            Adds an element to the stream being built.

            Raises
            - IllegalStateException: if the builder has already transitioned
            to the built state
            """
            ...


        def add(self, t: float) -> "Builder":
            """
            Adds an element to the stream being built.

            Arguments
            - t: the element to add

            Returns
            - `this` builder

            Raises
            - IllegalStateException: if the builder has already transitioned
            to the built state

            Unknown Tags
            - The default implementation behaves as if:
            ````accept(t)
                return this;````
            """
            ...


        def build(self) -> "DoubleStream":
            """
            Builds the stream, transitioning this builder to the built state.
            An `IllegalStateException` is thrown if there are further
            attempts to operate on the builder after it has entered the built
            state.

            Returns
            - the built stream

            Raises
            - IllegalStateException: if the builder has already transitioned
            to the built state
            """
            ...
