import typing
from dataclasses import dataclass
from typing import Dict, Any
from Options import Option, Choice, DeathLink, Range, Toggle, PerGameCommonOptions, OptionGroup, OptionSet

# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

class DragunGoal(Choice):
    """Require High Dragun defeat for completion"""
    display_name = "Dragun Goal"
    option_required = 1
    option_optional = 0
    default = 1

class LichGoal(Choice):
    """Require Lich Goal defeat for completion"""
    display_name = "Lich Goal"
    option_required = 1
    option_optional = 0
    default = 1

class Blobulord(Choice):
    """Require Blobulord defeat for completion"""
    display_name = "Blobulord Goal"
    option_required = 1
    option_optional = 0
    default = 1

class OldKing(Choice):
    """Require Old King defeat for completion"""
    display_name = "Old King Goal"
    option_required = 1
    option_optional = 0
    default = 1

class ResourcefulRat(Choice):
    """Require Resourceful Rat defeat for completion"""
    display_name = "Resourceful Rat Goal"
    option_required = 1
    option_optional = 0
    default = 0

class Agunim(Choice):
    """Require Agunim (R&D Dept) Goal defeat for completion"""
    display_name = "Agunim Goal"
    option_required = 1
    option_optional = 0
    default = 1

class AdvancedDragun(Choice):
    """Require Advanced Dragun Goal defeat for completion"""
    display_name = "Lich Goal"
    option_required = 1
    option_optional = 0
    default = 0

class RandomizeEnemies(Choice):
    """Randomize all basic enemies in the Gungeon."""
    display_name = "Randomize Enemies"
    option_random_enemies = 1
    option_standard_enemies = 0
    default = 1


"Default options defines 50 items, then 3 progression items"

class RandomGunTierD(Range):
    """Amount of D tier guns in the item pool"""
    display_name = "D Tier Guns"
    range_start = 0
    range_end = 20
    default = 5

class RandomGunTierC(Range):
    """Amount of C tier guns in the item pool"""
    display_name = "C Tier Guns"
    range_start = 0
    range_end = 20
    default = 3

class RandomGunTierB(Range):
    """Amount of B tier guns in the item pool"""
    display_name = "B Tier Guns"
    range_start = 0
    range_end = 20
    default = 3

class RandomGunTierA(Range):
    """Amount of A tier guns in the item pool"""
    display_name = "A Tier Guns"
    range_start = 0
    range_end = 20
    default = 2

class RandomGunTierS(Range):
    """Amount of S tier guns in the item pool"""
    display_name = "S Tier Guns"
    range_start = 0
    range_end = 20
    default = 2

class RandomItemTierD(Range):
    """Amount of D tier items in the item pool"""
    display_name = "D Tier Items"
    range_start = 0
    range_end = 20
    default = 5

class RandomItemTierC(Range):
    """Amount of C tier items in the item pool"""
    display_name = "C Tier Items"
    range_start = 0
    range_end = 20
    default = 3

class RandomItemTierB(Range):
    """Amount of B tier items in the item pool"""
    display_name = "B Tier Items"
    range_start = 0
    range_end = 20
    default = 3

class RandomItemTierA(Range):
    """Amount of A tier items in the item pool"""
    display_name = "A Tier Items"
    range_start = 0
    range_end = 20
    default = 2

class RandomItemTierS(Range):
    """Amount of S tier items in the item pool"""
    display_name = "S Tier Items"
    range_start = 0
    range_end = 20
    default = 2

class PickupAmount(Range):
    """Amount of item pickups in the item pool"""
    display_name = "Pickup Amount"
    range_start = 0
    range_end = 50
    default = 10

class TrapAmount(Range):
    """Amount of traps in the item pool"""
    display_name = "Trap Amount"
    range_start = 0
    range_end = 50
    default = 10


gungeon_option_groups = [
    OptionGroup("Boss Goals Options", [
        DragunGoal,
        LichGoal,
        Blobulord,
        OldKing,
        ResourcefulRat,
        Agunim,
        AdvancedDragun
    ]),
    OptionGroup("Item Amount Options", [
        RandomGunTierD,
        RandomGunTierC,
        RandomGunTierB,
        RandomGunTierA,
        RandomGunTierS,
        RandomItemTierD,
        RandomItemTierC,
        RandomItemTierB,
        RandomItemTierA,
        RandomItemTierS,
        PickupAmount,
        TrapAmount,
    ])
]

gungeon_options_presets: Dict[str, Dict[str, Any]] = {
    "All Bosses": {
        "high_dragun": DragunGoal.default,
        "lich": LichGoal.default,
        "blobulord": Blobulord.default,
        "old_king": OldKing.default,
        "resourceful_rat": ResourcefulRat.default,
        "agunim": Agunim.default,
        "advanced_dragun": AdvancedDragun.default,
    },
    "D Tier": {
        "random_gun_tier_d":     RandomGunTierD.range_end,
        "random_gun_tier_c":     0,
        "random_gun_tier_b":     0,
        "random_gun_tier_a":     0,
        "random_gun_tier_s":     0,
        "random_item_tier_d":    RandomItemTierD.range_end,
        "random_item_tier_c":    0,
        "random_item_tier_b":    0,
        "random_item_tier_a":    0,
        "random_item_tier_s":    0,
    },
    "Random": {
        "pickup_amount":         "random",
        "random_gun_tier_d":     "random",
        "random_gun_tier_c":     "random",
        "random_gun_tier_b":     "random",
        "random_gun_tier_a":     "random",
        "random_gun_tier_s":     "random",
        "trap_amount":           "random",
        "random_item_tier_d":    "random",
        "random_item_tier_c":    "random",
        "random_item_tier_b":    "random",
        "random_item_tier_a":    "random",
        "random_item_tier_s":    "random",
    },
    "random_enemies":        RandomizeEnemies.option_random_enemies,
}

@dataclass
class GungeonOptions(PerGameCommonOptions):
    dragun: DragunGoal
    lich: LichGoal
    blobulord: Blobulord
    old_king: OldKing
    resourceful_rat: ResourcefulRat
    agunim: Agunim
    advanced_dragun: AdvancedDragun

    random_enemies: RandomizeEnemies
    death_link: DeathLink

    pickup_amount: PickupAmount
    random_gun_tier_d: RandomGunTierD
    random_gun_tier_c: RandomGunTierC
    random_gun_tier_b: RandomGunTierB
    random_gun_tier_a: RandomGunTierA
    random_gun_tier_s: RandomGunTierS
    trap_amount: TrapAmount
    random_item_tier_d: RandomItemTierD
    random_item_tier_c: RandomItemTierC
    random_item_tier_b: RandomItemTierB
    random_item_tier_a: RandomItemTierA
    random_item_tier_s: RandomItemTierS

