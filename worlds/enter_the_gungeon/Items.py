from BaseClasses import Item

class ItemPoolGeneration:

    short_item_count = {
        "Random D Tier Gun": 4,
        "Random C Tier Gun": 3,
        "Random B Tier Gun": 3,
        "Random A Tier Gun": 2,
        "Random S Tier Gun": 1,
        "Random D Tier Item": 4,
        "Random C Tier Item": 3,
        "Random B Tier Item": 4,
        "Random A Tier Item": 3,
        "Random S Tier Item": 2,
        "Consumables": 10,
        "Traps": 10
    }

    standard_item_count = {
        "Random D Tier Gun": 5,
        "Random C Tier Gun": 4,
        "Random B Tier Gun": 4,
        "Random A Tier Gun": 3,
        "Random S Tier Gun": 2,
        "Random D Tier Item": 5,
        "Random C Tier Item": 4,
        "Random B Tier Item": 4,
        "Random A Tier Item": 3,
        "Random S Tier Item": 2,
        "Consumables": 20,
        "Traps": 15
    }

    marathon_item_count = {
        "Random D Tier Gun": 7,
        "Random C Tier Gun": 5,
        "Random B Tier Gun": 5,
        "Random A Tier Gun": 3,
        "Random S Tier Gun": 3,
        "Random D Tier Item": 7,
        "Random C Tier Item": 7,
        "Random B Tier Item": 5,
        "Random A Tier Item": 3,
        "Random S Tier Item": 3,
        "Consumables": 30,
        "Traps": 25
    }

    @classmethod
    def get_guns_count(cls, case_number=1):
        match case_number:
            case 0:
                return 13
            case 1:
                return 18
            case 2:
                return 23

        return 18

    @classmethod
    def get_passive_count(cls, case_number=1):
        match case_number:
            case 0:
                return 16
            case 1:
                return 18
            case 2:
                return 25

        return 18

    @classmethod
    def get_consumables_count(cls, case_number=1):

        match case_number:
            case 0:
                return ItemPoolGeneration.short_item_count["Consumables"]
            case 1:
                return ItemPoolGeneration.standard_item_count["Consumables"]
            case 2:
                return ItemPoolGeneration.marathon_item_count["Consumables"]

        return ItemPoolGeneration.standard_item_count["Consumables"]

    @classmethod
    def get_traps_count(cls, case_number=1):

        match case_number:
            case 0:
                return ItemPoolGeneration.short_item_count["Traps"]
            case 1:
                return ItemPoolGeneration.standard_item_count["Traps"]
            case 2:
                return ItemPoolGeneration.marathon_item_count["Traps"]

        return ItemPoolGeneration.standard_item_count["Traps"]

class GungeonItem(Item):
    game: str = "Enter The Gungeon"


item_table = {}

gun_item_table = {
    "Random D Tier Gun": 8754000,
    "Random C Tier Gun": 8754001,
    "Random B Tier Gun": 8754002,
    "Random A Tier Gun": 8754003,
    "Random S Tier Gun": 8754004,
}

passive_item_table = {
    "Random D Tier Item": 8754005,
    "Random C Tier Item": 8754006,
    "Random B Tier Item": 8754007,
    "Random A Tier Item": 8754008,
    "Random S Tier Item": 8754009,
}

pickup_item_table = {
    "Glassful of Guons": 8754100,
    "50 Casings": 8754101,
    "Key": 8754102,
    "Blank": 8754103,
    "Armor": 8754104,
    "Heart": 8754105,
    "Ammo": 8754106,
}

trap_item_table = {
    "Rats!! Trap": 8754200,
    "Mimic Gun Trap": 8754201,
    "Curse Trap": 8754202,
    "Fumble Gun Trap": 8754203,
    "Fire Trap": 8754204,
    "Poison Trap": 8754205,
    "Curse Meter Trap": 8754206,
    "Enemy Trap": 8754207,
}

progression_item_table = {
    "Gnawed Key": 8754301,
    "Old Crest": 8754302,
    "Weird Egg": 8754303,
}

paradox_character_unlock_table = {
    "Marine - Paradox": 8754300,
    "Convict - Paradox": 8754301,
    "Pilot - Paradox": 8754302,
    "Hunter - Paradox": 8754303,
    "Robot - Paradox": 8754304,
    "Bullet - Paradox": 8754305,
}

item_table.update(gun_item_table)
item_table.update(passive_item_table)
item_table.update(pickup_item_table)
item_table.update(trap_item_table)
item_table.update(progression_item_table)
item_table.update(paradox_character_unlock_table)

fill_item_table = {}
fill_item_table.update(gun_item_table)
fill_item_table.update(passive_item_table)
fill_item_table.update(pickup_item_table)
fill_item_table.update(trap_item_table)