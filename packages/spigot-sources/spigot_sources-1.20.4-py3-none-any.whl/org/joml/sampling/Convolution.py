"""
Python module generated from Java source file org.joml.sampling.Convolution

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Math
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class Convolution:
    """
    Generates various convolution kernels.

    Author(s)
    - Kai Burjack
    """

    @staticmethod
    def gaussianKernel(rows: int, cols: int, sigma: float, dest: "FloatBuffer") -> None:
        """
        Generate a Gaussian convolution kernel with the given number of rows and columns, and store
        the factors in row-major order in `dest`.

        Arguments
        - rows: the number of rows (must be an odd number)
        - cols: the number of columns (must be an odd number)
        - sigma: the standard deviation of the filter kernel values
        - dest: will hold the kernel factors in row-major order
        """
        ...


    @staticmethod
    def gaussianKernel(rows: int, cols: int, sigma: float, dest: list[float]) -> None:
        """
        Generate a Gaussian convolution kernel with the given number of rows and columns, and store
        the factors in row-major order in `dest`.

        Arguments
        - rows: the number of rows (must be an odd number)
        - cols: the number of columns (must be an odd number)
        - sigma: the standard deviation of the filter kernel values
        - dest: will hold the kernel factors in row-major order
        """
        ...
