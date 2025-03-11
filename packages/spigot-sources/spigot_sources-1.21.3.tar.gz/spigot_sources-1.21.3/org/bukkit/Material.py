"""
Python module generated from Java source file org.bukkit.Material

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.base import Suppliers
from com.google.common.collect import Maps
from com.google.common.collect import Multimap
from enum import Enum
from java.lang.reflect import Constructor
from java.util import Locale
from java.util.function import Consumer
from java.util.function import Supplier
from org.bukkit import *
from org.bukkit.attribute import Attribute
from org.bukkit.attribute import AttributeModifier
from org.bukkit.block import Block
from org.bukkit.block import BlockType
from org.bukkit.block.data import Ageable
from org.bukkit.block.data import AnaloguePowerable
from org.bukkit.block.data import Bisected
from org.bukkit.block.data import BlockData
from org.bukkit.block.data import Brushable
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Hatchable
from org.bukkit.block.data import Levelled
from org.bukkit.block.data import Lightable
from org.bukkit.block.data import MultipleFacing
from org.bukkit.block.data import Orientable
from org.bukkit.block.data import Powerable
from org.bukkit.block.data import Rail
from org.bukkit.block.data import Rotatable
from org.bukkit.block.data import Snowable
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import AmethystCluster
from org.bukkit.block.data.type import Bamboo
from org.bukkit.block.data.type import Barrel
from org.bukkit.block.data.type import Bed
from org.bukkit.block.data.type import Beehive
from org.bukkit.block.data.type import Bell
from org.bukkit.block.data.type import BigDripleaf
from org.bukkit.block.data.type import BrewingStand
from org.bukkit.block.data.type import BubbleColumn
from org.bukkit.block.data.type import Cake
from org.bukkit.block.data.type import CalibratedSculkSensor
from org.bukkit.block.data.type import Campfire
from org.bukkit.block.data.type import Candle
from org.bukkit.block.data.type import CaveVines
from org.bukkit.block.data.type import CaveVinesPlant
from org.bukkit.block.data.type import Chain
from org.bukkit.block.data.type import Chest
from org.bukkit.block.data.type import ChiseledBookshelf
from org.bukkit.block.data.type import Cocoa
from org.bukkit.block.data.type import CommandBlock
from org.bukkit.block.data.type import Comparator
from org.bukkit.block.data.type import CopperBulb
from org.bukkit.block.data.type import CoralWallFan
from org.bukkit.block.data.type import Crafter
from org.bukkit.block.data.type import CreakingHeart
from org.bukkit.block.data.type import DaylightDetector
from org.bukkit.block.data.type import DecoratedPot
from org.bukkit.block.data.type import Dispenser
from org.bukkit.block.data.type import Door
from org.bukkit.block.data.type import Dripleaf
from org.bukkit.block.data.type import EndPortalFrame
from org.bukkit.block.data.type import EnderChest
from org.bukkit.block.data.type import Farmland
from org.bukkit.block.data.type import Fence
from org.bukkit.block.data.type import Fire
from org.bukkit.block.data.type import Furnace
from org.bukkit.block.data.type import Gate
from org.bukkit.block.data.type import GlassPane
from org.bukkit.block.data.type import GlowLichen
from org.bukkit.block.data.type import Grindstone
from org.bukkit.block.data.type import HangingMoss
from org.bukkit.block.data.type import HangingSign
from org.bukkit.block.data.type import Hopper
from org.bukkit.block.data.type import Jigsaw
from org.bukkit.block.data.type import Jukebox
from org.bukkit.block.data.type import Ladder
from org.bukkit.block.data.type import Lantern
from org.bukkit.block.data.type import Leaves
from org.bukkit.block.data.type import Lectern
from org.bukkit.block.data.type import Light
from org.bukkit.block.data.type import LightningRod
from org.bukkit.block.data.type import MangrovePropagule
from org.bukkit.block.data.type import MossyCarpet
from org.bukkit.block.data.type import NoteBlock
from org.bukkit.block.data.type import Observer
from org.bukkit.block.data.type import PinkPetals
from org.bukkit.block.data.type import Piston
from org.bukkit.block.data.type import PistonHead
from org.bukkit.block.data.type import PitcherCrop
from org.bukkit.block.data.type import PointedDripstone
from org.bukkit.block.data.type import RedstoneRail
from org.bukkit.block.data.type import RedstoneWallTorch
from org.bukkit.block.data.type import RedstoneWire
from org.bukkit.block.data.type import Repeater
from org.bukkit.block.data.type import RespawnAnchor
from org.bukkit.block.data.type import Sapling
from org.bukkit.block.data.type import Scaffolding
from org.bukkit.block.data.type import SculkCatalyst
from org.bukkit.block.data.type import SculkSensor
from org.bukkit.block.data.type import SculkShrieker
from org.bukkit.block.data.type import SculkVein
from org.bukkit.block.data.type import SeaPickle
from org.bukkit.block.data.type import Sign
from org.bukkit.block.data.type import Skull
from org.bukkit.block.data.type import Slab
from org.bukkit.block.data.type import SmallDripleaf
from org.bukkit.block.data.type import Snow
from org.bukkit.block.data.type import Stairs
from org.bukkit.block.data.type import StructureBlock
from org.bukkit.block.data.type import Switch
from org.bukkit.block.data.type import TNT
from org.bukkit.block.data.type import TechnicalPiston
from org.bukkit.block.data.type import TrapDoor
from org.bukkit.block.data.type import TrialSpawner
from org.bukkit.block.data.type import Tripwire
from org.bukkit.block.data.type import TripwireHook
from org.bukkit.block.data.type import TurtleEgg
from org.bukkit.block.data.type import Vault
from org.bukkit.block.data.type import Wall
from org.bukkit.block.data.type import WallHangingSign
from org.bukkit.block.data.type import WallSign
from org.bukkit.block.data.type import WallSkull
from org.bukkit.inventory import CreativeCategory
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import ItemType
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class Material(Enum):
    """
    An enum of all material IDs accepted by the official server and client
    """

# Static fields
    LEGACY_PREFIX = "LEGACY_"


    AIR = (9648, 0)
    STONE = (22948)
    GRANITE = (21091)
    POLISHED_GRANITE = (5477)
    DIORITE = (24688)
    POLISHED_DIORITE = (31615)
    ANDESITE = (25975)
    POLISHED_ANDESITE = (8335)
    DEEPSLATE = (26842, Orientable)
    """
    BlockData: Orientable
    """
    COBBLED_DEEPSLATE = (8021)
    POLISHED_DEEPSLATE = (31772)
    CALCITE = (20311)
    TUFF = (24364)
    TUFF_SLAB = (19305, Slab)
    """
    BlockData: Slab
    """
    TUFF_STAIRS = (11268, Stairs)
    """
    BlockData: Stairs
    """
    TUFF_WALL = (24395, Wall)
    """
    BlockData: Wall
    """
    CHISELED_TUFF = (15831)
    POLISHED_TUFF = (17801)
    POLISHED_TUFF_SLAB = (31096, Slab)
    """
    BlockData: Slab
    """
    POLISHED_TUFF_STAIRS = (7964, Stairs)
    """
    BlockData: Stairs
    """
    POLISHED_TUFF_WALL = (28886, Wall)
    """
    BlockData: Wall
    """
    TUFF_BRICKS = (26276)
    TUFF_BRICK_SLAB = (11843, Slab)
    """
    BlockData: Slab
    """
    TUFF_BRICK_STAIRS = (30753, Stairs)
    """
    BlockData: Stairs
    """
    TUFF_BRICK_WALL = (11761, Wall)
    """
    BlockData: Wall
    """
    CHISELED_TUFF_BRICKS = (8601)
    DRIPSTONE_BLOCK = (26227)
    GRASS_BLOCK = (28346, Snowable)
    """
    BlockData: Snowable
    """
    DIRT = (10580)
    COARSE_DIRT = (15411)
    PODZOL = (24068, Snowable)
    """
    BlockData: Snowable
    """
    ROOTED_DIRT = (11410)
    MUD = (32418)
    CRIMSON_NYLIUM = (18139)
    WARPED_NYLIUM = (26396)
    COBBLESTONE = (32147)
    OAK_PLANKS = (14905)
    SPRUCE_PLANKS = (14593)
    BIRCH_PLANKS = (29322)
    JUNGLE_PLANKS = (26445)
    ACACIA_PLANKS = (31312)
    CHERRY_PLANKS = (8354)
    DARK_OAK_PLANKS = (20869)
    PALE_OAK_PLANKS = (21660)
    MANGROVE_PLANKS = (7078)
    BAMBOO_PLANKS = (8520)
    CRIMSON_PLANKS = (18812)
    WARPED_PLANKS = (16045)
    BAMBOO_MOSAIC = (10715)
    OAK_SAPLING = (9636, Sapling)
    """
    BlockData: Sapling
    """
    SPRUCE_SAPLING = (19874, Sapling)
    """
    BlockData: Sapling
    """
    BIRCH_SAPLING = (31533, Sapling)
    """
    BlockData: Sapling
    """
    JUNGLE_SAPLING = (17951, Sapling)
    """
    BlockData: Sapling
    """
    ACACIA_SAPLING = (20806, Sapling)
    """
    BlockData: Sapling
    """
    CHERRY_SAPLING = (25204, Sapling)
    """
    BlockData: Sapling
    """
    DARK_OAK_SAPLING = (14933, Sapling)
    """
    BlockData: Sapling
    """
    PALE_OAK_SAPLING = (15508, Sapling)
    """
    BlockData: Sapling
    """
    MANGROVE_PROPAGULE = (18688, MangrovePropagule)
    """
    BlockData: MangrovePropagule
    """
    BEDROCK = (23130)
    SAND = (11542)
    SUSPICIOUS_SAND = (18410, Brushable)
    """
    BlockData: Brushable
    """
    SUSPICIOUS_GRAVEL = (7353, Brushable)
    """
    BlockData: Brushable
    """
    RED_SAND = (16279)
    GRAVEL = (7804)
    COAL_ORE = (30965)
    DEEPSLATE_COAL_ORE = (16823)
    IRON_ORE = (19834)
    DEEPSLATE_IRON_ORE = (26021)
    COPPER_ORE = (32666)
    DEEPSLATE_COPPER_ORE = (6588)
    GOLD_ORE = (32625)
    DEEPSLATE_GOLD_ORE = (13582)
    REDSTONE_ORE = (10887, Lightable)
    """
    BlockData: Lightable
    """
    DEEPSLATE_REDSTONE_ORE = (6331, Lightable)
    """
    BlockData: Lightable
    """
    EMERALD_ORE = (16630)
    DEEPSLATE_EMERALD_ORE = (5299)
    LAPIS_ORE = (22934)
    DEEPSLATE_LAPIS_ORE = (13598)
    DIAMOND_ORE = (9292)
    DEEPSLATE_DIAMOND_ORE = (17792)
    NETHER_GOLD_ORE = (4185)
    NETHER_QUARTZ_ORE = (4807)
    ANCIENT_DEBRIS = (18198)
    COAL_BLOCK = (27968)
    RAW_IRON_BLOCK = (32210)
    RAW_COPPER_BLOCK = (17504)
    RAW_GOLD_BLOCK = (23246)
    HEAVY_CORE = (15788, Waterlogged)
    """
    BlockData: Waterlogged
    """
    AMETHYST_BLOCK = (18919)
    BUDDING_AMETHYST = (13963)
    IRON_BLOCK = (24754)
    COPPER_BLOCK = (12880)
    GOLD_BLOCK = (27392)
    DIAMOND_BLOCK = (5944)
    NETHERITE_BLOCK = (6527)
    EXPOSED_COPPER = (28488)
    WEATHERED_COPPER = (19699)
    OXIDIZED_COPPER = (19490)
    CHISELED_COPPER = (12143)
    EXPOSED_CHISELED_COPPER = (4570)
    WEATHERED_CHISELED_COPPER = (30876)
    OXIDIZED_CHISELED_COPPER = (27719)
    CUT_COPPER = (32519)
    EXPOSED_CUT_COPPER = (18000)
    WEATHERED_CUT_COPPER = (21158)
    OXIDIZED_CUT_COPPER = (5382)
    CUT_COPPER_STAIRS = (25925, Stairs)
    """
    BlockData: Stairs
    """
    EXPOSED_CUT_COPPER_STAIRS = (31621, Stairs)
    """
    BlockData: Stairs
    """
    WEATHERED_CUT_COPPER_STAIRS = (5851, Stairs)
    """
    BlockData: Stairs
    """
    OXIDIZED_CUT_COPPER_STAIRS = (25379, Stairs)
    """
    BlockData: Stairs
    """
    CUT_COPPER_SLAB = (28988, Slab)
    """
    BlockData: Slab
    """
    EXPOSED_CUT_COPPER_SLAB = (26694, Slab)
    """
    BlockData: Slab
    """
    WEATHERED_CUT_COPPER_SLAB = (4602, Slab)
    """
    BlockData: Slab
    """
    OXIDIZED_CUT_COPPER_SLAB = (29642, Slab)
    """
    BlockData: Slab
    """
    WAXED_COPPER_BLOCK = (14638)
    WAXED_EXPOSED_COPPER = (27989)
    WAXED_WEATHERED_COPPER = (5960)
    WAXED_OXIDIZED_COPPER = (25626)
    WAXED_CHISELED_COPPER = (7500)
    WAXED_EXPOSED_CHISELED_COPPER = (30658)
    WAXED_WEATHERED_CHISELED_COPPER = (5970)
    WAXED_OXIDIZED_CHISELED_COPPER = (7735)
    WAXED_CUT_COPPER = (11030)
    WAXED_EXPOSED_CUT_COPPER = (30043)
    WAXED_WEATHERED_CUT_COPPER = (13823)
    WAXED_OXIDIZED_CUT_COPPER = (22582)
    WAXED_CUT_COPPER_STAIRS = (23125, Stairs)
    """
    BlockData: Stairs
    """
    WAXED_EXPOSED_CUT_COPPER_STAIRS = (15532, Stairs)
    """
    BlockData: Stairs
    """
    WAXED_WEATHERED_CUT_COPPER_STAIRS = (29701, Stairs)
    """
    BlockData: Stairs
    """
    WAXED_OXIDIZED_CUT_COPPER_STAIRS = (9842, Stairs)
    """
    BlockData: Stairs
    """
    WAXED_CUT_COPPER_SLAB = (6271, Slab)
    """
    BlockData: Slab
    """
    WAXED_EXPOSED_CUT_COPPER_SLAB = (22091, Slab)
    """
    BlockData: Slab
    """
    WAXED_WEATHERED_CUT_COPPER_SLAB = (20035, Slab)
    """
    BlockData: Slab
    """
    WAXED_OXIDIZED_CUT_COPPER_SLAB = (11202, Slab)
    """
    BlockData: Slab
    """
    OAK_LOG = (26723, Orientable)
    """
    BlockData: Orientable
    """
    SPRUCE_LOG = (9726, Orientable)
    """
    BlockData: Orientable
    """
    BIRCH_LOG = (26727, Orientable)
    """
    BlockData: Orientable
    """
    JUNGLE_LOG = (20721, Orientable)
    """
    BlockData: Orientable
    """
    ACACIA_LOG = (8385, Orientable)
    """
    BlockData: Orientable
    """
    CHERRY_LOG = (20847, Orientable)
    """
    BlockData: Orientable
    """
    PALE_OAK_LOG = (13346, Orientable)
    """
    BlockData: Orientable
    """
    DARK_OAK_LOG = (14831, Orientable)
    """
    BlockData: Orientable
    """
    MANGROVE_LOG = (23890, Orientable)
    """
    BlockData: Orientable
    """
    MANGROVE_ROOTS = (22124, Waterlogged)
    """
    BlockData: Waterlogged
    """
    MUDDY_MANGROVE_ROOTS = (23244, Orientable)
    """
    BlockData: Orientable
    """
    CRIMSON_STEM = (27920, Orientable)
    """
    BlockData: Orientable
    """
    WARPED_STEM = (28920, Orientable)
    """
    BlockData: Orientable
    """
    BAMBOO_BLOCK = (20770, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_OAK_LOG = (20523, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_SPRUCE_LOG = (6140, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_BIRCH_LOG = (8838, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_JUNGLE_LOG = (15476, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_ACACIA_LOG = (18167, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_CHERRY_LOG = (18061, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_DARK_OAK_LOG = (6492, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_PALE_OAK_LOG = (25375, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_MANGROVE_LOG = (15197, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_CRIMSON_STEM = (16882, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_WARPED_STEM = (15627, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_OAK_WOOD = (31455, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_SPRUCE_WOOD = (6467, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_BIRCH_WOOD = (22350, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_JUNGLE_WOOD = (30315, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_ACACIA_WOOD = (27193, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_CHERRY_WOOD = (19647, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_DARK_OAK_WOOD = (16000, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_PALE_OAK_WOOD = (20330, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_MANGROVE_WOOD = (4828, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_CRIMSON_HYPHAE = (27488, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_WARPED_HYPHAE = (7422, Orientable)
    """
    BlockData: Orientable
    """
    STRIPPED_BAMBOO_BLOCK = (14799, Orientable)
    """
    BlockData: Orientable
    """
    OAK_WOOD = (7378, Orientable)
    """
    BlockData: Orientable
    """
    SPRUCE_WOOD = (32328, Orientable)
    """
    BlockData: Orientable
    """
    BIRCH_WOOD = (20913, Orientable)
    """
    BlockData: Orientable
    """
    JUNGLE_WOOD = (10341, Orientable)
    """
    BlockData: Orientable
    """
    ACACIA_WOOD = (9541, Orientable)
    """
    BlockData: Orientable
    """
    CHERRY_WOOD = (9826, Orientable)
    """
    BlockData: Orientable
    """
    PALE_OAK_WOOD = (29429, Orientable)
    """
    BlockData: Orientable
    """
    DARK_OAK_WOOD = (16995, Orientable)
    """
    BlockData: Orientable
    """
    MANGROVE_WOOD = (25484, Orientable)
    """
    BlockData: Orientable
    """
    CRIMSON_HYPHAE = (6550, Orientable)
    """
    BlockData: Orientable
    """
    WARPED_HYPHAE = (18439, Orientable)
    """
    BlockData: Orientable
    """
    OAK_LEAVES = (4385, Leaves)
    """
    BlockData: Leaves
    """
    SPRUCE_LEAVES = (20039, Leaves)
    """
    BlockData: Leaves
    """
    BIRCH_LEAVES = (12601, Leaves)
    """
    BlockData: Leaves
    """
    JUNGLE_LEAVES = (5133, Leaves)
    """
    BlockData: Leaves
    """
    ACACIA_LEAVES = (16606, Leaves)
    """
    BlockData: Leaves
    """
    CHERRY_LEAVES = (20856, Leaves)
    """
    BlockData: Leaves
    """
    DARK_OAK_LEAVES = (22254, Leaves)
    """
    BlockData: Leaves
    """
    PALE_OAK_LEAVES = (6408, Leaves)
    """
    BlockData: Leaves
    """
    MANGROVE_LEAVES = (15310, Leaves)
    """
    BlockData: Leaves
    """
    AZALEA_LEAVES = (23001, Leaves)
    """
    BlockData: Leaves
    """
    FLOWERING_AZALEA_LEAVES = (7139, Leaves)
    """
    BlockData: Leaves
    """
    SPONGE = (15860)
    WET_SPONGE = (9043)
    GLASS = (6195)
    TINTED_GLASS = (19154)
    LAPIS_BLOCK = (14485)
    SANDSTONE = (13141)
    CHISELED_SANDSTONE = (31763)
    CUT_SANDSTONE = (6118)
    COBWEB = (9469)
    SHORT_GRASS = (16335)
    FERN = (15794)
    AZALEA = (29386)
    FLOWERING_AZALEA = (28270)
    DEAD_BUSH = (22888)
    SEAGRASS = (23942)
    SEA_PICKLE = (19562, SeaPickle)
    """
    BlockData: SeaPickle
    """
    WHITE_WOOL = (8624)
    ORANGE_WOOL = (23957)
    MAGENTA_WOOL = (11853)
    LIGHT_BLUE_WOOL = (21073)
    YELLOW_WOOL = (29507)
    LIME_WOOL = (10443)
    PINK_WOOL = (7611)
    GRAY_WOOL = (27209)
    LIGHT_GRAY_WOOL = (22936)
    CYAN_WOOL = (12221)
    PURPLE_WOOL = (11922)
    BLUE_WOOL = (15738)
    BROWN_WOOL = (32638)
    GREEN_WOOL = (25085)
    RED_WOOL = (11621)
    BLACK_WOOL = (16693)
    DANDELION = (30558)
    POPPY = (12851)
    BLUE_ORCHID = (13432)
    ALLIUM = (6871)
    AZURE_BLUET = (17608)
    RED_TULIP = (16781)
    ORANGE_TULIP = (26038)
    WHITE_TULIP = (31495)
    PINK_TULIP = (27319)
    OXEYE_DAISY = (11709)
    CORNFLOWER = (15405)
    LILY_OF_THE_VALLEY = (7185)
    WITHER_ROSE = (8619)
    TORCHFLOWER = (4501)
    PITCHER_PLANT = (28172, Bisected)
    """
    BlockData: Bisected
    """
    SPORE_BLOSSOM = (20627)
    BROWN_MUSHROOM = (9665)
    RED_MUSHROOM = (19728)
    CRIMSON_FUNGUS = (26268)
    WARPED_FUNGUS = (19799)
    CRIMSON_ROOTS = (14064)
    WARPED_ROOTS = (13932)
    NETHER_SPROUTS = (10431)
    WEEPING_VINES = (29267, Ageable)
    """
    BlockData: Ageable
    """
    TWISTING_VINES = (27283, Ageable)
    """
    BlockData: Ageable
    """
    SUGAR_CANE = (7726, Ageable)
    """
    BlockData: Ageable
    """
    KELP = (21916, Ageable)
    """
    BlockData: Ageable
    """
    PINK_PETALS = (10420, PinkPetals)
    """
    BlockData: PinkPetals
    """
    MOSS_CARPET = (8221)
    MOSS_BLOCK = (9175)
    PALE_MOSS_CARPET = (24824, MossyCarpet)
    """
    BlockData: MossyCarpet
    """
    PALE_HANGING_MOSS = (13108, HangingMoss)
    """
    BlockData: HangingMoss
    """
    PALE_MOSS_BLOCK = (5318)
    HANGING_ROOTS = (15498, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BIG_DRIPLEAF = (26173, BigDripleaf)
    """
    BlockData: BigDripleaf
    """
    SMALL_DRIPLEAF = (17540, SmallDripleaf)
    """
    BlockData: SmallDripleaf
    """
    BAMBOO = (18728, Bamboo)
    """
    BlockData: Bamboo
    """
    OAK_SLAB = (12002, Slab)
    """
    BlockData: Slab
    """
    SPRUCE_SLAB = (28798, Slab)
    """
    BlockData: Slab
    """
    BIRCH_SLAB = (13807, Slab)
    """
    BlockData: Slab
    """
    JUNGLE_SLAB = (19117, Slab)
    """
    BlockData: Slab
    """
    ACACIA_SLAB = (23730, Slab)
    """
    BlockData: Slab
    """
    CHERRY_SLAB = (16673, Slab)
    """
    BlockData: Slab
    """
    DARK_OAK_SLAB = (28852, Slab)
    """
    BlockData: Slab
    """
    PALE_OAK_SLAB = (22048, Slab)
    """
    BlockData: Slab
    """
    MANGROVE_SLAB = (13704, Slab)
    """
    BlockData: Slab
    """
    BAMBOO_SLAB = (17798, Slab)
    """
    BlockData: Slab
    """
    BAMBOO_MOSAIC_SLAB = (22118, Slab)
    """
    BlockData: Slab
    """
    CRIMSON_SLAB = (4691, Slab)
    """
    BlockData: Slab
    """
    WARPED_SLAB = (27150, Slab)
    """
    BlockData: Slab
    """
    STONE_SLAB = (19838, Slab)
    """
    BlockData: Slab
    """
    SMOOTH_STONE_SLAB = (24129, Slab)
    """
    BlockData: Slab
    """
    SANDSTONE_SLAB = (29830, Slab)
    """
    BlockData: Slab
    """
    CUT_SANDSTONE_SLAB = (30944, Slab)
    """
    BlockData: Slab
    """
    PETRIFIED_OAK_SLAB = (18658, Slab)
    """
    BlockData: Slab
    """
    COBBLESTONE_SLAB = (6340, Slab)
    """
    BlockData: Slab
    """
    BRICK_SLAB = (26333, Slab)
    """
    BlockData: Slab
    """
    STONE_BRICK_SLAB = (19676, Slab)
    """
    BlockData: Slab
    """
    MUD_BRICK_SLAB = (10611, Slab)
    """
    BlockData: Slab
    """
    NETHER_BRICK_SLAB = (26586, Slab)
    """
    BlockData: Slab
    """
    QUARTZ_SLAB = (4423, Slab)
    """
    BlockData: Slab
    """
    RED_SANDSTONE_SLAB = (17550, Slab)
    """
    BlockData: Slab
    """
    CUT_RED_SANDSTONE_SLAB = (7220, Slab)
    """
    BlockData: Slab
    """
    PURPUR_SLAB = (11487, Slab)
    """
    BlockData: Slab
    """
    PRISMARINE_SLAB = (31323, Slab)
    """
    BlockData: Slab
    """
    PRISMARINE_BRICK_SLAB = (25624, Slab)
    """
    BlockData: Slab
    """
    DARK_PRISMARINE_SLAB = (7577, Slab)
    """
    BlockData: Slab
    """
    SMOOTH_QUARTZ = (14415)
    SMOOTH_RED_SANDSTONE = (25180)
    SMOOTH_SANDSTONE = (30039)
    SMOOTH_STONE = (21910)
    BRICKS = (14165)
    BOOKSHELF = (10069)
    CHISELED_BOOKSHELF = (8099, ChiseledBookshelf)
    """
    BlockData: ChiseledBookshelf
    """
    DECORATED_POT = (8720, DecoratedPot)
    """
    BlockData: DecoratedPot
    """
    MOSSY_COBBLESTONE = (21900)
    OBSIDIAN = (32723)
    TORCH = (6063)
    END_ROD = (24832, Directional)
    """
    BlockData: Directional
    """
    CHORUS_PLANT = (28243, MultipleFacing)
    """
    BlockData: MultipleFacing
    """
    CHORUS_FLOWER = (28542, Ageable)
    """
    BlockData: Ageable
    """
    PURPUR_BLOCK = (7538)
    PURPUR_PILLAR = (26718, Orientable)
    """
    BlockData: Orientable
    """
    PURPUR_STAIRS = (8921, Stairs)
    """
    BlockData: Stairs
    """
    SPAWNER = (7018)
    CREAKING_HEART = (11442, CreakingHeart)
    """
    BlockData: CreakingHeart
    """
    CHEST = (22969, Chest)
    """
    BlockData: Chest
    """
    CRAFTING_TABLE = (20706)
    FARMLAND = (31166, Farmland)
    """
    BlockData: Farmland
    """
    FURNACE = (8133, Furnace)
    """
    BlockData: Furnace
    """
    LADDER = (23599, Ladder)
    """
    BlockData: Ladder
    """
    COBBLESTONE_STAIRS = (24715, Stairs)
    """
    BlockData: Stairs
    """
    SNOW = (14146, Snow)
    """
    BlockData: Snow
    """
    ICE = (30428)
    SNOW_BLOCK = (19913)
    CACTUS = (12191, Ageable)
    """
    BlockData: Ageable
    """
    CLAY = (27880)
    JUKEBOX = (19264, Jukebox)
    """
    BlockData: Jukebox
    """
    OAK_FENCE = (6442, Fence)
    """
    BlockData: Fence
    """
    SPRUCE_FENCE = (25416, Fence)
    """
    BlockData: Fence
    """
    BIRCH_FENCE = (17347, Fence)
    """
    BlockData: Fence
    """
    JUNGLE_FENCE = (14358, Fence)
    """
    BlockData: Fence
    """
    ACACIA_FENCE = (4569, Fence)
    """
    BlockData: Fence
    """
    CHERRY_FENCE = (32047, Fence)
    """
    BlockData: Fence
    """
    DARK_OAK_FENCE = (21767, Fence)
    """
    BlockData: Fence
    """
    PALE_OAK_FENCE = (10547, Fence)
    """
    BlockData: Fence
    """
    MANGROVE_FENCE = (15021, Fence)
    """
    BlockData: Fence
    """
    BAMBOO_FENCE = (17207, Fence)
    """
    BlockData: Fence
    """
    CRIMSON_FENCE = (21075, Fence)
    """
    BlockData: Fence
    """
    WARPED_FENCE = (18438, Fence)
    """
    BlockData: Fence
    """
    PUMPKIN = (19170)
    CARVED_PUMPKIN = (25833, Directional)
    """
    BlockData: Directional
    """
    JACK_O_LANTERN = (13758, Directional)
    """
    BlockData: Directional
    """
    NETHERRACK = (23425)
    SOUL_SAND = (16841)
    SOUL_SOIL = (31140)
    BASALT = (28478, Orientable)
    """
    BlockData: Orientable
    """
    POLISHED_BASALT = (11659, Orientable)
    """
    BlockData: Orientable
    """
    SMOOTH_BASALT = (13617)
    SOUL_TORCH = (14292)
    GLOWSTONE = (32713)
    INFESTED_STONE = (18440)
    INFESTED_COBBLESTONE = (4348)
    INFESTED_STONE_BRICKS = (19749)
    INFESTED_MOSSY_STONE_BRICKS = (9850)
    INFESTED_CRACKED_STONE_BRICKS = (7476)
    INFESTED_CHISELED_STONE_BRICKS = (4728)
    INFESTED_DEEPSLATE = (9472, Orientable)
    """
    BlockData: Orientable
    """
    STONE_BRICKS = (6962)
    MOSSY_STONE_BRICKS = (16415)
    CRACKED_STONE_BRICKS = (27869)
    CHISELED_STONE_BRICKS = (9087)
    PACKED_MUD = (7472)
    MUD_BRICKS = (29168)
    DEEPSLATE_BRICKS = (13193)
    CRACKED_DEEPSLATE_BRICKS = (17105)
    DEEPSLATE_TILES = (11250)
    CRACKED_DEEPSLATE_TILES = (26249)
    CHISELED_DEEPSLATE = (23825)
    REINFORCED_DEEPSLATE = (10949)
    BROWN_MUSHROOM_BLOCK = (6291, MultipleFacing)
    """
    BlockData: MultipleFacing
    """
    RED_MUSHROOM_BLOCK = (20766, MultipleFacing)
    """
    BlockData: MultipleFacing
    """
    MUSHROOM_STEM = (16543, MultipleFacing)
    """
    BlockData: MultipleFacing
    """
    IRON_BARS = (9378, Fence)
    """
    BlockData: Fence
    """
    CHAIN = (28265, Chain)
    """
    BlockData: Chain
    """
    GLASS_PANE = (5709, Fence)
    """
    BlockData: Fence
    """
    MELON = (25172)
    VINE = (14564, MultipleFacing)
    """
    BlockData: MultipleFacing
    """
    GLOW_LICHEN = (19165, GlowLichen)
    """
    BlockData: GlowLichen
    """
    BRICK_STAIRS = (21534, Stairs)
    """
    BlockData: Stairs
    """
    STONE_BRICK_STAIRS = (27032, Stairs)
    """
    BlockData: Stairs
    """
    MUD_BRICK_STAIRS = (13620, Stairs)
    """
    BlockData: Stairs
    """
    MYCELIUM = (9913, Snowable)
    """
    BlockData: Snowable
    """
    LILY_PAD = (19271)
    NETHER_BRICKS = (27802)
    CRACKED_NETHER_BRICKS = (10888)
    CHISELED_NETHER_BRICKS = (21613)
    NETHER_BRICK_FENCE = (5286, Fence)
    """
    BlockData: Fence
    """
    NETHER_BRICK_STAIRS = (12085, Stairs)
    """
    BlockData: Stairs
    """
    SCULK = (17870)
    SCULK_VEIN = (11615, SculkVein)
    """
    BlockData: SculkVein
    """
    SCULK_CATALYST = (12017, SculkCatalyst)
    """
    BlockData: SculkCatalyst
    """
    SCULK_SHRIEKER = (20985, SculkShrieker)
    """
    BlockData: SculkShrieker
    """
    ENCHANTING_TABLE = (16255)
    END_PORTAL_FRAME = (15480, EndPortalFrame)
    """
    BlockData: EndPortalFrame
    """
    END_STONE = (29686)
    END_STONE_BRICKS = (20314)
    DRAGON_EGG = (29946)
    SANDSTONE_STAIRS = (18474, Stairs)
    """
    BlockData: Stairs
    """
    ENDER_CHEST = (32349, EnderChest)
    """
    BlockData: EnderChest
    """
    EMERALD_BLOCK = (9914)
    OAK_STAIRS = (5449, Stairs)
    """
    BlockData: Stairs
    """
    SPRUCE_STAIRS = (11192, Stairs)
    """
    BlockData: Stairs
    """
    BIRCH_STAIRS = (7657, Stairs)
    """
    BlockData: Stairs
    """
    JUNGLE_STAIRS = (20636, Stairs)
    """
    BlockData: Stairs
    """
    ACACIA_STAIRS = (17453, Stairs)
    """
    BlockData: Stairs
    """
    CHERRY_STAIRS = (18380, Stairs)
    """
    BlockData: Stairs
    """
    DARK_OAK_STAIRS = (22921, Stairs)
    """
    BlockData: Stairs
    """
    PALE_OAK_STAIRS = (20755, Stairs)
    """
    BlockData: Stairs
    """
    MANGROVE_STAIRS = (27641, Stairs)
    """
    BlockData: Stairs
    """
    BAMBOO_STAIRS = (25674, Stairs)
    """
    BlockData: Stairs
    """
    BAMBOO_MOSAIC_STAIRS = (20977, Stairs)
    """
    BlockData: Stairs
    """
    CRIMSON_STAIRS = (32442, Stairs)
    """
    BlockData: Stairs
    """
    WARPED_STAIRS = (17721, Stairs)
    """
    BlockData: Stairs
    """
    COMMAND_BLOCK = (4355, CommandBlock)
    """
    BlockData: CommandBlock
    """
    BEACON = (6608)
    COBBLESTONE_WALL = (12616, Wall)
    """
    BlockData: Wall
    """
    MOSSY_COBBLESTONE_WALL = (11536, Wall)
    """
    BlockData: Wall
    """
    BRICK_WALL = (18995, Wall)
    """
    BlockData: Wall
    """
    PRISMARINE_WALL = (18184, Wall)
    """
    BlockData: Wall
    """
    RED_SANDSTONE_WALL = (4753, Wall)
    """
    BlockData: Wall
    """
    MOSSY_STONE_BRICK_WALL = (18259, Wall)
    """
    BlockData: Wall
    """
    GRANITE_WALL = (23279, Wall)
    """
    BlockData: Wall
    """
    STONE_BRICK_WALL = (29073, Wall)
    """
    BlockData: Wall
    """
    MUD_BRICK_WALL = (18292, Wall)
    """
    BlockData: Wall
    """
    NETHER_BRICK_WALL = (10398, Wall)
    """
    BlockData: Wall
    """
    ANDESITE_WALL = (14938, Wall)
    """
    BlockData: Wall
    """
    RED_NETHER_BRICK_WALL = (4580, Wall)
    """
    BlockData: Wall
    """
    SANDSTONE_WALL = (18470, Wall)
    """
    BlockData: Wall
    """
    END_STONE_BRICK_WALL = (27225, Wall)
    """
    BlockData: Wall
    """
    DIORITE_WALL = (17412, Wall)
    """
    BlockData: Wall
    """
    BLACKSTONE_WALL = (17327, Wall)
    """
    BlockData: Wall
    """
    POLISHED_BLACKSTONE_WALL = (15119, Wall)
    """
    BlockData: Wall
    """
    POLISHED_BLACKSTONE_BRICK_WALL = (9540, Wall)
    """
    BlockData: Wall
    """
    COBBLED_DEEPSLATE_WALL = (21893, Wall)
    """
    BlockData: Wall
    """
    POLISHED_DEEPSLATE_WALL = (6574, Wall)
    """
    BlockData: Wall
    """
    DEEPSLATE_BRICK_WALL = (13304, Wall)
    """
    BlockData: Wall
    """
    DEEPSLATE_TILE_WALL = (17077, Wall)
    """
    BlockData: Wall
    """
    ANVIL = (18718, Directional)
    """
    BlockData: Directional
    """
    CHIPPED_ANVIL = (10623, Directional)
    """
    BlockData: Directional
    """
    DAMAGED_ANVIL = (10274, Directional)
    """
    BlockData: Directional
    """
    CHISELED_QUARTZ_BLOCK = (30964)
    QUARTZ_BLOCK = (11987)
    QUARTZ_BRICKS = (23358)
    QUARTZ_PILLAR = (16452, Orientable)
    """
    BlockData: Orientable
    """
    QUARTZ_STAIRS = (24079, Stairs)
    """
    BlockData: Stairs
    """
    WHITE_TERRACOTTA = (20975)
    ORANGE_TERRACOTTA = (18684)
    MAGENTA_TERRACOTTA = (25900)
    LIGHT_BLUE_TERRACOTTA = (31779)
    YELLOW_TERRACOTTA = (32129)
    LIME_TERRACOTTA = (24013)
    PINK_TERRACOTTA = (23727)
    GRAY_TERRACOTTA = (18004)
    LIGHT_GRAY_TERRACOTTA = (26388)
    CYAN_TERRACOTTA = (25940)
    PURPLE_TERRACOTTA = (10387)
    BLUE_TERRACOTTA = (5236)
    BROWN_TERRACOTTA = (23664)
    GREEN_TERRACOTTA = (4105)
    RED_TERRACOTTA = (5086)
    BLACK_TERRACOTTA = (26691)
    BARRIER = (26453, Waterlogged)
    """
    BlockData: Waterlogged
    """
    LIGHT = (17829, Light)
    """
    BlockData: Light
    """
    HAY_BLOCK = (17461, Orientable)
    """
    BlockData: Orientable
    """
    WHITE_CARPET = (15117)
    ORANGE_CARPET = (24752)
    MAGENTA_CARPET = (6180)
    LIGHT_BLUE_CARPET = (21194)
    YELLOW_CARPET = (18149)
    LIME_CARPET = (15443)
    PINK_CARPET = (27381)
    GRAY_CARPET = (26991)
    LIGHT_GRAY_CARPET = (11317)
    CYAN_CARPET = (9742)
    PURPLE_CARPET = (5574)
    BLUE_CARPET = (13292)
    BROWN_CARPET = (23352)
    GREEN_CARPET = (7780)
    RED_CARPET = (5424)
    BLACK_CARPET = (6056)
    TERRACOTTA = (16544)
    PACKED_ICE = (28993)
    DIRT_PATH = (10846)
    SUNFLOWER = (7408, Bisected)
    """
    BlockData: Bisected
    """
    LILAC = (22837, Bisected)
    """
    BlockData: Bisected
    """
    ROSE_BUSH = (6080, Bisected)
    """
    BlockData: Bisected
    """
    PEONY = (21155, Bisected)
    """
    BlockData: Bisected
    """
    TALL_GRASS = (21559, Bisected)
    """
    BlockData: Bisected
    """
    LARGE_FERN = (30177, Bisected)
    """
    BlockData: Bisected
    """
    WHITE_STAINED_GLASS = (31190)
    ORANGE_STAINED_GLASS = (25142)
    MAGENTA_STAINED_GLASS = (26814)
    LIGHT_BLUE_STAINED_GLASS = (17162)
    YELLOW_STAINED_GLASS = (12182)
    LIME_STAINED_GLASS = (24266)
    PINK_STAINED_GLASS = (16164)
    GRAY_STAINED_GLASS = (29979)
    LIGHT_GRAY_STAINED_GLASS = (5843)
    CYAN_STAINED_GLASS = (30604)
    PURPLE_STAINED_GLASS = (21845)
    BLUE_STAINED_GLASS = (7107)
    BROWN_STAINED_GLASS = (20945)
    GREEN_STAINED_GLASS = (22503)
    RED_STAINED_GLASS = (9717)
    BLACK_STAINED_GLASS = (13941)
    WHITE_STAINED_GLASS_PANE = (10557, GlassPane)
    """
    BlockData: GlassPane
    """
    ORANGE_STAINED_GLASS_PANE = (21089, GlassPane)
    """
    BlockData: GlassPane
    """
    MAGENTA_STAINED_GLASS_PANE = (14082, GlassPane)
    """
    BlockData: GlassPane
    """
    LIGHT_BLUE_STAINED_GLASS_PANE = (18721, GlassPane)
    """
    BlockData: GlassPane
    """
    YELLOW_STAINED_GLASS_PANE = (20298, GlassPane)
    """
    BlockData: GlassPane
    """
    LIME_STAINED_GLASS_PANE = (10610, GlassPane)
    """
    BlockData: GlassPane
    """
    PINK_STAINED_GLASS_PANE = (24637, GlassPane)
    """
    BlockData: GlassPane
    """
    GRAY_STAINED_GLASS_PANE = (25272, GlassPane)
    """
    BlockData: GlassPane
    """
    LIGHT_GRAY_STAINED_GLASS_PANE = (19008, GlassPane)
    """
    BlockData: GlassPane
    """
    CYAN_STAINED_GLASS_PANE = (11784, GlassPane)
    """
    BlockData: GlassPane
    """
    PURPLE_STAINED_GLASS_PANE = (10948, GlassPane)
    """
    BlockData: GlassPane
    """
    BLUE_STAINED_GLASS_PANE = (28484, GlassPane)
    """
    BlockData: GlassPane
    """
    BROWN_STAINED_GLASS_PANE = (17557, GlassPane)
    """
    BlockData: GlassPane
    """
    GREEN_STAINED_GLASS_PANE = (4767, GlassPane)
    """
    BlockData: GlassPane
    """
    RED_STAINED_GLASS_PANE = (8630, GlassPane)
    """
    BlockData: GlassPane
    """
    BLACK_STAINED_GLASS_PANE = (13201, GlassPane)
    """
    BlockData: GlassPane
    """
    PRISMARINE = (7539)
    PRISMARINE_BRICKS = (29118)
    DARK_PRISMARINE = (19940)
    PRISMARINE_STAIRS = (19217, Stairs)
    """
    BlockData: Stairs
    """
    PRISMARINE_BRICK_STAIRS = (15445, Stairs)
    """
    BlockData: Stairs
    """
    DARK_PRISMARINE_STAIRS = (26511, Stairs)
    """
    BlockData: Stairs
    """
    SEA_LANTERN = (20780)
    RED_SANDSTONE = (9092)
    CHISELED_RED_SANDSTONE = (15529)
    CUT_RED_SANDSTONE = (29108)
    RED_SANDSTONE_STAIRS = (25466, Stairs)
    """
    BlockData: Stairs
    """
    REPEATING_COMMAND_BLOCK = (12405, CommandBlock)
    """
    BlockData: CommandBlock
    """
    CHAIN_COMMAND_BLOCK = (26798, CommandBlock)
    """
    BlockData: CommandBlock
    """
    MAGMA_BLOCK = (25927)
    NETHER_WART_BLOCK = (15486)
    WARPED_WART_BLOCK = (15463)
    RED_NETHER_BRICKS = (18056)
    BONE_BLOCK = (17312, Orientable)
    """
    BlockData: Orientable
    """
    STRUCTURE_VOID = (30806)
    SHULKER_BOX = (7776, 1, Directional)
    """
    BlockData: Directional
    """
    WHITE_SHULKER_BOX = (31750, 1, Directional)
    """
    BlockData: Directional
    """
    ORANGE_SHULKER_BOX = (21673, 1, Directional)
    """
    BlockData: Directional
    """
    MAGENTA_SHULKER_BOX = (21566, 1, Directional)
    """
    BlockData: Directional
    """
    LIGHT_BLUE_SHULKER_BOX = (18226, 1, Directional)
    """
    BlockData: Directional
    """
    YELLOW_SHULKER_BOX = (28700, 1, Directional)
    """
    BlockData: Directional
    """
    LIME_SHULKER_BOX = (28360, 1, Directional)
    """
    BlockData: Directional
    """
    PINK_SHULKER_BOX = (24968, 1, Directional)
    """
    BlockData: Directional
    """
    GRAY_SHULKER_BOX = (12754, 1, Directional)
    """
    BlockData: Directional
    """
    LIGHT_GRAY_SHULKER_BOX = (21345, 1, Directional)
    """
    BlockData: Directional
    """
    CYAN_SHULKER_BOX = (28123, 1, Directional)
    """
    BlockData: Directional
    """
    PURPLE_SHULKER_BOX = (10373, 1, Directional)
    """
    BlockData: Directional
    """
    BLUE_SHULKER_BOX = (11476, 1, Directional)
    """
    BlockData: Directional
    """
    BROWN_SHULKER_BOX = (24230, 1, Directional)
    """
    BlockData: Directional
    """
    GREEN_SHULKER_BOX = (9377, 1, Directional)
    """
    BlockData: Directional
    """
    RED_SHULKER_BOX = (32448, 1, Directional)
    """
    BlockData: Directional
    """
    BLACK_SHULKER_BOX = (24076, 1, Directional)
    """
    BlockData: Directional
    """
    WHITE_GLAZED_TERRACOTTA = (11326, Directional)
    """
    BlockData: Directional
    """
    ORANGE_GLAZED_TERRACOTTA = (27451, Directional)
    """
    BlockData: Directional
    """
    MAGENTA_GLAZED_TERRACOTTA = (8067, Directional)
    """
    BlockData: Directional
    """
    LIGHT_BLUE_GLAZED_TERRACOTTA = (4336, Directional)
    """
    BlockData: Directional
    """
    YELLOW_GLAZED_TERRACOTTA = (10914, Directional)
    """
    BlockData: Directional
    """
    LIME_GLAZED_TERRACOTTA = (13861, Directional)
    """
    BlockData: Directional
    """
    PINK_GLAZED_TERRACOTTA = (10260, Directional)
    """
    BlockData: Directional
    """
    GRAY_GLAZED_TERRACOTTA = (6256, Directional)
    """
    BlockData: Directional
    """
    LIGHT_GRAY_GLAZED_TERRACOTTA = (10707, Directional)
    """
    BlockData: Directional
    """
    CYAN_GLAZED_TERRACOTTA = (9550, Directional)
    """
    BlockData: Directional
    """
    PURPLE_GLAZED_TERRACOTTA = (4818, Directional)
    """
    BlockData: Directional
    """
    BLUE_GLAZED_TERRACOTTA = (23823, Directional)
    """
    BlockData: Directional
    """
    BROWN_GLAZED_TERRACOTTA = (5655, Directional)
    """
    BlockData: Directional
    """
    GREEN_GLAZED_TERRACOTTA = (6958, Directional)
    """
    BlockData: Directional
    """
    RED_GLAZED_TERRACOTTA = (24989, Directional)
    """
    BlockData: Directional
    """
    BLACK_GLAZED_TERRACOTTA = (29678, Directional)
    """
    BlockData: Directional
    """
    WHITE_CONCRETE = (6281)
    ORANGE_CONCRETE = (19914)
    MAGENTA_CONCRETE = (20591)
    LIGHT_BLUE_CONCRETE = (29481)
    YELLOW_CONCRETE = (15722)
    LIME_CONCRETE = (5863)
    PINK_CONCRETE = (5227)
    GRAY_CONCRETE = (13959)
    LIGHT_GRAY_CONCRETE = (14453)
    CYAN_CONCRETE = (26522)
    PURPLE_CONCRETE = (20623)
    BLUE_CONCRETE = (18756)
    BROWN_CONCRETE = (19006)
    GREEN_CONCRETE = (17949)
    RED_CONCRETE = (8032)
    BLACK_CONCRETE = (13338)
    WHITE_CONCRETE_POWDER = (10363)
    ORANGE_CONCRETE_POWDER = (30159)
    MAGENTA_CONCRETE_POWDER = (8272)
    LIGHT_BLUE_CONCRETE_POWDER = (31206)
    YELLOW_CONCRETE_POWDER = (10655)
    LIME_CONCRETE_POWDER = (28859)
    PINK_CONCRETE_POWDER = (6421)
    GRAY_CONCRETE_POWDER = (13031)
    LIGHT_GRAY_CONCRETE_POWDER = (21589)
    CYAN_CONCRETE_POWDER = (15734)
    PURPLE_CONCRETE_POWDER = (26808)
    BLUE_CONCRETE_POWDER = (17773)
    BROWN_CONCRETE_POWDER = (21485)
    GREEN_CONCRETE_POWDER = (6904)
    RED_CONCRETE_POWDER = (13286)
    BLACK_CONCRETE_POWDER = (16150)
    TURTLE_EGG = (32101, TurtleEgg)
    """
    BlockData: TurtleEgg
    """
    SNIFFER_EGG = (12980, Hatchable)
    """
    BlockData: Hatchable
    """
    DEAD_TUBE_CORAL_BLOCK = (28350)
    DEAD_BRAIN_CORAL_BLOCK = (12979)
    DEAD_BUBBLE_CORAL_BLOCK = (28220)
    DEAD_FIRE_CORAL_BLOCK = (5307)
    DEAD_HORN_CORAL_BLOCK = (15103)
    TUBE_CORAL_BLOCK = (23723)
    BRAIN_CORAL_BLOCK = (30618)
    BUBBLE_CORAL_BLOCK = (15437)
    FIRE_CORAL_BLOCK = (12119)
    HORN_CORAL_BLOCK = (19958)
    TUBE_CORAL = (23048, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BRAIN_CORAL = (31316, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BUBBLE_CORAL = (12464, Waterlogged)
    """
    BlockData: Waterlogged
    """
    FIRE_CORAL = (29151, Waterlogged)
    """
    BlockData: Waterlogged
    """
    HORN_CORAL = (19511, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_BRAIN_CORAL = (9116, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_BUBBLE_CORAL = (30583, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_FIRE_CORAL = (8365, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_HORN_CORAL = (5755, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_TUBE_CORAL = (18028, Waterlogged)
    """
    BlockData: Waterlogged
    """
    TUBE_CORAL_FAN = (19929, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BRAIN_CORAL_FAN = (13849, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BUBBLE_CORAL_FAN = (10795, Waterlogged)
    """
    BlockData: Waterlogged
    """
    FIRE_CORAL_FAN = (11112, Waterlogged)
    """
    BlockData: Waterlogged
    """
    HORN_CORAL_FAN = (13610, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_TUBE_CORAL_FAN = (17628, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_BRAIN_CORAL_FAN = (26150, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_BUBBLE_CORAL_FAN = (17322, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_FIRE_CORAL_FAN = (27073, Waterlogged)
    """
    BlockData: Waterlogged
    """
    DEAD_HORN_CORAL_FAN = (11387, Waterlogged)
    """
    BlockData: Waterlogged
    """
    BLUE_ICE = (22449)
    CONDUIT = (5148, Waterlogged)
    """
    BlockData: Waterlogged
    """
    POLISHED_GRANITE_STAIRS = (29588, Stairs)
    """
    BlockData: Stairs
    """
    SMOOTH_RED_SANDSTONE_STAIRS = (17561, Stairs)
    """
    BlockData: Stairs
    """
    MOSSY_STONE_BRICK_STAIRS = (27578, Stairs)
    """
    BlockData: Stairs
    """
    POLISHED_DIORITE_STAIRS = (4625, Stairs)
    """
    BlockData: Stairs
    """
    MOSSY_COBBLESTONE_STAIRS = (29210, Stairs)
    """
    BlockData: Stairs
    """
    END_STONE_BRICK_STAIRS = (28831, Stairs)
    """
    BlockData: Stairs
    """
    STONE_STAIRS = (23784, Stairs)
    """
    BlockData: Stairs
    """
    SMOOTH_SANDSTONE_STAIRS = (21183, Stairs)
    """
    BlockData: Stairs
    """
    SMOOTH_QUARTZ_STAIRS = (19560, Stairs)
    """
    BlockData: Stairs
    """
    GRANITE_STAIRS = (21840, Stairs)
    """
    BlockData: Stairs
    """
    ANDESITE_STAIRS = (17747, Stairs)
    """
    BlockData: Stairs
    """
    RED_NETHER_BRICK_STAIRS = (26374, Stairs)
    """
    BlockData: Stairs
    """
    POLISHED_ANDESITE_STAIRS = (7573, Stairs)
    """
    BlockData: Stairs
    """
    DIORITE_STAIRS = (13134, Stairs)
    """
    BlockData: Stairs
    """
    COBBLED_DEEPSLATE_STAIRS = (20699, Stairs)
    """
    BlockData: Stairs
    """
    POLISHED_DEEPSLATE_STAIRS = (19513, Stairs)
    """
    BlockData: Stairs
    """
    DEEPSLATE_BRICK_STAIRS = (29624, Stairs)
    """
    BlockData: Stairs
    """
    DEEPSLATE_TILE_STAIRS = (6361, Stairs)
    """
    BlockData: Stairs
    """
    POLISHED_GRANITE_SLAB = (4521, Slab)
    """
    BlockData: Slab
    """
    SMOOTH_RED_SANDSTONE_SLAB = (16304, Slab)
    """
    BlockData: Slab
    """
    MOSSY_STONE_BRICK_SLAB = (14002, Slab)
    """
    BlockData: Slab
    """
    POLISHED_DIORITE_SLAB = (18303, Slab)
    """
    BlockData: Slab
    """
    MOSSY_COBBLESTONE_SLAB = (12139, Slab)
    """
    BlockData: Slab
    """
    END_STONE_BRICK_SLAB = (23239, Slab)
    """
    BlockData: Slab
    """
    SMOOTH_SANDSTONE_SLAB = (9030, Slab)
    """
    BlockData: Slab
    """
    SMOOTH_QUARTZ_SLAB = (26543, Slab)
    """
    BlockData: Slab
    """
    GRANITE_SLAB = (10901, Slab)
    """
    BlockData: Slab
    """
    ANDESITE_SLAB = (32124, Slab)
    """
    BlockData: Slab
    """
    RED_NETHER_BRICK_SLAB = (12462, Slab)
    """
    BlockData: Slab
    """
    POLISHED_ANDESITE_SLAB = (24573, Slab)
    """
    BlockData: Slab
    """
    DIORITE_SLAB = (25526, Slab)
    """
    BlockData: Slab
    """
    COBBLED_DEEPSLATE_SLAB = (17388, Slab)
    """
    BlockData: Slab
    """
    POLISHED_DEEPSLATE_SLAB = (32201, Slab)
    """
    BlockData: Slab
    """
    DEEPSLATE_BRICK_SLAB = (23910, Slab)
    """
    BlockData: Slab
    """
    DEEPSLATE_TILE_SLAB = (13315, Slab)
    """
    BlockData: Slab
    """
    SCAFFOLDING = (15757, Scaffolding)
    """
    BlockData: Scaffolding
    """
    REDSTONE = (11233)
    REDSTONE_TORCH = (22547, Lightable)
    """
    BlockData: Lightable
    """
    REDSTONE_BLOCK = (19496)
    REPEATER = (28823, Repeater)
    """
    BlockData: Repeater
    """
    COMPARATOR = (18911, Comparator)
    """
    BlockData: Comparator
    """
    PISTON = (21130, Piston)
    """
    BlockData: Piston
    """
    STICKY_PISTON = (18127, Piston)
    """
    BlockData: Piston
    """
    SLIME_BLOCK = (31892)
    HONEY_BLOCK = (30615)
    OBSERVER = (10726, Observer)
    """
    BlockData: Observer
    """
    HOPPER = (31974, Hopper)
    """
    BlockData: Hopper
    """
    DISPENSER = (20871, Dispenser)
    """
    BlockData: Dispenser
    """
    DROPPER = (31273, Dispenser)
    """
    BlockData: Dispenser
    """
    LECTERN = (23490, Lectern)
    """
    BlockData: Lectern
    """
    TARGET = (22637, AnaloguePowerable)
    """
    BlockData: AnaloguePowerable
    """
    LEVER = (15319, Switch)
    """
    BlockData: Switch
    """
    LIGHTNING_ROD = (30770, LightningRod)
    """
    BlockData: LightningRod
    """
    DAYLIGHT_DETECTOR = (8864, DaylightDetector)
    """
    BlockData: DaylightDetector
    """
    SCULK_SENSOR = (5598, SculkSensor)
    """
    BlockData: SculkSensor
    """
    CALIBRATED_SCULK_SENSOR = (21034, CalibratedSculkSensor)
    """
    BlockData: CalibratedSculkSensor
    """
    TRIPWIRE_HOOK = (8130, TripwireHook)
    """
    BlockData: TripwireHook
    """
    TRAPPED_CHEST = (18970, Chest)
    """
    BlockData: Chest
    """
    TNT = (7896, TNT)
    """
    BlockData: TNT
    """
    REDSTONE_LAMP = (8217, Lightable)
    """
    BlockData: Lightable
    """
    NOTE_BLOCK = (20979, NoteBlock)
    """
    BlockData: NoteBlock
    """
    STONE_BUTTON = (12279, Switch)
    """
    BlockData: Switch
    """
    POLISHED_BLACKSTONE_BUTTON = (20760, Switch)
    """
    BlockData: Switch
    """
    OAK_BUTTON = (13510, Switch)
    """
    BlockData: Switch
    """
    SPRUCE_BUTTON = (23281, Switch)
    """
    BlockData: Switch
    """
    BIRCH_BUTTON = (26934, Switch)
    """
    BlockData: Switch
    """
    JUNGLE_BUTTON = (25317, Switch)
    """
    BlockData: Switch
    """
    ACACIA_BUTTON = (13993, Switch)
    """
    BlockData: Switch
    """
    CHERRY_BUTTON = (9058, Switch)
    """
    BlockData: Switch
    """
    DARK_OAK_BUTTON = (6214, Switch)
    """
    BlockData: Switch
    """
    PALE_OAK_BUTTON = (5238, Switch)
    """
    BlockData: Switch
    """
    MANGROVE_BUTTON = (9838, Switch)
    """
    BlockData: Switch
    """
    BAMBOO_BUTTON = (21810, Switch)
    """
    BlockData: Switch
    """
    CRIMSON_BUTTON = (26799, Switch)
    """
    BlockData: Switch
    """
    WARPED_BUTTON = (25264, Switch)
    """
    BlockData: Switch
    """
    STONE_PRESSURE_PLATE = (22591, Powerable)
    """
    BlockData: Powerable
    """
    POLISHED_BLACKSTONE_PRESSURE_PLATE = (32340, Powerable)
    """
    BlockData: Powerable
    """
    LIGHT_WEIGHTED_PRESSURE_PLATE = (14875, AnaloguePowerable)
    """
    BlockData: AnaloguePowerable
    """
    HEAVY_WEIGHTED_PRESSURE_PLATE = (16970, AnaloguePowerable)
    """
    BlockData: AnaloguePowerable
    """
    OAK_PRESSURE_PLATE = (20108, Powerable)
    """
    BlockData: Powerable
    """
    SPRUCE_PRESSURE_PLATE = (15932, Powerable)
    """
    BlockData: Powerable
    """
    BIRCH_PRESSURE_PLATE = (9664, Powerable)
    """
    BlockData: Powerable
    """
    JUNGLE_PRESSURE_PLATE = (11376, Powerable)
    """
    BlockData: Powerable
    """
    ACACIA_PRESSURE_PLATE = (17586, Powerable)
    """
    BlockData: Powerable
    """
    CHERRY_PRESSURE_PLATE = (8651, Powerable)
    """
    BlockData: Powerable
    """
    DARK_OAK_PRESSURE_PLATE = (31375, Powerable)
    """
    BlockData: Powerable
    """
    PALE_OAK_PRESSURE_PLATE = (30527, Powerable)
    """
    BlockData: Powerable
    """
    MANGROVE_PRESSURE_PLATE = (9748, Powerable)
    """
    BlockData: Powerable
    """
    BAMBOO_PRESSURE_PLATE = (26740, Powerable)
    """
    BlockData: Powerable
    """
    CRIMSON_PRESSURE_PLATE = (18316, Powerable)
    """
    BlockData: Powerable
    """
    WARPED_PRESSURE_PLATE = (29516, Powerable)
    """
    BlockData: Powerable
    """
    IRON_DOOR = (4788, Door)
    """
    BlockData: Door
    """
    OAK_DOOR = (20341, Door)
    """
    BlockData: Door
    """
    SPRUCE_DOOR = (10642, Door)
    """
    BlockData: Door
    """
    BIRCH_DOOR = (14759, Door)
    """
    BlockData: Door
    """
    JUNGLE_DOOR = (28163, Door)
    """
    BlockData: Door
    """
    ACACIA_DOOR = (23797, Door)
    """
    BlockData: Door
    """
    CHERRY_DOOR = (12684, Door)
    """
    BlockData: Door
    """
    DARK_OAK_DOOR = (10669, Door)
    """
    BlockData: Door
    """
    PALE_OAK_DOOR = (23817, Door)
    """
    BlockData: Door
    """
    MANGROVE_DOOR = (18964, Door)
    """
    BlockData: Door
    """
    BAMBOO_DOOR = (19971, Door)
    """
    BlockData: Door
    """
    CRIMSON_DOOR = (19544, Door)
    """
    BlockData: Door
    """
    WARPED_DOOR = (15062, Door)
    """
    BlockData: Door
    """
    COPPER_DOOR = (26809, Door)
    """
    BlockData: Door
    """
    EXPOSED_COPPER_DOOR = (13236, Door)
    """
    BlockData: Door
    """
    WEATHERED_COPPER_DOOR = (10208, Door)
    """
    BlockData: Door
    """
    OXIDIZED_COPPER_DOOR = (5348, Door)
    """
    BlockData: Door
    """
    WAXED_COPPER_DOOR = (9954, Door)
    """
    BlockData: Door
    """
    WAXED_EXPOSED_COPPER_DOOR = (20748, Door)
    """
    BlockData: Door
    """
    WAXED_WEATHERED_COPPER_DOOR = (25073, Door)
    """
    BlockData: Door
    """
    WAXED_OXIDIZED_COPPER_DOOR = (23888, Door)
    """
    BlockData: Door
    """
    IRON_TRAPDOOR = (17095, TrapDoor)
    """
    BlockData: TrapDoor
    """
    OAK_TRAPDOOR = (16927, TrapDoor)
    """
    BlockData: TrapDoor
    """
    SPRUCE_TRAPDOOR = (10289, TrapDoor)
    """
    BlockData: TrapDoor
    """
    BIRCH_TRAPDOOR = (32585, TrapDoor)
    """
    BlockData: TrapDoor
    """
    JUNGLE_TRAPDOOR = (8626, TrapDoor)
    """
    BlockData: TrapDoor
    """
    ACACIA_TRAPDOOR = (18343, TrapDoor)
    """
    BlockData: TrapDoor
    """
    CHERRY_TRAPDOOR = (6293, TrapDoor)
    """
    BlockData: TrapDoor
    """
    DARK_OAK_TRAPDOOR = (10355, TrapDoor)
    """
    BlockData: TrapDoor
    """
    PALE_OAK_TRAPDOOR = (20647, TrapDoor)
    """
    BlockData: TrapDoor
    """
    MANGROVE_TRAPDOOR = (17066, TrapDoor)
    """
    BlockData: TrapDoor
    """
    BAMBOO_TRAPDOOR = (9174, TrapDoor)
    """
    BlockData: TrapDoor
    """
    CRIMSON_TRAPDOOR = (25056, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WARPED_TRAPDOOR = (7708, TrapDoor)
    """
    BlockData: TrapDoor
    """
    COPPER_TRAPDOOR = (12110, TrapDoor)
    """
    BlockData: TrapDoor
    """
    EXPOSED_COPPER_TRAPDOOR = (19219, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WEATHERED_COPPER_TRAPDOOR = (28254, TrapDoor)
    """
    BlockData: TrapDoor
    """
    OXIDIZED_COPPER_TRAPDOOR = (26518, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WAXED_COPPER_TRAPDOOR = (12626, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WAXED_EXPOSED_COPPER_TRAPDOOR = (11010, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WAXED_WEATHERED_COPPER_TRAPDOOR = (30709, TrapDoor)
    """
    BlockData: TrapDoor
    """
    WAXED_OXIDIZED_COPPER_TRAPDOOR = (21450, TrapDoor)
    """
    BlockData: TrapDoor
    """
    OAK_FENCE_GATE = (16689, Gate)
    """
    BlockData: Gate
    """
    SPRUCE_FENCE_GATE = (26423, Gate)
    """
    BlockData: Gate
    """
    BIRCH_FENCE_GATE = (6322, Gate)
    """
    BlockData: Gate
    """
    JUNGLE_FENCE_GATE = (21360, Gate)
    """
    BlockData: Gate
    """
    ACACIA_FENCE_GATE = (14145, Gate)
    """
    BlockData: Gate
    """
    CHERRY_FENCE_GATE = (28222, Gate)
    """
    BlockData: Gate
    """
    DARK_OAK_FENCE_GATE = (10679, Gate)
    """
    BlockData: Gate
    """
    PALE_OAK_FENCE_GATE = (21221, Gate)
    """
    BlockData: Gate
    """
    MANGROVE_FENCE_GATE = (28476, Gate)
    """
    BlockData: Gate
    """
    BAMBOO_FENCE_GATE = (14290, Gate)
    """
    BlockData: Gate
    """
    CRIMSON_FENCE_GATE = (15602, Gate)
    """
    BlockData: Gate
    """
    WARPED_FENCE_GATE = (11115, Gate)
    """
    BlockData: Gate
    """
    POWERED_RAIL = (11064, RedstoneRail)
    """
    BlockData: RedstoneRail
    """
    DETECTOR_RAIL = (13475, RedstoneRail)
    """
    BlockData: RedstoneRail
    """
    RAIL = (13285, Rail)
    """
    BlockData: Rail
    """
    ACTIVATOR_RAIL = (5834, RedstoneRail)
    """
    BlockData: RedstoneRail
    """
    SADDLE = (30206, 1)
    MINECART = (14352, 1)
    CHEST_MINECART = (4497, 1)
    FURNACE_MINECART = (14196, 1)
    TNT_MINECART = (4277, 1)
    HOPPER_MINECART = (19024, 1)
    CARROT_ON_A_STICK = (27809, 1, 25)
    WARPED_FUNGUS_ON_A_STICK = (11706, 1, 100)
    PHANTOM_MEMBRANE = (18398)
    ELYTRA = (23829, 1, 432)
    OAK_BOAT = (17570, 1)
    OAK_CHEST_BOAT = (7765, 1)
    SPRUCE_BOAT = (31427, 1)
    SPRUCE_CHEST_BOAT = (30841, 1)
    BIRCH_BOAT = (28104, 1)
    BIRCH_CHEST_BOAT = (18546, 1)
    JUNGLE_BOAT = (4495, 1)
    JUNGLE_CHEST_BOAT = (20133, 1)
    ACACIA_BOAT = (27326, 1)
    ACACIA_CHEST_BOAT = (28455, 1)
    CHERRY_BOAT = (13628, 1)
    CHERRY_CHEST_BOAT = (7165, 1)
    DARK_OAK_BOAT = (28618, 1)
    DARK_OAK_CHEST_BOAT = (8733, 1)
    PALE_OAK_BOAT = (18534, 1)
    PALE_OAK_CHEST_BOAT = (26297, 1)
    MANGROVE_BOAT = (20792, 1)
    MANGROVE_CHEST_BOAT = (18572, 1)
    BAMBOO_RAFT = (25901, 1)
    BAMBOO_CHEST_RAFT = (20056, 1)
    STRUCTURE_BLOCK = (26831, StructureBlock)
    """
    BlockData: StructureBlock
    """
    JIGSAW = (17398, Jigsaw)
    """
    BlockData: Jigsaw
    """
    TURTLE_HELMET = (30120, 1, 275)
    TURTLE_SCUTE = (6766)
    ARMADILLO_SCUTE = (11497)
    WOLF_ARMOR = (17138, 1, 64)
    FLINT_AND_STEEL = (28620, 1, 64)
    BOWL = (32661)
    APPLE = (7720)
    BOW = (8745, 1, 384)
    ARROW = (31091)
    COAL = (29067)
    CHARCOAL = (5390)
    DIAMOND = (20865)
    EMERALD = (5654)
    LAPIS_LAZULI = (11075)
    QUARTZ = (23608)
    AMETHYST_SHARD = (7613)
    RAW_IRON = (5329)
    IRON_INGOT = (24895)
    RAW_COPPER = (6162)
    COPPER_INGOT = (12611)
    RAW_GOLD = (19564)
    GOLD_INGOT = (28927)
    NETHERITE_INGOT = (32457)
    NETHERITE_SCRAP = (29331)
    WOODEN_SWORD = (7175, 1, 59)
    WOODEN_SHOVEL = (28432, 1, 59)
    WOODEN_PICKAXE = (12792, 1, 59)
    WOODEN_AXE = (6292, 1, 59)
    WOODEN_HOE = (16043, 1, 59)
    STONE_SWORD = (25084, 1, 131)
    STONE_SHOVEL = (9520, 1, 131)
    STONE_PICKAXE = (14611, 1, 131)
    STONE_AXE = (6338, 1, 131)
    STONE_HOE = (22855, 1, 131)
    GOLDEN_SWORD = (10505, 1, 32)
    GOLDEN_SHOVEL = (15597, 1, 32)
    GOLDEN_PICKAXE = (25898, 1, 32)
    GOLDEN_AXE = (4878, 1, 32)
    GOLDEN_HOE = (19337, 1, 32)
    IRON_SWORD = (10904, 1, 250)
    IRON_SHOVEL = (30045, 1, 250)
    IRON_PICKAXE = (8842, 1, 250)
    IRON_AXE = (15894, 1, 250)
    IRON_HOE = (11339, 1, 250)
    DIAMOND_SWORD = (27707, 1, 1561)
    DIAMOND_SHOVEL = (25415, 1, 1561)
    DIAMOND_PICKAXE = (24291, 1, 1561)
    DIAMOND_AXE = (27277, 1, 1561)
    DIAMOND_HOE = (24050, 1, 1561)
    NETHERITE_SWORD = (23871, 1, 2031)
    NETHERITE_SHOVEL = (29728, 1, 2031)
    NETHERITE_PICKAXE = (9930, 1, 2031)
    NETHERITE_AXE = (29533, 1, 2031)
    NETHERITE_HOE = (27385, 1, 2031)
    STICK = (9773)
    MUSHROOM_STEW = (16336, 1)
    STRING = (12806)
    FEATHER = (30548)
    GUNPOWDER = (29974)
    WHEAT_SEEDS = (28742)
    WHEAT = (27709, Ageable)
    """
    BlockData: Ageable
    """
    BREAD = (32049)
    LEATHER_HELMET = (11624, 1, 55)
    LEATHER_CHESTPLATE = (29275, 1, 80)
    LEATHER_LEGGINGS = (28210, 1, 75)
    LEATHER_BOOTS = (15282, 1, 65)
    CHAINMAIL_HELMET = (26114, 1, 165)
    CHAINMAIL_CHESTPLATE = (23602, 1, 240)
    CHAINMAIL_LEGGINGS = (19087, 1, 225)
    CHAINMAIL_BOOTS = (17953, 1, 195)
    IRON_HELMET = (12025, 1, 165)
    IRON_CHESTPLATE = (28112, 1, 240)
    IRON_LEGGINGS = (18951, 1, 225)
    IRON_BOOTS = (8531, 1, 195)
    DIAMOND_HELMET = (10755, 1, 363)
    DIAMOND_CHESTPLATE = (32099, 1, 528)
    DIAMOND_LEGGINGS = (26500, 1, 495)
    DIAMOND_BOOTS = (16522, 1, 429)
    GOLDEN_HELMET = (7945, 1, 77)
    GOLDEN_CHESTPLATE = (4507, 1, 112)
    GOLDEN_LEGGINGS = (21002, 1, 105)
    GOLDEN_BOOTS = (7859, 1, 91)
    NETHERITE_HELMET = (15907, 1, 407)
    NETHERITE_CHESTPLATE = (6106, 1, 592)
    NETHERITE_LEGGINGS = (25605, 1, 555)
    NETHERITE_BOOTS = (8923, 1, 481)
    FLINT = (23596)
    PORKCHOP = (30896)
    COOKED_PORKCHOP = (27231)
    PAINTING = (23945)
    GOLDEN_APPLE = (27732)
    ENCHANTED_GOLDEN_APPLE = (8280)
    OAK_SIGN = (8192, 16, Sign)
    """
    BlockData: Sign
    """
    SPRUCE_SIGN = (21502, 16, Sign)
    """
    BlockData: Sign
    """
    BIRCH_SIGN = (11351, 16, Sign)
    """
    BlockData: Sign
    """
    JUNGLE_SIGN = (24717, 16, Sign)
    """
    BlockData: Sign
    """
    ACACIA_SIGN = (29808, 16, Sign)
    """
    BlockData: Sign
    """
    CHERRY_SIGN = (16520, 16, Sign)
    """
    BlockData: Sign
    """
    DARK_OAK_SIGN = (15127, 16, Sign)
    """
    BlockData: Sign
    """
    PALE_OAK_SIGN = (12116, 16, Sign)
    """
    BlockData: Sign
    """
    MANGROVE_SIGN = (21975, 16, Sign)
    """
    BlockData: Sign
    """
    BAMBOO_SIGN = (26139, 16, Sign)
    """
    BlockData: Sign
    """
    CRIMSON_SIGN = (12162, 16, Sign)
    """
    BlockData: Sign
    """
    WARPED_SIGN = (10407, 16, Sign)
    """
    BlockData: Sign
    """
    OAK_HANGING_SIGN = (20116, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    SPRUCE_HANGING_SIGN = (24371, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    BIRCH_HANGING_SIGN = (17938, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    JUNGLE_HANGING_SIGN = (27671, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    ACACIA_HANGING_SIGN = (30257, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    CHERRY_HANGING_SIGN = (5088, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    DARK_OAK_HANGING_SIGN = (23360, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    PALE_OAK_HANGING_SIGN = (7097, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    MANGROVE_HANGING_SIGN = (25106, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    BAMBOO_HANGING_SIGN = (4726, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    CRIMSON_HANGING_SIGN = (20696, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    WARPED_HANGING_SIGN = (8195, 16, HangingSign)
    """
    BlockData: HangingSign
    """
    BUCKET = (15215, 16)
    WATER_BUCKET = (8802, 1)
    LAVA_BUCKET = (9228, 1)
    POWDER_SNOW_BUCKET = (31101, 1)
    SNOWBALL = (19487, 16)
    LEATHER = (16414)
    MILK_BUCKET = (9680, 1)
    PUFFERFISH_BUCKET = (8861, 1)
    SALMON_BUCKET = (9606, 1)
    COD_BUCKET = (28601, 1)
    TROPICAL_FISH_BUCKET = (29995, 1)
    AXOLOTL_BUCKET = (20669, 1)
    TADPOLE_BUCKET = (9731, 1)
    BRICK = (6820)
    CLAY_BALL = (24603)
    DRIED_KELP_BLOCK = (12966)
    PAPER = (9923)
    BOOK = (23097)
    SLIME_BALL = (5242)
    EGG = (21603, 16)
    COMPASS = (24139)
    RECOVERY_COMPASS = (12710)
    BUNDLE = (16835, 1)
    WHITE_BUNDLE = (12072, 1)
    ORANGE_BUNDLE = (18288, 1)
    MAGENTA_BUNDLE = (15328, 1)
    LIGHT_BLUE_BUNDLE = (18639, 1)
    YELLOW_BUNDLE = (27749, 1)
    LIME_BUNDLE = (30093, 1)
    PINK_BUNDLE = (21400, 1)
    GRAY_BUNDLE = (21262, 1)
    LIGHT_GRAY_BUNDLE = (26338, 1)
    CYAN_BUNDLE = (8942, 1)
    PURPLE_BUNDLE = (10319, 1)
    BLUE_BUNDLE = (31501, 1)
    BROWN_BUNDLE = (15464, 1)
    GREEN_BUNDLE = (4597, 1)
    RED_BUNDLE = (19986, 1)
    BLACK_BUNDLE = (22519, 1)
    FISHING_ROD = (4167, 1, 64)
    CLOCK = (14980)
    SPYGLASS = (27490, 1)
    GLOWSTONE_DUST = (6665)
    COD = (24691)
    SALMON = (18516)
    TROPICAL_FISH = (24879)
    PUFFERFISH = (8115)
    COOKED_COD = (9681)
    COOKED_SALMON = (5615)
    INK_SAC = (7184)
    GLOW_INK_SAC = (9686)
    COCOA_BEANS = (30186)
    WHITE_DYE = (10758)
    ORANGE_DYE = (13866)
    MAGENTA_DYE = (11788)
    LIGHT_BLUE_DYE = (28738)
    YELLOW_DYE = (5952)
    LIME_DYE = (6147)
    PINK_DYE = (31151)
    GRAY_DYE = (9184)
    LIGHT_GRAY_DYE = (27643)
    CYAN_DYE = (8043)
    PURPLE_DYE = (6347)
    BLUE_DYE = (11588)
    BROWN_DYE = (7648)
    GREEN_DYE = (23215)
    RED_DYE = (5728)
    BLACK_DYE = (6202)
    BONE_MEAL = (32458)
    BONE = (5686)
    SUGAR = (30638)
    CAKE = (27048, 1, Cake)
    """
    BlockData: Cake
    """
    WHITE_BED = (8185, 1, Bed)
    """
    BlockData: Bed
    """
    ORANGE_BED = (11194, 1, Bed)
    """
    BlockData: Bed
    """
    MAGENTA_BED = (20061, 1, Bed)
    """
    BlockData: Bed
    """
    LIGHT_BLUE_BED = (20957, 1, Bed)
    """
    BlockData: Bed
    """
    YELLOW_BED = (30410, 1, Bed)
    """
    BlockData: Bed
    """
    LIME_BED = (27860, 1, Bed)
    """
    BlockData: Bed
    """
    PINK_BED = (13795, 1, Bed)
    """
    BlockData: Bed
    """
    GRAY_BED = (15745, 1, Bed)
    """
    BlockData: Bed
    """
    LIGHT_GRAY_BED = (5090, 1, Bed)
    """
    BlockData: Bed
    """
    CYAN_BED = (16746, 1, Bed)
    """
    BlockData: Bed
    """
    PURPLE_BED = (29755, 1, Bed)
    """
    BlockData: Bed
    """
    BLUE_BED = (12714, 1, Bed)
    """
    BlockData: Bed
    """
    BROWN_BED = (26672, 1, Bed)
    """
    BlockData: Bed
    """
    GREEN_BED = (13797, 1, Bed)
    """
    BlockData: Bed
    """
    RED_BED = (30910, 1, Bed)
    """
    BlockData: Bed
    """
    BLACK_BED = (20490, 1, Bed)
    """
    BlockData: Bed
    """
    COOKIE = (27431)
    CRAFTER = (25243, Crafter)
    """
    BlockData: Crafter
    """
    FILLED_MAP = (23504)
    SHEARS = (27971, 1, 238)
    MELON_SLICE = (5347)
    DRIED_KELP = (21042)
    PUMPKIN_SEEDS = (28985)
    MELON_SEEDS = (18340)
    BEEF = (4803)
    COOKED_BEEF = (21595)
    CHICKEN = (17281)
    COOKED_CHICKEN = (16984)
    ROTTEN_FLESH = (21591)
    ENDER_PEARL = (5259, 16)
    BLAZE_ROD = (8289)
    GHAST_TEAR = (18222)
    GOLD_NUGGET = (28814)
    NETHER_WART = (29227, Ageable)
    """
    BlockData: Ageable
    """
    GLASS_BOTTLE = (6116)
    POTION = (24020, 1)
    SPIDER_EYE = (9318)
    FERMENTED_SPIDER_EYE = (19386)
    BLAZE_POWDER = (18941)
    MAGMA_CREAM = (25097)
    BREWING_STAND = (14539, BrewingStand)
    """
    BlockData: BrewingStand
    """
    CAULDRON = (26531)
    ENDER_EYE = (24860)
    GLISTERING_MELON_SLICE = (20158)
    ARMADILLO_SPAWN_EGG = (22098)
    ALLAY_SPAWN_EGG = (7909)
    AXOLOTL_SPAWN_EGG = (30381)
    BAT_SPAWN_EGG = (14607)
    BEE_SPAWN_EGG = (22924)
    BLAZE_SPAWN_EGG = (4759)
    BOGGED_SPAWN_EGG = (12042)
    BREEZE_SPAWN_EGG = (7580)
    CAT_SPAWN_EGG = (29583)
    CAMEL_SPAWN_EGG = (14760)
    CAVE_SPIDER_SPAWN_EGG = (23341)
    CHICKEN_SPAWN_EGG = (5462)
    COD_SPAWN_EGG = (27248)
    COW_SPAWN_EGG = (14761)
    CREEPER_SPAWN_EGG = (9653)
    DOLPHIN_SPAWN_EGG = (20787)
    DONKEY_SPAWN_EGG = (14513)
    DROWNED_SPAWN_EGG = (19368)
    ELDER_GUARDIAN_SPAWN_EGG = (11418)
    ENDER_DRAGON_SPAWN_EGG = (28092)
    ENDERMAN_SPAWN_EGG = (29488)
    ENDERMITE_SPAWN_EGG = (16617)
    EVOKER_SPAWN_EGG = (21271)
    FOX_SPAWN_EGG = (22376)
    FROG_SPAWN_EGG = (26682)
    GHAST_SPAWN_EGG = (9970)
    GLOW_SQUID_SPAWN_EGG = (31578)
    GOAT_SPAWN_EGG = (30639)
    GUARDIAN_SPAWN_EGG = (20113)
    HOGLIN_SPAWN_EGG = (14088)
    HORSE_SPAWN_EGG = (25981)
    HUSK_SPAWN_EGG = (20178)
    IRON_GOLEM_SPAWN_EGG = (12781)
    LLAMA_SPAWN_EGG = (23640)
    MAGMA_CUBE_SPAWN_EGG = (26638)
    MOOSHROOM_SPAWN_EGG = (22125)
    MULE_SPAWN_EGG = (11229)
    OCELOT_SPAWN_EGG = (30080)
    PANDA_SPAWN_EGG = (23759)
    PARROT_SPAWN_EGG = (23614)
    PHANTOM_SPAWN_EGG = (24648)
    PIG_SPAWN_EGG = (22584)
    PIGLIN_SPAWN_EGG = (16193)
    PIGLIN_BRUTE_SPAWN_EGG = (30230)
    PILLAGER_SPAWN_EGG = (28659)
    POLAR_BEAR_SPAWN_EGG = (17015)
    PUFFERFISH_SPAWN_EGG = (24570)
    RABBIT_SPAWN_EGG = (26496)
    RAVAGER_SPAWN_EGG = (8726)
    SALMON_SPAWN_EGG = (18739)
    SHEEP_SPAWN_EGG = (24488)
    SHULKER_SPAWN_EGG = (31848)
    SILVERFISH_SPAWN_EGG = (14537)
    SKELETON_SPAWN_EGG = (15261)
    SKELETON_HORSE_SPAWN_EGG = (21356)
    SLIME_SPAWN_EGG = (17196)
    SNIFFER_SPAWN_EGG = (27473)
    SNOW_GOLEM_SPAWN_EGG = (24732)
    SPIDER_SPAWN_EGG = (14984)
    SQUID_SPAWN_EGG = (10682)
    STRAY_SPAWN_EGG = (30153)
    STRIDER_SPAWN_EGG = (6203)
    TADPOLE_SPAWN_EGG = (32467)
    TRADER_LLAMA_SPAWN_EGG = (8439)
    TROPICAL_FISH_SPAWN_EGG = (19713)
    TURTLE_SPAWN_EGG = (17324)
    VEX_SPAWN_EGG = (27751)
    VILLAGER_SPAWN_EGG = (30348)
    VINDICATOR_SPAWN_EGG = (25324)
    WANDERING_TRADER_SPAWN_EGG = (17904)
    WARDEN_SPAWN_EGG = (27553)
    WITCH_SPAWN_EGG = (11837)
    WITHER_SPAWN_EGG = (8024)
    WITHER_SKELETON_SPAWN_EGG = (10073)
    WOLF_SPAWN_EGG = (21692)
    ZOGLIN_SPAWN_EGG = (7442)
    CREAKING_SPAWN_EGG = (9598)
    ZOMBIE_SPAWN_EGG = (5814)
    ZOMBIE_HORSE_SPAWN_EGG = (4275)
    ZOMBIE_VILLAGER_SPAWN_EGG = (10311)
    ZOMBIFIED_PIGLIN_SPAWN_EGG = (6626)
    EXPERIENCE_BOTTLE = (12858)
    FIRE_CHARGE = (4842)
    WIND_CHARGE = (23928)
    WRITABLE_BOOK = (13393, 1)
    WRITTEN_BOOK = (24164, 16)
    BREEZE_ROD = (14281)
    MACE = (4771, 1, 500)
    ITEM_FRAME = (27318)
    GLOW_ITEM_FRAME = (26473)
    FLOWER_POT = (30567)
    CARROT = (22824)
    POTATO = (21088)
    BAKED_POTATO = (14624)
    POISONOUS_POTATO = (32640)
    MAP = (21655)
    GOLDEN_CARROT = (5300)
    SKELETON_SKULL = (13270, Skull)
    """
    BlockData: Skull
    """
    WITHER_SKELETON_SKULL = (31487, Skull)
    """
    BlockData: Skull
    """
    PLAYER_HEAD = (21174, Skull)
    """
    BlockData: Skull
    """
    ZOMBIE_HEAD = (9304, Skull)
    """
    BlockData: Skull
    """
    CREEPER_HEAD = (29146, Skull)
    """
    BlockData: Skull
    """
    DRAGON_HEAD = (20084, Skull)
    """
    BlockData: Skull
    """
    PIGLIN_HEAD = (5512, Skull)
    """
    BlockData: Skull
    """
    NETHER_STAR = (12469)
    PUMPKIN_PIE = (28725)
    FIREWORK_ROCKET = (23841)
    FIREWORK_STAR = (12190)
    ENCHANTED_BOOK = (11741, 1)
    NETHER_BRICK = (19996)
    PRISMARINE_SHARD = (10993)
    PRISMARINE_CRYSTALS = (31546)
    RABBIT = (23068)
    COOKED_RABBIT = (4454)
    RABBIT_STEW = (25318, 1)
    RABBIT_FOOT = (13864)
    RABBIT_HIDE = (12467)
    ARMOR_STAND = (12852, 16)
    IRON_HORSE_ARMOR = (30108, 1)
    GOLDEN_HORSE_ARMOR = (7996, 1)
    DIAMOND_HORSE_ARMOR = (10321, 1)
    LEATHER_HORSE_ARMOR = (30667, 1)
    LEAD = (29539)
    NAME_TAG = (30731)
    COMMAND_BLOCK_MINECART = (7992, 1)
    MUTTON = (4792)
    COOKED_MUTTON = (31447)
    WHITE_BANNER = (17562, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    ORANGE_BANNER = (4839, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    MAGENTA_BANNER = (15591, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    LIGHT_BLUE_BANNER = (18060, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    YELLOW_BANNER = (30382, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    LIME_BANNER = (18887, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    PINK_BANNER = (19439, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    GRAY_BANNER = (12053, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    LIGHT_GRAY_BANNER = (11417, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    CYAN_BANNER = (9839, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    PURPLE_BANNER = (29027, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    BLUE_BANNER = (18481, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    BROWN_BANNER = (11481, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    GREEN_BANNER = (10698, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    RED_BANNER = (26961, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    BLACK_BANNER = (9365, 16, Rotatable)
    """
    BlockData: Rotatable
    """
    END_CRYSTAL = (19090)
    CHORUS_FRUIT = (7652)
    POPPED_CHORUS_FRUIT = (27844)
    TORCHFLOWER_SEEDS = (18153)
    PITCHER_POD = (7977)
    BEETROOT = (23305)
    BEETROOT_SEEDS = (21282)
    BEETROOT_SOUP = (16036, 1)
    DRAGON_BREATH = (20154)
    SPLASH_POTION = (30248, 1)
    SPECTRAL_ARROW = (4568)
    TIPPED_ARROW = (25164)
    LINGERING_POTION = (25857, 1)
    SHIELD = (29943, 1, 336)
    TOTEM_OF_UNDYING = (10139, 1)
    SHULKER_SHELL = (27848)
    IRON_NUGGET = (13715)
    KNOWLEDGE_BOOK = (12646, 1)
    DEBUG_STICK = (24562, 1)
    MUSIC_DISC_13 = (16359, 1)
    MUSIC_DISC_CAT = (16246, 1)
    MUSIC_DISC_BLOCKS = (26667, 1)
    MUSIC_DISC_CHIRP = (19436, 1)
    MUSIC_DISC_CREATOR = (20345, 1)
    MUSIC_DISC_CREATOR_MUSIC_BOX = (7202, 1)
    MUSIC_DISC_FAR = (31742, 1)
    MUSIC_DISC_MALL = (11517, 1)
    MUSIC_DISC_MELLOHI = (26117, 1)
    MUSIC_DISC_STAL = (14989, 1)
    MUSIC_DISC_STRAD = (16785, 1)
    MUSIC_DISC_WARD = (24026, 1)
    MUSIC_DISC_11 = (27426, 1)
    MUSIC_DISC_WAIT = (26499, 1)
    MUSIC_DISC_OTHERSIDE = (12974, 1)
    MUSIC_DISC_RELIC = (8200, 1)
    MUSIC_DISC_5 = (9212, 1)
    MUSIC_DISC_PIGSTEP = (21323, 1)
    MUSIC_DISC_PRECIPICE = (28677, 1)
    DISC_FRAGMENT_5 = (29729)
    TRIDENT = (7534, 1, 250)
    NAUTILUS_SHELL = (19989)
    HEART_OF_THE_SEA = (11807)
    CROSSBOW = (4340, 1, 465)
    SUSPICIOUS_STEW = (8173, 1)
    LOOM = (14276, Directional)
    """
    BlockData: Directional
    """
    FLOWER_BANNER_PATTERN = (5762, 1)
    CREEPER_BANNER_PATTERN = (15774, 1)
    SKULL_BANNER_PATTERN = (7680, 1)
    MOJANG_BANNER_PATTERN = (11903, 1)
    GLOBE_BANNER_PATTERN = (27753, 1)
    PIGLIN_BANNER_PATTERN = (22028, 1)
    FLOW_BANNER_PATTERN = (32683, 1)
    GUSTER_BANNER_PATTERN = (27267, 1)
    FIELD_MASONED_BANNER_PATTERN = (19157, 1)
    BORDURE_INDENTED_BANNER_PATTERN = (25850, 1)
    GOAT_HORN = (28237, 1)
    COMPOSTER = (31247, Levelled)
    """
    BlockData: Levelled
    """
    BARREL = (22396, Barrel)
    """
    BlockData: Barrel
    """
    SMOKER = (24781, Furnace)
    """
    BlockData: Furnace
    """
    BLAST_FURNACE = (31157, Furnace)
    """
    BlockData: Furnace
    """
    CARTOGRAPHY_TABLE = (28529)
    FLETCHING_TABLE = (30838)
    GRINDSTONE = (26260, Grindstone)
    """
    BlockData: Grindstone
    """
    SMITHING_TABLE = (9082)
    STONECUTTER = (25170, Directional)
    """
    BlockData: Directional
    """
    BELL = (20000, Bell)
    """
    BlockData: Bell
    """
    LANTERN = (5992, Lantern)
    """
    BlockData: Lantern
    """
    SOUL_LANTERN = (27778, Lantern)
    """
    BlockData: Lantern
    """
    SWEET_BERRIES = (19747)
    GLOW_BERRIES = (11584)
    CAMPFIRE = (8488, Campfire)
    """
    BlockData: Campfire
    """
    SOUL_CAMPFIRE = (4238, Campfire)
    """
    BlockData: Campfire
    """
    SHROOMLIGHT = (20424)
    HONEYCOMB = (9482)
    BEE_NEST = (8825, Beehive)
    """
    BlockData: Beehive
    """
    BEEHIVE = (11830, Beehive)
    """
    BlockData: Beehive
    """
    HONEY_BOTTLE = (22927, 16)
    HONEYCOMB_BLOCK = (28780)
    LODESTONE = (23127)
    CRYING_OBSIDIAN = (31545)
    BLACKSTONE = (7354)
    BLACKSTONE_SLAB = (11948, Slab)
    """
    BlockData: Slab
    """
    BLACKSTONE_STAIRS = (14646, Stairs)
    """
    BlockData: Stairs
    """
    GILDED_BLACKSTONE = (8498)
    POLISHED_BLACKSTONE = (18144)
    POLISHED_BLACKSTONE_SLAB = (23430, Slab)
    """
    BlockData: Slab
    """
    POLISHED_BLACKSTONE_STAIRS = (8653, Stairs)
    """
    BlockData: Stairs
    """
    CHISELED_POLISHED_BLACKSTONE = (21942)
    POLISHED_BLACKSTONE_BRICKS = (19844)
    POLISHED_BLACKSTONE_BRICK_SLAB = (12219, Slab)
    """
    BlockData: Slab
    """
    POLISHED_BLACKSTONE_BRICK_STAIRS = (17983, Stairs)
    """
    BlockData: Stairs
    """
    CRACKED_POLISHED_BLACKSTONE_BRICKS = (16846)
    RESPAWN_ANCHOR = (4099, RespawnAnchor)
    """
    BlockData: RespawnAnchor
    """
    CANDLE = (16122, Candle)
    """
    BlockData: Candle
    """
    WHITE_CANDLE = (26410, Candle)
    """
    BlockData: Candle
    """
    ORANGE_CANDLE = (22668, Candle)
    """
    BlockData: Candle
    """
    MAGENTA_CANDLE = (25467, Candle)
    """
    BlockData: Candle
    """
    LIGHT_BLUE_CANDLE = (28681, Candle)
    """
    BlockData: Candle
    """
    YELLOW_CANDLE = (14351, Candle)
    """
    BlockData: Candle
    """
    LIME_CANDLE = (21778, Candle)
    """
    BlockData: Candle
    """
    PINK_CANDLE = (28259, Candle)
    """
    BlockData: Candle
    """
    GRAY_CANDLE = (10721, Candle)
    """
    BlockData: Candle
    """
    LIGHT_GRAY_CANDLE = (10031, Candle)
    """
    BlockData: Candle
    """
    CYAN_CANDLE = (24765, Candle)
    """
    BlockData: Candle
    """
    PURPLE_CANDLE = (19606, Candle)
    """
    BlockData: Candle
    """
    BLUE_CANDLE = (29047, Candle)
    """
    BlockData: Candle
    """
    BROWN_CANDLE = (26145, Candle)
    """
    BlockData: Candle
    """
    GREEN_CANDLE = (29756, Candle)
    """
    BlockData: Candle
    """
    RED_CANDLE = (4214, Candle)
    """
    BlockData: Candle
    """
    BLACK_CANDLE = (12617, Candle)
    """
    BlockData: Candle
    """
    SMALL_AMETHYST_BUD = (14958, AmethystCluster)
    """
    BlockData: AmethystCluster
    """
    MEDIUM_AMETHYST_BUD = (8429, AmethystCluster)
    """
    BlockData: AmethystCluster
    """
    LARGE_AMETHYST_BUD = (7279, AmethystCluster)
    """
    BlockData: AmethystCluster
    """
    AMETHYST_CLUSTER = (13142, AmethystCluster)
    """
    BlockData: AmethystCluster
    """
    POINTED_DRIPSTONE = (18755, PointedDripstone)
    """
    BlockData: PointedDripstone
    """
    OCHRE_FROGLIGHT = (25330, Orientable)
    """
    BlockData: Orientable
    """
    VERDANT_FROGLIGHT = (22793, Orientable)
    """
    BlockData: Orientable
    """
    PEARLESCENT_FROGLIGHT = (21441, Orientable)
    """
    BlockData: Orientable
    """
    FROGSPAWN = (8350)
    ECHO_SHARD = (12529)
    BRUSH = (30569, 1, 64)
    NETHERITE_UPGRADE_SMITHING_TEMPLATE = (7615)
    SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE = (16124)
    DUNE_ARMOR_TRIM_SMITHING_TEMPLATE = (30925)
    COAST_ARMOR_TRIM_SMITHING_TEMPLATE = (25501)
    WILD_ARMOR_TRIM_SMITHING_TEMPLATE = (5870)
    WARD_ARMOR_TRIM_SMITHING_TEMPLATE = (24534)
    EYE_ARMOR_TRIM_SMITHING_TEMPLATE = (14663)
    VEX_ARMOR_TRIM_SMITHING_TEMPLATE = (25818)
    TIDE_ARMOR_TRIM_SMITHING_TEMPLATE = (20420)
    SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE = (14386)
    RIB_ARMOR_TRIM_SMITHING_TEMPLATE = (6010)
    SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE = (29143)
    WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE = (4957)
    SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE = (20537)
    SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE = (7070)
    RAISER_ARMOR_TRIM_SMITHING_TEMPLATE = (29116)
    HOST_ARMOR_TRIM_SMITHING_TEMPLATE = (12165)
    FLOW_ARMOR_TRIM_SMITHING_TEMPLATE = (29175)
    BOLT_ARMOR_TRIM_SMITHING_TEMPLATE = (9698)
    ANGLER_POTTERY_SHERD = (9952)
    ARCHER_POTTERY_SHERD = (21629)
    ARMS_UP_POTTERY_SHERD = (5484)
    BLADE_POTTERY_SHERD = (25079)
    BREWER_POTTERY_SHERD = (23429)
    BURN_POTTERY_SHERD = (21259)
    DANGER_POTTERY_SHERD = (30506)
    EXPLORER_POTTERY_SHERD = (5124)
    FLOW_POTTERY_SHERD = (4896)
    FRIEND_POTTERY_SHERD = (18221)
    GUSTER_POTTERY_SHERD = (28193)
    HEART_POTTERY_SHERD = (17607)
    HEARTBREAK_POTTERY_SHERD = (21108)
    HOWL_POTTERY_SHERD = (24900)
    MINER_POTTERY_SHERD = (30602)
    MOURNER_POTTERY_SHERD = (23993)
    PLENTY_POTTERY_SHERD = (28236)
    PRIZE_POTTERY_SHERD = (4341)
    SCRAPE_POTTERY_SHERD = (30034)
    SHEAF_POTTERY_SHERD = (23652)
    SHELTER_POTTERY_SHERD = (28390)
    SKULL_POTTERY_SHERD = (16980)
    SNORT_POTTERY_SHERD = (15921)
    COPPER_GRATE = (16221, Waterlogged)
    """
    BlockData: Waterlogged
    """
    EXPOSED_COPPER_GRATE = (7783, Waterlogged)
    """
    BlockData: Waterlogged
    """
    WEATHERED_COPPER_GRATE = (24954, Waterlogged)
    """
    BlockData: Waterlogged
    """
    OXIDIZED_COPPER_GRATE = (14122, Waterlogged)
    """
    BlockData: Waterlogged
    """
    WAXED_COPPER_GRATE = (11230, Waterlogged)
    """
    BlockData: Waterlogged
    """
    WAXED_EXPOSED_COPPER_GRATE = (20520, Waterlogged)
    """
    BlockData: Waterlogged
    """
    WAXED_WEATHERED_COPPER_GRATE = (16533, Waterlogged)
    """
    BlockData: Waterlogged
    """
    WAXED_OXIDIZED_COPPER_GRATE = (32010, Waterlogged)
    """
    BlockData: Waterlogged
    """
    COPPER_BULB = (21370, CopperBulb)
    """
    BlockData: CopperBulb
    """
    EXPOSED_COPPER_BULB = (11944, CopperBulb)
    """
    BlockData: CopperBulb
    """
    WEATHERED_COPPER_BULB = (10800, CopperBulb)
    """
    BlockData: CopperBulb
    """
    OXIDIZED_COPPER_BULB = (22421, CopperBulb)
    """
    BlockData: CopperBulb
    """
    WAXED_COPPER_BULB = (23756, CopperBulb)
    """
    BlockData: CopperBulb
    """
    WAXED_EXPOSED_COPPER_BULB = (5530, CopperBulb)
    """
    BlockData: CopperBulb
    """
    WAXED_WEATHERED_COPPER_BULB = (13239, CopperBulb)
    """
    BlockData: CopperBulb
    """
    WAXED_OXIDIZED_COPPER_BULB = (26892, CopperBulb)
    """
    BlockData: CopperBulb
    """
    TRIAL_SPAWNER = (19902, TrialSpawner)
    """
    BlockData: TrialSpawner
    """
    TRIAL_KEY = (12725)
    OMINOUS_TRIAL_KEY = (4986)
    VAULT = (6288, Vault)
    """
    BlockData: Vault
    """
    OMINOUS_BOTTLE = (26321)
    WATER = (24998, Levelled)
    """
    BlockData: Levelled
    """
    LAVA = (8415, Levelled)
    """
    BlockData: Levelled
    """
    TALL_SEAGRASS = (27189, Bisected)
    """
    BlockData: Bisected
    """
    PISTON_HEAD = (30226, PistonHead)
    """
    BlockData: PistonHead
    """
    MOVING_PISTON = (13831, TechnicalPiston)
    """
    BlockData: TechnicalPiston
    """
    WALL_TORCH = (25890, Directional)
    """
    BlockData: Directional
    """
    FIRE = (16396, Fire)
    """
    BlockData: Fire
    """
    SOUL_FIRE = (30163)
    REDSTONE_WIRE = (25984, RedstoneWire)
    """
    BlockData: RedstoneWire
    """
    OAK_WALL_SIGN = (12984, 16, WallSign)
    """
    BlockData: WallSign
    """
    SPRUCE_WALL_SIGN = (7352, 16, WallSign)
    """
    BlockData: WallSign
    """
    BIRCH_WALL_SIGN = (9887, 16, WallSign)
    """
    BlockData: WallSign
    """
    ACACIA_WALL_SIGN = (20316, 16, WallSign)
    """
    BlockData: WallSign
    """
    CHERRY_WALL_SIGN = (20188, 16, WallSign)
    """
    BlockData: WallSign
    """
    JUNGLE_WALL_SIGN = (29629, 16, WallSign)
    """
    BlockData: WallSign
    """
    DARK_OAK_WALL_SIGN = (9508, 16, WallSign)
    """
    BlockData: WallSign
    """
    PALE_OAK_WALL_SIGN = (23103, 16, WallSign)
    """
    BlockData: WallSign
    """
    MANGROVE_WALL_SIGN = (27203, 16, WallSign)
    """
    BlockData: WallSign
    """
    BAMBOO_WALL_SIGN = (18857, 16, WallSign)
    """
    BlockData: WallSign
    """
    OAK_WALL_HANGING_SIGN = (15637, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    SPRUCE_WALL_HANGING_SIGN = (18833, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    BIRCH_WALL_HANGING_SIGN = (15937, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    ACACIA_WALL_HANGING_SIGN = (22477, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    CHERRY_WALL_HANGING_SIGN = (10953, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    JUNGLE_WALL_HANGING_SIGN = (16691, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    DARK_OAK_WALL_HANGING_SIGN = (14296, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    PALE_OAK_WALL_HANGING_SIGN = (23484, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    MANGROVE_WALL_HANGING_SIGN = (16974, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    CRIMSON_WALL_HANGING_SIGN = (28982, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    WARPED_WALL_HANGING_SIGN = (20605, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    BAMBOO_WALL_HANGING_SIGN = (6669, WallHangingSign)
    """
    BlockData: WallHangingSign
    """
    REDSTONE_WALL_TORCH = (7595, RedstoneWallTorch)
    """
    BlockData: RedstoneWallTorch
    """
    SOUL_WALL_TORCH = (27500, Directional)
    """
    BlockData: Directional
    """
    NETHER_PORTAL = (19469, Orientable)
    """
    BlockData: Orientable
    """
    ATTACHED_PUMPKIN_STEM = (12724, Directional)
    """
    BlockData: Directional
    """
    ATTACHED_MELON_STEM = (30882, Directional)
    """
    BlockData: Directional
    """
    PUMPKIN_STEM = (19021, Ageable)
    """
    BlockData: Ageable
    """
    MELON_STEM = (8247, Ageable)
    """
    BlockData: Ageable
    """
    WATER_CAULDRON = (32008, Levelled)
    """
    BlockData: Levelled
    """
    LAVA_CAULDRON = (4514)
    POWDER_SNOW_CAULDRON = (31571, Levelled)
    """
    BlockData: Levelled
    """
    END_PORTAL = (16782)
    COCOA = (29709, Cocoa)
    """
    BlockData: Cocoa
    """
    TRIPWIRE = (8810, Tripwire)
    """
    BlockData: Tripwire
    """
    POTTED_TORCHFLOWER = (21278)
    POTTED_OAK_SAPLING = (11905)
    POTTED_SPRUCE_SAPLING = (29498)
    POTTED_BIRCH_SAPLING = (32484)
    POTTED_JUNGLE_SAPLING = (7525)
    POTTED_ACACIA_SAPLING = (14096)
    POTTED_CHERRY_SAPLING = (30785)
    POTTED_DARK_OAK_SAPLING = (6486)
    POTTED_PALE_OAK_SAPLING = (15538)
    POTTED_MANGROVE_PROPAGULE = (22003)
    POTTED_FERN = (23315)
    POTTED_DANDELION = (9727)
    POTTED_POPPY = (7457)
    POTTED_BLUE_ORCHID = (6599)
    POTTED_ALLIUM = (13184)
    POTTED_AZURE_BLUET = (8754)
    POTTED_RED_TULIP = (28594)
    POTTED_ORANGE_TULIP = (28807)
    POTTED_WHITE_TULIP = (24330)
    POTTED_PINK_TULIP = (10089)
    POTTED_OXEYE_DAISY = (19707)
    POTTED_CORNFLOWER = (28917)
    POTTED_LILY_OF_THE_VALLEY = (9364)
    POTTED_WITHER_ROSE = (26876)
    POTTED_RED_MUSHROOM = (22881)
    POTTED_BROWN_MUSHROOM = (14481)
    POTTED_DEAD_BUSH = (13020)
    POTTED_CACTUS = (8777)
    CARROTS = (17258, Ageable)
    """
    BlockData: Ageable
    """
    POTATOES = (10879, Ageable)
    """
    BlockData: Ageable
    """
    SKELETON_WALL_SKULL = (31650, WallSkull)
    """
    BlockData: WallSkull
    """
    WITHER_SKELETON_WALL_SKULL = (9326, WallSkull)
    """
    BlockData: WallSkull
    """
    ZOMBIE_WALL_HEAD = (16296, WallSkull)
    """
    BlockData: WallSkull
    """
    PLAYER_WALL_HEAD = (13164, WallSkull)
    """
    BlockData: WallSkull
    """
    CREEPER_WALL_HEAD = (30123, WallSkull)
    """
    BlockData: WallSkull
    """
    DRAGON_WALL_HEAD = (19818, WallSkull)
    """
    BlockData: WallSkull
    """
    PIGLIN_WALL_HEAD = (4446, WallSkull)
    """
    BlockData: WallSkull
    """
    WHITE_WALL_BANNER = (15967, Directional)
    """
    BlockData: Directional
    """
    ORANGE_WALL_BANNER = (9936, Directional)
    """
    BlockData: Directional
    """
    MAGENTA_WALL_BANNER = (23291, Directional)
    """
    BlockData: Directional
    """
    LIGHT_BLUE_WALL_BANNER = (12011, Directional)
    """
    BlockData: Directional
    """
    YELLOW_WALL_BANNER = (32004, Directional)
    """
    BlockData: Directional
    """
    LIME_WALL_BANNER = (21422, Directional)
    """
    BlockData: Directional
    """
    PINK_WALL_BANNER = (9421, Directional)
    """
    BlockData: Directional
    """
    GRAY_WALL_BANNER = (24275, Directional)
    """
    BlockData: Directional
    """
    LIGHT_GRAY_WALL_BANNER = (31088, Directional)
    """
    BlockData: Directional
    """
    CYAN_WALL_BANNER = (10889, Directional)
    """
    BlockData: Directional
    """
    PURPLE_WALL_BANNER = (14298, Directional)
    """
    BlockData: Directional
    """
    BLUE_WALL_BANNER = (17757, Directional)
    """
    BlockData: Directional
    """
    BROWN_WALL_BANNER = (14731, Directional)
    """
    BlockData: Directional
    """
    GREEN_WALL_BANNER = (15046, Directional)
    """
    BlockData: Directional
    """
    RED_WALL_BANNER = (4378, Directional)
    """
    BlockData: Directional
    """
    BLACK_WALL_BANNER = (4919, Directional)
    """
    BlockData: Directional
    """
    TORCHFLOWER_CROP = (28460, Ageable)
    """
    BlockData: Ageable
    """
    PITCHER_CROP = (15420, PitcherCrop)
    """
    BlockData: PitcherCrop
    """
    BEETROOTS = (22075, Ageable)
    """
    BlockData: Ageable
    """
    END_GATEWAY = (26605)
    FROSTED_ICE = (21814, Ageable)
    """
    BlockData: Ageable
    """
    KELP_PLANT = (29697)
    DEAD_TUBE_CORAL_WALL_FAN = (5128, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    DEAD_BRAIN_CORAL_WALL_FAN = (23718, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    DEAD_BUBBLE_CORAL_WALL_FAN = (18453, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    DEAD_FIRE_CORAL_WALL_FAN = (23375, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    DEAD_HORN_CORAL_WALL_FAN = (27550, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    TUBE_CORAL_WALL_FAN = (25282, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    BRAIN_CORAL_WALL_FAN = (22685, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    BUBBLE_CORAL_WALL_FAN = (20382, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    FIRE_CORAL_WALL_FAN = (20100, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    HORN_CORAL_WALL_FAN = (28883, CoralWallFan)
    """
    BlockData: CoralWallFan
    """
    BAMBOO_SAPLING = (8478)
    POTTED_BAMBOO = (22542)
    VOID_AIR = (13668)
    CAVE_AIR = (17422)
    BUBBLE_COLUMN = (31612, BubbleColumn)
    """
    BlockData: BubbleColumn
    """
    SWEET_BERRY_BUSH = (11958, Ageable)
    """
    BlockData: Ageable
    """
    WEEPING_VINES_PLANT = (19437)
    TWISTING_VINES_PLANT = (25338)
    CRIMSON_WALL_SIGN = (19242, 16, WallSign)
    """
    BlockData: WallSign
    """
    WARPED_WALL_SIGN = (13534, 16, WallSign)
    """
    BlockData: WallSign
    """
    POTTED_CRIMSON_FUNGUS = (5548)
    POTTED_WARPED_FUNGUS = (30800)
    POTTED_CRIMSON_ROOTS = (13852)
    POTTED_WARPED_ROOTS = (6403)
    CANDLE_CAKE = (25423, Lightable)
    """
    BlockData: Lightable
    """
    WHITE_CANDLE_CAKE = (12674, Lightable)
    """
    BlockData: Lightable
    """
    ORANGE_CANDLE_CAKE = (24982, Lightable)
    """
    BlockData: Lightable
    """
    MAGENTA_CANDLE_CAKE = (11022, Lightable)
    """
    BlockData: Lightable
    """
    LIGHT_BLUE_CANDLE_CAKE = (7787, Lightable)
    """
    BlockData: Lightable
    """
    YELLOW_CANDLE_CAKE = (17157, Lightable)
    """
    BlockData: Lightable
    """
    LIME_CANDLE_CAKE = (14309, Lightable)
    """
    BlockData: Lightable
    """
    PINK_CANDLE_CAKE = (20405, Lightable)
    """
    BlockData: Lightable
    """
    GRAY_CANDLE_CAKE = (6777, Lightable)
    """
    BlockData: Lightable
    """
    LIGHT_GRAY_CANDLE_CAKE = (11318, Lightable)
    """
    BlockData: Lightable
    """
    CYAN_CANDLE_CAKE = (21202, Lightable)
    """
    BlockData: Lightable
    """
    PURPLE_CANDLE_CAKE = (22663, Lightable)
    """
    BlockData: Lightable
    """
    BLUE_CANDLE_CAKE = (26425, Lightable)
    """
    BlockData: Lightable
    """
    BROWN_CANDLE_CAKE = (26024, Lightable)
    """
    BlockData: Lightable
    """
    GREEN_CANDLE_CAKE = (16334, Lightable)
    """
    BlockData: Lightable
    """
    RED_CANDLE_CAKE = (24151, Lightable)
    """
    BlockData: Lightable
    """
    BLACK_CANDLE_CAKE = (15191, Lightable)
    """
    BlockData: Lightable
    """
    POWDER_SNOW = (24077)
    CAVE_VINES = (7339, CaveVines)
    """
    BlockData: CaveVines
    """
    CAVE_VINES_PLANT = (30645, CaveVinesPlant)
    """
    BlockData: CaveVinesPlant
    """
    BIG_DRIPLEAF_STEM = (13167, Dripleaf)
    """
    BlockData: Dripleaf
    """
    POTTED_AZALEA_BUSH = (20430)
    POTTED_FLOWERING_AZALEA_BUSH = (10609)
    LEGACY_AIR = (0, 0)
    LEGACY_STONE = (1)
    LEGACY_GRASS = (2)
    LEGACY_DIRT = (3)
    LEGACY_COBBLESTONE = (4)
    LEGACY_WOOD = (5, org.bukkit.material.Wood)
    LEGACY_SAPLING = (6, org.bukkit.material.Sapling)
    LEGACY_BEDROCK = (7)
    LEGACY_WATER = (8, org.bukkit.material.MaterialData)
    LEGACY_STATIONARY_WATER = (9, org.bukkit.material.MaterialData)
    LEGACY_LAVA = (10, org.bukkit.material.MaterialData)
    LEGACY_STATIONARY_LAVA = (11, org.bukkit.material.MaterialData)
    LEGACY_SAND = (12)
    LEGACY_GRAVEL = (13)
    LEGACY_GOLD_ORE = (14)
    LEGACY_IRON_ORE = (15)
    LEGACY_COAL_ORE = (16)
    LEGACY_LOG = (17, org.bukkit.material.Tree)
    LEGACY_LEAVES = (18, org.bukkit.material.Leaves)
    LEGACY_SPONGE = (19)
    LEGACY_GLASS = (20)
    LEGACY_LAPIS_ORE = (21)
    LEGACY_LAPIS_BLOCK = (22)
    LEGACY_DISPENSER = (23, org.bukkit.material.Dispenser)
    LEGACY_SANDSTONE = (24, org.bukkit.material.Sandstone)
    LEGACY_NOTE_BLOCK = (25)
    LEGACY_BED_BLOCK = (26, org.bukkit.material.Bed)
    LEGACY_POWERED_RAIL = (27, org.bukkit.material.PoweredRail)
    LEGACY_DETECTOR_RAIL = (28, org.bukkit.material.DetectorRail)
    LEGACY_PISTON_STICKY_BASE = (29, org.bukkit.material.PistonBaseMaterial)
    LEGACY_WEB = (30)
    LEGACY_LONG_GRASS = (31, org.bukkit.material.LongGrass)
    LEGACY_DEAD_BUSH = (32)
    LEGACY_PISTON_BASE = (33, org.bukkit.material.PistonBaseMaterial)
    LEGACY_PISTON_EXTENSION = (34, org.bukkit.material.PistonExtensionMaterial)
    LEGACY_WOOL = (35, org.bukkit.material.Wool)
    LEGACY_PISTON_MOVING_PIECE = (36)
    LEGACY_YELLOW_FLOWER = (37)
    LEGACY_RED_ROSE = (38)
    LEGACY_BROWN_MUSHROOM = (39)
    LEGACY_RED_MUSHROOM = (40)
    LEGACY_GOLD_BLOCK = (41)
    LEGACY_IRON_BLOCK = (42)
    LEGACY_DOUBLE_STEP = (43, org.bukkit.material.Step)
    LEGACY_STEP = (44, org.bukkit.material.Step)
    LEGACY_BRICK = (45)
    LEGACY_TNT = (46)
    LEGACY_BOOKSHELF = (47)
    LEGACY_MOSSY_COBBLESTONE = (48)
    LEGACY_OBSIDIAN = (49)
    LEGACY_TORCH = (50, org.bukkit.material.Torch)
    LEGACY_FIRE = (51)
    LEGACY_MOB_SPAWNER = (52)
    LEGACY_WOOD_STAIRS = (53, org.bukkit.material.Stairs)
    LEGACY_CHEST = (54, org.bukkit.material.Chest)
    LEGACY_REDSTONE_WIRE = (55, org.bukkit.material.RedstoneWire)
    LEGACY_DIAMOND_ORE = (56)
    LEGACY_DIAMOND_BLOCK = (57)
    LEGACY_WORKBENCH = (58)
    LEGACY_CROPS = (59, org.bukkit.material.Crops)
    LEGACY_SOIL = (60, org.bukkit.material.MaterialData)
    LEGACY_FURNACE = (61, org.bukkit.material.Furnace)
    LEGACY_BURNING_FURNACE = (62, org.bukkit.material.Furnace)
    LEGACY_SIGN_POST = (63, 64, org.bukkit.material.Sign)
    LEGACY_WOODEN_DOOR = (64, org.bukkit.material.Door)
    LEGACY_LADDER = (65, org.bukkit.material.Ladder)
    LEGACY_RAILS = (66, org.bukkit.material.Rails)
    LEGACY_COBBLESTONE_STAIRS = (67, org.bukkit.material.Stairs)
    LEGACY_WALL_SIGN = (68, 64, org.bukkit.material.Sign)
    LEGACY_LEVER = (69, org.bukkit.material.Lever)
    LEGACY_STONE_PLATE = (70, org.bukkit.material.PressurePlate)
    LEGACY_IRON_DOOR_BLOCK = (71, org.bukkit.material.Door)
    LEGACY_WOOD_PLATE = (72, org.bukkit.material.PressurePlate)
    LEGACY_REDSTONE_ORE = (73)
    LEGACY_GLOWING_REDSTONE_ORE = (74)
    LEGACY_REDSTONE_TORCH_OFF = (75, org.bukkit.material.RedstoneTorch)
    LEGACY_REDSTONE_TORCH_ON = (76, org.bukkit.material.RedstoneTorch)
    LEGACY_STONE_BUTTON = (77, org.bukkit.material.Button)
    LEGACY_SNOW = (78)
    LEGACY_ICE = (79)
    LEGACY_SNOW_BLOCK = (80)
    LEGACY_CACTUS = (81, org.bukkit.material.MaterialData)
    LEGACY_CLAY = (82)
    LEGACY_SUGAR_CANE_BLOCK = (83, org.bukkit.material.MaterialData)
    LEGACY_JUKEBOX = (84)
    LEGACY_FENCE = (85)
    LEGACY_PUMPKIN = (86, org.bukkit.material.Pumpkin)
    LEGACY_NETHERRACK = (87)
    LEGACY_SOUL_SAND = (88)
    LEGACY_GLOWSTONE = (89)
    LEGACY_PORTAL = (90)
    LEGACY_JACK_O_LANTERN = (91, org.bukkit.material.Pumpkin)
    LEGACY_CAKE_BLOCK = (92, 64, org.bukkit.material.Cake)
    LEGACY_DIODE_BLOCK_OFF = (93, org.bukkit.material.Diode)
    LEGACY_DIODE_BLOCK_ON = (94, org.bukkit.material.Diode)
    LEGACY_STAINED_GLASS = (95)
    LEGACY_TRAP_DOOR = (96, org.bukkit.material.TrapDoor)
    LEGACY_MONSTER_EGGS = (97, org.bukkit.material.MonsterEggs)
    LEGACY_SMOOTH_BRICK = (98, org.bukkit.material.SmoothBrick)
    LEGACY_HUGE_MUSHROOM_1 = (99, org.bukkit.material.Mushroom)
    LEGACY_HUGE_MUSHROOM_2 = (100, org.bukkit.material.Mushroom)
    LEGACY_IRON_FENCE = (101)
    LEGACY_THIN_GLASS = (102)
    LEGACY_MELON_BLOCK = (103)
    LEGACY_PUMPKIN_STEM = (104, org.bukkit.material.MaterialData)
    LEGACY_MELON_STEM = (105, org.bukkit.material.MaterialData)
    LEGACY_VINE = (106, org.bukkit.material.Vine)
    LEGACY_FENCE_GATE = (107, org.bukkit.material.Gate)
    LEGACY_BRICK_STAIRS = (108, org.bukkit.material.Stairs)
    LEGACY_SMOOTH_STAIRS = (109, org.bukkit.material.Stairs)
    LEGACY_MYCEL = (110)
    LEGACY_WATER_LILY = (111)
    LEGACY_NETHER_BRICK = (112)
    LEGACY_NETHER_FENCE = (113)
    LEGACY_NETHER_BRICK_STAIRS = (114, org.bukkit.material.Stairs)
    LEGACY_NETHER_WARTS = (115, org.bukkit.material.NetherWarts)
    LEGACY_ENCHANTMENT_TABLE = (116)
    LEGACY_BREWING_STAND = (117, org.bukkit.material.MaterialData)
    LEGACY_CAULDRON = (118, org.bukkit.material.Cauldron)
    LEGACY_ENDER_PORTAL = (119)
    LEGACY_ENDER_PORTAL_FRAME = (120)
    LEGACY_ENDER_STONE = (121)
    LEGACY_DRAGON_EGG = (122)
    LEGACY_REDSTONE_LAMP_OFF = (123)
    LEGACY_REDSTONE_LAMP_ON = (124)
    LEGACY_WOOD_DOUBLE_STEP = (125, org.bukkit.material.Wood)
    LEGACY_WOOD_STEP = (126, org.bukkit.material.WoodenStep)
    LEGACY_COCOA = (127, org.bukkit.material.CocoaPlant)
    LEGACY_SANDSTONE_STAIRS = (128, org.bukkit.material.Stairs)
    LEGACY_EMERALD_ORE = (129)
    LEGACY_ENDER_CHEST = (130, org.bukkit.material.EnderChest)
    LEGACY_TRIPWIRE_HOOK = (131, org.bukkit.material.TripwireHook)
    LEGACY_TRIPWIRE = (132, org.bukkit.material.Tripwire)
    LEGACY_EMERALD_BLOCK = (133)
    LEGACY_SPRUCE_WOOD_STAIRS = (134, org.bukkit.material.Stairs)
    LEGACY_BIRCH_WOOD_STAIRS = (135, org.bukkit.material.Stairs)
    LEGACY_JUNGLE_WOOD_STAIRS = (136, org.bukkit.material.Stairs)
    LEGACY_COMMAND = (137, org.bukkit.material.Command)
    LEGACY_BEACON = (138)
    LEGACY_COBBLE_WALL = (139)
    LEGACY_FLOWER_POT = (140, org.bukkit.material.FlowerPot)
    LEGACY_CARROT = (141, org.bukkit.material.Crops)
    LEGACY_POTATO = (142, org.bukkit.material.Crops)
    LEGACY_WOOD_BUTTON = (143, org.bukkit.material.Button)
    LEGACY_SKULL = (144, org.bukkit.material.Skull)
    LEGACY_ANVIL = (145)
    LEGACY_TRAPPED_CHEST = (146, org.bukkit.material.Chest)
    LEGACY_GOLD_PLATE = (147)
    LEGACY_IRON_PLATE = (148)
    LEGACY_REDSTONE_COMPARATOR_OFF = (149, org.bukkit.material.Comparator)
    LEGACY_REDSTONE_COMPARATOR_ON = (150, org.bukkit.material.Comparator)
    LEGACY_DAYLIGHT_DETECTOR = (151)
    LEGACY_REDSTONE_BLOCK = (152)
    LEGACY_QUARTZ_ORE = (153)
    LEGACY_HOPPER = (154, org.bukkit.material.Hopper)
    LEGACY_QUARTZ_BLOCK = (155)
    LEGACY_QUARTZ_STAIRS = (156, org.bukkit.material.Stairs)
    LEGACY_ACTIVATOR_RAIL = (157, org.bukkit.material.PoweredRail)
    LEGACY_DROPPER = (158, org.bukkit.material.Dispenser)
    LEGACY_STAINED_CLAY = (159)
    LEGACY_STAINED_GLASS_PANE = (160)
    LEGACY_LEAVES_2 = (161, org.bukkit.material.Leaves)
    LEGACY_LOG_2 = (162, org.bukkit.material.Tree)
    LEGACY_ACACIA_STAIRS = (163, org.bukkit.material.Stairs)
    LEGACY_DARK_OAK_STAIRS = (164, org.bukkit.material.Stairs)
    LEGACY_SLIME_BLOCK = (165)
    LEGACY_BARRIER = (166)
    LEGACY_IRON_TRAPDOOR = (167, org.bukkit.material.TrapDoor)
    LEGACY_PRISMARINE = (168)
    LEGACY_SEA_LANTERN = (169)
    LEGACY_HAY_BLOCK = (170)
    LEGACY_CARPET = (171)
    LEGACY_HARD_CLAY = (172)
    LEGACY_COAL_BLOCK = (173)
    LEGACY_PACKED_ICE = (174)
    LEGACY_DOUBLE_PLANT = (175)
    LEGACY_STANDING_BANNER = (176, org.bukkit.material.Banner)
    LEGACY_WALL_BANNER = (177, org.bukkit.material.Banner)
    LEGACY_DAYLIGHT_DETECTOR_INVERTED = (178)
    LEGACY_RED_SANDSTONE = (179)
    LEGACY_RED_SANDSTONE_STAIRS = (180, org.bukkit.material.Stairs)
    LEGACY_DOUBLE_STONE_SLAB2 = (181)
    LEGACY_STONE_SLAB2 = (182)
    LEGACY_SPRUCE_FENCE_GATE = (183, org.bukkit.material.Gate)
    LEGACY_BIRCH_FENCE_GATE = (184, org.bukkit.material.Gate)
    LEGACY_JUNGLE_FENCE_GATE = (185, org.bukkit.material.Gate)
    LEGACY_DARK_OAK_FENCE_GATE = (186, org.bukkit.material.Gate)
    LEGACY_ACACIA_FENCE_GATE = (187, org.bukkit.material.Gate)
    LEGACY_SPRUCE_FENCE = (188)
    LEGACY_BIRCH_FENCE = (189)
    LEGACY_JUNGLE_FENCE = (190)
    LEGACY_DARK_OAK_FENCE = (191)
    LEGACY_ACACIA_FENCE = (192)
    LEGACY_SPRUCE_DOOR = (193, org.bukkit.material.Door)
    LEGACY_BIRCH_DOOR = (194, org.bukkit.material.Door)
    LEGACY_JUNGLE_DOOR = (195, org.bukkit.material.Door)
    LEGACY_ACACIA_DOOR = (196, org.bukkit.material.Door)
    LEGACY_DARK_OAK_DOOR = (197, org.bukkit.material.Door)
    LEGACY_END_ROD = (198)
    LEGACY_CHORUS_PLANT = (199)
    LEGACY_CHORUS_FLOWER = (200)
    LEGACY_PURPUR_BLOCK = (201)
    LEGACY_PURPUR_PILLAR = (202)
    LEGACY_PURPUR_STAIRS = (203, org.bukkit.material.Stairs)
    LEGACY_PURPUR_DOUBLE_SLAB = (204)
    LEGACY_PURPUR_SLAB = (205)
    LEGACY_END_BRICKS = (206)
    LEGACY_BEETROOT_BLOCK = (207, org.bukkit.material.Crops)
    LEGACY_GRASS_PATH = (208)
    LEGACY_END_GATEWAY = (209)
    LEGACY_COMMAND_REPEATING = (210, org.bukkit.material.Command)
    LEGACY_COMMAND_CHAIN = (211, org.bukkit.material.Command)
    LEGACY_FROSTED_ICE = (212)
    LEGACY_MAGMA = (213)
    LEGACY_NETHER_WART_BLOCK = (214)
    LEGACY_RED_NETHER_BRICK = (215)
    LEGACY_BONE_BLOCK = (216)
    LEGACY_STRUCTURE_VOID = (217)
    LEGACY_OBSERVER = (218, org.bukkit.material.Observer)
    LEGACY_WHITE_SHULKER_BOX = (219, 1)
    LEGACY_ORANGE_SHULKER_BOX = (220, 1)
    LEGACY_MAGENTA_SHULKER_BOX = (221, 1)
    LEGACY_LIGHT_BLUE_SHULKER_BOX = (222, 1)
    LEGACY_YELLOW_SHULKER_BOX = (223, 1)
    LEGACY_LIME_SHULKER_BOX = (224, 1)
    LEGACY_PINK_SHULKER_BOX = (225, 1)
    LEGACY_GRAY_SHULKER_BOX = (226, 1)
    LEGACY_SILVER_SHULKER_BOX = (227, 1)
    LEGACY_CYAN_SHULKER_BOX = (228, 1)
    LEGACY_PURPLE_SHULKER_BOX = (229, 1)
    LEGACY_BLUE_SHULKER_BOX = (230, 1)
    LEGACY_BROWN_SHULKER_BOX = (231, 1)
    LEGACY_GREEN_SHULKER_BOX = (232, 1)
    LEGACY_RED_SHULKER_BOX = (233, 1)
    LEGACY_BLACK_SHULKER_BOX = (234, 1)
    LEGACY_WHITE_GLAZED_TERRACOTTA = (235)
    LEGACY_ORANGE_GLAZED_TERRACOTTA = (236)
    LEGACY_MAGENTA_GLAZED_TERRACOTTA = (237)
    LEGACY_LIGHT_BLUE_GLAZED_TERRACOTTA = (238)
    LEGACY_YELLOW_GLAZED_TERRACOTTA = (239)
    LEGACY_LIME_GLAZED_TERRACOTTA = (240)
    LEGACY_PINK_GLAZED_TERRACOTTA = (241)
    LEGACY_GRAY_GLAZED_TERRACOTTA = (242)
    LEGACY_SILVER_GLAZED_TERRACOTTA = (243)
    LEGACY_CYAN_GLAZED_TERRACOTTA = (244)
    LEGACY_PURPLE_GLAZED_TERRACOTTA = (245)
    LEGACY_BLUE_GLAZED_TERRACOTTA = (246)
    LEGACY_BROWN_GLAZED_TERRACOTTA = (247)
    LEGACY_GREEN_GLAZED_TERRACOTTA = (248)
    LEGACY_RED_GLAZED_TERRACOTTA = (249)
    LEGACY_BLACK_GLAZED_TERRACOTTA = (250)
    LEGACY_CONCRETE = (251)
    LEGACY_CONCRETE_POWDER = (252)
    LEGACY_STRUCTURE_BLOCK = (255)
    LEGACY_IRON_SPADE = (256, 1, 250)
    LEGACY_IRON_PICKAXE = (257, 1, 250)
    LEGACY_IRON_AXE = (258, 1, 250)
    LEGACY_FLINT_AND_STEEL = (259, 1, 64)
    LEGACY_APPLE = (260)
    LEGACY_BOW = (261, 1, 384)
    LEGACY_ARROW = (262)
    LEGACY_COAL = (263, org.bukkit.material.Coal)
    LEGACY_DIAMOND = (264)
    LEGACY_IRON_INGOT = (265)
    LEGACY_GOLD_INGOT = (266)
    LEGACY_IRON_SWORD = (267, 1, 250)
    LEGACY_WOOD_SWORD = (268, 1, 59)
    LEGACY_WOOD_SPADE = (269, 1, 59)
    LEGACY_WOOD_PICKAXE = (270, 1, 59)
    LEGACY_WOOD_AXE = (271, 1, 59)
    LEGACY_STONE_SWORD = (272, 1, 131)
    LEGACY_STONE_SPADE = (273, 1, 131)
    LEGACY_STONE_PICKAXE = (274, 1, 131)
    LEGACY_STONE_AXE = (275, 1, 131)
    LEGACY_DIAMOND_SWORD = (276, 1, 1561)
    LEGACY_DIAMOND_SPADE = (277, 1, 1561)
    LEGACY_DIAMOND_PICKAXE = (278, 1, 1561)
    LEGACY_DIAMOND_AXE = (279, 1, 1561)
    LEGACY_STICK = (280)
    LEGACY_BOWL = (281)
    LEGACY_MUSHROOM_SOUP = (282, 1)
    LEGACY_GOLD_SWORD = (283, 1, 32)
    LEGACY_GOLD_SPADE = (284, 1, 32)
    LEGACY_GOLD_PICKAXE = (285, 1, 32)
    LEGACY_GOLD_AXE = (286, 1, 32)
    LEGACY_STRING = (287)
    LEGACY_FEATHER = (288)
    LEGACY_SULPHUR = (289)
    LEGACY_WOOD_HOE = (290, 1, 59)
    LEGACY_STONE_HOE = (291, 1, 131)
    LEGACY_IRON_HOE = (292, 1, 250)
    LEGACY_DIAMOND_HOE = (293, 1, 1561)
    LEGACY_GOLD_HOE = (294, 1, 32)
    LEGACY_SEEDS = (295)
    LEGACY_WHEAT = (296)
    LEGACY_BREAD = (297)
    LEGACY_LEATHER_HELMET = (298, 1, 55)
    LEGACY_LEATHER_CHESTPLATE = (299, 1, 80)
    LEGACY_LEATHER_LEGGINGS = (300, 1, 75)
    LEGACY_LEATHER_BOOTS = (301, 1, 65)
    LEGACY_CHAINMAIL_HELMET = (302, 1, 165)
    LEGACY_CHAINMAIL_CHESTPLATE = (303, 1, 240)
    LEGACY_CHAINMAIL_LEGGINGS = (304, 1, 225)
    LEGACY_CHAINMAIL_BOOTS = (305, 1, 195)
    LEGACY_IRON_HELMET = (306, 1, 165)
    LEGACY_IRON_CHESTPLATE = (307, 1, 240)
    LEGACY_IRON_LEGGINGS = (308, 1, 225)
    LEGACY_IRON_BOOTS = (309, 1, 195)
    LEGACY_DIAMOND_HELMET = (310, 1, 363)
    LEGACY_DIAMOND_CHESTPLATE = (311, 1, 528)
    LEGACY_DIAMOND_LEGGINGS = (312, 1, 495)
    LEGACY_DIAMOND_BOOTS = (313, 1, 429)
    LEGACY_GOLD_HELMET = (314, 1, 77)
    LEGACY_GOLD_CHESTPLATE = (315, 1, 112)
    LEGACY_GOLD_LEGGINGS = (316, 1, 105)
    LEGACY_GOLD_BOOTS = (317, 1, 91)
    LEGACY_FLINT = (318)
    LEGACY_PORK = (319)
    LEGACY_GRILLED_PORK = (320)
    LEGACY_PAINTING = (321)
    LEGACY_GOLDEN_APPLE = (322)
    LEGACY_SIGN = (323, 16)
    LEGACY_WOOD_DOOR = (324, 64)
    LEGACY_BUCKET = (325, 16)
    LEGACY_WATER_BUCKET = (326, 1)
    LEGACY_LAVA_BUCKET = (327, 1)
    LEGACY_MINECART = (328, 1)
    LEGACY_SADDLE = (329, 1)
    LEGACY_IRON_DOOR = (330, 64)
    LEGACY_REDSTONE = (331)
    LEGACY_SNOW_BALL = (332, 16)
    LEGACY_BOAT = (333, 1)
    LEGACY_LEATHER = (334)
    LEGACY_MILK_BUCKET = (335, 1)
    LEGACY_CLAY_BRICK = (336)
    LEGACY_CLAY_BALL = (337)
    LEGACY_SUGAR_CANE = (338)
    LEGACY_PAPER = (339)
    LEGACY_BOOK = (340)
    LEGACY_SLIME_BALL = (341)
    LEGACY_STORAGE_MINECART = (342, 1)
    LEGACY_POWERED_MINECART = (343, 1)
    LEGACY_EGG = (344, 16)
    LEGACY_COMPASS = (345)
    LEGACY_FISHING_ROD = (346, 1, 64)
    LEGACY_WATCH = (347)
    LEGACY_GLOWSTONE_DUST = (348)
    LEGACY_RAW_FISH = (349)
    LEGACY_COOKED_FISH = (350)
    LEGACY_INK_SACK = (351, org.bukkit.material.Dye)
    LEGACY_BONE = (352)
    LEGACY_SUGAR = (353)
    LEGACY_CAKE = (354, 1)
    LEGACY_BED = (355, 1)
    LEGACY_DIODE = (356)
    LEGACY_COOKIE = (357)
    LEGACY_MAP = (358, org.bukkit.material.MaterialData)
    """
    See
    - org.bukkit.map.MapView
    """
    LEGACY_SHEARS = (359, 1, 238)
    LEGACY_MELON = (360)
    LEGACY_PUMPKIN_SEEDS = (361)
    LEGACY_MELON_SEEDS = (362)
    LEGACY_RAW_BEEF = (363)
    LEGACY_COOKED_BEEF = (364)
    LEGACY_RAW_CHICKEN = (365)
    LEGACY_COOKED_CHICKEN = (366)
    LEGACY_ROTTEN_FLESH = (367)
    LEGACY_ENDER_PEARL = (368, 16)
    LEGACY_BLAZE_ROD = (369)
    LEGACY_GHAST_TEAR = (370)
    LEGACY_GOLD_NUGGET = (371)
    LEGACY_NETHER_STALK = (372)
    LEGACY_POTION = (373, 1, org.bukkit.material.MaterialData)
    LEGACY_GLASS_BOTTLE = (374)
    LEGACY_SPIDER_EYE = (375)
    LEGACY_FERMENTED_SPIDER_EYE = (376)
    LEGACY_BLAZE_POWDER = (377)
    LEGACY_MAGMA_CREAM = (378)
    LEGACY_BREWING_STAND_ITEM = (379)
    LEGACY_CAULDRON_ITEM = (380)
    LEGACY_EYE_OF_ENDER = (381)
    LEGACY_SPECKLED_MELON = (382)
    LEGACY_MONSTER_EGG = (383, 64, org.bukkit.material.SpawnEgg)
    LEGACY_EXP_BOTTLE = (384, 64)
    LEGACY_FIREBALL = (385, 64)
    LEGACY_BOOK_AND_QUILL = (386, 1)
    LEGACY_WRITTEN_BOOK = (387, 16)
    LEGACY_EMERALD = (388, 64)
    LEGACY_ITEM_FRAME = (389)
    LEGACY_FLOWER_POT_ITEM = (390)
    LEGACY_CARROT_ITEM = (391)
    LEGACY_POTATO_ITEM = (392)
    LEGACY_BAKED_POTATO = (393)
    LEGACY_POISONOUS_POTATO = (394)
    LEGACY_EMPTY_MAP = (395)
    LEGACY_GOLDEN_CARROT = (396)
    LEGACY_SKULL_ITEM = (397)
    LEGACY_CARROT_STICK = (398, 1, 25)
    LEGACY_NETHER_STAR = (399)
    LEGACY_PUMPKIN_PIE = (400)
    LEGACY_FIREWORK = (401)
    LEGACY_FIREWORK_CHARGE = (402)
    LEGACY_ENCHANTED_BOOK = (403, 1)
    LEGACY_REDSTONE_COMPARATOR = (404)
    LEGACY_NETHER_BRICK_ITEM = (405)
    LEGACY_QUARTZ = (406)
    LEGACY_EXPLOSIVE_MINECART = (407, 1)
    LEGACY_HOPPER_MINECART = (408, 1)
    LEGACY_PRISMARINE_SHARD = (409)
    LEGACY_PRISMARINE_CRYSTALS = (410)
    LEGACY_RABBIT = (411)
    LEGACY_COOKED_RABBIT = (412)
    LEGACY_RABBIT_STEW = (413, 1)
    LEGACY_RABBIT_FOOT = (414)
    LEGACY_RABBIT_HIDE = (415)
    LEGACY_ARMOR_STAND = (416, 16)
    LEGACY_IRON_BARDING = (417, 1)
    LEGACY_GOLD_BARDING = (418, 1)
    LEGACY_DIAMOND_BARDING = (419, 1)
    LEGACY_LEASH = (420)
    LEGACY_NAME_TAG = (421)
    LEGACY_COMMAND_MINECART = (422, 1)
    LEGACY_MUTTON = (423)
    LEGACY_COOKED_MUTTON = (424)
    LEGACY_BANNER = (425, 16)
    LEGACY_END_CRYSTAL = (426)
    LEGACY_SPRUCE_DOOR_ITEM = (427)
    LEGACY_BIRCH_DOOR_ITEM = (428)
    LEGACY_JUNGLE_DOOR_ITEM = (429)
    LEGACY_ACACIA_DOOR_ITEM = (430)
    LEGACY_DARK_OAK_DOOR_ITEM = (431)
    LEGACY_CHORUS_FRUIT = (432)
    LEGACY_CHORUS_FRUIT_POPPED = (433)
    LEGACY_BEETROOT = (434)
    LEGACY_BEETROOT_SEEDS = (435)
    LEGACY_BEETROOT_SOUP = (436, 1)
    LEGACY_DRAGONS_BREATH = (437)
    LEGACY_SPLASH_POTION = (438, 1)
    LEGACY_SPECTRAL_ARROW = (439)
    LEGACY_TIPPED_ARROW = (440)
    LEGACY_LINGERING_POTION = (441, 1)
    LEGACY_SHIELD = (442, 1, 336)
    LEGACY_ELYTRA = (443, 1, 431)
    LEGACY_BOAT_SPRUCE = (444, 1)
    LEGACY_BOAT_BIRCH = (445, 1)
    LEGACY_BOAT_JUNGLE = (446, 1)
    LEGACY_BOAT_ACACIA = (447, 1)
    LEGACY_BOAT_DARK_OAK = (448, 1)
    LEGACY_TOTEM = (449, 1)
    LEGACY_SHULKER_SHELL = (450)
    LEGACY_IRON_NUGGET = (452)
    LEGACY_KNOWLEDGE_BOOK = (453, 1)
    LEGACY_GOLD_RECORD = (2256, 1)
    LEGACY_GREEN_RECORD = (2257, 1)
    LEGACY_RECORD_3 = (2258, 1)
    LEGACY_RECORD_4 = (2259, 1)
    LEGACY_RECORD_5 = (2260, 1)
    LEGACY_RECORD_6 = (2261, 1)
    LEGACY_RECORD_7 = (2262, 1)
    LEGACY_RECORD_8 = (2263, 1)
    LEGACY_RECORD_9 = (2264, 1)
    LEGACY_RECORD_10 = (2265, 1)
    LEGACY_RECORD_11 = (2266, 1)
    LEGACY_RECORD_12 = (2267, 1)


    def getId(self) -> int:
        """
        Do not use for any reason.

        Returns
        - ID of this material

        Deprecated
        - Magic value
        """
        ...


    def isLegacy(self) -> bool:
        """
        Do not use for any reason.

        Returns
        - legacy status
        """
        ...


    def getKey(self) -> "NamespacedKey":
        ...


    def getMaxStackSize(self) -> int:
        """
        Gets the maximum amount of this material that can be held in a stack.
        
        Note that this is the <strong>default</strong> maximum size for this Material.
        ItemStack ItemStacks are able to change their maximum stack size per
        stack with ItemMeta.setMaxStackSize(Integer). If an ItemStack instance
        is available, ItemStack.getMaxStackSize() may be preferred.

        Returns
        - Maximum stack size for this material
        """
        ...


    def getMaxDurability(self) -> int:
        """
        Gets the maximum durability of this material

        Returns
        - Maximum durability for this material
        """
        ...


    def createBlockData(self) -> "BlockData":
        """
        Creates a new BlockData instance for this Material, with all
        properties initialized to unspecified defaults.

        Returns
        - new data instance
        """
        ...


    def createBlockData(self, consumer: "Consumer"["BlockData"]) -> "BlockData":
        """
        Creates a new BlockData instance for this Material, with
        all properties initialized to unspecified defaults.

        Arguments
        - consumer: consumer to run on new instance before returning

        Returns
        - new data instance
        """
        ...


    def createBlockData(self, data: str) -> "BlockData":
        """
        Creates a new BlockData instance for this Material, with all
        properties initialized to unspecified defaults, except for those provided
        in data.

        Arguments
        - data: data string

        Returns
        - new data instance

        Raises
        - IllegalArgumentException: if the specified data is not valid
        """
        ...


    def getData(self) -> type["MaterialData"]:
        """
        Gets the MaterialData class associated with this Material

        Returns
        - MaterialData associated with this Material
        """
        ...


    def getNewData(self, raw: int) -> "MaterialData":
        """
        Constructs a new MaterialData relevant for this Material, with the
        given initial data

        Arguments
        - raw: Initial data to construct the MaterialData with

        Returns
        - New MaterialData with the given data

        Deprecated
        - Magic value
        """
        ...


    def isBlock(self) -> bool:
        """
        Checks if this Material is a placable block

        Returns
        - True if this material is a block
        """
        ...


    def isEdible(self) -> bool:
        """
        Checks if this Material is edible.

        Returns
        - True if this Material is edible.
        """
        ...


    @staticmethod
    def getMaterial(name: str) -> "Material":
        """
        Attempts to get the Material with the given name.
        
        This is a normal lookup, names must be the precise name they are given
        in the enum.

        Arguments
        - name: Name of the material to get

        Returns
        - Material if found, or null
        """
        ...


    @staticmethod
    def getMaterial(name: str, legacyName: bool) -> "Material":
        """
        Attempts to get the Material with the given name.
        
        This is a normal lookup, names must be the precise name they are given in
        the enum (but optionally including the LEGACY_PREFIX if legacyName is
        True).
        
        If legacyName is True, then the lookup will be against legacy materials,
        but the returned Material will be a modern material (ie this method is
        useful for updating stored data).

        Arguments
        - name: Name of the material to get
        - legacyName: whether this is a legacy name lookup

        Returns
        - Material if found, or null
        """
        ...


    @staticmethod
    def matchMaterial(name: str) -> "Material":
        """
        Attempts to match the Material with the given name.
        
        This is a match lookup; names will be stripped of the "minecraft:"
        namespace, converted to uppercase, then stripped of special characters in
        an attempt to format it like the enum.

        Arguments
        - name: Name of the material to get

        Returns
        - Material if found, or null
        """
        ...


    @staticmethod
    def matchMaterial(name: str, legacyName: bool) -> "Material":
        """
        Attempts to match the Material with the given name.
        
        This is a match lookup; names will be stripped of the "minecraft:"
        namespace, converted to uppercase, then stripped of special characters in
        an attempt to format it like the enum.

        Arguments
        - name: Name of the material to get
        - legacyName: whether this is a legacy name (see
        .getMaterial(java.lang.String, boolean)

        Returns
        - Material if found, or null
        """
        ...


    def isRecord(self) -> bool:
        """
        Returns
        - True if this material represents a playable music disk.
        """
        ...


    def isSolid(self) -> bool:
        """
        Check if the material is a block and solid (can be built upon)

        Returns
        - True if this material is a block and solid
        """
        ...


    def isAir(self) -> bool:
        """
        Check if the material is an air block.

        Returns
        - True if this material is an air block.
        """
        ...


    def isTransparent(self) -> bool:
        """
        Check if the material is a block and does not block any light

        Returns
        - True if this material is a block and does not block any light

        Deprecated
        - currently does not have an implementation which is well
        linked to the underlying server. Contributions welcome.
        """
        ...


    def isFlammable(self) -> bool:
        """
        Check if the material is a block and can catch fire

        Returns
        - True if this material is a block and can catch fire
        """
        ...


    def isBurnable(self) -> bool:
        """
        Check if the material is a block and can burn away

        Returns
        - True if this material is a block and can burn away
        """
        ...


    def isFuel(self) -> bool:
        """
        Checks if this Material can be used as fuel in a Furnace

        Returns
        - True if this Material can be used as fuel.
        """
        ...


    def isOccluding(self) -> bool:
        """
        Check if the material is a block and occludes light in the lighting engine.
        
        Generally speaking, most full blocks will occlude light. Non-full blocks are
        not occluding (e.g. anvils, chests, tall grass, stairs, etc.), nor are specific
        full blocks such as barriers or spawners which block light despite their texture.
        
        An occluding block will have the following effects:
        
          - Chests cannot be opened if an occluding block is above it.
          - Mobs cannot spawn inside of occluding blocks.
          - Only occluding blocks can be "powered" (Block.isBlockPowered()).
        
        This list may be inconclusive. For a full list of the side effects of an occluding
        block, see the <a href="https://minecraft.wiki/w/Opacity">Minecraft Wiki</a>.

        Returns
        - True if this material is a block and occludes light
        """
        ...


    def hasGravity(self) -> bool:
        """
        Returns
        - True if this material is affected by gravity.
        """
        ...


    def isItem(self) -> bool:
        """
        Checks if this Material is an obtainable item.

        Returns
        - True if this material is an item
        """
        ...


    def isInteractable(self) -> bool:
        """
        Checks if this Material can be interacted with.
        
        Interactable materials include those with functionality when they are
        interacted with by a player such as chests, furnaces, etc.
        
        Some blocks such as piston heads and stairs are considered interactable
        though may not perform any additional functionality.
        
        Note that the interactability of some materials may be dependant on their
        state as well. This method will return True if there is at least one
        state in which additional interact handling is performed for the
        material.

        Returns
        - True if this material can be interacted with.
        """
        ...


    def getHardness(self) -> float:
        """
        Obtains the block's hardness level (also known as "strength").
        
        This number is used to calculate the time required to break each block.
        
        Only available when .isBlock() is True.

        Returns
        - the hardness of that material.
        """
        ...


    def getBlastResistance(self) -> float:
        """
        Obtains the blast resistance value (also known as block "durability").
        
        This value is used in explosions to calculate whether a block should be
        broken or not.
        
        Only available when .isBlock() is True.

        Returns
        - the blast resistance of that material.
        """
        ...


    def getSlipperiness(self) -> float:
        """
        Returns a value that represents how 'slippery' the block is.
        
        Blocks with higher slipperiness, like Material.ICE can be slid on
        further by the player and other entities.
        
        Most blocks have a default slipperiness of `0.6f`.
        
        Only available when .isBlock() is True.

        Returns
        - the slipperiness of this block
        """
        ...


    def getCraftingRemainingItem(self) -> "Material":
        """
        Determines the remaining item in a crafting grid after crafting with this
        ingredient.
        
        Only available when .isItem() is True.

        Returns
        - the item left behind when crafting, or null if nothing is.
        """
        ...


    def getEquipmentSlot(self) -> "EquipmentSlot":
        """
        Get the best suitable slot for this Material.
        
        For most items this will be EquipmentSlot.HAND.

        Returns
        - the best EquipmentSlot for this Material
        """
        ...


    def getDefaultAttributeModifiers(self, slot: "EquipmentSlot") -> "Multimap"["Attribute", "AttributeModifier"]:
        """
        Return an immutable copy of all default Attributes and their
        AttributeModifiers for a given EquipmentSlot.
        
        Default attributes are those that are always preset on some items, such
        as the attack damage on weapons or the armor value on armor.
        
        Only available when .isItem() is True.

        Arguments
        - slot: the EquipmentSlot to check

        Returns
        - the immutable Multimap with the respective default
        Attributes and modifiers, or an empty map if no attributes are set.
        """
        ...


    def getCreativeCategory(self) -> "CreativeCategory":
        """
        Get the CreativeCategory to which this material belongs.

        Returns
        - the creative category. null if does not belong to a category
        """
        ...


    def getTranslationKey(self) -> str:
        """
        Get the translation key of the item or block associated with this
        material.
        
        If this material has both an item and a block form, the item form is
        used.

        Returns
        - the translation key of the item or block associated with this
        material

        See
        - .getItemTranslationKey()
        """
        ...


    def getBlockTranslationKey(self) -> str:
        """
        Get the translation key of the block associated with this material, or
        null if this material does not have an associated block.

        Returns
        - the translation key of the block associated with this material,
        or null if this material does not have an associated block
        """
        ...


    def getItemTranslationKey(self) -> str:
        """
        Get the translation key of the item associated with this material, or
        null if this material does not have an associated item.

        Returns
        - the translation key of the item associated with this material, or
        null if this material does not have an associated item.
        """
        ...


    def isEnabledByFeature(self, world: "World") -> bool:
        """
        Gets if the Material is enabled by the features in a world.

        Arguments
        - world: the world to check

        Returns
        - True if this material can be used in this World.
        """
        ...


    def isCompostable(self) -> bool:
        """
        Checks whether this material is compostable (can be inserted into a
        composter).

        Returns
        - True if this material is compostable

        See
        - .getCompostChance()
        """
        ...


    def getCompostChance(self) -> float:
        """
        Get the chance that this material will successfully compost. The returned
        value is between 0 and 1 (inclusive).
        
        Materials with a compost chance of 1 will always raise the composter's
        level, while materials with a compost chance of 0 will never raise it.
        
        Plugins should check that .isCompostable returns True before
        calling this method.

        Returns
        - the chance that this material will successfully compost

        Raises
        - IllegalArgumentException: if the material is not compostable

        See
        - .isCompostable()
        """
        ...


    def asItemType(self) -> "ItemType":
        """
        Tries to convert this Material to an item type

        Returns
        - the converted item type or null

        Unknown Tags
        - only for internal use
        """
        ...


    def asBlockType(self) -> "BlockType":
        """
        Tries to convert this Material to a block type

        Returns
        - the converted block type or null

        Unknown Tags
        - only for internal use
        """
        ...
