"""
Python module generated from Java source file org.bukkit.inventory.ItemType

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Multimap
from java.util.function import Consumer
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit import World
from org.bukkit.attribute import Attribute
from org.bukkit.attribute import AttributeModifier
from org.bukkit.block import BlockType
from org.bukkit.inventory import *
from org.bukkit.inventory.meta import ArmorMeta
from org.bukkit.inventory.meta import AxolotlBucketMeta
from org.bukkit.inventory.meta import BannerMeta
from org.bukkit.inventory.meta import BlockStateMeta
from org.bukkit.inventory.meta import BookMeta
from org.bukkit.inventory.meta import BundleMeta
from org.bukkit.inventory.meta import ColorableArmorMeta
from org.bukkit.inventory.meta import CompassMeta
from org.bukkit.inventory.meta import CrossbowMeta
from org.bukkit.inventory.meta import EnchantmentStorageMeta
from org.bukkit.inventory.meta import FireworkEffectMeta
from org.bukkit.inventory.meta import FireworkMeta
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.inventory.meta import KnowledgeBookMeta
from org.bukkit.inventory.meta import LeatherArmorMeta
from org.bukkit.inventory.meta import MapMeta
from org.bukkit.inventory.meta import MusicInstrumentMeta
from org.bukkit.inventory.meta import OminousBottleMeta
from org.bukkit.inventory.meta import PotionMeta
from org.bukkit.inventory.meta import ShieldMeta
from org.bukkit.inventory.meta import SkullMeta
from org.bukkit.inventory.meta import SpawnEggMeta
from org.bukkit.inventory.meta import SuspiciousStewMeta
from org.bukkit.inventory.meta import TropicalFishBucketMeta
from typing import Any, Callable, Iterable, Tuple


class ItemType(Keyed, Translatable):
    """
    While this API is in a public interface, it is not intended for use by
    plugins until further notice. The purpose of these types is to make
    Material more maintenance friendly, but will in due time be the
    official replacement for the aforementioned enum. Entirely incompatible
    changes may occur. Do not use this API in plugins.
    """

    AIR = getItemType("air")
    """
    Air does not have any ItemMeta
    """
    STONE = getItemType("stone")
    GRANITE = getItemType("granite")
    POLISHED_GRANITE = getItemType("polished_granite")
    DIORITE = getItemType("diorite")
    POLISHED_DIORITE = getItemType("polished_diorite")
    ANDESITE = getItemType("andesite")
    POLISHED_ANDESITE = getItemType("polished_andesite")
    DEEPSLATE = getItemType("deepslate")
    COBBLED_DEEPSLATE = getItemType("cobbled_deepslate")
    POLISHED_DEEPSLATE = getItemType("polished_deepslate")
    CALCITE = getItemType("calcite")
    TUFF = getItemType("tuff")
    TUFF_SLAB = getItemType("tuff_slab")
    TUFF_STAIRS = getItemType("tuff_stairs")
    TUFF_WALL = getItemType("tuff_wall")
    CHISELED_TUFF = getItemType("chiseled_tuff")
    POLISHED_TUFF = getItemType("polished_tuff")
    POLISHED_TUFF_SLAB = getItemType("polished_tuff_slab")
    POLISHED_TUFF_STAIRS = getItemType("polished_tuff_stairs")
    POLISHED_TUFF_WALL = getItemType("polished_tuff_wall")
    TUFF_BRICKS = getItemType("tuff_bricks")
    TUFF_BRICK_SLAB = getItemType("tuff_brick_slab")
    TUFF_BRICK_STAIRS = getItemType("tuff_brick_stairs")
    TUFF_BRICK_WALL = getItemType("tuff_brick_wall")
    CHISELED_TUFF_BRICKS = getItemType("chiseled_tuff_bricks")
    DRIPSTONE_BLOCK = getItemType("dripstone_block")
    GRASS_BLOCK = getItemType("grass_block")
    DIRT = getItemType("dirt")
    COARSE_DIRT = getItemType("coarse_dirt")
    PODZOL = getItemType("podzol")
    ROOTED_DIRT = getItemType("rooted_dirt")
    MUD = getItemType("mud")
    CRIMSON_NYLIUM = getItemType("crimson_nylium")
    WARPED_NYLIUM = getItemType("warped_nylium")
    COBBLESTONE = getItemType("cobblestone")
    OAK_PLANKS = getItemType("oak_planks")
    SPRUCE_PLANKS = getItemType("spruce_planks")
    BIRCH_PLANKS = getItemType("birch_planks")
    JUNGLE_PLANKS = getItemType("jungle_planks")
    ACACIA_PLANKS = getItemType("acacia_planks")
    CHERRY_PLANKS = getItemType("cherry_planks")
    DARK_OAK_PLANKS = getItemType("dark_oak_planks")
    MANGROVE_PLANKS = getItemType("mangrove_planks")
    BAMBOO_PLANKS = getItemType("bamboo_planks")
    CRIMSON_PLANKS = getItemType("crimson_planks")
    WARPED_PLANKS = getItemType("warped_planks")
    BAMBOO_MOSAIC = getItemType("bamboo_mosaic")
    OAK_SAPLING = getItemType("oak_sapling")
    SPRUCE_SAPLING = getItemType("spruce_sapling")
    BIRCH_SAPLING = getItemType("birch_sapling")
    JUNGLE_SAPLING = getItemType("jungle_sapling")
    ACACIA_SAPLING = getItemType("acacia_sapling")
    CHERRY_SAPLING = getItemType("cherry_sapling")
    DARK_OAK_SAPLING = getItemType("dark_oak_sapling")
    MANGROVE_PROPAGULE = getItemType("mangrove_propagule")
    BEDROCK = getItemType("bedrock")
    SAND = getItemType("sand")
    SUSPICIOUS_SAND = getItemType("suspicious_sand")
    """
    ItemMeta: BlockStateMeta
    """
    SUSPICIOUS_GRAVEL = getItemType("suspicious_gravel")
    """
    ItemMeta: BlockStateMeta
    """
    RED_SAND = getItemType("red_sand")
    GRAVEL = getItemType("gravel")
    COAL_ORE = getItemType("coal_ore")
    DEEPSLATE_COAL_ORE = getItemType("deepslate_coal_ore")
    IRON_ORE = getItemType("iron_ore")
    DEEPSLATE_IRON_ORE = getItemType("deepslate_iron_ore")
    COPPER_ORE = getItemType("copper_ore")
    DEEPSLATE_COPPER_ORE = getItemType("deepslate_copper_ore")
    GOLD_ORE = getItemType("gold_ore")
    DEEPSLATE_GOLD_ORE = getItemType("deepslate_gold_ore")
    REDSTONE_ORE = getItemType("redstone_ore")
    DEEPSLATE_REDSTONE_ORE = getItemType("deepslate_redstone_ore")
    EMERALD_ORE = getItemType("emerald_ore")
    DEEPSLATE_EMERALD_ORE = getItemType("deepslate_emerald_ore")
    LAPIS_ORE = getItemType("lapis_ore")
    DEEPSLATE_LAPIS_ORE = getItemType("deepslate_lapis_ore")
    DIAMOND_ORE = getItemType("diamond_ore")
    DEEPSLATE_DIAMOND_ORE = getItemType("deepslate_diamond_ore")
    NETHER_GOLD_ORE = getItemType("nether_gold_ore")
    NETHER_QUARTZ_ORE = getItemType("nether_quartz_ore")
    ANCIENT_DEBRIS = getItemType("ancient_debris")
    COAL_BLOCK = getItemType("coal_block")
    RAW_IRON_BLOCK = getItemType("raw_iron_block")
    RAW_COPPER_BLOCK = getItemType("raw_copper_block")
    RAW_GOLD_BLOCK = getItemType("raw_gold_block")
    HEAVY_CORE = getItemType("heavy_core")
    AMETHYST_BLOCK = getItemType("amethyst_block")
    BUDDING_AMETHYST = getItemType("budding_amethyst")
    IRON_BLOCK = getItemType("iron_block")
    COPPER_BLOCK = getItemType("copper_block")
    GOLD_BLOCK = getItemType("gold_block")
    DIAMOND_BLOCK = getItemType("diamond_block")
    NETHERITE_BLOCK = getItemType("netherite_block")
    EXPOSED_COPPER = getItemType("exposed_copper")
    WEATHERED_COPPER = getItemType("weathered_copper")
    OXIDIZED_COPPER = getItemType("oxidized_copper")
    CHISELED_COPPER = getItemType("chiseled_copper")
    EXPOSED_CHISELED_COPPER = getItemType("exposed_chiseled_copper")
    WEATHERED_CHISELED_COPPER = getItemType("weathered_chiseled_copper")
    OXIDIZED_CHISELED_COPPER = getItemType("oxidized_chiseled_copper")
    CUT_COPPER = getItemType("cut_copper")
    EXPOSED_CUT_COPPER = getItemType("exposed_cut_copper")
    WEATHERED_CUT_COPPER = getItemType("weathered_cut_copper")
    OXIDIZED_CUT_COPPER = getItemType("oxidized_cut_copper")
    CUT_COPPER_STAIRS = getItemType("cut_copper_stairs")
    EXPOSED_CUT_COPPER_STAIRS = getItemType("exposed_cut_copper_stairs")
    WEATHERED_CUT_COPPER_STAIRS = getItemType("weathered_cut_copper_stairs")
    OXIDIZED_CUT_COPPER_STAIRS = getItemType("oxidized_cut_copper_stairs")
    CUT_COPPER_SLAB = getItemType("cut_copper_slab")
    EXPOSED_CUT_COPPER_SLAB = getItemType("exposed_cut_copper_slab")
    WEATHERED_CUT_COPPER_SLAB = getItemType("weathered_cut_copper_slab")
    OXIDIZED_CUT_COPPER_SLAB = getItemType("oxidized_cut_copper_slab")
    WAXED_COPPER_BLOCK = getItemType("waxed_copper_block")
    WAXED_EXPOSED_COPPER = getItemType("waxed_exposed_copper")
    WAXED_WEATHERED_COPPER = getItemType("waxed_weathered_copper")
    WAXED_OXIDIZED_COPPER = getItemType("waxed_oxidized_copper")
    WAXED_CHISELED_COPPER = getItemType("waxed_chiseled_copper")
    WAXED_EXPOSED_CHISELED_COPPER = getItemType("waxed_exposed_chiseled_copper")
    WAXED_WEATHERED_CHISELED_COPPER = getItemType("waxed_weathered_chiseled_copper")
    WAXED_OXIDIZED_CHISELED_COPPER = getItemType("waxed_oxidized_chiseled_copper")
    WAXED_CUT_COPPER = getItemType("waxed_cut_copper")
    WAXED_EXPOSED_CUT_COPPER = getItemType("waxed_exposed_cut_copper")
    WAXED_WEATHERED_CUT_COPPER = getItemType("waxed_weathered_cut_copper")
    WAXED_OXIDIZED_CUT_COPPER = getItemType("waxed_oxidized_cut_copper")
    WAXED_CUT_COPPER_STAIRS = getItemType("waxed_cut_copper_stairs")
    WAXED_EXPOSED_CUT_COPPER_STAIRS = getItemType("waxed_exposed_cut_copper_stairs")
    WAXED_WEATHERED_CUT_COPPER_STAIRS = getItemType("waxed_weathered_cut_copper_stairs")
    WAXED_OXIDIZED_CUT_COPPER_STAIRS = getItemType("waxed_oxidized_cut_copper_stairs")
    WAXED_CUT_COPPER_SLAB = getItemType("waxed_cut_copper_slab")
    WAXED_EXPOSED_CUT_COPPER_SLAB = getItemType("waxed_exposed_cut_copper_slab")
    WAXED_WEATHERED_CUT_COPPER_SLAB = getItemType("waxed_weathered_cut_copper_slab")
    WAXED_OXIDIZED_CUT_COPPER_SLAB = getItemType("waxed_oxidized_cut_copper_slab")
    OAK_LOG = getItemType("oak_log")
    SPRUCE_LOG = getItemType("spruce_log")
    BIRCH_LOG = getItemType("birch_log")
    JUNGLE_LOG = getItemType("jungle_log")
    ACACIA_LOG = getItemType("acacia_log")
    CHERRY_LOG = getItemType("cherry_log")
    DARK_OAK_LOG = getItemType("dark_oak_log")
    MANGROVE_LOG = getItemType("mangrove_log")
    MANGROVE_ROOTS = getItemType("mangrove_roots")
    MUDDY_MANGROVE_ROOTS = getItemType("muddy_mangrove_roots")
    CRIMSON_STEM = getItemType("crimson_stem")
    WARPED_STEM = getItemType("warped_stem")
    BAMBOO_BLOCK = getItemType("bamboo_block")
    STRIPPED_OAK_LOG = getItemType("stripped_oak_log")
    STRIPPED_SPRUCE_LOG = getItemType("stripped_spruce_log")
    STRIPPED_BIRCH_LOG = getItemType("stripped_birch_log")
    STRIPPED_JUNGLE_LOG = getItemType("stripped_jungle_log")
    STRIPPED_ACACIA_LOG = getItemType("stripped_acacia_log")
    STRIPPED_CHERRY_LOG = getItemType("stripped_cherry_log")
    STRIPPED_DARK_OAK_LOG = getItemType("stripped_dark_oak_log")
    STRIPPED_MANGROVE_LOG = getItemType("stripped_mangrove_log")
    STRIPPED_CRIMSON_STEM = getItemType("stripped_crimson_stem")
    STRIPPED_WARPED_STEM = getItemType("stripped_warped_stem")
    STRIPPED_OAK_WOOD = getItemType("stripped_oak_wood")
    STRIPPED_SPRUCE_WOOD = getItemType("stripped_spruce_wood")
    STRIPPED_BIRCH_WOOD = getItemType("stripped_birch_wood")
    STRIPPED_JUNGLE_WOOD = getItemType("stripped_jungle_wood")
    STRIPPED_ACACIA_WOOD = getItemType("stripped_acacia_wood")
    STRIPPED_CHERRY_WOOD = getItemType("stripped_cherry_wood")
    STRIPPED_DARK_OAK_WOOD = getItemType("stripped_dark_oak_wood")
    STRIPPED_MANGROVE_WOOD = getItemType("stripped_mangrove_wood")
    STRIPPED_CRIMSON_HYPHAE = getItemType("stripped_crimson_hyphae")
    STRIPPED_WARPED_HYPHAE = getItemType("stripped_warped_hyphae")
    STRIPPED_BAMBOO_BLOCK = getItemType("stripped_bamboo_block")
    OAK_WOOD = getItemType("oak_wood")
    SPRUCE_WOOD = getItemType("spruce_wood")
    BIRCH_WOOD = getItemType("birch_wood")
    JUNGLE_WOOD = getItemType("jungle_wood")
    ACACIA_WOOD = getItemType("acacia_wood")
    CHERRY_WOOD = getItemType("cherry_wood")
    DARK_OAK_WOOD = getItemType("dark_oak_wood")
    MANGROVE_WOOD = getItemType("mangrove_wood")
    CRIMSON_HYPHAE = getItemType("crimson_hyphae")
    WARPED_HYPHAE = getItemType("warped_hyphae")
    OAK_LEAVES = getItemType("oak_leaves")
    SPRUCE_LEAVES = getItemType("spruce_leaves")
    BIRCH_LEAVES = getItemType("birch_leaves")
    JUNGLE_LEAVES = getItemType("jungle_leaves")
    ACACIA_LEAVES = getItemType("acacia_leaves")
    CHERRY_LEAVES = getItemType("cherry_leaves")
    DARK_OAK_LEAVES = getItemType("dark_oak_leaves")
    MANGROVE_LEAVES = getItemType("mangrove_leaves")
    AZALEA_LEAVES = getItemType("azalea_leaves")
    FLOWERING_AZALEA_LEAVES = getItemType("flowering_azalea_leaves")
    SPONGE = getItemType("sponge")
    WET_SPONGE = getItemType("wet_sponge")
    GLASS = getItemType("glass")
    TINTED_GLASS = getItemType("tinted_glass")
    LAPIS_BLOCK = getItemType("lapis_block")
    SANDSTONE = getItemType("sandstone")
    CHISELED_SANDSTONE = getItemType("chiseled_sandstone")
    CUT_SANDSTONE = getItemType("cut_sandstone")
    COBWEB = getItemType("cobweb")
    SHORT_GRASS = getItemType("short_grass")
    FERN = getItemType("fern")
    AZALEA = getItemType("azalea")
    FLOWERING_AZALEA = getItemType("flowering_azalea")
    DEAD_BUSH = getItemType("dead_bush")
    SEAGRASS = getItemType("seagrass")
    SEA_PICKLE = getItemType("sea_pickle")
    WHITE_WOOL = getItemType("white_wool")
    ORANGE_WOOL = getItemType("orange_wool")
    MAGENTA_WOOL = getItemType("magenta_wool")
    LIGHT_BLUE_WOOL = getItemType("light_blue_wool")
    YELLOW_WOOL = getItemType("yellow_wool")
    LIME_WOOL = getItemType("lime_wool")
    PINK_WOOL = getItemType("pink_wool")
    GRAY_WOOL = getItemType("gray_wool")
    LIGHT_GRAY_WOOL = getItemType("light_gray_wool")
    CYAN_WOOL = getItemType("cyan_wool")
    PURPLE_WOOL = getItemType("purple_wool")
    BLUE_WOOL = getItemType("blue_wool")
    BROWN_WOOL = getItemType("brown_wool")
    GREEN_WOOL = getItemType("green_wool")
    RED_WOOL = getItemType("red_wool")
    BLACK_WOOL = getItemType("black_wool")
    DANDELION = getItemType("dandelion")
    POPPY = getItemType("poppy")
    BLUE_ORCHID = getItemType("blue_orchid")
    ALLIUM = getItemType("allium")
    AZURE_BLUET = getItemType("azure_bluet")
    RED_TULIP = getItemType("red_tulip")
    ORANGE_TULIP = getItemType("orange_tulip")
    WHITE_TULIP = getItemType("white_tulip")
    PINK_TULIP = getItemType("pink_tulip")
    OXEYE_DAISY = getItemType("oxeye_daisy")
    CORNFLOWER = getItemType("cornflower")
    LILY_OF_THE_VALLEY = getItemType("lily_of_the_valley")
    WITHER_ROSE = getItemType("wither_rose")
    TORCHFLOWER = getItemType("torchflower")
    PITCHER_PLANT = getItemType("pitcher_plant")
    SPORE_BLOSSOM = getItemType("spore_blossom")
    BROWN_MUSHROOM = getItemType("brown_mushroom")
    RED_MUSHROOM = getItemType("red_mushroom")
    CRIMSON_FUNGUS = getItemType("crimson_fungus")
    WARPED_FUNGUS = getItemType("warped_fungus")
    CRIMSON_ROOTS = getItemType("crimson_roots")
    WARPED_ROOTS = getItemType("warped_roots")
    NETHER_SPROUTS = getItemType("nether_sprouts")
    WEEPING_VINES = getItemType("weeping_vines")
    TWISTING_VINES = getItemType("twisting_vines")
    SUGAR_CANE = getItemType("sugar_cane")
    KELP = getItemType("kelp")
    MOSS_CARPET = getItemType("moss_carpet")
    PINK_PETALS = getItemType("pink_petals")
    MOSS_BLOCK = getItemType("moss_block")
    HANGING_ROOTS = getItemType("hanging_roots")
    BIG_DRIPLEAF = getItemType("big_dripleaf")
    SMALL_DRIPLEAF = getItemType("small_dripleaf")
    BAMBOO = getItemType("bamboo")
    OAK_SLAB = getItemType("oak_slab")
    SPRUCE_SLAB = getItemType("spruce_slab")
    BIRCH_SLAB = getItemType("birch_slab")
    JUNGLE_SLAB = getItemType("jungle_slab")
    ACACIA_SLAB = getItemType("acacia_slab")
    CHERRY_SLAB = getItemType("cherry_slab")
    DARK_OAK_SLAB = getItemType("dark_oak_slab")
    MANGROVE_SLAB = getItemType("mangrove_slab")
    BAMBOO_SLAB = getItemType("bamboo_slab")
    BAMBOO_MOSAIC_SLAB = getItemType("bamboo_mosaic_slab")
    CRIMSON_SLAB = getItemType("crimson_slab")
    WARPED_SLAB = getItemType("warped_slab")
    STONE_SLAB = getItemType("stone_slab")
    SMOOTH_STONE_SLAB = getItemType("smooth_stone_slab")
    SANDSTONE_SLAB = getItemType("sandstone_slab")
    CUT_SANDSTONE_SLAB = getItemType("cut_sandstone_slab")
    PETRIFIED_OAK_SLAB = getItemType("petrified_oak_slab")
    COBBLESTONE_SLAB = getItemType("cobblestone_slab")
    BRICK_SLAB = getItemType("brick_slab")
    STONE_BRICK_SLAB = getItemType("stone_brick_slab")
    MUD_BRICK_SLAB = getItemType("mud_brick_slab")
    NETHER_BRICK_SLAB = getItemType("nether_brick_slab")
    QUARTZ_SLAB = getItemType("quartz_slab")
    RED_SANDSTONE_SLAB = getItemType("red_sandstone_slab")
    CUT_RED_SANDSTONE_SLAB = getItemType("cut_red_sandstone_slab")
    PURPUR_SLAB = getItemType("purpur_slab")
    PRISMARINE_SLAB = getItemType("prismarine_slab")
    PRISMARINE_BRICK_SLAB = getItemType("prismarine_brick_slab")
    DARK_PRISMARINE_SLAB = getItemType("dark_prismarine_slab")
    SMOOTH_QUARTZ = getItemType("smooth_quartz")
    SMOOTH_RED_SANDSTONE = getItemType("smooth_red_sandstone")
    SMOOTH_SANDSTONE = getItemType("smooth_sandstone")
    SMOOTH_STONE = getItemType("smooth_stone")
    BRICKS = getItemType("bricks")
    BOOKSHELF = getItemType("bookshelf")
    CHISELED_BOOKSHELF = getItemType("chiseled_bookshelf")
    """
    ItemMeta: BlockStateMeta
    """
    DECORATED_POT = getItemType("decorated_pot")
    """
    ItemMeta: BlockStateMeta
    """
    MOSSY_COBBLESTONE = getItemType("mossy_cobblestone")
    OBSIDIAN = getItemType("obsidian")
    TORCH = getItemType("torch")
    END_ROD = getItemType("end_rod")
    CHORUS_PLANT = getItemType("chorus_plant")
    CHORUS_FLOWER = getItemType("chorus_flower")
    PURPUR_BLOCK = getItemType("purpur_block")
    PURPUR_PILLAR = getItemType("purpur_pillar")
    PURPUR_STAIRS = getItemType("purpur_stairs")
    SPAWNER = getItemType("spawner")
    """
    ItemMeta: BlockStateMeta
    """
    CHEST = getItemType("chest")
    """
    ItemMeta: BlockStateMeta
    """
    CRAFTING_TABLE = getItemType("crafting_table")
    FARMLAND = getItemType("farmland")
    FURNACE = getItemType("furnace")
    """
    ItemMeta: BlockStateMeta
    """
    LADDER = getItemType("ladder")
    COBBLESTONE_STAIRS = getItemType("cobblestone_stairs")
    SNOW = getItemType("snow")
    ICE = getItemType("ice")
    SNOW_BLOCK = getItemType("snow_block")
    CACTUS = getItemType("cactus")
    CLAY = getItemType("clay")
    JUKEBOX = getItemType("jukebox")
    """
    ItemMeta: BlockStateMeta
    """
    OAK_FENCE = getItemType("oak_fence")
    SPRUCE_FENCE = getItemType("spruce_fence")
    BIRCH_FENCE = getItemType("birch_fence")
    JUNGLE_FENCE = getItemType("jungle_fence")
    ACACIA_FENCE = getItemType("acacia_fence")
    CHERRY_FENCE = getItemType("cherry_fence")
    DARK_OAK_FENCE = getItemType("dark_oak_fence")
    MANGROVE_FENCE = getItemType("mangrove_fence")
    BAMBOO_FENCE = getItemType("bamboo_fence")
    CRIMSON_FENCE = getItemType("crimson_fence")
    WARPED_FENCE = getItemType("warped_fence")
    PUMPKIN = getItemType("pumpkin")
    CARVED_PUMPKIN = getItemType("carved_pumpkin")
    JACK_O_LANTERN = getItemType("jack_o_lantern")
    NETHERRACK = getItemType("netherrack")
    SOUL_SAND = getItemType("soul_sand")
    SOUL_SOIL = getItemType("soul_soil")
    BASALT = getItemType("basalt")
    POLISHED_BASALT = getItemType("polished_basalt")
    SMOOTH_BASALT = getItemType("smooth_basalt")
    SOUL_TORCH = getItemType("soul_torch")
    GLOWSTONE = getItemType("glowstone")
    INFESTED_STONE = getItemType("infested_stone")
    INFESTED_COBBLESTONE = getItemType("infested_cobblestone")
    INFESTED_STONE_BRICKS = getItemType("infested_stone_bricks")
    INFESTED_MOSSY_STONE_BRICKS = getItemType("infested_mossy_stone_bricks")
    INFESTED_CRACKED_STONE_BRICKS = getItemType("infested_cracked_stone_bricks")
    INFESTED_CHISELED_STONE_BRICKS = getItemType("infested_chiseled_stone_bricks")
    INFESTED_DEEPSLATE = getItemType("infested_deepslate")
    STONE_BRICKS = getItemType("stone_bricks")
    MOSSY_STONE_BRICKS = getItemType("mossy_stone_bricks")
    CRACKED_STONE_BRICKS = getItemType("cracked_stone_bricks")
    CHISELED_STONE_BRICKS = getItemType("chiseled_stone_bricks")
    PACKED_MUD = getItemType("packed_mud")
    MUD_BRICKS = getItemType("mud_bricks")
    DEEPSLATE_BRICKS = getItemType("deepslate_bricks")
    CRACKED_DEEPSLATE_BRICKS = getItemType("cracked_deepslate_bricks")
    DEEPSLATE_TILES = getItemType("deepslate_tiles")
    CRACKED_DEEPSLATE_TILES = getItemType("cracked_deepslate_tiles")
    CHISELED_DEEPSLATE = getItemType("chiseled_deepslate")
    REINFORCED_DEEPSLATE = getItemType("reinforced_deepslate")
    BROWN_MUSHROOM_BLOCK = getItemType("brown_mushroom_block")
    RED_MUSHROOM_BLOCK = getItemType("red_mushroom_block")
    MUSHROOM_STEM = getItemType("mushroom_stem")
    IRON_BARS = getItemType("iron_bars")
    CHAIN = getItemType("chain")
    GLASS_PANE = getItemType("glass_pane")
    MELON = getItemType("melon")
    VINE = getItemType("vine")
    GLOW_LICHEN = getItemType("glow_lichen")
    BRICK_STAIRS = getItemType("brick_stairs")
    STONE_BRICK_STAIRS = getItemType("stone_brick_stairs")
    MUD_BRICK_STAIRS = getItemType("mud_brick_stairs")
    MYCELIUM = getItemType("mycelium")
    LILY_PAD = getItemType("lily_pad")
    NETHER_BRICKS = getItemType("nether_bricks")
    CRACKED_NETHER_BRICKS = getItemType("cracked_nether_bricks")
    CHISELED_NETHER_BRICKS = getItemType("chiseled_nether_bricks")
    NETHER_BRICK_FENCE = getItemType("nether_brick_fence")
    NETHER_BRICK_STAIRS = getItemType("nether_brick_stairs")
    SCULK = getItemType("sculk")
    SCULK_VEIN = getItemType("sculk_vein")
    SCULK_CATALYST = getItemType("sculk_catalyst")
    """
    ItemMeta: BlockStateMeta
    """
    SCULK_SHRIEKER = getItemType("sculk_shrieker")
    """
    ItemMeta: BlockStateMeta
    """
    ENCHANTING_TABLE = getItemType("enchanting_table")
    """
    ItemMeta: BlockStateMeta
    """
    END_PORTAL_FRAME = getItemType("end_portal_frame")
    END_STONE = getItemType("end_stone")
    END_STONE_BRICKS = getItemType("end_stone_bricks")
    DRAGON_EGG = getItemType("dragon_egg")
    SANDSTONE_STAIRS = getItemType("sandstone_stairs")
    ENDER_CHEST = getItemType("ender_chest")
    """
    ItemMeta: BlockStateMeta
    """
    EMERALD_BLOCK = getItemType("emerald_block")
    OAK_STAIRS = getItemType("oak_stairs")
    SPRUCE_STAIRS = getItemType("spruce_stairs")
    BIRCH_STAIRS = getItemType("birch_stairs")
    JUNGLE_STAIRS = getItemType("jungle_stairs")
    ACACIA_STAIRS = getItemType("acacia_stairs")
    CHERRY_STAIRS = getItemType("cherry_stairs")
    DARK_OAK_STAIRS = getItemType("dark_oak_stairs")
    MANGROVE_STAIRS = getItemType("mangrove_stairs")
    BAMBOO_STAIRS = getItemType("bamboo_stairs")
    BAMBOO_MOSAIC_STAIRS = getItemType("bamboo_mosaic_stairs")
    CRIMSON_STAIRS = getItemType("crimson_stairs")
    WARPED_STAIRS = getItemType("warped_stairs")
    COMMAND_BLOCK = getItemType("command_block")
    """
    ItemMeta: BlockStateMeta
    """
    BEACON = getItemType("beacon")
    """
    ItemMeta: BlockStateMeta
    """
    COBBLESTONE_WALL = getItemType("cobblestone_wall")
    MOSSY_COBBLESTONE_WALL = getItemType("mossy_cobblestone_wall")
    BRICK_WALL = getItemType("brick_wall")
    PRISMARINE_WALL = getItemType("prismarine_wall")
    RED_SANDSTONE_WALL = getItemType("red_sandstone_wall")
    MOSSY_STONE_BRICK_WALL = getItemType("mossy_stone_brick_wall")
    GRANITE_WALL = getItemType("granite_wall")
    STONE_BRICK_WALL = getItemType("stone_brick_wall")
    MUD_BRICK_WALL = getItemType("mud_brick_wall")
    NETHER_BRICK_WALL = getItemType("nether_brick_wall")
    ANDESITE_WALL = getItemType("andesite_wall")
    RED_NETHER_BRICK_WALL = getItemType("red_nether_brick_wall")
    SANDSTONE_WALL = getItemType("sandstone_wall")
    END_STONE_BRICK_WALL = getItemType("end_stone_brick_wall")
    DIORITE_WALL = getItemType("diorite_wall")
    BLACKSTONE_WALL = getItemType("blackstone_wall")
    POLISHED_BLACKSTONE_WALL = getItemType("polished_blackstone_wall")
    POLISHED_BLACKSTONE_BRICK_WALL = getItemType("polished_blackstone_brick_wall")
    COBBLED_DEEPSLATE_WALL = getItemType("cobbled_deepslate_wall")
    POLISHED_DEEPSLATE_WALL = getItemType("polished_deepslate_wall")
    DEEPSLATE_BRICK_WALL = getItemType("deepslate_brick_wall")
    DEEPSLATE_TILE_WALL = getItemType("deepslate_tile_wall")
    ANVIL = getItemType("anvil")
    CHIPPED_ANVIL = getItemType("chipped_anvil")
    DAMAGED_ANVIL = getItemType("damaged_anvil")
    CHISELED_QUARTZ_BLOCK = getItemType("chiseled_quartz_block")
    QUARTZ_BLOCK = getItemType("quartz_block")
    QUARTZ_BRICKS = getItemType("quartz_bricks")
    QUARTZ_PILLAR = getItemType("quartz_pillar")
    QUARTZ_STAIRS = getItemType("quartz_stairs")
    WHITE_TERRACOTTA = getItemType("white_terracotta")
    ORANGE_TERRACOTTA = getItemType("orange_terracotta")
    MAGENTA_TERRACOTTA = getItemType("magenta_terracotta")
    LIGHT_BLUE_TERRACOTTA = getItemType("light_blue_terracotta")
    YELLOW_TERRACOTTA = getItemType("yellow_terracotta")
    LIME_TERRACOTTA = getItemType("lime_terracotta")
    PINK_TERRACOTTA = getItemType("pink_terracotta")
    GRAY_TERRACOTTA = getItemType("gray_terracotta")
    LIGHT_GRAY_TERRACOTTA = getItemType("light_gray_terracotta")
    CYAN_TERRACOTTA = getItemType("cyan_terracotta")
    PURPLE_TERRACOTTA = getItemType("purple_terracotta")
    BLUE_TERRACOTTA = getItemType("blue_terracotta")
    BROWN_TERRACOTTA = getItemType("brown_terracotta")
    GREEN_TERRACOTTA = getItemType("green_terracotta")
    RED_TERRACOTTA = getItemType("red_terracotta")
    BLACK_TERRACOTTA = getItemType("black_terracotta")
    BARRIER = getItemType("barrier")
    LIGHT = getItemType("light")
    HAY_BLOCK = getItemType("hay_block")
    WHITE_CARPET = getItemType("white_carpet")
    ORANGE_CARPET = getItemType("orange_carpet")
    MAGENTA_CARPET = getItemType("magenta_carpet")
    LIGHT_BLUE_CARPET = getItemType("light_blue_carpet")
    YELLOW_CARPET = getItemType("yellow_carpet")
    LIME_CARPET = getItemType("lime_carpet")
    PINK_CARPET = getItemType("pink_carpet")
    GRAY_CARPET = getItemType("gray_carpet")
    LIGHT_GRAY_CARPET = getItemType("light_gray_carpet")
    CYAN_CARPET = getItemType("cyan_carpet")
    PURPLE_CARPET = getItemType("purple_carpet")
    BLUE_CARPET = getItemType("blue_carpet")
    BROWN_CARPET = getItemType("brown_carpet")
    GREEN_CARPET = getItemType("green_carpet")
    RED_CARPET = getItemType("red_carpet")
    BLACK_CARPET = getItemType("black_carpet")
    TERRACOTTA = getItemType("terracotta")
    PACKED_ICE = getItemType("packed_ice")
    DIRT_PATH = getItemType("dirt_path")
    SUNFLOWER = getItemType("sunflower")
    LILAC = getItemType("lilac")
    ROSE_BUSH = getItemType("rose_bush")
    PEONY = getItemType("peony")
    TALL_GRASS = getItemType("tall_grass")
    LARGE_FERN = getItemType("large_fern")
    WHITE_STAINED_GLASS = getItemType("white_stained_glass")
    ORANGE_STAINED_GLASS = getItemType("orange_stained_glass")
    MAGENTA_STAINED_GLASS = getItemType("magenta_stained_glass")
    LIGHT_BLUE_STAINED_GLASS = getItemType("light_blue_stained_glass")
    YELLOW_STAINED_GLASS = getItemType("yellow_stained_glass")
    LIME_STAINED_GLASS = getItemType("lime_stained_glass")
    PINK_STAINED_GLASS = getItemType("pink_stained_glass")
    GRAY_STAINED_GLASS = getItemType("gray_stained_glass")
    LIGHT_GRAY_STAINED_GLASS = getItemType("light_gray_stained_glass")
    CYAN_STAINED_GLASS = getItemType("cyan_stained_glass")
    PURPLE_STAINED_GLASS = getItemType("purple_stained_glass")
    BLUE_STAINED_GLASS = getItemType("blue_stained_glass")
    BROWN_STAINED_GLASS = getItemType("brown_stained_glass")
    GREEN_STAINED_GLASS = getItemType("green_stained_glass")
    RED_STAINED_GLASS = getItemType("red_stained_glass")
    BLACK_STAINED_GLASS = getItemType("black_stained_glass")
    WHITE_STAINED_GLASS_PANE = getItemType("white_stained_glass_pane")
    ORANGE_STAINED_GLASS_PANE = getItemType("orange_stained_glass_pane")
    MAGENTA_STAINED_GLASS_PANE = getItemType("magenta_stained_glass_pane")
    LIGHT_BLUE_STAINED_GLASS_PANE = getItemType("light_blue_stained_glass_pane")
    YELLOW_STAINED_GLASS_PANE = getItemType("yellow_stained_glass_pane")
    LIME_STAINED_GLASS_PANE = getItemType("lime_stained_glass_pane")
    PINK_STAINED_GLASS_PANE = getItemType("pink_stained_glass_pane")
    GRAY_STAINED_GLASS_PANE = getItemType("gray_stained_glass_pane")
    LIGHT_GRAY_STAINED_GLASS_PANE = getItemType("light_gray_stained_glass_pane")
    CYAN_STAINED_GLASS_PANE = getItemType("cyan_stained_glass_pane")
    PURPLE_STAINED_GLASS_PANE = getItemType("purple_stained_glass_pane")
    BLUE_STAINED_GLASS_PANE = getItemType("blue_stained_glass_pane")
    BROWN_STAINED_GLASS_PANE = getItemType("brown_stained_glass_pane")
    GREEN_STAINED_GLASS_PANE = getItemType("green_stained_glass_pane")
    RED_STAINED_GLASS_PANE = getItemType("red_stained_glass_pane")
    BLACK_STAINED_GLASS_PANE = getItemType("black_stained_glass_pane")
    PRISMARINE = getItemType("prismarine")
    PRISMARINE_BRICKS = getItemType("prismarine_bricks")
    DARK_PRISMARINE = getItemType("dark_prismarine")
    PRISMARINE_STAIRS = getItemType("prismarine_stairs")
    PRISMARINE_BRICK_STAIRS = getItemType("prismarine_brick_stairs")
    DARK_PRISMARINE_STAIRS = getItemType("dark_prismarine_stairs")
    SEA_LANTERN = getItemType("sea_lantern")
    RED_SANDSTONE = getItemType("red_sandstone")
    CHISELED_RED_SANDSTONE = getItemType("chiseled_red_sandstone")
    CUT_RED_SANDSTONE = getItemType("cut_red_sandstone")
    RED_SANDSTONE_STAIRS = getItemType("red_sandstone_stairs")
    REPEATING_COMMAND_BLOCK = getItemType("repeating_command_block")
    """
    ItemMeta: BlockStateMeta
    """
    CHAIN_COMMAND_BLOCK = getItemType("chain_command_block")
    """
    ItemMeta: BlockStateMeta
    """
    MAGMA_BLOCK = getItemType("magma_block")
    NETHER_WART_BLOCK = getItemType("nether_wart_block")
    WARPED_WART_BLOCK = getItemType("warped_wart_block")
    RED_NETHER_BRICKS = getItemType("red_nether_bricks")
    BONE_BLOCK = getItemType("bone_block")
    STRUCTURE_VOID = getItemType("structure_void")
    SHULKER_BOX = getItemType("shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    WHITE_SHULKER_BOX = getItemType("white_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    ORANGE_SHULKER_BOX = getItemType("orange_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    MAGENTA_SHULKER_BOX = getItemType("magenta_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    LIGHT_BLUE_SHULKER_BOX = getItemType("light_blue_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    YELLOW_SHULKER_BOX = getItemType("yellow_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    LIME_SHULKER_BOX = getItemType("lime_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    PINK_SHULKER_BOX = getItemType("pink_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    GRAY_SHULKER_BOX = getItemType("gray_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    LIGHT_GRAY_SHULKER_BOX = getItemType("light_gray_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    CYAN_SHULKER_BOX = getItemType("cyan_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    PURPLE_SHULKER_BOX = getItemType("purple_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    BLUE_SHULKER_BOX = getItemType("blue_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    BROWN_SHULKER_BOX = getItemType("brown_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    GREEN_SHULKER_BOX = getItemType("green_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    RED_SHULKER_BOX = getItemType("red_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    BLACK_SHULKER_BOX = getItemType("black_shulker_box")
    """
    ItemMeta: BlockStateMeta
    """
    WHITE_GLAZED_TERRACOTTA = getItemType("white_glazed_terracotta")
    ORANGE_GLAZED_TERRACOTTA = getItemType("orange_glazed_terracotta")
    MAGENTA_GLAZED_TERRACOTTA = getItemType("magenta_glazed_terracotta")
    LIGHT_BLUE_GLAZED_TERRACOTTA = getItemType("light_blue_glazed_terracotta")
    YELLOW_GLAZED_TERRACOTTA = getItemType("yellow_glazed_terracotta")
    LIME_GLAZED_TERRACOTTA = getItemType("lime_glazed_terracotta")
    PINK_GLAZED_TERRACOTTA = getItemType("pink_glazed_terracotta")
    GRAY_GLAZED_TERRACOTTA = getItemType("gray_glazed_terracotta")
    LIGHT_GRAY_GLAZED_TERRACOTTA = getItemType("light_gray_glazed_terracotta")
    CYAN_GLAZED_TERRACOTTA = getItemType("cyan_glazed_terracotta")
    PURPLE_GLAZED_TERRACOTTA = getItemType("purple_glazed_terracotta")
    BLUE_GLAZED_TERRACOTTA = getItemType("blue_glazed_terracotta")
    BROWN_GLAZED_TERRACOTTA = getItemType("brown_glazed_terracotta")
    GREEN_GLAZED_TERRACOTTA = getItemType("green_glazed_terracotta")
    RED_GLAZED_TERRACOTTA = getItemType("red_glazed_terracotta")
    BLACK_GLAZED_TERRACOTTA = getItemType("black_glazed_terracotta")
    WHITE_CONCRETE = getItemType("white_concrete")
    ORANGE_CONCRETE = getItemType("orange_concrete")
    MAGENTA_CONCRETE = getItemType("magenta_concrete")
    LIGHT_BLUE_CONCRETE = getItemType("light_blue_concrete")
    YELLOW_CONCRETE = getItemType("yellow_concrete")
    LIME_CONCRETE = getItemType("lime_concrete")
    PINK_CONCRETE = getItemType("pink_concrete")
    GRAY_CONCRETE = getItemType("gray_concrete")
    LIGHT_GRAY_CONCRETE = getItemType("light_gray_concrete")
    CYAN_CONCRETE = getItemType("cyan_concrete")
    PURPLE_CONCRETE = getItemType("purple_concrete")
    BLUE_CONCRETE = getItemType("blue_concrete")
    BROWN_CONCRETE = getItemType("brown_concrete")
    GREEN_CONCRETE = getItemType("green_concrete")
    RED_CONCRETE = getItemType("red_concrete")
    BLACK_CONCRETE = getItemType("black_concrete")
    WHITE_CONCRETE_POWDER = getItemType("white_concrete_powder")
    ORANGE_CONCRETE_POWDER = getItemType("orange_concrete_powder")
    MAGENTA_CONCRETE_POWDER = getItemType("magenta_concrete_powder")
    LIGHT_BLUE_CONCRETE_POWDER = getItemType("light_blue_concrete_powder")
    YELLOW_CONCRETE_POWDER = getItemType("yellow_concrete_powder")
    LIME_CONCRETE_POWDER = getItemType("lime_concrete_powder")
    PINK_CONCRETE_POWDER = getItemType("pink_concrete_powder")
    GRAY_CONCRETE_POWDER = getItemType("gray_concrete_powder")
    LIGHT_GRAY_CONCRETE_POWDER = getItemType("light_gray_concrete_powder")
    CYAN_CONCRETE_POWDER = getItemType("cyan_concrete_powder")
    PURPLE_CONCRETE_POWDER = getItemType("purple_concrete_powder")
    BLUE_CONCRETE_POWDER = getItemType("blue_concrete_powder")
    BROWN_CONCRETE_POWDER = getItemType("brown_concrete_powder")
    GREEN_CONCRETE_POWDER = getItemType("green_concrete_powder")
    RED_CONCRETE_POWDER = getItemType("red_concrete_powder")
    BLACK_CONCRETE_POWDER = getItemType("black_concrete_powder")
    TURTLE_EGG = getItemType("turtle_egg")
    SNIFFER_EGG = getItemType("sniffer_egg")
    DEAD_TUBE_CORAL_BLOCK = getItemType("dead_tube_coral_block")
    DEAD_BRAIN_CORAL_BLOCK = getItemType("dead_brain_coral_block")
    DEAD_BUBBLE_CORAL_BLOCK = getItemType("dead_bubble_coral_block")
    DEAD_FIRE_CORAL_BLOCK = getItemType("dead_fire_coral_block")
    DEAD_HORN_CORAL_BLOCK = getItemType("dead_horn_coral_block")
    TUBE_CORAL_BLOCK = getItemType("tube_coral_block")
    BRAIN_CORAL_BLOCK = getItemType("brain_coral_block")
    BUBBLE_CORAL_BLOCK = getItemType("bubble_coral_block")
    FIRE_CORAL_BLOCK = getItemType("fire_coral_block")
    HORN_CORAL_BLOCK = getItemType("horn_coral_block")
    TUBE_CORAL = getItemType("tube_coral")
    BRAIN_CORAL = getItemType("brain_coral")
    BUBBLE_CORAL = getItemType("bubble_coral")
    FIRE_CORAL = getItemType("fire_coral")
    HORN_CORAL = getItemType("horn_coral")
    DEAD_BRAIN_CORAL = getItemType("dead_brain_coral")
    DEAD_BUBBLE_CORAL = getItemType("dead_bubble_coral")
    DEAD_FIRE_CORAL = getItemType("dead_fire_coral")
    DEAD_HORN_CORAL = getItemType("dead_horn_coral")
    DEAD_TUBE_CORAL = getItemType("dead_tube_coral")
    TUBE_CORAL_FAN = getItemType("tube_coral_fan")
    BRAIN_CORAL_FAN = getItemType("brain_coral_fan")
    BUBBLE_CORAL_FAN = getItemType("bubble_coral_fan")
    FIRE_CORAL_FAN = getItemType("fire_coral_fan")
    HORN_CORAL_FAN = getItemType("horn_coral_fan")
    DEAD_TUBE_CORAL_FAN = getItemType("dead_tube_coral_fan")
    DEAD_BRAIN_CORAL_FAN = getItemType("dead_brain_coral_fan")
    DEAD_BUBBLE_CORAL_FAN = getItemType("dead_bubble_coral_fan")
    DEAD_FIRE_CORAL_FAN = getItemType("dead_fire_coral_fan")
    DEAD_HORN_CORAL_FAN = getItemType("dead_horn_coral_fan")
    BLUE_ICE = getItemType("blue_ice")
    CONDUIT = getItemType("conduit")
    POLISHED_GRANITE_STAIRS = getItemType("polished_granite_stairs")
    SMOOTH_RED_SANDSTONE_STAIRS = getItemType("smooth_red_sandstone_stairs")
    MOSSY_STONE_BRICK_STAIRS = getItemType("mossy_stone_brick_stairs")
    POLISHED_DIORITE_STAIRS = getItemType("polished_diorite_stairs")
    MOSSY_COBBLESTONE_STAIRS = getItemType("mossy_cobblestone_stairs")
    END_STONE_BRICK_STAIRS = getItemType("end_stone_brick_stairs")
    STONE_STAIRS = getItemType("stone_stairs")
    SMOOTH_SANDSTONE_STAIRS = getItemType("smooth_sandstone_stairs")
    SMOOTH_QUARTZ_STAIRS = getItemType("smooth_quartz_stairs")
    GRANITE_STAIRS = getItemType("granite_stairs")
    ANDESITE_STAIRS = getItemType("andesite_stairs")
    RED_NETHER_BRICK_STAIRS = getItemType("red_nether_brick_stairs")
    POLISHED_ANDESITE_STAIRS = getItemType("polished_andesite_stairs")
    DIORITE_STAIRS = getItemType("diorite_stairs")
    COBBLED_DEEPSLATE_STAIRS = getItemType("cobbled_deepslate_stairs")
    POLISHED_DEEPSLATE_STAIRS = getItemType("polished_deepslate_stairs")
    DEEPSLATE_BRICK_STAIRS = getItemType("deepslate_brick_stairs")
    DEEPSLATE_TILE_STAIRS = getItemType("deepslate_tile_stairs")
    POLISHED_GRANITE_SLAB = getItemType("polished_granite_slab")
    SMOOTH_RED_SANDSTONE_SLAB = getItemType("smooth_red_sandstone_slab")
    MOSSY_STONE_BRICK_SLAB = getItemType("mossy_stone_brick_slab")
    POLISHED_DIORITE_SLAB = getItemType("polished_diorite_slab")
    MOSSY_COBBLESTONE_SLAB = getItemType("mossy_cobblestone_slab")
    END_STONE_BRICK_SLAB = getItemType("end_stone_brick_slab")
    SMOOTH_SANDSTONE_SLAB = getItemType("smooth_sandstone_slab")
    SMOOTH_QUARTZ_SLAB = getItemType("smooth_quartz_slab")
    GRANITE_SLAB = getItemType("granite_slab")
    ANDESITE_SLAB = getItemType("andesite_slab")
    RED_NETHER_BRICK_SLAB = getItemType("red_nether_brick_slab")
    POLISHED_ANDESITE_SLAB = getItemType("polished_andesite_slab")
    DIORITE_SLAB = getItemType("diorite_slab")
    COBBLED_DEEPSLATE_SLAB = getItemType("cobbled_deepslate_slab")
    POLISHED_DEEPSLATE_SLAB = getItemType("polished_deepslate_slab")
    DEEPSLATE_BRICK_SLAB = getItemType("deepslate_brick_slab")
    DEEPSLATE_TILE_SLAB = getItemType("deepslate_tile_slab")
    SCAFFOLDING = getItemType("scaffolding")
    REDSTONE = getItemType("redstone")
    REDSTONE_TORCH = getItemType("redstone_torch")
    REDSTONE_BLOCK = getItemType("redstone_block")
    REPEATER = getItemType("repeater")
    COMPARATOR = getItemType("comparator")
    """
    ItemMeta: BlockStateMeta
    """
    PISTON = getItemType("piston")
    STICKY_PISTON = getItemType("sticky_piston")
    SLIME_BLOCK = getItemType("slime_block")
    HONEY_BLOCK = getItemType("honey_block")
    OBSERVER = getItemType("observer")
    HOPPER = getItemType("hopper")
    """
    ItemMeta: BlockStateMeta
    """
    DISPENSER = getItemType("dispenser")
    """
    ItemMeta: BlockStateMeta
    """
    DROPPER = getItemType("dropper")
    """
    ItemMeta: BlockStateMeta
    """
    LECTERN = getItemType("lectern")
    """
    ItemMeta: BlockStateMeta
    """
    TARGET = getItemType("target")
    LEVER = getItemType("lever")
    LIGHTNING_ROD = getItemType("lightning_rod")
    DAYLIGHT_DETECTOR = getItemType("daylight_detector")
    """
    ItemMeta: BlockStateMeta
    """
    SCULK_SENSOR = getItemType("sculk_sensor")
    """
    ItemMeta: BlockStateMeta
    """
    CALIBRATED_SCULK_SENSOR = getItemType("calibrated_sculk_sensor")
    """
    ItemMeta: BlockStateMeta
    """
    TRIPWIRE_HOOK = getItemType("tripwire_hook")
    TRAPPED_CHEST = getItemType("trapped_chest")
    """
    ItemMeta: BlockStateMeta
    """
    TNT = getItemType("tnt")
    REDSTONE_LAMP = getItemType("redstone_lamp")
    NOTE_BLOCK = getItemType("note_block")
    STONE_BUTTON = getItemType("stone_button")
    POLISHED_BLACKSTONE_BUTTON = getItemType("polished_blackstone_button")
    OAK_BUTTON = getItemType("oak_button")
    SPRUCE_BUTTON = getItemType("spruce_button")
    BIRCH_BUTTON = getItemType("birch_button")
    JUNGLE_BUTTON = getItemType("jungle_button")
    ACACIA_BUTTON = getItemType("acacia_button")
    CHERRY_BUTTON = getItemType("cherry_button")
    DARK_OAK_BUTTON = getItemType("dark_oak_button")
    MANGROVE_BUTTON = getItemType("mangrove_button")
    BAMBOO_BUTTON = getItemType("bamboo_button")
    CRIMSON_BUTTON = getItemType("crimson_button")
    WARPED_BUTTON = getItemType("warped_button")
    STONE_PRESSURE_PLATE = getItemType("stone_pressure_plate")
    POLISHED_BLACKSTONE_PRESSURE_PLATE = getItemType("polished_blackstone_pressure_plate")
    LIGHT_WEIGHTED_PRESSURE_PLATE = getItemType("light_weighted_pressure_plate")
    HEAVY_WEIGHTED_PRESSURE_PLATE = getItemType("heavy_weighted_pressure_plate")
    OAK_PRESSURE_PLATE = getItemType("oak_pressure_plate")
    SPRUCE_PRESSURE_PLATE = getItemType("spruce_pressure_plate")
    BIRCH_PRESSURE_PLATE = getItemType("birch_pressure_plate")
    JUNGLE_PRESSURE_PLATE = getItemType("jungle_pressure_plate")
    ACACIA_PRESSURE_PLATE = getItemType("acacia_pressure_plate")
    CHERRY_PRESSURE_PLATE = getItemType("cherry_pressure_plate")
    DARK_OAK_PRESSURE_PLATE = getItemType("dark_oak_pressure_plate")
    MANGROVE_PRESSURE_PLATE = getItemType("mangrove_pressure_plate")
    BAMBOO_PRESSURE_PLATE = getItemType("bamboo_pressure_plate")
    CRIMSON_PRESSURE_PLATE = getItemType("crimson_pressure_plate")
    WARPED_PRESSURE_PLATE = getItemType("warped_pressure_plate")
    IRON_DOOR = getItemType("iron_door")
    OAK_DOOR = getItemType("oak_door")
    SPRUCE_DOOR = getItemType("spruce_door")
    BIRCH_DOOR = getItemType("birch_door")
    JUNGLE_DOOR = getItemType("jungle_door")
    ACACIA_DOOR = getItemType("acacia_door")
    CHERRY_DOOR = getItemType("cherry_door")
    DARK_OAK_DOOR = getItemType("dark_oak_door")
    MANGROVE_DOOR = getItemType("mangrove_door")
    BAMBOO_DOOR = getItemType("bamboo_door")
    CRIMSON_DOOR = getItemType("crimson_door")
    WARPED_DOOR = getItemType("warped_door")
    COPPER_DOOR = getItemType("copper_door")
    EXPOSED_COPPER_DOOR = getItemType("exposed_copper_door")
    WEATHERED_COPPER_DOOR = getItemType("weathered_copper_door")
    OXIDIZED_COPPER_DOOR = getItemType("oxidized_copper_door")
    WAXED_COPPER_DOOR = getItemType("waxed_copper_door")
    WAXED_EXPOSED_COPPER_DOOR = getItemType("waxed_exposed_copper_door")
    WAXED_WEATHERED_COPPER_DOOR = getItemType("waxed_weathered_copper_door")
    WAXED_OXIDIZED_COPPER_DOOR = getItemType("waxed_oxidized_copper_door")
    IRON_TRAPDOOR = getItemType("iron_trapdoor")
    OAK_TRAPDOOR = getItemType("oak_trapdoor")
    SPRUCE_TRAPDOOR = getItemType("spruce_trapdoor")
    BIRCH_TRAPDOOR = getItemType("birch_trapdoor")
    JUNGLE_TRAPDOOR = getItemType("jungle_trapdoor")
    ACACIA_TRAPDOOR = getItemType("acacia_trapdoor")
    CHERRY_TRAPDOOR = getItemType("cherry_trapdoor")
    DARK_OAK_TRAPDOOR = getItemType("dark_oak_trapdoor")
    MANGROVE_TRAPDOOR = getItemType("mangrove_trapdoor")
    BAMBOO_TRAPDOOR = getItemType("bamboo_trapdoor")
    CRIMSON_TRAPDOOR = getItemType("crimson_trapdoor")
    WARPED_TRAPDOOR = getItemType("warped_trapdoor")
    COPPER_TRAPDOOR = getItemType("copper_trapdoor")
    EXPOSED_COPPER_TRAPDOOR = getItemType("exposed_copper_trapdoor")
    WEATHERED_COPPER_TRAPDOOR = getItemType("weathered_copper_trapdoor")
    OXIDIZED_COPPER_TRAPDOOR = getItemType("oxidized_copper_trapdoor")
    WAXED_COPPER_TRAPDOOR = getItemType("waxed_copper_trapdoor")
    WAXED_EXPOSED_COPPER_TRAPDOOR = getItemType("waxed_exposed_copper_trapdoor")
    WAXED_WEATHERED_COPPER_TRAPDOOR = getItemType("waxed_weathered_copper_trapdoor")
    WAXED_OXIDIZED_COPPER_TRAPDOOR = getItemType("waxed_oxidized_copper_trapdoor")
    OAK_FENCE_GATE = getItemType("oak_fence_gate")
    SPRUCE_FENCE_GATE = getItemType("spruce_fence_gate")
    BIRCH_FENCE_GATE = getItemType("birch_fence_gate")
    JUNGLE_FENCE_GATE = getItemType("jungle_fence_gate")
    ACACIA_FENCE_GATE = getItemType("acacia_fence_gate")
    CHERRY_FENCE_GATE = getItemType("cherry_fence_gate")
    DARK_OAK_FENCE_GATE = getItemType("dark_oak_fence_gate")
    MANGROVE_FENCE_GATE = getItemType("mangrove_fence_gate")
    BAMBOO_FENCE_GATE = getItemType("bamboo_fence_gate")
    CRIMSON_FENCE_GATE = getItemType("crimson_fence_gate")
    WARPED_FENCE_GATE = getItemType("warped_fence_gate")
    POWERED_RAIL = getItemType("powered_rail")
    DETECTOR_RAIL = getItemType("detector_rail")
    RAIL = getItemType("rail")
    ACTIVATOR_RAIL = getItemType("activator_rail")
    SADDLE = getItemType("saddle")
    MINECART = getItemType("minecart")
    CHEST_MINECART = getItemType("chest_minecart")
    FURNACE_MINECART = getItemType("furnace_minecart")
    TNT_MINECART = getItemType("tnt_minecart")
    HOPPER_MINECART = getItemType("hopper_minecart")
    CARROT_ON_A_STICK = getItemType("carrot_on_a_stick")
    WARPED_FUNGUS_ON_A_STICK = getItemType("warped_fungus_on_a_stick")
    ELYTRA = getItemType("elytra")
    OAK_BOAT = getItemType("oak_boat")
    OAK_CHEST_BOAT = getItemType("oak_chest_boat")
    SPRUCE_BOAT = getItemType("spruce_boat")
    SPRUCE_CHEST_BOAT = getItemType("spruce_chest_boat")
    BIRCH_BOAT = getItemType("birch_boat")
    BIRCH_CHEST_BOAT = getItemType("birch_chest_boat")
    JUNGLE_BOAT = getItemType("jungle_boat")
    JUNGLE_CHEST_BOAT = getItemType("jungle_chest_boat")
    ACACIA_BOAT = getItemType("acacia_boat")
    ACACIA_CHEST_BOAT = getItemType("acacia_chest_boat")
    CHERRY_BOAT = getItemType("cherry_boat")
    CHERRY_CHEST_BOAT = getItemType("cherry_chest_boat")
    DARK_OAK_BOAT = getItemType("dark_oak_boat")
    DARK_OAK_CHEST_BOAT = getItemType("dark_oak_chest_boat")
    MANGROVE_BOAT = getItemType("mangrove_boat")
    MANGROVE_CHEST_BOAT = getItemType("mangrove_chest_boat")
    BAMBOO_RAFT = getItemType("bamboo_raft")
    BAMBOO_CHEST_RAFT = getItemType("bamboo_chest_raft")
    STRUCTURE_BLOCK = getItemType("structure_block")
    """
    ItemMeta: BlockStateMeta
    """
    JIGSAW = getItemType("jigsaw")
    """
    ItemMeta: BlockStateMeta
    """
    TURTLE_HELMET = getItemType("turtle_helmet")
    """
    ItemMeta: ArmorMeta
    """
    TURTLE_SCUTE = getItemType("turtle_scute")
    ARMADILLO_SCUTE = getItemType("armadillo_scute")
    WOLF_ARMOR = getItemType("wolf_armor")
    """
    ItemMeta: ColorableArmorMeta
    """
    FLINT_AND_STEEL = getItemType("flint_and_steel")
    BOWL = getItemType("bowl")
    APPLE = getItemType("apple")
    BOW = getItemType("bow")
    ARROW = getItemType("arrow")
    COAL = getItemType("coal")
    CHARCOAL = getItemType("charcoal")
    DIAMOND = getItemType("diamond")
    EMERALD = getItemType("emerald")
    LAPIS_LAZULI = getItemType("lapis_lazuli")
    QUARTZ = getItemType("quartz")
    AMETHYST_SHARD = getItemType("amethyst_shard")
    RAW_IRON = getItemType("raw_iron")
    IRON_INGOT = getItemType("iron_ingot")
    RAW_COPPER = getItemType("raw_copper")
    COPPER_INGOT = getItemType("copper_ingot")
    RAW_GOLD = getItemType("raw_gold")
    GOLD_INGOT = getItemType("gold_ingot")
    NETHERITE_INGOT = getItemType("netherite_ingot")
    NETHERITE_SCRAP = getItemType("netherite_scrap")
    WOODEN_SWORD = getItemType("wooden_sword")
    WOODEN_SHOVEL = getItemType("wooden_shovel")
    WOODEN_PICKAXE = getItemType("wooden_pickaxe")
    WOODEN_AXE = getItemType("wooden_axe")
    WOODEN_HOE = getItemType("wooden_hoe")
    STONE_SWORD = getItemType("stone_sword")
    STONE_SHOVEL = getItemType("stone_shovel")
    STONE_PICKAXE = getItemType("stone_pickaxe")
    STONE_AXE = getItemType("stone_axe")
    STONE_HOE = getItemType("stone_hoe")
    GOLDEN_SWORD = getItemType("golden_sword")
    GOLDEN_SHOVEL = getItemType("golden_shovel")
    GOLDEN_PICKAXE = getItemType("golden_pickaxe")
    GOLDEN_AXE = getItemType("golden_axe")
    GOLDEN_HOE = getItemType("golden_hoe")
    IRON_SWORD = getItemType("iron_sword")
    IRON_SHOVEL = getItemType("iron_shovel")
    IRON_PICKAXE = getItemType("iron_pickaxe")
    IRON_AXE = getItemType("iron_axe")
    IRON_HOE = getItemType("iron_hoe")
    DIAMOND_SWORD = getItemType("diamond_sword")
    DIAMOND_SHOVEL = getItemType("diamond_shovel")
    DIAMOND_PICKAXE = getItemType("diamond_pickaxe")
    DIAMOND_AXE = getItemType("diamond_axe")
    DIAMOND_HOE = getItemType("diamond_hoe")
    NETHERITE_SWORD = getItemType("netherite_sword")
    NETHERITE_SHOVEL = getItemType("netherite_shovel")
    NETHERITE_PICKAXE = getItemType("netherite_pickaxe")
    NETHERITE_AXE = getItemType("netherite_axe")
    NETHERITE_HOE = getItemType("netherite_hoe")
    STICK = getItemType("stick")
    MUSHROOM_STEW = getItemType("mushroom_stew")
    STRING = getItemType("string")
    FEATHER = getItemType("feather")
    GUNPOWDER = getItemType("gunpowder")
    WHEAT_SEEDS = getItemType("wheat_seeds")
    WHEAT = getItemType("wheat")
    BREAD = getItemType("bread")
    LEATHER_HELMET = getItemType("leather_helmet")
    """
    ItemMeta: ColorableArmorMeta
    """
    LEATHER_CHESTPLATE = getItemType("leather_chestplate")
    """
    ItemMeta: ColorableArmorMeta
    """
    LEATHER_LEGGINGS = getItemType("leather_leggings")
    """
    ItemMeta: ColorableArmorMeta
    """
    LEATHER_BOOTS = getItemType("leather_boots")
    """
    ItemMeta: ColorableArmorMeta
    """
    CHAINMAIL_HELMET = getItemType("chainmail_helmet")
    """
    ItemMeta: ArmorMeta
    """
    CHAINMAIL_CHESTPLATE = getItemType("chainmail_chestplate")
    """
    ItemMeta: ArmorMeta
    """
    CHAINMAIL_LEGGINGS = getItemType("chainmail_leggings")
    """
    ItemMeta: ArmorMeta
    """
    CHAINMAIL_BOOTS = getItemType("chainmail_boots")
    """
    ItemMeta: ArmorMeta
    """
    IRON_HELMET = getItemType("iron_helmet")
    """
    ItemMeta: ArmorMeta
    """
    IRON_CHESTPLATE = getItemType("iron_chestplate")
    """
    ItemMeta: ArmorMeta
    """
    IRON_LEGGINGS = getItemType("iron_leggings")
    """
    ItemMeta: ArmorMeta
    """
    IRON_BOOTS = getItemType("iron_boots")
    """
    ItemMeta: ArmorMeta
    """
    DIAMOND_HELMET = getItemType("diamond_helmet")
    """
    ItemMeta: ArmorMeta
    """
    DIAMOND_CHESTPLATE = getItemType("diamond_chestplate")
    """
    ItemMeta: ArmorMeta
    """
    DIAMOND_LEGGINGS = getItemType("diamond_leggings")
    """
    ItemMeta: ArmorMeta
    """
    DIAMOND_BOOTS = getItemType("diamond_boots")
    """
    ItemMeta: ArmorMeta
    """
    GOLDEN_HELMET = getItemType("golden_helmet")
    """
    ItemMeta: ArmorMeta
    """
    GOLDEN_CHESTPLATE = getItemType("golden_chestplate")
    """
    ItemMeta: ArmorMeta
    """
    GOLDEN_LEGGINGS = getItemType("golden_leggings")
    """
    ItemMeta: ArmorMeta
    """
    GOLDEN_BOOTS = getItemType("golden_boots")
    """
    ItemMeta: ArmorMeta
    """
    NETHERITE_HELMET = getItemType("netherite_helmet")
    """
    ItemMeta: ArmorMeta
    """
    NETHERITE_CHESTPLATE = getItemType("netherite_chestplate")
    """
    ItemMeta: ArmorMeta
    """
    NETHERITE_LEGGINGS = getItemType("netherite_leggings")
    """
    ItemMeta: ArmorMeta
    """
    NETHERITE_BOOTS = getItemType("netherite_boots")
    """
    ItemMeta: ArmorMeta
    """
    FLINT = getItemType("flint")
    PORKCHOP = getItemType("porkchop")
    COOKED_PORKCHOP = getItemType("cooked_porkchop")
    PAINTING = getItemType("painting")
    GOLDEN_APPLE = getItemType("golden_apple")
    ENCHANTED_GOLDEN_APPLE = getItemType("enchanted_golden_apple")
    OAK_SIGN = getItemType("oak_sign")
    """
    ItemMeta: BlockStateMeta
    """
    SPRUCE_SIGN = getItemType("spruce_sign")
    """
    ItemMeta: BlockStateMeta
    """
    BIRCH_SIGN = getItemType("birch_sign")
    """
    ItemMeta: BlockStateMeta
    """
    JUNGLE_SIGN = getItemType("jungle_sign")
    """
    ItemMeta: BlockStateMeta
    """
    ACACIA_SIGN = getItemType("acacia_sign")
    """
    ItemMeta: BlockStateMeta
    """
    CHERRY_SIGN = getItemType("cherry_sign")
    """
    ItemMeta: BlockStateMeta
    """
    DARK_OAK_SIGN = getItemType("dark_oak_sign")
    """
    ItemMeta: BlockStateMeta
    """
    MANGROVE_SIGN = getItemType("mangrove_sign")
    """
    ItemMeta: BlockStateMeta
    """
    BAMBOO_SIGN = getItemType("bamboo_sign")
    """
    ItemMeta: BlockStateMeta
    """
    CRIMSON_SIGN = getItemType("crimson_sign")
    """
    ItemMeta: BlockStateMeta
    """
    WARPED_SIGN = getItemType("warped_sign")
    """
    ItemMeta: BlockStateMeta
    """
    OAK_HANGING_SIGN = getItemType("oak_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    SPRUCE_HANGING_SIGN = getItemType("spruce_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    BIRCH_HANGING_SIGN = getItemType("birch_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    JUNGLE_HANGING_SIGN = getItemType("jungle_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    ACACIA_HANGING_SIGN = getItemType("acacia_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    CHERRY_HANGING_SIGN = getItemType("cherry_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    DARK_OAK_HANGING_SIGN = getItemType("dark_oak_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    MANGROVE_HANGING_SIGN = getItemType("mangrove_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    BAMBOO_HANGING_SIGN = getItemType("bamboo_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    CRIMSON_HANGING_SIGN = getItemType("crimson_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    WARPED_HANGING_SIGN = getItemType("warped_hanging_sign")
    """
    ItemMeta: BlockStateMeta
    """
    BUCKET = getItemType("bucket")
    WATER_BUCKET = getItemType("water_bucket")
    LAVA_BUCKET = getItemType("lava_bucket")
    POWDER_SNOW_BUCKET = getItemType("powder_snow_bucket")
    SNOWBALL = getItemType("snowball")
    LEATHER = getItemType("leather")
    MILK_BUCKET = getItemType("milk_bucket")
    PUFFERFISH_BUCKET = getItemType("pufferfish_bucket")
    SALMON_BUCKET = getItemType("salmon_bucket")
    COD_BUCKET = getItemType("cod_bucket")
    TROPICAL_FISH_BUCKET = getItemType("tropical_fish_bucket")
    """
    ItemMeta: TropicalFishBucketMeta
    """
    AXOLOTL_BUCKET = getItemType("axolotl_bucket")
    """
    ItemMeta: AxolotlBucketMeta
    """
    TADPOLE_BUCKET = getItemType("tadpole_bucket")
    BRICK = getItemType("brick")
    CLAY_BALL = getItemType("clay_ball")
    DRIED_KELP_BLOCK = getItemType("dried_kelp_block")
    PAPER = getItemType("paper")
    BOOK = getItemType("book")
    SLIME_BALL = getItemType("slime_ball")
    EGG = getItemType("egg")
    COMPASS = getItemType("compass")
    """
    ItemMeta: CompassMeta
    """
    RECOVERY_COMPASS = getItemType("recovery_compass")
    BUNDLE = getItemType("bundle")
    """
    ItemMeta: BundleMeta
    """
    FISHING_ROD = getItemType("fishing_rod")
    CLOCK = getItemType("clock")
    SPYGLASS = getItemType("spyglass")
    GLOWSTONE_DUST = getItemType("glowstone_dust")
    COD = getItemType("cod")
    SALMON = getItemType("salmon")
    TROPICAL_FISH = getItemType("tropical_fish")
    PUFFERFISH = getItemType("pufferfish")
    COOKED_COD = getItemType("cooked_cod")
    COOKED_SALMON = getItemType("cooked_salmon")
    INK_SAC = getItemType("ink_sac")
    GLOW_INK_SAC = getItemType("glow_ink_sac")
    COCOA_BEANS = getItemType("cocoa_beans")
    WHITE_DYE = getItemType("white_dye")
    ORANGE_DYE = getItemType("orange_dye")
    MAGENTA_DYE = getItemType("magenta_dye")
    LIGHT_BLUE_DYE = getItemType("light_blue_dye")
    YELLOW_DYE = getItemType("yellow_dye")
    LIME_DYE = getItemType("lime_dye")
    PINK_DYE = getItemType("pink_dye")
    GRAY_DYE = getItemType("gray_dye")
    LIGHT_GRAY_DYE = getItemType("light_gray_dye")
    CYAN_DYE = getItemType("cyan_dye")
    PURPLE_DYE = getItemType("purple_dye")
    BLUE_DYE = getItemType("blue_dye")
    BROWN_DYE = getItemType("brown_dye")
    GREEN_DYE = getItemType("green_dye")
    RED_DYE = getItemType("red_dye")
    BLACK_DYE = getItemType("black_dye")
    BONE_MEAL = getItemType("bone_meal")
    BONE = getItemType("bone")
    SUGAR = getItemType("sugar")
    CAKE = getItemType("cake")
    WHITE_BED = getItemType("white_bed")
    ORANGE_BED = getItemType("orange_bed")
    MAGENTA_BED = getItemType("magenta_bed")
    LIGHT_BLUE_BED = getItemType("light_blue_bed")
    YELLOW_BED = getItemType("yellow_bed")
    LIME_BED = getItemType("lime_bed")
    PINK_BED = getItemType("pink_bed")
    GRAY_BED = getItemType("gray_bed")
    LIGHT_GRAY_BED = getItemType("light_gray_bed")
    CYAN_BED = getItemType("cyan_bed")
    PURPLE_BED = getItemType("purple_bed")
    BLUE_BED = getItemType("blue_bed")
    BROWN_BED = getItemType("brown_bed")
    GREEN_BED = getItemType("green_bed")
    RED_BED = getItemType("red_bed")
    BLACK_BED = getItemType("black_bed")
    COOKIE = getItemType("cookie")
    CRAFTER = getItemType("crafter")
    """
    ItemMeta: BlockStateMeta
    """
    FILLED_MAP = getItemType("filled_map")
    """
    ItemMeta: MapMeta
    """
    SHEARS = getItemType("shears")
    MELON_SLICE = getItemType("melon_slice")
    DRIED_KELP = getItemType("dried_kelp")
    PUMPKIN_SEEDS = getItemType("pumpkin_seeds")
    MELON_SEEDS = getItemType("melon_seeds")
    BEEF = getItemType("beef")
    COOKED_BEEF = getItemType("cooked_beef")
    CHICKEN = getItemType("chicken")
    COOKED_CHICKEN = getItemType("cooked_chicken")
    ROTTEN_FLESH = getItemType("rotten_flesh")
    ENDER_PEARL = getItemType("ender_pearl")
    BLAZE_ROD = getItemType("blaze_rod")
    GHAST_TEAR = getItemType("ghast_tear")
    GOLD_NUGGET = getItemType("gold_nugget")
    NETHER_WART = getItemType("nether_wart")
    POTION = getItemType("potion")
    """
    ItemMeta: PotionMeta
    """
    GLASS_BOTTLE = getItemType("glass_bottle")
    SPIDER_EYE = getItemType("spider_eye")
    FERMENTED_SPIDER_EYE = getItemType("fermented_spider_eye")
    BLAZE_POWDER = getItemType("blaze_powder")
    MAGMA_CREAM = getItemType("magma_cream")
    BREWING_STAND = getItemType("brewing_stand")
    """
    ItemMeta: BlockStateMeta
    """
    CAULDRON = getItemType("cauldron")
    ENDER_EYE = getItemType("ender_eye")
    GLISTERING_MELON_SLICE = getItemType("glistering_melon_slice")
    ARMADILLO_SPAWN_EGG = getItemType("armadillo_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ALLAY_SPAWN_EGG = getItemType("allay_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    AXOLOTL_SPAWN_EGG = getItemType("axolotl_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    BAT_SPAWN_EGG = getItemType("bat_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    BEE_SPAWN_EGG = getItemType("bee_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    BLAZE_SPAWN_EGG = getItemType("blaze_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    BOGGED_SPAWN_EGG = getItemType("bogged_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    BREEZE_SPAWN_EGG = getItemType("breeze_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    CAT_SPAWN_EGG = getItemType("cat_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    CAMEL_SPAWN_EGG = getItemType("camel_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    CAVE_SPIDER_SPAWN_EGG = getItemType("cave_spider_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    CHICKEN_SPAWN_EGG = getItemType("chicken_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    COD_SPAWN_EGG = getItemType("cod_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    COW_SPAWN_EGG = getItemType("cow_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    CREEPER_SPAWN_EGG = getItemType("creeper_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    DOLPHIN_SPAWN_EGG = getItemType("dolphin_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    DONKEY_SPAWN_EGG = getItemType("donkey_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    DROWNED_SPAWN_EGG = getItemType("drowned_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ELDER_GUARDIAN_SPAWN_EGG = getItemType("elder_guardian_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ENDER_DRAGON_SPAWN_EGG = getItemType("ender_dragon_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ENDERMAN_SPAWN_EGG = getItemType("enderman_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ENDERMITE_SPAWN_EGG = getItemType("endermite_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    EVOKER_SPAWN_EGG = getItemType("evoker_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    FOX_SPAWN_EGG = getItemType("fox_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    FROG_SPAWN_EGG = getItemType("frog_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    GHAST_SPAWN_EGG = getItemType("ghast_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    GLOW_SQUID_SPAWN_EGG = getItemType("glow_squid_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    GOAT_SPAWN_EGG = getItemType("goat_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    GUARDIAN_SPAWN_EGG = getItemType("guardian_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    HOGLIN_SPAWN_EGG = getItemType("hoglin_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    HORSE_SPAWN_EGG = getItemType("horse_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    HUSK_SPAWN_EGG = getItemType("husk_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    IRON_GOLEM_SPAWN_EGG = getItemType("iron_golem_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    LLAMA_SPAWN_EGG = getItemType("llama_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    MAGMA_CUBE_SPAWN_EGG = getItemType("magma_cube_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    MOOSHROOM_SPAWN_EGG = getItemType("mooshroom_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    MULE_SPAWN_EGG = getItemType("mule_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    OCELOT_SPAWN_EGG = getItemType("ocelot_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PANDA_SPAWN_EGG = getItemType("panda_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PARROT_SPAWN_EGG = getItemType("parrot_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PHANTOM_SPAWN_EGG = getItemType("phantom_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PIG_SPAWN_EGG = getItemType("pig_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PIGLIN_SPAWN_EGG = getItemType("piglin_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PIGLIN_BRUTE_SPAWN_EGG = getItemType("piglin_brute_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PILLAGER_SPAWN_EGG = getItemType("pillager_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    POLAR_BEAR_SPAWN_EGG = getItemType("polar_bear_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    PUFFERFISH_SPAWN_EGG = getItemType("pufferfish_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    RABBIT_SPAWN_EGG = getItemType("rabbit_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    RAVAGER_SPAWN_EGG = getItemType("ravager_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SALMON_SPAWN_EGG = getItemType("salmon_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SHEEP_SPAWN_EGG = getItemType("sheep_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SHULKER_SPAWN_EGG = getItemType("shulker_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SILVERFISH_SPAWN_EGG = getItemType("silverfish_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SKELETON_SPAWN_EGG = getItemType("skeleton_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SKELETON_HORSE_SPAWN_EGG = getItemType("skeleton_horse_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SLIME_SPAWN_EGG = getItemType("slime_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SNIFFER_SPAWN_EGG = getItemType("sniffer_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SNOW_GOLEM_SPAWN_EGG = getItemType("snow_golem_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SPIDER_SPAWN_EGG = getItemType("spider_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    SQUID_SPAWN_EGG = getItemType("squid_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    STRAY_SPAWN_EGG = getItemType("stray_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    STRIDER_SPAWN_EGG = getItemType("strider_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    TADPOLE_SPAWN_EGG = getItemType("tadpole_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    TRADER_LLAMA_SPAWN_EGG = getItemType("trader_llama_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    TROPICAL_FISH_SPAWN_EGG = getItemType("tropical_fish_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    TURTLE_SPAWN_EGG = getItemType("turtle_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    VEX_SPAWN_EGG = getItemType("vex_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    VILLAGER_SPAWN_EGG = getItemType("villager_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    VINDICATOR_SPAWN_EGG = getItemType("vindicator_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WANDERING_TRADER_SPAWN_EGG = getItemType("wandering_trader_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WARDEN_SPAWN_EGG = getItemType("warden_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WITCH_SPAWN_EGG = getItemType("witch_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WITHER_SPAWN_EGG = getItemType("wither_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WITHER_SKELETON_SPAWN_EGG = getItemType("wither_skeleton_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    WOLF_SPAWN_EGG = getItemType("wolf_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ZOGLIN_SPAWN_EGG = getItemType("zoglin_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ZOMBIE_SPAWN_EGG = getItemType("zombie_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ZOMBIE_HORSE_SPAWN_EGG = getItemType("zombie_horse_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ZOMBIE_VILLAGER_SPAWN_EGG = getItemType("zombie_villager_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    ZOMBIFIED_PIGLIN_SPAWN_EGG = getItemType("zombified_piglin_spawn_egg")
    """
    ItemMeta: SpawnEggMeta
    """
    EXPERIENCE_BOTTLE = getItemType("experience_bottle")
    FIRE_CHARGE = getItemType("fire_charge")
    WIND_CHARGE = getItemType("wind_charge")
    WRITABLE_BOOK = getItemType("writable_book")
    """
    ItemMeta: BookMeta
    """
    WRITTEN_BOOK = getItemType("written_book")
    """
    ItemMeta: BookMeta
    """
    MACE = getItemType("mace")
    ITEM_FRAME = getItemType("item_frame")
    GLOW_ITEM_FRAME = getItemType("glow_item_frame")
    FLOWER_POT = getItemType("flower_pot")
    CARROT = getItemType("carrot")
    POTATO = getItemType("potato")
    BAKED_POTATO = getItemType("baked_potato")
    POISONOUS_POTATO = getItemType("poisonous_potato")
    MAP = getItemType("map")
    GOLDEN_CARROT = getItemType("golden_carrot")
    SKELETON_SKULL = getItemType("skeleton_skull")
    """
    ItemMeta: SkullMeta
    """
    WITHER_SKELETON_SKULL = getItemType("wither_skeleton_skull")
    """
    ItemMeta: SkullMeta
    """
    PLAYER_HEAD = getItemType("player_head")
    """
    ItemMeta: SkullMeta
    """
    ZOMBIE_HEAD = getItemType("zombie_head")
    """
    ItemMeta: SkullMeta
    """
    CREEPER_HEAD = getItemType("creeper_head")
    """
    ItemMeta: SkullMeta
    """
    DRAGON_HEAD = getItemType("dragon_head")
    """
    ItemMeta: SkullMeta
    """
    PIGLIN_HEAD = getItemType("piglin_head")
    """
    ItemMeta: SkullMeta
    """
    NETHER_STAR = getItemType("nether_star")
    PUMPKIN_PIE = getItemType("pumpkin_pie")
    FIREWORK_ROCKET = getItemType("firework_rocket")
    """
    ItemMeta: FireworkMeta
    """
    FIREWORK_STAR = getItemType("firework_star")
    """
    ItemMeta: FireworkEffectMeta
    """
    ENCHANTED_BOOK = getItemType("enchanted_book")
    """
    ItemMeta: EnchantmentStorageMeta
    """
    NETHER_BRICK = getItemType("nether_brick")
    PRISMARINE_SHARD = getItemType("prismarine_shard")
    PRISMARINE_CRYSTALS = getItemType("prismarine_crystals")
    RABBIT = getItemType("rabbit")
    COOKED_RABBIT = getItemType("cooked_rabbit")
    RABBIT_STEW = getItemType("rabbit_stew")
    RABBIT_FOOT = getItemType("rabbit_foot")
    RABBIT_HIDE = getItemType("rabbit_hide")
    ARMOR_STAND = getItemType("armor_stand")
    IRON_HORSE_ARMOR = getItemType("iron_horse_armor")
    GOLDEN_HORSE_ARMOR = getItemType("golden_horse_armor")
    DIAMOND_HORSE_ARMOR = getItemType("diamond_horse_armor")
    LEATHER_HORSE_ARMOR = getItemType("leather_horse_armor")
    """
    ItemMeta: LeatherArmorMeta
    """
    LEAD = getItemType("lead")
    NAME_TAG = getItemType("name_tag")
    COMMAND_BLOCK_MINECART = getItemType("command_block_minecart")
    MUTTON = getItemType("mutton")
    COOKED_MUTTON = getItemType("cooked_mutton")
    WHITE_BANNER = getItemType("white_banner")
    """
    ItemMeta: BannerMeta
    """
    ORANGE_BANNER = getItemType("orange_banner")
    """
    ItemMeta: BannerMeta
    """
    MAGENTA_BANNER = getItemType("magenta_banner")
    """
    ItemMeta: BannerMeta
    """
    LIGHT_BLUE_BANNER = getItemType("light_blue_banner")
    """
    ItemMeta: BannerMeta
    """
    YELLOW_BANNER = getItemType("yellow_banner")
    """
    ItemMeta: BannerMeta
    """
    LIME_BANNER = getItemType("lime_banner")
    """
    ItemMeta: BannerMeta
    """
    PINK_BANNER = getItemType("pink_banner")
    """
    ItemMeta: BannerMeta
    """
    GRAY_BANNER = getItemType("gray_banner")
    """
    ItemMeta: BannerMeta
    """
    LIGHT_GRAY_BANNER = getItemType("light_gray_banner")
    """
    ItemMeta: BannerMeta
    """
    CYAN_BANNER = getItemType("cyan_banner")
    """
    ItemMeta: BannerMeta
    """
    PURPLE_BANNER = getItemType("purple_banner")
    """
    ItemMeta: BannerMeta
    """
    BLUE_BANNER = getItemType("blue_banner")
    """
    ItemMeta: BannerMeta
    """
    BROWN_BANNER = getItemType("brown_banner")
    """
    ItemMeta: BannerMeta
    """
    GREEN_BANNER = getItemType("green_banner")
    """
    ItemMeta: BannerMeta
    """
    RED_BANNER = getItemType("red_banner")
    """
    ItemMeta: BannerMeta
    """
    BLACK_BANNER = getItemType("black_banner")
    """
    ItemMeta: BannerMeta
    """
    END_CRYSTAL = getItemType("end_crystal")
    CHORUS_FRUIT = getItemType("chorus_fruit")
    POPPED_CHORUS_FRUIT = getItemType("popped_chorus_fruit")
    TORCHFLOWER_SEEDS = getItemType("torchflower_seeds")
    PITCHER_POD = getItemType("pitcher_pod")
    BEETROOT = getItemType("beetroot")
    BEETROOT_SEEDS = getItemType("beetroot_seeds")
    BEETROOT_SOUP = getItemType("beetroot_soup")
    DRAGON_BREATH = getItemType("dragon_breath")
    SPLASH_POTION = getItemType("splash_potion")
    """
    ItemMeta: PotionMeta
    """
    SPECTRAL_ARROW = getItemType("spectral_arrow")
    TIPPED_ARROW = getItemType("tipped_arrow")
    """
    ItemMeta: PotionMeta
    """
    LINGERING_POTION = getItemType("lingering_potion")
    """
    ItemMeta: PotionMeta
    """
    SHIELD = getItemType("shield")
    """
    ItemMeta: ShieldMeta
    """
    TOTEM_OF_UNDYING = getItemType("totem_of_undying")
    SHULKER_SHELL = getItemType("shulker_shell")
    IRON_NUGGET = getItemType("iron_nugget")
    KNOWLEDGE_BOOK = getItemType("knowledge_book")
    """
    ItemMeta: KnowledgeBookMeta
    """
    DEBUG_STICK = getItemType("debug_stick")
    MUSIC_DISC_13 = getItemType("music_disc_13")
    MUSIC_DISC_CAT = getItemType("music_disc_cat")
    MUSIC_DISC_BLOCKS = getItemType("music_disc_blocks")
    MUSIC_DISC_CHIRP = getItemType("music_disc_chirp")
    MUSIC_DISC_CREATOR = getItemType("music_disc_creator")
    MUSIC_DISC_CREATOR_MUSIC_BOX = getItemType("music_disc_creator_music_box")
    MUSIC_DISC_FAR = getItemType("music_disc_far")
    MUSIC_DISC_MALL = getItemType("music_disc_mall")
    MUSIC_DISC_MELLOHI = getItemType("music_disc_mellohi")
    MUSIC_DISC_STAL = getItemType("music_disc_stal")
    MUSIC_DISC_STRAD = getItemType("music_disc_strad")
    MUSIC_DISC_WARD = getItemType("music_disc_ward")
    MUSIC_DISC_11 = getItemType("music_disc_11")
    MUSIC_DISC_WAIT = getItemType("music_disc_wait")
    MUSIC_DISC_OTHERSIDE = getItemType("music_disc_otherside")
    MUSIC_DISC_RELIC = getItemType("music_disc_relic")
    MUSIC_DISC_5 = getItemType("music_disc_5")
    MUSIC_DISC_PIGSTEP = getItemType("music_disc_pigstep")
    MUSIC_DISC_PRECIPICE = getItemType("music_disc_precipice")
    DISC_FRAGMENT_5 = getItemType("disc_fragment_5")
    TRIDENT = getItemType("trident")
    PHANTOM_MEMBRANE = getItemType("phantom_membrane")
    NAUTILUS_SHELL = getItemType("nautilus_shell")
    HEART_OF_THE_SEA = getItemType("heart_of_the_sea")
    CROSSBOW = getItemType("crossbow")
    """
    ItemMeta: CrossbowMeta
    """
    SUSPICIOUS_STEW = getItemType("suspicious_stew")
    """
    ItemMeta: SuspiciousStewMeta
    """
    LOOM = getItemType("loom")
    FLOWER_BANNER_PATTERN = getItemType("flower_banner_pattern")
    CREEPER_BANNER_PATTERN = getItemType("creeper_banner_pattern")
    SKULL_BANNER_PATTERN = getItemType("skull_banner_pattern")
    MOJANG_BANNER_PATTERN = getItemType("mojang_banner_pattern")
    GLOBE_BANNER_PATTERN = getItemType("globe_banner_pattern")
    PIGLIN_BANNER_PATTERN = getItemType("piglin_banner_pattern")
    FLOW_BANNER_PATTERN = getItemType("flow_banner_pattern")
    GUSTER_BANNER_PATTERN = getItemType("guster_banner_pattern")
    GOAT_HORN = getItemType("goat_horn")
    """
    ItemMeta: MusicInstrumentMeta
    """
    COMPOSTER = getItemType("composter")
    BARREL = getItemType("barrel")
    """
    ItemMeta: BlockStateMeta
    """
    SMOKER = getItemType("smoker")
    """
    ItemMeta: BlockStateMeta
    """
    BLAST_FURNACE = getItemType("blast_furnace")
    """
    ItemMeta: BlockStateMeta
    """
    CARTOGRAPHY_TABLE = getItemType("cartography_table")
    FLETCHING_TABLE = getItemType("fletching_table")
    GRINDSTONE = getItemType("grindstone")
    SMITHING_TABLE = getItemType("smithing_table")
    STONECUTTER = getItemType("stonecutter")
    BELL = getItemType("bell")
    """
    ItemMeta: BlockStateMeta
    """
    LANTERN = getItemType("lantern")
    SOUL_LANTERN = getItemType("soul_lantern")
    SWEET_BERRIES = getItemType("sweet_berries")
    GLOW_BERRIES = getItemType("glow_berries")
    CAMPFIRE = getItemType("campfire")
    """
    ItemMeta: BlockStateMeta
    """
    SOUL_CAMPFIRE = getItemType("soul_campfire")
    """
    ItemMeta: BlockStateMeta
    """
    SHROOMLIGHT = getItemType("shroomlight")
    HONEYCOMB = getItemType("honeycomb")
    BEE_NEST = getItemType("bee_nest")
    """
    ItemMeta: BlockStateMeta
    """
    BEEHIVE = getItemType("beehive")
    """
    ItemMeta: BlockStateMeta
    """
    HONEY_BOTTLE = getItemType("honey_bottle")
    HONEYCOMB_BLOCK = getItemType("honeycomb_block")
    LODESTONE = getItemType("lodestone")
    CRYING_OBSIDIAN = getItemType("crying_obsidian")
    BLACKSTONE = getItemType("blackstone")
    BLACKSTONE_SLAB = getItemType("blackstone_slab")
    BLACKSTONE_STAIRS = getItemType("blackstone_stairs")
    GILDED_BLACKSTONE = getItemType("gilded_blackstone")
    POLISHED_BLACKSTONE = getItemType("polished_blackstone")
    POLISHED_BLACKSTONE_SLAB = getItemType("polished_blackstone_slab")
    POLISHED_BLACKSTONE_STAIRS = getItemType("polished_blackstone_stairs")
    CHISELED_POLISHED_BLACKSTONE = getItemType("chiseled_polished_blackstone")
    POLISHED_BLACKSTONE_BRICKS = getItemType("polished_blackstone_bricks")
    POLISHED_BLACKSTONE_BRICK_SLAB = getItemType("polished_blackstone_brick_slab")
    POLISHED_BLACKSTONE_BRICK_STAIRS = getItemType("polished_blackstone_brick_stairs")
    CRACKED_POLISHED_BLACKSTONE_BRICKS = getItemType("cracked_polished_blackstone_bricks")
    RESPAWN_ANCHOR = getItemType("respawn_anchor")
    CANDLE = getItemType("candle")
    WHITE_CANDLE = getItemType("white_candle")
    ORANGE_CANDLE = getItemType("orange_candle")
    MAGENTA_CANDLE = getItemType("magenta_candle")
    LIGHT_BLUE_CANDLE = getItemType("light_blue_candle")
    YELLOW_CANDLE = getItemType("yellow_candle")
    LIME_CANDLE = getItemType("lime_candle")
    PINK_CANDLE = getItemType("pink_candle")
    GRAY_CANDLE = getItemType("gray_candle")
    LIGHT_GRAY_CANDLE = getItemType("light_gray_candle")
    CYAN_CANDLE = getItemType("cyan_candle")
    PURPLE_CANDLE = getItemType("purple_candle")
    BLUE_CANDLE = getItemType("blue_candle")
    BROWN_CANDLE = getItemType("brown_candle")
    GREEN_CANDLE = getItemType("green_candle")
    RED_CANDLE = getItemType("red_candle")
    BLACK_CANDLE = getItemType("black_candle")
    SMALL_AMETHYST_BUD = getItemType("small_amethyst_bud")
    MEDIUM_AMETHYST_BUD = getItemType("medium_amethyst_bud")
    LARGE_AMETHYST_BUD = getItemType("large_amethyst_bud")
    AMETHYST_CLUSTER = getItemType("amethyst_cluster")
    POINTED_DRIPSTONE = getItemType("pointed_dripstone")
    OCHRE_FROGLIGHT = getItemType("ochre_froglight")
    VERDANT_FROGLIGHT = getItemType("verdant_froglight")
    PEARLESCENT_FROGLIGHT = getItemType("pearlescent_froglight")
    FROGSPAWN = getItemType("frogspawn")
    ECHO_SHARD = getItemType("echo_shard")
    BRUSH = getItemType("brush")
    NETHERITE_UPGRADE_SMITHING_TEMPLATE = getItemType("netherite_upgrade_smithing_template")
    SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("sentry_armor_trim_smithing_template")
    DUNE_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("dune_armor_trim_smithing_template")
    COAST_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("coast_armor_trim_smithing_template")
    WILD_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("wild_armor_trim_smithing_template")
    WARD_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("ward_armor_trim_smithing_template")
    EYE_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("eye_armor_trim_smithing_template")
    VEX_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("vex_armor_trim_smithing_template")
    TIDE_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("tide_armor_trim_smithing_template")
    SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("snout_armor_trim_smithing_template")
    RIB_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("rib_armor_trim_smithing_template")
    SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("spire_armor_trim_smithing_template")
    WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("wayfinder_armor_trim_smithing_template")
    SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("shaper_armor_trim_smithing_template")
    SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("silence_armor_trim_smithing_template")
    RAISER_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("raiser_armor_trim_smithing_template")
    HOST_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("host_armor_trim_smithing_template")
    FLOW_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("flow_armor_trim_smithing_template")
    BOLT_ARMOR_TRIM_SMITHING_TEMPLATE = getItemType("bolt_armor_trim_smithing_template")
    ANGLER_POTTERY_SHERD = getItemType("angler_pottery_sherd")
    ARCHER_POTTERY_SHERD = getItemType("archer_pottery_sherd")
    ARMS_UP_POTTERY_SHERD = getItemType("arms_up_pottery_sherd")
    BLADE_POTTERY_SHERD = getItemType("blade_pottery_sherd")
    BREWER_POTTERY_SHERD = getItemType("brewer_pottery_sherd")
    BURN_POTTERY_SHERD = getItemType("burn_pottery_sherd")
    DANGER_POTTERY_SHERD = getItemType("danger_pottery_sherd")
    EXPLORER_POTTERY_SHERD = getItemType("explorer_pottery_sherd")
    FLOW_POTTERY_SHERD = getItemType("flow_pottery_sherd")
    FRIEND_POTTERY_SHERD = getItemType("friend_pottery_sherd")
    GUSTER_POTTERY_SHERD = getItemType("guster_pottery_sherd")
    HEART_POTTERY_SHERD = getItemType("heart_pottery_sherd")
    HEARTBREAK_POTTERY_SHERD = getItemType("heartbreak_pottery_sherd")
    HOWL_POTTERY_SHERD = getItemType("howl_pottery_sherd")
    MINER_POTTERY_SHERD = getItemType("miner_pottery_sherd")
    MOURNER_POTTERY_SHERD = getItemType("mourner_pottery_sherd")
    PLENTY_POTTERY_SHERD = getItemType("plenty_pottery_sherd")
    PRIZE_POTTERY_SHERD = getItemType("prize_pottery_sherd")
    SCRAPE_POTTERY_SHERD = getItemType("scrape_pottery_sherd")
    SHEAF_POTTERY_SHERD = getItemType("sheaf_pottery_sherd")
    SHELTER_POTTERY_SHERD = getItemType("shelter_pottery_sherd")
    SKULL_POTTERY_SHERD = getItemType("skull_pottery_sherd")
    SNORT_POTTERY_SHERD = getItemType("snort_pottery_sherd")
    COPPER_GRATE = getItemType("copper_grate")
    EXPOSED_COPPER_GRATE = getItemType("exposed_copper_grate")
    WEATHERED_COPPER_GRATE = getItemType("weathered_copper_grate")
    OXIDIZED_COPPER_GRATE = getItemType("oxidized_copper_grate")
    WAXED_COPPER_GRATE = getItemType("waxed_copper_grate")
    WAXED_EXPOSED_COPPER_GRATE = getItemType("waxed_exposed_copper_grate")
    WAXED_WEATHERED_COPPER_GRATE = getItemType("waxed_weathered_copper_grate")
    WAXED_OXIDIZED_COPPER_GRATE = getItemType("waxed_oxidized_copper_grate")
    COPPER_BULB = getItemType("copper_bulb")
    EXPOSED_COPPER_BULB = getItemType("exposed_copper_bulb")
    WEATHERED_COPPER_BULB = getItemType("weathered_copper_bulb")
    OXIDIZED_COPPER_BULB = getItemType("oxidized_copper_bulb")
    WAXED_COPPER_BULB = getItemType("waxed_copper_bulb")
    WAXED_EXPOSED_COPPER_BULB = getItemType("waxed_exposed_copper_bulb")
    WAXED_WEATHERED_COPPER_BULB = getItemType("waxed_weathered_copper_bulb")
    WAXED_OXIDIZED_COPPER_BULB = getItemType("waxed_oxidized_copper_bulb")
    TRIAL_SPAWNER = getItemType("trial_spawner")
    """
    ItemMeta: BlockStateMeta
    """
    TRIAL_KEY = getItemType("trial_key")
    OMINOUS_TRIAL_KEY = getItemType("ominous_trial_key")
    VAULT = getItemType("vault")
    """
    ItemMeta: BlockStateMeta
    """
    OMINOUS_BOTTLE = getItemType("ominous_bottle")
    """
    ItemMeta: OminousBottleMeta
    """
    BREEZE_ROD = getItemType("breeze_rod")


    @staticmethod
    def getItemType(key: str) -> "M":
        ...


    def typed(self) -> "Typed"["ItemMeta"]:
        """
        Yields this item type as a typed version of itself with a plain ItemMeta representing it.

        Returns
        - the typed item type.
        """
        ...


    def typed(self, itemMetaType: type["M"]) -> "Typed"["M"]:
        """
        Yields this item type as a typed version of itself with a plain ItemMeta representing it.
        
        Type `<M>`: the generic type of the item meta to type this item type with.

        Arguments
        - itemMetaType: the class type of the ItemMeta to type this ItemType with.

        Returns
        - the typed item type.
        """
        ...


    def createItemStack(self) -> "ItemStack":
        """
        Constructs a new itemstack with this item type that has the amount 1.

        Returns
        - the constructed item stack.
        """
        ...


    def createItemStack(self, amount: int) -> "ItemStack":
        """
        Constructs a new itemstack with this item type.

        Arguments
        - amount: the amount of the item stack.

        Returns
        - the constructed item stack.
        """
        ...


    def hasBlockType(self) -> bool:
        """
        Returns True if this ItemType has a corresponding BlockType.

        Returns
        - True if there is a corresponding BlockType, otherwise False

        See
        - .getBlockType()
        """
        ...


    def getBlockType(self) -> "BlockType":
        """
        Returns the corresponding BlockType for the given ItemType.
        
        If there is no corresponding BlockType an error will be thrown.

        Returns
        - the corresponding BlockType

        See
        - .hasBlockType()
        """
        ...


    def getItemMetaClass(self) -> type["ItemMeta"]:
        """
        Gets the ItemMeta class of this ItemType

        Returns
        - the ItemMeta class of this ItemType
        """
        ...


    def getMaxStackSize(self) -> int:
        """
        Gets the maximum amount of this item type that can be held in a stack

        Returns
        - Maximum stack size for this item type
        """
        ...


    def getMaxDurability(self) -> int:
        """
        Gets the maximum durability of this item type

        Returns
        - Maximum durability for this item type
        """
        ...


    def isEdible(self) -> bool:
        """
        Checks if this item type is edible.

        Returns
        - True if this item type is edible.
        """
        ...


    def isRecord(self) -> bool:
        """
        Returns
        - True if this item type represents a playable music disk.
        """
        ...


    def isFuel(self) -> bool:
        """
        Checks if this item type can be used as fuel in a Furnace

        Returns
        - True if this item type can be used as fuel.
        """
        ...


    def isCompostable(self) -> bool:
        """
        Checks whether this item type is compostable (can be inserted into a
        composter).

        Returns
        - True if this item type is compostable

        See
        - .getCompostChance()
        """
        ...


    def getCompostChance(self) -> float:
        """
        Get the chance that this item type will successfully compost. The
        returned value is between 0 and 1 (inclusive).
        
        Items with a compost chance of 1 will always raise the composter's level,
        while items with a compost chance of 0 will never raise it.
        
        Plugins should check that .isCompostable returns True before
        calling this method.

        Returns
        - the chance that this item type will successfully compost

        Raises
        - IllegalArgumentException: if this item type is not compostable

        See
        - .isCompostable()
        """
        ...


    def getCraftingRemainingItem(self) -> "ItemType":
        """
        Determines the remaining item in a crafting grid after crafting with this
        ingredient.

        Returns
        - the item left behind when crafting, or null if nothing is.
        """
        ...


    def getDefaultAttributeModifiers(self, slot: "EquipmentSlot") -> "Multimap"["Attribute", "AttributeModifier"]:
        """
        Return an immutable copy of all default Attributes and their
        AttributeModifiers for a given EquipmentSlot.
        
        Default attributes are those that are always preset on some items, such
        as the attack damage on weapons or the armor value on armor.

        Arguments
        - slot: the EquipmentSlot to check

        Returns
        - the immutable Multimap with the respective default
        Attributes and modifiers, or an empty map if no attributes are set.
        """
        ...


    def getCreativeCategory(self) -> "CreativeCategory":
        """
        Get the CreativeCategory to which this item type belongs.

        Returns
        - the creative category. null if does not belong to a category

        Deprecated
        - creative categories no longer exist on the server
        """
        ...


    def isEnabledByFeature(self, world: "World") -> bool:
        """
        Gets if the ItemType is enabled by the features in a world.

        Arguments
        - world: the world to check

        Returns
        - True if this ItemType can be used in this World.
        """
        ...


    def asMaterial(self) -> "Material":
        """
        Tries to convert this ItemType into a Material

        Returns
        - the converted Material or null

        Deprecated
        - only for internal use
        """
        ...
