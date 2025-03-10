"""
Python module generated from Java source file org.bukkit.attribute.AttributeModifier

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Objects
from java.util import UUID
from org.apache.commons.lang import Validate
from org.bukkit.attribute import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.util import NumberConversions
from typing import Any, Callable, Iterable, Tuple


class AttributeModifier(ConfigurationSerializable):
    """
    Concrete implementation of an attribute modifier.
    """

    def __init__(self, name: str, amount: float, operation: "Operation"):
        ...


    def __init__(self, uuid: "UUID", name: str, amount: float, operation: "Operation"):
        ...


    def __init__(self, uuid: "UUID", name: str, amount: float, operation: "Operation", slot: "EquipmentSlot"):
        ...


    def getUniqueId(self) -> "UUID":
        """
        Get the unique ID for this modifier.

        Returns
        - unique id
        """
        ...


    def getName(self) -> str:
        """
        Get the name of this modifier.

        Returns
        - name
        """
        ...


    def getAmount(self) -> float:
        """
        Get the amount by which this modifier will apply its Operation.

        Returns
        - modification amount
        """
        ...


    def getOperation(self) -> "Operation":
        """
        Get the operation this modifier will apply.

        Returns
        - operation
        """
        ...


    def getSlot(self) -> "EquipmentSlot":
        """
        Get the EquipmentSlot this AttributeModifier is active on,
        or null if this modifier is applicable for any slot.

        Returns
        - the slot
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    def equals(self, other: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "AttributeModifier":
        ...


    class Operation(Enum):
        """
        Enumerable operation to be applied.
        """

        ADD_NUMBER = 0
        """
        Adds (or subtracts) the specified amount to the base value.
        """
        ADD_SCALAR = 1
        """
        Adds this scalar of amount to the base value.
        """
        MULTIPLY_SCALAR_1 = 2
        """
        Multiply amount by this value, after adding 1 to it.
        """
