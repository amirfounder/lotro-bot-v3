import math
import random
import time

import mss.tools
import pyautogui
import pydirectinput
import pytesseract
from PIL import Image

# CONSTANTS
sct = mss.mss()
SCREEN_RES = (1920, 1080)
SCALE_X, SCALE_Y = 1920 / SCREEN_RES[0], 1080 / SCREEN_RES[1]

BOXES = {
    'collapse_all': (35 * SCALE_X, 85 * SCALE_Y, 10 * SCALE_X, 10 * SCALE_Y),
    'portraits': (10 * SCALE_X, 20 * SCALE_Y, 570 * SCALE_X, 50 * SCALE_Y),
    'buttons': {
        'make': (645 * SCALE_X, 525 * SCALE_Y, 65 * SCALE_X, 15 * SCALE_Y),
        'make_all': (720 * SCALE_X, 530 * SCALE_Y, 60 * SCALE_X, 10 * SCALE_Y),
        'repair_all': (1750 * SCALE_X, 450 * SCALE_Y, 60 * SCALE_X, 10 * SCALE_Y)
    },
    'tabs': {
        'repair': (1805 * SCALE_X, 70 * SCALE_Y, 80 * SCALE_X, 10 * SCALE_Y),
        'farmer': (60 * SCALE_X, 50 * SCALE_Y, 125 * SCALE_X, 12 * SCALE_Y),
        'cook': (130 * SCALE_X, 30 * SCALE_Y, 125 * SCALE_X, 12 * SCALE_Y)
    },
    'tiers': {
        'minas_ithil': (15 * SCALE_X, 345 * SCALE_Y, 100 * SCALE_X, 12 * SCALE_Y)
    },
    'categories': {
        'minas_ithil_vegetables': (23 * SCALE_X, 382 * SCALE_Y, 90 * SCALE_X, 10 * SCALE_Y),
        'minas_ithil_ingredients': (25 * SCALE_X, 398 * SCALE_Y, 100 * SCALE_X, 12 * SCALE_Y)
    },
    'recipes': {
        'minas_ithil_field': (40 * SCALE_X, 400 * SCALE_Y, 125 * SCALE_X, 10 * SCALE_Y),
        'bunch_of_par_cooked_vegetables': (35 * SCALE_X, 414 * SCALE_Y, 165 * SCALE_X, 12 * SCALE_Y)
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
    print(f'Generated random coordinates: {rand_x}, {rand_y}')
    return rand_x, rand_y


def generate_random_time(target=200, margin=390):
    rand_time = random.randint(int(target - margin / 2), int(target + margin / 2))
    print(f'Generated random time: {rand_time} ms')
    return rand_time


def generate_random_delay(target=200, margin=200):
    rand_delay = generate_random_time(target, margin) / 1000
    time.sleep(rand_delay)
    print(f'Generated random delay: {rand_delay} sec')


# MOUSE INTERACTIONS CORE
def click(box):
    x, y = generate_random_coords(box)
    duration = generate_random_time() / 1000
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()
    print(f'Clicked on screen at: {x}, {y}; Mouse travel time: {duration}')
    generate_random_delay()


# MOUSE INTERACTIONS
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
    click(BOXES['buttons']['make_all'])


# CRAFTING
def collapse_all_tiers():
    click(BOXES['collapse_all'])


def toggle_minas_ithil_tier():
    click(BOXES['tiers']['minas_ithil'])


def toggle_minas_ithil_vegetables():
    click(BOXES['categories']['minas_ithil_vegetables'])


def toggle_minas_ithil_field():
    click(BOXES['recipes']['minas_ithil_field'])


def toggle_minas_ithil_ingredients():
    click(BOXES['categories']['minas_ithil_ingredients'])


def toggle_bunch_of_par_cooked_vegetables():
    click(BOXES['recipes']['bunch_of_par_cooked_vegetables'])


# MOVEMENTS
def move(key, duration_ms=0):
    if duration_ms == 0:
        pydirectinput.press(key)
        generate_random_delay()
        return
    pydirectinput.keyDown(key)
    time.sleep(duration_ms / 1000)
    pydirectinput.keyUp(key)


def rotate(key, degrees):
    duration_ms = generate_random_time(degrees * 5, 20)
    pydirectinput.keyDown(key)
    time.sleep(duration_ms / 1000)
    pydirectinput.keyUp(key)
    generate_random_delay()


def move_forward(duration_ms=0):
    move(KEY_BINDINGS['movement']['move_forward'], duration_ms)


def move_backward(duration_ms=0):
    move(KEY_BINDINGS['movement']['move_backward'], duration_ms)


def rotate_right(degrees):
    rotate(KEY_BINDINGS['movement']['rotate_right'], degrees)


def rotate_left(degrees):
    rotate(KEY_BINDINGS['movement']['rotate_left'], degrees)


# SELECTIONS
def hotkey(*args):
    print(f'Clicked hotkey: {args}')
    args = list(args)
    for i in args:
        pydirectinput.keyDown(i)
    args.reverse()
    for i in args:
        pydirectinput.keyUp(i)
    generate_random_delay()


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
    generate_random_delay()


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
    move_forward(generate_random_time(1750, 500))

    # GO TO THE FARMING FACILITY
    generate_random_delay(1250, 500)
    rotate_left(90)
    move_forward(generate_random_time(3100, 200))
    rotate_left(180)

    # FARM
    for i in range(1):
        pydirectinput.press('t')
        collapse_all_tiers()
        click_farmer_tab()
        toggle_minas_ithil_tier()
        toggle_minas_ithil_vegetables()
        toggle_minas_ithil_field()
        for i in range(34):
            click_make_button()
            hotkey('ctrl', 'alt', 'i')
            utilize_selection()

        pydirectinput.press('t')
        hotkey('ctrl', 'shift', 'n')

        # sct.grab docs accept only dicts, but works with tuple
        # noinspection PyTypeChecker
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
        click_repair_tab()
        click_repair_all_button()
        pydirectinput.press('esc')
        pydirectinput.press('esc')
        move_backward(generate_random_time(3500, 250))


def make(total, batch_count):
    leftover = total % (batch_count * 2)
    click_cook_tab()
    collapse_all_tiers()
    toggle_minas_ithil_tier()
    toggle_minas_ithil_ingredients()
    toggle_bunch_of_par_cooked_vegetables()
    for i in range(math.floor(total / batch_count * 2)):
        click_make_all_button()
        for j in range(batch_count):
            time.sleep(2.9897)
            print(f'Successfully completed "make" (Total: ~{j + 1}; Left: ~{batch_count + batch_count - j - 1})')
        generate_random_delay(1150, 200)
        move_forward()
        click_repair_tab()
        click_repair_all_button()
        click_make_all_button()
        for j in range(batch_count):
            time.sleep(2.9897)
            print(f'Successfully completed "make" (Total: ~{j + batch_count + 1}; Left: ~{batch_count - j - 1})')
        generate_random_delay(1150, 200)
        move_backward()
        click_repair_tab()
        click_repair_all_button()
        print(f'Successfully completed batch (Total: {i + 1}; Left: {total - batch_count * 2 - 1})')
    if batch_count > leftover > 0:
        click_make_all_button()
        time.sleep(4 * leftover)
        for j in range(batch_count):
            time.sleep(2.9897)
            print(f'Successfully completed "make" (Total: ~{j + 1}; Left: {leftover - j - 1})')
        generate_random_delay(1150, 200)
        move_backward()
        click_repair_tab()
        click_repair_all_button()
        click_make_all_button()
        for j in range(leftover):
            time.sleep(2.9897)
            print(f'Successfully completed "make" (Total: ~{j + 1}; Left: {leftover - batch_count - j - 1})')
        generate_random_delay(1150, 200)
        move_backward()
        click_repair_tab()
        click_repair_all_button()
    else:
        click_make_all_button()
        for j in range(leftover):
            time.sleep(2.9897)
            print(f'Successfully completed "make" (Total: ~{j + 1}; Left: {leftover - j - 1})')
        generate_random_delay(1150, 200)
        move_backward()
        click_repair_tab()
        click_repair_all_button()
    print('done')


countdown()
farm()
