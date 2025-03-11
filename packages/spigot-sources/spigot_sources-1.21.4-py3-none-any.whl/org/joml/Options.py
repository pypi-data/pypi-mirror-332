"""
Python module generated from Java source file org.joml.Options

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import DecimalFormat
from java.text import NumberFormat
from java.util import Arrays
from java.util import Locale
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Options:
    """
    Utility class for reading system properties.

    Author(s)
    - Kai Burjack
    """

    DEBUG = hasOption(System.getProperty("joml.debug", "false"))
    """
    Whether certain debugging checks should be made, such as that only direct NIO Buffers are used when Unsafe is active,
    and a proxy should be created on calls to readOnlyView().
    """
    NO_UNSAFE = hasOption(System.getProperty("joml.nounsafe", "false"))
    """
    Whether *not* to use sun.misc.Unsafe when copying memory with MemUtil.
    """
    FORCE_UNSAFE = hasOption(System.getProperty("joml.forceUnsafe", "false"))
    """
    Whether to *force* the use of sun.misc.Unsafe when copying memory with MemUtil.
    """
    FASTMATH = hasOption(System.getProperty("joml.fastmath", "false"))
    """
    Whether fast approximations of some java.lang.Math operations should be used.
    """
    SIN_LOOKUP = hasOption(System.getProperty("joml.sinLookup", "false"))
    """
    When .FASTMATH is `True`, whether to use a lookup table for sin/cos.
    """
    SIN_LOOKUP_BITS = Integer.parseInt(System.getProperty("joml.sinLookup.bits", "14"))
    """
    When .SIN_LOOKUP is `True`, this determines the table size.
    """
    useNumberFormat = hasOption(System.getProperty("joml.format", "true"))
    """
    Whether to use a NumberFormat producing scientific notation output when formatting matrix,
    vector and quaternion components to strings.
    """
    USE_MATH_FMA = hasOption(System.getProperty("joml.useMathFma", "false"))
    """
    Whether to try using java.lang.Math.fma() in most matrix/vector/quaternion operations if it is available.
    If the CPU does *not* support it, it will be a lot slower than `a*b+c` and potentially generate a lot of memory allocations
    for the emulation with `java.util.BigDecimal`, though.
    """
    numberFormatDecimals = Integer.parseInt(System.getProperty("joml.format.decimals", "3"))
    """
    When .useNumberFormat is `True` then this determines the number of decimal digits
    produced in the formatted numbers.
    """
    NUMBER_FORMAT = decimalFormat()
    """
    The NumberFormat used to format all numbers throughout all JOML classes.
    """
