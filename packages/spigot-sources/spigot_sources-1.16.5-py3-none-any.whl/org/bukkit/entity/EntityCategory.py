"""
Python module generated from Java source file org.bukkit.entity.EntityCategory

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import *
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class EntityCategory(Enum):
    """
    A classification of entities which may behave differently than others or be
    affected uniquely by enchantments and potion effects among other things.
    """

    NONE = 0
    """
    Any uncategorized entity. No additional effects are applied to these
    entities relating to a categorization.
    """
    UNDEAD = 1
    """
    Undead creatures. These creatures:
    
      - Are damaged by potions of healing.
      - Are healed by potions of harming.
      - Are immune to drowning and poison.
      - Are subject to burning in daylight (though not all).
      - Sink in water (except Drowned, Phantom Phantoms
      and Wither Withers).
      - Take additional damage from Enchantment.DAMAGE_UNDEAD.
      - Are ignored by Wither Withers.
    """
    ARTHROPOD = 2
    """
    Entities of the arthropod family. These creatures:
    
      - Take additional damage and receive PotionEffectType.SLOW
      from Enchantment.DAMAGE_ARTHROPODS.
      - Are immune to PotionEffectType.POISON if they are spiders.
    """
    ILLAGER = 3
    """
    Entities that participate in raids. These creatures:
    
      - Are immune to damage from EvokerFangs.
      - Are ignored by Vindicator vindicators named "Johnny".
      - Are hostile to Villager villagers,
      WanderingTrader wandering traders, IronGolem iron golems
      and Player players.
    """
    WATER = 4
    """
    Entities that reside primarily underwater (excluding Drowned).
    These creatures:
    
      - Take additional damage from Enchantment.IMPALING.
      - Are immune to drowning (excluding Dolphin dolphins).
      - Take suffocation damage when out of water for extended periods of
      time (excluding Guardian guardians and Turtle turtles).
      - Are capable of swimming in water rather than floating or sinking.
    """
