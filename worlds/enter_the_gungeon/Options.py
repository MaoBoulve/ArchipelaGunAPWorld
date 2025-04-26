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

class KillThePastGoal(Choice):
    """Require Past Kills for game completion. 'Standard' is base 4 characters. 'All' adds Robot & Bullet
    Mod provides way to use all game characters"""
    display_name = "Kill The Past Goal"
    option_optional = 0
    option_standard = 1
    option_all_pasts = 2
    default = 1

class LichGoal(Choice):
    """Require Lich Goal defeat for completion"""
    display_name = "Lich Goal"
    option_required = 1
    option_optional = 0
    default = 1

class BaseSecretChamberBosses(Choice):
    """Require Blobulord & Old King for completion"""
    display_name = "Base Secret Chamber Boss Goal"
    option_required = 1
    option_optional = 0
    default = 1

class AdvancedGungeonDragunsBosses(Choice):
    """Require bosses from the AG&D Update (Resourceful Rat, Advanced Dragun) for completion.
    Do not need to beat Rat at Punch Out"""
    display_name = "Advanced Gungeon & Draguns Bosses"
    option_required = 1
    option_optional = 0
    default = 0

class FarewellToArmsBosses(Choice):
    """Require bosses from the Farewell To Arms Update (Cam Clarke AS Agunim) for completion
    [Paradox Lich currently WIP]"""
    display_name = "Farewell To Arms Bosses"
    option_required = 0
    option_optional = 1
    default = 0

class RandomizeEnemies(Choice):
    """Randomize all basic enemies in the Gungeon."""
    display_name = "Randomize Enemies"
    option_random_enemies = 1
    option_standard_enemies = 0
    default = 1

class ParadoxMode(Choice):
    """Start all runs as Paradox. Other playable characters are Items in randomizer"""
    display_name = "Paradox Mode"
    option_enabled = 1
    option_disabled = 0
    default = 1

class GunItems(Choice):
    """Amount of Guns in your item pool"""
    display_name = "Gun Pool Items"
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 1

class PassiveItems(Choice):
    """Amount of Passive & Active items in your item pool"""
    display_name = "Passive & Active Pool Items"
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 1

class ConsumableItems(Choice):
    """Amount of Consumable items in your item pool"""
    display_name = "Consumable Items"
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 0

class TrapItems(Choice):
    """Amount of Traps in your item pool"""
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 1

class AchievementLocationChecks(Choice):
    """Location checks for accomplishing tasks in Enter the Gungeon"""
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 1

class APItemLocationChecks(Choice):
    """Location checks from APItem replacing item in chests, shops, etc."""
    option_short = 0
    option_standard = 1
    option_marathon = 2
    default = 1


gungeon_option_groups = [
    OptionGroup("Boss Goals Options", [
        DragunGoal,
        KillThePastGoal,
        LichGoal,
        BaseSecretChamberBosses,
        AdvancedGungeonDragunsBosses,
        FarewellToArmsBosses
    ]),
    OptionGroup("Randomizer Options", [
       DeathLink,
       ParadoxMode,
       RandomizeEnemies
    ]),
    OptionGroup("Gungeon Item Pool Options", [
       GunItems,
       PassiveItems,
       ConsumableItems,
       TrapItems
    ]),

    OptionGroup("Location Check Options", [
       APItemLocationChecks,
       AchievementLocationChecks
    ]),

]

gungeon_options_presets: Dict[str, Dict[str, Any]] = {
    "dragun": DragunGoal.default,
    "past_kills": KillThePastGoal.default,
    "lich": LichGoal.default,
    "base_secret_chamber": BaseSecretChamberBosses.default,
    "advanced_gungeon": AdvancedGungeonDragunsBosses.default,
    "farewell_arms": FarewellToArmsBosses.default,

    "paradox_mode": ParadoxMode.default,
    "random_enemies": RandomizeEnemies.default,
    "death_link": DeathLink.default,

    "guns": GunItems.default,
    "passives": PassiveItems.default,
    "traps": TrapItems.default,
    "consumable": ConsumableItems.default,

    "achievement_locations": AchievementLocationChecks.default,
    "ap_item_locations": APItemLocationChecks.default
}

@dataclass
class GungeonOptions(PerGameCommonOptions):
    dragun: DragunGoal
    past_kills: KillThePastGoal
    lich: LichGoal
    base_secret_chamber: BaseSecretChamberBosses
    advanced_gungeon: AdvancedGungeonDragunsBosses
    farewell_arms: FarewellToArmsBosses

    paradox_mode: ParadoxMode
    random_enemies: RandomizeEnemies
    death_link: DeathLink

    guns: GunItems
    passives: PassiveItems
    traps: TrapItems
    consumable: ConsumableItems

    achievement_locations: AchievementLocationChecks
    ap_item_locations: APItemLocationChecks



