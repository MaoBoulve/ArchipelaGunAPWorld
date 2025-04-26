from BaseClasses import Location, MultiWorld
from .Options import AchievementLocationChecks, APItemLocationChecks
from .Items import progression_item_table

class GungeonLocation(Location):
    game: str = "Enter The Gungeon"


class LocationGeneration:

    location_id = {
        "Room Clear Points": 8755200,
        "Chests Opened": 8755300,
        "Cash Spent": 8755400,
        "Past Clears": 8755600,
        "Floor 1 Clears": 8755700,
        "Floor 2 Clears": 8755720,
        "Floor 3 Clears": 8755740,
        "Floor 4 Clears": 8755760,
        "Floor 5 Clears": 8755780,
        "Bullet Hell Clears": 8755800,
        "Oubliette Clears": 8755820,
        "Abbey Clears": 8755840,
        "Resourceful Rat Lair Clears": 8755860,
        "R&D Department Clears": 8755880,
        "Chest AP Item": 8755000,
        "Shop AP Item": 8755100
    }

    short_location_count = {
        "Room Clear Points": 5,
        "Chests Opened": 4,
        "Cash Spent": 3,
        "Past Clears": 1,
        "Floor 1 Clears": 4,
        "Floor 2 Clears": 4,
        "Floor 3 Clears": 3,
        "Floor 4 Clears": 3,
        "Floor 5 Clears": 2,
        "Bullet Hell Clears": 1,
        "Oubliette Clears": 2,
        "Abbey Clears": 1,
        "Resourceful Rat Lair Clears": 0,
        "R&D Department Clears": 0,
        "Chest AP Item": 11,
        "Shop AP Item": 5
    }

    standard_location_count = {
        "Room Clear Points": 8,
        "Chests Opened": 6,
        "Cash Spent": 5,
        "Past Clears": 4,
        "Floor 1 Clears": 6,
        "Floor 2 Clears": 6,
        "Floor 3 Clears": 4,
        "Floor 4 Clears": 4,
        "Floor 5 Clears": 4,
        "Bullet Hell Clears": 2,
        "Oubliette Clears": 3,
        "Abbey Clears": 2,
        "Resourceful Rat Lair Clears": 1,
        "R&D Department Clears": 1,
        "Chest AP Item": 16,
        "Shop AP Item": 9
    }

    marathon_location_count = {
        "Room Clear Points": 13,
        "Chests Opened": 8,
        "Cash Spent": 7,
        "Past Clears": 6,
        "Floor 1 Clears": 8,
        "Floor 2 Clears": 8,
        "Floor 3 Clears": 6,
        "Floor 4 Clears": 6,
        "Floor 5 Clears": 6,
        "Bullet Hell Clears": 3,
        "Oubliette Clears": 6,
        "Abbey Clears": 3,
        "Resourceful Rat Lair Clears": 2,
        "R&D Department Clears": 2,
        "Chest AP Item": 25,
        "Shop AP Item": 15
    }

    @classmethod
    def get_achievement_location_count(cls, case_number=1):

        match case_number:
            case 0:
                return 33
            case 1:
                return 56
            case 2:
                return 84

        return 56

    @classmethod
    def get_ap_item_location_count(cls, case_number=1):

        match case_number:
            case 0:
                return 16
            case 1:
                return 25
            case 2:
                return 40

        return 40

    @classmethod
    def get_ap_item_sub_count(cls, case_number=1):
        match case_number:
            case 0:
                return 11, 5
            case 1:
                return 16, 9
            case 2:
                return 25, 15

        return 16, 9

    @classmethod
    def get_location_count_list(cls, case_number=1):
        match case_number:
            case 0:
                return LocationGeneration.short_location_count
            case 1:
                return LocationGeneration.standard_location_count
            case 2:
                return LocationGeneration.marathon_location_count

        return LocationGeneration.standard_location_count

def fill_ap_item_locations_to_max():
    for i in range(0, 98):
        location_table.update({f"Chest AP Item {i + 1}": LocationGeneration.location_id["Chest AP Item"] + i})
        location_table.update({f"Shop AP Item {i + 1}": LocationGeneration.location_id["Shop AP Item"] + i})
    return

def fill_achievement_locations():
    name_list = LocationGeneration.location_id.keys()

    for name in name_list:
        if name != "Chest AP Item" or name != "Shop AP Item":
            for i in range(0, LocationGeneration.marathon_location_count[name]):
                location_table.update({f"{name} {i + 1}": LocationGeneration.location_id[name] + i})

    return


location_table = {}

fill_ap_item_locations_to_max()
fill_achievement_locations()

event_location_table = {
    "The High Dragun": None,
    "The Lich": None,
    "Base Secret Chamber Bosses": None,
    "Past Killed": None,
    "Advanced Gungeon Bosses": None,
    "Farewell To Arms Bosses": None
}

location_table.update(event_location_table)
