from collections.abc import Mapping
from typing import Any

import json

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules#, web_world
from . import options as beatblock_options

from .data import game_name, origin_region

class BeatblockWorld(World):
    """
    Beatblock is a headspinning rhythm game with a simple goal: hit blocks to the beat as the paddle-wielding Cranky. The song revolves around you, and it's your job to keep up.
    """

    game = game_name

    options_dataclass = beatblock_options.BeatblockOptions
    options: beatblock_options.BeatblockOptions

    # These dont work, fix them
    location_name_to_id = locations.LOCATION_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = origin_region

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
    
    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BeatblockItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # return self.options.as_dict(
        #     "fishsanity", "ranksanity", "target_rank", "custom_levels"
        # )

        return self.fill_json_data()
    
    def fill_json_data(self) -> Mapping[str, Any]:
        print(self.location_name_to_id)
        print(self.item_name_to_id)

        self.location_name_to_id = locations.LOCATION_TO_ID
        self.item_name_to_id = items.ITEM_NAME_TO_ID

        # Get of the custom levels here ig

        base_data = {
            "goal_level": self.options.goal_level.value,
            "death_link": bool(self.options.deathlink),
            "fishsanity": bool(self.options.fishsanity),
            "ranksanity": bool(self.options.ranksanity),
            "target_rank": self.options.target_rank.value,
            "locations": json.dumps(locations.ID_TO_LOCATION),
            "items": json.dumps(items.ITEM_ID_TO_NAME),
            # "custom_levels": self.options.custom_levels,
        }

        return base_data