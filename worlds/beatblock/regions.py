from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region

from .data import origin_region

if TYPE_CHECKING:
    from .world import BeatblockWorld

def create_and_connect_regions(world: BeatblockWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BeatblockWorld) -> None:
    game_region = Region(origin_region, world.player, world.multiworld)

    regions = [game_region]

    if world.options.fishsanity:
        fishing_room = Region("Fishing", world.player, world.multiworld)
        regions.append(fishing_room)

    world.multiworld.regions += regions

def connect_regions(world: BeatblockWorld) -> None:
    game_region = world.get_region(origin_region)

    if world.options.fishsanity:
        fishing_room = world.get_region("Fishing")
        game_region.connect(fishing_room, "fishing special")