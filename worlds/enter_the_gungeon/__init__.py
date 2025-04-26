from typing import List
from .Items import item_table, pickup_item_table, trap_item_table, GungeonItem, progression_item_table, fill_item_table
from .Items import gun_item_table, passive_item_table, paradox_character_unlock_table
from .Locations import location_table, GungeonLocation
from .Options import GungeonOptions, gungeon_option_groups, gungeon_options_presets
from .Rules import set_rules
from .Regions import create_regions, get_gungeon_items_count, get_user_requested_locations_count
from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from ..AutoWorld import World, WebWorld

client_version = 1


class GungeonWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Enter The Gungeon for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["MaoBoulve"]
    )]

    option_groups = gungeon_option_groups
    options_presets = gungeon_options_presets


class GungeonWorld(World):
    # Lifted from Store Page
    """ Enter the Gungeon is a bullet hell roguelike to get the Gungeon's treasure: the gun that can kill the past.

    The randomizer replaces all chests with APItems location checks. Milestones also send location checks.
    Received items/traps play a matching effect and spawn by the player.
    """

    game: str = "Enter The Gungeon"
    topology_present = False
    web = GungeonWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table

    options_dataclass = GungeonOptions
    options: GungeonOptions

    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)
        self.place_events()

    """Defines Session.DataStorage.GetSlotData() dict"""

    def fill_slot_data(self):
        return {
            "Dragun": self.options.dragun.value,
            "Lich": self.options.lich.value,

            "Pasts": self.options.past_kills.value,

            "BaseSecret": self.options.base_secret_chamber.value,
            "AdvancedGungeon": self.options.advanced_gungeon.value,
            "FarewellArms": self.options.farewell_arms.value,

            "Paradox": self.options.paradox_mode.value,
            "DeathLink": self.options.death_link.value,
            "RandomEnemies": self.options.random_enemies.value,

            "AchievementChecks": self.options.achievement_locations.value,
            "APItemChecks": self.options.ap_item_locations.value,
            "ExtraLocations": self.count_extra_locations()
        }

    def count_extra_locations(self):

        item_count = get_gungeon_items_count(self.options)
        location_count = get_user_requested_locations_count(self.options)

        extra_locations = item_count - location_count

        if extra_locations > 0:
            return extra_locations

        else:
            return 0

    def set_rules(self):
        self.area_connections = {}
        self.area_cost_map = {}
        set_rules(self.multiworld, self.options, self.player, self.area_connections, self.area_cost_map)

    def create_item(self, name: str) -> Item:
        return GungeonItem(name, ItemClassification.filler, item_table[name], self.player)

    def create_progress_item(self, name: str) -> Item:
        return GungeonItem(name, ItemClassification.progression, progression_item_table[name], self.player)

    def create_useful_item(self, name: str) -> Item:
        return GungeonItem(name, ItemClassification.useful, item_table[name], self.player)

    def create_trap_item(self, name: str) -> Item:
        return GungeonItem(name, ItemClassification.trap, item_table[name], self.player)

    def create_event(self, name: str) -> GungeonItem:
        return GungeonItem(name, ItemClassification.progression, None, self.player)

    def create_items(self):
        item_pool: List[GungeonItem] = []

        item_pool = self.create_item_pool(item_pool, amount_case=self.options.guns.value,
                                          item_table_list=gun_item_table)
        item_pool = self.create_item_pool(item_pool, amount_case=self.options.passives.value,
                                          item_table_list=passive_item_table)

        "Progress items"
        for progression_item_name, itemID in progression_item_table.items():
            item_pool.append(self.create_progress_item(progression_item_name))

        consumables_count = Items.ItemPoolGeneration.get_consumables_count(self.options.consumable.value)
        "Consumables items"
        for i in range(0, consumables_count):
            item_pool.append(self.create_item(list(pickup_item_table)[i % len(pickup_item_table)]))

        trap_count = Items.ItemPoolGeneration.get_consumables_count(self.options.traps.value)
        "Traps"
        for i in range(0, trap_count):
            item_pool.append(self.create_trap_item(list(trap_item_table)[i % len(trap_item_table)]))

        "Paradox Mode"
        if self.options.paradox_mode.value == 1:
            for character_name, itemID in paradox_character_unlock_table():
                item_pool.append(self.create_progress_item(character_name))

        item_count = get_gungeon_items_count(self.options)
        location_count = get_user_requested_locations_count(self.options)

        if location_count > item_count:
            items_to_fill = location_count - item_count
            item_pool = self.create_fill_items(item_pool, items_to_fill)

        self.multiworld.itempool += item_pool

    def create_fill_items(self, item_pool, amount_to_fill=10):
        for i in range(0, amount_to_fill):
            item_name = list(fill_item_table)[i % len(fill_item_table)]

            if "Trap" in item_name:
                item_pool.append(self.create_trap_item(item_name))
            else:
                item_pool.append(self.create_item(item_name))

        return item_pool

    def create_item_pool(self, item_pool, amount_case=0, item_table_list=gun_item_table):
        for name, data in item_table_list:
            quantity = 0

            match amount_case:
                case 0:
                    "Short amount"
                    quantity = Items.ItemPoolGeneration.short_item_count[name]
                case 1:
                    "Standard"
                    quantity = Items.ItemPoolGeneration.standard_item_count[name]
                case 2:
                    "Marathon"
                    quantity = Items.ItemPoolGeneration.marathon_item_count[name]
            item_pool += [self.create_item(name) for i in range(0, quantity)]
        return item_pool

    def place_events(self):
        self.multiworld.get_location("The High Dragun", self.player).place_locked_item(
            self.create_event("Defeat The High Dragun"))

        self.multiworld.get_location("The Lich", self.player).place_locked_item(
            self.create_event("Defeat The Lich"))

        self.multiworld.get_location("Base Secret Chamber Bosses", self.player).place_locked_item(
            self.create_event("Base Secret Chamber Bosses"))

        self.multiworld.get_location("Past Killed", self.player).place_locked_item(
            self.create_event("Past Killed"))

        self.multiworld.get_location("Advanced Gungeon Bosses", self.player).place_locked_item(
            self.create_event("Advanced Gungeon Bosses"))

        self.multiworld.get_location("Farewell To Arms Bosses", self.player).place_locked_item(
            self.create_event("Farewell To Arms Bosses"))
        return
