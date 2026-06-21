# NOTE: Brub i dont even use items in the rules.py file

from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BeatblockWorld

from .options import Fishsanity
from .data import levels_list, game_name

STARTING_ITEM = ""
ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

def create_item_list(world: BeatblockWorld) -> None:
    counter = 100
    # Levels :3
    for i, item in enumerate(levels_list):
        ITEM_NAME_TO_ID[item] = counter
        DEFAULT_ITEM_CLASSIFICATIONS[item] = ItemClassification.progression
        counter += 1

def create_item_list_add_fish(world: BeatblockWorld) -> None:
    counter = 100 + len(levels_list)
    # Fish :drool:
    if world.options.fishsanity.value:
        ITEM_NAME_TO_ID["Fishing Rod"] = counter
        DEFAULT_ITEM_CLASSIFICATIONS["Fishing Rod"] = ItemClassification.progression
        counter += 1


# Add costumes here i guess

# TODO add costumes

class BeatblockItem(Item):
    game = game_name

def get_random_filler_item_name(world: BeatblockWorld) -> str:
    return "A Beat maybe a block"

def create_item_with_correct_classification(world: BeatblockWorld, name: str) -> BeatblockItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return BeatblockItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: BeatblocktWorld) -> None:
    create_item_list(world)

    STARTING_ITEM = world.random.choice(levels_list)

    create_item_list_add_fish(world)

    itempool: list[Item] = []

    starting_item = None
    for item in ITEM_NAME_TO_ID:
        if item == STARTING_ITEM:
            starting_item = world.create_item(item)
            world.push_precollected(starting_item)
            continue
        itempool.append(world.create_item(item))
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool