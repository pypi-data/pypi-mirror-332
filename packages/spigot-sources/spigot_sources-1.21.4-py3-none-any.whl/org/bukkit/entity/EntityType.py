"""
Python module generated from Java source file org.bukkit.entity.EntityType

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from java.util import Locale
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import Location
from org.bukkit import NamespacedKey
from org.bukkit import Translatable
from org.bukkit import World
from org.bukkit.entity import *
from org.bukkit.entity.boat import AcaciaBoat
from org.bukkit.entity.boat import AcaciaChestBoat
from org.bukkit.entity.boat import BambooChestRaft
from org.bukkit.entity.boat import BambooRaft
from org.bukkit.entity.boat import BirchBoat
from org.bukkit.entity.boat import BirchChestBoat
from org.bukkit.entity.boat import CherryBoat
from org.bukkit.entity.boat import CherryChestBoat
from org.bukkit.entity.boat import DarkOakBoat
from org.bukkit.entity.boat import DarkOakChestBoat
from org.bukkit.entity.boat import JungleBoat
from org.bukkit.entity.boat import JungleChestBoat
from org.bukkit.entity.boat import MangroveBoat
from org.bukkit.entity.boat import MangroveChestBoat
from org.bukkit.entity.boat import OakBoat
from org.bukkit.entity.boat import OakChestBoat
from org.bukkit.entity.boat import PaleOakBoat
from org.bukkit.entity.boat import PaleOakChestBoat
from org.bukkit.entity.boat import SpruceBoat
from org.bukkit.entity.boat import SpruceChestBoat
from org.bukkit.entity.minecart import CommandMinecart
from org.bukkit.entity.minecart import ExplosiveMinecart
from org.bukkit.entity.minecart import HopperMinecart
from org.bukkit.entity.minecart import PoweredMinecart
from org.bukkit.entity.minecart import RideableMinecart
from org.bukkit.entity.minecart import SpawnerMinecart
from org.bukkit.entity.minecart import StorageMinecart
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffectType
from org.bukkit.registry import RegistryAware
from typing import Any, Callable, Iterable, Tuple


class EntityType(Enum):

    ITEM = ("item", Item, 1)
    """
    An item resting on the ground.
    
    Spawn with World.dropItem(Location, ItemStack) or World.dropItemNaturally(Location, ItemStack)
    """
    EXPERIENCE_ORB = ("experience_orb", ExperienceOrb, 2)
    """
    An experience orb.
    """
    AREA_EFFECT_CLOUD = ("area_effect_cloud", AreaEffectCloud, 3)
    """
    See
    - AreaEffectCloud
    """
    ELDER_GUARDIAN = ("elder_guardian", ElderGuardian, 4)
    """
    See
    - ElderGuardian
    """
    WITHER_SKELETON = ("wither_skeleton", WitherSkeleton, 5)
    """
    See
    - WitherSkeleton
    """
    STRAY = ("stray", Stray, 6)
    """
    See
    - Stray
    """
    EGG = ("egg", Egg, 7)
    """
    A flying chicken egg.
    """
    LEASH_KNOT = ("leash_knot", LeashHitch, 8)
    """
    A leash attached to a fencepost.
    """
    PAINTING = ("painting", Painting, 9)
    """
    A painting on a wall.
    """
    ARROW = ("arrow", Arrow, 10)
    """
    An arrow projectile; may get stuck in the ground.
    """
    SNOWBALL = ("snowball", Snowball, 11)
    """
    A flying snowball.
    """
    FIREBALL = ("fireball", LargeFireball, 12)
    """
    A flying large fireball, as thrown by a Ghast for example.
    """
    SMALL_FIREBALL = ("small_fireball", SmallFireball, 13)
    """
    A flying small fireball, such as thrown by a Blaze or player.
    """
    ENDER_PEARL = ("ender_pearl", EnderPearl, 14)
    """
    A flying ender pearl.
    """
    EYE_OF_ENDER = ("eye_of_ender", EnderSignal, 15)
    """
    An ender eye signal.
    """
    POTION = ("potion", ThrownPotion, 16)
    """
    A flying splash potion.
    """
    EXPERIENCE_BOTTLE = ("experience_bottle", ThrownExpBottle, 17)
    """
    A flying experience bottle.
    """
    ITEM_FRAME = ("item_frame", ItemFrame, 18)
    """
    An item frame on a wall.
    """
    WITHER_SKULL = ("wither_skull", WitherSkull, 19)
    """
    A flying wither skull projectile.
    """
    TNT = ("tnt", TNTPrimed, 20)
    """
    Primed TNT that is about to explode.
    """
    FALLING_BLOCK = ("falling_block", FallingBlock, 21)
    """
    A block that is going to or is about to fall.
    """
    FIREWORK_ROCKET = ("firework_rocket", Firework, 22)
    """
    Internal representation of a Firework once it has been launched.
    """
    HUSK = ("husk", Husk, 23)
    """
    See
    - Husk
    """
    SPECTRAL_ARROW = ("spectral_arrow", SpectralArrow, 24)
    """
    Like .ARROW but causes the PotionEffectType.GLOWING effect on all team members.
    """
    SHULKER_BULLET = ("shulker_bullet", ShulkerBullet, 25)
    """
    Bullet fired by .SHULKER.
    """
    DRAGON_FIREBALL = ("dragon_fireball", DragonFireball, 26)
    """
    Like .FIREBALL but with added effects.
    """
    ZOMBIE_VILLAGER = ("zombie_villager", ZombieVillager, 27)
    """
    See
    - ZombieVillager
    """
    SKELETON_HORSE = ("skeleton_horse", SkeletonHorse, 28)
    """
    See
    - SkeletonHorse
    """
    ZOMBIE_HORSE = ("zombie_horse", ZombieHorse, 29)
    """
    See
    - ZombieHorse
    """
    ARMOR_STAND = ("armor_stand", ArmorStand, 30)
    """
    Mechanical entity with an inventory for placing weapons / armor into.
    """
    DONKEY = ("donkey", Donkey, 31)
    """
    See
    - Donkey
    """
    MULE = ("mule", Mule, 32)
    """
    See
    - Mule
    """
    EVOKER_FANGS = ("evoker_fangs", EvokerFangs, 33)
    """
    See
    - EvokerFangs
    """
    EVOKER = ("evoker", Evoker, 34)
    """
    See
    - Evoker
    """
    VEX = ("vex", Vex, 35)
    """
    See
    - Vex
    """
    VINDICATOR = ("vindicator", Vindicator, 36)
    """
    See
    - Vindicator
    """
    ILLUSIONER = ("illusioner", Illusioner, 37)
    """
    See
    - Illusioner
    """
    COMMAND_BLOCK_MINECART = ("command_block_minecart", CommandMinecart, 40)
    """
    See
    - CommandMinecart
    """
    MINECART = ("minecart", RideableMinecart, 42)
    """
    See
    - RideableMinecart
    """
    CHEST_MINECART = ("chest_minecart", StorageMinecart, 43)
    """
    See
    - StorageMinecart
    """
    FURNACE_MINECART = ("furnace_minecart", PoweredMinecart, 44)
    """
    See
    - PoweredMinecart
    """
    TNT_MINECART = ("tnt_minecart", ExplosiveMinecart, 45)
    """
    See
    - ExplosiveMinecart
    """
    HOPPER_MINECART = ("hopper_minecart", HopperMinecart, 46)
    """
    See
    - HopperMinecart
    """
    SPAWNER_MINECART = ("spawner_minecart", SpawnerMinecart, 47)
    """
    See
    - SpawnerMinecart
    """
    CREEPER = ("creeper", Creeper, 50)
    SKELETON = ("skeleton", Skeleton, 51)
    SPIDER = ("spider", Spider, 52)
    GIANT = ("giant", Giant, 53)
    ZOMBIE = ("zombie", Zombie, 54)
    SLIME = ("slime", Slime, 55)
    GHAST = ("ghast", Ghast, 56)
    ZOMBIFIED_PIGLIN = ("zombified_piglin", PigZombie, 57)
    ENDERMAN = ("enderman", Enderman, 58)
    CAVE_SPIDER = ("cave_spider", CaveSpider, 59)
    SILVERFISH = ("silverfish", Silverfish, 60)
    BLAZE = ("blaze", Blaze, 61)
    MAGMA_CUBE = ("magma_cube", MagmaCube, 62)
    ENDER_DRAGON = ("ender_dragon", EnderDragon, 63)
    WITHER = ("wither", Wither, 64)
    BAT = ("bat", Bat, 65)
    WITCH = ("witch", Witch, 66)
    ENDERMITE = ("endermite", Endermite, 67)
    GUARDIAN = ("guardian", Guardian, 68)
    SHULKER = ("shulker", Shulker, 69)
    PIG = ("pig", Pig, 90)
    SHEEP = ("sheep", Sheep, 91)
    COW = ("cow", Cow, 92)
    CHICKEN = ("chicken", Chicken, 93)
    SQUID = ("squid", Squid, 94)
    WOLF = ("wolf", Wolf, 95)
    MOOSHROOM = ("mooshroom", MushroomCow, 96)
    SNOW_GOLEM = ("snow_golem", Snowman, 97)
    OCELOT = ("ocelot", Ocelot, 98)
    IRON_GOLEM = ("iron_golem", IronGolem, 99)
    HORSE = ("horse", Horse, 100)
    RABBIT = ("rabbit", Rabbit, 101)
    POLAR_BEAR = ("polar_bear", PolarBear, 102)
    LLAMA = ("llama", Llama, 103)
    LLAMA_SPIT = ("llama_spit", LlamaSpit, 104)
    PARROT = ("parrot", Parrot, 105)
    VILLAGER = ("villager", Villager, 120)
    END_CRYSTAL = ("end_crystal", EnderCrystal, 200)
    TURTLE = ("turtle", Turtle, -1)
    PHANTOM = ("phantom", Phantom, -1)
    TRIDENT = ("trident", Trident, -1)
    COD = ("cod", Cod, -1)
    SALMON = ("salmon", Salmon, -1)
    PUFFERFISH = ("pufferfish", PufferFish, -1)
    TROPICAL_FISH = ("tropical_fish", TropicalFish, -1)
    DROWNED = ("drowned", Drowned, -1)
    DOLPHIN = ("dolphin", Dolphin, -1)
    CAT = ("cat", Cat, -1)
    PANDA = ("panda", Panda, -1)
    PILLAGER = ("pillager", Pillager, -1)
    RAVAGER = ("ravager", Ravager, -1)
    TRADER_LLAMA = ("trader_llama", TraderLlama, -1)
    WANDERING_TRADER = ("wandering_trader", WanderingTrader, -1)
    FOX = ("fox", Fox, -1)
    BEE = ("bee", Bee, -1)
    HOGLIN = ("hoglin", Hoglin, -1)
    PIGLIN = ("piglin", Piglin, -1)
    STRIDER = ("strider", Strider, -1)
    ZOGLIN = ("zoglin", Zoglin, -1)
    PIGLIN_BRUTE = ("piglin_brute", PiglinBrute, -1)
    AXOLOTL = ("axolotl", Axolotl, -1)
    GLOW_ITEM_FRAME = ("glow_item_frame", GlowItemFrame, -1)
    GLOW_SQUID = ("glow_squid", GlowSquid, -1)
    GOAT = ("goat", Goat, -1)
    MARKER = ("marker", Marker, -1)
    ALLAY = ("allay", Allay, -1)
    FROG = ("frog", Frog, -1)
    TADPOLE = ("tadpole", Tadpole, -1)
    WARDEN = ("warden", Warden, -1)
    CAMEL = ("camel", Camel, -1)
    BLOCK_DISPLAY = ("block_display", BlockDisplay, -1)
    INTERACTION = ("interaction", Interaction, -1)
    ITEM_DISPLAY = ("item_display", ItemDisplay, -1)
    SNIFFER = ("sniffer", Sniffer, -1)
    TEXT_DISPLAY = ("text_display", TextDisplay, -1)
    BREEZE = ("breeze", Breeze, -1)
    WIND_CHARGE = ("wind_charge", WindCharge, -1)
    BREEZE_WIND_CHARGE = ("breeze_wind_charge", BreezeWindCharge, -1)
    ARMADILLO = ("armadillo", Armadillo, -1)
    BOGGED = ("bogged", Bogged, -1)
    OMINOUS_ITEM_SPAWNER = ("ominous_item_spawner", OminousItemSpawner, -1)
    ACACIA_BOAT = ("acacia_boat", AcaciaBoat, -1)
    ACACIA_CHEST_BOAT = ("acacia_chest_boat", AcaciaChestBoat, -1)
    BAMBOO_RAFT = ("bamboo_raft", BambooRaft, -1)
    BAMBOO_CHEST_RAFT = ("bamboo_chest_raft", BambooChestRaft, -1)
    BIRCH_BOAT = ("birch_boat", BirchBoat, -1)
    BIRCH_CHEST_BOAT = ("birch_chest_boat", BirchChestBoat, -1)
    CHERRY_BOAT = ("cherry_boat", CherryBoat, -1)
    CHERRY_CHEST_BOAT = ("cherry_chest_boat", CherryChestBoat, -1)
    DARK_OAK_BOAT = ("dark_oak_boat", DarkOakBoat, -1)
    DARK_OAK_CHEST_BOAT = ("dark_oak_chest_boat", DarkOakChestBoat, -1)
    JUNGLE_BOAT = ("jungle_boat", JungleBoat, -1)
    JUNGLE_CHEST_BOAT = ("jungle_chest_boat", JungleChestBoat, -1)
    MANGROVE_BOAT = ("mangrove_boat", MangroveBoat, -1)
    MANGROVE_CHEST_BOAT = ("mangrove_chest_boat", MangroveChestBoat, -1)
    OAK_BOAT = ("oak_boat", OakBoat, -1)
    OAK_CHEST_BOAT = ("oak_chest_boat", OakChestBoat, -1)
    PALE_OAK_BOAT = ("pale_oak_boat", PaleOakBoat, -1)
    PALE_OAK_CHEST_BOAT = ("pale_oak_chest_boat", PaleOakChestBoat, -1)
    SPRUCE_BOAT = ("spruce_boat", SpruceBoat, -1)
    SPRUCE_CHEST_BOAT = ("spruce_chest_boat", SpruceChestBoat, -1)
    CREAKING = ("creaking", Creaking, -1)
    FISHING_BOBBER = ("fishing_bobber", FishHook, -1, False)
    """
    A fishing line and bobber.
    """
    LIGHTNING_BOLT = ("lightning_bolt", LightningStrike, -1)
    """
    A bolt of lightning.
    
    Spawn with World.strikeLightning(Location).
    """
    PLAYER = ("player", Player, -1, False)
    UNKNOWN = (None, None, -1, False)
    """
    An unknown entity without an Entity Class
    """


    def getName(self) -> str:
        """
        Gets the entity type name.

        Returns
        - the entity type's name

        Deprecated
        - Magic value
        """
        ...


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...


    def getEntityClass(self) -> type["Entity"]:
        ...


    def getTypeId(self) -> int:
        """
        Gets the entity type id.

        Returns
        - the raw type id

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def fromName(name: str) -> "EntityType":
        """
        Gets an entity type from its name.

        Arguments
        - name: the entity type's name

        Returns
        - the matching entity type or null

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def fromId(id: int) -> "EntityType":
        """
        Gets an entity from its id.

        Arguments
        - id: the raw type id

        Returns
        - the matching entity type or null

        Deprecated
        - Magic value
        """
        ...


    def isSpawnable(self) -> bool:
        """
        Some entities cannot be spawned using World.spawnEntity(Location, EntityType) or World.spawn(Location, Class), usually because they require additional
        information in order to spawn.

        Returns
        - False if the entity type cannot be spawned
        """
        ...


    def isAlive(self) -> bool:
        ...


    def getTranslationKey(self) -> str:
        ...


    def isEnabledByFeature(self, world: "World") -> bool:
        """
        Gets if this EntityType is enabled by feature in a world.

        Arguments
        - world: the world to check

        Returns
        - True if this EntityType can be used to spawn an Entity for this World.
        """
        ...


    def getKeyOrThrow(self) -> "NamespacedKey":
        ...


    def getKeyOrNull(self) -> "NamespacedKey":
        ...


    def isRegistered(self) -> bool:
        ...
