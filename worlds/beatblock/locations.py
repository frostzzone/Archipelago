from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BeatblockWorld

from .options import Ranksanity, TargetRank, Fishsanity

# Replace amount_of_fish with actual fish_list when it is implemented
from .data import game_name, origin_region, levels_list, ranks_list, amount_of_fish

# TODO: REWITE everything to be registered no matter what

# TODO: Add customizable completion condition
VICTORY_LOCATION = "Era Chimaera"

# Create location IDs
level_dict: dict[str, list[str]] = {} # { location_name: [ Check, Check, ...]}
fish_locations = []
LOCATION_TO_ID = {}
# for simplicity on the client side
ID_TO_LOCATION = {}

def create_location_list(world: BeatblockWorld) -> None:
    print("Goal Level: ", levels_list[world.options.goal_level.value])
    counter = 1100
    # Levels
    for loc in levels_list:

        # NOTE: removes the location
        if loc == VICTORY_LOCATION:
            continue


        if world.options.ranksanity.value == True:
            level_dict[loc] = []
            for rank in ranks_list:
                location_name = f"{loc} Get {rank} Rank"
                level_dict[loc].append(location_name)
                LOCATION_TO_ID[location_name] = counter
                ID_TO_LOCATION[counter] = location_name
                counter += 1
        else:
            location_name = f"{loc} Get {ranks_list[world.options.target_rank.value]} Rank"
            level_dict[loc] = [location_name]
            LOCATION_TO_ID[location_name] = counter
            ID_TO_LOCATION[counter] = location_name
            counter += 1

    # Fish
    if world.options.fishsanity:
        for i in range(1, amount_of_fish + 1):
            location_name = f"Catch {i} Fish"
            fish_locations.append(location_name)
            LOCATION_TO_ID[location_name] = counter
            ID_TO_LOCATION[counter] = location_name
            counter += 1

        # replace amount_of_fish function with this when fish_list is implemented
        # if Fishsanity:
        #     for i, fish in enumerate(fish_list):
        #         fish_locations.append(f"Catch {fish}")
        #         LOCATION_TO_ID[location_name] = location_id
        #         counter += 1


class BeatblockLocation(Location):
    game = game_name

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: BeatblockWorld) -> None:
    create_location_list(world)
    create_regular_locations(world)
    create_events(world)

    print(ID_TO_LOCATION)

def create_regular_locations(world: BeatblockWorld) -> None:
    game_region = world.get_region(origin_region)

    level_location_ids = {}
    for location_name, location_checks in level_dict.items():
        location_ids = get_location_names_with_ids(location_checks)
        level_location_ids = level_location_ids | location_ids

    game_region.add_locations(level_location_ids, BeatblockLocation)
    
    if world.options.fishsanity:
        fishing_room = world.get_region("Fishing")
        fish_location_ids = get_location_names_with_ids(fish_locations)
        fishing_room.add_locations(fish_location_ids, BeatblockLocation)
        
def create_events(world: BeatblockWorld) -> None:
    # Add completion event
    game_region = world.get_region(origin_region)

    game_region.add_event(VICTORY_LOCATION + " (B- or Above)", "Victory", location_type=BeatblockLocation, item_type=items.BeatblockItem)