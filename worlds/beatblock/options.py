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

class MarathonSanity(Toggle):
    """
    Adds every marathon completion as a check.
    """

    display_name = "Marathons"

class Achievements(Toggle):
    """
    Adds the silly achievements to the itempool.
    (Single miss/barely, P rank, ratemod, Tangent, and fail DAMOCLISM)
    """

    display_name = "Achievement Checks"

class Ladybug(Toggle):
    """
    Adds the ladybug achievement to the itempool.
    """

    display_name = "Ladybug Achievement"
    
class Ranksanity(Toggle):
    """
    Adds every rank to the locationpool.
    If enabled target rank wont matter
    (Only DAMOCLISM F(?), and A to P will be added)
    """

    display_name = "Ranksanity"

class ImpossibleRanks(Toggle):
    """
    Enable Impossible/Very difficult DAMOCLISM ranks in ranksanity
    (DAMOCLISM D- to B+)
    """

    display_name = "Impossible Ranks"


TargetRank = make_dynamic_choice("TargetRank", ranks_list, "Target Rank", "s", """
The minimum target rank for checks
Will be ignored if ranksanity is on
""")

GoalLevel = make_dynamic_choice("GoalLevel", levels_list, "Goal Level", "Era Chimaera", """
The final level needed before go Mode
""")

GoalRank = make_dynamic_choice("GoalRank", ranks_list, "Goal Rank", "a plus", """
The Rank needed to beat the goal level
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
    target_rank: TargetRank
    goal_level: GoalLevel
    goal_rank: GoalRank
    ranksanity: Ranksanity
    impossible_ranks: ImpossibleRanks
    fishsanity: Fishsanity
    marathonsanity: MarathonSanity
    achievements: Achievements
    ladybug: Ladybug
    custom_levels: CustomLevels

option_groups = [
        OptionGroup(
            "Gameplay Options",
            [
                DeathLink,
                TargetRank,
                GoalLevel,
                GoalRank,
                Ranksanity,
                ImpossibleRanks,
                Fishsanity,
                MarathonSanity,
                Achievements,
                Ladybug,
                CustomLevels
            ],
        )
]

option_presets = {
    "default": {
        "deathlink": False,
        "target_rank": "s",
        "goal_level": "era_chimaera",
        "goal_rank": "s",
        "ranksanity": False,
        "impossible_ranks": False,
        "fishsanity": False,
        "marathonSanity": False,
        "achievements": False,
        "ladybug": False,
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