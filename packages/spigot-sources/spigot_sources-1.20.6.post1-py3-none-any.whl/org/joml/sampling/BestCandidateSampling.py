"""
Python module generated from Java source file org.joml.sampling.BestCandidateSampling

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Random
from org.joml import Vector2f
from org.joml import Vector3f
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class BestCandidateSampling:
    """
    Creates samples using the "Best Candidate" algorithm.

    Author(s)
    - Kai Burjack
    """

    class Sphere:
        """
        Generates Best Candidate samples on a unit sphere.
        
        References:
        
        - <a href="https://arxiv.org/ftp/cs/papers/0701/0701164.pdf">Indexing the Sphere with the Hierarchical Triangular Mesh</a>
        - <a href="http://math.stackexchange.com/questions/1244512/point-in-a-spherical-triangle-test">Point in a spherical triangle test</a>

    Author(s)
        - Kai Burjack
        """

        def __init__(self):
            """
            Create a new instance of Sphere to configure and generate 'best candidate' sample positions on the unit sphere.
            """
            ...


        def generate(self, xyzs: list[float]) -> "Sphere":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xyzs` float array.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xyzs: will hold the x, y and z coordinates of all samples in the order `XYZXYZXYZ...`.
                       This array must have a length of at least `numSamples`

            Returns
            - this
            """
            ...


        def generate(self, xyzs: "FloatBuffer") -> "Sphere":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xyzs` FloatBuffer.
            
            The samples will be written starting at the current position of the FloatBuffer. The position of the FloatBuffer will not be modified.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xyzs: will hold the x, y and z coordinates of all samples in the order `XYZXYZXYZ...`.
                       This FloatBuffer must have at least `numSamples` remaining elements.
                       The position of the buffer will not be modified by this method

            Returns
            - this
            """
            ...


        def seed(self, seed: int) -> "Sphere":
            """
            Set the seed to initialize the pseudo-random number generator with.

            Arguments
            - seed: the seed value

            Returns
            - this
            """
            ...


        def numSamples(self, numSamples: int) -> "Sphere":
            """
            Set the number of samples to generate.

            Arguments
            - numSamples: the number of samples

            Returns
            - this
            """
            ...


        def numCandidates(self, numCandidates: int) -> "Sphere":
            """
            Set the number of candidates to try for each generated sample.

            Arguments
            - numCandidates: the number of candidates to try

            Returns
            - this
            """
            ...


        def onHemisphere(self, onHemisphere: bool) -> "Sphere":
            """
            Set whether to generate samples on a hemisphere around the `+Z` axis.
            
            The default is `False`, which will generate samples on the whole unit sphere.

            Arguments
            - onHemisphere: whether to generate samples on the hemisphere

            Returns
            - this
            """
            ...


        def generate(self, callback: "Callback3d") -> "Sphere":
            """
            Generate 'best candidate' sample call the given `callback` for each generated sample.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - callback: will be called with the coordinates of each generated sample position

            Returns
            - this
            """
            ...


    class Disk:
        """
        Generates Best Candidate samples on a unit disk.

    Author(s)
        - Kai Burjack
        """

        def __init__(self):
            """
            Create a new instance of Disk to configure and generate 'best candidate' sample positions on the unit disk.
            """
            ...


        def seed(self, seed: int) -> "Disk":
            """
            Set the seed to initialize the pseudo-random number generator with.

            Arguments
            - seed: the seed value

            Returns
            - this
            """
            ...


        def numSamples(self, numSamples: int) -> "Disk":
            """
            Set the number of samples to generate.

            Arguments
            - numSamples: the number of samples

            Returns
            - this
            """
            ...


        def numCandidates(self, numCandidates: int) -> "Disk":
            """
            Set the number of candidates to try for each generated sample.

            Arguments
            - numCandidates: the number of candidates to try

            Returns
            - this
            """
            ...


        def generate(self, xys: list[float]) -> "Disk":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xys` float array.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xys: will hold the x and y coordinates of all samples in the order `XYXYXY...`.
                       This array must have a length of at least `numSamples`

            Returns
            - this
            """
            ...


        def generate(self, xys: "FloatBuffer") -> "Disk":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xys` FloatBuffer.
            
            The samples will be written starting at the current position of the FloatBuffer. The position of the FloatBuffer will not be modified.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xys: will hold the x and y coordinates of all samples in the order `XYXYXY...`. This FloatBuffer must have at least `numSamples` remaining elements. The
                       position of the buffer will not be modified by this method

            Returns
            - this
            """
            ...


        def generate(self, callback: "Callback2d") -> "Disk":
            """
            Generate 'best candidate' sample positions and call the given `callback` for each generated sample.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - callback: will be called with the coordinates of each generated sample position

            Returns
            - this
            """
            ...


    class Quad:
        """
        Generates Best Candidate samples on a unit quad.

    Author(s)
        - Kai Burjack
        """

        def __init__(self):
            """
            Create a new instance of Quad to configure and generate 'best candidate' sample positions on the unit quad.
            """
            ...


        def seed(self, seed: int) -> "Quad":
            """
            Set the seed to initialize the pseudo-random number generator with.

            Arguments
            - seed: the seed value

            Returns
            - this
            """
            ...


        def numSamples(self, numSamples: int) -> "Quad":
            """
            Set the number of samples to generate.

            Arguments
            - numSamples: the number of samples

            Returns
            - this
            """
            ...


        def numCandidates(self, numCandidates: int) -> "Quad":
            """
            Set the number of candidates to try for each generated sample.

            Arguments
            - numCandidates: the number of candidates to try

            Returns
            - this
            """
            ...


        def generate(self, xyzs: list[float]) -> "Quad":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xyzs` float array.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xyzs: will hold the x, y and z coordinates of all samples in the order `XYZXYZXYZ...`.
                       This array must have a length of at least `numSamples`

            Returns
            - this
            """
            ...


        def generate(self, xys: "FloatBuffer") -> "Quad":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xys` FloatBuffer.
            
            The samples will be written starting at the current position of the FloatBuffer. The position of the FloatBuffer will not be modified.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xys: will hold the x and y coordinates of all samples in the order `XYXYXY...`. This FloatBuffer must have at least `numSamples` remaining elements. The position of
                       the buffer will not be modified by this method

            Returns
            - this
            """
            ...


        def generate(self, callback: "Callback2d") -> "Quad":
            """
            Generate 'best candidate' sample positions and call the given `callback` for each generated sample.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - callback: will be called with the coordinates of each generated sample position

            Returns
            - this
            """
            ...


    class Cube:
        """
        Generates Best Candidate samples inside a unit cube.

    Author(s)
        - Kai Burjack
        """

        def __init__(self):
            """
            Create a new instance of Cube to configure and generate 'best candidate' sample positions
            on the unit cube with each sample tried `numCandidates` number of times, and call the 
            given `callback` for each sample generate.
            """
            ...


        def seed(self, seed: int) -> "Cube":
            """
            Set the seed to initialize the pseudo-random number generator with.

            Arguments
            - seed: the seed value

            Returns
            - this
            """
            ...


        def numSamples(self, numSamples: int) -> "Cube":
            """
            Set the number of samples to generate.

            Arguments
            - numSamples: the number of samples

            Returns
            - this
            """
            ...


        def numCandidates(self, numCandidates: int) -> "Cube":
            """
            Set the number of candidates to try for each generated sample.

            Arguments
            - numCandidates: the number of candidates to try

            Returns
            - this
            """
            ...


        def generate(self, xyzs: list[float]) -> "Cube":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xyzs` float array.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xyzs: will hold the x, y and z coordinates of all samples in the order `XYZXYZXYZ...`.
                       This array must have a length of at least `numSamples`

            Returns
            - this
            """
            ...


        def generate(self, xyzs: "FloatBuffer") -> "Cube":
            """
            Generate 'best candidate' sample positions and store the coordinates of all generated samples into the given `xyzs` FloatBuffer.
            
            The samples will be written starting at the current position of the FloatBuffer. The position of the FloatBuffer will not be modified.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - xyzs: will hold the x, y and z coordinates of all samples in the order `XYZXYZXYZ...`.
                       This FloatBuffer must have at least `numSamples` remaining elements.
                       The position of the buffer will not be modified by this method

            Returns
            - this
            """
            ...


        def generate(self, callback: "Callback3d") -> "Cube":
            """
            Generate 'best candidate' sample positions and call the given `callback` for each generated sample.
            
            *This method performs heap allocations, so should be used sparingly.*

            Arguments
            - callback: will be called with the coordinates of each generated sample position

            Returns
            - this
            """
            ...
