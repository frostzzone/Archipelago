from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .data import origin_region, levels_list, GAME

from .locations import level_dict, fish_locations

#from .options import HardMode

if TYPE_CHECKING:
    from .world import BeatblockWorld

def set_all_rules(world: BeatblockWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BeatblockWorld) -> None:
    # Theres NOT only the fish entrance 

    Intro_atom = world.get_region("Intro")
    world.set_rule(Intro_atom, Has("Intro Key"))

    Mines_atom = world.get_region("Mines")
    world.set_rule(Mines_atom, Has("Mines Key"))

    Bounces_atom = world.get_region("Bounces")
    world.set_rule(Bounces_atom, Has("Bounces Key"))

    Inverses_atom = world.get_region("Inverses")
    world.set_rule(Inverses_atom, Has("Inverses Key"))

    Sides_atom = world.get_region("Sides")
    world.set_rule(Sides_atom, Has("Sides Key"))

    Challenge_atom = world.get_region("Challenge")
    world.set_rule(Challenge_atom, Has("Challenge Key"))

    Extras_atom = world.get_region("Extras")
    world.set_rule(Extras_atom, Has("Extras Key"))

    Collab_atom = world.get_region("Collab")
    world.set_rule(Collab_atom, Has("Collab Key"))

    if world.options.fishsanity:
        fishing_room = world.get_entrance("fishing special")
        can_fish = Has("Fishing Rod")
        world.set_rule(fishing_room, can_fish)

def set_all_location_rules(world: BeatblockWorld) -> None:
    # THE PAIN OF STUPID LOOKING CODE

    # NOT TODO: Add multi level completion condition ( Extra Atom Unlocks )
    # Levels location rules

    ### Level dictionary
    # { item_name: [ location, location, ...]}
    # print("Levels: ", level_dict)
    victory_location = levels_list[world.options.goal_level.value]

    for loc in level_dict:
        # { atom: "BLAH", level: "BLAH", ranks: ["BLAH", "BLAH"] }
        atom_unlocked = Has(level_dict[loc]["atom"] + " Key")
        level_unlocked = Has(level_dict[loc]["level"])

        for rank in level_dict[loc]["ranks"]:
            location = world.get_location(rank)
            world.set_rule(location, atom_unlocked & level_unlocked)
            
    

    # for level_name, level_locations in level_dict.items():
    #     level_unlocked = Has(level_name)
    #     for location_name in level_locations:
    #         location = world.get_location(location_name)
    #         # world.set_rule(location, level_unlocked)

    #         world.set_rule(
    #             location,
    #             lambda state, level=level_name: state.has(level, world.player)
    #         )
    
    # Fish location rules
    if world.options.fishsanity:
        for location_name in fish_locations:
            location = world.get_location(location_name)
            world.set_rule(location, Has("Fishing Rod"))

    can_complete_game = Has(victory_location)

    final_level = world.get_location(victory_location + " (B- or Above)")
    world.set_rule(final_level, can_complete_game)

def set_completion_condition(world: BeatblockWorld) -> None:
    
    world.set_completion_rule(Has("Victory"))