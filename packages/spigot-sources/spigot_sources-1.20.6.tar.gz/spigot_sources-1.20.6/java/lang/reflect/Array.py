"""
Python module generated from Java source file java.lang.reflect.Array

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from jdk.internal.vm.annotation import IntrinsicCandidate
from typing import Any, Callable, Iterable, Tuple


class Array:
    """
    The `Array` class provides static methods to dynamically create and
    access Java arrays.
    
    `Array` permits widening conversions to occur during a get or set
    operation, but throws an `IllegalArgumentException` if a narrowing
    conversion would occur.

    Author(s)
    - Nakul Saraiya

    Since
    - 1.1
    """

    @staticmethod
    def newInstance(componentType: type[Any], length: int) -> "Object":
        """
        Creates a new array with the specified component type and
        length.
        Invoking this method is equivalent to creating an array
        as follows:
        <blockquote>
        ```
        int[] x = {length};
        Array.newInstance(componentType, x);
        ```
        </blockquote>
        
        The number of dimensions of the new array must not
        exceed 255.

        Arguments
        - componentType: the `Class` object representing the
                component type of the new array
        - length: the length of the new array

        Returns
        - the new array

        Raises
        - NullPointerException: if the specified
                `componentType` parameter is null
        - IllegalArgumentException: if componentType is Void.TYPE or if the number of dimensions of the requested array
                instance exceed 255.
        - NegativeArraySizeException: if the specified `length`
                is negative
        """
        ...


    @staticmethod
    def newInstance(componentType: type[Any], *dimensions: Tuple[int, ...]) -> "Object":
        """
        Creates a new array
        with the specified component type and dimensions.
        If `componentType`
        represents a non-array class or interface, the new array
        has `dimensions.length` dimensions and
        `componentType` as its component type. If
        `componentType` represents an array class, the
        number of dimensions of the new array is equal to the sum
        of `dimensions.length` and the number of
        dimensions of `componentType`. In this case, the
        component type of the new array is the component type of
        `componentType`.
        
        The number of dimensions of the new array must not
        exceed 255.

        Arguments
        - componentType: the `Class` object representing the component
        type of the new array
        - dimensions: an array of `int` representing the dimensions of
        the new array

        Returns
        - the new array

        Raises
        - NullPointerException: if the specified
        `componentType` argument is null
        - IllegalArgumentException: if the specified `dimensions`
        argument is a zero-dimensional array, if componentType is Void.TYPE, or if the number of dimensions of the requested array
        instance exceed 255.
        - NegativeArraySizeException: if any of the components in
        the specified `dimensions` argument is negative.
        """
        ...


    @staticmethod
    def getLength(array: "Object") -> int:
        """
        Returns the length of the specified array object, as an `int`.

        Arguments
        - array: the array

        Returns
        - the length of the array

        Raises
        - IllegalArgumentException: if the object argument is not
        an array
        """
        ...


    @staticmethod
    def get(array: "Object", index: int) -> "Object":
        """
        Returns the value of the indexed component in the specified
        array object.  The value is automatically wrapped in an object
        if it has a primitive type.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the (possibly wrapped) value of the indexed component in
        the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array
        """
        ...


    @staticmethod
    def getBoolean(array: "Object", index: int) -> bool:
        """
        Returns the value of the indexed component in the specified
        array object, as a `boolean`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getByte(array: "Object", index: int) -> int:
        """
        Returns the value of the indexed component in the specified
        array object, as a `byte`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getChar(array: "Object", index: int) -> str:
        """
        Returns the value of the indexed component in the specified
        array object, as a `char`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getShort(array: "Object", index: int) -> int:
        """
        Returns the value of the indexed component in the specified
        array object, as a `short`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getInt(array: "Object", index: int) -> int:
        """
        Returns the value of the indexed component in the specified
        array object, as an `int`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getLong(array: "Object", index: int) -> int:
        """
        Returns the value of the indexed component in the specified
        array object, as a `long`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getFloat(array: "Object", index: int) -> float:
        """
        Returns the value of the indexed component in the specified
        array object, as a `float`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def getDouble(array: "Object", index: int) -> float:
        """
        Returns the value of the indexed component in the specified
        array object, as a `double`.

        Arguments
        - array: the array
        - index: the index

        Returns
        - the value of the indexed component in the specified array

        Raises
        - NullPointerException: If the specified object is null
        - IllegalArgumentException: If the specified object is not
        an array, or if the indexed element cannot be converted to the
        return type by an identity or widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to the
        length of the specified array

        See
        - Array.get
        """
        ...


    @staticmethod
    def set(array: "Object", index: int, value: "Object") -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified new value.  The new value is first
        automatically unwrapped if the array has a primitive component
        type.

        Arguments
        - array: the array
        - index: the index into the array
        - value: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the array component type is primitive and
        an unwrapping conversion fails
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array
        """
        ...


    @staticmethod
    def setBoolean(array: "Object", index: int, z: bool) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `boolean` value.

        Arguments
        - array: the array
        - index: the index into the array
        - z: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setByte(array: "Object", index: int, b: int) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `byte` value.

        Arguments
        - array: the array
        - index: the index into the array
        - b: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setChar(array: "Object", index: int, c: str) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `char` value.

        Arguments
        - array: the array
        - index: the index into the array
        - c: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setShort(array: "Object", index: int, s: int) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `short` value.

        Arguments
        - array: the array
        - index: the index into the array
        - s: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setInt(array: "Object", index: int, i: int) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `int` value.

        Arguments
        - array: the array
        - index: the index into the array
        - i: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setLong(array: "Object", index: int, l: int) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `long` value.

        Arguments
        - array: the array
        - index: the index into the array
        - l: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setFloat(array: "Object", index: int, f: float) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `float` value.

        Arguments
        - array: the array
        - index: the index into the array
        - f: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...


    @staticmethod
    def setDouble(array: "Object", index: int, d: float) -> None:
        """
        Sets the value of the indexed component of the specified array
        object to the specified `double` value.

        Arguments
        - array: the array
        - index: the index into the array
        - d: the new value of the indexed component

        Raises
        - NullPointerException: If the specified object argument
        is null
        - IllegalArgumentException: If the specified object argument
        is not an array, or if the specified value cannot be converted
        to the underlying array's component type by an identity or a
        primitive widening conversion
        - ArrayIndexOutOfBoundsException: If the specified `index`
        argument is negative, or if it is greater than or equal to
        the length of the specified array

        See
        - Array.set
        """
        ...
