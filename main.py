import random
import time

import mss.tools
import pyautogui
import pydirectinput
import pytesseract
from PIL import Image

# CONSTANTS

sct = mss.mss()

BOXES = {
    'collapse_all': (35, 85, 10, 10),
    'portraits': (10, 20, 570, 50),
    'buttons': {
        'make': (645, 525, 65, 15),
        'make_all': (720, 530, 60, 10),
        'repair_all': (1750, 450, 60, 10)
    },
    'tabs': {
        'repair': (1805, 70, 80, 10),
        'farmer': (60, 50, 125, 12),
        'cook': (130, 30, 125, 12)
    },
    'tiers': {
        'minas_ithil': (15, 345, 100, 12)
    },
    'categories': {
        'minas_ithil_vegetables': (23, 382, 90, 10)
    },
    'recipes': {
        'minas_ithil_field': (40, 400, 125, 10)
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


# RANDOM GENERATORS
def generate_random_coords(box):
    x, y, w, h = box
    rand_x = random.randint(x, x + w)
    rand_y = random.randint(y, y + h)
    return rand_x, rand_y


def generate_random_time(default=500, margin=500):
    return random.randint(int(default - margin / 2), int(default + margin / 2))


# MOUSE INTERACTIONS
def click(box):
    x, y = generate_random_coords(box)
    duration = generate_random_time() / 1000
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()


def click_repair_tab():
    click(BOXES['tabs']['repair'])


def click_farmer_tab():
    click(BOXES['tabs']['farmer'])


def click_cook_tab():
    click(BOXES['tabs']['cook'])


def click_repair_all_button():
    click(BOXES['buttons']['repair_all'])


def click_make_button():
    click(BOXES['buttons']['make'])


def click_make_all_button():
    click(BOXES['button']['make_all'])


# CRAFTING
def collapse_all_tiers():
    click(BOXES['collapse_all'])


def toggle_minas_ithil_tier():
    click(BOXES['tiers']['minas_ithil'])


def toggle_minas_ithil_vegetables():
    click(BOXES['categories']['minas_ithil_vegetables'])


def toggle_minas_ithil_field():
    click(BOXES['recipes']['minas_ithil_field'])


# MOVEMENTS
def move(key, duration_ms=0):
    if duration_ms == 0:
        pydirectinput.press(key)
        return
    pydirectinput.keyDown(key)
    time.sleep(duration_ms / 1000)
    pydirectinput.keyUp(key)


def rotate(key, degrees):
    duration_ms = generate_random_time(degrees * 5, 20)
    pydirectinput.keyDown(key)
    time.sleep(duration_ms / 1000)
    pydirectinput.keyUp(key)


def move_forward(duration_ms):
    move(KEY_BINDINGS['movement']['move_forward'], duration_ms)


def move_backward(duration_ms):
    move(KEY_BINDINGS['movement']['move_backward'], duration_ms)


def rotate_right(degrees):
    rotate(KEY_BINDINGS['movement']['rotate_right'], degrees)


def rotate_left(degrees):
    rotate(KEY_BINDINGS['movement']['rotate_left'], degrees)


# SELECTIONS
def hotkey(*args):
    args = list(args)
    for i in args:
        pydirectinput.keyDown(i)
    args.reverse()
    for i in args:
        pydirectinput.keyUp(i)


def select_nearest_item():
    hotkey(KEY_BINDINGS['select_nearest_item'])


def select_nearest_npc():
    hotkey(KEY_BINDINGS['select_nearest_npc'])


def select_next_item():
    hotkey(KEY_BINDINGS['select_next_item'])


def select_next_npc():
    hotkey(KEY_BINDINGS['select_next_npc'])


def utilize_selection():
    pydirectinput.press(KEY_BINDINGS['selection']['utilize_selection'])


# SKILLS
def guide_to_thorins_hall():
    pydirectinput.press(KEY_BINDINGS['skills']['guide_to_thorins_hall'])
    time.sleep(generate_random_time(11000, 500) / 1000)


# MAIN CALLS
def countdown():
    w, h = pyautogui.size()
    click((int(w / 4), int(h / 4), int(w / 2 - 10), int(h / 2 - 10)))
    print('starting bot...')
    for i in range(3):
        print(f'{3 - i}...')
        time.sleep(1)


def setup_buffs():
    for i in range(3):
        pydirectinput.press(KEY_BINDINGS['skills']['track_crops'])
    time.sleep(generate_random_time(3500, 500))
    for i in range(3):
        pydirectinput.press(KEY_BINDINGS['skills']['find_the_path'])
    time.sleep(generate_random_time(11500, 500))


# FARM AND SETUP FARM
def farm():
    guide_to_thorins_hall()

    # GO TO THE GREENHOUSE
    rotate_left(90)
    move_forward(generate_random_time(5000, 250))
    hotkey('ctrl', 'alt', 'i')
    utilize_selection()
    time.sleep(generate_random_time(1000, 250) / 1000)
    move_forward(generate_random_time(1750, 500))

    # GO TO THE FARMING FACILITY
    time.sleep(generate_random_time(750, 200) / 1000)
    rotate_left(90)
    move_forward(generate_random_time(3100, 200))
    time.sleep(generate_random_time(400, 200) / 1000)
    rotate_left(180)

    # FARM
    for i in range(3):
        pydirectinput.press('t')
        time.sleep(generate_random_time(100, 90) / 1000)
        collapse_all_tiers()
        time.sleep(generate_random_time(100, 90) / 1000)
        click_farmer_tab()
        time.sleep(generate_random_time(100, 90) / 1000)
        toggle_minas_ithil_tier()
        time.sleep(generate_random_time(100, 90) / 1000)
        toggle_minas_ithil_vegetables()
        time.sleep(generate_random_time(100, 90) / 1000)
        toggle_minas_ithil_field()
        for i in range(3):
            click_make_button()
            pydirectinput.press('t')
            time.sleep(generate_random_time(3250, 250) / 1000)
            hotkey('ctrl', 'alt', 'i')
            utilize_selection()
            time.sleep(generate_random_time(6000, 500) / 1000)
            pydirectinput.press('t')
            time.sleep(generate_random_time(200, 190) / 1000)

        pydirectinput.press('t')
        time.sleep(generate_random_time(200, 190) / 1000)
        hotkey('ctrl', 'shift', 'n')

        img = sct.grab(BOXES['portraits'])
        img = Image.frombytes("RGB", img.size, img.bgra, 'raw', 'BGRX')
        text = pytesseract.image_to_string(img)

        text = text.strip().lower()

        if "expert" not in text or "farmhand" not in text:
            hotkey('ctrl', 'shift', 'n')

            img = sct.grab(BOXES['portraits'])
            img = Image.frombytes("RGB", img.size, img.bgra, 'raw', 'BGRX')
            text = pytesseract.image_to_string(img)

            text = text.strip().lower()

            if "expert not in text" or "farmhand" not in text:
                raise Exception("Unable to find the expert farmhand")

        utilize_selection()
        time.sleep(generate_random_time(2250, 500) / 1000)
        click_repair_tab()
        time.sleep(generate_random_time(100, 90) / 1000)
        click_repair_all_button()
        time.sleep(generate_random_time(100, 90) / 1000)
        pydirectinput.press('esc')
        time.sleep(generate_random_time(100, 90) / 1000)
        pydirectinput.press('esc')
        move_backward(generate_random_time(3500, 250))
        time.sleep(generate_random_time(100, 90) / 1000)

countdown()
farm()