"""
Python module generated from Java source file com.google.common.math.Quantiles

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.math import *
from com.google.common.primitives import Doubles
from com.google.common.primitives import Ints
from java.math import RoundingMode
from typing import Any, Callable, Iterable, Tuple


class Quantiles:
    """
    Provides a fluent API for calculating <a
    href="http://en.wikipedia.org/wiki/Quantile">quantiles</a>.
    
    <h3>Examples</h3>
    
    To compute the median:
    
    ````double myMedian = median().compute(myDataset);````
    
    where .median() has been statically imported.
    
    To compute the 99th percentile:
    
    ````double myPercentile99 = percentiles().index(99).compute(myDataset);````
    
    where .percentiles() has been statically imported.
    
    To compute median and the 90th and 99th percentiles:
    
    ````Map<Integer, Double> myPercentiles =
        percentiles().indexes(50, 90, 99).compute(myDataset);````
    
    where .percentiles() has been statically imported: `myPercentiles` maps the keys
    50, 90, and 99, to their corresponding quantile values.
    
    To compute quartiles, use .quartiles() instead of .percentiles(). To compute
    arbitrary q-quantiles, use .scale scale(q).
    
    These examples all take a copy of your dataset. If you have a double array, you are okay with
    it being arbitrarily reordered, and you want to avoid that copy, you can use `computeInPlace` instead of `compute`.
    
    <h3>Definition and notes on interpolation</h3>
    
    The definition of the kth q-quantile of N values is as follows: define x = k * (N - 1) / q; if
    x is an integer, the result is the value which would appear at index x in the sorted dataset
    (unless there are Double.NaN NaN values, see below); otherwise, the result is the average
    of the values which would appear at the indexes floor(x) and ceil(x) weighted by (1-frac(x)) and
    frac(x) respectively. This is the same definition as used by Excel and by S, it is the Type 7
    definition in <a
    href="http://stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html">R</a>, and it is
    described by <a
    href="http://en.wikipedia.org/wiki/Quantile#Estimating_the_quantiles_of_a_population">
    wikipedia</a> as providing "Linear interpolation of the modes for the order statistics for the
    uniform distribution on [0,1]."
    
    <h3>Handling of non-finite values</h3>
    
    If any values in the input are Double.NaN NaN then all values returned are Double.NaN NaN. (This is the one occasion when the behaviour is not the same as you'd get from
    sorting with java.util.Arrays.sort(double[]) Arrays.sort(double[]) or java.util.Collections.sort(java.util.List) Collections.sort(List&lt;Double&gt;) and selecting
    the required value(s). Those methods would sort Double.NaN NaN as if it is greater than
    any other value and place them at the end of the dataset, even after Double.POSITIVE_INFINITY POSITIVE_INFINITY.)
    
    Otherwise, Double.NEGATIVE_INFINITY NEGATIVE_INFINITY and Double.POSITIVE_INFINITY POSITIVE_INFINITY sort to the beginning and the end of the dataset, as
    you would expect.
    
    If required to do a weighted average between an infinity and a finite value, or between an
    infinite value and itself, the infinite value is returned. If required to do a weighted average
    between Double.NEGATIVE_INFINITY NEGATIVE_INFINITY and Double.POSITIVE_INFINITY
    POSITIVE_INFINITY, Double.NaN NaN is returned (note that this will only happen if the
    dataset contains no finite values).
    
    <h3>Performance</h3>
    
    The average time complexity of the computation is O(N) in the size of the dataset. There is a
    worst case time complexity of O(N^2). You are extremely unlikely to hit this quadratic case on
    randomly ordered data (the probability decreases faster than exponentially in N), but if you are
    passing in unsanitized user data then a malicious user could force it. A light shuffle of the
    data using an unpredictable seed should normally be enough to thwart this attack.
    
    The time taken to compute multiple quantiles on the same dataset using Scale.indexes
    indexes is generally less than the total time taken to compute each of them separately, and
    sometimes much less. For example, on a large enough dataset, computing the 90th and 99th
    percentiles together takes about 55% as long as computing them separately.
    
    When calling ScaleAndIndex.compute (in ScaleAndIndexes.compute either
    form), the memory requirement is 8*N bytes for the copy of the dataset plus an overhead which is
    independent of N (but depends on the quantiles being computed). When calling ScaleAndIndex.computeInPlace computeInPlace (in ScaleAndIndexes.computeInPlace
    either form), only the overhead is required. The number of object allocations is independent of
    N in both cases.

    Author(s)
    - Pete Gillin

    Since
    - 20.0
    """

    @staticmethod
    def median() -> "ScaleAndIndex":
        """
        Specifies the computation of a median (i.e. the 1st 2-quantile).
        """
        ...


    @staticmethod
    def quartiles() -> "Scale":
        """
        Specifies the computation of quartiles (i.e. 4-quantiles).
        """
        ...


    @staticmethod
    def percentiles() -> "Scale":
        """
        Specifies the computation of percentiles (i.e. 100-quantiles).
        """
        ...


    @staticmethod
    def scale(scale: int) -> "Scale":
        """
        Specifies the computation of q-quantiles.

        Arguments
        - scale: the scale for the quantiles to be calculated, i.e. the q of the q-quantiles, which
            must be positive
        """
        ...


    class Scale:
        """
        Describes the point in a fluent API chain where only the scale (i.e. the q in q-quantiles) has
        been specified.

        Since
        - 20.0
        """

        def index(self, index: int) -> "ScaleAndIndex":
            """
            Specifies a single quantile index to be calculated, i.e. the k in the kth q-quantile.

            Arguments
            - index: the quantile index, which must be in the inclusive range [0, q] for q-quantiles
            """
            ...


        def indexes(self, *indexes: Tuple[int, ...]) -> "ScaleAndIndexes":
            """
            Specifies multiple quantile indexes to be calculated, each index being the k in the kth
            q-quantile.

            Arguments
            - indexes: the quantile indexes, each of which must be in the inclusive range [0, q] for
                q-quantiles; the order of the indexes is unimportant, duplicates will be ignored, and the
                set will be snapshotted when this method is called

            Raises
            - IllegalArgumentException: if `indexes` is empty
            """
            ...


        def indexes(self, indexes: Iterable["Integer"]) -> "ScaleAndIndexes":
            """
            Specifies multiple quantile indexes to be calculated, each index being the k in the kth
            q-quantile.

            Arguments
            - indexes: the quantile indexes, each of which must be in the inclusive range [0, q] for
                q-quantiles; the order of the indexes is unimportant, duplicates will be ignored, and the
                set will be snapshotted when this method is called

            Raises
            - IllegalArgumentException: if `indexes` is empty
            """
            ...


    class ScaleAndIndex:
        """
        Describes the point in a fluent API chain where the scale and a single quantile index (i.e. the
        q and the k in the kth q-quantile) have been specified.

        Since
        - 20.0
        """

        def compute(self, dataset: Iterable["Number"]) -> float:
            """
            Computes the quantile value of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles (with any associated lost of precision), and which will not be mutated by
                this call (it is copied instead)

            Returns
            - the quantile value
            """
            ...


        def compute(self, *dataset: Tuple[float, ...]) -> float:
            """
            Computes the quantile value of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will not
                be mutated by this call (it is copied instead)

            Returns
            - the quantile value
            """
            ...


        def compute(self, *dataset: Tuple[int, ...]) -> float:
            """
            Computes the quantile value of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles (with any associated lost of precision), and which will not be mutated by
                this call (it is copied instead)

            Returns
            - the quantile value
            """
            ...


        def compute(self, *dataset: Tuple[int, ...]) -> float:
            """
            Computes the quantile value of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles, and which will not be mutated by this call (it is copied instead)

            Returns
            - the quantile value
            """
            ...


        def computeInPlace(self, *dataset: Tuple[float, ...]) -> float:
            """
            Computes the quantile value of the given dataset, performing the computation in-place.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, and which will
                be arbitrarily reordered by this method call

            Returns
            - the quantile value
            """
            ...


    class ScaleAndIndexes:
        """
        Describes the point in a fluent API chain where the scale and a multiple quantile indexes (i.e.
        the q and a set of values for the k in the kth q-quantile) have been specified.

        Since
        - 20.0
        """

        def compute(self, dataset: Iterable["Number"]) -> dict["Integer", "Double"]:
            """
            Computes the quantile values of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles (with any associated lost of precision), and which will not be mutated by
                this call (it is copied instead)

            Returns
            - an unmodifiable, ordered map of results: the keys will be the specified quantile
                indexes, and the values the corresponding quantile values. When iterating, entries in the
                map are ordered by quantile index in the same order they were passed to the `indexes` method.
            """
            ...


        def compute(self, *dataset: Tuple[float, ...]) -> dict["Integer", "Double"]:
            """
            Computes the quantile values of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will not
                be mutated by this call (it is copied instead)

            Returns
            - an unmodifiable, ordered map of results: the keys will be the specified quantile
                indexes, and the values the corresponding quantile values. When iterating, entries in the
                map are ordered by quantile index in the same order they were passed to the `indexes` method.
            """
            ...


        def compute(self, *dataset: Tuple[int, ...]) -> dict["Integer", "Double"]:
            """
            Computes the quantile values of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles (with any associated lost of precision), and which will not be mutated by
                this call (it is copied instead)

            Returns
            - an unmodifiable, ordered map of results: the keys will be the specified quantile
                indexes, and the values the corresponding quantile values. When iterating, entries in the
                map are ordered by quantile index in the same order they were passed to the `indexes` method.
            """
            ...


        def compute(self, *dataset: Tuple[int, ...]) -> dict["Integer", "Double"]:
            """
            Computes the quantile values of the given dataset.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, which will be
                cast to doubles, and which will not be mutated by this call (it is copied instead)

            Returns
            - an unmodifiable, ordered map of results: the keys will be the specified quantile
                indexes, and the values the corresponding quantile values. When iterating, entries in the
                map are ordered by quantile index in the same order they were passed to the `indexes` method.
            """
            ...


        def computeInPlace(self, *dataset: Tuple[float, ...]) -> dict["Integer", "Double"]:
            """
            Computes the quantile values of the given dataset, performing the computation in-place.

            Arguments
            - dataset: the dataset to do the calculation on, which must be non-empty, and which will
                be arbitrarily reordered by this method call

            Returns
            - an unmodifiable, ordered map of results: the keys will be the specified quantile
                indexes, and the values the corresponding quantile values. When iterating, entries in the
                map are ordered by quantile index in the same order that the indexes were passed to the
                `indexes` method.
            """
            ...
