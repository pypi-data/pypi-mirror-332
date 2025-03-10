"""
Python module generated from Java source file com.google.common.math.StatsAccumulator

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.math import *
from java.util import Iterator
from java.util.stream import DoubleStream
from java.util.stream import IntStream
from java.util.stream import LongStream
from typing import Any, Callable, Iterable, Tuple


class StatsAccumulator:
    """
    A mutable object which accumulates double values and tracks some basic statistics over all the
    values added so far. The values may be added singly or in groups. This class is not thread safe.

    Author(s)
    - Kevin Bourrillion

    Since
    - 20.0
    """

    def add(self, value: float) -> None:
        """
        Adds the given value to the dataset.
        """
        ...


    def addAll(self, values: Iterable["Number"]) -> None:
        """
        Adds the given values to the dataset.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)
        """
        ...


    def addAll(self, values: Iterator["Number"]) -> None:
        """
        Adds the given values to the dataset.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)
        """
        ...


    def addAll(self, *values: Tuple[float, ...]) -> None:
        """
        Adds the given values to the dataset.

        Arguments
        - values: a series of values
        """
        ...


    def addAll(self, *values: Tuple[int, ...]) -> None:
        """
        Adds the given values to the dataset.

        Arguments
        - values: a series of values
        """
        ...


    def addAll(self, *values: Tuple[int, ...]) -> None:
        """
        Adds the given values to the dataset.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision for longs of magnitude over 2^53 (slightly over 9e15))
        """
        ...


    def addAll(self, values: "DoubleStream") -> None:
        """
        Adds the given values to the dataset. The stream will be completely consumed by this method.

        Arguments
        - values: a series of values

        Since
        - 28.2
        """
        ...


    def addAll(self, values: "IntStream") -> None:
        """
        Adds the given values to the dataset. The stream will be completely consumed by this method.

        Arguments
        - values: a series of values

        Since
        - 28.2
        """
        ...


    def addAll(self, values: "LongStream") -> None:
        """
        Adds the given values to the dataset. The stream will be completely consumed by this method.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision for longs of magnitude over 2^53 (slightly over 9e15))

        Since
        - 28.2
        """
        ...


    def addAll(self, values: "Stats") -> None:
        """
        Adds the given statistics to the dataset, as if the individual values used to compute the
        statistics had been added directly.
        """
        ...


    def addAll(self, values: "StatsAccumulator") -> None:
        """
        Adds the given statistics to the dataset, as if the individual values used to compute the
        statistics had been added directly.

        Since
        - 28.2
        """
        ...


    def snapshot(self) -> "Stats":
        """
        Returns an immutable snapshot of the current statistics.
        """
        ...


    def count(self) -> int:
        """
        Returns the number of values.
        """
        ...


    def mean(self) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains both Double.POSITIVE_INFINITY and Double.NEGATIVE_INFINITY then the
        result is Double.NaN. If it contains Double.POSITIVE_INFINITY and finite values
        only or Double.POSITIVE_INFINITY only, the result is Double.POSITIVE_INFINITY.
        If it contains Double.NEGATIVE_INFINITY and finite values only or Double.NEGATIVE_INFINITY only, the result is Double.NEGATIVE_INFINITY.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def sum(self) -> float:
        """
        Returns the sum of the values.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains both Double.POSITIVE_INFINITY and Double.NEGATIVE_INFINITY then the
        result is Double.NaN. If it contains Double.POSITIVE_INFINITY and finite values
        only or Double.POSITIVE_INFINITY only, the result is Double.POSITIVE_INFINITY.
        If it contains Double.NEGATIVE_INFINITY and finite values only or Double.NEGATIVE_INFINITY only, the result is Double.NEGATIVE_INFINITY.
        """
        ...


    def populationVariance(self) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Variance#Population_variance">population
        variance</a> of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains only exactly one finite value. It
        is not guaranteed to return zero when the dataset consists of the same value multiple times,
        due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def populationStandardDeviation(self) -> float:
        """
        Returns the <a
        href="http://en.wikipedia.org/wiki/Standard_deviation#Definition_of_population_values">
        population standard deviation</a> of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains only exactly one finite value. It
        is not guaranteed to return zero when the dataset consists of the same value multiple times,
        due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def sampleVariance(self) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Variance#Sample_variance">unbiased sample
        variance</a> of the values. If this dataset is a sample drawn from a population, this is an
        unbiased estimator of the population variance of the population. The count must be greater than
        one.
        
        This is not guaranteed to return zero when the dataset consists of the same value multiple
        times, due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single value
        """
        ...


    def sampleStandardDeviation(self) -> float:
        """
        Returns the <a
        href="http://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation">
        corrected sample standard deviation</a> of the values. If this dataset is a sample drawn from a
        population, this is an estimator of the population standard deviation of the population which
        is less biased than .populationStandardDeviation() (the unbiased estimator depends on
        the distribution). The count must be greater than one.
        
        This is not guaranteed to return zero when the dataset consists of the same value multiple
        times, due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single value
        """
        ...


    def min(self) -> float:
        """
        Returns the lowest value in the dataset. The count must be non-zero.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains Double.NEGATIVE_INFINITY and not Double.NaN then the result is Double.NEGATIVE_INFINITY. If it contains Double.POSITIVE_INFINITY and finite values
        only then the result is the lowest finite value. If it contains Double.POSITIVE_INFINITY only then the result is Double.POSITIVE_INFINITY.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def max(self) -> float:
        """
        Returns the highest value in the dataset. The count must be non-zero.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains Double.POSITIVE_INFINITY and not Double.NaN then the result is Double.POSITIVE_INFINITY. If it contains Double.NEGATIVE_INFINITY and finite values
        only then the result is the highest finite value. If it contains Double.NEGATIVE_INFINITY only then the result is Double.NEGATIVE_INFINITY.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...
