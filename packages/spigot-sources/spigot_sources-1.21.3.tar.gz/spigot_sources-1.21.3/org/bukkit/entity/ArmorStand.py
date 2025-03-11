"""
Python module generated from Java source file org.bukkit.entity.ArmorStand

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from org.bukkit.inventory import EntityEquipment
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.util import EulerAngle
from typing import Any, Callable, Iterable, Tuple


class ArmorStand(LivingEntity):

    def getItemInHand(self) -> "ItemStack":
        """
        Returns the item the armor stand is currently holding.

        Returns
        - the held item

        See
        - .getEquipment()

        Deprecated
        - prefer EntityEquipment.getItemInHand()
        """
        ...


    def setItemInHand(self, item: "ItemStack") -> None:
        """
        Sets the item the armor stand is currently holding.

        Arguments
        - item: the item to hold

        See
        - .getEquipment()

        Deprecated
        - prefer
        EntityEquipment.setItemInHand(org.bukkit.inventory.ItemStack)
        """
        ...


    def getBoots(self) -> "ItemStack":
        """
        Returns the item currently being worn by the armor stand on its feet.

        Returns
        - the worn item

        See
        - .getEquipment()

        Deprecated
        - prefer EntityEquipment.getBoots()
        """
        ...


    def setBoots(self, item: "ItemStack") -> None:
        """
        Sets the item currently being worn by the armor stand on its feet.

        Arguments
        - item: the item to wear

        See
        - .getEquipment()

        Deprecated
        - prefer
        EntityEquipment.setBoots(org.bukkit.inventory.ItemStack)
        """
        ...


    def getLeggings(self) -> "ItemStack":
        """
        Returns the item currently being worn by the armor stand on its legs.

        Returns
        - the worn item

        See
        - .getEquipment()

        Deprecated
        - prefer EntityEquipment.getLeggings()
        """
        ...


    def setLeggings(self, item: "ItemStack") -> None:
        """
        Sets the item currently being worn by the armor stand on its legs.

        Arguments
        - item: the item to wear

        See
        - .getEquipment()

        Deprecated
        - prefer
        EntityEquipment.setLeggings(org.bukkit.inventory.ItemStack)
        """
        ...


    def getChestplate(self) -> "ItemStack":
        """
        Returns the item currently being worn by the armor stand on its chest.

        Returns
        - the worn item

        See
        - .getEquipment()

        Deprecated
        - prefer EntityEquipment.getChestplate()
        """
        ...


    def setChestplate(self, item: "ItemStack") -> None:
        """
        Sets the item currently being worn by the armor stand on its chest.

        Arguments
        - item: the item to wear

        See
        - .getEquipment()

        Deprecated
        - prefer
        EntityEquipment.setChestplate(org.bukkit.inventory.ItemStack)
        """
        ...


    def getHelmet(self) -> "ItemStack":
        """
        Returns the item currently being worn by the armor stand on its head.

        Returns
        - the worn item

        See
        - .getEquipment()

        Deprecated
        - prefer EntityEquipment.getHelmet()
        """
        ...


    def setHelmet(self, item: "ItemStack") -> None:
        """
        Sets the item currently being worn by the armor stand on its head.

        Arguments
        - item: the item to wear

        See
        - .getEquipment()

        Deprecated
        - prefer
        EntityEquipment.setHelmet(org.bukkit.inventory.ItemStack)
        """
        ...


    def getBodyPose(self) -> "EulerAngle":
        """
        Returns the armor stand's body's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setBodyPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's body's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def getLeftArmPose(self) -> "EulerAngle":
        """
        Returns the armor stand's left arm's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setLeftArmPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's left arm's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def getRightArmPose(self) -> "EulerAngle":
        """
        Returns the armor stand's right arm's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setRightArmPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's right arm's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def getLeftLegPose(self) -> "EulerAngle":
        """
        Returns the armor stand's left leg's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setLeftLegPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's left leg's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def getRightLegPose(self) -> "EulerAngle":
        """
        Returns the armor stand's right leg's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setRightLegPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's right leg's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def getHeadPose(self) -> "EulerAngle":
        """
        Returns the armor stand's head's current pose as a
        org.bukkit.util.EulerAngle.

        Returns
        - the current pose
        """
        ...


    def setHeadPose(self, pose: "EulerAngle") -> None:
        """
        Sets the armor stand's head's current pose as a
        org.bukkit.util.EulerAngle.

        Arguments
        - pose: the current pose
        """
        ...


    def hasBasePlate(self) -> bool:
        """
        Returns whether the armor stand has a base plate.

        Returns
        - whether it has a base plate
        """
        ...


    def setBasePlate(self, basePlate: bool) -> None:
        """
        Sets whether the armor stand has a base plate.

        Arguments
        - basePlate: whether is has a base plate
        """
        ...


    def isVisible(self) -> bool:
        """
        Returns whether the armor stand should be visible or not.

        Returns
        - whether the stand is visible or not
        """
        ...


    def setVisible(self, visible: bool) -> None:
        """
        Sets whether the armor stand should be visible or not.

        Arguments
        - visible: whether the stand is visible or not
        """
        ...


    def hasArms(self) -> bool:
        """
        Returns whether this armor stand has arms.

        Returns
        - whether this has arms or not
        """
        ...


    def setArms(self, arms: bool) -> None:
        """
        Sets whether this armor stand has arms.

        Arguments
        - arms: whether this has arms or not
        """
        ...


    def isSmall(self) -> bool:
        """
        Returns whether this armor stand is scaled down.

        Returns
        - whether this is scaled down
        """
        ...


    def setSmall(self, small: bool) -> None:
        """
        Sets whether this armor stand is scaled down.

        Arguments
        - small: whether this is scaled down
        """
        ...


    def isMarker(self) -> bool:
        """
        Returns whether this armor stand is a marker, meaning it has a very small
        collision box.

        Returns
        - whether this is a marker
        """
        ...


    def setMarker(self, marker: bool) -> None:
        """
        Sets whether this armor stand is a marker, meaning it has a very small
        collision box.

        Arguments
        - marker: whether this is a marker
        """
        ...


    def addEquipmentLock(self, slot: "EquipmentSlot", lockType: "LockType") -> None:
        """
        Locks the equipment slot with the specified
        LockType locking mechanism.

        Arguments
        - slot: the equipment slot to lock
        - lockType: the LockType to lock the equipment slot with
        """
        ...


    def removeEquipmentLock(self, slot: "EquipmentSlot", lockType: "LockType") -> None:
        """
        Remove a LockType locking mechanism.

        Arguments
        - slot: the equipment slot to change
        - lockType: the LockType to remove
        """
        ...


    def hasEquipmentLock(self, slot: "EquipmentSlot", lockType: "LockType") -> bool:
        """
        Returns if the ArmorStand has the specified
        LockType locking mechanism.

        Arguments
        - slot: the EquipmentSlot to test
        - lockType: the LockType to test

        Returns
        - if the ArmorStand has been locked with the parameters specified
        """
        ...


    class LockType(Enum):
        """
        Represents types of locking mechanisms for ArmorStand equipment.
        """

        ADDING_OR_CHANGING = 0
        """
        Prevents adding or changing the respective equipment - players cannot
        replace the empty slot with a new item or swap the items between
        themselves and the ArmorStand.
        """
        REMOVING_OR_CHANGING = 1
        """
        Prevents removing or changing the respective equipment - players
        cannot take an item from the slot or swap the items between
        themselves and the ArmorStand.
        """
        ADDING = 2
        """
        Prevents adding the respective equipment - players cannot replace the
        empty slot with a new item, but can swap items between themselves and
        the ArmorStand.
        """
