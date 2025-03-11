"""
Python module generated from Java source file com.google.common.math.LinearTransformation

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.math import *
from com.google.errorprone.annotations.concurrent import LazyInit
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class LinearTransformation:
    """
    The representation of a linear transformation between real numbers `x` and `y`.
    Graphically, this is the specification of a straight line on a plane. The transformation can be
    expressed as `y = m * x + c` for finite `m` and `c`, unless it is a vertical
    transformation in which case `x` has a constant value for all `y`. In the
    non-vertical case, `m` is the slope of the transformation (and a horizontal transformation
    has zero slope).

    Author(s)
    - Pete Gillin

    Since
    - 20.0
    """

    @staticmethod
    def mapping(x1: float, y1: float) -> "LinearTransformationBuilder":
        """
        Start building an instance which maps `x = x1` to `y = y1`. Both arguments must be
        finite. Call either LinearTransformationBuilder.and or LinearTransformationBuilder.withSlope on the returned object to finish building the instance.
        """
        ...


    @staticmethod
    def vertical(x: float) -> "LinearTransformation":
        """
        Builds an instance representing a vertical transformation with a constant value of `x`.
        (The inverse of this will be a horizontal transformation.)
        """
        ...


    @staticmethod
    def horizontal(y: float) -> "LinearTransformation":
        """
        Builds an instance representing a horizontal transformation with a constant value of `y`.
        (The inverse of this will be a vertical transformation.)
        """
        ...


    @staticmethod
    def forNaN() -> "LinearTransformation":
        """
        Builds an instance for datasets which contains Double.NaN. The .isHorizontal
        and .isVertical methods return `False` and the .slope, and .transform methods all return Double.NaN. The .inverse method returns the same
        instance.
        """
        ...


    def isVertical(self) -> bool:
        """
        Returns whether this is a vertical transformation.
        """
        ...


    def isHorizontal(self) -> bool:
        """
        Returns whether this is a horizontal transformation.
        """
        ...


    def slope(self) -> float:
        """
        Returns the slope of the transformation, i.e. the rate of change of `y` with respect to
        `x`. This must not be called on a vertical transformation (i.e. when .isVertical() is True).
        """
        ...


    def transform(self, x: float) -> float:
        """
        Returns the `y` corresponding to the given `x`. This must not be called on a
        vertical transformation (i.e. when .isVertical() is True).
        """
        ...


    def inverse(self) -> "LinearTransformation":
        """
        Returns the inverse linear transformation. The inverse of a horizontal transformation is a
        vertical transformation, and vice versa. The inverse of the .forNaN transformation is
        itself. In all other cases, the inverse is a transformation such that applying both the
        original transformation and its inverse to a value gives you the original value give-or-take
        numerical errors. Calling this method multiple times on the same instance will always return
        the same instance. Calling this method on the result of calling this method on an instance will
        always return that original instance.
        """
        ...


    class LinearTransformationBuilder:
        """
        This is an intermediate stage in the construction process. It is returned by LinearTransformation.mapping. You almost certainly don't want to keep instances around, but
        instead use method chaining. This represents a single point mapping, i.e. a mapping between one
        `x` and `y` value pair.

        Since
        - 20.0
        """

        def and(self, x2: float, y2: float) -> "LinearTransformation":
            """
            Finish building an instance which also maps `x = x2` to `y = y2`. These values
            must not both be identical to the values given in the first mapping. If only the `x`
            values are identical, the transformation is vertical. If only the `y` values are
            identical, the transformation is horizontal (i.e. the slope is zero).
            """
            ...


        def withSlope(self, slope: float) -> "LinearTransformation":
            """
            Finish building an instance with the given slope, i.e. the rate of change of `y` with
            respect to `x`. The slope must not be `NaN`. It may be infinite, in which case
            the transformation is vertical. (If it is zero, the transformation is horizontal.)
            """
            ...
