"""
Python module generated from Java source file com.google.common.math.PairedStats

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
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class PairedStats(Serializable):
    """
    An immutable value object capturing some basic statistics about a collection of paired double
    values (e.g. points on a plane). Build instances with PairedStatsAccumulator.snapshot.

    Author(s)
    - Pete Gillin

    Since
    - 20.0
    """

    def count(self) -> int:
        """
        Returns the number of pairs in the dataset.
        """
        ...


    def xStats(self) -> "Stats":
        """
        Returns the statistics on the `x` values alone.
        """
        ...


    def yStats(self) -> "Stats":
        """
        Returns the statistics on the `y` values alone.
        """
        ...


    def populationCovariance(self) -> float:
        """
        Returns the population covariance of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains a single pair of finite values. It
        is not guaranteed to return zero when the dataset consists of the same pair of values multiple
        times, due to numerical errors.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty
        """
        ...


    def sampleCovariance(self) -> float:
        """
        Returns the sample covariance of the values. The count must be greater than one.
        
        This is not guaranteed to return zero when the dataset consists of the same pair of values
        multiple times, due to numerical errors.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values
        """
        ...


    def pearsonsCorrelationCoefficient(self) -> float:
        """
        Returns the <a href="http://mathworld.wolfram.com/CorrelationCoefficient.html">Pearson's or
        product-moment correlation coefficient</a> of the values. The count must greater than one, and
        the `x` and `y` values must both have non-zero population variance (i.e.
        `xStats().populationVariance() > 0.0 && yStats().populationVariance() > 0.0`). The result
        is not guaranteed to be exactly +/-1 even when the data are perfectly (anti-)correlated, due to
        numerical errors. However, it is guaranteed to be in the inclusive range [-1, +1].
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values, or
            either the `x` and `y` dataset has zero population variance
        """
        ...


    def leastSquaresFit(self) -> "LinearTransformation":
        """
        Returns a linear transformation giving the best fit to the data according to
        <a href="http://mathworld.wolfram.com/LeastSquaresFitting.html">Ordinary Least Squares linear
        regression</a> of `y` as a function of `x`. The count must be greater than one, and
        either the `x` or `y` data must have a non-zero population variance (i.e.
        `xStats().populationVariance() > 0.0 || yStats().populationVariance() > 0.0`). The result
        is guaranteed to be horizontal if there is variance in the `x` data but not the `y`
        data, and vertical if there is variance in the `y` data but not the `x` data.
        
        This fit minimizes the root-mean-square error in `y` as a function of `x`. This
        error is defined as the square root of the mean of the squares of the differences between the
        actual `y` values of the data and the values predicted by the fit for the `x`
        values (i.e. it is the square root of the mean of the squares of the vertical distances between
        the data points and the best fit line). For this fit, this error is a fraction
        `sqrt(1 - R*R)` of the population standard deviation of `y`, where `R` is the
        Pearson's correlation coefficient (as given by .pearsonsCorrelationCoefficient()).
        
        The corresponding root-mean-square error in `x` as a function of `y` is a
        fraction `sqrt(1/(R*R) - 1)` of the population standard deviation of `x`. This fit
        does not normally minimize that error: to do that, you should swap the roles of `x` and
        `y`.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY,
        Double.NEGATIVE_INFINITY, or Double.NaN) then the result is
        LinearTransformation.forNaN().

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values, or
            both the `x` and `y` dataset must have zero population variance
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


    def toByteArray(self) -> list[int]:
        """
        Gets a byte array representation of this instance.
        
        **Note:** No guarantees are made regarding stability of the representation between
        versions.
        """
        ...


    @staticmethod
    def fromByteArray(byteArray: list[int]) -> "PairedStats":
        """
        Creates a PairedStats instance from the given byte representation which was obtained by
        .toByteArray.
        
        **Note:** No guarantees are made regarding stability of the representation between
        versions.
        """
        ...
