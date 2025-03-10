"""
Python module generated from Java source file org.joml.Matrix4fc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix4fc:
    """
    Interface to a read-only view of a 4x4 matrix of single-precision floats.

    Author(s)
    - Kai Burjack
    """

    PLANE_NX = 0
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `x=-1` when using the identity matrix.
    """
    PLANE_PX = 1
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `x=1` when using the identity matrix.
    """
    PLANE_NY = 2
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `y=-1` when using the identity matrix.
    """
    PLANE_PY = 3
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `y=1` when using the identity matrix.
    """
    PLANE_NZ = 4
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `z=-1` when using the identity matrix.
    """
    PLANE_PZ = 5
    """
    Argument to the first parameter of .frustumPlane(int, Vector4f)
    identifying the plane with equation `z=1` when using the identity matrix.
    """
    CORNER_NXNYNZ = 0
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(-1, -1, -1)` when using the identity matrix.
    """
    CORNER_PXNYNZ = 1
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(1, -1, -1)` when using the identity matrix.
    """
    CORNER_PXPYNZ = 2
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(1, 1, -1)` when using the identity matrix.
    """
    CORNER_NXPYNZ = 3
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(-1, 1, -1)` when using the identity matrix.
    """
    CORNER_PXNYPZ = 4
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(1, -1, 1)` when using the identity matrix.
    """
    CORNER_NXNYPZ = 5
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(-1, -1, 1)` when using the identity matrix.
    """
    CORNER_NXPYPZ = 6
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(-1, 1, 1)` when using the identity matrix.
    """
    CORNER_PXPYPZ = 7
    """
    Argument to the first parameter of .frustumCorner(int, Vector3f)
    identifying the corner `(1, 1, 1)` when using the identity matrix.
    """
    PROPERTY_PERSPECTIVE = 1 << 0
    """
    Bit returned by .properties() to indicate that the matrix represents a perspective transformation.
    """
    PROPERTY_AFFINE = 1 << 1
    """
    Bit returned by .properties() to indicate that the matrix represents an affine transformation.
    """
    PROPERTY_IDENTITY = 1 << 2
    """
    Bit returned by .properties() to indicate that the matrix represents the identity transformation.
    """
    PROPERTY_TRANSLATION = 1 << 3
    """
    Bit returned by .properties() to indicate that the matrix represents a pure translation transformation.
    """
    PROPERTY_ORTHONORMAL = 1 << 4
    """
    Bit returned by .properties() to indicate that the upper-left 3x3 submatrix represents an orthogonal
    matrix (i.e. orthonormal basis). For practical reasons, this property also always implies 
    .PROPERTY_AFFINE in this implementation.
    """


    def properties(self) -> int:
        """
        Return the assumed properties of this matrix. This is a bit-combination of
        .PROPERTY_IDENTITY, .PROPERTY_AFFINE,
        .PROPERTY_TRANSLATION and .PROPERTY_PERSPECTIVE.

        Returns
        - the properties of the matrix
        """
        ...


    def m00(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m01(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m02(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def m03(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 3.

        Returns
        - the value of the matrix element
        """
        ...


    def m10(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m11(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m12(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def m13(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 3.

        Returns
        - the value of the matrix element
        """
        ...


    def m20(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m21(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m22(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def m23(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 3.

        Returns
        - the value of the matrix element
        """
        ...


    def m30(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m31(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m32(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def m33(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 3.

        Returns
        - the value of the matrix element
        """
        ...


    def mul(self, right: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul0(self, right: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!
        
        This method neither assumes nor checks for any matrix properties of `this` or `right`
        and will always perform a complete 4x4 matrix multiplication. This method should only be used whenever the
        multiplied matrices do not have any properties for which there are optimized multiplication methods available.

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, r00: float, r01: float, r02: float, r03: float, r10: float, r11: float, r12: float, r13: float, r20: float, r21: float, r22: float, r23: float, r30: float, r31: float, r32: float, r33: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the matrix with the supplied elements and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix whose 
        elements are supplied via the parameters, then the new matrix will be `M * R`.
        So when transforming a vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - r00: the m00 element of the right matrix
        - r01: the m01 element of the right matrix
        - r02: the m02 element of the right matrix
        - r03: the m03 element of the right matrix
        - r10: the m10 element of the right matrix
        - r11: the m11 element of the right matrix
        - r12: the m12 element of the right matrix
        - r13: the m13 element of the right matrix
        - r20: the m20 element of the right matrix
        - r21: the m21 element of the right matrix
        - r22: the m22 element of the right matrix
        - r23: the m23 element of the right matrix
        - r30: the m30 element of the right matrix
        - r31: the m31 element of the right matrix
        - r32: the m32 element of the right matrix
        - r33: the m33 element of the right matrix
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul3x3(self, r00: float, r01: float, r02: float, r10: float, r11: float, r12: float, r20: float, r21: float, r22: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the 3x3 matrix with the supplied elements expanded to a 4x4 matrix with 
        all other matrix elements set to identity, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix whose 
        elements are supplied via the parameters, then the new matrix will be `M * R`.
        So when transforming a vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - r00: the m00 element of the right matrix
        - r01: the m01 element of the right matrix
        - r02: the m02 element of the right matrix
        - r10: the m10 element of the right matrix
        - r11: the m11 element of the right matrix
        - r12: the m12 element of the right matrix
        - r20: the m20 element of the right matrix
        - r21: the m21 element of the right matrix
        - r22: the m22 element of the right matrix
        - dest: the destination matrix, which will hold the result

        Returns
        - this
        """
        ...


    def mulLocal(self, left: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply this matrix by the supplied `left` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the `left` matrix,
        then the new matrix will be `L * M`. So when transforming a
        vector `v` with the new matrix by using `L * M * v`, the
        transformation of `this` matrix will be applied first!

        Arguments
        - left: the left operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulLocalAffine(self, left: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply this matrix by the supplied `left` matrix, both of which are assumed to be .isAffine() affine, and store the result in `dest`.
        
        This method assumes that `this` matrix and the given `left` matrix both represent an .isAffine() affine transformation
        (i.e. their last rows are equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrices only represent affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        This method will not modify either the last row of `this` or the last row of `left`.
        
        If `M` is `this` matrix and `L` the `left` matrix,
        then the new matrix will be `L * M`. So when transforming a
        vector `v` with the new matrix by using `L * M * v`, the
        transformation of `this` matrix will be applied first!

        Arguments
        - left: the left operand of the matrix multiplication (the last row is assumed to be `(0, 0, 0, 1)`)
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, right: "Matrix3x2fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, right: "Matrix4x3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        The last row of the `right` matrix is assumed to be `(0, 0, 0, 1)`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulPerspectiveAffine(self, view: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` symmetric perspective projection matrix by the supplied .isAffine() affine `view` matrix and store the result in `dest`.
        
        If `P` is `this` matrix and `V` the `view` matrix,
        then the new matrix will be `P * V`. So when transforming a
        vector `v` with the new matrix by using `P * V * v`, the
        transformation of the `view` matrix will be applied first!

        Arguments
        - view: the .isAffine() affine matrix to multiply `this` symmetric perspective projection matrix by
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulPerspectiveAffine(self, view: "Matrix4x3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` symmetric perspective projection matrix by the supplied `view` matrix and store the result in `dest`.
        
        If `P` is `this` matrix and `V` the `view` matrix,
        then the new matrix will be `P * V`. So when transforming a
        vector `v` with the new matrix by using `P * V * v`, the
        transformation of the `view` matrix will be applied first!

        Arguments
        - view: the matrix to multiply `this` symmetric perspective projection matrix by
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulAffineR(self, right: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix, which is assumed to be .isAffine() affine, and store the result in `dest`.
        
        This method assumes that the given `right` matrix represents an .isAffine() affine transformation (i.e. its last row is equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrix only represents affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication (the last row is assumed to be `(0, 0, 0, 1)`)
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulAffine(self, right: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix by the supplied `right` matrix, both of which are assumed to be .isAffine() affine, and store the result in `dest`.
        
        This method assumes that `this` matrix and the given `right` matrix both represent an .isAffine() affine transformation
        (i.e. their last rows are equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrices only represent affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        This method will not modify either the last row of `this` or the last row of `right`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication (the last row is assumed to be `(0, 0, 0, 1)`)
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulTranslationAffine(self, right: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply this matrix, which is assumed to only contain a translation, by the supplied `right` matrix, which is assumed to be .isAffine() affine, and store the result in `dest`.
        
        This method assumes that `this` matrix only contains a translation, and that the given `right` matrix represents an .isAffine() affine transformation
        (i.e. its last row is equal to `(0, 0, 0, 1)`).
        
        This method will not modify either the last row of `this` or the last row of `right`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication (the last row is assumed to be `(0, 0, 0, 1)`)
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulOrthoAffine(self, view: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` orthographic projection matrix by the supplied .isAffine() affine `view` matrix
        and store the result in `dest`.
        
        If `M` is `this` matrix and `V` the `view` matrix,
        then the new matrix will be `M * V`. So when transforming a
        vector `v` with the new matrix by using `M * V * v`, the
        transformation of the `view` matrix will be applied first!

        Arguments
        - view: the affine matrix which to multiply `this` with
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def fma4x3(self, other: "Matrix4fc", otherFactor: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise add the upper 4x3 submatrices of `this` and `other`
        by first multiplying each component of `other`'s 4x3 submatrix by `otherFactor`,
        adding that to `this` and storing the final result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.
        
        The matrices `this` and `other` will not be changed.

        Arguments
        - other: the other matrix
        - otherFactor: the factor to multiply each of the other matrix's 4x3 components
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, other: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise add `this` and `other` and store the result in `dest`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, subtrahend: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise subtract `subtrahend` from `this` and store the result in `dest`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulComponentWise(self, other: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise multiply `this` by `other` and store the result in `dest`.

        Arguments
        - other: the other matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add4x3(self, other: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise add the upper 4x3 submatrices of `this` and `other`
        and store the result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub4x3(self, subtrahend: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise subtract the upper 4x3 submatrices of `subtrahend` from `this`
        and store the result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul4x3ComponentWise(self, other: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Component-wise multiply the upper 4x3 submatrices of `this` by `other`
        and store the result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.

        Arguments
        - other: the other matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def determinant(self) -> float:
        """
        Return the determinant of this matrix.
        
        If `this` matrix represents an .isAffine() affine transformation, such as translation, rotation, scaling and shearing,
        and thus its last row is equal to `(0, 0, 0, 1)`, then .determinantAffine() can be used instead of this method.

        Returns
        - the determinant

        See
        - .determinantAffine()
        """
        ...


    def determinant3x3(self) -> float:
        """
        Return the determinant of the upper left 3x3 submatrix of this matrix.

        Returns
        - the determinant
        """
        ...


    def determinantAffine(self) -> float:
        """
        Return the determinant of this matrix by assuming that it represents an .isAffine() affine transformation and thus
        its last row is equal to `(0, 0, 0, 1)`.

        Returns
        - the determinant
        """
        ...


    def invert(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Invert this matrix and write the result into `dest`.
        
        If `this` matrix represents an .isAffine() affine transformation, such as translation, rotation, scaling and shearing,
        and thus its last row is equal to `(0, 0, 0, 1)`, then .invertAffine(Matrix4f) can be used instead of this method.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .invertAffine(Matrix4f)
        """
        ...


    def invertPerspective(self, dest: "Matrix4f") -> "Matrix4f":
        """
        If `this` is a perspective projection matrix obtained via one of the .perspective(float, float, float, float, Matrix4f) perspective() methods,
        that is, if `this` is a symmetrical perspective frustum transformation,
        then this method builds the inverse of `this` and stores it into the given `dest`.
        
        This method can be used to quickly obtain the inverse of a perspective projection matrix when being obtained via .perspective(float, float, float, float, Matrix4f) perspective().

        Arguments
        - dest: will hold the inverse of `this`

        Returns
        - dest

        See
        - .perspective(float, float, float, float, Matrix4f)
        """
        ...


    def invertFrustum(self, dest: "Matrix4f") -> "Matrix4f":
        """
        If `this` is an arbitrary perspective projection matrix obtained via one of the .frustum(float, float, float, float, float, float, Matrix4f) frustum() methods,
        then this method builds the inverse of `this` and stores it into the given `dest`.
        
        This method can be used to quickly obtain the inverse of a perspective projection matrix.
        
        If this matrix represents a symmetric perspective frustum transformation, as obtained via .perspective(float, float, float, float, Matrix4f) perspective(), then
        .invertPerspective(Matrix4f) should be used instead.

        Arguments
        - dest: will hold the inverse of `this`

        Returns
        - dest

        See
        - .invertPerspective(Matrix4f)
        """
        ...


    def invertOrtho(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Invert `this` orthographic projection matrix and store the result into the given `dest`.
        
        This method can be used to quickly obtain the inverse of an orthographic projection matrix.

        Arguments
        - dest: will hold the inverse of `this`

        Returns
        - dest
        """
        ...


    def invertPerspectiveView(self, view: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        If `this` is a perspective projection matrix obtained via one of the .perspective(float, float, float, float, Matrix4f) perspective() methods,
        that is, if `this` is a symmetrical perspective frustum transformation
        and the given `view` matrix is .isAffine() affine and has unit scaling (for example by being obtained via .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f) lookAt()),
        then this method builds the inverse of `this * view` and stores it into the given `dest`.
        
        This method can be used to quickly obtain the inverse of the combination of the view and projection matrices, when both were obtained
        via the common methods .perspective(float, float, float, float, Matrix4f) perspective() and .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f) lookAt() or
        other methods, that build affine matrices, such as .translate(float, float, float, Matrix4f) translate and .rotate(float, float, float, float, Matrix4f), except for .scale(float, float, float, Matrix4f) scale().
        
        For the special cases of the matrices `this` and `view` mentioned above, this method is equivalent to the following code:
        ```
        dest.set(this).mul(view).invert();
        ```

        Arguments
        - view: the view transformation (must be .isAffine() affine and have unit scaling)
        - dest: will hold the inverse of `this * view`

        Returns
        - dest
        """
        ...


    def invertPerspectiveView(self, view: "Matrix4x3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        If `this` is a perspective projection matrix obtained via one of the .perspective(float, float, float, float, Matrix4f) perspective() methods,
        that is, if `this` is a symmetrical perspective frustum transformation
        and the given `view` matrix has unit scaling,
        then this method builds the inverse of `this * view` and stores it into the given `dest`.
        
        This method can be used to quickly obtain the inverse of the combination of the view and projection matrices, when both were obtained
        via the common methods .perspective(float, float, float, float, Matrix4f) perspective() and .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f) lookAt() or
        other methods, that build affine matrices, such as .translate(float, float, float, Matrix4f) translate and .rotate(float, float, float, float, Matrix4f), except for .scale(float, float, float, Matrix4f) scale().
        
        For the special cases of the matrices `this` and `view` mentioned above, this method is equivalent to the following code:
        ```
        dest.set(this).mul(view).invert();
        ```

        Arguments
        - view: the view transformation (must have unit scaling)
        - dest: will hold the inverse of `this * view`

        Returns
        - dest
        """
        ...


    def invertAffine(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Invert this matrix by assuming that it is an .isAffine() affine transformation (i.e. its last row is equal to `(0, 0, 0, 1)`)
        and write the result into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Transpose this matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose3x3(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Transpose only the upper left 3x3 submatrix of this matrix and store the result in `dest`.
        
        All other matrix elements are left unchanged.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose3x3(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Transpose only the upper left 3x3 submatrix of this matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getTranslation(self, dest: "Vector3f") -> "Vector3f":
        """
        Get only the translation components `(m30, m31, m32)` of this matrix and store them in the given vector `xyz`.

        Arguments
        - dest: will hold the translation components of this matrix

        Returns
        - dest
        """
        ...


    def getScale(self, dest: "Vector3f") -> "Vector3f":
        """
        Get the scaling factors of `this` matrix for the three base axes.

        Arguments
        - dest: will hold the scaling factors for `x`, `y` and `z`

        Returns
        - dest
        """
        ...


    def get(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination
        """
        ...


    def get4x3(self, dest: "Matrix4x3f") -> "Matrix4x3f":
        """
        Get the current values of the upper 4x3 submatrix of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - Matrix4x3f.set(Matrix4fc)
        """
        ...


    def get(self, dest: "Matrix4d") -> "Matrix4d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination
        """
        ...


    def get3x3(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Get the current values of the upper left 3x3 submatrix of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - Matrix3f.set(Matrix4fc)
        """
        ...


    def get3x3(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Get the current values of the upper left 3x3 submatrix of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - Matrix3d.set(Matrix4fc)
        """
        ...


    def getRotation(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        """
        Get the rotational component of `this` matrix and store the represented rotation
        into the given AxisAngle4f.

        Arguments
        - dest: the destination AxisAngle4f

        Returns
        - the passed in destination

        See
        - AxisAngle4f.set(Matrix4fc)
        """
        ...


    def getRotation(self, dest: "AxisAngle4d") -> "AxisAngle4d":
        """
        Get the rotational component of `this` matrix and store the represented rotation
        into the given AxisAngle4d.

        Arguments
        - dest: the destination AxisAngle4d

        Returns
        - the passed in destination

        See
        - AxisAngle4f.set(Matrix4fc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the first three column vectors of the upper left 3x3 submatrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromUnnormalized(Matrix4fc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the first three column vectors of the upper left 3x3 submatrix are normalized.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromNormalized(Matrix4fc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the first three column vectors of the upper left 3x3 submatrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromUnnormalized(Matrix4fc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the first three column vectors of the upper left 3x3 submatrix are normalized.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromNormalized(Matrix4fc)
        """
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .get(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, FloatBuffer)
        """
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x3(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the upper 4x3 submatrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .get(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the upper 4x3 submatrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, FloatBuffer)
        """
        ...


    def get4x3(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the upper 4x3 submatrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of the upper 4x3 submatrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x3(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the upper 4x3 submatrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the upper 4x3 submatrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def get4x3(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the upper 4x3 submatrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of the upper 4x3 submatrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get3x4(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the left 3x4 submatrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .get3x4(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the left 3x4 submatrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get3x4(int, FloatBuffer)
        """
        ...


    def get3x4(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the left 3x4 submatrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of the left 3x4 submatrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get3x4(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the left 3x4 submatrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get3x4(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the left 3x4 submatrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get3x4(int, ByteBuffer)
        """
        ...


    def get3x4(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the left 3x4 submatrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of the left 3x4 submatrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .getTransposed(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, FloatBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .getTransposed(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, ByteBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x3Transposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the upper 4x3 submatrix of `this` matrix in row-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .get4x3Transposed(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the upper 4x3 submatrix in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get4x3Transposed(int, FloatBuffer)
        """
        ...


    def get4x3Transposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the upper 4x3 submatrix of `this` matrix in row-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of the upper 4x3 submatrix in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x3Transposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the upper 4x3 submatrix of `this` matrix in row-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get4x3Transposed(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of the upper 4x3 submatrix in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get4x3Transposed(int, ByteBuffer)
        """
        ...


    def get4x3Transposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the upper 4x3 submatrix of `this` matrix in row-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of the upper 4x3 submatrix in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Matrix4fc":
        """
        Store this matrix in column-major order at the given off-heap address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap address where to store this matrix

        Returns
        - this
        """
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        """
        Store this matrix into the supplied float array in column-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get(self, arr: list[float]) -> list[float]:
        """
        Store this matrix into the supplied float array in column-major order.
        
        In order to specify an explicit offset into the array, use the method .get(float[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get(float[], int)
        """
        ...


    def transform(self, v: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by this matrix and store the result in that vector.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector4f.mul(Matrix4fc)
        """
        ...


    def transform(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector4f.mul(Matrix4fc, Vector4f)
        """
        ...


    def transform(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the vector `(x, y, z, w)` by this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - w: the w coordinate of the vector to transform
        - dest: will contain the result

        Returns
        - dest
        """
        ...


    def transformTranspose(self, v: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by the transpose of this matrix and store the result in that vector.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector4f.mulTranspose(Matrix4fc)
        """
        ...


    def transformTranspose(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by the transpose of this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector4f.mulTranspose(Matrix4fc, Vector4f)
        """
        ...


    def transformTranspose(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the vector `(x, y, z, w)` by the transpose of this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - w: the w coordinate of the vector to transform
        - dest: will contain the result

        Returns
        - dest
        """
        ...


    def transformProject(self, v: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by this matrix, perform perspective divide and store the result in that vector.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector4f.mulProject(Matrix4fc)
        """
        ...


    def transformProject(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given vector by this matrix, perform perspective divide and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector4f.mulProject(Matrix4fc, Vector4f)
        """
        ...


    def transformProject(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the vector `(x, y, z, w)` by this matrix, perform perspective divide and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - w: the w coordinate of the vector to transform
        - dest: will contain the result

        Returns
        - dest
        """
        ...


    def transformProject(self, v: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given vector by this matrix, perform perspective divide and store the result in that vector.
        
        This method uses `w=1.0` as the fourth vector component.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector3f.mulProject(Matrix4fc)
        """
        ...


    def transformProject(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given vector by this matrix, perform perspective divide and store the result in `dest`.
        
        This method uses `w=1.0` as the fourth vector component.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector3f.mulProject(Matrix4fc, Vector3f)
        """
        ...


    def transformProject(self, v: "Vector4fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given vector by this matrix, perform perspective divide and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the `(x, y, z)` components of the result

        Returns
        - dest

        See
        - Vector4f.mulProject(Matrix4fc, Vector4f)
        """
        ...


    def transformProject(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the vector `(x, y, z)` by this matrix, perform perspective divide and store the result in `dest`.
        
        This method uses `w=1.0` as the fourth vector component.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will contain the result

        Returns
        - dest
        """
        ...


    def transformProject(self, x: float, y: float, z: float, w: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the vector `(x, y, z, w)` by this matrix, perform perspective divide and store
        `(x, y, z)` of the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - w: the w coordinate of the vector to transform
        - dest: will contain the `(x, y, z)` components of the result

        Returns
        - dest
        """
        ...


    def transformPosition(self, v: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=1, by
        this matrix and store the result in that vector.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being 1.0, so it
        will represent a position/location in 3D-space rather than a direction. This method is therefore
        not suited for perspective projection transformations as it will not save the
        `w` component of the transformed vector.
        For perspective projection use .transform(Vector4f) or .transformProject(Vector3f)
        when perspective divide should be applied, too.
        
        In order to store the result in another vector, use .transformPosition(Vector3fc, Vector3f).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transformProject(Vector3f)
        """
        ...


    def transformPosition(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=1, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being 1.0, so it
        will represent a position/location in 3D-space rather than a direction. This method is therefore
        not suited for perspective projection transformations as it will not save the
        `w` component of the transformed vector.
        For perspective projection use .transform(Vector4fc, Vector4f) or
        .transformProject(Vector3fc, Vector3f) when perspective divide should be applied, too.
        
        In order to store the result in the same vector, use .transformPosition(Vector3f).

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformProject(Vector3fc, Vector3f)
        """
        ...


    def transformPosition(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the 3D-vector `(x, y, z)`, as if it was a 4D-vector with w=1, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being 1.0, so it
        will represent a position/location in 3D-space rather than a direction. This method is therefore
        not suited for perspective projection transformations as it will not save the
        `w` component of the transformed vector.
        For perspective projection use .transform(float, float, float, float, Vector4f) or
        .transformProject(float, float, float, Vector3f) when perspective divide should be applied, too.

        Arguments
        - x: the x coordinate of the position
        - y: the y coordinate of the position
        - z: the z coordinate of the position
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformProject(float, float, float, Vector3f)
        """
        ...


    def transformDirection(self, v: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=0, by
        this matrix and store the result in that vector.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being `0.0`, so it
        will represent a direction in 3D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in another vector, use .transformDirection(Vector3fc, Vector3f).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transformDirection(Vector3fc, Vector3f)
        """
        ...


    def transformDirection(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=0, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being `0.0`, so it
        will represent a direction in 3D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in the same vector, use .transformDirection(Vector3f).

        Arguments
        - v: the vector to transform and to hold the final result
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformDirection(Vector3f)
        """
        ...


    def transformDirection(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform/multiply the given 3D-vector `(x, y, z)`, as if it was a 4D-vector with w=0, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being `0.0`, so it
        will represent a direction in 3D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.

        Arguments
        - x: the x coordinate of the direction to transform
        - y: the y coordinate of the direction to transform
        - z: the z coordinate of the direction to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformAffine(self, v: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given 4D-vector by assuming that `this` matrix represents an .isAffine() affine transformation
        (i.e. its last row is equal to `(0, 0, 0, 1)`).
        
        In order to store the result in another vector, use .transformAffine(Vector4fc, Vector4f).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transformAffine(Vector4fc, Vector4f)
        """
        ...


    def transformAffine(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the given 4D-vector by assuming that `this` matrix represents an .isAffine() affine transformation
        (i.e. its last row is equal to `(0, 0, 0, 1)`) and store the result in `dest`.
        
        In order to store the result in the same vector, use .transformAffine(Vector4f).

        Arguments
        - v: the vector to transform and to hold the final result
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformAffine(Vector4f)
        """
        ...


    def transformAffine(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform/multiply the 4D-vector `(x, y, z, w)` by assuming that `this` matrix represents an .isAffine() affine transformation
        (i.e. its last row is equal to `(0, 0, 0, 1)`) and store the result in `dest`.

        Arguments
        - x: the x coordinate of the direction to transform
        - y: the y coordinate of the direction to transform
        - z: the z coordinate of the direction to transform
        - w: the w coordinate of the direction to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xyz: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given `xyz.x`,
        `xyz.y` and `xyz.z` factors, respectively and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xyz: the factors of the x, y and z component, respectively
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xyz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given `xyz` factor
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        Individual scaling of all three axes can be applied using .scale(float, float, float, Matrix4f).

        Arguments
        - xyz: the factor for all components
        - dest: will hold the result

        Returns
        - dest

        See
        - .scale(float, float, float, Matrix4f)
        """
        ...


    def scaleXY(self, x: float, y: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to this matrix by by scaling the X axis by `x` and the Y axis by `y`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given x,
        y and z factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAround(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given sx,
        sy and sz factors while using `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).scale(sx, sy, sz).translate(-ox, -oy, -oz)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - sz: the scaling factor of the z component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply scaling to this matrix by scaling all three base axes by the given `factor`
        while using `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).scale(factor).translate(-ox, -oy, -oz)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def scaleLocal(self, xyz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply scaling to `this` matrix by scaling all base axes by the given `xyz` factor,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!

        Arguments
        - xyz: the factor to scale all three base axes by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleLocal(self, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given x,
        y and z factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAroundLocal(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given sx,
        sy and sz factors while using the given `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix4f().translate(ox, oy, oz).scale(sx, sy, sz).translate(-ox, -oy, -oz).mul(this, dest)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - sz: the scaling factor of the z component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAroundLocal(self, factor: float, ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply scaling to this matrix by scaling all three base axes by the given `factor`
        while using `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix4f().translate(ox, oy, oz).scale(factor).translate(-ox, -oy, -oz).mul(this, dest)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def rotateX(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation about the X axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateY(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation about the Y axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZ(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation about the Z axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTowardsXY(self, dirX: float, dirY: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation about the Z axis to align the local `+X` towards `(dirX, dirY)` and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        The vector `(dirX, dirY)` must be a unit vector.

        Arguments
        - dirX: the x component of the normalized direction
        - dirY: the y component of the normalized direction
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleX` radians about the X axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateX(angleX, dest).rotateY(angleY).rotateZ(angleZ)`

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAffineXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleX` radians about the X axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method assumes that `this` matrix represents an .isAffine() affine transformation (i.e. its last row is equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrix only represents affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleZ` radians about the Z axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleX` radians about the X axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateZ(angleZ, dest).rotateY(angleY).rotateX(angleX)`

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAffineZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleZ` radians about the Z axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleX` radians about the X axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method assumes that `this` matrix represents an .isAffine() affine transformation (i.e. its last row is equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrix only represents affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleY` radians about the Y axis, followed by a rotation of `angleX` radians about the X axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateY(angleY, dest).rotateX(angleX).rotateZ(angleZ)`

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAffineYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation of `angleY` radians about the Y axis, followed by a rotation of `angleX` radians about the X axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method assumes that `this` matrix represents an .isAffine() affine transformation (i.e. its last row is equal to `(0, 0, 0, 1)`)
        and can be used to speed up matrix multiplication if the matrix only represents affine transformations, such as translation, rotation, scaling and shearing (in any combination).
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, ang: float, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTranslation(self, ang: float, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation to this matrix, which is assumed to only contain a translation, by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        This method assumes `this` to only contain a translation.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAffine(self, ang: float, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply rotation to this .isAffine() affine matrix by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        This method assumes `this` to be .isAffine() affine.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocal(self, ang: float, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalX(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a rotation around the X axis to this matrix by rotating the given amount of radians
        about the X axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalY(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a rotation around the Y axis to this matrix by rotating the given amount of radians
        about the Y axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalZ(self, ang: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a rotation around the Z axis to this matrix by rotating the given amount of radians
        about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def translate(self, offset: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def translate(self, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def translateLocal(self, offset: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def translateLocal(self, x: float, y: float, z: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .ortho(float, float, float, float, float, float, boolean, Matrix4f) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .ortho(float, float, float, float, float, float, Matrix4f) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(float, float, float, float, float, float, boolean, Matrix4f) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(float, float, float, float, float, float, Matrix4f) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def ortho2D(self, left: float, right: float, bottom: float, top: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system to this matrix
        and store the result in `dest`.
        
        This method is equivalent to calling .ortho(float, float, float, float, float, float, Matrix4f) ortho() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - dest: will hold the result

        Returns
        - dest

        See
        - .ortho(float, float, float, float, float, float, Matrix4f)
        """
        ...


    def ortho2DLH(self, left: float, right: float, bottom: float, top: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an orthographic projection transformation for a left-handed coordinate system to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(float, float, float, float, float, float, Matrix4f) orthoLH() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - dest: will hold the result

        Returns
        - dest

        See
        - .orthoLH(float, float, float, float, float, float, Matrix4f)
        """
        ...


    def lookAlong(self, dir: "Vector3fc", up: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(Vector3fc, Vector3fc, Vector3fc, Matrix4f) lookAt
        with `eye = (0, 0, 0)` and `center = dir`.

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(Vector3fc, Vector3fc, Vector3fc, Matrix4f)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f) lookAt()
        with `eye = (0, 0, 0)` and `center = dir`.

        Arguments
        - dirX: the x-coordinate of the direction to look along
        - dirY: the y-coordinate of the direction to look along
        - dirZ: the z-coordinate of the direction to look along
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f)
        """
        ...


    def lookAt(self, eye: "Vector3fc", center: "Vector3fc", up: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f)
        """
        ...


    def lookAt(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(Vector3fc, Vector3fc, Vector3fc, Matrix4f)
        """
        ...


    def lookAtPerspective(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye` and store the result in `dest`.
        
        This method assumes `this` to be a perspective transformation, obtained via
        .frustum(float, float, float, float, float, float, Matrix4f) frustum() or .perspective(float, float, float, float, Matrix4f) perspective() or
        one of their overloads.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lookAtLH(self, eye: "Vector3fc", center: "Vector3fc", up: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAtLH(float, float, float, float, float, float, float, float, float, Matrix4f)
        """
        ...


    def lookAtLH(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAtLH(Vector3fc, Vector3fc, Vector3fc, Matrix4f)
        """
        ...


    def lookAtPerspectiveLH(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye` and store the result in `dest`.
        
        This method assumes `this` to be a perspective transformation, obtained via
        .frustumLH(float, float, float, float, float, float, Matrix4f) frustumLH() or .perspectiveLH(float, float, float, float, Matrix4f) perspectiveLH() or
        one of their overloads.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def tile(self, x: int, y: int, w: int, h: int, dest: "Matrix4f") -> "Matrix4f":
        """
        This method is equivalent to calling: `translate(w-1-2*x, h-1-2*y, 0, dest).scale(w, h, 1)`
        
        If `M` is `this` matrix and `T` the created transformation matrix,
        then the new matrix will be `M * T`. So when transforming a
        vector `v` with the new matrix by using `M * T * v`, the
        created transformation will be applied first!

        Arguments
        - x: the tile's x coordinate/index (should be in `[0..w)`)
        - y: the tile's y coordinate/index (should be in `[0..h)`)
        - w: the number of tiles along the x axis
        - h: the number of tiles along the y axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspective(self, fovy: float, aspect: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest
        """
        ...


    def perspective(self, fovy: float, aspect: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveRect(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - width: the width of the near frustum plane
        - height: the height of the near frustum plane
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest
        """
        ...


    def perspectiveRect(self, width: float, height: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - width: the width of the near frustum plane
        - height: the height of the near frustum plane
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveOffCenter(self, fovy: float, offAngleX: float, offAngleY: float, aspect: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        The given angles `offAngleX` and `offAngleY` are the horizontal and vertical angles between
        the line of sight and the line given by the center of the near and far frustum planes. So, when `offAngleY`
        is just `fovy/2` then the projection frustum is rotated towards +Y and the bottom frustum plane 
        is parallel to the XZ-plane.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - offAngleX: the horizontal angle between the line of sight and the line crossing the center of the near and far frustum planes
        - offAngleY: the vertical angle between the line of sight and the line crossing the center of the near and far frustum planes
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest
        """
        ...


    def perspectiveOffCenter(self, fovy: float, offAngleX: float, offAngleY: float, aspect: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        The given angles `offAngleX` and `offAngleY` are the horizontal and vertical angles between
        the line of sight and the line given by the center of the near and far frustum planes. So, when `offAngleY`
        is just `fovy/2` then the projection frustum is rotated towards +Y and the bottom frustum plane 
        is parallel to the XZ-plane.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - offAngleX: the horizontal angle between the line of sight and the line crossing the center of the near and far frustum planes
        - offAngleY: the vertical angle between the line of sight and the line crossing the center of the near and far frustum planes
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveOffCenterFov(self, angleLeft: float, angleRight: float, angleDown: float, angleUp: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        The given angles `angleLeft` and `angleRight` are the horizontal angles between
        the left and right frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        The angles `angleDown` and `angleUp` are the vertical angles between
        the bottom and top frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - angleLeft: the horizontal angle between left frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleRight: the horizontal angle between right frustum plane and a line perpendicular to the near/far frustum planes
        - angleDown: the vertical angle between bottom frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleUp: the vertical angle between top frustum plane and a line perpendicular to the near/far frustum planes
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveOffCenterFov(self, angleLeft: float, angleRight: float, angleDown: float, angleUp: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        The given angles `angleLeft` and `angleRight` are the horizontal angles between
        the left and right frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        The angles `angleDown` and `angleUp` are the vertical angles between
        the bottom and top frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - angleLeft: the horizontal angle between left frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleRight: the horizontal angle between right frustum plane and a line perpendicular to the near/far frustum planes
        - angleDown: the vertical angle between bottom frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleUp: the vertical angle between top frustum plane and a line perpendicular to the near/far frustum planes
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveOffCenterFovLH(self, angleLeft: float, angleRight: float, angleDown: float, angleUp: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a left-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        The given angles `angleLeft` and `angleRight` are the horizontal angles between
        the left and right frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        The angles `angleDown` and `angleUp` are the vertical angles between
        the bottom and top frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - angleLeft: the horizontal angle between left frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleRight: the horizontal angle between right frustum plane and a line perpendicular to the near/far frustum planes
        - angleDown: the vertical angle between bottom frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleUp: the vertical angle between top frustum plane and a line perpendicular to the near/far frustum planes
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveOffCenterFovLH(self, angleLeft: float, angleRight: float, angleDown: float, angleUp: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an asymmetric off-center perspective projection frustum transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        The given angles `angleLeft` and `angleRight` are the horizontal angles between
        the left and right frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        The angles `angleDown` and `angleUp` are the vertical angles between
        the bottom and top frustum planes, respectively, and a line perpendicular to the near and far frustum planes.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - angleLeft: the horizontal angle between left frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleRight: the horizontal angle between right frustum plane and a line perpendicular to the near/far frustum planes
        - angleDown: the vertical angle between bottom frustum plane and a line perpendicular to the near/far frustum planes.
                   For a symmetric frustum, this value is negative.
        - angleUp: the vertical angle between top frustum plane and a line perpendicular to the near/far frustum planes
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveLH(self, fovy: float, aspect: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a left-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def perspectiveLH(self, fovy: float, aspect: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a symmetric perspective projection frustum transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `P` the perspective projection matrix,
        then the new matrix will be `M * P`. So when transforming a
        vector `v` with the new matrix by using `M * P * v`,
        the perspective projection will be applied first!

        Arguments
        - fovy: the vertical field of view in radians (must be greater than zero and less than Math.PI PI)
        - aspect: the aspect ratio (i.e. width / height; must be greater than zero)
        - zNear: near clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustum(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arbitrary perspective projection frustum transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `F` the frustum matrix,
        then the new matrix will be `M * F`. So when transforming a
        vector `v` with the new matrix by using `M * F * v`,
        the frustum transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#perspective">http://www.songho.ca</a>

        Arguments
        - left: the distance along the x-axis to the left frustum edge
        - right: the distance along the x-axis to the right frustum edge
        - bottom: the distance along the y-axis to the bottom frustum edge
        - top: the distance along the y-axis to the top frustum edge
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustum(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arbitrary perspective projection frustum transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `F` the frustum matrix,
        then the new matrix will be `M * F`. So when transforming a
        vector `v` with the new matrix by using `M * F * v`,
        the frustum transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#perspective">http://www.songho.ca</a>

        Arguments
        - left: the distance along the x-axis to the left frustum edge
        - right: the distance along the x-axis to the right frustum edge
        - bottom: the distance along the y-axis to the bottom frustum edge
        - top: the distance along the y-axis to the top frustum edge
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustumLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arbitrary perspective projection frustum transformation for a left-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `F` the frustum matrix,
        then the new matrix will be `M * F`. So when transforming a
        vector `v` with the new matrix by using `M * F * v`,
        the frustum transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#perspective">http://www.songho.ca</a>

        Arguments
        - left: the distance along the x-axis to the left frustum edge
        - right: the distance along the x-axis to the right frustum edge
        - bottom: the distance along the y-axis to the bottom frustum edge
        - top: the distance along the y-axis to the top frustum edge
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustumLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arbitrary perspective projection frustum transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `F` the frustum matrix,
        then the new matrix will be `M * F`. So when transforming a
        vector `v` with the new matrix by using `M * F * v`,
        the frustum transformation will be applied first!
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#perspective">http://www.songho.ca</a>

        Arguments
        - left: the distance along the x-axis to the left frustum edge
        - right: the distance along the x-axis to the right frustum edge
        - bottom: the distance along the y-axis to the bottom frustum edge
        - top: the distance along the y-axis to the top frustum edge
        - zNear: near clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the near clipping plane will be at positive infinity.
                   In that case, `zFar` may not also be Float.POSITIVE_INFINITY.
        - zFar: far clipping plane distance. This value must be greater than zero.
                   If the special value Float.POSITIVE_INFINITY is used, the far clipping plane will be at positive infinity.
                   In that case, `zNear` may not also be Float.POSITIVE_INFINITY.
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, quat: "Quaternionfc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAffine(self, quat: "Quaternionfc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this .isAffine() affine matrix and store
        the result in `dest`.
        
        This method assumes `this` to be .isAffine() affine.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTranslation(self, quat: "Quaternionfc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply the rotation - and possibly scaling - ransformation of the given Quaternionfc to this matrix, which is assumed to only contain a translation, and store
        the result in `dest`.
        
        This method assumes `this` to only contain a translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAroundAffine(self, quat: "Quaternionfc", ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this .isAffine() affine
        matrix while using `(ox, oy, oz)` as the rotation origin, and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        This method is only applicable if `this` is an .isAffine() affine matrix.
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).rotate(quat).translate(-ox, -oy, -oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAround(self, quat: "Quaternionfc", ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix while using `(ox, oy, oz)` as the rotation origin,
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).rotate(quat).translate(-ox, -oy, -oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocal(self, quat: "Quaternionfc", dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAroundLocal(self, quat: "Quaternionfc", ox: float, oy: float, oz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Pre-multiply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix while using `(ox, oy, oz)`
        as the rotation origin, and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        This method is equivalent to calling: `translateLocal(-ox, -oy, -oz, dest).rotateLocal(quat).translateLocal(ox, oy, oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4f", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given AxisAngle4f,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the AxisAngle4f rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(float, float, float, float, Matrix4f)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis and store the result in `dest`.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given axis-angle,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the axis-angle rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3fc.normalize(Vector3f) normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(float, float, float, float, Matrix4f)
        """
        ...


    def unproject(self, winX: float, winY: float, winZ: float, viewport: list[int], dest: "Vector4f") -> "Vector4f":
        """
        Unproject the given window coordinates `(winX, winY, winZ)` by `this` matrix using the specified viewport.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        The depth range of `winZ` is assumed to be `[0..1]`, which is also the OpenGL default.
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInv(float, float, float, int[], Vector4f) unprojectInv() can be invoked on it.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - winZ: the z-coordinate, which is the depth value in `[0..1]`
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .invert(Matrix4f)
        """
        ...


    def unproject(self, winX: float, winY: float, winZ: float, viewport: list[int], dest: "Vector3f") -> "Vector3f":
        """
        Unproject the given window coordinates `(winX, winY, winZ)` by `this` matrix using the specified viewport.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        The depth range of `winZ` is assumed to be `[0..1]`, which is also the OpenGL default.
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInv(float, float, float, int[], Vector3f) unprojectInv() can be invoked on it.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - winZ: the z-coordinate, which is the depth value in `[0..1]`
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .invert(Matrix4f)
        """
        ...


    def unproject(self, winCoords: "Vector3fc", viewport: list[int], dest: "Vector4f") -> "Vector4f":
        """
        Unproject the given window coordinates `winCoords` by `this` matrix using the specified viewport.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        The depth range of `winCoords.z` is assumed to be `[0..1]`, which is also the OpenGL default.
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInv(float, float, float, int[], Vector4f) unprojectInv() can be invoked on it.

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .invert(Matrix4f)
        """
        ...


    def unproject(self, winCoords: "Vector3fc", viewport: list[int], dest: "Vector3f") -> "Vector3f":
        """
        Unproject the given window coordinates `winCoords` by `this` matrix using the specified viewport.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        The depth range of `winCoords.z` is assumed to be `[0..1]`, which is also the OpenGL default.
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInv(float, float, float, int[], Vector3f) unprojectInv() can be invoked on it.

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .invert(Matrix4f)
        """
        ...


    def unprojectRay(self, winX: float, winY: float, viewport: list[int], originDest: "Vector3f", dirDest: "Vector3f") -> "Matrix4f":
        """
        Unproject the given 2D window coordinates `(winX, winY)` by `this` matrix using the specified viewport
        and compute the origin and the direction of the resulting ray which starts at NDC `z = -1.0` and goes through NDC `z = +1.0`.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInvRay(float, float, int[], Vector3f, Vector3f) unprojectInvRay() can be invoked on it.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - viewport: the viewport described by `[x, y, width, height]`
        - originDest: will hold the ray origin
        - dirDest: will hold the (unnormalized) ray direction

        Returns
        - this

        See
        - .invert(Matrix4f)
        """
        ...


    def unprojectRay(self, winCoords: "Vector2fc", viewport: list[int], originDest: "Vector3f", dirDest: "Vector3f") -> "Matrix4f":
        """
        Unproject the given 2D window coordinates `winCoords` by `this` matrix using the specified viewport
        and compute the origin and the direction of the resulting ray which starts at NDC `z = -1.0` and goes through NDC `z = +1.0`.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix4f) and then the method .unprojectInvRay(float, float, int[], Vector3f, Vector3f) unprojectInvRay() can be invoked on it.

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - originDest: will hold the ray origin
        - dirDest: will hold the (unnormalized) ray direction

        Returns
        - this

        See
        - .invert(Matrix4f)
        """
        ...


    def unprojectInv(self, winCoords: "Vector3fc", viewport: list[int], dest: "Vector4f") -> "Vector4f":
        """
        Unproject the given window coordinates `winCoords` by `this` matrix using the specified viewport.
        
        This method differs from .unproject(Vector3fc, int[], Vector4f) unproject() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.
        
        The depth range of `winCoords.z` is assumed to be `[0..1]`, which is also the OpenGL default.
        
        This method reads the four viewport parameters from the given int[].

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .unproject(Vector3fc, int[], Vector4f)
        """
        ...


    def unprojectInv(self, winX: float, winY: float, winZ: float, viewport: list[int], dest: "Vector4f") -> "Vector4f":
        """
        Unproject the given window coordinates `(winX, winY, winZ)` by `this` matrix using the specified viewport.
        
        This method differs from .unproject(float, float, float, int[], Vector4f) unproject() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.
        
        The depth range of `winZ` is assumed to be `[0..1]`, which is also the OpenGL default.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - winZ: the z-coordinate, which is the depth value in `[0..1]`
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .unproject(float, float, float, int[], Vector4f)
        """
        ...


    def unprojectInvRay(self, winCoords: "Vector2fc", viewport: list[int], originDest: "Vector3f", dirDest: "Vector3f") -> "Matrix4f":
        """
        Unproject the given window coordinates `winCoords` by `this` matrix using the specified viewport
        and compute the origin and the direction of the resulting ray which starts at NDC `z = -1.0` and goes through NDC `z = +1.0`.
        
        This method differs from .unprojectRay(Vector2fc, int[], Vector3f, Vector3f) unprojectRay() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - originDest: will hold the ray origin
        - dirDest: will hold the (unnormalized) ray direction

        Returns
        - this

        See
        - .unprojectRay(Vector2fc, int[], Vector3f, Vector3f)
        """
        ...


    def unprojectInvRay(self, winX: float, winY: float, viewport: list[int], originDest: "Vector3f", dirDest: "Vector3f") -> "Matrix4f":
        """
        Unproject the given 2D window coordinates `(winX, winY)` by `this` matrix using the specified viewport
        and compute the origin and the direction of the resulting ray which starts at NDC `z = -1.0` and goes through NDC `z = +1.0`.
        
        This method differs from .unprojectRay(float, float, int[], Vector3f, Vector3f) unprojectRay() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - viewport: the viewport described by `[x, y, width, height]`
        - originDest: will hold the ray origin
        - dirDest: will hold the (unnormalized) ray direction

        Returns
        - this

        See
        - .unprojectRay(float, float, int[], Vector3f, Vector3f)
        """
        ...


    def unprojectInv(self, winCoords: "Vector3fc", viewport: list[int], dest: "Vector3f") -> "Vector3f":
        """
        Unproject the given window coordinates `winCoords` by `this` matrix using the specified viewport.
        
        This method differs from .unproject(Vector3fc, int[], Vector3f) unproject() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.
        
        The depth range of `winCoords.z` is assumed to be `[0..1]`, which is also the OpenGL default.

        Arguments
        - winCoords: the window coordinates to unproject
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .unproject(Vector3fc, int[], Vector3f)
        """
        ...


    def unprojectInv(self, winX: float, winY: float, winZ: float, viewport: list[int], dest: "Vector3f") -> "Vector3f":
        """
        Unproject the given window coordinates `(winX, winY, winZ)` by `this` matrix using the specified viewport.
        
        This method differs from .unproject(float, float, float, int[], Vector3f) unproject() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.
        
        The depth range of `winZ` is assumed to be `[0..1]`, which is also the OpenGL default.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - winZ: the z-coordinate, which is the depth value in `[0..1]`
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .unproject(float, float, float, int[], Vector3f)
        """
        ...


    def project(self, x: float, y: float, z: float, viewport: list[int], winCoordsDest: "Vector4f") -> "Vector4f":
        """
        Project the given `(x, y, z)` position via `this` matrix using the specified viewport
        and store the resulting window coordinates in `winCoordsDest`.
        
        This method transforms the given coordinates by `this` matrix including perspective division to 
        obtain normalized device coordinates, and then translates these into window coordinates by using the
        given `viewport` settings `[x, y, width, height]`.
        
        The depth range of the returned `winCoordsDest.z` will be `[0..1]`, which is also the OpenGL default.

        Arguments
        - x: the x-coordinate of the position to project
        - y: the y-coordinate of the position to project
        - z: the z-coordinate of the position to project
        - viewport: the viewport described by `[x, y, width, height]`
        - winCoordsDest: will hold the projected window coordinates

        Returns
        - winCoordsDest
        """
        ...


    def project(self, x: float, y: float, z: float, viewport: list[int], winCoordsDest: "Vector3f") -> "Vector3f":
        """
        Project the given `(x, y, z)` position via `this` matrix using the specified viewport
        and store the resulting window coordinates in `winCoordsDest`.
        
        This method transforms the given coordinates by `this` matrix including perspective division to 
        obtain normalized device coordinates, and then translates these into window coordinates by using the
        given `viewport` settings `[x, y, width, height]`.
        
        The depth range of the returned `winCoordsDest.z` will be `[0..1]`, which is also the OpenGL default.

        Arguments
        - x: the x-coordinate of the position to project
        - y: the y-coordinate of the position to project
        - z: the z-coordinate of the position to project
        - viewport: the viewport described by `[x, y, width, height]`
        - winCoordsDest: will hold the projected window coordinates

        Returns
        - winCoordsDest
        """
        ...


    def project(self, position: "Vector3fc", viewport: list[int], winCoordsDest: "Vector4f") -> "Vector4f":
        """
        Project the given `position` via `this` matrix using the specified viewport
        and store the resulting window coordinates in `winCoordsDest`.
        
        This method transforms the given coordinates by `this` matrix including perspective division to 
        obtain normalized device coordinates, and then translates these into window coordinates by using the
        given `viewport` settings `[x, y, width, height]`.
        
        The depth range of the returned `winCoordsDest.z` will be `[0..1]`, which is also the OpenGL default.

        Arguments
        - position: the position to project into window coordinates
        - viewport: the viewport described by `[x, y, width, height]`
        - winCoordsDest: will hold the projected window coordinates

        Returns
        - winCoordsDest

        See
        - .project(float, float, float, int[], Vector4f)
        """
        ...


    def project(self, position: "Vector3fc", viewport: list[int], winCoordsDest: "Vector3f") -> "Vector3f":
        """
        Project the given `position` via `this` matrix using the specified viewport
        and store the resulting window coordinates in `winCoordsDest`.
        
        This method transforms the given coordinates by `this` matrix including perspective division to 
        obtain normalized device coordinates, and then translates these into window coordinates by using the
        given `viewport` settings `[x, y, width, height]`.
        
        The depth range of the returned `winCoordsDest.z` will be `[0..1]`, which is also the OpenGL default.

        Arguments
        - position: the position to project into window coordinates
        - viewport: the viewport described by `[x, y, width, height]`
        - winCoordsDest: will hold the projected window coordinates

        Returns
        - winCoordsDest

        See
        - .project(float, float, float, int[], Vector4f)
        """
        ...


    def reflect(self, a: float, b: float, c: float, d: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the equation `x*a + y*b + z*c + d = 0` and store the result in `dest`.
        
        The vector `(a, b, c)` must be a unit vector.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!
        
        Reference: <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/bb281733(v=vs.85).aspx">msdn.microsoft.com</a>

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, nx: float, ny: float, nz: float, px: float, py: float, pz: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal
        - px: the x-coordinate of a point on the plane
        - py: the y-coordinate of a point on the plane
        - pz: the z-coordinate of a point on the plane
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, orientation: "Quaternionfc", point: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about a plane
        specified via the plane orientation and a point on the plane, and store the result in `dest`.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaternionfc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`, offset by the given `point`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - orientation: the plane orientation relative to an implied normal vector of `(0, 0, 1)`
        - point: a point on the plane
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, normal: "Vector3fc", point: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - normal: the plane normal
        - point: a point on the plane
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getRow(self, row: int, dest: "Vector4f") -> "Vector4f":
        """
        Get the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..3]`
        - dest: will hold the row components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..3]`
        """
        ...


    def getRow(self, row: int, dest: "Vector3f") -> "Vector3f":
        """
        Get the first three components of the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..3]`
        - dest: will hold the first three row components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..3]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector4f") -> "Vector4f":
        """
        Get the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..3]`
        - dest: will hold the column components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..3]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector3f") -> "Vector3f":
        """
        Get the first three components of the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..3]`
        - dest: will hold the first three column components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..3]`
        """
        ...


    def get(self, column: int, row: int) -> float:
        """
        Get the matrix element value at the given column and row.

        Arguments
        - column: the colum index in `[0..3]`
        - row: the row index in `[0..3]`

        Returns
        - the element value
        """
        ...


    def getRowColumn(self, row: int, column: int) -> float:
        """
        Get the matrix element value at the given row and column.

        Arguments
        - row: the row index in `[0..3]`
        - column: the colum index in `[0..3]`

        Returns
        - the element value
        """
        ...


    def normal(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Compute a normal matrix from the upper left 3x3 submatrix of `this`
        and store it into the upper left 3x3 submatrix of `dest`.
        All other values of `dest` will be set to identity.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normal(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Compute a normal matrix from the upper left 3x3 submatrix of `this`
        and store it into `dest`.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .get3x3(Matrix3f)
        """
        ...


    def cofactor3x3(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Compute the cofactor matrix of the upper left 3x3 submatrix of `this`
        and store it into `dest`.
        
        The cofactor matrix can be used instead of .normal(Matrix3f) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def cofactor3x3(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Compute the cofactor matrix of the upper left 3x3 submatrix of `this`
        and store it into `dest`.
        All other values of `dest` will be set to identity.
        
        The cofactor matrix can be used instead of .normal(Matrix4f) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3x3(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Normalize the upper left 3x3 submatrix of this matrix and store the result in `dest`.
        
        The resulting matrix will map unit vectors to unit vectors, though a pair of orthogonal input unit
        vectors need not be mapped to a pair of orthogonal output vectors if the original matrix was not orthogonal itself
        (i.e. had *skewing*).

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3x3(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Normalize the upper left 3x3 submatrix of this matrix and store the result in `dest`.
        
        The resulting matrix will map unit vectors to unit vectors, though a pair of orthogonal input unit
        vectors need not be mapped to a pair of orthogonal output vectors if the original matrix was not orthogonal itself
        (i.e. had *skewing*).

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustumPlane(self, plane: int, planeEquation: "Vector4f") -> "Vector4f":
        """
        Calculate a frustum plane of `this` matrix, which
        can be a projection matrix or a combined modelview-projection matrix, and store the result
        in the given `planeEquation`.
        
        Generally, this method computes the frustum plane in the local frame of
        any coordinate system that existed before `this`
        transformation was applied to it in order to yield homogeneous clipping space.
        
        The frustum plane will be given in the form of a general plane equation:
        `a*x + b*y + c*z + d = 0`, where the given Vector4f components will
        hold the `(a, b, c, d)` values of the equation.
        
        The plane normal, which is `(a, b, c)`, is directed "inwards" of the frustum.
        Any plane/point test using `a*x + b*y + c*z + d` therefore will yield a result greater than zero
        if the point is within the frustum (i.e. at the *positive* side of the frustum plane).
        
        For performing frustum culling, the class FrustumIntersection should be used instead of 
        manually obtaining the frustum planes and testing them against points, spheres or axis-aligned boxes.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - plane: one of the six possible planes, given as numeric constants
                 .PLANE_NX, .PLANE_PX,
                 .PLANE_NY, .PLANE_PY,
                 .PLANE_NZ and .PLANE_PZ
        - planeEquation: will hold the computed plane equation.
                 The plane equation will be normalized, meaning that `(a, b, c)` will be a unit vector

        Returns
        - planeEquation
        """
        ...


    def frustumCorner(self, corner: int, point: "Vector3f") -> "Vector3f":
        """
        Compute the corner coordinates of the frustum defined by `this` matrix, which
        can be a projection matrix or a combined modelview-projection matrix, and store the result
        in the given `point`.
        
        Generally, this method computes the frustum corners in the local frame of
        any coordinate system that existed before `this`
        transformation was applied to it in order to yield homogeneous clipping space.
        
        Reference: <a href="http://geomalgorithms.com/a05-_intersect-1.html">http://geomalgorithms.com</a>
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - corner: one of the eight possible corners, given as numeric constants
                 .CORNER_NXNYNZ, .CORNER_PXNYNZ, .CORNER_PXPYNZ, .CORNER_NXPYNZ,
                 .CORNER_PXNYPZ, .CORNER_NXNYPZ, .CORNER_NXPYPZ, .CORNER_PXPYPZ
        - point: will hold the resulting corner point coordinates

        Returns
        - point
        """
        ...


    def perspectiveOrigin(self, origin: "Vector3f") -> "Vector3f":
        """
        Compute the eye/origin of the perspective frustum transformation defined by `this` matrix, 
        which can be a projection matrix or a combined modelview-projection matrix, and store the result
        in the given `origin`.
        
        Note that this method will only work using perspective projections obtained via one of the
        perspective methods, such as .perspective(float, float, float, float, Matrix4f) perspective()
        or .frustum(float, float, float, float, float, float, Matrix4f) frustum().
        
        Generally, this method computes the origin in the local frame of
        any coordinate system that existed before `this`
        transformation was applied to it in order to yield homogeneous clipping space.
        
        This method is equivalent to calling: `invert(new Matrix4f()).transformProject(0, 0, -1, 0, origin)`
        and in the case of an already available inverse of `this` matrix, the method .perspectiveInvOrigin(Vector3f)
        on the inverse of the matrix should be used instead.
        
        Reference: <a href="http://geomalgorithms.com/a05-_intersect-1.html">http://geomalgorithms.com</a>
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - origin: will hold the origin of the coordinate system before applying `this`
                 perspective projection transformation

        Returns
        - origin
        """
        ...


    def perspectiveInvOrigin(self, dest: "Vector3f") -> "Vector3f":
        """
        Compute the eye/origin of the inverse of the perspective frustum transformation defined by `this` matrix, 
        which can be the inverse of a projection matrix or the inverse of a combined modelview-projection matrix, and store the result
        in the given `dest`.
        
        Note that this method will only work using perspective projections obtained via one of the
        perspective methods, such as .perspective(float, float, float, float, Matrix4f) perspective()
        or .frustum(float, float, float, float, float, float, Matrix4f) frustum().
        
        If the inverse of the modelview-projection matrix is not available, then calling .perspectiveOrigin(Vector3f)
        on the original modelview-projection matrix is preferred.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .perspectiveOrigin(Vector3f)
        """
        ...


    def perspectiveFov(self) -> float:
        """
        Return the vertical field-of-view angle in radians of this perspective transformation matrix.
        
        Note that this method will only work using perspective projections obtained via one of the
        perspective methods, such as .perspective(float, float, float, float, Matrix4f) perspective()
        or .frustum(float, float, float, float, float, float, Matrix4f) frustum().
        
        For orthogonal transformations this method will return `0.0`.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Returns
        - the vertical field-of-view angle in radians
        """
        ...


    def perspectiveNear(self) -> float:
        """
        Extract the near clip plane distance from `this` perspective projection matrix.
        
        This method only works if `this` is a perspective projection matrix, for example obtained via .perspective(float, float, float, float, Matrix4f).

        Returns
        - the near clip plane distance
        """
        ...


    def perspectiveFar(self) -> float:
        """
        Extract the far clip plane distance from `this` perspective projection matrix.
        
        This method only works if `this` is a perspective projection matrix, for example obtained via .perspective(float, float, float, float, Matrix4f).

        Returns
        - the far clip plane distance
        """
        ...


    def frustumRayDir(self, x: float, y: float, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of a ray starting at the center of the coordinate system and going 
        through the near frustum plane.
        
        This method computes the `dir` vector in the local frame of
        any coordinate system that existed before `this`
        transformation was applied to it in order to yield homogeneous clipping space.
        
        The parameters `x` and `y` are used to interpolate the generated ray direction
        from the bottom-left to the top-right frustum corners.
        
        For optimal efficiency when building many ray directions over the whole frustum,
        it is recommended to use this method only in order to compute the four corner rays at
        `(0, 0)`, `(1, 0)`, `(0, 1)` and `(1, 1)`
        and then bilinearly interpolating between them; or to use the FrustumRayBuilder.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - x: the interpolation factor along the left-to-right frustum planes, within `[0..1]`
        - y: the interpolation factor along the bottom-to-top frustum planes, within `[0..1]`
        - dir: will hold the normalized ray direction in the local frame of the coordinate system before 
                 transforming to homogeneous clipping space using `this` matrix

        Returns
        - dir
        """
        ...


    def positiveZ(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+Z` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+Z` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).invert();
        inv.transformDirection(dir.set(0, 0, 1)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveZ(Vector3f) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def normalizedPositiveZ(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+Z` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+Z` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).transpose();
        inv.transformDirection(dir.set(0, 0, 1));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def positiveX(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+X` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).invert();
        inv.transformDirection(dir.set(1, 0, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveX(Vector3f) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def normalizedPositiveX(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+X` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).transpose();
        inv.transformDirection(dir.set(1, 0, 0));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def positiveY(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).invert();
        inv.transformDirection(dir.set(0, 1, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveY(Vector3f) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def normalizedPositiveY(self, dir: "Vector3f") -> "Vector3f":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the upper left 3x3 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).transpose();
        inv.transformDirection(dir.set(0, 1, 0));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def originAffine(self, origin: "Vector3f") -> "Vector3f":
        """
        Obtain the position that gets transformed to the origin by `this` .isAffine() affine matrix.
        This can be used to get the position of the "camera" from a given *view* transformation matrix.
        
        This method only works with .isAffine() affine matrices.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).invertAffine();
        inv.transformPosition(origin.set(0, 0, 0));
        ```

        Arguments
        - origin: will hold the position transformed to the origin

        Returns
        - origin
        """
        ...


    def origin(self, origin: "Vector3f") -> "Vector3f":
        """
        Obtain the position that gets transformed to the origin by `this` matrix.
        This can be used to get the position of the "camera" from a given *view/projection* transformation matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4f inv = new Matrix4f(this).invert();
        inv.transformPosition(origin.set(0, 0, 0));
        ```

        Arguments
        - origin: will hold the position transformed to the origin

        Returns
        - origin
        """
        ...


    def shadow(self, light: "Vector4f", a: float, b: float, c: float, d: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `light`
        and store the result in `dest`.
        
        If `light.w` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!
        
        Reference: <a href="ftp://ftp.sgi.com/opengl/contrib/blythe/advanced99/notes/node192.html">ftp.sgi.com</a>

        Arguments
        - light: the light's vector
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, a: float, b: float, c: float, d: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`
        and store the result in `dest`.
        
        If `lightW` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!
        
        Reference: <a href="ftp://ftp.sgi.com/opengl/contrib/blythe/advanced99/notes/node192.html">ftp.sgi.com</a>

        Arguments
        - lightX: the x-component of the light's vector
        - lightY: the y-component of the light's vector
        - lightZ: the z-component of the light's vector
        - lightW: the w-component of the light's vector
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, light: "Vector4f", planeTransform: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `light`
        and store the result in `dest`.
        
        Before the shadow projection is applied, the plane is transformed via the specified `planeTransformation`.
        
        If `light.w` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!

        Arguments
        - light: the light's vector
        - planeTransform: the transformation to transform the implied plane `y = 0` before applying the projection
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, planeTransform: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`
        and store the result in `dest`.
        
        Before the shadow projection is applied, the plane is transformed via the specified `planeTransformation`.
        
        If `lightW` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!

        Arguments
        - lightX: the x-component of the light vector
        - lightY: the y-component of the light vector
        - lightZ: the z-component of the light vector
        - lightW: the w-component of the light vector
        - planeTransform: the transformation to transform the implied plane `y = 0` before applying the projection
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def pick(self, x: float, y: float, width: float, height: float, viewport: list[int], dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a picking transformation to this matrix using the given window coordinates `(x, y)` as the pick center
        and the given `(width, height)` as the size of the picking region in window coordinates, and store the result
        in `dest`.

        Arguments
        - x: the x coordinate of the picking region center in window coordinates
        - y: the y coordinate of the picking region center in window coordinates
        - width: the width of the picking region in window coordinates
        - height: the height of the picking region in window coordinates
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def isAffine(self) -> bool:
        """
        Determine whether this matrix describes an affine transformation. This is the case iff its last row is equal to `(0, 0, 0, 1)`.

        Returns
        - `True` iff this matrix is affine; `False` otherwise
        """
        ...


    def arcball(self, radius: float, centerX: float, centerY: float, centerZ: float, angleX: float, angleY: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and center `(centerX, centerY, centerZ)`
        position of the arcball and the specified X and Y rotation angles, and store the result in `dest`.
        
        This method is equivalent to calling: `translate(0, 0, -radius, dest).rotateX(angleX).rotateY(angleY).translate(-centerX, -centerY, -centerZ)`

        Arguments
        - radius: the arcball radius
        - centerX: the x coordinate of the center position of the arcball
        - centerY: the y coordinate of the center position of the arcball
        - centerZ: the z coordinate of the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def arcball(self, radius: float, center: "Vector3fc", angleX: float, angleY: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and `center`
        position of the arcball and the specified X and Y rotation angles, and store the result in `dest`.
        
        This method is equivalent to calling: `translate(0, 0, -radius).rotateX(angleX).rotateY(angleY).translate(-center.x, -center.y, -center.z)`

        Arguments
        - radius: the arcball radius
        - center: the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def frustumAabb(self, min: "Vector3f", max: "Vector3f") -> "Matrix4f":
        """
        Compute the axis-aligned bounding box of the frustum described by `this` matrix and store the minimum corner
        coordinates in the given `min` and the maximum corner coordinates in the given `max` vector.
        
        The matrix `this` is assumed to be the .invert(Matrix4f) inverse of the origial view-projection matrix
        for which to compute the axis-aligned bounding box in world-space.
        
        The axis-aligned bounding box of the unit frustum is `(-1, -1, -1)`, `(1, 1, 1)`.

        Arguments
        - min: will hold the minimum corner coordinates of the axis-aligned bounding box
        - max: will hold the maximum corner coordinates of the axis-aligned bounding box

        Returns
        - this
        """
        ...


    def projectedGridRange(self, projector: "Matrix4fc", sLower: float, sUpper: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Compute the *range matrix* for the Projected Grid transformation as described in chapter "2.4.2 Creating the range conversion matrix"
        of the paper <a href="http://fileadmin.cs.lth.se/graphics/theses/projects/projgrid/projgrid-lq.pdf">Real-time water rendering - Introducing the projected grid concept</a>
        based on the *inverse* of the view-projection matrix which is assumed to be `this`, and store that range matrix into `dest`.
        
        If the projected grid will not be visible then this method returns `null`.
        
        This method uses the `y = 0` plane for the projection.

        Arguments
        - projector: the projector view-projection transformation
        - sLower: the lower (smallest) Y-coordinate which any transformed vertex might have while still being visible on the projected grid
        - sUpper: the upper (highest) Y-coordinate which any transformed vertex might have while still being visible on the projected grid
        - dest: will hold the resulting range matrix

        Returns
        - the computed range matrix; or `null` if the projected grid will not be visible
        """
        ...


    def perspectiveFrustumSlice(self, near: float, far: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Change the near and far clip plane distances of `this` perspective frustum transformation matrix
        and store the result in `dest`.
        
        This method only works if `this` is a perspective projection frustum transformation, for example obtained
        via .perspective(float, float, float, float, Matrix4f) perspective() or .frustum(float, float, float, float, float, float, Matrix4f) frustum().

        Arguments
        - near: the new near clip plane distance
        - far: the new far clip plane distance
        - dest: will hold the resulting matrix

        Returns
        - dest

        See
        - .frustum(float, float, float, float, float, float, Matrix4f)
        """
        ...


    def orthoCrop(self, view: "Matrix4fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Build an ortographic projection transformation that fits the view-projection transformation represented by `this`
        into the given affine `view` transformation.
        
        The transformation represented by `this` must be given as the .invert(Matrix4f) inverse of a typical combined camera view-projection
        transformation, whose projection can be either orthographic or perspective.
        
        The `view` must be an .isAffine() affine transformation which in the application of Cascaded Shadow Maps is usually the light view transformation.
        It be obtained via any affine transformation or for example via .lookAt(float, float, float, float, float, float, float, float, float, Matrix4f) lookAt().
        
        Reference: <a href="http://developer.download.nvidia.com/SDK/10.5/opengl/screenshots/samples/cascaded_shadow_maps.html">OpenGL SDK - Cascaded Shadow Maps</a>

        Arguments
        - view: the view transformation to build a corresponding orthographic projection to fit the frustum of `this`
        - dest: will hold the crop projection transformation

        Returns
        - dest
        """
        ...


    def transformAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, outMin: "Vector3f", outMax: "Vector3f") -> "Matrix4f":
        """
        Transform the axis-aligned box given as the minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`
        by `this` .isAffine() affine matrix and compute the axis-aligned box of the result whose minimum corner is stored in `outMin`
        and maximum corner stored in `outMax`.
        
        Reference: <a href="http://dev.theomader.com/transform-bounding-boxes/">http://dev.theomader.com</a>

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the y coordinate of the maximum corner of the axis-aligned box
        - outMin: will hold the minimum corner of the resulting axis-aligned box
        - outMax: will hold the maximum corner of the resulting axis-aligned box

        Returns
        - this
        """
        ...


    def transformAab(self, min: "Vector3fc", max: "Vector3fc", outMin: "Vector3f", outMax: "Vector3f") -> "Matrix4f":
        """
        Transform the axis-aligned box given as the minimum corner `min` and maximum corner `max`
        by `this` .isAffine() affine matrix and compute the axis-aligned box of the result whose minimum corner is stored in `outMin`
        and maximum corner stored in `outMax`.

        Arguments
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - outMin: will hold the minimum corner of the resulting axis-aligned box
        - outMax: will hold the maximum corner of the resulting axis-aligned box

        Returns
        - this
        """
        ...


    def lerp(self, other: "Matrix4fc", t: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `dest`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other matrix
        - t: the interpolation factor between 0.0 and 1.0
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTowards(self, dir: "Vector3fc", up: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `dir`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        This method is equivalent to calling: `mulAffine(new Matrix4f().lookAt(new Vector3f(), new Vector3f(dir).negate(), up).invertAffine(), dest)`

        Arguments
        - dir: the direction to rotate towards
        - up: the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateTowards(float, float, float, float, float, float, Matrix4f)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `(dirX, dirY, dirZ)`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        This method is equivalent to calling: `mulAffine(new Matrix4f().lookAt(0, 0, 0, -dirX, -dirY, -dirZ, upX, upY, upZ).invertAffine(), dest)`

        Arguments
        - dirX: the x-coordinate of the direction to rotate towards
        - dirY: the y-coordinate of the direction to rotate towards
        - dirZ: the z-coordinate of the direction to rotate towards
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateTowards(Vector3fc, Vector3fc, Matrix4f)
        """
        ...


    def getEulerAnglesXYZ(self, dest: "Vector3f") -> "Vector3f":
        """
        Extract the Euler angles from the rotation represented by the upper left 3x3 submatrix of `this`
        and store the extracted Euler angles in `dest`.
        
        This method assumes that the upper left of `this` only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3f.x field, the angle around Y in the Vector3f.y
        field and the angle around Z in the Vector3f.z field of the supplied Vector3f instance.
        
        Note that the returned Euler angles must be applied in the order `X * Y * Z` to obtain the identical matrix.
        This means that calling Matrix4fc.rotateXYZ(float, float, float, Matrix4f) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix4f m = ...; // &lt;- matrix only representing rotation
        Matrix4f n = new Matrix4f();
        n.rotateXYZ(m.getEulerAnglesXYZ(new Vector3f()));
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">http://en.wikipedia.org/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
        """
        ...


    def getEulerAnglesZYX(self, dest: "Vector3f") -> "Vector3f":
        """
        Extract the Euler angles from the rotation represented by the upper left 3x3 submatrix of `this`
        and store the extracted Euler angles in `dest`.
        
        This method assumes that the upper left of `this` only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3f.x field, the angle around Y in the Vector3f.y
        field and the angle around Z in the Vector3f.z field of the supplied Vector3f instance.
        
        Note that the returned Euler angles must be applied in the order `Z * Y * X` to obtain the identical matrix.
        This means that calling Matrix4fc.rotateZYX(float, float, float, Matrix4f) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix4f m = ...; // &lt;- matrix only representing rotation
        Matrix4f n = new Matrix4f();
        n.rotateZYX(m.getEulerAnglesZYX(new Vector3f()));
        ```
        
        Reference: <a href="http://nghiaho.com/?page_id=846">http://nghiaho.com/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
        """
        ...


    def testPoint(self, x: float, y: float, z: float) -> bool:
        """
        Test whether the given point `(x, y, z)` is within the frustum defined by `this` matrix.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given point with the coordinates `(x, y, z)` given
        in space `M` is within the clip space.
        
        When testing multiple points using the same transformation matrix, FrustumIntersection should be used instead.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - x: the x-coordinate of the point
        - y: the y-coordinate of the point
        - z: the z-coordinate of the point

        Returns
        - `True` if the given point is inside the frustum; `False` otherwise
        """
        ...


    def testSphere(self, x: float, y: float, z: float, r: float) -> bool:
        """
        Test whether the given sphere is partly or completely within or outside of the frustum defined by `this` matrix.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given sphere with the coordinates `(x, y, z)` given
        in space `M` is within the clip space.
        
        When testing multiple spheres using the same transformation matrix, or more sophisticated/optimized intersection algorithms are required,
        FrustumIntersection should be used instead.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for spheres that are actually not visible.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - x: the x-coordinate of the sphere's center
        - y: the y-coordinate of the sphere's center
        - z: the z-coordinate of the sphere's center
        - r: the sphere's radius

        Returns
        - `True` if the given sphere is partly or completely inside the frustum; `False` otherwise
        """
        ...


    def testAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """
        Test whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` matrix.
        The box is specified via its min and max corner coordinates.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given axis-aligned box with its minimum corner coordinates `(minX, minY, minZ)`
        and maximum corner coordinates `(maxX, maxY, maxZ)` given in space `M` is within the clip space.
        
        When testing multiple axis-aligned boxes using the same transformation matrix, or more sophisticated/optimized intersection algorithms are required,
        FrustumIntersection should be used instead.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `-1` for boxes that are actually not visible/do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner

        Returns
        - `True` if the axis-aligned box is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def obliqueZ(self, a: float, b: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply an oblique projection transformation to this matrix with the given values for `a` and
        `b` and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the oblique transformation matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        oblique transformation will be applied first!
        
        The oblique transformation is defined as:
        ```
        x' = x + a*z
        y' = y + a*z
        z' = z
        ```
        or in matrix form:
        ```
        1 0 a 0
        0 1 b 0
        0 0 1 0
        0 0 0 1
        ```

        Arguments
        - a: the value for the z factor that applies to x
        - b: the value for the z factor that applies to y
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def withLookAtUp(self, up: "Vector3fc", dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a transformation to this matrix to ensure that the local Y axis (as obtained by .positiveY(Vector3f))
        will be coplanar to the plane spanned by the local Z axis (as obtained by .positiveZ(Vector3f)) and the
        given vector `up`, and store the result in `dest`.
        
        This effectively ensures that the resulting matrix will be equal to the one obtained from calling
        Matrix4f.setLookAt(Vector3fc, Vector3fc, Vector3fc) with the current 
        local origin of this matrix (as obtained by .originAffine(Vector3f)), the sum of this position and the 
        negated local Z axis as well as the given vector `up`.
        
        This method must only be called on .isAffine() matrices.

        Arguments
        - up: the up vector
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def withLookAtUp(self, upX: float, upY: float, upZ: float, dest: "Matrix4f") -> "Matrix4f":
        """
        Apply a transformation to this matrix to ensure that the local Y axis (as obtained by .positiveY(Vector3f))
        will be coplanar to the plane spanned by the local Z axis (as obtained by .positiveZ(Vector3f)) and the
        given vector `(upX, upY, upZ)`, and store the result in `dest`.
        
        This effectively ensures that the resulting matrix will be equal to the one obtained from calling
        Matrix4f.setLookAt(float, float, float, float, float, float, float, float, float) called with the current 
        local origin of this matrix (as obtained by .originAffine(Vector3f)), the sum of this position and the 
        negated local Z axis as well as the given vector `(upX, upY, upZ)`.
        
        This method must only be called on .isAffine() matrices.

        Arguments
        - upX: the x coordinate of the up vector
        - upY: the y coordinate of the up vector
        - upZ: the z coordinate of the up vector
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def mapXZY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1 0 0 0
        0 0 1 0
        0 1 0 0
        0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXZnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 0 -1 0
        0 1  0 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnYnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0 -1  0 0
        0  0 -1 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0  0 1 0
        0 -1 0 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0  0 -1 0
        0 -1  0 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        1 0 0 0
        0 0 1 0
        0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        1 0  0 0
        0 0 -1 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        1 0 0 0
        0 1 0 0
        0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        1 0  0 0
        0 1  0 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        1  0 0 0
        0  0 1 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        1  0  0 0
        0  0 -1 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        1  0 0 0
        0 -1 0 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        1  0  0 0
        0 -1  0 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        0 0 1 0
        1 0 0 0
        0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        0 0 -1 0
        1 0  0 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        0 1 0 0
        1 0 0 0
        0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        0 1  0 0
        1 0  0 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        0  0 1 0
        1  0 0 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        0  0 -1 0
        1  0  0 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        0 -1 0 0
        1  0 0 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        0 -1  0 0
        1  0  0 0
        0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXYnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 1  0 0
         0 0 -1 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 0 1 0
         0 1 0 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 0 -1 0
         0 1  0 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0 -1 0 0
         0  0 1 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0 -1  0 0
         0  0 -1 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0  0 1 0
         0 -1 0 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0  0 -1 0
         0 -1  0 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
        -1 0 0 0
         0 0 1 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
        -1 0  0 0
         0 0 -1 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
        -1 0 0 0
         0 1 0 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
        -1 0  0 0
         0 1  0 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
        -1  0 0 0
         0  0 1 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXnZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
        -1  0  0 0
         0  0 -1 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
        -1  0 0 0
         0 -1 0 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
        -1  0  0 0
         0 -1  0 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
         0 0 1 0
        -1 0 0 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
         0 0 -1 0
        -1 0  0 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
         0 1 0 0
        -1 0 0 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
         0 1  0 0
        -1 0  0 0
         0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
         0  0 1 0
        -1  0 0 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXnY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
         0  0 -1 0
        -1  0  0 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
         0 -1 0 0
        -1  0 0 0
         0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYnX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
         0 -1  0 0
        -1  0  0 0
         0  0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateX(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 1 0 0
         0 0 1 0
         0 0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateY(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0 -1 0 0
        0  0 1 0
        0  0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateZ(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 1  0 0
        0 0 -1 0
        0 0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, m: "Matrix4fc", delta: float) -> bool:
        """
        Compare the matrix elements of `this` matrix with the given matrix using the given `delta`
        and return whether all of them are equal within a maximum difference of `delta`.
        
        Please note that this method is not used by any data structure such as ArrayList HashSet or HashMap
        and their operations, such as ArrayList.contains(Object) or HashSet.remove(Object), since those
        data structures only use the Object.equals(Object) and Object.hashCode() methods.

        Arguments
        - m: the other matrix
        - delta: the allowed maximum difference

        Returns
        - `True` whether all of the matrix elements are equal; `False` otherwise
        """
        ...


    def isFinite(self) -> bool:
        """
        Determine whether all matrix elements are finite floating-point values, that
        is, they are not Float.isNaN() NaN and not
        Float.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...
