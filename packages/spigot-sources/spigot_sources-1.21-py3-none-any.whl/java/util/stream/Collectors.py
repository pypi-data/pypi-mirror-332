"""
Python module generated from Java source file java.util.stream.Collectors

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractSet
from java.util import Collections
from java.util import Comparator
from java.util import DoubleSummaryStatistics
from java.util import EnumSet
from java.util import IntSummaryStatistics
from java.util import Iterator
from java.util import LongSummaryStatistics
from java.util import Objects
from java.util import Optional
from java.util import StringJoiner
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import BinaryOperator
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import Predicate
from java.util.function import Supplier
from java.util.function import ToDoubleFunction
from java.util.function import ToIntFunction
from java.util.function import ToLongFunction
from java.util.stream import *
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class Collectors:
    """
    Implementations of Collector that implement various useful reduction
    operations, such as accumulating elements into collections, summarizing
    elements according to various criteria, etc.
    
    The following are examples of using the predefined collectors to perform
    common mutable reduction tasks:
    
    ````// Accumulate names into a List
    List<String> list = people.stream()
      .map(Person::getName)
      .collect(Collectors.toList());
    
    // Accumulate names into a TreeSet
    Set<String> set = people.stream()
      .map(Person::getName)
      .collect(Collectors.toCollection(TreeSet::new));
    
    // Convert elements to strings and concatenate them, separated by commas
    String joined = things.stream()
      .map(Object::toString)
      .collect(Collectors.joining(", "));
    
    // Compute sum of salaries of employee
    int total = employees.stream()
      .collect(Collectors.summingInt(Employee::getSalary));
    
    // Group employees by department
    Map<Department, List<Employee>> byDept = employees.stream()
      .collect(Collectors.groupingBy(Employee::getDepartment));
    
    // Compute sum of salaries by department
    Map<Department, Integer> totalByDept = employees.stream()
      .collect(Collectors.groupingBy(Employee::getDepartment,
                                     Collectors.summingInt(Employee::getSalary)));
    
    // Partition students into passing and failing
    Map<Boolean, List<Student>> passingFailing = students.stream()
      .collect(Collectors.partitioningBy(s -> s.getGrade() >= PASS_THRESHOLD));````

    Since
    - 1.8
    """

    @staticmethod
    def toCollection(collectionFactory: "Supplier"["C"]) -> "Collector"["T", Any, "C"]:
        """
        Returns a `Collector` that accumulates the input elements into a
        new `Collection`, in encounter order.  The `Collection` is
        created by the provided factory.
        
        Type `<T>`: the type of the input elements
        
        Type `<C>`: the type of the resulting `Collection`

        Arguments
        - collectionFactory: a supplier providing a new empty `Collection`
                                 into which the results will be inserted

        Returns
        - a `Collector` which collects all the input elements into a
        `Collection`, in encounter order
        """
        ...


    @staticmethod
    def toList() -> "Collector"["T", Any, list["T"]]:
        """
        Returns a `Collector` that accumulates the input elements into a
        new `List`. There are no guarantees on the type, mutability,
        serializability, or thread-safety of the `List` returned; if more
        control over the returned `List` is required, use .toCollection(Supplier).
        
        Type `<T>`: the type of the input elements

        Returns
        - a `Collector` which collects all the input elements into a
        `List`, in encounter order
        """
        ...


    @staticmethod
    def toUnmodifiableList() -> "Collector"["T", Any, list["T"]]:
        """
        Returns a `Collector` that accumulates the input elements into an
        <a href="../List.html#unmodifiable">unmodifiable List</a> in encounter
        order. The returned Collector disallows null values and will throw
        `NullPointerException` if it is presented with a null value.
        
        Type `<T>`: the type of the input elements

        Returns
        - a `Collector` that accumulates the input elements into an
        <a href="../List.html#unmodifiable">unmodifiable List</a> in encounter order

        Since
        - 10
        """
        ...


    @staticmethod
    def toSet() -> "Collector"["T", Any, set["T"]]:
        """
        Returns a `Collector` that accumulates the input elements into a
        new `Set`. There are no guarantees on the type, mutability,
        serializability, or thread-safety of the `Set` returned; if more
        control over the returned `Set` is required, use
        .toCollection(Supplier).
        
        This is an Collector.Characteristics.UNORDERED unordered
        Collector.
        
        Type `<T>`: the type of the input elements

        Returns
        - a `Collector` which collects all the input elements into a
        `Set`
        """
        ...


    @staticmethod
    def toUnmodifiableSet() -> "Collector"["T", Any, set["T"]]:
        """
        Returns a `Collector` that accumulates the input elements into an
        <a href="../Set.html#unmodifiable">unmodifiable Set</a>. The returned
        Collector disallows null values and will throw `NullPointerException`
        if it is presented with a null value. If the input contains duplicate elements,
        an arbitrary element of the duplicates is preserved.
        
        This is an Collector.Characteristics.UNORDERED unordered
        Collector.
        
        Type `<T>`: the type of the input elements

        Returns
        - a `Collector` that accumulates the input elements into an
        <a href="../Set.html#unmodifiable">unmodifiable Set</a>

        Since
        - 10
        """
        ...


    @staticmethod
    def joining() -> "Collector"["CharSequence", Any, str]:
        """
        Returns a `Collector` that concatenates the input elements into a
        `String`, in encounter order.

        Returns
        - a `Collector` that concatenates the input elements into a
        `String`, in encounter order
        """
        ...


    @staticmethod
    def joining(delimiter: "CharSequence") -> "Collector"["CharSequence", Any, str]:
        """
        Returns a `Collector` that concatenates the input elements,
        separated by the specified delimiter, in encounter order.

        Arguments
        - delimiter: the delimiter to be used between each element

        Returns
        - A `Collector` which concatenates CharSequence elements,
        separated by the specified delimiter, in encounter order
        """
        ...


    @staticmethod
    def joining(delimiter: "CharSequence", prefix: "CharSequence", suffix: "CharSequence") -> "Collector"["CharSequence", Any, str]:
        """
        Returns a `Collector` that concatenates the input elements,
        separated by the specified delimiter, with the specified prefix and
        suffix, in encounter order.

        Arguments
        - delimiter: the delimiter to be used between each element
        - prefix: the sequence of characters to be used at the beginning
                       of the joined result
        - suffix: the sequence of characters to be used at the end
                       of the joined result

        Returns
        - A `Collector` which concatenates CharSequence elements,
        separated by the specified delimiter, in encounter order
        """
        ...


    @staticmethod
    def mapping(mapper: "Function"["T", "U"], downstream: "Collector"["U", "A", "R"]) -> "Collector"["T", Any, "R"]:
        """
        Adapts a `Collector` accepting elements of type `U` to one
        accepting elements of type `T` by applying a mapping function to
        each input element before accumulation.
        
        Type `<T>`: the type of the input elements
        
        Type `<U>`: type of elements accepted by downstream collector
        
        Type `<A>`: intermediate accumulation type of the downstream collector
        
        Type `<R>`: result type of collector

        Arguments
        - mapper: a function to be applied to the input elements
        - downstream: a collector which will accept mapped values

        Returns
        - a collector which applies the mapping function to the input
        elements and provides the mapped results to the downstream collector

        Unknown Tags
        - The `mapping()` collectors are most useful when used in a
        multi-level reduction, such as downstream of a `groupingBy` or
        `partitioningBy`.  For example, given a stream of
        `Person`, to accumulate the set of last names in each city:
        ````Map<City, Set<String>> lastNamesByCity
          = people.stream().collect(
            groupingBy(Person::getCity,
                       mapping(Person::getLastName,
                               toSet())));````
        """
        ...


    @staticmethod
    def flatMapping(mapper: "Function"["T", "Stream"["U"]], downstream: "Collector"["U", "A", "R"]) -> "Collector"["T", Any, "R"]:
        """
        Adapts a `Collector` accepting elements of type `U` to one
        accepting elements of type `T` by applying a flat mapping function
        to each input element before accumulation.  The flat mapping function
        maps an input element to a Stream stream covering zero or more
        output elements that are then accumulated downstream.  Each mapped stream
        is java.util.stream.BaseStream.close() closed after its contents
        have been placed downstream.  (If a mapped stream is `null`
        an empty stream is used, instead.)
        
        Type `<T>`: the type of the input elements
        
        Type `<U>`: type of elements accepted by downstream collector
        
        Type `<A>`: intermediate accumulation type of the downstream collector
        
        Type `<R>`: result type of collector

        Arguments
        - mapper: a function to be applied to the input elements, which
        returns a stream of results
        - downstream: a collector which will receive the elements of the
        stream returned by mapper

        Returns
        - a collector which applies the mapping function to the input
        elements and provides the flat mapped results to the downstream collector

        Since
        - 9

        Unknown Tags
        - The `flatMapping()` collectors are most useful when used in a
        multi-level reduction, such as downstream of a `groupingBy` or
        `partitioningBy`.  For example, given a stream of
        `Order`, to accumulate the set of line items for each customer:
        ````Map<String, Set<LineItem>> itemsByCustomerName
          = orders.stream().collect(
            groupingBy(Order::getCustomerName,
                       flatMapping(order -> order.getLineItems().stream(),
                                   toSet())));````
        """
        ...


    @staticmethod
    def filtering(predicate: "Predicate"["T"], downstream: "Collector"["T", "A", "R"]) -> "Collector"["T", Any, "R"]:
        """
        Adapts a `Collector` to one accepting elements of the same type
        `T` by applying the predicate to each input element and only
        accumulating if the predicate returns `True`.
        
        Type `<T>`: the type of the input elements
        
        Type `<A>`: intermediate accumulation type of the downstream collector
        
        Type `<R>`: result type of collector

        Arguments
        - predicate: a predicate to be applied to the input elements
        - downstream: a collector which will accept values that match the
        predicate

        Returns
        - a collector which applies the predicate to the input elements
        and provides matching elements to the downstream collector

        Since
        - 9

        Unknown Tags
        - The `filtering()` collectors are most useful when used in a
        multi-level reduction, such as downstream of a `groupingBy` or
        `partitioningBy`.  For example, given a stream of
        `Employee`, to accumulate the employees in each department that have a
        salary above a certain threshold:
        ````Map<Department, Set<Employee>> wellPaidEmployeesByDepartment
          = employees.stream().collect(
            groupingBy(Employee::getDepartment,
                       filtering(e -> e.getSalary() > 2000,
                                 toSet())));````
        A filtering collector differs from a stream's `filter()` operation.
        In this example, suppose there are no employees whose salary is above the
        threshold in some department.  Using a filtering collector as shown above
        would result in a mapping from that department to an empty `Set`.
        If a stream `filter()` operation were done instead, there would be
        no mapping for that department at all.
        """
        ...


    @staticmethod
    def collectingAndThen(downstream: "Collector"["T", "A", "R"], finisher: "Function"["R", "RR"]) -> "Collector"["T", "A", "RR"]:
        """
        Adapts a `Collector` to perform an additional finishing
        transformation.  For example, one could adapt the .toList()
        collector to always produce an immutable list with:
        ````List<String> list = people.stream().collect(
          collectingAndThen(toList(),
                            Collections::unmodifiableList));````
        
        Type `<T>`: the type of the input elements
        
        Type `<A>`: intermediate accumulation type of the downstream collector
        
        Type `<R>`: result type of the downstream collector

        Arguments
        - <RR>: result type of the resulting collector
        - downstream: a collector
        - finisher: a function to be applied to the final result of the downstream collector

        Returns
        - a collector which performs the action of the downstream collector,
        followed by an additional finishing step
        """
        ...


    @staticmethod
    def counting() -> "Collector"["T", Any, "Long"]:
        """
        Returns a `Collector` accepting elements of type `T` that
        counts the number of input elements.  If no elements are present, the
        result is 0.
        
        Type `<T>`: the type of the input elements

        Returns
        - a `Collector` that counts the input elements

        Unknown Tags
        - This produces a result equivalent to:
        ````reducing(0L, e -> 1L, Long::sum)````
        """
        ...


    @staticmethod
    def minBy(comparator: "Comparator"["T"]) -> "Collector"["T", Any, "Optional"["T"]]:
        """
        Returns a `Collector` that produces the minimal element according
        to a given `Comparator`, described as an `Optional<T>`.
        
        Type `<T>`: the type of the input elements

        Arguments
        - comparator: a `Comparator` for comparing elements

        Returns
        - a `Collector` that produces the minimal value

        Unknown Tags
        - This produces a result equivalent to:
        ````reducing(BinaryOperator.minBy(comparator))````
        """
        ...


    @staticmethod
    def maxBy(comparator: "Comparator"["T"]) -> "Collector"["T", Any, "Optional"["T"]]:
        """
        Returns a `Collector` that produces the maximal element according
        to a given `Comparator`, described as an `Optional<T>`.
        
        Type `<T>`: the type of the input elements

        Arguments
        - comparator: a `Comparator` for comparing elements

        Returns
        - a `Collector` that produces the maximal value

        Unknown Tags
        - This produces a result equivalent to:
        ````reducing(BinaryOperator.maxBy(comparator))````
        """
        ...


    @staticmethod
    def summingInt(mapper: "ToIntFunction"["T"]) -> "Collector"["T", Any, "Integer"]:
        """
        Returns a `Collector` that produces the sum of a integer-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be summed

        Returns
        - a `Collector` that produces the sum of a derived property
        """
        ...


    @staticmethod
    def summingLong(mapper: "ToLongFunction"["T"]) -> "Collector"["T", Any, "Long"]:
        """
        Returns a `Collector` that produces the sum of a long-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be summed

        Returns
        - a `Collector` that produces the sum of a derived property
        """
        ...


    @staticmethod
    def summingDouble(mapper: "ToDoubleFunction"["T"]) -> "Collector"["T", Any, "Double"]:
        """
        Returns a `Collector` that produces the sum of a double-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        The sum returned can vary depending upon the order in which
        values are recorded, due to accumulated rounding error in
        addition of values of differing magnitudes. Values sorted by increasing
        absolute magnitude tend to yield more accurate results.  If any recorded
        value is a `NaN` or the sum is at any point a `NaN` then the
        sum will be `NaN`.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be summed

        Returns
        - a `Collector` that produces the sum of a derived property
        """
        ...


    @staticmethod
    def averagingInt(mapper: "ToIntFunction"["T"]) -> "Collector"["T", Any, "Double"]:
        """
        Returns a `Collector` that produces the arithmetic mean of an integer-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be averaged

        Returns
        - a `Collector` that produces the arithmetic mean of a
        derived property
        """
        ...


    @staticmethod
    def averagingLong(mapper: "ToLongFunction"["T"]) -> "Collector"["T", Any, "Double"]:
        """
        Returns a `Collector` that produces the arithmetic mean of a long-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be averaged

        Returns
        - a `Collector` that produces the arithmetic mean of a
        derived property
        """
        ...


    @staticmethod
    def averagingDouble(mapper: "ToDoubleFunction"["T"]) -> "Collector"["T", Any, "Double"]:
        """
        Returns a `Collector` that produces the arithmetic mean of a double-valued
        function applied to the input elements.  If no elements are present,
        the result is 0.
        
        The average returned can vary depending upon the order in which
        values are recorded, due to accumulated rounding error in
        addition of values of differing magnitudes. Values sorted by increasing
        absolute magnitude tend to yield more accurate results.  If any recorded
        value is a `NaN` or the sum is at any point a `NaN` then the
        average will be `NaN`.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a function extracting the property to be averaged

        Returns
        - a `Collector` that produces the arithmetic mean of a
        derived property

        Unknown Tags
        - The `double` format can represent all
        consecutive integers in the range -2<sup>53</sup> to
        2<sup>53</sup>. If the pipeline has more than 2<sup>53</sup>
        values, the divisor in the average computation will saturate at
        2<sup>53</sup>, leading to additional numerical errors.
        """
        ...


    @staticmethod
    def reducing(identity: "T", op: "BinaryOperator"["T"]) -> "Collector"["T", Any, "T"]:
        """
        Returns a `Collector` which performs a reduction of its
        input elements under a specified `BinaryOperator` using the
        provided identity.
        
        Type `<T>`: element type for the input and output of the reduction

        Arguments
        - identity: the identity value for the reduction (also, the value
                        that is returned when there are no input elements)
        - op: a `BinaryOperator<T>` used to reduce the input elements

        Returns
        - a `Collector` which implements the reduction operation

        See
        - .reducing(Object, Function, BinaryOperator)

        Unknown Tags
        - The `reducing()` collectors are most useful when used in a
        multi-level reduction, downstream of `groupingBy` or
        `partitioningBy`.  To perform a simple reduction on a stream,
        use Stream.reduce(Object, BinaryOperator)} instead.
        """
        ...


    @staticmethod
    def reducing(op: "BinaryOperator"["T"]) -> "Collector"["T", Any, "Optional"["T"]]:
        """
        Returns a `Collector` which performs a reduction of its
        input elements under a specified `BinaryOperator`.  The result
        is described as an `Optional<T>`.
        
        Type `<T>`: element type for the input and output of the reduction

        Arguments
        - op: a `BinaryOperator<T>` used to reduce the input elements

        Returns
        - a `Collector` which implements the reduction operation

        See
        - .reducing(Object, Function, BinaryOperator)

        Unknown Tags
        - The `reducing()` collectors are most useful when used in a
        multi-level reduction, downstream of `groupingBy` or
        `partitioningBy`.  To perform a simple reduction on a stream,
        use Stream.reduce(BinaryOperator) instead.
        
        For example, given a stream of `Person`, to calculate tallest
        person in each city:
        ````Comparator<Person> byHeight = Comparator.comparing(Person::getHeight);
        Map<City, Optional<Person>> tallestByCity
          = people.stream().collect(
            groupingBy(Person::getCity,
                       reducing(BinaryOperator.maxBy(byHeight))));````
        """
        ...


    @staticmethod
    def reducing(identity: "U", mapper: "Function"["T", "U"], op: "BinaryOperator"["U"]) -> "Collector"["T", Any, "U"]:
        """
        Returns a `Collector` which performs a reduction of its
        input elements under a specified mapping function and
        `BinaryOperator`. This is a generalization of
        .reducing(Object, BinaryOperator) which allows a transformation
        of the elements before reduction.
        
        Type `<T>`: the type of the input elements
        
        Type `<U>`: the type of the mapped values

        Arguments
        - identity: the identity value for the reduction (also, the value
                        that is returned when there are no input elements)
        - mapper: a mapping function to apply to each input value
        - op: a `BinaryOperator<U>` used to reduce the mapped values

        Returns
        - a `Collector` implementing the map-reduce operation

        See
        - .reducing(BinaryOperator)

        Unknown Tags
        - The `reducing()` collectors are most useful when used in a
        multi-level reduction, downstream of `groupingBy` or
        `partitioningBy`.  To perform a simple map-reduce on a stream,
        use Stream.map(Function) and Stream.reduce(Object, BinaryOperator)
        instead.
        
        For example, given a stream of `Person`, to calculate the longest
        last name of residents in each city:
        ````Comparator<String> byLength = Comparator.comparing(String::length);
        Map<City, String> longestLastNameByCity
          = people.stream().collect(
            groupingBy(Person::getCity,
                       reducing("",
                                Person::getLastName,
                                BinaryOperator.maxBy(byLength))));````
        """
        ...


    @staticmethod
    def groupingBy(classifier: "Function"["T", "K"]) -> "Collector"["T", Any, dict["K", list["T"]]]:
        """
        Returns a `Collector` implementing a "group by" operation on
        input elements of type `T`, grouping elements according to a
        classification function, and returning the results in a `Map`.
        
        The classification function maps elements to some key type `K`.
        The collector produces a `Map<K, List<T>>` whose keys are the
        values resulting from applying the classification function to the input
        elements, and whose corresponding values are `List`s containing the
        input elements which map to the associated key under the classification
        function.
        
        There are no guarantees on the type, mutability, serializability, or
        thread-safety of the `Map` or `List` objects returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys

        Arguments
        - classifier: the classifier function mapping input elements to keys

        Returns
        - a `Collector` implementing the group-by operation

        See
        - .groupingByConcurrent(Function)

        Unknown Tags
        - This produces a result similar to:
        ````groupingBy(classifier, toList());````
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If
        preservation of the order in which elements appear in the resulting `Map`
        collector is not required, using .groupingByConcurrent(Function)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def groupingBy(classifier: "Function"["T", "K"], downstream: "Collector"["T", "A", "D"]) -> "Collector"["T", Any, dict["K", "D"]]:
        """
        Returns a `Collector` implementing a cascaded "group by" operation
        on input elements of type `T`, grouping elements according to a
        classification function, and then performing a reduction operation on
        the values associated with a given key using the specified downstream
        `Collector`.
        
        The classification function maps elements to some key type `K`.
        The downstream collector operates on elements of type `T` and
        produces a result of type `D`. The resulting collector produces a
        `Map<K, D>`.
        
        There are no guarantees on the type, mutability,
        serializability, or thread-safety of the `Map` returned.
        
        For example, to compute the set of last names of people in each city:
        ````Map<City, Set<String>> namesByCity
          = people.stream().collect(
            groupingBy(Person::getCity,
                       mapping(Person::getLastName,
                               toSet())));````
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys
        
        Type `<A>`: the intermediate accumulation type of the downstream collector
        
        Type `<D>`: the result type of the downstream reduction

        Arguments
        - classifier: a classifier function mapping input elements to keys
        - downstream: a `Collector` implementing the downstream reduction

        Returns
        - a `Collector` implementing the cascaded group-by operation

        See
        - .groupingByConcurrent(Function, Collector)

        Unknown Tags
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If
        preservation of the order in which elements are presented to the downstream
        collector is not required, using .groupingByConcurrent(Function, Collector)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def groupingBy(classifier: "Function"["T", "K"], mapFactory: "Supplier"["M"], downstream: "Collector"["T", "A", "D"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a `Collector` implementing a cascaded "group by" operation
        on input elements of type `T`, grouping elements according to a
        classification function, and then performing a reduction operation on
        the values associated with a given key using the specified downstream
        `Collector`.  The `Map` produced by the Collector is created
        with the supplied factory function.
        
        The classification function maps elements to some key type `K`.
        The downstream collector operates on elements of type `T` and
        produces a result of type `D`. The resulting collector produces a
        `Map<K, D>`.
        
        For example, to compute the set of last names of people in each city,
        where the city names are sorted:
        ````Map<City, Set<String>> namesByCity
          = people.stream().collect(
            groupingBy(Person::getCity,
                       TreeMap::new,
                       mapping(Person::getLastName,
                               toSet())));````
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys
        
        Type `<A>`: the intermediate accumulation type of the downstream collector
        
        Type `<D>`: the result type of the downstream reduction
        
        Type `<M>`: the type of the resulting `Map`

        Arguments
        - classifier: a classifier function mapping input elements to keys
        - downstream: a `Collector` implementing the downstream reduction
        - mapFactory: a supplier providing a new empty `Map`
                          into which the results will be inserted

        Returns
        - a `Collector` implementing the cascaded group-by operation

        See
        - .groupingByConcurrent(Function, Supplier, Collector)

        Unknown Tags
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If
        preservation of the order in which elements are presented to the downstream
        collector is not required, using .groupingByConcurrent(Function, Supplier, Collector)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def groupingByConcurrent(classifier: "Function"["T", "K"]) -> "Collector"["T", Any, "ConcurrentMap"["K", list["T"]]]:
        """
        Returns a concurrent `Collector` implementing a "group by"
        operation on input elements of type `T`, grouping elements
        according to a classification function.
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        
        The classification function maps elements to some key type `K`.
        The collector produces a `ConcurrentMap<K, List<T>>` whose keys are the
        values resulting from applying the classification function to the input
        elements, and whose corresponding values are `List`s containing the
        input elements which map to the associated key under the classification
        function.
        
        There are no guarantees on the type, mutability, or serializability
        of the `ConcurrentMap` or `List` objects returned, or of the
        thread-safety of the `List` objects returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys

        Arguments
        - classifier: a classifier function mapping input elements to keys

        Returns
        - a concurrent, unordered `Collector` implementing the group-by operation

        See
        - .groupingByConcurrent(Function, Supplier, Collector)

        Unknown Tags
        - This produces a result similar to:
        ````groupingByConcurrent(classifier, toList());````
        """
        ...


    @staticmethod
    def groupingByConcurrent(classifier: "Function"["T", "K"], downstream: "Collector"["T", "A", "D"]) -> "Collector"["T", Any, "ConcurrentMap"["K", "D"]]:
        """
        Returns a concurrent `Collector` implementing a cascaded "group by"
        operation on input elements of type `T`, grouping elements
        according to a classification function, and then performing a reduction
        operation on the values associated with a given key using the specified
        downstream `Collector`.
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        
        The classification function maps elements to some key type `K`.
        The downstream collector operates on elements of type `T` and
        produces a result of type `D`. The resulting collector produces a
        `ConcurrentMap<K, D>`.
        
        There are no guarantees on the type, mutability, or serializability
        of the `ConcurrentMap` returned.
        
        For example, to compute the set of last names of people in each city,
        where the city names are sorted:
        ````ConcurrentMap<City, Set<String>> namesByCity
          = people.stream().collect(
            groupingByConcurrent(Person::getCity,
                                 mapping(Person::getLastName,
                                         toSet())));````
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys
        
        Type `<A>`: the intermediate accumulation type of the downstream collector
        
        Type `<D>`: the result type of the downstream reduction

        Arguments
        - classifier: a classifier function mapping input elements to keys
        - downstream: a `Collector` implementing the downstream reduction

        Returns
        - a concurrent, unordered `Collector` implementing the cascaded group-by operation

        See
        - .groupingByConcurrent(Function, Supplier, Collector)
        """
        ...


    @staticmethod
    def groupingByConcurrent(classifier: "Function"["T", "K"], mapFactory: "Supplier"["M"], downstream: "Collector"["T", "A", "D"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a concurrent `Collector` implementing a cascaded "group by"
        operation on input elements of type `T`, grouping elements
        according to a classification function, and then performing a reduction
        operation on the values associated with a given key using the specified
        downstream `Collector`.  The `ConcurrentMap` produced by the
        Collector is created with the supplied factory function.
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        
        The classification function maps elements to some key type `K`.
        The downstream collector operates on elements of type `T` and
        produces a result of type `D`. The resulting collector produces a
        `ConcurrentMap<K, D>`.
        
        For example, to compute the set of last names of people in each city,
        where the city names are sorted:
        ````ConcurrentMap<City, Set<String>> namesByCity
          = people.stream().collect(
            groupingByConcurrent(Person::getCity,
                                 ConcurrentSkipListMap::new,
                                 mapping(Person::getLastName,
                                         toSet())));````
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the type of the keys
        
        Type `<A>`: the intermediate accumulation type of the downstream collector
        
        Type `<D>`: the result type of the downstream reduction
        
        Type `<M>`: the type of the resulting `ConcurrentMap`

        Arguments
        - classifier: a classifier function mapping input elements to keys
        - downstream: a `Collector` implementing the downstream reduction
        - mapFactory: a supplier providing a new empty `ConcurrentMap`
                          into which the results will be inserted

        Returns
        - a concurrent, unordered `Collector` implementing the cascaded group-by operation

        See
        - .groupingBy(Function, Supplier, Collector)
        """
        ...


    @staticmethod
    def partitioningBy(predicate: "Predicate"["T"]) -> "Collector"["T", Any, dict["Boolean", list["T"]]]:
        """
        Returns a `Collector` which partitions the input elements according
        to a `Predicate`, and organizes them into a
        `Map<Boolean, List<T>>`.
        
        The returned `Map` always contains mappings for both
        `False` and `True` keys.
        There are no guarantees on the type, mutability,
        serializability, or thread-safety of the `Map` or `List`
        returned.
        
        Type `<T>`: the type of the input elements

        Arguments
        - predicate: a predicate used for classifying input elements

        Returns
        - a `Collector` implementing the partitioning operation

        See
        - .partitioningBy(Predicate, Collector)

        Unknown Tags
        - If a partition has no elements, its value in the result Map will be
        an empty List.
        """
        ...


    @staticmethod
    def partitioningBy(predicate: "Predicate"["T"], downstream: "Collector"["T", "A", "D"]) -> "Collector"["T", Any, dict["Boolean", "D"]]:
        """
        Returns a `Collector` which partitions the input elements according
        to a `Predicate`, reduces the values in each partition according to
        another `Collector`, and organizes them into a
        `Map<Boolean, D>` whose values are the result of the downstream
        reduction.
        
        
        The returned `Map` always contains mappings for both
        `False` and `True` keys.
        There are no guarantees on the type, mutability,
        serializability, or thread-safety of the `Map` returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<A>`: the intermediate accumulation type of the downstream collector
        
        Type `<D>`: the result type of the downstream reduction

        Arguments
        - predicate: a predicate used for classifying input elements
        - downstream: a `Collector` implementing the downstream
                          reduction

        Returns
        - a `Collector` implementing the cascaded partitioning
                operation

        See
        - .partitioningBy(Predicate)

        Unknown Tags
        - If a partition has no elements, its value in the result Map will be
        obtained by calling the downstream collector's supplier function and then
        applying the finisher function.
        """
        ...


    @staticmethod
    def toMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"]) -> "Collector"["T", Any, dict["K", "U"]]:
        """
        Returns a `Collector` that accumulates elements into a
        `Map` whose keys and values are the result of applying the provided
        mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to
        Object.equals(Object)), an `IllegalStateException` is
        thrown when the collection operation is performed.  If the mapped keys
        might have duplicates, use .toMap(Function, Function, BinaryOperator)
        instead.
        
        There are no guarantees on the type, mutability, serializability,
        or thread-safety of the `Map` returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: a mapping function to produce keys
        - valueMapper: a mapping function to produce values

        Returns
        - a `Collector` which collects elements into a `Map`
        whose keys and values are the result of applying mapping functions to
        the input elements

        See
        - .toConcurrentMap(Function, Function)

        Unknown Tags
        - It is common for either the key or the value to be the input elements.
        In this case, the utility method
        java.util.function.Function.identity() may be helpful.
        For example, the following produces a `Map` mapping
        students to their grade point average:
        ````Map<Student, Double> studentToGPA
          = students.stream().collect(
            toMap(Function.identity(),
                  student -> computeGPA(student)));````
        And the following produces a `Map` mapping a unique identifier to
        students:
        ````Map<String, Student> studentIdToStudent
          = students.stream().collect(
            toMap(Student::getId,
                  Function.identity()));````
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If it is
        not required that results are inserted into the `Map` in encounter
        order, using .toConcurrentMap(Function, Function)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def toUnmodifiableMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"]) -> "Collector"["T", Any, dict["K", "U"]]:
        """
        Returns a `Collector` that accumulates the input elements into an
        <a href="../Map.html#unmodifiable">unmodifiable Map</a>,
        whose keys and values are the result of applying the provided
        mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to
        Object.equals(Object)), an `IllegalStateException` is
        thrown when the collection operation is performed.  If the mapped keys
        might have duplicates, use .toUnmodifiableMap(Function, Function, BinaryOperator)
        to handle merging of the values.
        
        The returned Collector disallows null keys and values. If either mapping function
        returns null, `NullPointerException` will be thrown.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: a mapping function to produce keys, must be non-null
        - valueMapper: a mapping function to produce values, must be non-null

        Returns
        - a `Collector` that accumulates the input elements into an
        <a href="../Map.html#unmodifiable">unmodifiable Map</a>, whose keys and values
        are the result of applying the provided mapping functions to the input elements

        Raises
        - NullPointerException: if either keyMapper or valueMapper is null

        See
        - .toUnmodifiableMap(Function, Function, BinaryOperator)

        Since
        - 10
        """
        ...


    @staticmethod
    def toMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"], mergeFunction: "BinaryOperator"["U"]) -> "Collector"["T", Any, dict["K", "U"]]:
        """
        Returns a `Collector` that accumulates elements into a
        `Map` whose keys and values are the result of applying the provided
        mapping functions to the input elements.
        
        If the mapped
        keys contain duplicates (according to Object.equals(Object)),
        the value mapping function is applied to each equal element, and the
        results are merged using the provided merging function.
        
        There are no guarantees on the type, mutability, serializability,
        or thread-safety of the `Map` returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: a mapping function to produce keys
        - valueMapper: a mapping function to produce values
        - mergeFunction: a merge function, used to resolve collisions between
                             values associated with the same key, as supplied
                             to Map.merge(Object, Object, BiFunction)

        Returns
        - a `Collector` which collects elements into a `Map`
        whose keys are the result of applying a key mapping function to the input
        elements, and whose values are the result of applying a value mapping
        function to all input elements equal to the key and combining them
        using the merge function

        See
        - .toConcurrentMap(Function, Function, BinaryOperator)

        Unknown Tags
        - There are multiple ways to deal with collisions between multiple elements
        mapping to the same key.  The other forms of `toMap` simply use
        a merge function that throws unconditionally, but you can easily write
        more flexible merge policies.  For example, if you have a stream
        of `Person`, and you want to produce a "phone book" mapping name to
        address, but it is possible that two persons have the same name, you can
        do as follows to gracefully deal with these collisions, and produce a
        `Map` mapping names to a concatenated list of addresses:
        ````Map<String, String> phoneBook
          = people.stream().collect(
            toMap(Person::getName,
                  Person::getAddress,
                  (s, a) -> s + ", " + a));````
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If it is
        not required that results are merged into the `Map` in encounter
        order, using .toConcurrentMap(Function, Function, BinaryOperator)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def toUnmodifiableMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"], mergeFunction: "BinaryOperator"["U"]) -> "Collector"["T", Any, dict["K", "U"]]:
        """
        Returns a `Collector` that accumulates the input elements into an
        <a href="../Map.html#unmodifiable">unmodifiable Map</a>,
        whose keys and values are the result of applying the provided
        mapping functions to the input elements.
        
        If the mapped
        keys contain duplicates (according to Object.equals(Object)),
        the value mapping function is applied to each equal element, and the
        results are merged using the provided merging function.
        
        The returned Collector disallows null keys and values. If either mapping function
        returns null, `NullPointerException` will be thrown.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: a mapping function to produce keys, must be non-null
        - valueMapper: a mapping function to produce values, must be non-null
        - mergeFunction: a merge function, used to resolve collisions between
                             values associated with the same key, as supplied
                             to Map.merge(Object, Object, BiFunction),
                             must be non-null

        Returns
        - a `Collector` that accumulates the input elements into an
        <a href="../Map.html#unmodifiable">unmodifiable Map</a>, whose keys and values
        are the result of applying the provided mapping functions to the input elements

        Raises
        - NullPointerException: if the keyMapper, valueMapper, or mergeFunction is null

        See
        - .toUnmodifiableMap(Function, Function)

        Since
        - 10
        """
        ...


    @staticmethod
    def toMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"], mergeFunction: "BinaryOperator"["U"], mapFactory: "Supplier"["M"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a `Collector` that accumulates elements into a
        `Map` whose keys and values are the result of applying the provided
        mapping functions to the input elements.
        
        If the mapped
        keys contain duplicates (according to Object.equals(Object)),
        the value mapping function is applied to each equal element, and the
        results are merged using the provided merging function.  The `Map`
        is created by a provided supplier function.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function
        
        Type `<M>`: the type of the resulting `Map`

        Arguments
        - keyMapper: a mapping function to produce keys
        - valueMapper: a mapping function to produce values
        - mergeFunction: a merge function, used to resolve collisions between
                             values associated with the same key, as supplied
                             to Map.merge(Object, Object, BiFunction)
        - mapFactory: a supplier providing a new empty `Map`
                          into which the results will be inserted

        Returns
        - a `Collector` which collects elements into a `Map`
        whose keys are the result of applying a key mapping function to the input
        elements, and whose values are the result of applying a value mapping
        function to all input elements equal to the key and combining them
        using the merge function

        See
        - .toConcurrentMap(Function, Function, BinaryOperator, Supplier)

        Unknown Tags
        - The returned `Collector` is not concurrent.  For parallel stream
        pipelines, the `combiner` function operates by merging the keys
        from one map into another, which can be an expensive operation.  If it is
        not required that results are merged into the `Map` in encounter
        order, using .toConcurrentMap(Function, Function, BinaryOperator, Supplier)
        may offer better parallel performance.
        """
        ...


    @staticmethod
    def toConcurrentMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"]) -> "Collector"["T", Any, "ConcurrentMap"["K", "U"]]:
        """
        Returns a concurrent `Collector` that accumulates elements into a
        `ConcurrentMap` whose keys and values are the result of applying
        the provided mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to
        Object.equals(Object)), an `IllegalStateException` is
        thrown when the collection operation is performed.  If the mapped keys
        may have duplicates, use
        .toConcurrentMap(Function, Function, BinaryOperator) instead.
        
        There are no guarantees on the type, mutability, or serializability
        of the `ConcurrentMap` returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: the mapping function to produce keys
        - valueMapper: the mapping function to produce values

        Returns
        - a concurrent, unordered `Collector` which collects elements into a
        `ConcurrentMap` whose keys are the result of applying a key mapping
        function to the input elements, and whose values are the result of
        applying a value mapping function to the input elements

        See
        - .toConcurrentMap(Function, Function, BinaryOperator, Supplier)

        Unknown Tags
        - It is common for either the key or the value to be the input elements.
        In this case, the utility method
        java.util.function.Function.identity() may be helpful.
        For example, the following produces a `ConcurrentMap` mapping
        students to their grade point average:
        ````ConcurrentMap<Student, Double> studentToGPA
          = students.stream().collect(
            toConcurrentMap(Function.identity(),
                            student -> computeGPA(student)));````
        And the following produces a `ConcurrentMap` mapping a
        unique identifier to students:
        ````ConcurrentMap<String, Student> studentIdToStudent
          = students.stream().collect(
            toConcurrentMap(Student::getId,
                            Function.identity()));````
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        """
        ...


    @staticmethod
    def toConcurrentMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"], mergeFunction: "BinaryOperator"["U"]) -> "Collector"["T", Any, "ConcurrentMap"["K", "U"]]:
        """
        Returns a concurrent `Collector` that accumulates elements into a
        `ConcurrentMap` whose keys and values are the result of applying
        the provided mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to Object.equals(Object)),
        the value mapping function is applied to each equal element, and the
        results are merged using the provided merging function.
        
        There are no guarantees on the type, mutability, or serializability
        of the `ConcurrentMap` returned.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function

        Arguments
        - keyMapper: a mapping function to produce keys
        - valueMapper: a mapping function to produce values
        - mergeFunction: a merge function, used to resolve collisions between
                             values associated with the same key, as supplied
                             to Map.merge(Object, Object, BiFunction)

        Returns
        - a concurrent, unordered `Collector` which collects elements into a
        `ConcurrentMap` whose keys are the result of applying a key mapping
        function to the input elements, and whose values are the result of
        applying a value mapping function to all input elements equal to the key
        and combining them using the merge function

        See
        - .toMap(Function, Function, BinaryOperator)

        Unknown Tags
        - There are multiple ways to deal with collisions between multiple elements
        mapping to the same key.  The other forms of `toConcurrentMap` simply use
        a merge function that throws unconditionally, but you can easily write
        more flexible merge policies.  For example, if you have a stream
        of `Person`, and you want to produce a "phone book" mapping name to
        address, but it is possible that two persons have the same name, you can
        do as follows to gracefully deal with these collisions, and produce a
        `ConcurrentMap` mapping names to a concatenated list of addresses:
        ````ConcurrentMap<String, String> phoneBook
          = people.stream().collect(
            toConcurrentMap(Person::getName,
                            Person::getAddress,
                            (s, a) -> s + ", " + a));````
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        """
        ...


    @staticmethod
    def toConcurrentMap(keyMapper: "Function"["T", "K"], valueMapper: "Function"["T", "U"], mergeFunction: "BinaryOperator"["U"], mapFactory: "Supplier"["M"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a concurrent `Collector` that accumulates elements into a
        `ConcurrentMap` whose keys and values are the result of applying
        the provided mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to Object.equals(Object)),
        the value mapping function is applied to each equal element, and the
        results are merged using the provided merging function.  The
        `ConcurrentMap` is created by a provided supplier function.
        
        This is a Collector.Characteristics.CONCURRENT concurrent and
        Collector.Characteristics.UNORDERED unordered Collector.
        
        Type `<T>`: the type of the input elements
        
        Type `<K>`: the output type of the key mapping function
        
        Type `<U>`: the output type of the value mapping function
        
        Type `<M>`: the type of the resulting `ConcurrentMap`

        Arguments
        - keyMapper: a mapping function to produce keys
        - valueMapper: a mapping function to produce values
        - mergeFunction: a merge function, used to resolve collisions between
                             values associated with the same key, as supplied
                             to Map.merge(Object, Object, BiFunction)
        - mapFactory: a supplier providing a new empty `ConcurrentMap`
                          into which the results will be inserted

        Returns
        - a concurrent, unordered `Collector` which collects elements into a
        `ConcurrentMap` whose keys are the result of applying a key mapping
        function to the input elements, and whose values are the result of
        applying a value mapping function to all input elements equal to the key
        and combining them using the merge function

        See
        - .toMap(Function, Function, BinaryOperator, Supplier)
        """
        ...


    @staticmethod
    def summarizingInt(mapper: "ToIntFunction"["T"]) -> "Collector"["T", Any, "IntSummaryStatistics"]:
        """
        Returns a `Collector` which applies an `int`-producing
        mapping function to each input element, and returns summary statistics
        for the resulting values.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a mapping function to apply to each element

        Returns
        - a `Collector` implementing the summary-statistics reduction

        See
        - .summarizingLong(ToLongFunction)
        """
        ...


    @staticmethod
    def summarizingLong(mapper: "ToLongFunction"["T"]) -> "Collector"["T", Any, "LongSummaryStatistics"]:
        """
        Returns a `Collector` which applies an `long`-producing
        mapping function to each input element, and returns summary statistics
        for the resulting values.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: the mapping function to apply to each element

        Returns
        - a `Collector` implementing the summary-statistics reduction

        See
        - .summarizingInt(ToIntFunction)
        """
        ...


    @staticmethod
    def summarizingDouble(mapper: "ToDoubleFunction"["T"]) -> "Collector"["T", Any, "DoubleSummaryStatistics"]:
        """
        Returns a `Collector` which applies an `double`-producing
        mapping function to each input element, and returns summary statistics
        for the resulting values.
        
        Type `<T>`: the type of the input elements

        Arguments
        - mapper: a mapping function to apply to each element

        Returns
        - a `Collector` implementing the summary-statistics reduction

        See
        - .summarizingInt(ToIntFunction)
        """
        ...


    @staticmethod
    def teeing(downstream1: "Collector"["T", Any, "R1"], downstream2: "Collector"["T", Any, "R2"], merger: "BiFunction"["R1", "R2", "R"]) -> "Collector"["T", Any, "R"]:
        """
        Returns a `Collector` that is a composite of two downstream collectors.
        Every element passed to the resulting collector is processed by both downstream
        collectors, then their results are merged using the specified merge function
        into the final result.
        
        The resulting collector functions do the following:
        
        
        - supplier: creates a result container that contains result containers
        obtained by calling each collector's supplier
        - accumulator: calls each collector's accumulator with its result container
        and the input element
        - combiner: calls each collector's combiner with two result containers
        - finisher: calls each collector's finisher with its result container,
        then calls the supplied merger and returns its result.
        
        
        The resulting collector is Collector.Characteristics.UNORDERED if both downstream
        collectors are unordered and Collector.Characteristics.CONCURRENT if both downstream
        collectors are concurrent.
        
        Type `<T>`: the type of the input elements
        
        Type `<R>`: the final result type

        Arguments
        - <R1>: the result type of the first collector
        - <R2>: the result type of the second collector
        - downstream1: the first downstream collector
        - downstream2: the second downstream collector
        - merger: the function which merges two results into the single one

        Returns
        - a `Collector` which aggregates the results of two supplied collectors.

        Since
        - 12
        """
        ...
