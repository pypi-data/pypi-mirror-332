"""
Python module generated from Java source file java.util.stream.Collector

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from java.util import EnumSet
from java.util import Objects
from java.util.function import BiConsumer
from java.util.function import BinaryOperator
from java.util.function import Function
from java.util.function import Supplier
from java.util.stream import *
from typing import Any, Callable, Iterable, Tuple


class Collector:
    """
    A <a href="package-summary.html#Reduction">mutable reduction operation</a> that
    accumulates input elements into a mutable result container, optionally transforming
    the accumulated result into a final representation after all input elements
    have been processed.  Reduction operations can be performed either sequentially
    or in parallel.
    
    Examples of mutable reduction operations include:
    accumulating elements into a `Collection`; concatenating
    strings using a `StringBuilder`; computing summary information about
    elements such as sum, min, max, or average; computing "pivot table" summaries
    such as "maximum valued transaction by seller", etc.  The class Collectors
    provides implementations of many common mutable reductions.
    
    A `Collector` is specified by four functions that work together to
    accumulate entries into a mutable result container, and optionally perform
    a final transform on the result.  They are: 
        - creation of a new result container (.supplier())
        - incorporating a new data element into a result container (.accumulator())
        - combining two result containers into one (.combiner())
        - performing an optional final transform on the container (.finisher())
    
    
    Collectors also have a set of characteristics, such as
    Characteristics.CONCURRENT, that provide hints that can be used by a
    reduction implementation to provide better performance.
    
    A sequential implementation of a reduction using a collector would
    create a single result container using the supplier function, and invoke the
    accumulator function once for each input element.  A parallel implementation
    would partition the input, create a result container for each partition,
    accumulate the contents of each partition into a subresult for that partition,
    and then use the combiner function to merge the subresults into a combined
    result.
    
    To ensure that sequential and parallel executions produce equivalent
    results, the collector functions must satisfy an *identity* and an
    <a href="package-summary.html#Associativity">associativity</a> constraints.
    
    The identity constraint says that for any partially accumulated result,
    combining it with an empty result container must produce an equivalent
    result.  That is, for a partially accumulated result `a` that is the
    result of any series of accumulator and combiner invocations, `a` must
    be equivalent to `combiner.apply(a, supplier.get())`.
    
    The associativity constraint says that splitting the computation must
    produce an equivalent result.  That is, for any input elements `t1`
    and `t2`, the results `r1` and `r2` in the computation
    below must be equivalent:
    ````A a1 = supplier.get();
        accumulator.accept(a1, t1);
        accumulator.accept(a1, t2);
        R r1 = finisher.apply(a1);  // result without splitting
    
        A a2 = supplier.get();
        accumulator.accept(a2, t1);
        A a3 = supplier.get();
        accumulator.accept(a3, t2);
        R r2 = finisher.apply(combiner.apply(a2, a3));  // result with splitting` ```
    
    For collectors that do not have the `UNORDERED` characteristic,
    two accumulated results `a1` and `a2` are equivalent if
    `finisher.apply(a1).equals(finisher.apply(a2))`.  For unordered
    collectors, equivalence is relaxed to allow for non-equality related to
    differences in order.  (For example, an unordered collector that accumulated
    elements to a `List` would consider two lists equivalent if they
    contained the same elements, ignoring order.)
    
    Libraries that implement reduction based on `Collector`, such as
    Stream.collect(Collector), must adhere to the following constraints:
    
        - The first argument passed to the accumulator function, both
        arguments passed to the combiner function, and the argument passed to the
        finisher function must be the result of a previous invocation of the
        result supplier, accumulator, or combiner functions.
        - The implementation should not do anything with the result of any of
        the result supplier, accumulator, or combiner functions other than to
        pass them again to the accumulator, combiner, or finisher functions,
        or return them to the caller of the reduction operation.
        - If a result is passed to the combiner or finisher
        function, and the same object is not returned from that function, it is
        never used again.
        - Once a result is passed to the combiner or finisher function, it
        is never passed to the accumulator function again.
        - For non-concurrent collectors, any result returned from the result
        supplier, accumulator, or combiner functions must be serially
        thread-confined.  This enables collection to occur in parallel without
        the `Collector` needing to implement any additional synchronization.
        The reduction implementation must manage that the input is properly
        partitioned, that partitions are processed in isolation, and combining
        happens only after accumulation is complete.
        - For concurrent collectors, an implementation is free to (but not
        required to) implement reduction concurrently.  A concurrent reduction
        is one where the accumulator function is called concurrently from
        multiple threads, using the same concurrently-modifiable result container,
        rather than keeping the result isolated during accumulation.
        A concurrent reduction should only be applied if the collector has the
        Characteristics.UNORDERED characteristics or if the
        originating data is unordered.
    
    
    In addition to the predefined implementations in Collectors, the
    static factory methods .of(Supplier, BiConsumer, BinaryOperator, Characteristics...)
    can be used to construct collectors.  For example, you could create a collector
    that accumulates widgets into a `TreeSet` with:
    
    ````Collector<Widget, ?, TreeSet<Widget>> intoSet =
            Collector.of(TreeSet::new, TreeSet::add,
                         (left, right) -> { left.addAll(right); return left;`);
    }```
    
    (This behavior is also implemented by the predefined collector
    Collectors.toCollection(Supplier)).
    
    Type `<T>`: the type of input elements to the reduction operation
    
    Type `<A>`: the mutable accumulation type of the reduction operation (often
               hidden as an implementation detail)
    
    Type `<R>`: the result type of the reduction operation

    See
    - Collectors

    Since
    - 1.8

    Unknown Tags
    - Performing a reduction operation with a `Collector` should produce a
    result equivalent to:
    ````A container = collector.supplier().get();
        for (T t : data)
            collector.accumulator().accept(container, t);
        return collector.finisher().apply(container);````
    
    However, the library is free to partition the input, perform the reduction
    on the partitions, and then use the combiner function to combine the partial
    results to achieve a parallel reduction.  (Depending on the specific reduction
    operation, this may perform better or worse, depending on the relative cost
    of the accumulator and combiner functions.)
    
    Collectors are designed to be *composed*; many of the methods
    in Collectors are functions that take a collector and produce
    a new collector.  For example, given the following collector that computes
    the sum of the salaries of a stream of employees:
    
    ````Collector<Employee, ?, Integer> summingSalaries
            = Collectors.summingInt(Employee::getSalary))````
    
    If we wanted to create a collector to tabulate the sum of salaries by
    department, we could reuse the "sum of salaries" logic using
    Collectors.groupingBy(Function, Collector):
    
    ````Collector<Employee, ?, Map<Department, Integer>> summingSalariesByDept
            = Collectors.groupingBy(Employee::getDepartment, summingSalaries);````
    """

    def supplier(self) -> "Supplier"["A"]:
        """
        A function that creates and returns a new mutable result container.

        Returns
        - a function which returns a new, mutable result container
        """
        ...


    def accumulator(self) -> "BiConsumer"["A", "T"]:
        """
        A function that folds a value into a mutable result container.

        Returns
        - a function which folds a value into a mutable result container
        """
        ...


    def combiner(self) -> "BinaryOperator"["A"]:
        """
        A function that accepts two partial results and merges them.  The
        combiner function may fold state from one argument into the other and
        return that, or may return a new result container.

        Returns
        - a function which combines two partial results into a combined
        result
        """
        ...


    def finisher(self) -> "Function"["A", "R"]:
        """
        Perform the final transformation from the intermediate accumulation type
        `A` to the final result type `R`.
        
        If the characteristic `IDENTITY_FINISH` is
        set, this function may be presumed to be an identity transform with an
        unchecked cast from `A` to `R`.

        Returns
        - a function which transforms the intermediate result to the final
        result
        """
        ...


    def characteristics(self) -> set["Characteristics"]:
        """
        Returns a `Set` of `Collector.Characteristics` indicating
        the characteristics of this Collector.  This set should be immutable.

        Returns
        - an immutable set of collector characteristics
        """
        ...


    @staticmethod
    def of(supplier: "Supplier"["R"], accumulator: "BiConsumer"["R", "T"], combiner: "BinaryOperator"["R"], *characteristics: Tuple["Characteristics", ...]) -> "Collector"["T", "R", "R"]:
        """
        Returns a new `Collector` described by the given `supplier`,
        `accumulator`, and `combiner` functions.  The resulting
        `Collector` has the `Collector.Characteristics.IDENTITY_FINISH`
        characteristic.
        
        Type `<T>`: The type of input elements for the new collector
        
        Type `<R>`: The type of intermediate accumulation result, and final result,
                  for the new collector

        Arguments
        - supplier: The supplier function for the new collector
        - accumulator: The accumulator function for the new collector
        - combiner: The combiner function for the new collector
        - characteristics: The collector characteristics for the new
                               collector

        Returns
        - the new `Collector`

        Raises
        - NullPointerException: if any argument is null
        """
        ...


    @staticmethod
    def of(supplier: "Supplier"["A"], accumulator: "BiConsumer"["A", "T"], combiner: "BinaryOperator"["A"], finisher: "Function"["A", "R"], *characteristics: Tuple["Characteristics", ...]) -> "Collector"["T", "A", "R"]:
        """
        Returns a new `Collector` described by the given `supplier`,
        `accumulator`, `combiner`, and `finisher` functions.
        
        Type `<T>`: The type of input elements for the new collector
        
        Type `<A>`: The intermediate accumulation type of the new collector
        
        Type `<R>`: The final result type of the new collector

        Arguments
        - supplier: The supplier function for the new collector
        - accumulator: The accumulator function for the new collector
        - combiner: The combiner function for the new collector
        - finisher: The finisher function for the new collector
        - characteristics: The collector characteristics for the new
                               collector

        Returns
        - the new `Collector`

        Raises
        - NullPointerException: if any argument is null
        """
        ...
