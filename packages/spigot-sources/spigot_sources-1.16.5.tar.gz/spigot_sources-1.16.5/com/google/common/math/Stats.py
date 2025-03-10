"""
Python module generated from Java source file com.google.common.math.Stats

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import MoreObjects
from com.google.common.base import Objects
from com.google.common.math import *
from java.io import Serializable
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Stats(Serializable):
    """
    A bundle of statistical summary values -- sum, count, mean/average, min and max, and several
    forms of variance -- that were computed from a single set of zero or more floating-point values.
    
    There are two ways to obtain a `Stats` instance:
    
    
    - If all the values you want to summarize are already known, use the appropriate `Stats.of` factory method below. Primitive arrays, iterables and iterators of any kind of
        `Number`, and primitive varargs are supported.
    - Or, to avoid storing up all the data first, create a StatsAccumulator instance, feed
        values to it as you get them, then call StatsAccumulator.snapshot.
    
    
    Static convenience methods called `meanOf` are also provided for users who wish to
    calculate *only* the mean.
    
    **Java 8 users:** If you are not using any of the variance statistics, you may wish to use
    built-in JDK libraries instead of this class.

    Author(s)
    - Kevin Bourrillion

    Since
    - 20.0
    """

    @staticmethod
    def of(values: Iterable["Number"]) -> "Stats":
        """
        Returns statistics over a dataset containing the given values.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)
        """
        ...


    @staticmethod
    def of(values: Iterator["Number"]) -> "Stats":
        """
        Returns statistics over a dataset containing the given values.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)
        """
        ...


    @staticmethod
    def of(*values: Tuple[float, ...]) -> "Stats":
        """
        Returns statistics over a dataset containing the given values.

        Arguments
        - values: a series of values
        """
        ...


    @staticmethod
    def of(*values: Tuple[int, ...]) -> "Stats":
        """
        Returns statistics over a dataset containing the given values.

        Arguments
        - values: a series of values
        """
        ...


    @staticmethod
    def of(*values: Tuple[int, ...]) -> "Stats":
        """
        Returns statistics over a dataset containing the given values.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision for longs of magnitude over 2^53 (slightly over 9e15))
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
        If it contains Double.NEGATIVE_INFINITY and finite values only or
        Double.NEGATIVE_INFINITY only, the result is Double.NEGATIVE_INFINITY.
        
        If you only want to calculate the mean, use {#meanOf} instead of creating a Stats
        instance.

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
        If it contains Double.NEGATIVE_INFINITY and finite values only or
        Double.NEGATIVE_INFINITY only, the result is Double.NEGATIVE_INFINITY.
        """
        ...


    def populationVariance(self) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Variance#Population_variance">population
        variance</a> of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains only exactly one finite value.
        It is not guaranteed to return zero when the dataset consists of the same value multiple times,
        due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def populationStandardDeviation(self) -> float:
        """
        Returns the
        <a href="http://en.wikipedia.org/wiki/Standard_deviation#Definition_of_population_values">
        population standard deviation</a> of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains only exactly one finite value.
        It is not guaranteed to return zero when the dataset consists of the same value multiple times,
        due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

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
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single value
        """
        ...


    def sampleStandardDeviation(self) -> float:
        """
        Returns the
        <a href="http://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation">
        corrected sample standard deviation</a> of the values. If this dataset is a sample drawn from a
        population, this is an estimator of the population standard deviation of the population which
        is less biased than .populationStandardDeviation() (the unbiased estimator depends on
        the distribution). The count must be greater than one.
        
        This is not guaranteed to return zero when the dataset consists of the same value multiple
        times, due to numerical errors. However, it is guaranteed never to return a negative result.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single value
        """
        ...


    def min(self) -> float:
        """
        Returns the lowest value in the dataset. The count must be non-zero.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains Double.NEGATIVE_INFINITY and not Double.NaN then the result is
        Double.NEGATIVE_INFINITY. If it contains Double.POSITIVE_INFINITY and finite
        values only then the result is the lowest finite value. If it contains
        Double.POSITIVE_INFINITY only then the result is Double.POSITIVE_INFINITY.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def max(self) -> float:
        """
        Returns the highest value in the dataset. The count must be non-zero.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains Double.NaN then the result is Double.NaN. If it
        contains Double.POSITIVE_INFINITY and not Double.NaN then the result is
        Double.POSITIVE_INFINITY. If it contains Double.NEGATIVE_INFINITY and finite
        values only then the result is the highest finite value. If it contains
        Double.NEGATIVE_INFINITY only then the result is Double.NEGATIVE_INFINITY.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        
        
        **Note:** This tests exact equality of the calculated statistics, including the floating
        point values. It is definitely True for instances constructed from exactly the same values in
        the same order. It is also True for an instance round-tripped through java serialization.
        However, floating point rounding errors mean that it may be False for some instances where the
        statistics are mathematically equal, including the same values in a different order.
        """
        ...


    def hashCode(self) -> int:
        """
        
        
        **Note:** This hash code is consistent with exact equality of the calculated statistics,
        including the floating point values. See the note on .equals for details.
        """
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def meanOf(values: Iterable["Number"]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        The definition of the mean is the same as Stats.mean.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)

        Raises
        - IllegalArgumentException: if the dataset is empty
        """
        ...


    @staticmethod
    def meanOf(values: Iterator["Number"]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        The definition of the mean is the same as Stats.mean.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision)

        Raises
        - IllegalArgumentException: if the dataset is empty
        """
        ...


    @staticmethod
    def meanOf(*values: Tuple[float, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        The definition of the mean is the same as Stats.mean.

        Arguments
        - values: a series of values

        Raises
        - IllegalArgumentException: if the dataset is empty
        """
        ...


    @staticmethod
    def meanOf(*values: Tuple[int, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        The definition of the mean is the same as Stats.mean.

        Arguments
        - values: a series of values

        Raises
        - IllegalArgumentException: if the dataset is empty
        """
        ...


    @staticmethod
    def meanOf(*values: Tuple[int, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of the
        values. The count must be non-zero.
        
        The definition of the mean is the same as Stats.mean.

        Arguments
        - values: a series of values, which will be converted to `double` values (this may
            cause loss of precision for longs of magnitude over 2^53 (slightly over 9e15))

        Raises
        - IllegalArgumentException: if the dataset is empty
        """
        ...


    def toByteArray(self) -> list[int]:
        """
        Gets a byte array representation of this instance.
        
        **Note:** No guarantees are made regarding stability of the representation between
        versions.
        """
        ...


    @staticmethod
    def fromByteArray(byteArray: list[int]) -> "Stats":
        """
        Creates a Stats instance from the given byte representation which was obtained by
        .toByteArray.
        
        **Note:** No guarantees are made regarding stability of the representation between
        versions.
        """
        ...
