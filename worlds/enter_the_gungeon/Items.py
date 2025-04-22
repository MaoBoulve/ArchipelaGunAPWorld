from BaseClasses import Item

class GungeonItem(Item):
    game: str = "Enter The Gungeon"


item_table = {}

normal_item_table = {
    "Random D Tier Gun": 8754000,
    "Random C Tier Gun": 8754001,
    "Random B Tier Gun": 8754002,
    "Random A Tier Gun": 8754003,
    "Random S Tier Gun": 8754004,
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
    "Mimic Gun": 8754201,
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

item_table.update(normal_item_table)
item_table.update(pickup_item_table)
item_table.update(trap_item_table)
item_table.update(progression_item_table)
