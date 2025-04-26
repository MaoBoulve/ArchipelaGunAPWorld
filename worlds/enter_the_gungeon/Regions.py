import typing
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import GungeonLocation, location_table, event_location_table, LocationGeneration
from .Items import progression_item_table, ItemPoolGeneration
from .Options import GungeonOptions

def get_gungeon_items_count(options: GungeonOptions):
    item_count = 0

    item_count += ItemPoolGeneration.get_guns_count(options.guns.value)
    item_count += ItemPoolGeneration.get_passive_count(options.passives.value)
    item_count += ItemPoolGeneration.get_consumables_count(options.consumable.value)
    item_count += ItemPoolGeneration.get_traps_count(options.traps.value)

    if options.paradox_mode.value == 1:
        item_count += 6
    item_count += len(progression_item_table)

    return item_count

def get_user_requested_locations_count(options: GungeonOptions):
    loc_count = 0
    loc_count += LocationGeneration.get_achievement_location_count(options.achievement_locations.value)
    loc_count += LocationGeneration.get_ap_item_location_count(options.ap_item_locations.value)

    return loc_count


def fill_add_locations(amount: 10, item_case: 1):

    chest_fill = amount

    last_chest, last_shop = LocationGeneration.get_ap_item_sub_count(case_number=item_case)
    loc_name_list = []

    for i in range(0, chest_fill):
        loc_name = f"Chest AP Item {i + 1 + last_chest}"
        loc_name_list.append(loc_name)

    return loc_name_list


def create_regions(world: MultiWorld, options: GungeonOptions, player: int):
    region = Region("Menu", player, world, "")

    item_count = get_gungeon_items_count(options)
    location_count = get_user_requested_locations_count(options)

    if item_count > location_count:
        locations_to_fill = item_count - location_count
        fill_name_list = fill_add_locations(locations_to_fill, options.ap_item_locations.value)

        for location_name in fill_name_list:
            region.locations.append(GungeonLocation(player, location_name, location_table[location_name], region))

    ap_item_location_checks_option = options.ap_item_locations.value
    ap_item_location_count_list = LocationGeneration.get_location_count_list(ap_item_location_checks_option)

    achievement_locations_option = options.achievement_locations.value
    achievement_count_list = LocationGeneration.get_location_count_list(achievement_locations_option)

    for name, data in LocationGeneration.location_id:
        if name != "Chest AP Item" or name != "Shop AP Item":
            for i in range(0, achievement_count_list[name]):
                loc_name = f"{name} {i + 1}"
                region.locations.append(GungeonLocation(player, loc_name, location_table[loc_name], region))
        else:
            for i in range(0, ap_item_location_count_list[name]):
                loc_name = f"{name} {i + 1}"
                region.locations.append(GungeonLocation(player, loc_name, location_table[loc_name], region))

    # Add event locations
    for name in event_location_table:
        region.locations.append(GungeonLocation(player, name, None, region))

    world.regions.append(region)
