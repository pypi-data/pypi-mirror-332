"""
Python module generated from Java source file org.bukkit.damage.DamageType

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.damage import *
from typing import Any, Callable, Iterable, Tuple


class DamageType(Keyed, Translatable):
    """
    Represent a type of damage that an entity can receive.
    
    Constants in this class include the base types provided by the vanilla
    server. Data packs are capable of registering more types of damage which may
    be obtained through the Registry.DAMAGE_TYPE.

    See
    - <a href="https://minecraft.wiki/w/Damage_type">Minecraft Wiki</a>
    """

    IN_FIRE = getDamageType("in_fire")
    LIGHTNING_BOLT = getDamageType("lightning_bolt")
    ON_FIRE = getDamageType("on_fire")
    LAVA = getDamageType("lava")
    HOT_FLOOR = getDamageType("hot_floor")
    IN_WALL = getDamageType("in_wall")
    CRAMMING = getDamageType("cramming")
    DROWN = getDamageType("drown")
    STARVE = getDamageType("starve")
    CACTUS = getDamageType("cactus")
    FALL = getDamageType("fall")
    FLY_INTO_WALL = getDamageType("fly_into_wall")
    OUT_OF_WORLD = getDamageType("out_of_world")
    GENERIC = getDamageType("generic")
    MAGIC = getDamageType("magic")
    WITHER = getDamageType("wither")
    DRAGON_BREATH = getDamageType("dragon_breath")
    DRY_OUT = getDamageType("dry_out")
    SWEET_BERRY_BUSH = getDamageType("sweet_berry_bush")
    FREEZE = getDamageType("freeze")
    STALAGMITE = getDamageType("stalagmite")
    FALLING_BLOCK = getDamageType("falling_block")
    FALLING_ANVIL = getDamageType("falling_anvil")
    FALLING_STALACTITE = getDamageType("falling_stalactite")
    STING = getDamageType("sting")
    MOB_ATTACK = getDamageType("mob_attack")
    MOB_ATTACK_NO_AGGRO = getDamageType("mob_attack_no_aggro")
    PLAYER_ATTACK = getDamageType("player_attack")
    ARROW = getDamageType("arrow")
    TRIDENT = getDamageType("trident")
    MOB_PROJECTILE = getDamageType("mob_projectile")
    SPIT = getDamageType("spit")
    FIREWORKS = getDamageType("fireworks")
    FIREBALL = getDamageType("fireball")
    UNATTRIBUTED_FIREBALL = getDamageType("unattributed_fireball")
    WITHER_SKULL = getDamageType("wither_skull")
    THROWN = getDamageType("thrown")
    INDIRECT_MAGIC = getDamageType("indirect_magic")
    THORNS = getDamageType("thorns")
    EXPLOSION = getDamageType("explosion")
    PLAYER_EXPLOSION = getDamageType("player_explosion")
    SONIC_BOOM = getDamageType("sonic_boom")
    BAD_RESPAWN_POINT = getDamageType("bad_respawn_point")
    OUTSIDE_BORDER = getDamageType("outside_border")
    GENERIC_KILL = getDamageType("generic_kill")


    @staticmethod
    def getDamageType(key: str) -> "DamageType":
        ...


    def getTranslationKey(self) -> str:
        """
        
        
        The returned key is that of the death message sent when this damage type
        is responsible for the death of an entity.
        
        <strong>Note</strong> This translation key is only used if
        .getDeathMessageType() is DeathMessageType.DEFAULT
        """
        ...


    def getDamageScaling(self) -> "DamageScaling":
        """
        Get the DamageScaling for this damage type.

        Returns
        - the damage scaling
        """
        ...


    def getDamageEffect(self) -> "DamageEffect":
        """
        Get the DamageEffect for this damage type.

        Returns
        - the damage effect
        """
        ...


    def getDeathMessageType(self) -> "DeathMessageType":
        """
        Get the DeathMessageType for this damage type.

        Returns
        - the death message type
        """
        ...


    def getExhaustion(self) -> float:
        """
        Get the amount of hunger exhaustion caused by this damage type.

        Returns
        - the exhaustion
        """
        ...
