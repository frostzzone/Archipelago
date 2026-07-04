from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
import re

from . import items

if TYPE_CHECKING:
    from .world import BeatblockWorld

from .options import Ranksanity, TargetRank, Fishsanity

# Replace amount_of_fish with actual fish_list when it is implemented
from .data import game_name, origin_region, levels_list, ranks_list, amount_of_fish

# Buh, levles
level_dict: dict[str, list[str]] = {} # { location_name: [ Check, Check, ...]}

# Every location registered
rank_locations: list[str] = []
fish_locations: list[str] = []

LOCATION_TO_ID = {}
# for simplicity on the client side
ID_TO_LOCATION = {}

def create_location_list() -> None:
    counter = 1100
    # Levels
    for loc in levels_list:
         # Rank checks
        for rank in ranks_list:
            location_name = f"{loc} Get {rank} Rank"
            rank_locations.append(location_name)

            LOCATION_TO_ID[location_name] = counter
            ID_TO_LOCATION[counter] = location_name
            counter += 1

    # Fish
    for i in range(1, amount_of_fish + 1):
        location_name = f"Catch {i} Fish"
        fish_locations.append(location_name)
        LOCATION_TO_ID[location_name] = counter
        ID_TO_LOCATION[counter] = location_name
        counter += 1

def create_level_locations(world: BeatblockWorld) -> None:
    # Levels
    target_rank = ranks_list[world.options.target_rank.value]
    victory_location = levels_list[world.options.goal_level.value]

    for rank in rank_locations:
        # if rank has victory location in the string, skip it
        if rank.find(victory_location) != -1:
            continue

        # Regex for location because im stupid
        match = re.search(r"^(.*?) Get (.*?) Rank$", rank)

        loc = match.group(1)
        rank_letter = match.group(2)

        if loc not in level_dict:
            level_dict[loc] = []

        if world.options.ranksanity.value == True:
            level_dict[loc].append(rank)
        elif world.options.ranksanity.value == False and rank_letter == target_rank:
            level_dict[loc].append(rank)

    # Fish
    # if world.options.fishsanity.value == True:
    #     print("Fish")

create_location_list()

class BeatblockLocation(Location):
    game = game_name

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: BeatblockWorld) -> None:
    create_level_locations(world)

    create_regular_locations(world)
    create_events(world)

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

    game_region.add_event(levels_list[world.options.goal_level.value] + " (B- or Above)", "Victory", location_type=BeatblockLocation, item_type=items.BeatblockItem)