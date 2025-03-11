"""
Python module generated from Java source file org.bukkit.inventory.view.BeaconView

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import BeaconInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class BeaconView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    beacon view data.
    """

    def getTopInventory(self) -> "BeaconInventory":
        ...


    def getTier(self) -> int:
        """
        Gets the tier of the beacon
        
        Beacon tier is deduced by the height of the pyramid the beacon is
        standing on. The level of the beacon is 0 unless the beacon is activated.

        Returns
        - The tier of the beacon
        """
        ...


    def getPrimaryEffect(self) -> "PotionEffectType":
        """
        Gets the primary effect of the beacon.
        
        If the beacon level is high enough where the primary effect can be
        upgraded to level two, e.g. Speed 2. Instead of
        .getSecondaryEffect() being null it .getSecondaryEffect()
        returns the same PotionEffectType as this method.

        Returns
        - The primary effect enabled on the beacon
        """
        ...


    def getSecondaryEffect(self) -> "PotionEffectType":
        """
        Gets the secondary effect of the beacon.
        
        If the beacon level is high enough where the primary effect can be
        upgraded to level two, e.g. Speed 2. The secondary effect will return the
        same effect as .getPrimaryEffect().

        Returns
        - The secondary effect enabled on the beacon
        """
        ...


    def setPrimaryEffect(self, effect: "PotionEffectType") -> None:
        """
        Sets the primary effect of the beacon, or null to clear
        
        The PotionEffectType provided must be one that is already within
        the beacon as a valid option.
        <ol>
        - PotionEffectType.SPEED
        - PotionEffectType.HASTE
        - PotionEffectType.RESISTANCE
        - PotionEffectType.JUMP_BOOST
        - PotionEffectType.STRENGTH
        - PotionEffectType.REGENERATION
        </ol>

        Arguments
        - effect: desired primary effect
        """
        ...


    def setSecondaryEffect(self, effect: "PotionEffectType") -> None:
        """
        Sets the secondary effect on this beacon, or null to clear. Note that
        tier must be &gt;= 4 and a primary effect must be set in order for this
        effect to be active.
        
        The PotionEffectType provided must be one that is already within
        the beacon as a valid option.
        <ol>
        - PotionEffectType.SPEED
        - PotionEffectType.HASTE
        - PotionEffectType.RESISTANCE
        - PotionEffectType.JUMP_BOOST
        - PotionEffectType.STRENGTH
        - PotionEffectType.REGENERATION
        </ol>

        Arguments
        - effect: the desired secondary effect
        """
        ...
