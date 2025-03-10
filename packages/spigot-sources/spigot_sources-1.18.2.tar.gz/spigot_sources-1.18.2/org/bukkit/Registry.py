"""
Python module generated from Java source file org.bukkit.Registry

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Predicates
from com.google.common.collect import ImmutableMap
from java.util import Arrays
from java.util import Iterator
from java.util.function import Predicate
from org.bukkit import *
from org.bukkit.advancement import Advancement
from org.bukkit.attribute import Attribute
from org.bukkit.block import Biome
from org.bukkit.boss import KeyedBossBar
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import EntityType
from org.bukkit.entity import Villager
from org.bukkit.entity.memory import MemoryKey
from org.bukkit.loot import LootTables
from typing import Any, Callable, Iterable, Tuple


class Registry(Iterable):
    """
    Represents a registry of Bukkit objects that may be retrieved by
    NamespacedKey.
    
    Type `<T>`: type of item in the registry
    """

    ADVANCEMENT = Registry<Advancement>() {
    
        @Nullable
        @Override
        public Advancement get(@NotNull NamespacedKey key) {
            return Bukkit.getAdvancement(key);
        }
    
        @NotNull
        @Override
        public Iterator<Advancement> iterator() {
            return Bukkit.advancementIterator();
        }
    }
    """
    Server advancements.

    See
    - Bukkit.advancementIterator()
    """
    ART = SimpleRegistry<>(Art.class)
    """
    Server art.

    See
    - Art
    """
    ATTRIBUTE = SimpleRegistry<>(Attribute.class)
    """
    Attribute.

    See
    - Attribute
    """
    BIOME = SimpleRegistry<>(Biome.class)
    """
    Server biomes.

    See
    - Biome
    """
    BOSS_BARS = Registry<KeyedBossBar>() {
    
        @Nullable
        @Override
        public KeyedBossBar get(@NotNull NamespacedKey key) {
            return Bukkit.getBossBar(key);
        }
    
        @NotNull
        @Override
        public Iterator<KeyedBossBar> iterator() {
            return Bukkit.getBossBars();
        }
    }
    """
    Custom boss bars.

    See
    - Bukkit.getBossBars()
    """
    ENCHANTMENT = Registry<Enchantment>() {
    
        @Nullable
        @Override
        public Enchantment get(@NotNull NamespacedKey key) {
            return Enchantment.getByKey(key);
        }
    
        @NotNull
        @Override
        public Iterator<Enchantment> iterator() {
            return Arrays.asList(Enchantment.values()).iterator();
        }
    }
    """
    Server enchantments.

    See
    - Enchantment.getByKey(org.bukkit.NamespacedKey)
    """
    ENTITY_TYPE = SimpleRegistry<>(EntityType.class, (entity) -> entity != EntityType.UNKNOWN)
    """
    Server entity types.

    See
    - EntityType
    """
    LOOT_TABLES = SimpleRegistry<>(LootTables.class)
    """
    Default server loot tables.

    See
    - LootTables
    """
    MATERIAL = SimpleRegistry<>(Material.class, (mat) -> !mat.isLegacy())
    """
    Server materials.

    See
    - Material
    """
    STATISTIC = SimpleRegistry<>(Statistic.class)
    """
    Server statistics.

    See
    - Statistic
    """
    SOUNDS = SimpleRegistry<>(Sound.class)
    """
    Sound keys.

    See
    - Sound
    """
    VILLAGER_PROFESSION = SimpleRegistry<>(Villager.Profession.class)
    """
    Villager profession.

    See
    - Villager.Profession
    """
    VILLAGER_TYPE = SimpleRegistry<>(Villager.Type.class)
    """
    Villager type.

    See
    - Villager.Type
    """
    MEMORY_MODULE_TYPE = Registry<MemoryKey>() {
    
        @NotNull
        @Override
        public Iterator iterator() {
            return MemoryKey.values().iterator();
        }
    
        @Nullable
        @Override
        public MemoryKey get(@NotNull NamespacedKey key) {
            return MemoryKey.getByKey(key);
        }
    }
    """
    Memory Keys.

    See
    - MemoryKey
    """
    FLUID = SimpleRegistry<>(Fluid.class)
    """
    Server fluids.

    See
    - Fluid
    """
    GAME_EVENT = Registry<GameEvent>() {
    
        @NotNull
        @Override
        public Iterator iterator() {
            return GameEvent.values().iterator();
        }
    
        @Nullable
        @Override
        public GameEvent get(@NotNull NamespacedKey key) {
            return GameEvent.getByKey(key);
        }
    }
    """
    Game events.

    See
    - GameEvent
    """


    def get(self, key: "NamespacedKey") -> "T":
        """
        Get the object by its key.

        Arguments
        - key: non-null key

        Returns
        - item or null if does not exist
        """
        ...
