"""
Python module generated from Java source file org.bukkit.inventory.RecipeChoice

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Arrays
from java.util import Collections
from java.util import Objects
from java.util.function import Predicate
from org.bukkit import Material
from org.bukkit import Tag
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class RecipeChoice(Predicate, Cloneable):
    """
    Represents a potential item match within a recipe. All choices within a
    recipe must be satisfied for it to be craftable.
    
    **This class is not legal for implementation by plugins!**
    """

    def getItemStack(self) -> "ItemStack":
        """
        Gets a single item stack representative of this stack choice.

        Returns
        - a single representative item

        Deprecated
        - for compatibility only
        """
        ...


    def clone(self) -> "RecipeChoice":
        ...


    def test(self, itemStack: "ItemStack") -> bool:
        ...


    class MaterialChoice(RecipeChoice):
        """
        Represents a choice of multiple matching Materials.
        """

        def __init__(self, choice: "Material"):
            ...


        def __init__(self, *choices: Tuple["Material", ...]):
            ...


        def __init__(self, choices: "Tag"["Material"]):
            """
            Constructs a MaterialChoice with the current values of the specified
            tag.

            Arguments
            - choices: the tag
            """
            ...


        def __init__(self, choices: list["Material"]):
            ...


        def test(self, t: "ItemStack") -> bool:
            ...


        def getItemStack(self) -> "ItemStack":
            ...


        def getChoices(self) -> list["Material"]:
            ...


        def clone(self) -> "MaterialChoice":
            ...


        def hashCode(self) -> int:
            ...


        def equals(self, obj: "Object") -> bool:
            ...


        def toString(self) -> str:
            ...


    class ExactChoice(RecipeChoice):
        """
        Represents a choice that will be valid only one of the stacks is exactly
        matched (aside from stack size).
        
        **Only valid for shaped recipes**
        """

        def __init__(self, stack: "ItemStack"):
            ...


        def __init__(self, *stacks: Tuple["ItemStack", ...]):
            ...


        def __init__(self, choices: list["ItemStack"]):
            ...


        def getItemStack(self) -> "ItemStack":
            ...


        def getChoices(self) -> list["ItemStack"]:
            ...


        def clone(self) -> "ExactChoice":
            ...


        def test(self, t: "ItemStack") -> bool:
            ...


        def hashCode(self) -> int:
            ...


        def equals(self, obj: "Object") -> bool:
            ...


        def toString(self) -> str:
            ...
