# CONSTANT VARIABLES
DELAYS = {
    'loading_screen': 3000,
    'ingredient_cooking_induction': 2.9897,
    'crop_processing_induction': 5.01
}
LOCATIONS = {
    'hobbiton': 'hobbiton',
    'thorins_hall': 'thorins_hall'
}
KNOWN_VENDORS = [
    'olo_proudfoot',
    'porto_brownlock',
    'novice_farmhand',
    'expert_farmhand'
]

# CHARACTER CONFIGURATIONS
CONFIG = {
    'screen_dimensions': (1920, 1080),
    'farming_tools_harvesting_deduction': 3000,
    'location': LOCATIONS['hobbiton']
}

# CONFIG DEPENDENTS
BOXES = {
    'collapse_all': (35, 85, 10, 10),
    'portraits': (10, 20, 570, 50),
    'buttons': {
        'make': (645, 525, 65, 15),
        'make_all': (720, 530, 60, 10),
        'repair_all': (1750 - (1920 - CONFIG['screen_dimensions'][0]), 450, 60, 10),
        'browse_the_shop': (22, 330, 165, 15)
    },
    'tabs': {
        'repair': (1805 - (1920 - CONFIG['screen_dimensions'][0]), 70, 80, 10),
        'farmer': (60, 50, 125, 12),
        'cook': (130, 30, 125, 12)
    },
    'tiers': {
        'minas_ithil': (15, 345, 100, 12),
        'gundabad': (15, 364, 100, 12)
    },
    'categories': {
        'minas_ithil_vegetables': (23, 382, 90, 10),
        'minas_ithil_ingredients': (25, 398, 100, 12),
        'gundabad_vegetables': (24, 400, 90, 10)
    },
    'recipes': {
        'minas_ithil_field': (40, 400, 125, 10),
        'bunch_of_par_cooked_vegetables': (35, 414, 165, 12),
        'vegetable_treble': (36, 432, 160, 10),
        'gundabad_field': (35, 432, 120, 10)
    }
}
KEY_BINDINGS = {
    'movement': {
        'move_forward': 'e',
        'move_backward': 'd',
        'rotate_left': 's',
        'rotate_right': 'f',
    },
    'selection': {
        'select_nearest_item': ('ctrl', 'alt', 'i'),
        'select_next_item': ('ctrl', 'shift', 'i'),
        'select_nearest_npc': ('ctrl', 'alt', 'n'),
        'select_next_npc': ('ctrl', 'shift', 'n'),
        'utilize_selection': 'u',
    },
    'skills': {
        'track_crops': '-',
        'find_the_path': '=',
        'guide_to_thorins_hall': '1',
    }
}
