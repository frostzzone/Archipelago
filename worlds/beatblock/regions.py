from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region

from .data import origin_region

if TYPE_CHECKING:
    from .world import BeatblockWorld

# GAME >
#   FISHING
#   INTRO > [levels]
#   MINES > [levels]
#   BOUNCES > [levels]
#   INVERSES > [levels]
#   SIDES > [levels]
#   Fusion > [levels]
#   Master > [levels]
#   COLLAB > [levels]

def create_and_connect_regions(world: BeatblockWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BeatblockWorld) -> None:
    game_region = Region(origin_region, world.player, world.multiworld)

    intro_atom = Region("Intro", world.player, world.multiworld)
    mines_atom = Region("Mines", world.player, world.multiworld)
    bounces_atom = Region("Bounces", world.player, world.multiworld)
    inverses_atom = Region("Inverses", world.player, world.multiworld)
    sides_atom = Region("Sides", world.player, world.multiworld)
    fusion_atom = Region("Fusion", world.player, world.multiworld)
    master_atom = Region("Master", world.player, world.multiworld)
    collab_atom = Region("Collab", world.player, world.multiworld)

    regions = [
        game_region,
        intro_atom,
        mines_atom,
        bounces_atom,
        inverses_atom,
        sides_atom,
        fusion_atom,
        master_atom,
        collab_atom
    ]

    if world.options.fishsanity.value:
        fishing_room = Region("Fishing", world.player, world.multiworld)
        regions.append(fishing_room)

    world.multiworld.regions += regions

def connect_regions(world: BeatblockWorld) -> None:
    game_region = world.get_region(origin_region)

    intro_atom = world.get_region("Intro")
    mines_atom = world.get_region("Mines")
    bounces_atom = world.get_region("Bounces")
    inverses_atom = world.get_region("Inverses")
    sides_atom = world.get_region("Sides")
    fusion_atom = world.get_region("Fusion")
    master_atom = world.get_region("Master")
    collab_atom = world.get_region("Collab")

    game_region.connect(intro_atom, "Intro atom", lambda state: state.has("Intro Key", world.player))
    game_region.connect(mines_atom, "Mines atom", lambda state: state.has("Mines Key", world.player))
    game_region.connect(bounces_atom, "Bounces atom", lambda state: state.has("Bounces Key", world.player))
    game_region.connect(inverses_atom, "Inverses atom", lambda state: state.has("Inverses Key", world.player))
    game_region.connect(sides_atom, "Sides atom", lambda state: state.has("Sides Key", world.player))
    game_region.connect(fusion_atom, "Fusion atom", lambda state: state.has("Fusion Key", world.player))
    game_region.connect(master_atom, "Master atom", lambda state: state.has("Master Key", world.player))
    game_region.connect(collab_atom, "Collab atom", lambda state: state.has("Collab Key", world.player))

    if world.options.fishsanity.value:
        fishing_room = world.get_region("Fishing")
        game_region.connect(fishing_room, "fishing special")