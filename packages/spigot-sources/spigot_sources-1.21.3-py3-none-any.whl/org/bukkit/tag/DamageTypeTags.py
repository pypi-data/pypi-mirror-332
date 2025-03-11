"""
Python module generated from Java source file org.bukkit.tag.DamageTypeTags

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit import NamespacedKey
from org.bukkit import Tag
from org.bukkit.damage import DamageType
from org.bukkit.tag import *
from typing import Any, Callable, Iterable, Tuple


class DamageTypeTags:
    """
    Vanilla DamageType Tag tags.
    """

    DAMAGES_HELMET = getTag("damages_helmet")
    """
    Vanilla tag representing damage types which damage helmets.
    """
    BYPASSES_ARMOR = getTag("bypasses_armor")
    """
    Vanilla tag representing damage types which bypass armor.
    """
    BYPASSES_SHIELD = getTag("bypasses_shield")
    """
    Vanilla tag representing damage types which bypass shields.
    """
    BYPASSES_INVULNERABILITY = getTag("bypasses_invulnerability")
    """
    Vanilla tag representing damage types which bypass invulnerability.
    """
    BYPASSES_COOLDOWN = getTag("bypasses_cooldown")
    """
    Vanilla tag representing damage types which bypass cooldowns.
    
    **Note:** this can be null unless a datapack add values to this tag because vanilla not has any values for this.
    """
    BYPASSES_EFFECTS = getTag("bypasses_effects")
    """
    Vanilla tag representing damage types which bypass effects.
    """
    BYPASSES_RESISTANCE = getTag("bypasses_resistance")
    """
    Vanilla tag representing damage types which bypass resistance.
    """
    BYPASSES_ENCHANTMENTS = getTag("bypasses_enchantments")
    """
    Vanilla tag representing damage types which bypass enchantments.
    """
    IS_FIRE = getTag("is_fire")
    """
    Vanilla tag representing all fire damage types.
    """
    IS_PROJECTILE = getTag("is_projectile")
    """
    Vanilla tag representing damage types which originate from projectiles.
    """
    WITCH_RESISTANT_TO = getTag("witch_resistant_to")
    """
    Vanilla tag representing damage types which witches are resistant to.
    """
    IS_EXPLOSION = getTag("is_explosion")
    """
    Vanilla tag representing all explosion damage types.
    """
    IS_FALL = getTag("is_fall")
    """
    Vanilla tag representing all fall damage types.
    """
    IS_DROWNING = getTag("is_drowning")
    """
    Vanilla tag representing all drowning damage types.
    """
    IS_FREEZING = getTag("is_freezing")
    """
    Vanilla tag representing all freezing damage types.
    """
    IS_LIGHTNING = getTag("is_lightning")
    """
    Vanilla tag representing all lightning damage types.
    """
    NO_ANGER = getTag("no_anger")
    """
    Vanilla tag representing damage types which do not cause entities to
    anger.
    """
    NO_IMPACT = getTag("no_impact")
    """
    Vanilla tag representing damage types which do not cause an impact.
    """
    ALWAYS_MOST_SIGNIFICANT_FALL = getTag("always_most_significant_fall")
    """
    Vanilla tag representing damage types which cause maximum fall damage.
    """
    WITHER_IMMUNE_TO = getTag("wither_immune_to")
    """
    Vanilla tag representing damage types which withers are immune to.
    """
    IGNITES_ARMOR_STANDS = getTag("ignites_armor_stands")
    """
    Vanilla tag representing damage types which ignite armor stands.
    """
    BURNS_ARMOR_STANDS = getTag("burns_armor_stands")
    """
    Vanilla tag representing damage types which burn armor stands.
    """
    AVOIDS_GUARDIAN_THORNS = getTag("avoids_guardian_thorns")
    """
    Vanilla tag representing damage types which avoid guardian thorn damage.
    """
    ALWAYS_TRIGGERS_SILVERFISH = getTag("always_triggers_silverfish")
    """
    Vanilla tag representing damage types which always trigger silverfish.
    """
    ALWAYS_HURTS_ENDER_DRAGONS = getTag("always_hurts_ender_dragons")
    """
    Vanilla tag representing damage types which always hurt enderdragons.
    """
    NO_KNOCKBACK = getTag("no_knockback")
    """
    Vanilla tag representing damage types which do not cause knockback.
    """
    ALWAYS_KILLS_ARMOR_STANDS = getTag("always_kills_armor_stands")
    """
    Vanilla tag representing damage types which always kill armor stands.
    """
    CAN_BREAK_ARMOR_STAND = getTag("can_break_armor_stand")
    """
    Vanilla tag representing damage types which can break armor stands.
    """
    BYPASSES_WOLF_ARMOR = getTag("bypasses_wolf_armor")
    """
    Vanilla tag representing damage types which bypass wolf armor.
    """
    IS_PLAYER_ATTACK = getTag("is_player_attack")
    """
    Vanilla tag representing damage types which are from player attacks.
    """
    BURN_FROM_STEPPING = getTag("burn_from_stepping")
    """
    Vanilla tag representing damage types which originate from hot blocks.
    """
    PANIC_CAUSES = getTag("panic_causes")
    """
    Vanilla tag representing damage types which cause entities to panic.
    """
    PANIC_ENVIRONMENTAL_CAUSES = getTag("panic_environmental_causes")
    """
    Vanilla tag representing environmental damage types which cause entities
    to panic.
    """
    IS_MACE_SMASH = getTag("mace_smash")
    """
    Vanilla tag representing damage types which originate from mace smashes.
    """
    REGISTRY_DAMAGE_TYPES = "damage_types"
    """
    Internal use only.
    """
