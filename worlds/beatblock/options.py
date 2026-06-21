from dataclasses import dataclass

from schema import Schema, Optional
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionDict, Visibility

from .data import levels_list

class Fishsanity(Toggle):
    """
    Adds every fish to the itempool.
    """

    display_name = "Fishsanity"

    
class Ranksanity(Toggle):
    """
    Adds every rank to the locationpool.
    If enabled target rank wont matter
    """

    display_name = "Ranksanity"

class TargetRank(Choice):
    """
    The target rank for checks
    """

    display_name = "Target Rank"

    option_P = 0
    option_S_Plus = 1
    option_S = 2
    option_A_Plus = 3
    option_A = 4
    option_B_Plus = 5
    option_B = 6
    option_B_Minus = 7
    option_C_Plus = 8
    option_C = 9
    option_C_Minus = 10
    option_D_Plus = 11
    option_D = 12
    option_D_Minus = 13
    option_F = 14

    # Choice options must define an explicit default value.
    default = option_S

class CustomLevels(OptionDict):
    """
    Custom levels
    """

    display_name = "Custom Levels"
    schema = Schema({
        Optional(str): str
    })

    visibility = Visibility.none

@dataclass
class BeatblockOptions(PerGameCommonOptions):
    fishsanity: Fishsanity
    ranksanity: Ranksanity
    target_rank: TargetRank
    custom_levels: CustomLevels

option_groups = [
        OptionGroup(
            "Gameplay Options",
            [TargetRank, Ranksanity, Fishsanity],
        )
]

option_presets = {
    "default": {
        "fishsanity": False,
        "ranksanity": False,
        "target_rank": TargetRank.option_S,
        "custom_levels": {}
    }
}