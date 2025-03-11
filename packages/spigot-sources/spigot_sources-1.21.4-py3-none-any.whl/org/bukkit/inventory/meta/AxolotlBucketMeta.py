"""
Python module generated from Java source file org.bukkit.inventory.meta.AxolotlBucketMeta

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Axolotl
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class AxolotlBucketMeta(ItemMeta):
    """
    Represents a bucket of axolotl.
    """

    def getVariant(self) -> "Axolotl.Variant":
        """
        Get the variant of the axolotl in the bucket.
        
        Plugins should check that hasVariant() returns `True` before
        calling this method.

        Returns
        - axolotl variant
        """
        ...


    def setVariant(self, variant: "Axolotl.Variant") -> None:
        """
        Set the variant of this axolotl in the bucket.

        Arguments
        - variant: axolotl variant
        """
        ...


    def hasVariant(self) -> bool:
        """
        Checks for existence of a variant tag indicating a specific axolotl will be
        spawned.

        Returns
        - if there is a variant
        """
        ...


    def clone(self) -> "AxolotlBucketMeta":
        ...
