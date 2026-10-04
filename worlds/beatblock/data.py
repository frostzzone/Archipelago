game_name = "Beatblockapelago"

origin_region = "game"

# Level names are case sensitive
GAME = {
    "Intro" : [
        "Tutorial", #You start with this anyways because the game demands it
        "Shinamon no Neko",
        "Move Right Along!",
        "so stressed!",
        "Rhythmic Shield",
    ],
    "Mines" : [
        "Through the Static",
        "Gritted Strings",
        "BLOW A FUSE",
        "Femme Fatale",
        "Take A Number (Polished Gem Mix)",
    ],
    "Bounces" : [
        "Night Echo (Future Funk Mix)",
        "Ladybug Castle",
        "Cache",
        "BEATROCK (get it?)",
    ],
    "Inverses" : [
        "Cobblestone Counterpoint",
        "Island of Orchids",
        "selfportrait",
        "UNDO UNDO",
        "ILOVEYOU.vbs",
    ],
    "Sides" : [
        "publico cautivo",
        "3-Bit Bebop",
        "AU CONTRAIRE",
        "Triplet Test",
        "Destroy, Destroy (ft. eili)",
    ],
    "Fusion" : [
        "Lawrence",
        "Heated Battle! ~ Disco Bakery",
        "C-ミ B-ミ",
        "Omelette Cafe By Road 38",
        "cloud factory",
        "Fragmented Existence",
        ":))))",
    ],
    "Master" : [
        "DAMOCLISM",
        "+ERABY+E CONNEC+10N",
        "NISENEN",
        "Novena",
        "what's a keygen?", # THIS IS LOWERCASE BECAUSE STOOPID
        "Era Chimaera",
    ],
    "Collab" : [
        "Code Remix",
        "Lucky Break",
        "Empty Diary",
        "Spin Cycle",
        "heptagramme",
        "Recollection (ft. Risa Kodaka)",
    ],
    # You're not allowed to tanget becasue we are EVIL
    # "Freeplay" : [
    #     "gone fishin'"
    # ]
}

# Exclude tutorial?
levels_list = [
    level
    for atom_levels in GAME.values()
    for level in atom_levels
    if level != "Tutorial"
]

atom_list = list(GAME.keys())

costumes_list = [
	# "random",
	# "none",
	"tophat",
	"pirate",
	"dogears",
	"chefhat",
	"gearshift",
	"jolly",
	"jester",

	"gradcap",
	"origami",
	"catears",
	"square",
	
	"mine",
	"cowboy",
	"antispiralglasses",
	
	"antennae",
	"triangle",
	"spike",
	
	"bricks",
	"bunny",
	"inverted",

	"huxley",
	"construction",
	"shades",
	"antique",
	
	"lawrence",
	"invisible",
	"stache",
	"bulb",
	"cloudy",
	"novena",
	
	"crown",
	"blob",
	"fedora",
	"atom",
	
	"samurai",
	"2p5d",
	"ribbon",
	"heptagramme",
	"jimspim",
	"0ssembli",
	"rfandf"
]

fish_list = [
    "blockjaw",
    "heeld",
    "puffermine",
    "hammerside",
    "inversalmon",
    "burbounce",
    "tutorbass",
    "cubelacanth",
    "catgirlfish",
    "armorana",
    "staticback",
    "gritgill",
    "blowafish",
    "allstarfish",
    "ladybug",
    "goldfish",
    "sheatrock",
    "signyfin",
    "orangeoarchid",
    "selfish",
    "sharpen",
    "suckerphish",
    "proofofperchase",
    "bebocaccio",
    "ditheredfish",
    "pianosesolphin",
    "bonesfish",
    "gearstropod",
    "deepcsmelt",
    "sunnyfish",
    "twofish",
    "stringfish",
    "seaplane",
    "teradon",
    "lefisheauchocolat",
    "falsechimaera",
    "codefish",
    "homerudd",
    "unbelugable",
    "turntadpole",
    "wholelobster",
    "groovecroakster",
    "guitarherring",
    "beatmantaray",
    "playdart",
    "jazzy"
]

ranks_list = [
    "p",
    "s plus",
    "s",
    "a plus",
    "a",
    "b plus",
    "b",
    "b minus",
    "c plus",
    "c",
    "c minus",
    "d plus",
    "d",
    "d minus",
    "f",
]

amount_of_costumes = len(costumes_list)

amount_of_fish = len(fish_list)

amount_of_levels = len(levels_list)

amount_of_ranks = len(ranks_list)