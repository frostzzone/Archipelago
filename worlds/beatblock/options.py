from dataclasses import dataclass

from schema import Schema, Optional
from Options import Choice, TextChoice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionDict, Visibility

from .data import levels_list, ranks_list


def make_dynamic_choice(class_name, options, display_name="unset", default=0, doc = """I forgor to set this please tell me"""):
    choice_attributes = {
        "__doc__": doc,
        "display_name": display_name,
    }

    for i, option in enumerate(options):
        choice_attributes[f"option_{option.replace(' ', '_')}"] = i
        if option == default:
            choice_attributes["default"] = i

    return type(class_name, (Choice,), choice_attributes)

class DeathLink(Toggle):
    """
    When you die, everyone who enabled death link dies. Of course, the reverse is true too.
    """
    display_name = "Death Link"

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


TargetRank = make_dynamic_choice("TargetRank", ranks_list, "Target Rank", "S", """
The minimum target rank for checks
Will be ignored if ranksanity is on
""")

GoalLevel = make_dynamic_choice("GoalLevel", levels_list, "Goal Level", "Era Chimaera", """
The final level needed before go Mode
""")

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
    deathlink: DeathLink
    fishsanity: Fishsanity
    ranksanity: Ranksanity
    target_rank: TargetRank
    goal_level: GoalLevel
    custom_levels: CustomLevels

option_groups = [
        OptionGroup(
            "Gameplay Options",
            [DeathLink, TargetRank, GoalLevel, Ranksanity, Fishsanity],
        )
]

option_presets = {
    "default": {
        "deathlink": False,
        "fishsanity": False,
        "ranksanity": False,
        "target_rank": "s",
        "goal_level": "era_chimaera",
        "custom_levels": {
            "#comment": "Not implemented yet",
            "#comment2": "any level with a # in front of it will be ignored",
            "#shown_name": {
                "folder":"level_folder",
                "workshop": False
            }
        }
    }
}