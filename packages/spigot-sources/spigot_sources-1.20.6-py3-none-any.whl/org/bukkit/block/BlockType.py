"""
Python module generated from Java source file org.bukkit.block.BlockType

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util.function import Consumer
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import MinecraftExperimental
from org.bukkit.MinecraftExperimental import Requires
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit import World
from org.bukkit.block import *
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
from org.bukkit.block.data.type import Wall
from org.bukkit.block.data.type import WallHangingSign
from org.bukkit.block.data.type import WallSign
from org.bukkit.inventory import ItemType
from typing import Any, Callable, Iterable, Tuple


class BlockType(Keyed, Translatable):
    """
    While this API is in a public interface, it is not intended for use by
    plugins until further notice. The purpose of these types is to make
    Material more maintenance friendly, but will in due time be the
    official replacement for the aforementioned enum. Entirely incompatible
    changes may occur. Do not use this API in plugins.
    """

    AIR = getBlockType("air")
    STONE = getBlockType("stone")
    GRANITE = getBlockType("granite")
    POLISHED_GRANITE = getBlockType("polished_granite")
    DIORITE = getBlockType("diorite")
    POLISHED_DIORITE = getBlockType("polished_diorite")
    ANDESITE = getBlockType("andesite")
    POLISHED_ANDESITE = getBlockType("polished_andesite")
    GRASS_BLOCK = getBlockType("grass_block")
    """
    BlockData: Snowable
    """
    DIRT = getBlockType("dirt")
    COARSE_DIRT = getBlockType("coarse_dirt")
    PODZOL = getBlockType("podzol")
    """
    BlockData: Snowable
    """
    COBBLESTONE = getBlockType("cobblestone")
    OAK_PLANKS = getBlockType("oak_planks")
    SPRUCE_PLANKS = getBlockType("spruce_planks")
    BIRCH_PLANKS = getBlockType("birch_planks")
    JUNGLE_PLANKS = getBlockType("jungle_planks")
    ACACIA_PLANKS = getBlockType("acacia_planks")
    CHERRY_PLANKS = getBlockType("cherry_planks")
    DARK_OAK_PLANKS = getBlockType("dark_oak_planks")
    MANGROVE_PLANKS = getBlockType("mangrove_planks")
    BAMBOO_PLANKS = getBlockType("bamboo_planks")
    BAMBOO_MOSAIC = getBlockType("bamboo_mosaic")
    OAK_SAPLING = getBlockType("oak_sapling")
    """
    BlockData: Sapling
    """
    SPRUCE_SAPLING = getBlockType("spruce_sapling")
    """
    BlockData: Sapling
    """
    BIRCH_SAPLING = getBlockType("birch_sapling")
    """
    BlockData: Sapling
    """
    JUNGLE_SAPLING = getBlockType("jungle_sapling")
    """
    BlockData: Sapling
    """
    ACACIA_SAPLING = getBlockType("acacia_sapling")
    """
    BlockData: Sapling
    """
    CHERRY_SAPLING = getBlockType("cherry_sapling")
    """
    BlockData: Sapling
    """
    DARK_OAK_SAPLING = getBlockType("dark_oak_sapling")
    """
    BlockData: Sapling
    """
    MANGROVE_PROPAGULE = getBlockType("mangrove_propagule")
    """
    BlockData: MangrovePropagule
    """
    BEDROCK = getBlockType("bedrock")
    WATER = getBlockType("water")
    """
    BlockData: Levelled
    """
    LAVA = getBlockType("lava")
    """
    BlockData: Levelled
    """
    SAND = getBlockType("sand")
    SUSPICIOUS_SAND = getBlockType("suspicious_sand")
    """
    BlockData: Brushable
    """
    RED_SAND = getBlockType("red_sand")
    GRAVEL = getBlockType("gravel")
    SUSPICIOUS_GRAVEL = getBlockType("suspicious_gravel")
    """
    BlockData: Brushable
    """
    GOLD_ORE = getBlockType("gold_ore")
    DEEPSLATE_GOLD_ORE = getBlockType("deepslate_gold_ore")
    IRON_ORE = getBlockType("iron_ore")
    DEEPSLATE_IRON_ORE = getBlockType("deepslate_iron_ore")
    COAL_ORE = getBlockType("coal_ore")
    DEEPSLATE_COAL_ORE = getBlockType("deepslate_coal_ore")
    NETHER_GOLD_ORE = getBlockType("nether_gold_ore")
    OAK_LOG = getBlockType("oak_log")
    """
    BlockData: Orientable
    """
    SPRUCE_LOG = getBlockType("spruce_log")
    """
    BlockData: Orientable
    """
    BIRCH_LOG = getBlockType("birch_log")
    """
    BlockData: Orientable
    """
    JUNGLE_LOG = getBlockType("jungle_log")
    """
    BlockData: Orientable
    """
    ACACIA_LOG = getBlockType("acacia_log")
    """
    BlockData: Orientable
    """
    CHERRY_LOG = getBlockType("cherry_log")
    """
    BlockData: Orientable
    """
    DARK_OAK_LOG = getBlockType("dark_oak_log")
    """
    BlockData: Orientable
    """
    MANGROVE_LOG = getBlockType("mangrove_log")
    """
    BlockData: Orientable
    """
    MANGROVE_ROOTS = getBlockType("mangrove_roots")
    """
    BlockData: Waterlogged
    """
    MUDDY_MANGROVE_ROOTS = getBlockType("muddy_mangrove_roots")
    """
    BlockData: Orientable
    """
    BAMBOO_BLOCK = getBlockType("bamboo_block")
    """
    BlockData: Orientable
    """
    STRIPPED_SPRUCE_LOG = getBlockType("stripped_spruce_log")
    """
    BlockData: Orientable
    """
    STRIPPED_BIRCH_LOG = getBlockType("stripped_birch_log")
    """
    BlockData: Orientable
    """
    STRIPPED_JUNGLE_LOG = getBlockType("stripped_jungle_log")
    """
    BlockData: Orientable
    """
    STRIPPED_ACACIA_LOG = getBlockType("stripped_acacia_log")
    """
    BlockData: Orientable
    """
    STRIPPED_CHERRY_LOG = getBlockType("stripped_cherry_log")
    """
    BlockData: Orientable
    """
    STRIPPED_DARK_OAK_LOG = getBlockType("stripped_dark_oak_log")
    """
    BlockData: Orientable
    """
    STRIPPED_OAK_LOG = getBlockType("stripped_oak_log")
    """
    BlockData: Orientable
    """
    STRIPPED_MANGROVE_LOG = getBlockType("stripped_mangrove_log")
    """
    BlockData: Orientable
    """
    STRIPPED_BAMBOO_BLOCK = getBlockType("stripped_bamboo_block")
    """
    BlockData: Orientable
    """
    OAK_WOOD = getBlockType("oak_wood")
    """
    BlockData: Orientable
    """
    SPRUCE_WOOD = getBlockType("spruce_wood")
    """
    BlockData: Orientable
    """
    BIRCH_WOOD = getBlockType("birch_wood")
    """
    BlockData: Orientable
    """
    JUNGLE_WOOD = getBlockType("jungle_wood")
    """
    BlockData: Orientable
    """
    ACACIA_WOOD = getBlockType("acacia_wood")
    """
    BlockData: Orientable
    """
    CHERRY_WOOD = getBlockType("cherry_wood")
    """
    BlockData: Orientable
    """
    DARK_OAK_WOOD = getBlockType("dark_oak_wood")
    """
    BlockData: Orientable
    """
    MANGROVE_WOOD = getBlockType("mangrove_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_OAK_WOOD = getBlockType("stripped_oak_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_SPRUCE_WOOD = getBlockType("stripped_spruce_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_BIRCH_WOOD = getBlockType("stripped_birch_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_JUNGLE_WOOD = getBlockType("stripped_jungle_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_ACACIA_WOOD = getBlockType("stripped_acacia_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_CHERRY_WOOD = getBlockType("stripped_cherry_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_DARK_OAK_WOOD = getBlockType("stripped_dark_oak_wood")
    """
    BlockData: Orientable
    """
    STRIPPED_MANGROVE_WOOD = getBlockType("stripped_mangrove_wood")
    """
    BlockData: Orientable
    """
    OAK_LEAVES = getBlockType("oak_leaves")
    """
    BlockData: Leaves
    """
    SPRUCE_LEAVES = getBlockType("spruce_leaves")
    """
    BlockData: Leaves
    """
    BIRCH_LEAVES = getBlockType("birch_leaves")
    """
    BlockData: Leaves
    """
    JUNGLE_LEAVES = getBlockType("jungle_leaves")
    """
    BlockData: Leaves
    """
    ACACIA_LEAVES = getBlockType("acacia_leaves")
    """
    BlockData: Leaves
    """
    CHERRY_LEAVES = getBlockType("cherry_leaves")
    """
    BlockData: Leaves
    """
    DARK_OAK_LEAVES = getBlockType("dark_oak_leaves")
    """
    BlockData: Leaves
    """
    MANGROVE_LEAVES = getBlockType("mangrove_leaves")
    """
    BlockData: Leaves
    """
    AZALEA_LEAVES = getBlockType("azalea_leaves")
    """
    BlockData: Leaves
    """
    FLOWERING_AZALEA_LEAVES = getBlockType("flowering_azalea_leaves")
    """
    BlockData: Leaves
    """
    SPONGE = getBlockType("sponge")
    WET_SPONGE = getBlockType("wet_sponge")
    GLASS = getBlockType("glass")
    LAPIS_ORE = getBlockType("lapis_ore")
    DEEPSLATE_LAPIS_ORE = getBlockType("deepslate_lapis_ore")
    LAPIS_BLOCK = getBlockType("lapis_block")
    DISPENSER = getBlockType("dispenser")
    """
    BlockData: Dispenser
    """
    SANDSTONE = getBlockType("sandstone")
    CHISELED_SANDSTONE = getBlockType("chiseled_sandstone")
    CUT_SANDSTONE = getBlockType("cut_sandstone")
    NOTE_BLOCK = getBlockType("note_block")
    """
    BlockData: NoteBlock
    """
    WHITE_BED = getBlockType("white_bed")
    """
    BlockData: Bed
    """
    ORANGE_BED = getBlockType("orange_bed")
    """
    BlockData: Bed
    """
    MAGENTA_BED = getBlockType("magenta_bed")
    """
    BlockData: Bed
    """
    LIGHT_BLUE_BED = getBlockType("light_blue_bed")
    """
    BlockData: Bed
    """
    YELLOW_BED = getBlockType("yellow_bed")
    """
    BlockData: Bed
    """
    LIME_BED = getBlockType("lime_bed")
    """
    BlockData: Bed
    """
    PINK_BED = getBlockType("pink_bed")
    """
    BlockData: Bed
    """
    GRAY_BED = getBlockType("gray_bed")
    """
    BlockData: Bed
    """
    LIGHT_GRAY_BED = getBlockType("light_gray_bed")
    """
    BlockData: Bed
    """
    CYAN_BED = getBlockType("cyan_bed")
    """
    BlockData: Bed
    """
    PURPLE_BED = getBlockType("purple_bed")
    """
    BlockData: Bed
    """
    BLUE_BED = getBlockType("blue_bed")
    """
    BlockData: Bed
    """
    BROWN_BED = getBlockType("brown_bed")
    """
    BlockData: Bed
    """
    GREEN_BED = getBlockType("green_bed")
    """
    BlockData: Bed
    """
    RED_BED = getBlockType("red_bed")
    """
    BlockData: Bed
    """
    BLACK_BED = getBlockType("black_bed")
    """
    BlockData: Bed
    """
    POWERED_RAIL = getBlockType("powered_rail")
    """
    BlockData: RedstoneRail
    """
    DETECTOR_RAIL = getBlockType("detector_rail")
    """
    BlockData: RedstoneRail
    """
    STICKY_PISTON = getBlockType("sticky_piston")
    """
    BlockData: Piston
    """
    COBWEB = getBlockType("cobweb")
    SHORT_GRASS = getBlockType("short_grass")
    FERN = getBlockType("fern")
    DEAD_BUSH = getBlockType("dead_bush")
    SEAGRASS = getBlockType("seagrass")
    TALL_SEAGRASS = getBlockType("tall_seagrass")
    """
    BlockData: Bisected
    """
    PISTON = getBlockType("piston")
    """
    BlockData: Piston
    """
    PISTON_HEAD = getBlockType("piston_head")
    """
    BlockData: PistonHead
    """
    WHITE_WOOL = getBlockType("white_wool")
    ORANGE_WOOL = getBlockType("orange_wool")
    MAGENTA_WOOL = getBlockType("magenta_wool")
    LIGHT_BLUE_WOOL = getBlockType("light_blue_wool")
    YELLOW_WOOL = getBlockType("yellow_wool")
    LIME_WOOL = getBlockType("lime_wool")
    PINK_WOOL = getBlockType("pink_wool")
    GRAY_WOOL = getBlockType("gray_wool")
    LIGHT_GRAY_WOOL = getBlockType("light_gray_wool")
    CYAN_WOOL = getBlockType("cyan_wool")
    PURPLE_WOOL = getBlockType("purple_wool")
    BLUE_WOOL = getBlockType("blue_wool")
    BROWN_WOOL = getBlockType("brown_wool")
    GREEN_WOOL = getBlockType("green_wool")
    RED_WOOL = getBlockType("red_wool")
    BLACK_WOOL = getBlockType("black_wool")
    MOVING_PISTON = getBlockType("moving_piston")
    """
    BlockData: TechnicalPiston
    """
    DANDELION = getBlockType("dandelion")
    TORCHFLOWER = getBlockType("torchflower")
    POPPY = getBlockType("poppy")
    BLUE_ORCHID = getBlockType("blue_orchid")
    ALLIUM = getBlockType("allium")
    AZURE_BLUET = getBlockType("azure_bluet")
    RED_TULIP = getBlockType("red_tulip")
    ORANGE_TULIP = getBlockType("orange_tulip")
    WHITE_TULIP = getBlockType("white_tulip")
    PINK_TULIP = getBlockType("pink_tulip")
    OXEYE_DAISY = getBlockType("oxeye_daisy")
    CORNFLOWER = getBlockType("cornflower")
    WITHER_ROSE = getBlockType("wither_rose")
    LILY_OF_THE_VALLEY = getBlockType("lily_of_the_valley")
    BROWN_MUSHROOM = getBlockType("brown_mushroom")
    RED_MUSHROOM = getBlockType("red_mushroom")
    GOLD_BLOCK = getBlockType("gold_block")
    IRON_BLOCK = getBlockType("iron_block")
    BRICKS = getBlockType("bricks")
    TNT = getBlockType("tnt")
    """
    BlockData: TNT
    """
    BOOKSHELF = getBlockType("bookshelf")
    CHISELED_BOOKSHELF = getBlockType("chiseled_bookshelf")
    """
    BlockData: ChiseledBookshelf
    """
    MOSSY_COBBLESTONE = getBlockType("mossy_cobblestone")
    OBSIDIAN = getBlockType("obsidian")
    TORCH = getBlockType("torch")
    WALL_TORCH = getBlockType("wall_torch")
    """
    BlockData: Directional
    """
    FIRE = getBlockType("fire")
    """
    BlockData: Fire
    """
    SOUL_FIRE = getBlockType("soul_fire")
    SPAWNER = getBlockType("spawner")
    OAK_STAIRS = getBlockType("oak_stairs")
    """
    BlockData: Stairs
    """
    CHEST = getBlockType("chest")
    """
    BlockData: Chest
    """
    REDSTONE_WIRE = getBlockType("redstone_wire")
    """
    BlockData: RedstoneWire
    """
    DIAMOND_ORE = getBlockType("diamond_ore")
    DEEPSLATE_DIAMOND_ORE = getBlockType("deepslate_diamond_ore")
    DIAMOND_BLOCK = getBlockType("diamond_block")
    CRAFTING_TABLE = getBlockType("crafting_table")
    WHEAT = getBlockType("wheat")
    """
    BlockData: Ageable
    """
    FARMLAND = getBlockType("farmland")
    """
    BlockData: Farmland
    """
    FURNACE = getBlockType("furnace")
    """
    BlockData: Furnace
    """
    OAK_SIGN = getBlockType("oak_sign")
    """
    BlockData: Sign
    """
    SPRUCE_SIGN = getBlockType("spruce_sign")
    """
    BlockData: Sign
    """
    BIRCH_SIGN = getBlockType("birch_sign")
    """
    BlockData: Sign
    """
    ACACIA_SIGN = getBlockType("acacia_sign")
    """
    BlockData: Sign
    """
    CHERRY_SIGN = getBlockType("cherry_sign")
    """
    BlockData: Sign
    """
    JUNGLE_SIGN = getBlockType("jungle_sign")
    """
    BlockData: Sign
    """
    DARK_OAK_SIGN = getBlockType("dark_oak_sign")
    """
    BlockData: Sign
    """
    MANGROVE_SIGN = getBlockType("mangrove_sign")
    """
    BlockData: Sign
    """
    BAMBOO_SIGN = getBlockType("bamboo_sign")
    """
    BlockData: Sign
    """
    OAK_DOOR = getBlockType("oak_door")
    """
    BlockData: Door
    """
    LADDER = getBlockType("ladder")
    """
    BlockData: Ladder
    """
    RAIL = getBlockType("rail")
    """
    BlockData: Rail
    """
    COBBLESTONE_STAIRS = getBlockType("cobblestone_stairs")
    """
    BlockData: Stairs
    """
    OAK_WALL_SIGN = getBlockType("oak_wall_sign")
    """
    BlockData: WallSign
    """
    SPRUCE_WALL_SIGN = getBlockType("spruce_wall_sign")
    """
    BlockData: WallSign
    """
    BIRCH_WALL_SIGN = getBlockType("birch_wall_sign")
    """
    BlockData: WallSign
    """
    ACACIA_WALL_SIGN = getBlockType("acacia_wall_sign")
    """
    BlockData: WallSign
    """
    CHERRY_WALL_SIGN = getBlockType("cherry_wall_sign")
    """
    BlockData: WallSign
    """
    JUNGLE_WALL_SIGN = getBlockType("jungle_wall_sign")
    """
    BlockData: WallSign
    """
    DARK_OAK_WALL_SIGN = getBlockType("dark_oak_wall_sign")
    """
    BlockData: WallSign
    """
    MANGROVE_WALL_SIGN = getBlockType("mangrove_wall_sign")
    """
    BlockData: WallSign
    """
    BAMBOO_WALL_SIGN = getBlockType("bamboo_wall_sign")
    """
    BlockData: WallSign
    """
    OAK_HANGING_SIGN = getBlockType("oak_hanging_sign")
    """
    BlockData: HangingSign
    """
    SPRUCE_HANGING_SIGN = getBlockType("spruce_hanging_sign")
    """
    BlockData: HangingSign
    """
    BIRCH_HANGING_SIGN = getBlockType("birch_hanging_sign")
    """
    BlockData: HangingSign
    """
    ACACIA_HANGING_SIGN = getBlockType("acacia_hanging_sign")
    """
    BlockData: HangingSign
    """
    CHERRY_HANGING_SIGN = getBlockType("cherry_hanging_sign")
    """
    BlockData: HangingSign
    """
    JUNGLE_HANGING_SIGN = getBlockType("jungle_hanging_sign")
    """
    BlockData: HangingSign
    """
    DARK_OAK_HANGING_SIGN = getBlockType("dark_oak_hanging_sign")
    """
    BlockData: HangingSign
    """
    CRIMSON_HANGING_SIGN = getBlockType("crimson_hanging_sign")
    """
    BlockData: HangingSign
    """
    WARPED_HANGING_SIGN = getBlockType("warped_hanging_sign")
    """
    BlockData: HangingSign
    """
    MANGROVE_HANGING_SIGN = getBlockType("mangrove_hanging_sign")
    """
    BlockData: HangingSign
    """
    BAMBOO_HANGING_SIGN = getBlockType("bamboo_hanging_sign")
    """
    BlockData: HangingSign
    """
    OAK_WALL_HANGING_SIGN = getBlockType("oak_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    SPRUCE_WALL_HANGING_SIGN = getBlockType("spruce_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    BIRCH_WALL_HANGING_SIGN = getBlockType("birch_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    ACACIA_WALL_HANGING_SIGN = getBlockType("acacia_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    CHERRY_WALL_HANGING_SIGN = getBlockType("cherry_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    JUNGLE_WALL_HANGING_SIGN = getBlockType("jungle_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    DARK_OAK_WALL_HANGING_SIGN = getBlockType("dark_oak_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    MANGROVE_WALL_HANGING_SIGN = getBlockType("mangrove_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    CRIMSON_WALL_HANGING_SIGN = getBlockType("crimson_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    WARPED_WALL_HANGING_SIGN = getBlockType("warped_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    BAMBOO_WALL_HANGING_SIGN = getBlockType("bamboo_wall_hanging_sign")
    """
    BlockData: WallHangingSign
    """
    LEVER = getBlockType("lever")
    """
    BlockData: Switch
    """
    STONE_PRESSURE_PLATE = getBlockType("stone_pressure_plate")
    """
    BlockData: Powerable
    """
    IRON_DOOR = getBlockType("iron_door")
    """
    BlockData: Door
    """
    OAK_PRESSURE_PLATE = getBlockType("oak_pressure_plate")
    """
    BlockData: Powerable
    """
    SPRUCE_PRESSURE_PLATE = getBlockType("spruce_pressure_plate")
    """
    BlockData: Powerable
    """
    BIRCH_PRESSURE_PLATE = getBlockType("birch_pressure_plate")
    """
    BlockData: Powerable
    """
    JUNGLE_PRESSURE_PLATE = getBlockType("jungle_pressure_plate")
    """
    BlockData: Powerable
    """
    ACACIA_PRESSURE_PLATE = getBlockType("acacia_pressure_plate")
    """
    BlockData: Powerable
    """
    CHERRY_PRESSURE_PLATE = getBlockType("cherry_pressure_plate")
    """
    BlockData: Powerable
    """
    DARK_OAK_PRESSURE_PLATE = getBlockType("dark_oak_pressure_plate")
    """
    BlockData: Powerable
    """
    MANGROVE_PRESSURE_PLATE = getBlockType("mangrove_pressure_plate")
    """
    BlockData: Powerable
    """
    BAMBOO_PRESSURE_PLATE = getBlockType("bamboo_pressure_plate")
    """
    BlockData: Powerable
    """
    REDSTONE_ORE = getBlockType("redstone_ore")
    """
    BlockData: Lightable
    """
    DEEPSLATE_REDSTONE_ORE = getBlockType("deepslate_redstone_ore")
    """
    BlockData: Lightable
    """
    REDSTONE_TORCH = getBlockType("redstone_torch")
    """
    BlockData: Lightable
    """
    REDSTONE_WALL_TORCH = getBlockType("redstone_wall_torch")
    """
    BlockData: RedstoneWallTorch
    """
    STONE_BUTTON = getBlockType("stone_button")
    """
    BlockData: Switch
    """
    SNOW = getBlockType("snow")
    """
    BlockData: Snow
    """
    ICE = getBlockType("ice")
    SNOW_BLOCK = getBlockType("snow_block")
    CACTUS = getBlockType("cactus")
    """
    BlockData: Ageable
    """
    CLAY = getBlockType("clay")
    SUGAR_CANE = getBlockType("sugar_cane")
    """
    BlockData: Ageable
    """
    JUKEBOX = getBlockType("jukebox")
    """
    BlockData: Jukebox
    """
    OAK_FENCE = getBlockType("oak_fence")
    """
    BlockData: Fence
    """
    NETHERRACK = getBlockType("netherrack")
    SOUL_SAND = getBlockType("soul_sand")
    SOUL_SOIL = getBlockType("soul_soil")
    BASALT = getBlockType("basalt")
    """
    BlockData: Orientable
    """
    POLISHED_BASALT = getBlockType("polished_basalt")
    """
    BlockData: Orientable
    """
    SOUL_TORCH = getBlockType("soul_torch")
    SOUL_WALL_TORCH = getBlockType("soul_wall_torch")
    """
    BlockData: Directional
    """
    GLOWSTONE = getBlockType("glowstone")
    NETHER_PORTAL = getBlockType("nether_portal")
    """
    BlockData: Orientable
    """
    CARVED_PUMPKIN = getBlockType("carved_pumpkin")
    """
    BlockData: Directional
    """
    JACK_O_LANTERN = getBlockType("jack_o_lantern")
    """
    BlockData: Directional
    """
    CAKE = getBlockType("cake")
    """
    BlockData: Cake
    """
    REPEATER = getBlockType("repeater")
    """
    BlockData: Repeater
    """
    WHITE_STAINED_GLASS = getBlockType("white_stained_glass")
    ORANGE_STAINED_GLASS = getBlockType("orange_stained_glass")
    MAGENTA_STAINED_GLASS = getBlockType("magenta_stained_glass")
    LIGHT_BLUE_STAINED_GLASS = getBlockType("light_blue_stained_glass")
    YELLOW_STAINED_GLASS = getBlockType("yellow_stained_glass")
    LIME_STAINED_GLASS = getBlockType("lime_stained_glass")
    PINK_STAINED_GLASS = getBlockType("pink_stained_glass")
    GRAY_STAINED_GLASS = getBlockType("gray_stained_glass")
    LIGHT_GRAY_STAINED_GLASS = getBlockType("light_gray_stained_glass")
    CYAN_STAINED_GLASS = getBlockType("cyan_stained_glass")
    PURPLE_STAINED_GLASS = getBlockType("purple_stained_glass")
    BLUE_STAINED_GLASS = getBlockType("blue_stained_glass")
    BROWN_STAINED_GLASS = getBlockType("brown_stained_glass")
    GREEN_STAINED_GLASS = getBlockType("green_stained_glass")
    RED_STAINED_GLASS = getBlockType("red_stained_glass")
    BLACK_STAINED_GLASS = getBlockType("black_stained_glass")
    OAK_TRAPDOOR = getBlockType("oak_trapdoor")
    """
    BlockData: TrapDoor
    """
    SPRUCE_TRAPDOOR = getBlockType("spruce_trapdoor")
    """
    BlockData: TrapDoor
    """
    BIRCH_TRAPDOOR = getBlockType("birch_trapdoor")
    """
    BlockData: TrapDoor
    """
    JUNGLE_TRAPDOOR = getBlockType("jungle_trapdoor")
    """
    BlockData: TrapDoor
    """
    ACACIA_TRAPDOOR = getBlockType("acacia_trapdoor")
    """
    BlockData: TrapDoor
    """
    CHERRY_TRAPDOOR = getBlockType("cherry_trapdoor")
    """
    BlockData: TrapDoor
    """
    DARK_OAK_TRAPDOOR = getBlockType("dark_oak_trapdoor")
    """
    BlockData: TrapDoor
    """
    MANGROVE_TRAPDOOR = getBlockType("mangrove_trapdoor")
    """
    BlockData: TrapDoor
    """
    BAMBOO_TRAPDOOR = getBlockType("bamboo_trapdoor")
    """
    BlockData: TrapDoor
    """
    STONE_BRICKS = getBlockType("stone_bricks")
    MOSSY_STONE_BRICKS = getBlockType("mossy_stone_bricks")
    CRACKED_STONE_BRICKS = getBlockType("cracked_stone_bricks")
    CHISELED_STONE_BRICKS = getBlockType("chiseled_stone_bricks")
    PACKED_MUD = getBlockType("packed_mud")
    MUD_BRICKS = getBlockType("mud_bricks")
    INFESTED_STONE = getBlockType("infested_stone")
    INFESTED_COBBLESTONE = getBlockType("infested_cobblestone")
    INFESTED_STONE_BRICKS = getBlockType("infested_stone_bricks")
    INFESTED_MOSSY_STONE_BRICKS = getBlockType("infested_mossy_stone_bricks")
    INFESTED_CRACKED_STONE_BRICKS = getBlockType("infested_cracked_stone_bricks")
    INFESTED_CHISELED_STONE_BRICKS = getBlockType("infested_chiseled_stone_bricks")
    BROWN_MUSHROOM_BLOCK = getBlockType("brown_mushroom_block")
    """
    BlockData: MultipleFacing
    """
    RED_MUSHROOM_BLOCK = getBlockType("red_mushroom_block")
    """
    BlockData: MultipleFacing
    """
    MUSHROOM_STEM = getBlockType("mushroom_stem")
    """
    BlockData: MultipleFacing
    """
    IRON_BARS = getBlockType("iron_bars")
    """
    BlockData: Fence
    """
    CHAIN = getBlockType("chain")
    """
    BlockData: Chain
    """
    GLASS_PANE = getBlockType("glass_pane")
    """
    BlockData: Fence
    """
    PUMPKIN = getBlockType("pumpkin")
    MELON = getBlockType("melon")
    ATTACHED_PUMPKIN_STEM = getBlockType("attached_pumpkin_stem")
    """
    BlockData: Directional
    """
    ATTACHED_MELON_STEM = getBlockType("attached_melon_stem")
    """
    BlockData: Directional
    """
    PUMPKIN_STEM = getBlockType("pumpkin_stem")
    """
    BlockData: Ageable
    """
    MELON_STEM = getBlockType("melon_stem")
    """
    BlockData: Ageable
    """
    VINE = getBlockType("vine")
    """
    BlockData: MultipleFacing
    """
    GLOW_LICHEN = getBlockType("glow_lichen")
    """
    BlockData: GlowLichen
    """
    OAK_FENCE_GATE = getBlockType("oak_fence_gate")
    """
    BlockData: Gate
    """
    BRICK_STAIRS = getBlockType("brick_stairs")
    """
    BlockData: Stairs
    """
    STONE_BRICK_STAIRS = getBlockType("stone_brick_stairs")
    """
    BlockData: Stairs
    """
    MUD_BRICK_STAIRS = getBlockType("mud_brick_stairs")
    """
    BlockData: Stairs
    """
    MYCELIUM = getBlockType("mycelium")
    """
    BlockData: Snowable
    """
    LILY_PAD = getBlockType("lily_pad")
    NETHER_BRICKS = getBlockType("nether_bricks")
    NETHER_BRICK_FENCE = getBlockType("nether_brick_fence")
    """
    BlockData: Fence
    """
    NETHER_BRICK_STAIRS = getBlockType("nether_brick_stairs")
    """
    BlockData: Stairs
    """
    NETHER_WART = getBlockType("nether_wart")
    """
    BlockData: Ageable
    """
    ENCHANTING_TABLE = getBlockType("enchanting_table")
    BREWING_STAND = getBlockType("brewing_stand")
    """
    BlockData: BrewingStand
    """
    CAULDRON = getBlockType("cauldron")
    WATER_CAULDRON = getBlockType("water_cauldron")
    """
    BlockData: Levelled
    """
    LAVA_CAULDRON = getBlockType("lava_cauldron")
    POWDER_SNOW_CAULDRON = getBlockType("powder_snow_cauldron")
    """
    BlockData: Levelled
    """
    END_PORTAL = getBlockType("end_portal")
    END_PORTAL_FRAME = getBlockType("end_portal_frame")
    """
    BlockData: EndPortalFrame
    """
    END_STONE = getBlockType("end_stone")
    DRAGON_EGG = getBlockType("dragon_egg")
    REDSTONE_LAMP = getBlockType("redstone_lamp")
    """
    BlockData: Lightable
    """
    COCOA = getBlockType("cocoa")
    """
    BlockData: Cocoa
    """
    SANDSTONE_STAIRS = getBlockType("sandstone_stairs")
    """
    BlockData: Stairs
    """
    EMERALD_ORE = getBlockType("emerald_ore")
    DEEPSLATE_EMERALD_ORE = getBlockType("deepslate_emerald_ore")
    ENDER_CHEST = getBlockType("ender_chest")
    """
    BlockData: EnderChest
    """
    TRIPWIRE_HOOK = getBlockType("tripwire_hook")
    """
    BlockData: TripwireHook
    """
    TRIPWIRE = getBlockType("tripwire")
    """
    BlockData: Tripwire
    """
    EMERALD_BLOCK = getBlockType("emerald_block")
    SPRUCE_STAIRS = getBlockType("spruce_stairs")
    """
    BlockData: Stairs
    """
    BIRCH_STAIRS = getBlockType("birch_stairs")
    """
    BlockData: Stairs
    """
    JUNGLE_STAIRS = getBlockType("jungle_stairs")
    """
    BlockData: Stairs
    """
    COMMAND_BLOCK = getBlockType("command_block")
    """
    BlockData: CommandBlock
    """
    BEACON = getBlockType("beacon")
    COBBLESTONE_WALL = getBlockType("cobblestone_wall")
    """
    BlockData: Wall
    """
    MOSSY_COBBLESTONE_WALL = getBlockType("mossy_cobblestone_wall")
    """
    BlockData: Wall
    """
    FLOWER_POT = getBlockType("flower_pot")
    POTTED_TORCHFLOWER = getBlockType("potted_torchflower")
    POTTED_OAK_SAPLING = getBlockType("potted_oak_sapling")
    POTTED_SPRUCE_SAPLING = getBlockType("potted_spruce_sapling")
    POTTED_BIRCH_SAPLING = getBlockType("potted_birch_sapling")
    POTTED_JUNGLE_SAPLING = getBlockType("potted_jungle_sapling")
    POTTED_ACACIA_SAPLING = getBlockType("potted_acacia_sapling")
    POTTED_CHERRY_SAPLING = getBlockType("potted_cherry_sapling")
    POTTED_DARK_OAK_SAPLING = getBlockType("potted_dark_oak_sapling")
    POTTED_MANGROVE_PROPAGULE = getBlockType("potted_mangrove_propagule")
    POTTED_FERN = getBlockType("potted_fern")
    POTTED_DANDELION = getBlockType("potted_dandelion")
    POTTED_POPPY = getBlockType("potted_poppy")
    POTTED_BLUE_ORCHID = getBlockType("potted_blue_orchid")
    POTTED_ALLIUM = getBlockType("potted_allium")
    POTTED_AZURE_BLUET = getBlockType("potted_azure_bluet")
    POTTED_RED_TULIP = getBlockType("potted_red_tulip")
    POTTED_ORANGE_TULIP = getBlockType("potted_orange_tulip")
    POTTED_WHITE_TULIP = getBlockType("potted_white_tulip")
    POTTED_PINK_TULIP = getBlockType("potted_pink_tulip")
    POTTED_OXEYE_DAISY = getBlockType("potted_oxeye_daisy")
    POTTED_CORNFLOWER = getBlockType("potted_cornflower")
    POTTED_LILY_OF_THE_VALLEY = getBlockType("potted_lily_of_the_valley")
    POTTED_WITHER_ROSE = getBlockType("potted_wither_rose")
    POTTED_RED_MUSHROOM = getBlockType("potted_red_mushroom")
    POTTED_BROWN_MUSHROOM = getBlockType("potted_brown_mushroom")
    POTTED_DEAD_BUSH = getBlockType("potted_dead_bush")
    POTTED_CACTUS = getBlockType("potted_cactus")
    CARROTS = getBlockType("carrots")
    """
    BlockData: Ageable
    """
    POTATOES = getBlockType("potatoes")
    """
    BlockData: Ageable
    """
    OAK_BUTTON = getBlockType("oak_button")
    """
    BlockData: Switch
    """
    SPRUCE_BUTTON = getBlockType("spruce_button")
    """
    BlockData: Switch
    """
    BIRCH_BUTTON = getBlockType("birch_button")
    """
    BlockData: Switch
    """
    JUNGLE_BUTTON = getBlockType("jungle_button")
    """
    BlockData: Switch
    """
    ACACIA_BUTTON = getBlockType("acacia_button")
    """
    BlockData: Switch
    """
    CHERRY_BUTTON = getBlockType("cherry_button")
    """
    BlockData: Switch
    """
    DARK_OAK_BUTTON = getBlockType("dark_oak_button")
    """
    BlockData: Switch
    """
    MANGROVE_BUTTON = getBlockType("mangrove_button")
    """
    BlockData: Switch
    """
    BAMBOO_BUTTON = getBlockType("bamboo_button")
    """
    BlockData: Switch
    """
    SKELETON_SKULL = getBlockType("skeleton_skull")
    """
    BlockData: Rotatable
    """
    SKELETON_WALL_SKULL = getBlockType("skeleton_wall_skull")
    """
    BlockData: Directional
    """
    WITHER_SKELETON_SKULL = getBlockType("wither_skeleton_skull")
    """
    BlockData: Rotatable
    """
    WITHER_SKELETON_WALL_SKULL = getBlockType("wither_skeleton_wall_skull")
    """
    BlockData: Directional
    """
    ZOMBIE_HEAD = getBlockType("zombie_head")
    """
    BlockData: Rotatable
    """
    ZOMBIE_WALL_HEAD = getBlockType("zombie_wall_head")
    """
    BlockData: Directional
    """
    PLAYER_HEAD = getBlockType("player_head")
    """
    BlockData: Rotatable
    """
    PLAYER_WALL_HEAD = getBlockType("player_wall_head")
    """
    BlockData: Directional
    """
    CREEPER_HEAD = getBlockType("creeper_head")
    """
    BlockData: Rotatable
    """
    CREEPER_WALL_HEAD = getBlockType("creeper_wall_head")
    """
    BlockData: Directional
    """
    DRAGON_HEAD = getBlockType("dragon_head")
    """
    BlockData: Rotatable
    """
    DRAGON_WALL_HEAD = getBlockType("dragon_wall_head")
    """
    BlockData: Directional
    """
    PIGLIN_HEAD = getBlockType("piglin_head")
    """
    BlockData: Rotatable
    """
    PIGLIN_WALL_HEAD = getBlockType("piglin_wall_head")
    """
    BlockData: Directional
    """
    ANVIL = getBlockType("anvil")
    """
    BlockData: Directional
    """
    CHIPPED_ANVIL = getBlockType("chipped_anvil")
    """
    BlockData: Directional
    """
    DAMAGED_ANVIL = getBlockType("damaged_anvil")
    """
    BlockData: Directional
    """
    TRAPPED_CHEST = getBlockType("trapped_chest")
    """
    BlockData: Chest
    """
    LIGHT_WEIGHTED_PRESSURE_PLATE = getBlockType("light_weighted_pressure_plate")
    """
    BlockData: AnaloguePowerable
    """
    HEAVY_WEIGHTED_PRESSURE_PLATE = getBlockType("heavy_weighted_pressure_plate")
    """
    BlockData: AnaloguePowerable
    """
    COMPARATOR = getBlockType("comparator")
    """
    BlockData: Comparator
    """
    DAYLIGHT_DETECTOR = getBlockType("daylight_detector")
    """
    BlockData: DaylightDetector
    """
    REDSTONE_BLOCK = getBlockType("redstone_block")
    NETHER_QUARTZ_ORE = getBlockType("nether_quartz_ore")
    HOPPER = getBlockType("hopper")
    """
    BlockData: Hopper
    """
    QUARTZ_BLOCK = getBlockType("quartz_block")
    CHISELED_QUARTZ_BLOCK = getBlockType("chiseled_quartz_block")
    QUARTZ_PILLAR = getBlockType("quartz_pillar")
    """
    BlockData: Orientable
    """
    QUARTZ_STAIRS = getBlockType("quartz_stairs")
    """
    BlockData: Stairs
    """
    ACTIVATOR_RAIL = getBlockType("activator_rail")
    """
    BlockData: RedstoneRail
    """
    DROPPER = getBlockType("dropper")
    """
    BlockData: Dispenser
    """
    WHITE_TERRACOTTA = getBlockType("white_terracotta")
    ORANGE_TERRACOTTA = getBlockType("orange_terracotta")
    MAGENTA_TERRACOTTA = getBlockType("magenta_terracotta")
    LIGHT_BLUE_TERRACOTTA = getBlockType("light_blue_terracotta")
    YELLOW_TERRACOTTA = getBlockType("yellow_terracotta")
    LIME_TERRACOTTA = getBlockType("lime_terracotta")
    PINK_TERRACOTTA = getBlockType("pink_terracotta")
    GRAY_TERRACOTTA = getBlockType("gray_terracotta")
    LIGHT_GRAY_TERRACOTTA = getBlockType("light_gray_terracotta")
    CYAN_TERRACOTTA = getBlockType("cyan_terracotta")
    PURPLE_TERRACOTTA = getBlockType("purple_terracotta")
    BLUE_TERRACOTTA = getBlockType("blue_terracotta")
    BROWN_TERRACOTTA = getBlockType("brown_terracotta")
    GREEN_TERRACOTTA = getBlockType("green_terracotta")
    RED_TERRACOTTA = getBlockType("red_terracotta")
    BLACK_TERRACOTTA = getBlockType("black_terracotta")
    WHITE_STAINED_GLASS_PANE = getBlockType("white_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    ORANGE_STAINED_GLASS_PANE = getBlockType("orange_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    MAGENTA_STAINED_GLASS_PANE = getBlockType("magenta_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    LIGHT_BLUE_STAINED_GLASS_PANE = getBlockType("light_blue_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    YELLOW_STAINED_GLASS_PANE = getBlockType("yellow_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    LIME_STAINED_GLASS_PANE = getBlockType("lime_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    PINK_STAINED_GLASS_PANE = getBlockType("pink_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    GRAY_STAINED_GLASS_PANE = getBlockType("gray_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    LIGHT_GRAY_STAINED_GLASS_PANE = getBlockType("light_gray_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    CYAN_STAINED_GLASS_PANE = getBlockType("cyan_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    PURPLE_STAINED_GLASS_PANE = getBlockType("purple_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    BLUE_STAINED_GLASS_PANE = getBlockType("blue_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    BROWN_STAINED_GLASS_PANE = getBlockType("brown_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    GREEN_STAINED_GLASS_PANE = getBlockType("green_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    RED_STAINED_GLASS_PANE = getBlockType("red_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    BLACK_STAINED_GLASS_PANE = getBlockType("black_stained_glass_pane")
    """
    BlockData: GlassPane
    """
    ACACIA_STAIRS = getBlockType("acacia_stairs")
    """
    BlockData: Stairs
    """
    CHERRY_STAIRS = getBlockType("cherry_stairs")
    """
    BlockData: Stairs
    """
    DARK_OAK_STAIRS = getBlockType("dark_oak_stairs")
    """
    BlockData: Stairs
    """
    MANGROVE_STAIRS = getBlockType("mangrove_stairs")
    """
    BlockData: Stairs
    """
    BAMBOO_STAIRS = getBlockType("bamboo_stairs")
    """
    BlockData: Stairs
    """
    BAMBOO_MOSAIC_STAIRS = getBlockType("bamboo_mosaic_stairs")
    """
    BlockData: Stairs
    """
    SLIME_BLOCK = getBlockType("slime_block")
    BARRIER = getBlockType("barrier")
    """
    BlockData: Waterlogged
    """
    LIGHT = getBlockType("light")
    """
    BlockData: Light
    """
    IRON_TRAPDOOR = getBlockType("iron_trapdoor")
    """
    BlockData: TrapDoor
    """
    PRISMARINE = getBlockType("prismarine")
    PRISMARINE_BRICKS = getBlockType("prismarine_bricks")
    DARK_PRISMARINE = getBlockType("dark_prismarine")
    PRISMARINE_STAIRS = getBlockType("prismarine_stairs")
    """
    BlockData: Stairs
    """
    PRISMARINE_BRICK_STAIRS = getBlockType("prismarine_brick_stairs")
    """
    BlockData: Stairs
    """
    DARK_PRISMARINE_STAIRS = getBlockType("dark_prismarine_stairs")
    """
    BlockData: Stairs
    """
    PRISMARINE_SLAB = getBlockType("prismarine_slab")
    """
    BlockData: Slab
    """
    PRISMARINE_BRICK_SLAB = getBlockType("prismarine_brick_slab")
    """
    BlockData: Slab
    """
    DARK_PRISMARINE_SLAB = getBlockType("dark_prismarine_slab")
    """
    BlockData: Slab
    """
    SEA_LANTERN = getBlockType("sea_lantern")
    HAY_BLOCK = getBlockType("hay_block")
    """
    BlockData: Orientable
    """
    WHITE_CARPET = getBlockType("white_carpet")
    ORANGE_CARPET = getBlockType("orange_carpet")
    MAGENTA_CARPET = getBlockType("magenta_carpet")
    LIGHT_BLUE_CARPET = getBlockType("light_blue_carpet")
    YELLOW_CARPET = getBlockType("yellow_carpet")
    LIME_CARPET = getBlockType("lime_carpet")
    PINK_CARPET = getBlockType("pink_carpet")
    GRAY_CARPET = getBlockType("gray_carpet")
    LIGHT_GRAY_CARPET = getBlockType("light_gray_carpet")
    CYAN_CARPET = getBlockType("cyan_carpet")
    PURPLE_CARPET = getBlockType("purple_carpet")
    BLUE_CARPET = getBlockType("blue_carpet")
    BROWN_CARPET = getBlockType("brown_carpet")
    GREEN_CARPET = getBlockType("green_carpet")
    RED_CARPET = getBlockType("red_carpet")
    BLACK_CARPET = getBlockType("black_carpet")
    TERRACOTTA = getBlockType("terracotta")
    COAL_BLOCK = getBlockType("coal_block")
    PACKED_ICE = getBlockType("packed_ice")
    SUNFLOWER = getBlockType("sunflower")
    """
    BlockData: Bisected
    """
    LILAC = getBlockType("lilac")
    """
    BlockData: Bisected
    """
    ROSE_BUSH = getBlockType("rose_bush")
    """
    BlockData: Bisected
    """
    PEONY = getBlockType("peony")
    """
    BlockData: Bisected
    """
    TALL_GRASS = getBlockType("tall_grass")
    """
    BlockData: Bisected
    """
    LARGE_FERN = getBlockType("large_fern")
    """
    BlockData: Bisected
    """
    WHITE_BANNER = getBlockType("white_banner")
    """
    BlockData: Rotatable
    """
    ORANGE_BANNER = getBlockType("orange_banner")
    """
    BlockData: Rotatable
    """
    MAGENTA_BANNER = getBlockType("magenta_banner")
    """
    BlockData: Rotatable
    """
    LIGHT_BLUE_BANNER = getBlockType("light_blue_banner")
    """
    BlockData: Rotatable
    """
    YELLOW_BANNER = getBlockType("yellow_banner")
    """
    BlockData: Rotatable
    """
    LIME_BANNER = getBlockType("lime_banner")
    """
    BlockData: Rotatable
    """
    PINK_BANNER = getBlockType("pink_banner")
    """
    BlockData: Rotatable
    """
    GRAY_BANNER = getBlockType("gray_banner")
    """
    BlockData: Rotatable
    """
    LIGHT_GRAY_BANNER = getBlockType("light_gray_banner")
    """
    BlockData: Rotatable
    """
    CYAN_BANNER = getBlockType("cyan_banner")
    """
    BlockData: Rotatable
    """
    PURPLE_BANNER = getBlockType("purple_banner")
    """
    BlockData: Rotatable
    """
    BLUE_BANNER = getBlockType("blue_banner")
    """
    BlockData: Rotatable
    """
    BROWN_BANNER = getBlockType("brown_banner")
    """
    BlockData: Rotatable
    """
    GREEN_BANNER = getBlockType("green_banner")
    """
    BlockData: Rotatable
    """
    RED_BANNER = getBlockType("red_banner")
    """
    BlockData: Rotatable
    """
    BLACK_BANNER = getBlockType("black_banner")
    """
    BlockData: Rotatable
    """
    WHITE_WALL_BANNER = getBlockType("white_wall_banner")
    """
    BlockData: Directional
    """
    ORANGE_WALL_BANNER = getBlockType("orange_wall_banner")
    """
    BlockData: Directional
    """
    MAGENTA_WALL_BANNER = getBlockType("magenta_wall_banner")
    """
    BlockData: Directional
    """
    LIGHT_BLUE_WALL_BANNER = getBlockType("light_blue_wall_banner")
    """
    BlockData: Directional
    """
    YELLOW_WALL_BANNER = getBlockType("yellow_wall_banner")
    """
    BlockData: Directional
    """
    LIME_WALL_BANNER = getBlockType("lime_wall_banner")
    """
    BlockData: Directional
    """
    PINK_WALL_BANNER = getBlockType("pink_wall_banner")
    """
    BlockData: Directional
    """
    GRAY_WALL_BANNER = getBlockType("gray_wall_banner")
    """
    BlockData: Directional
    """
    LIGHT_GRAY_WALL_BANNER = getBlockType("light_gray_wall_banner")
    """
    BlockData: Directional
    """
    CYAN_WALL_BANNER = getBlockType("cyan_wall_banner")
    """
    BlockData: Directional
    """
    PURPLE_WALL_BANNER = getBlockType("purple_wall_banner")
    """
    BlockData: Directional
    """
    BLUE_WALL_BANNER = getBlockType("blue_wall_banner")
    """
    BlockData: Directional
    """
    BROWN_WALL_BANNER = getBlockType("brown_wall_banner")
    """
    BlockData: Directional
    """
    GREEN_WALL_BANNER = getBlockType("green_wall_banner")
    """
    BlockData: Directional
    """
    RED_WALL_BANNER = getBlockType("red_wall_banner")
    """
    BlockData: Directional
    """
    BLACK_WALL_BANNER = getBlockType("black_wall_banner")
    """
    BlockData: Directional
    """
    RED_SANDSTONE = getBlockType("red_sandstone")
    CHISELED_RED_SANDSTONE = getBlockType("chiseled_red_sandstone")
    CUT_RED_SANDSTONE = getBlockType("cut_red_sandstone")
    RED_SANDSTONE_STAIRS = getBlockType("red_sandstone_stairs")
    """
    BlockData: Stairs
    """
    OAK_SLAB = getBlockType("oak_slab")
    """
    BlockData: Slab
    """
    SPRUCE_SLAB = getBlockType("spruce_slab")
    """
    BlockData: Slab
    """
    BIRCH_SLAB = getBlockType("birch_slab")
    """
    BlockData: Slab
    """
    JUNGLE_SLAB = getBlockType("jungle_slab")
    """
    BlockData: Slab
    """
    ACACIA_SLAB = getBlockType("acacia_slab")
    """
    BlockData: Slab
    """
    CHERRY_SLAB = getBlockType("cherry_slab")
    """
    BlockData: Slab
    """
    DARK_OAK_SLAB = getBlockType("dark_oak_slab")
    """
    BlockData: Slab
    """
    MANGROVE_SLAB = getBlockType("mangrove_slab")
    """
    BlockData: Slab
    """
    BAMBOO_SLAB = getBlockType("bamboo_slab")
    """
    BlockData: Slab
    """
    BAMBOO_MOSAIC_SLAB = getBlockType("bamboo_mosaic_slab")
    """
    BlockData: Slab
    """
    STONE_SLAB = getBlockType("stone_slab")
    """
    BlockData: Slab
    """
    SMOOTH_STONE_SLAB = getBlockType("smooth_stone_slab")
    """
    BlockData: Slab
    """
    SANDSTONE_SLAB = getBlockType("sandstone_slab")
    """
    BlockData: Slab
    """
    CUT_SANDSTONE_SLAB = getBlockType("cut_sandstone_slab")
    """
    BlockData: Slab
    """
    PETRIFIED_OAK_SLAB = getBlockType("petrified_oak_slab")
    """
    BlockData: Slab
    """
    COBBLESTONE_SLAB = getBlockType("cobblestone_slab")
    """
    BlockData: Slab
    """
    BRICK_SLAB = getBlockType("brick_slab")
    """
    BlockData: Slab
    """
    STONE_BRICK_SLAB = getBlockType("stone_brick_slab")
    """
    BlockData: Slab
    """
    MUD_BRICK_SLAB = getBlockType("mud_brick_slab")
    """
    BlockData: Slab
    """
    NETHER_BRICK_SLAB = getBlockType("nether_brick_slab")
    """
    BlockData: Slab
    """
    QUARTZ_SLAB = getBlockType("quartz_slab")
    """
    BlockData: Slab
    """
    RED_SANDSTONE_SLAB = getBlockType("red_sandstone_slab")
    """
    BlockData: Slab
    """
    CUT_RED_SANDSTONE_SLAB = getBlockType("cut_red_sandstone_slab")
    """
    BlockData: Slab
    """
    PURPUR_SLAB = getBlockType("purpur_slab")
    """
    BlockData: Slab
    """
    SMOOTH_STONE = getBlockType("smooth_stone")
    SMOOTH_SANDSTONE = getBlockType("smooth_sandstone")
    SMOOTH_QUARTZ = getBlockType("smooth_quartz")
    SMOOTH_RED_SANDSTONE = getBlockType("smooth_red_sandstone")
    SPRUCE_FENCE_GATE = getBlockType("spruce_fence_gate")
    """
    BlockData: Gate
    """
    BIRCH_FENCE_GATE = getBlockType("birch_fence_gate")
    """
    BlockData: Gate
    """
    JUNGLE_FENCE_GATE = getBlockType("jungle_fence_gate")
    """
    BlockData: Gate
    """
    ACACIA_FENCE_GATE = getBlockType("acacia_fence_gate")
    """
    BlockData: Gate
    """
    CHERRY_FENCE_GATE = getBlockType("cherry_fence_gate")
    """
    BlockData: Gate
    """
    DARK_OAK_FENCE_GATE = getBlockType("dark_oak_fence_gate")
    """
    BlockData: Gate
    """
    MANGROVE_FENCE_GATE = getBlockType("mangrove_fence_gate")
    """
    BlockData: Gate
    """
    BAMBOO_FENCE_GATE = getBlockType("bamboo_fence_gate")
    """
    BlockData: Gate
    """
    SPRUCE_FENCE = getBlockType("spruce_fence")
    """
    BlockData: Fence
    """
    BIRCH_FENCE = getBlockType("birch_fence")
    """
    BlockData: Fence
    """
    JUNGLE_FENCE = getBlockType("jungle_fence")
    """
    BlockData: Fence
    """
    ACACIA_FENCE = getBlockType("acacia_fence")
    """
    BlockData: Fence
    """
    CHERRY_FENCE = getBlockType("cherry_fence")
    """
    BlockData: Fence
    """
    DARK_OAK_FENCE = getBlockType("dark_oak_fence")
    """
    BlockData: Fence
    """
    MANGROVE_FENCE = getBlockType("mangrove_fence")
    """
    BlockData: Fence
    """
    BAMBOO_FENCE = getBlockType("bamboo_fence")
    """
    BlockData: Fence
    """
    SPRUCE_DOOR = getBlockType("spruce_door")
    """
    BlockData: Door
    """
    BIRCH_DOOR = getBlockType("birch_door")
    """
    BlockData: Door
    """
    JUNGLE_DOOR = getBlockType("jungle_door")
    """
    BlockData: Door
    """
    ACACIA_DOOR = getBlockType("acacia_door")
    """
    BlockData: Door
    """
    CHERRY_DOOR = getBlockType("cherry_door")
    """
    BlockData: Door
    """
    DARK_OAK_DOOR = getBlockType("dark_oak_door")
    """
    BlockData: Door
    """
    MANGROVE_DOOR = getBlockType("mangrove_door")
    """
    BlockData: Door
    """
    BAMBOO_DOOR = getBlockType("bamboo_door")
    """
    BlockData: Door
    """
    END_ROD = getBlockType("end_rod")
    """
    BlockData: Directional
    """
    CHORUS_PLANT = getBlockType("chorus_plant")
    """
    BlockData: MultipleFacing
    """
    CHORUS_FLOWER = getBlockType("chorus_flower")
    """
    BlockData: Ageable
    """
    PURPUR_BLOCK = getBlockType("purpur_block")
    PURPUR_PILLAR = getBlockType("purpur_pillar")
    """
    BlockData: Orientable
    """
    PURPUR_STAIRS = getBlockType("purpur_stairs")
    """
    BlockData: Stairs
    """
    END_STONE_BRICKS = getBlockType("end_stone_bricks")
    TORCHFLOWER_CROP = getBlockType("torchflower_crop")
    """
    BlockData: Ageable
    """
    PITCHER_CROP = getBlockType("pitcher_crop")
    """
    BlockData: PitcherCrop
    """
    PITCHER_PLANT = getBlockType("pitcher_plant")
    """
    BlockData: Bisected
    """
    BEETROOTS = getBlockType("beetroots")
    """
    BlockData: Ageable
    """
    DIRT_PATH = getBlockType("dirt_path")
    END_GATEWAY = getBlockType("end_gateway")
    REPEATING_COMMAND_BLOCK = getBlockType("repeating_command_block")
    """
    BlockData: CommandBlock
    """
    CHAIN_COMMAND_BLOCK = getBlockType("chain_command_block")
    """
    BlockData: CommandBlock
    """
    FROSTED_ICE = getBlockType("frosted_ice")
    """
    BlockData: Ageable
    """
    MAGMA_BLOCK = getBlockType("magma_block")
    NETHER_WART_BLOCK = getBlockType("nether_wart_block")
    RED_NETHER_BRICKS = getBlockType("red_nether_bricks")
    BONE_BLOCK = getBlockType("bone_block")
    """
    BlockData: Orientable
    """
    STRUCTURE_VOID = getBlockType("structure_void")
    OBSERVER = getBlockType("observer")
    """
    BlockData: Observer
    """
    SHULKER_BOX = getBlockType("shulker_box")
    """
    BlockData: Directional
    """
    WHITE_SHULKER_BOX = getBlockType("white_shulker_box")
    """
    BlockData: Directional
    """
    ORANGE_SHULKER_BOX = getBlockType("orange_shulker_box")
    """
    BlockData: Directional
    """
    MAGENTA_SHULKER_BOX = getBlockType("magenta_shulker_box")
    """
    BlockData: Directional
    """
    LIGHT_BLUE_SHULKER_BOX = getBlockType("light_blue_shulker_box")
    """
    BlockData: Directional
    """
    YELLOW_SHULKER_BOX = getBlockType("yellow_shulker_box")
    """
    BlockData: Directional
    """
    LIME_SHULKER_BOX = getBlockType("lime_shulker_box")
    """
    BlockData: Directional
    """
    PINK_SHULKER_BOX = getBlockType("pink_shulker_box")
    """
    BlockData: Directional
    """
    GRAY_SHULKER_BOX = getBlockType("gray_shulker_box")
    """
    BlockData: Directional
    """
    LIGHT_GRAY_SHULKER_BOX = getBlockType("light_gray_shulker_box")
    """
    BlockData: Directional
    """
    CYAN_SHULKER_BOX = getBlockType("cyan_shulker_box")
    """
    BlockData: Directional
    """
    PURPLE_SHULKER_BOX = getBlockType("purple_shulker_box")
    """
    BlockData: Directional
    """
    BLUE_SHULKER_BOX = getBlockType("blue_shulker_box")
    """
    BlockData: Directional
    """
    BROWN_SHULKER_BOX = getBlockType("brown_shulker_box")
    """
    BlockData: Directional
    """
    GREEN_SHULKER_BOX = getBlockType("green_shulker_box")
    """
    BlockData: Directional
    """
    RED_SHULKER_BOX = getBlockType("red_shulker_box")
    """
    BlockData: Directional
    """
    BLACK_SHULKER_BOX = getBlockType("black_shulker_box")
    """
    BlockData: Directional
    """
    WHITE_GLAZED_TERRACOTTA = getBlockType("white_glazed_terracotta")
    """
    BlockData: Directional
    """
    ORANGE_GLAZED_TERRACOTTA = getBlockType("orange_glazed_terracotta")
    """
    BlockData: Directional
    """
    MAGENTA_GLAZED_TERRACOTTA = getBlockType("magenta_glazed_terracotta")
    """
    BlockData: Directional
    """
    LIGHT_BLUE_GLAZED_TERRACOTTA = getBlockType("light_blue_glazed_terracotta")
    """
    BlockData: Directional
    """
    YELLOW_GLAZED_TERRACOTTA = getBlockType("yellow_glazed_terracotta")
    """
    BlockData: Directional
    """
    LIME_GLAZED_TERRACOTTA = getBlockType("lime_glazed_terracotta")
    """
    BlockData: Directional
    """
    PINK_GLAZED_TERRACOTTA = getBlockType("pink_glazed_terracotta")
    """
    BlockData: Directional
    """
    GRAY_GLAZED_TERRACOTTA = getBlockType("gray_glazed_terracotta")
    """
    BlockData: Directional
    """
    LIGHT_GRAY_GLAZED_TERRACOTTA = getBlockType("light_gray_glazed_terracotta")
    """
    BlockData: Directional
    """
    CYAN_GLAZED_TERRACOTTA = getBlockType("cyan_glazed_terracotta")
    """
    BlockData: Directional
    """
    PURPLE_GLAZED_TERRACOTTA = getBlockType("purple_glazed_terracotta")
    """
    BlockData: Directional
    """
    BLUE_GLAZED_TERRACOTTA = getBlockType("blue_glazed_terracotta")
    """
    BlockData: Directional
    """
    BROWN_GLAZED_TERRACOTTA = getBlockType("brown_glazed_terracotta")
    """
    BlockData: Directional
    """
    GREEN_GLAZED_TERRACOTTA = getBlockType("green_glazed_terracotta")
    """
    BlockData: Directional
    """
    RED_GLAZED_TERRACOTTA = getBlockType("red_glazed_terracotta")
    """
    BlockData: Directional
    """
    BLACK_GLAZED_TERRACOTTA = getBlockType("black_glazed_terracotta")
    """
    BlockData: Directional
    """
    WHITE_CONCRETE = getBlockType("white_concrete")
    ORANGE_CONCRETE = getBlockType("orange_concrete")
    MAGENTA_CONCRETE = getBlockType("magenta_concrete")
    LIGHT_BLUE_CONCRETE = getBlockType("light_blue_concrete")
    YELLOW_CONCRETE = getBlockType("yellow_concrete")
    LIME_CONCRETE = getBlockType("lime_concrete")
    PINK_CONCRETE = getBlockType("pink_concrete")
    GRAY_CONCRETE = getBlockType("gray_concrete")
    LIGHT_GRAY_CONCRETE = getBlockType("light_gray_concrete")
    CYAN_CONCRETE = getBlockType("cyan_concrete")
    PURPLE_CONCRETE = getBlockType("purple_concrete")
    BLUE_CONCRETE = getBlockType("blue_concrete")
    BROWN_CONCRETE = getBlockType("brown_concrete")
    GREEN_CONCRETE = getBlockType("green_concrete")
    RED_CONCRETE = getBlockType("red_concrete")
    BLACK_CONCRETE = getBlockType("black_concrete")
    WHITE_CONCRETE_POWDER = getBlockType("white_concrete_powder")
    ORANGE_CONCRETE_POWDER = getBlockType("orange_concrete_powder")
    MAGENTA_CONCRETE_POWDER = getBlockType("magenta_concrete_powder")
    LIGHT_BLUE_CONCRETE_POWDER = getBlockType("light_blue_concrete_powder")
    YELLOW_CONCRETE_POWDER = getBlockType("yellow_concrete_powder")
    LIME_CONCRETE_POWDER = getBlockType("lime_concrete_powder")
    PINK_CONCRETE_POWDER = getBlockType("pink_concrete_powder")
    GRAY_CONCRETE_POWDER = getBlockType("gray_concrete_powder")
    LIGHT_GRAY_CONCRETE_POWDER = getBlockType("light_gray_concrete_powder")
    CYAN_CONCRETE_POWDER = getBlockType("cyan_concrete_powder")
    PURPLE_CONCRETE_POWDER = getBlockType("purple_concrete_powder")
    BLUE_CONCRETE_POWDER = getBlockType("blue_concrete_powder")
    BROWN_CONCRETE_POWDER = getBlockType("brown_concrete_powder")
    GREEN_CONCRETE_POWDER = getBlockType("green_concrete_powder")
    RED_CONCRETE_POWDER = getBlockType("red_concrete_powder")
    BLACK_CONCRETE_POWDER = getBlockType("black_concrete_powder")
    KELP = getBlockType("kelp")
    """
    BlockData: Ageable
    """
    KELP_PLANT = getBlockType("kelp_plant")
    DRIED_KELP_BLOCK = getBlockType("dried_kelp_block")
    TURTLE_EGG = getBlockType("turtle_egg")
    """
    BlockData: TurtleEgg
    """
    SNIFFER_EGG = getBlockType("sniffer_egg")
    """
    BlockData: Hatchable
    """
    DEAD_TUBE_CORAL_BLOCK = getBlockType("dead_tube_coral_block")
    DEAD_BRAIN_CORAL_BLOCK = getBlockType("dead_brain_coral_block")
    DEAD_BUBBLE_CORAL_BLOCK = getBlockType("dead_bubble_coral_block")
    DEAD_FIRE_CORAL_BLOCK = getBlockType("dead_fire_coral_block")
    DEAD_HORN_CORAL_BLOCK = getBlockType("dead_horn_coral_block")
    TUBE_CORAL_BLOCK = getBlockType("tube_coral_block")
    BRAIN_CORAL_BLOCK = getBlockType("brain_coral_block")
    BUBBLE_CORAL_BLOCK = getBlockType("bubble_coral_block")
    FIRE_CORAL_BLOCK = getBlockType("fire_coral_block")
    HORN_CORAL_BLOCK = getBlockType("horn_coral_block")
    DEAD_TUBE_CORAL = getBlockType("dead_tube_coral")
    """
    BlockData: Waterlogged
    """
    DEAD_BRAIN_CORAL = getBlockType("dead_brain_coral")
    """
    BlockData: Waterlogged
    """
    DEAD_BUBBLE_CORAL = getBlockType("dead_bubble_coral")
    """
    BlockData: Waterlogged
    """
    DEAD_FIRE_CORAL = getBlockType("dead_fire_coral")
    """
    BlockData: Waterlogged
    """
    DEAD_HORN_CORAL = getBlockType("dead_horn_coral")
    """
    BlockData: Waterlogged
    """
    TUBE_CORAL = getBlockType("tube_coral")
    """
    BlockData: Waterlogged
    """
    BRAIN_CORAL = getBlockType("brain_coral")
    """
    BlockData: Waterlogged
    """
    BUBBLE_CORAL = getBlockType("bubble_coral")
    """
    BlockData: Waterlogged
    """
    FIRE_CORAL = getBlockType("fire_coral")
    """
    BlockData: Waterlogged
    """
    HORN_CORAL = getBlockType("horn_coral")
    """
    BlockData: Waterlogged
    """
    DEAD_TUBE_CORAL_FAN = getBlockType("dead_tube_coral_fan")
    """
    BlockData: Waterlogged
    """
    DEAD_BRAIN_CORAL_FAN = getBlockType("dead_brain_coral_fan")
    """
    BlockData: Waterlogged
    """
    DEAD_BUBBLE_CORAL_FAN = getBlockType("dead_bubble_coral_fan")
    """
    BlockData: Waterlogged
    """
    DEAD_FIRE_CORAL_FAN = getBlockType("dead_fire_coral_fan")
    """
    BlockData: Waterlogged
    """
    DEAD_HORN_CORAL_FAN = getBlockType("dead_horn_coral_fan")
    """
    BlockData: Waterlogged
    """
    TUBE_CORAL_FAN = getBlockType("tube_coral_fan")
    """
    BlockData: Waterlogged
    """
    BRAIN_CORAL_FAN = getBlockType("brain_coral_fan")
    """
    BlockData: Waterlogged
    """
    BUBBLE_CORAL_FAN = getBlockType("bubble_coral_fan")
    """
    BlockData: Waterlogged
    """
    FIRE_CORAL_FAN = getBlockType("fire_coral_fan")
    """
    BlockData: Waterlogged
    """
    HORN_CORAL_FAN = getBlockType("horn_coral_fan")
    """
    BlockData: Waterlogged
    """
    DEAD_TUBE_CORAL_WALL_FAN = getBlockType("dead_tube_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    DEAD_BRAIN_CORAL_WALL_FAN = getBlockType("dead_brain_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    DEAD_BUBBLE_CORAL_WALL_FAN = getBlockType("dead_bubble_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    DEAD_FIRE_CORAL_WALL_FAN = getBlockType("dead_fire_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    DEAD_HORN_CORAL_WALL_FAN = getBlockType("dead_horn_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    TUBE_CORAL_WALL_FAN = getBlockType("tube_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    BRAIN_CORAL_WALL_FAN = getBlockType("brain_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    BUBBLE_CORAL_WALL_FAN = getBlockType("bubble_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    FIRE_CORAL_WALL_FAN = getBlockType("fire_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    HORN_CORAL_WALL_FAN = getBlockType("horn_coral_wall_fan")
    """
    BlockData: CoralWallFan
    """
    SEA_PICKLE = getBlockType("sea_pickle")
    """
    BlockData: SeaPickle
    """
    BLUE_ICE = getBlockType("blue_ice")
    CONDUIT = getBlockType("conduit")
    """
    BlockData: Waterlogged
    """
    BAMBOO_SAPLING = getBlockType("bamboo_sapling")
    BAMBOO = getBlockType("bamboo")
    """
    BlockData: Bamboo
    """
    POTTED_BAMBOO = getBlockType("potted_bamboo")
    VOID_AIR = getBlockType("void_air")
    CAVE_AIR = getBlockType("cave_air")
    BUBBLE_COLUMN = getBlockType("bubble_column")
    """
    BlockData: BubbleColumn
    """
    POLISHED_GRANITE_STAIRS = getBlockType("polished_granite_stairs")
    """
    BlockData: Stairs
    """
    SMOOTH_RED_SANDSTONE_STAIRS = getBlockType("smooth_red_sandstone_stairs")
    """
    BlockData: Stairs
    """
    MOSSY_STONE_BRICK_STAIRS = getBlockType("mossy_stone_brick_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_DIORITE_STAIRS = getBlockType("polished_diorite_stairs")
    """
    BlockData: Stairs
    """
    MOSSY_COBBLESTONE_STAIRS = getBlockType("mossy_cobblestone_stairs")
    """
    BlockData: Stairs
    """
    END_STONE_BRICK_STAIRS = getBlockType("end_stone_brick_stairs")
    """
    BlockData: Stairs
    """
    STONE_STAIRS = getBlockType("stone_stairs")
    """
    BlockData: Stairs
    """
    SMOOTH_SANDSTONE_STAIRS = getBlockType("smooth_sandstone_stairs")
    """
    BlockData: Stairs
    """
    SMOOTH_QUARTZ_STAIRS = getBlockType("smooth_quartz_stairs")
    """
    BlockData: Stairs
    """
    GRANITE_STAIRS = getBlockType("granite_stairs")
    """
    BlockData: Stairs
    """
    ANDESITE_STAIRS = getBlockType("andesite_stairs")
    """
    BlockData: Stairs
    """
    RED_NETHER_BRICK_STAIRS = getBlockType("red_nether_brick_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_ANDESITE_STAIRS = getBlockType("polished_andesite_stairs")
    """
    BlockData: Stairs
    """
    DIORITE_STAIRS = getBlockType("diorite_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_GRANITE_SLAB = getBlockType("polished_granite_slab")
    """
    BlockData: Slab
    """
    SMOOTH_RED_SANDSTONE_SLAB = getBlockType("smooth_red_sandstone_slab")
    """
    BlockData: Slab
    """
    MOSSY_STONE_BRICK_SLAB = getBlockType("mossy_stone_brick_slab")
    """
    BlockData: Slab
    """
    POLISHED_DIORITE_SLAB = getBlockType("polished_diorite_slab")
    """
    BlockData: Slab
    """
    MOSSY_COBBLESTONE_SLAB = getBlockType("mossy_cobblestone_slab")
    """
    BlockData: Slab
    """
    END_STONE_BRICK_SLAB = getBlockType("end_stone_brick_slab")
    """
    BlockData: Slab
    """
    SMOOTH_SANDSTONE_SLAB = getBlockType("smooth_sandstone_slab")
    """
    BlockData: Slab
    """
    SMOOTH_QUARTZ_SLAB = getBlockType("smooth_quartz_slab")
    """
    BlockData: Slab
    """
    GRANITE_SLAB = getBlockType("granite_slab")
    """
    BlockData: Slab
    """
    ANDESITE_SLAB = getBlockType("andesite_slab")
    """
    BlockData: Slab
    """
    RED_NETHER_BRICK_SLAB = getBlockType("red_nether_brick_slab")
    """
    BlockData: Slab
    """
    POLISHED_ANDESITE_SLAB = getBlockType("polished_andesite_slab")
    """
    BlockData: Slab
    """
    DIORITE_SLAB = getBlockType("diorite_slab")
    """
    BlockData: Slab
    """
    BRICK_WALL = getBlockType("brick_wall")
    """
    BlockData: Wall
    """
    PRISMARINE_WALL = getBlockType("prismarine_wall")
    """
    BlockData: Wall
    """
    RED_SANDSTONE_WALL = getBlockType("red_sandstone_wall")
    """
    BlockData: Wall
    """
    MOSSY_STONE_BRICK_WALL = getBlockType("mossy_stone_brick_wall")
    """
    BlockData: Wall
    """
    GRANITE_WALL = getBlockType("granite_wall")
    """
    BlockData: Wall
    """
    STONE_BRICK_WALL = getBlockType("stone_brick_wall")
    """
    BlockData: Wall
    """
    MUD_BRICK_WALL = getBlockType("mud_brick_wall")
    """
    BlockData: Wall
    """
    NETHER_BRICK_WALL = getBlockType("nether_brick_wall")
    """
    BlockData: Wall
    """
    ANDESITE_WALL = getBlockType("andesite_wall")
    """
    BlockData: Wall
    """
    RED_NETHER_BRICK_WALL = getBlockType("red_nether_brick_wall")
    """
    BlockData: Wall
    """
    SANDSTONE_WALL = getBlockType("sandstone_wall")
    """
    BlockData: Wall
    """
    END_STONE_BRICK_WALL = getBlockType("end_stone_brick_wall")
    """
    BlockData: Wall
    """
    DIORITE_WALL = getBlockType("diorite_wall")
    """
    BlockData: Wall
    """
    SCAFFOLDING = getBlockType("scaffolding")
    """
    BlockData: Scaffolding
    """
    LOOM = getBlockType("loom")
    """
    BlockData: Directional
    """
    BARREL = getBlockType("barrel")
    """
    BlockData: Barrel
    """
    SMOKER = getBlockType("smoker")
    """
    BlockData: Furnace
    """
    BLAST_FURNACE = getBlockType("blast_furnace")
    """
    BlockData: Furnace
    """
    CARTOGRAPHY_TABLE = getBlockType("cartography_table")
    FLETCHING_TABLE = getBlockType("fletching_table")
    GRINDSTONE = getBlockType("grindstone")
    """
    BlockData: Grindstone
    """
    LECTERN = getBlockType("lectern")
    """
    BlockData: Lectern
    """
    SMITHING_TABLE = getBlockType("smithing_table")
    STONECUTTER = getBlockType("stonecutter")
    """
    BlockData: Directional
    """
    BELL = getBlockType("bell")
    """
    BlockData: Bell
    """
    LANTERN = getBlockType("lantern")
    """
    BlockData: Lantern
    """
    SOUL_LANTERN = getBlockType("soul_lantern")
    """
    BlockData: Lantern
    """
    CAMPFIRE = getBlockType("campfire")
    """
    BlockData: Campfire
    """
    SOUL_CAMPFIRE = getBlockType("soul_campfire")
    """
    BlockData: Campfire
    """
    SWEET_BERRY_BUSH = getBlockType("sweet_berry_bush")
    """
    BlockData: Ageable
    """
    WARPED_STEM = getBlockType("warped_stem")
    """
    BlockData: Orientable
    """
    STRIPPED_WARPED_STEM = getBlockType("stripped_warped_stem")
    """
    BlockData: Orientable
    """
    WARPED_HYPHAE = getBlockType("warped_hyphae")
    """
    BlockData: Orientable
    """
    STRIPPED_WARPED_HYPHAE = getBlockType("stripped_warped_hyphae")
    """
    BlockData: Orientable
    """
    WARPED_NYLIUM = getBlockType("warped_nylium")
    WARPED_FUNGUS = getBlockType("warped_fungus")
    WARPED_WART_BLOCK = getBlockType("warped_wart_block")
    WARPED_ROOTS = getBlockType("warped_roots")
    NETHER_SPROUTS = getBlockType("nether_sprouts")
    CRIMSON_STEM = getBlockType("crimson_stem")
    """
    BlockData: Orientable
    """
    STRIPPED_CRIMSON_STEM = getBlockType("stripped_crimson_stem")
    """
    BlockData: Orientable
    """
    CRIMSON_HYPHAE = getBlockType("crimson_hyphae")
    """
    BlockData: Orientable
    """
    STRIPPED_CRIMSON_HYPHAE = getBlockType("stripped_crimson_hyphae")
    """
    BlockData: Orientable
    """
    CRIMSON_NYLIUM = getBlockType("crimson_nylium")
    CRIMSON_FUNGUS = getBlockType("crimson_fungus")
    SHROOMLIGHT = getBlockType("shroomlight")
    WEEPING_VINES = getBlockType("weeping_vines")
    """
    BlockData: Ageable
    """
    WEEPING_VINES_PLANT = getBlockType("weeping_vines_plant")
    TWISTING_VINES = getBlockType("twisting_vines")
    """
    BlockData: Ageable
    """
    TWISTING_VINES_PLANT = getBlockType("twisting_vines_plant")
    CRIMSON_ROOTS = getBlockType("crimson_roots")
    CRIMSON_PLANKS = getBlockType("crimson_planks")
    WARPED_PLANKS = getBlockType("warped_planks")
    CRIMSON_SLAB = getBlockType("crimson_slab")
    """
    BlockData: Slab
    """
    WARPED_SLAB = getBlockType("warped_slab")
    """
    BlockData: Slab
    """
    CRIMSON_PRESSURE_PLATE = getBlockType("crimson_pressure_plate")
    """
    BlockData: Powerable
    """
    WARPED_PRESSURE_PLATE = getBlockType("warped_pressure_plate")
    """
    BlockData: Powerable
    """
    CRIMSON_FENCE = getBlockType("crimson_fence")
    """
    BlockData: Fence
    """
    WARPED_FENCE = getBlockType("warped_fence")
    """
    BlockData: Fence
    """
    CRIMSON_TRAPDOOR = getBlockType("crimson_trapdoor")
    """
    BlockData: TrapDoor
    """
    WARPED_TRAPDOOR = getBlockType("warped_trapdoor")
    """
    BlockData: TrapDoor
    """
    CRIMSON_FENCE_GATE = getBlockType("crimson_fence_gate")
    """
    BlockData: Gate
    """
    WARPED_FENCE_GATE = getBlockType("warped_fence_gate")
    """
    BlockData: Gate
    """
    CRIMSON_STAIRS = getBlockType("crimson_stairs")
    """
    BlockData: Stairs
    """
    WARPED_STAIRS = getBlockType("warped_stairs")
    """
    BlockData: Stairs
    """
    CRIMSON_BUTTON = getBlockType("crimson_button")
    """
    BlockData: Switch
    """
    WARPED_BUTTON = getBlockType("warped_button")
    """
    BlockData: Switch
    """
    CRIMSON_DOOR = getBlockType("crimson_door")
    """
    BlockData: Door
    """
    WARPED_DOOR = getBlockType("warped_door")
    """
    BlockData: Door
    """
    CRIMSON_SIGN = getBlockType("crimson_sign")
    """
    BlockData: Sign
    """
    WARPED_SIGN = getBlockType("warped_sign")
    """
    BlockData: Sign
    """
    CRIMSON_WALL_SIGN = getBlockType("crimson_wall_sign")
    """
    BlockData: WallSign
    """
    WARPED_WALL_SIGN = getBlockType("warped_wall_sign")
    """
    BlockData: WallSign
    """
    STRUCTURE_BLOCK = getBlockType("structure_block")
    """
    BlockData: StructureBlock
    """
    JIGSAW = getBlockType("jigsaw")
    """
    BlockData: Jigsaw
    """
    COMPOSTER = getBlockType("composter")
    """
    BlockData: Levelled
    """
    TARGET = getBlockType("target")
    """
    BlockData: AnaloguePowerable
    """
    BEE_NEST = getBlockType("bee_nest")
    """
    BlockData: Beehive
    """
    BEEHIVE = getBlockType("beehive")
    """
    BlockData: Beehive
    """
    HONEY_BLOCK = getBlockType("honey_block")
    HONEYCOMB_BLOCK = getBlockType("honeycomb_block")
    NETHERITE_BLOCK = getBlockType("netherite_block")
    ANCIENT_DEBRIS = getBlockType("ancient_debris")
    CRYING_OBSIDIAN = getBlockType("crying_obsidian")
    RESPAWN_ANCHOR = getBlockType("respawn_anchor")
    """
    BlockData: RespawnAnchor
    """
    POTTED_CRIMSON_FUNGUS = getBlockType("potted_crimson_fungus")
    POTTED_WARPED_FUNGUS = getBlockType("potted_warped_fungus")
    POTTED_CRIMSON_ROOTS = getBlockType("potted_crimson_roots")
    POTTED_WARPED_ROOTS = getBlockType("potted_warped_roots")
    LODESTONE = getBlockType("lodestone")
    BLACKSTONE = getBlockType("blackstone")
    BLACKSTONE_STAIRS = getBlockType("blackstone_stairs")
    """
    BlockData: Stairs
    """
    BLACKSTONE_WALL = getBlockType("blackstone_wall")
    """
    BlockData: Wall
    """
    BLACKSTONE_SLAB = getBlockType("blackstone_slab")
    """
    BlockData: Slab
    """
    POLISHED_BLACKSTONE = getBlockType("polished_blackstone")
    POLISHED_BLACKSTONE_BRICKS = getBlockType("polished_blackstone_bricks")
    CRACKED_POLISHED_BLACKSTONE_BRICKS = getBlockType("cracked_polished_blackstone_bricks")
    CHISELED_POLISHED_BLACKSTONE = getBlockType("chiseled_polished_blackstone")
    POLISHED_BLACKSTONE_BRICK_SLAB = getBlockType("polished_blackstone_brick_slab")
    """
    BlockData: Slab
    """
    POLISHED_BLACKSTONE_BRICK_STAIRS = getBlockType("polished_blackstone_brick_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_BLACKSTONE_BRICK_WALL = getBlockType("polished_blackstone_brick_wall")
    """
    BlockData: Wall
    """
    GILDED_BLACKSTONE = getBlockType("gilded_blackstone")
    POLISHED_BLACKSTONE_STAIRS = getBlockType("polished_blackstone_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_BLACKSTONE_SLAB = getBlockType("polished_blackstone_slab")
    """
    BlockData: Slab
    """
    POLISHED_BLACKSTONE_PRESSURE_PLATE = getBlockType("polished_blackstone_pressure_plate")
    """
    BlockData: Powerable
    """
    POLISHED_BLACKSTONE_BUTTON = getBlockType("polished_blackstone_button")
    """
    BlockData: Switch
    """
    POLISHED_BLACKSTONE_WALL = getBlockType("polished_blackstone_wall")
    """
    BlockData: Wall
    """
    CHISELED_NETHER_BRICKS = getBlockType("chiseled_nether_bricks")
    CRACKED_NETHER_BRICKS = getBlockType("cracked_nether_bricks")
    QUARTZ_BRICKS = getBlockType("quartz_bricks")
    CANDLE = getBlockType("candle")
    """
    BlockData: Candle
    """
    WHITE_CANDLE = getBlockType("white_candle")
    """
    BlockData: Candle
    """
    ORANGE_CANDLE = getBlockType("orange_candle")
    """
    BlockData: Candle
    """
    MAGENTA_CANDLE = getBlockType("magenta_candle")
    """
    BlockData: Candle
    """
    LIGHT_BLUE_CANDLE = getBlockType("light_blue_candle")
    """
    BlockData: Candle
    """
    YELLOW_CANDLE = getBlockType("yellow_candle")
    """
    BlockData: Candle
    """
    LIME_CANDLE = getBlockType("lime_candle")
    """
    BlockData: Candle
    """
    PINK_CANDLE = getBlockType("pink_candle")
    """
    BlockData: Candle
    """
    GRAY_CANDLE = getBlockType("gray_candle")
    """
    BlockData: Candle
    """
    LIGHT_GRAY_CANDLE = getBlockType("light_gray_candle")
    """
    BlockData: Candle
    """
    CYAN_CANDLE = getBlockType("cyan_candle")
    """
    BlockData: Candle
    """
    PURPLE_CANDLE = getBlockType("purple_candle")
    """
    BlockData: Candle
    """
    BLUE_CANDLE = getBlockType("blue_candle")
    """
    BlockData: Candle
    """
    BROWN_CANDLE = getBlockType("brown_candle")
    """
    BlockData: Candle
    """
    GREEN_CANDLE = getBlockType("green_candle")
    """
    BlockData: Candle
    """
    RED_CANDLE = getBlockType("red_candle")
    """
    BlockData: Candle
    """
    BLACK_CANDLE = getBlockType("black_candle")
    """
    BlockData: Candle
    """
    CANDLE_CAKE = getBlockType("candle_cake")
    """
    BlockData: Lightable
    """
    WHITE_CANDLE_CAKE = getBlockType("white_candle_cake")
    """
    BlockData: Lightable
    """
    ORANGE_CANDLE_CAKE = getBlockType("orange_candle_cake")
    """
    BlockData: Lightable
    """
    MAGENTA_CANDLE_CAKE = getBlockType("magenta_candle_cake")
    """
    BlockData: Lightable
    """
    LIGHT_BLUE_CANDLE_CAKE = getBlockType("light_blue_candle_cake")
    """
    BlockData: Lightable
    """
    YELLOW_CANDLE_CAKE = getBlockType("yellow_candle_cake")
    """
    BlockData: Lightable
    """
    LIME_CANDLE_CAKE = getBlockType("lime_candle_cake")
    """
    BlockData: Lightable
    """
    PINK_CANDLE_CAKE = getBlockType("pink_candle_cake")
    """
    BlockData: Lightable
    """
    GRAY_CANDLE_CAKE = getBlockType("gray_candle_cake")
    """
    BlockData: Lightable
    """
    LIGHT_GRAY_CANDLE_CAKE = getBlockType("light_gray_candle_cake")
    """
    BlockData: Lightable
    """
    CYAN_CANDLE_CAKE = getBlockType("cyan_candle_cake")
    """
    BlockData: Lightable
    """
    PURPLE_CANDLE_CAKE = getBlockType("purple_candle_cake")
    """
    BlockData: Lightable
    """
    BLUE_CANDLE_CAKE = getBlockType("blue_candle_cake")
    """
    BlockData: Lightable
    """
    BROWN_CANDLE_CAKE = getBlockType("brown_candle_cake")
    """
    BlockData: Lightable
    """
    GREEN_CANDLE_CAKE = getBlockType("green_candle_cake")
    """
    BlockData: Lightable
    """
    RED_CANDLE_CAKE = getBlockType("red_candle_cake")
    """
    BlockData: Lightable
    """
    BLACK_CANDLE_CAKE = getBlockType("black_candle_cake")
    """
    BlockData: Lightable
    """
    AMETHYST_BLOCK = getBlockType("amethyst_block")
    BUDDING_AMETHYST = getBlockType("budding_amethyst")
    AMETHYST_CLUSTER = getBlockType("amethyst_cluster")
    """
    BlockData: AmethystCluster
    """
    LARGE_AMETHYST_BUD = getBlockType("large_amethyst_bud")
    """
    BlockData: AmethystCluster
    """
    MEDIUM_AMETHYST_BUD = getBlockType("medium_amethyst_bud")
    """
    BlockData: AmethystCluster
    """
    SMALL_AMETHYST_BUD = getBlockType("small_amethyst_bud")
    """
    BlockData: AmethystCluster
    """
    TUFF = getBlockType("tuff")
    TUFF_SLAB = getBlockType("tuff_slab")
    """
    BlockData: Slab
    """
    TUFF_STAIRS = getBlockType("tuff_stairs")
    """
    BlockData: Stairs
    """
    TUFF_WALL = getBlockType("tuff_wall")
    """
    BlockData: Wall
    """
    POLISHED_TUFF = getBlockType("polished_tuff")
    POLISHED_TUFF_SLAB = getBlockType("polished_tuff_slab")
    """
    BlockData: Slab
    """
    POLISHED_TUFF_STAIRS = getBlockType("polished_tuff_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_TUFF_WALL = getBlockType("polished_tuff_wall")
    """
    BlockData: Wall
    """
    CHISELED_TUFF = getBlockType("chiseled_tuff")
    TUFF_BRICKS = getBlockType("tuff_bricks")
    TUFF_BRICK_SLAB = getBlockType("tuff_brick_slab")
    """
    BlockData: Slab
    """
    TUFF_BRICK_STAIRS = getBlockType("tuff_brick_stairs")
    """
    BlockData: Stairs
    """
    TUFF_BRICK_WALL = getBlockType("tuff_brick_wall")
    """
    BlockData: Wall
    """
    CHISELED_TUFF_BRICKS = getBlockType("chiseled_tuff_bricks")
    CALCITE = getBlockType("calcite")
    TINTED_GLASS = getBlockType("tinted_glass")
    POWDER_SNOW = getBlockType("powder_snow")
    SCULK_SENSOR = getBlockType("sculk_sensor")
    """
    BlockData: SculkSensor
    """
    CALIBRATED_SCULK_SENSOR = getBlockType("calibrated_sculk_sensor")
    """
    BlockData: CalibratedSculkSensor
    """
    SCULK = getBlockType("sculk")
    SCULK_VEIN = getBlockType("sculk_vein")
    """
    BlockData: SculkVein
    """
    SCULK_CATALYST = getBlockType("sculk_catalyst")
    """
    BlockData: SculkCatalyst
    """
    SCULK_SHRIEKER = getBlockType("sculk_shrieker")
    """
    BlockData: SculkShrieker
    """
    COPPER_BLOCK = getBlockType("copper_block")
    EXPOSED_COPPER = getBlockType("exposed_copper")
    WEATHERED_COPPER = getBlockType("weathered_copper")
    OXIDIZED_COPPER = getBlockType("oxidized_copper")
    COPPER_ORE = getBlockType("copper_ore")
    DEEPSLATE_COPPER_ORE = getBlockType("deepslate_copper_ore")
    OXIDIZED_CUT_COPPER = getBlockType("oxidized_cut_copper")
    WEATHERED_CUT_COPPER = getBlockType("weathered_cut_copper")
    EXPOSED_CUT_COPPER = getBlockType("exposed_cut_copper")
    CUT_COPPER = getBlockType("cut_copper")
    OXIDIZED_CHISELED_COPPER = getBlockType("oxidized_chiseled_copper")
    WEATHERED_CHISELED_COPPER = getBlockType("weathered_chiseled_copper")
    EXPOSED_CHISELED_COPPER = getBlockType("exposed_chiseled_copper")
    CHISELED_COPPER = getBlockType("chiseled_copper")
    WAXED_OXIDIZED_CHISELED_COPPER = getBlockType("waxed_oxidized_chiseled_copper")
    WAXED_WEATHERED_CHISELED_COPPER = getBlockType("waxed_weathered_chiseled_copper")
    WAXED_EXPOSED_CHISELED_COPPER = getBlockType("waxed_exposed_chiseled_copper")
    WAXED_CHISELED_COPPER = getBlockType("waxed_chiseled_copper")
    OXIDIZED_CUT_COPPER_STAIRS = getBlockType("oxidized_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    WEATHERED_CUT_COPPER_STAIRS = getBlockType("weathered_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    EXPOSED_CUT_COPPER_STAIRS = getBlockType("exposed_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    CUT_COPPER_STAIRS = getBlockType("cut_copper_stairs")
    """
    BlockData: Stairs
    """
    OXIDIZED_CUT_COPPER_SLAB = getBlockType("oxidized_cut_copper_slab")
    """
    BlockData: Slab
    """
    WEATHERED_CUT_COPPER_SLAB = getBlockType("weathered_cut_copper_slab")
    """
    BlockData: Slab
    """
    EXPOSED_CUT_COPPER_SLAB = getBlockType("exposed_cut_copper_slab")
    """
    BlockData: Slab
    """
    CUT_COPPER_SLAB = getBlockType("cut_copper_slab")
    """
    BlockData: Slab
    """
    WAXED_COPPER_BLOCK = getBlockType("waxed_copper_block")
    WAXED_WEATHERED_COPPER = getBlockType("waxed_weathered_copper")
    WAXED_EXPOSED_COPPER = getBlockType("waxed_exposed_copper")
    WAXED_OXIDIZED_COPPER = getBlockType("waxed_oxidized_copper")
    WAXED_OXIDIZED_CUT_COPPER = getBlockType("waxed_oxidized_cut_copper")
    WAXED_WEATHERED_CUT_COPPER = getBlockType("waxed_weathered_cut_copper")
    WAXED_EXPOSED_CUT_COPPER = getBlockType("waxed_exposed_cut_copper")
    WAXED_CUT_COPPER = getBlockType("waxed_cut_copper")
    WAXED_OXIDIZED_CUT_COPPER_STAIRS = getBlockType("waxed_oxidized_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    WAXED_WEATHERED_CUT_COPPER_STAIRS = getBlockType("waxed_weathered_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    WAXED_EXPOSED_CUT_COPPER_STAIRS = getBlockType("waxed_exposed_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    WAXED_CUT_COPPER_STAIRS = getBlockType("waxed_cut_copper_stairs")
    """
    BlockData: Stairs
    """
    WAXED_OXIDIZED_CUT_COPPER_SLAB = getBlockType("waxed_oxidized_cut_copper_slab")
    """
    BlockData: Slab
    """
    WAXED_WEATHERED_CUT_COPPER_SLAB = getBlockType("waxed_weathered_cut_copper_slab")
    """
    BlockData: Slab
    """
    WAXED_EXPOSED_CUT_COPPER_SLAB = getBlockType("waxed_exposed_cut_copper_slab")
    """
    BlockData: Slab
    """
    WAXED_CUT_COPPER_SLAB = getBlockType("waxed_cut_copper_slab")
    """
    BlockData: Slab
    """
    COPPER_DOOR = getBlockType("copper_door")
    """
    BlockData: Door
    """
    EXPOSED_COPPER_DOOR = getBlockType("exposed_copper_door")
    """
    BlockData: Door
    """
    OXIDIZED_COPPER_DOOR = getBlockType("oxidized_copper_door")
    """
    BlockData: Door
    """
    WEATHERED_COPPER_DOOR = getBlockType("weathered_copper_door")
    """
    BlockData: Door
    """
    WAXED_COPPER_DOOR = getBlockType("waxed_copper_door")
    """
    BlockData: Door
    """
    WAXED_EXPOSED_COPPER_DOOR = getBlockType("waxed_exposed_copper_door")
    """
    BlockData: Door
    """
    WAXED_OXIDIZED_COPPER_DOOR = getBlockType("waxed_oxidized_copper_door")
    """
    BlockData: Door
    """
    WAXED_WEATHERED_COPPER_DOOR = getBlockType("waxed_weathered_copper_door")
    """
    BlockData: Door
    """
    COPPER_TRAPDOOR = getBlockType("copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    EXPOSED_COPPER_TRAPDOOR = getBlockType("exposed_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    OXIDIZED_COPPER_TRAPDOOR = getBlockType("oxidized_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    WEATHERED_COPPER_TRAPDOOR = getBlockType("weathered_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    WAXED_COPPER_TRAPDOOR = getBlockType("waxed_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    WAXED_EXPOSED_COPPER_TRAPDOOR = getBlockType("waxed_exposed_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    WAXED_OXIDIZED_COPPER_TRAPDOOR = getBlockType("waxed_oxidized_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    WAXED_WEATHERED_COPPER_TRAPDOOR = getBlockType("waxed_weathered_copper_trapdoor")
    """
    BlockData: TrapDoor
    """
    COPPER_GRATE = getBlockType("copper_grate")
    """
    BlockData: Waterlogged
    """
    EXPOSED_COPPER_GRATE = getBlockType("exposed_copper_grate")
    """
    BlockData: Waterlogged
    """
    WEATHERED_COPPER_GRATE = getBlockType("weathered_copper_grate")
    """
    BlockData: Waterlogged
    """
    OXIDIZED_COPPER_GRATE = getBlockType("oxidized_copper_grate")
    """
    BlockData: Waterlogged
    """
    WAXED_COPPER_GRATE = getBlockType("waxed_copper_grate")
    """
    BlockData: Waterlogged
    """
    WAXED_EXPOSED_COPPER_GRATE = getBlockType("waxed_exposed_copper_grate")
    """
    BlockData: Waterlogged
    """
    WAXED_WEATHERED_COPPER_GRATE = getBlockType("waxed_weathered_copper_grate")
    """
    BlockData: Waterlogged
    """
    WAXED_OXIDIZED_COPPER_GRATE = getBlockType("waxed_oxidized_copper_grate")
    """
    BlockData: Waterlogged
    """
    COPPER_BULB = getBlockType("copper_bulb")
    """
    BlockData: CopperBulb
    """
    EXPOSED_COPPER_BULB = getBlockType("exposed_copper_bulb")
    """
    BlockData: CopperBulb
    """
    WEATHERED_COPPER_BULB = getBlockType("weathered_copper_bulb")
    """
    BlockData: CopperBulb
    """
    OXIDIZED_COPPER_BULB = getBlockType("oxidized_copper_bulb")
    """
    BlockData: CopperBulb
    """
    WAXED_COPPER_BULB = getBlockType("waxed_copper_bulb")
    """
    BlockData: CopperBulb
    """
    WAXED_EXPOSED_COPPER_BULB = getBlockType("waxed_exposed_copper_bulb")
    """
    BlockData: CopperBulb
    """
    WAXED_WEATHERED_COPPER_BULB = getBlockType("waxed_weathered_copper_bulb")
    """
    BlockData: CopperBulb
    """
    WAXED_OXIDIZED_COPPER_BULB = getBlockType("waxed_oxidized_copper_bulb")
    """
    BlockData: CopperBulb
    """
    LIGHTNING_ROD = getBlockType("lightning_rod")
    """
    BlockData: LightningRod
    """
    POINTED_DRIPSTONE = getBlockType("pointed_dripstone")
    """
    BlockData: PointedDripstone
    """
    DRIPSTONE_BLOCK = getBlockType("dripstone_block")
    CAVE_VINES = getBlockType("cave_vines")
    """
    BlockData: CaveVines
    """
    CAVE_VINES_PLANT = getBlockType("cave_vines_plant")
    """
    BlockData: CaveVinesPlant
    """
    SPORE_BLOSSOM = getBlockType("spore_blossom")
    AZALEA = getBlockType("azalea")
    FLOWERING_AZALEA = getBlockType("flowering_azalea")
    MOSS_CARPET = getBlockType("moss_carpet")
    PINK_PETALS = getBlockType("pink_petals")
    """
    BlockData: PinkPetals
    """
    MOSS_BLOCK = getBlockType("moss_block")
    BIG_DRIPLEAF = getBlockType("big_dripleaf")
    """
    BlockData: BigDripleaf
    """
    BIG_DRIPLEAF_STEM = getBlockType("big_dripleaf_stem")
    """
    BlockData: Dripleaf
    """
    SMALL_DRIPLEAF = getBlockType("small_dripleaf")
    """
    BlockData: SmallDripleaf
    """
    HANGING_ROOTS = getBlockType("hanging_roots")
    """
    BlockData: Waterlogged
    """
    ROOTED_DIRT = getBlockType("rooted_dirt")
    MUD = getBlockType("mud")
    DEEPSLATE = getBlockType("deepslate")
    """
    BlockData: Orientable
    """
    COBBLED_DEEPSLATE = getBlockType("cobbled_deepslate")
    COBBLED_DEEPSLATE_STAIRS = getBlockType("cobbled_deepslate_stairs")
    """
    BlockData: Stairs
    """
    COBBLED_DEEPSLATE_SLAB = getBlockType("cobbled_deepslate_slab")
    """
    BlockData: Slab
    """
    COBBLED_DEEPSLATE_WALL = getBlockType("cobbled_deepslate_wall")
    """
    BlockData: Wall
    """
    POLISHED_DEEPSLATE = getBlockType("polished_deepslate")
    POLISHED_DEEPSLATE_STAIRS = getBlockType("polished_deepslate_stairs")
    """
    BlockData: Stairs
    """
    POLISHED_DEEPSLATE_SLAB = getBlockType("polished_deepslate_slab")
    """
    BlockData: Slab
    """
    POLISHED_DEEPSLATE_WALL = getBlockType("polished_deepslate_wall")
    """
    BlockData: Wall
    """
    DEEPSLATE_TILES = getBlockType("deepslate_tiles")
    DEEPSLATE_TILE_STAIRS = getBlockType("deepslate_tile_stairs")
    """
    BlockData: Stairs
    """
    DEEPSLATE_TILE_SLAB = getBlockType("deepslate_tile_slab")
    """
    BlockData: Slab
    """
    DEEPSLATE_TILE_WALL = getBlockType("deepslate_tile_wall")
    """
    BlockData: Wall
    """
    DEEPSLATE_BRICKS = getBlockType("deepslate_bricks")
    DEEPSLATE_BRICK_STAIRS = getBlockType("deepslate_brick_stairs")
    """
    BlockData: Stairs
    """
    DEEPSLATE_BRICK_SLAB = getBlockType("deepslate_brick_slab")
    """
    BlockData: Slab
    """
    DEEPSLATE_BRICK_WALL = getBlockType("deepslate_brick_wall")
    """
    BlockData: Wall
    """
    CHISELED_DEEPSLATE = getBlockType("chiseled_deepslate")
    CRACKED_DEEPSLATE_BRICKS = getBlockType("cracked_deepslate_bricks")
    CRACKED_DEEPSLATE_TILES = getBlockType("cracked_deepslate_tiles")
    INFESTED_DEEPSLATE = getBlockType("infested_deepslate")
    """
    BlockData: Orientable
    """
    SMOOTH_BASALT = getBlockType("smooth_basalt")
    RAW_IRON_BLOCK = getBlockType("raw_iron_block")
    RAW_COPPER_BLOCK = getBlockType("raw_copper_block")
    RAW_GOLD_BLOCK = getBlockType("raw_gold_block")
    POTTED_AZALEA_BUSH = getBlockType("potted_azalea_bush")
    POTTED_FLOWERING_AZALEA_BUSH = getBlockType("potted_flowering_azalea_bush")
    OCHRE_FROGLIGHT = getBlockType("ochre_froglight")
    """
    BlockData: Orientable
    """
    VERDANT_FROGLIGHT = getBlockType("verdant_froglight")
    """
    BlockData: Orientable
    """
    PEARLESCENT_FROGLIGHT = getBlockType("pearlescent_froglight")
    """
    BlockData: Orientable
    """
    FROGSPAWN = getBlockType("frogspawn")
    REINFORCED_DEEPSLATE = getBlockType("reinforced_deepslate")
    DECORATED_POT = getBlockType("decorated_pot")
    """
    BlockData: DecoratedPot
    """
    CRAFTER = getBlockType("crafter")
    """
    BlockData: Crafter
    """
    TRIAL_SPAWNER = getBlockType("trial_spawner")
    """
    BlockData: TrialSpawner
    """


    @staticmethod
    def getBlockType(key: str) -> "B":
        ...


    def typed(self) -> "BlockType.Typed"["BlockData"]:
        """
        Yields this block type as a typed version of itself with a plain BlockData representing it.

        Returns
        - the typed block type.
        """
        ...


    def typed(self, blockDataType: type["B"]) -> "BlockType.Typed"["B"]:
        """
        Yields this block type as a typed version of itself with a specific BlockData representing it.
        
        Type `<B>`: the generic type of the block data to type this block type with.

        Arguments
        - blockDataType: the class type of the BlockData to type this BlockType with.

        Returns
        - the typed block type.
        """
        ...


    def hasItemType(self) -> bool:
        """
        Returns True if this BlockType has a corresponding ItemType.

        Returns
        - True if there is a corresponding ItemType, otherwise False

        See
        - .getItemType()
        """
        ...


    def getItemType(self) -> "ItemType":
        """
        Returns the corresponding ItemType for the given BlockType.
        
        If there is no corresponding ItemType an error will be thrown.

        Returns
        - the corresponding ItemType

        See
        - BlockData.getPlacementMaterial()
        """
        ...


    def getBlockDataClass(self) -> type["BlockData"]:
        """
        Gets the BlockData class of this BlockType

        Returns
        - the BlockData class of this BlockType
        """
        ...


    def createBlockData(self) -> "BlockData":
        """
        Creates a new BlockData instance for this block type, with all
        properties initialized to unspecified defaults.

        Returns
        - new data instance
        """
        ...


    def createBlockData(self, data: str) -> "BlockData":
        """
        Creates a new BlockData instance for this block type, with all
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


    def isSolid(self) -> bool:
        """
        Check if the blockt type is solid (can be built upon)

        Returns
        - True if this block type is solid
        """
        ...


    def isFlammable(self) -> bool:
        """
        Check if the block type can catch fire

        Returns
        - True if this block type can catch fire
        """
        ...


    def isBurnable(self) -> bool:
        """
        Check if the block type can burn away

        Returns
        - True if this block type can burn away
        """
        ...


    def isOccluding(self) -> bool:
        """
        Check if the block type is occludes light in the lighting engine.
        
        Generally speaking, most full blocks will occlude light. Non-full blocks are
        not occluding (e.g. anvils, chests, tall grass, stairs, etc.), nor are specific
        full blocks such as barriers or spawners which block light despite their texture.
        
        An occluding block will have the following effects:
        
          - Chests cannot be opened if an occluding block is above it.
          - Mobs cannot spawn inside of occluding blocks.
          - Only occluding blocks can be "powered" (Block.isBlockPowered()).
        
        This list may be inconclusive. For a full list of the side effects of an occluding
        block, see the <a href="https://minecraft.fandom.com/wiki/Opacity">Minecraft Wiki</a>.

        Returns
        - True if this block type occludes light
        """
        ...


    def hasGravity(self) -> bool:
        """
        Returns
        - True if this block type is affected by gravity.
        """
        ...


    def isInteractable(self) -> bool:
        """
        Checks if this block type can be interacted with.
        
        Interactable block types include those with functionality when they are
        interacted with by a player such as chests, furnaces, etc.
        
        Some blocks such as piston heads and stairs are considered interactable
        though may not perform any additional functionality.
        
        Note that the interactability of some block types may be dependant on their
        state as well. This method will return True if there is at least one
        state in which additional interact handling is performed for the
        block type.

        Returns
        - True if this block type can be interacted with.
        """
        ...


    def getHardness(self) -> float:
        """
        Obtains the block's hardness level (also known as "strength").
        
        This number is used to calculate the time required to break each block.

        Returns
        - the hardness of that block type.
        """
        ...


    def getBlastResistance(self) -> float:
        """
        Obtains the blast resistance value (also known as block "durability").
        
        This value is used in explosions to calculate whether a block should be
        broken or not.

        Returns
        - the blast resistance of that block type.
        """
        ...


    def getSlipperiness(self) -> float:
        """
        Returns a value that represents how 'slippery' the block is.
        
        Blocks with higher slipperiness, like BlockType.ICE can be slid on
        further by the player and other entities.
        
        Most blocks have a default slipperiness of `0.6f`.

        Returns
        - the slipperiness of this block
        """
        ...


    def isAir(self) -> bool:
        """
        Check if the block type is an air block.

        Returns
        - True if this block type is an air block.
        """
        ...


    def isEnabledByFeature(self, world: "World") -> bool:
        """
        Gets if the BlockType is enabled by the features in a world.

        Arguments
        - world: the world to check

        Returns
        - True if this BlockType can be used in this World.
        """
        ...


    def asMaterial(self) -> "Material":
        """
        Tries to convert this BlockType into a Material

        Returns
        - the converted Material or null

        Deprecated
        - only for internal use
        """
        ...
