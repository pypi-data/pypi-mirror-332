"""
Python module generated from Java source file org.bukkit.inventory.meta.components.ToolComponent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import Tag
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components import *
from typing import Any, Callable, Iterable, Tuple


class ToolComponent(ConfigurationSerializable):
    """
    Represents a component which can turn any item into a tool.
    """

    def getDefaultMiningSpeed(self) -> float:
        """
        Get the default mining speed of this tool. This value is used by the tool
        if no rule explicitly overrides it. 1.0 is standard mining speed.

        Returns
        - the default mining speed

        See
        - ToolRule.getSpeed()
        """
        ...


    def setDefaultMiningSpeed(self, speed: float) -> None:
        """
        Set the default mining speed of this tool. This value is used by the tool
        if no rule explicitly overrides it. 1.0 is standard mining speed.

        Arguments
        - speed: the speed to set
        """
        ...


    def getDamagePerBlock(self) -> int:
        """
        Get the amount of durability to be removed from the tool each time a
        block is broken.

        Returns
        - the damage per block
        """
        ...


    def setDamagePerBlock(self, damage: int) -> None:
        """
        Set the amount of durability to be removed from the tool each time a
        block is broken.

        Arguments
        - damage: the damage to set. Must be 0 or a positive integer
        """
        ...


    def getRules(self) -> list["ToolRule"]:
        """
        Get the list of ToolRule ToolRules that apply to this tool.

        Returns
        - all tool rules. The mutability of the returned list cannot be
        guaranteed, but its contents are mutable and can have their values
        changed
        """
        ...


    def setRules(self, rules: list["ToolRule"]) -> None:
        """
        Set the list of ToolRule ToolRules to apply to this tool. This
        will remove any existing tool rules.

        Arguments
        - rules: the rules to set
        """
        ...


    def addRule(self, block: "Material", speed: "Float", correctForDrops: "Boolean") -> "ToolRule":
        """
        Add a new rule to this tool component, which provides further information
        about a specific block type.

        Arguments
        - block: the block type to which the rule applies
        - speed: the mining speed to use when mining the block, or null to
        use the default mining speed
        - correctForDrops: whether or not this tool, when mining the block,
        is considered the optimal tool for the block and will drop its items when
        broken, or null to use the default tool checking behavior defined by
        Minecraft

        Returns
        - the ToolRule instance that was added to this tool
        """
        ...


    def addRule(self, blocks: Iterable["Material"], speed: "Float", correctForDrops: "Boolean") -> "ToolRule":
        """
        Add a new rule to this tool component, which provides further information
        about a collection of block types.

        Arguments
        - blocks: the block types to which the rule applies
        - speed: the mining speed to use when mining one of the blocks, or
        null to use the default mining speed
        - correctForDrops: whether or not this tool, when mining one of the
        blocks, is considered the optimal tool for the block and will drop its
        items when broken, or null to use the default tool checking behavior
        defined by Minecraft

        Returns
        - the ToolRule instance that was added to this tool
        """
        ...


    def addRule(self, tag: "Tag"["Material"], speed: "Float", correctForDrops: "Boolean") -> "ToolRule":
        """
        Add a new rule to this tool component, which provides further information
        about a collection of block types represented by a block Tag.

        Arguments
        - tag: the block tag containing block types to which the rule
        applies.
        - speed: the mining speed to use when mining one of the blocks, or
        null to use the default mining speed
        - correctForDrops: whether or not this tool, when mining one of the
        blocks, is considered the optimal tool for the block and will drop its
        items when broken, or null to use the default tool checking behavior
        defined by Minecraft

        Returns
        - the ToolRule instance that was added to this tool

        Raises
        - IllegalArgumentException: if the passed `tag` is not a block
        tag
        """
        ...


    def removeRule(self, rule: "ToolRule") -> bool:
        """
        Remove the given ToolRule from this tool.

        Arguments
        - rule: the rule to remove

        Returns
        - True if the rule was removed, False if this component did not
        contain a matching rule
        """
        ...


    class ToolRule(ConfigurationSerializable):
        """
        A rule governing use of this tool and overriding attributes per-block.
        """

        def getBlocks(self) -> Iterable["Material"]:
            """
            Get a collection of the block types to which this tool rule applies.

            Returns
            - the blocks
            """
            ...


        def setBlocks(self, block: "Material") -> None:
            """
            Set the block type to which this rule applies.

            Arguments
            - block: the block type
            """
            ...


        def setBlocks(self, blocks: Iterable["Material"]) -> None:
            """
            Set the block types to which this rule applies.

            Arguments
            - blocks: the block types
            """
            ...


        def setBlocks(self, tag: "Tag"["Material"]) -> None:
            """
            Set the block types (represented as a block Tag) to which
            this rule applies.

            Arguments
            - tag: the block tag

            Raises
            - IllegalArgumentException: if the passed `tag` is not a
            block tag
            """
            ...


        def getSpeed(self) -> "Float":
            """
            Get the mining speed of this rule. If non-null, this speed value is
            used in lieu of the default speed value of the tool. 1.0 is standard
            mining speed.

            Returns
            - the mining speed, or null if the default speed is used
            """
            ...


        def setSpeed(self, speed: "Float") -> None:
            """
            Set the mining speed of this rule. 1.0 is standard mining speed.

            Arguments
            - speed: the mining speed, or null to use the default speed
            """
            ...


        def isCorrectForDrops(self) -> "Boolean":
            """
            Get whether or not this rule is considered the optimal tool for the
            blocks listed by this rule and will drop items. If non-null, this
            value is used in lieu of the default tool checking behavior defined
            by Minecraft.

            Returns
            - True if correct for drops, False otherwise, or null to
            fallback to vanilla tool checking behavior
            """
            ...


        def setCorrectForDrops(self, correct: "Boolean") -> None:
            """
            Set whether or not this rule is considered the optimal tool for the
            blocks listed by this rule and will drop items.

            Arguments
            - correct: whether or not this rule is correct for drops, or null
            to fallback to vanilla tool checking behavior
            """
            ...
