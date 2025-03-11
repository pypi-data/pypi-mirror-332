"""
Python module generated from Java source file org.joml.Math

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Math:
    """
    Contains fast approximations of some java.lang.Math operations.
    
    By default, java.lang.Math methods will be used by all other JOML classes. In order to use the approximations in this class, start the JVM with the parameter `-Djoml.fastmath`.
    
    There are two algorithms for approximating sin/cos:
    <ol>
    - arithmetic <a href="http://www.java-gaming.org/topics/joml-1-8-0-release/37491/msg/361815/view.html#msg361815">polynomial approximation</a> contributed by roquendm 
    - theagentd's <a href="http://www.java-gaming.org/topics/extremely-fast-sine-cosine/36469/msg/346213/view.html#msg346213">linear interpolation</a> variant of Riven's algorithm from
    <a href="http://www.java-gaming.org/topics/extremely-fast-sine-cosine/36469/view.html">http://www.java-gaming.org/</a>
    </ol>
    By default, the first algorithm is being used. In order to use the second one, start the JVM with `-Djoml.sinLookup`. The lookup table bit length of the second algorithm can also be adjusted
    for improved accuracy via `-Djoml.sinLookup.bits=&lt;n&gt;`, where &lt;n&gt; is the number of bits of the lookup table.

    Author(s)
    - Kai Burjack
    """

    PI = java.lang.Math.PI
    PI_TIMES_2 = PI * 2.0
    PI_f = (float) java.lang.Math.PI
    PI_TIMES_2_f = PI_f * 2.0f
    PI_OVER_2 = PI * 0.5
    PI_OVER_2_f = (float) (PI * 0.5)
    PI_OVER_4 = PI * 0.25
    PI_OVER_4_f = (float) (PI * 0.25)
    ONE_OVER_PI = 1.0 / PI
    ONE_OVER_PI_f = (float) (1.0 / PI)


    @staticmethod
    def sin(rad: float) -> float:
        ...


    @staticmethod
    def sin(rad: float) -> float:
        ...


    @staticmethod
    def cos(rad: float) -> float:
        ...


    @staticmethod
    def cos(rad: float) -> float:
        ...


    @staticmethod
    def cosFromSin(sin: float, angle: float) -> float:
        ...


    @staticmethod
    def cosFromSin(sin: float, angle: float) -> float:
        ...


    @staticmethod
    def sqrt(r: float) -> float:
        ...


    @staticmethod
    def sqrt(r: float) -> float:
        ...


    @staticmethod
    def invsqrt(r: float) -> float:
        ...


    @staticmethod
    def invsqrt(r: float) -> float:
        ...


    @staticmethod
    def tan(r: float) -> float:
        ...


    @staticmethod
    def tan(r: float) -> float:
        ...


    @staticmethod
    def acos(r: float) -> float:
        ...


    @staticmethod
    def acos(r: float) -> float:
        ...


    @staticmethod
    def safeAcos(v: float) -> float:
        ...


    @staticmethod
    def safeAcos(v: float) -> float:
        ...


    @staticmethod
    def atan2(y: float, x: float) -> float:
        ...


    @staticmethod
    def atan2(y: float, x: float) -> float:
        ...


    @staticmethod
    def asin(r: float) -> float:
        ...


    @staticmethod
    def asin(r: float) -> float:
        ...


    @staticmethod
    def safeAsin(r: float) -> float:
        ...


    @staticmethod
    def safeAsin(r: float) -> float:
        ...


    @staticmethod
    def abs(r: float) -> float:
        ...


    @staticmethod
    def abs(r: float) -> float:
        ...


    @staticmethod
    def abs(r: int) -> int:
        ...


    @staticmethod
    def abs(r: int) -> int:
        ...


    @staticmethod
    def max(x: int, y: int) -> int:
        ...


    @staticmethod
    def min(x: int, y: int) -> int:
        ...


    @staticmethod
    def max(x: int, y: int) -> int:
        ...


    @staticmethod
    def min(x: int, y: int) -> int:
        ...


    @staticmethod
    def min(a: float, b: float) -> float:
        ...


    @staticmethod
    def min(a: float, b: float) -> float:
        ...


    @staticmethod
    def max(a: float, b: float) -> float:
        ...


    @staticmethod
    def max(a: float, b: float) -> float:
        ...


    @staticmethod
    def clamp(a: float, b: float, val: float) -> float:
        ...


    @staticmethod
    def clamp(a: float, b: float, val: float) -> float:
        ...


    @staticmethod
    def clamp(a: int, b: int, val: int) -> int:
        ...


    @staticmethod
    def clamp(a: int, b: int, val: int) -> int:
        ...


    @staticmethod
    def toRadians(angles: float) -> float:
        ...


    @staticmethod
    def toRadians(angles: float) -> float:
        ...


    @staticmethod
    def toDegrees(angles: float) -> float:
        ...


    @staticmethod
    def toDegrees(angles: float) -> float:
        ...


    @staticmethod
    def floor(v: float) -> float:
        ...


    @staticmethod
    def floor(v: float) -> float:
        ...


    @staticmethod
    def ceil(v: float) -> float:
        ...


    @staticmethod
    def ceil(v: float) -> float:
        ...


    @staticmethod
    def round(v: float) -> int:
        ...


    @staticmethod
    def round(v: float) -> int:
        ...


    @staticmethod
    def exp(a: float) -> float:
        ...


    @staticmethod
    def isFinite(d: float) -> bool:
        ...


    @staticmethod
    def isFinite(f: float) -> bool:
        ...


    @staticmethod
    def fma(a: float, b: float, c: float) -> float:
        ...


    @staticmethod
    def fma(a: float, b: float, c: float) -> float:
        ...


    @staticmethod
    def roundUsing(v: float, mode: int) -> int:
        ...


    @staticmethod
    def roundUsing(v: float, mode: int) -> int:
        ...


    @staticmethod
    def roundLongUsing(v: float, mode: int) -> int:
        ...


    @staticmethod
    def lerp(a: float, b: float, t: float) -> float:
        ...


    @staticmethod
    def lerp(a: float, b: float, t: float) -> float:
        ...


    @staticmethod
    def biLerp(q00: float, q10: float, q01: float, q11: float, tx: float, ty: float) -> float:
        ...


    @staticmethod
    def biLerp(q00: float, q10: float, q01: float, q11: float, tx: float, ty: float) -> float:
        ...


    @staticmethod
    def triLerp(q000: float, q100: float, q010: float, q110: float, q001: float, q101: float, q011: float, q111: float, tx: float, ty: float, tz: float) -> float:
        ...


    @staticmethod
    def triLerp(q000: float, q100: float, q010: float, q110: float, q001: float, q101: float, q011: float, q111: float, tx: float, ty: float, tz: float) -> float:
        ...


    @staticmethod
    def roundHalfEven(v: float) -> int:
        ...


    @staticmethod
    def roundHalfDown(v: float) -> int:
        ...


    @staticmethod
    def roundHalfUp(v: float) -> int:
        ...


    @staticmethod
    def roundHalfEven(v: float) -> int:
        ...


    @staticmethod
    def roundHalfDown(v: float) -> int:
        ...


    @staticmethod
    def roundHalfUp(v: float) -> int:
        ...


    @staticmethod
    def roundLongHalfEven(v: float) -> int:
        ...


    @staticmethod
    def roundLongHalfDown(v: float) -> int:
        ...


    @staticmethod
    def roundLongHalfUp(v: float) -> int:
        ...


    @staticmethod
    def random() -> float:
        ...


    @staticmethod
    def signum(v: float) -> float:
        ...


    @staticmethod
    def signum(v: float) -> float:
        ...


    @staticmethod
    def signum(v: int) -> int:
        ...


    @staticmethod
    def signum(v: int) -> int:
        ...
