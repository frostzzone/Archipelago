from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .data import origin_region, levels_list

from .locations import level_dict, fish_locations, VICTORY_LOCATION

#from .options import HardMode

if TYPE_CHECKING:
    from .world import BeatblockWorld

def set_all_rules(world: BeatblockWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BeatblockWorld) -> None:
    # Theres only the fish entrance 
    if world.options.fishsanity:
        fishing_room = world.get_entrance("fishing special")
        can_fish = Has("Fishing Rod")
        world.set_rule(fishing_room, can_fish)

def set_all_location_rules(world: BeatblockWorld) -> None:
    # THE PAIN OF STUPID LOOKING CODE

    # TODO: Add multi level completion condition ( Extra Atom Unlocks )
    # Levels location rules

    ### Level dictionary
    # { item_name: [ location, location, ...]}
    for level_name, level_locations in level_dict.items():
        level_unlocked = Has(level_name)
        for location_name in level_locations:
            location = world.get_location(location_name)
            # world.set_rule(location, level_unlocked)
            world.set_rule(
                location,
                lambda state, level=level_name: state.has(level, world.player)
            )
    
    # Fish location rules
    if world.options.fishsanity:
        for location_name in fish_locations:
            location = world.get_location(location_name)
            world.set_rule(location, Has("Fishing Rod"))

    can_complete_game = Has(VICTORY_LOCATION)

    final_level = world.get_location(VICTORY_LOCATION + " (B- or Above)")
    world.set_rule(final_level, can_complete_game)

def set_completion_condition(world: BeatblockWorld) -> None:
    
    world.set_completion_rule(Has("Victory"))