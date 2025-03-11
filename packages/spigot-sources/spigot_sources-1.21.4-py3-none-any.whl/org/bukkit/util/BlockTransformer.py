"""
Python module generated from Java source file org.bukkit.util.BlockTransformer

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.generator import LimitedRegion
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class BlockTransformer:
    """
    A BlockTransformer is used to modify blocks that are placed by structure.
    """

    def transform(self, region: "LimitedRegion", x: int, y: int, z: int, current: "BlockState", state: "TransformationState") -> "BlockState":
        """
        Transforms a block in a structure.
        
        NOTE: The usage of BlockData.createBlockState() can provide even
        more flexibility to return the exact block state you might want to
        return.

        Arguments
        - region: the accessible region
        - x: the x position of the block
        - y: the y position of the block
        - z: the z position of the block
        - current: the state of the block that should be placed
        - state: the state of this transformation.

        Returns
        - the new block state
        """
        ...


    class TransformationState:
        """
        The TransformationState allows access to the original block state and the
        block state of the block that was at the location of the transformation
        in the world before the transformation started.
        """

        def getOriginal(self) -> "BlockState":
            """
            Creates a clone of the original block state that a structure wanted
            to place and caches it for the current transformer.

            Returns
            - a clone of the original block state.
            """
            ...


        def getWorld(self) -> "BlockState":
            """
            Creates a clone of the block state that was at the location of the
            currently modified block at the start of the transformation process
            and caches it for the current transformer.

            Returns
            - a clone of the world block state.
            """
            ...
