# NOTE: Brub i dont even use items in the rules.py file

from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BeatblockWorld

from .options import Fishsanity
from .data import levels_list, game_name

STARTING_ITEM = ""
ITEM_NAME_TO_ID = {}
ITEM_ID_TO_NAME = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

def add_item(name: str, item_id: int, classification: ItemClassification = ItemClassification.progression) -> None:
    ITEM_NAME_TO_ID[name] = item_id
    ITEM_ID_TO_NAME[item_id] = name
    DEFAULT_ITEM_CLASSIFICATIONS[name] = classification

def create_item_list() -> None:
    add_item("A Beat maybe a block", 10, ItemClassification.filler)

    counter = 100
    for i, item in enumerate(levels_list):
        add_item(item, counter)
        counter += 1
    
    add_item("Fishing Rod", counter)
    counter += 1

# def create_item_list_add_fish(world: BeatblockWorld) -> None:
#     counter = 100 + len(levels_list)
#     # Fish :drool:
#     if world.options.fishsanity.value:
        

create_item_list()

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
    STARTING_ITEM = world.random.choice(levels_list)

    itempool: list[Item] = []

    starting_item = None
    for item in ITEM_NAME_TO_ID:
        # Ignore fishing rod if fishsanity is off
        if not world.options.fishsanity.value and item == "Fishing Rod":
            print("skipping fishing rod")
            continue

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