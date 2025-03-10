"""
Python module generated from Java source file com.google.common.math.PairedStatsAccumulator

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.math import *
from com.google.common.primitives import Doubles
from typing import Any, Callable, Iterable, Tuple


class PairedStatsAccumulator:
    """
    A mutable object which accumulates paired double values (e.g. points on a plane) and tracks some
    basic statistics over all the values added so far. This class is not thread safe.

    Author(s)
    - Pete Gillin

    Since
    - 20.0
    """

    def add(self, x: float, y: float) -> None:
        """
        Adds the given pair of values to the dataset.
        """
        ...


    def addAll(self, values: "PairedStats") -> None:
        """
        Adds the given statistics to the dataset, as if the individual values used to compute the
        statistics had been added directly.
        """
        ...


    def snapshot(self) -> "PairedStats":
        """
        Returns an immutable snapshot of the current statistics.
        """
        ...


    def count(self) -> int:
        """
        Returns the number of pairs in the dataset.
        """
        ...


    def xStats(self) -> "Stats":
        """
        Returns an immutable snapshot of the statistics on the `x` values alone.
        """
        ...


    def yStats(self) -> "Stats":
        """
        Returns an immutable snapshot of the statistics on the `y` values alone.
        """
        ...


    def populationCovariance(self) -> float:
        """
        Returns the population covariance of the values. The count must be non-zero.
        
        This is guaranteed to return zero if the dataset contains a single pair of finite values. It
        is not guaranteed to return zero when the dataset consists of the same pair of values multiple
        times, due to numerical errors.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

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
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values
        """
        ...


    def pearsonsCorrelationCoefficient(self) -> float:
        """
        Returns the <a href="http://mathworld.wolfram.com/CorrelationCoefficient.html">Pearson's or
        product-moment correlation coefficient</a> of the values. The count must greater than one, and
        the `x` and `y` values must both have non-zero population variance (i.e. `xStats().populationVariance() > 0.0 && yStats().populationVariance() > 0.0`). The result is not
        guaranteed to be exactly +/-1 even when the data are perfectly (anti-)correlated, due to
        numerical errors. However, it is guaranteed to be in the inclusive range [-1, +1].
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is Double.NaN.

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values, or
            either the `x` and `y` dataset has zero population variance
        """
        ...


    def leastSquaresFit(self) -> "LinearTransformation":
        """
        Returns a linear transformation giving the best fit to the data according to <a
        href="http://mathworld.wolfram.com/LeastSquaresFitting.html">Ordinary Least Squares linear
        regression</a> of `y` as a function of `x`. The count must be greater than one, and
        either the `x` or `y` data must have a non-zero population variance (i.e. `xStats().populationVariance() > 0.0 || yStats().populationVariance() > 0.0`). The result is
        guaranteed to be horizontal if there is variance in the `x` data but not the `y`
        data, and vertical if there is variance in the `y` data but not the `x` data.
        
        This fit minimizes the root-mean-square error in `y` as a function of `x`. This
        error is defined as the square root of the mean of the squares of the differences between the
        actual `y` values of the data and the values predicted by the fit for the `x`
        values (i.e. it is the square root of the mean of the squares of the vertical distances between
        the data points and the best fit line). For this fit, this error is a fraction `sqrt(1 -
        R*R)` of the population standard deviation of `y`, where `R` is the Pearson's
        correlation coefficient (as given by .pearsonsCorrelationCoefficient()).
        
        The corresponding root-mean-square error in `x` as a function of `y` is a
        fraction `sqrt(1/(R*R) - 1)` of the population standard deviation of `x`. This fit
        does not normally minimize that error: to do that, you should swap the roles of `x` and
        `y`.
        
        <h3>Non-finite values</h3>
        
        If the dataset contains any non-finite values (Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, or Double.NaN) then the result is LinearTransformation.forNaN().

        Raises
        - IllegalStateException: if the dataset is empty or contains a single pair of values, or
            both the `x` and `y` dataset have zero population variance
        """
        ...
