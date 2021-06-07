import math
import random
import time

import mss.tools
import pyautogui
import pydirectinput

# CONSTANTS
import constants
from imaging import screenshot_portraits, convert_to_text


# RANDOM GENERATORS
def generate_random_coords(box):
    x, y, w, h = box
    rand_x = random.randint(x, x + w)
    rand_y = random.randint(y, y + h)
    print(f'Generated random coordinates: {rand_x}, {rand_y}')
    return rand_x, rand_y


def generate_random_time(target=350, margin=690):
    rand_time = random.randint(int(target - margin / 2), int(target + margin / 2))
    print(f'Generated random time: {rand_time} ms')
    return rand_time


def generate_random_delay(target=350, margin=690):
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
def click_center_of_screen():
    w, h = pyautogui.size()
    click((int(w / 5), int(h / 5), int(w / 2.5 - 10), int(h / 2.5 - 10)))


def click_repair_tab():
    click(constants.BOXES['tabs']['repair'])


def click_farmer_tab():
    click(constants.BOXES['tabs']['farmer'])


def click_cook_tab():
    click(constants.BOXES['tabs']['cook'])


def click_repair_all_button():
    click(constants.BOXES['buttons']['repair_all'])


def click_make_button():
    click(constants.BOXES['buttons']['make'])


def click_make_all_button():
    click(constants.BOXES['buttons']['make_all'])
    print('Clicked make all button')


def browse_the_shop():
    click(constants.BOXES['buttons']['browse_the_shop'])


# CRAFTING
def collapse_all_tiers():
    click(constants.BOXES['collapse_all'])
    print('Collapsed all tiers')


def toggle_minas_ithil_tier():
    click(constants.BOXES['tiers']['minas_ithil'])
    print('Toggled minas ithil tier')


def toggle_minas_ithil_vegetables():
    click(constants.BOXES['categories']['minas_ithil_vegetables'])
    print('Toggled minas ithil tier')


def toggle_minas_ithil_field():
    click(constants.BOXES['recipes']['minas_ithil_field'])
    print('Toggled minas ithil field recipe')


def toggle_vegetable_treble():
    click(constants.BOXES['recipes']['vegetable_treble'])
    print('Toggled vegetable treble recipe')


def toggle_minas_ithil_ingredients():
    click(constants.BOXES['categories']['minas_ithil_ingredients'])
    print('Toggled minas ithil ingredients categories')


def toggle_bunch_of_par_cooked_vegetables():
    click(constants.BOXES['recipes']['bunch_of_par_cooked_vegetables'])
    print('Toggled bunch of par cooked vegetables recipe')


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
    duration_ms = generate_random_time(degrees * 5, 10)
    pydirectinput.keyDown(key)
    time.sleep(duration_ms / 1000)
    pydirectinput.keyUp(key)
    generate_random_delay()


def move_forward(duration_ms=50, duration_margin_ms=90):
    move(
        constants.KEY_BINDINGS['movement']['move_forward'],
        generate_random_time(duration_ms, duration_margin_ms)
    )


def move_backward(duration_ms=50, duration_margin_ms=90):
    move(
        constants.KEY_BINDINGS['movement']['move_backward'],
        generate_random_time(duration_ms, duration_margin_ms)
    )


def rotate_right(degrees):
    rotate(constants.KEY_BINDINGS['movement']['rotate_right'], degrees)


def rotate_left(degrees):
    rotate(constants.KEY_BINDINGS['movement']['rotate_left'], degrees)


# SELECTIONS
def hotkey(args):
    print(f'Clicked hotkey: {args}')
    args = list(args)
    for i in args:
        pydirectinput.keyDown(i)
    args.reverse()
    for i in args:
        pydirectinput.keyUp(i)
    generate_random_delay()


def select_nearest_item():
    hotkey(constants.KEY_BINDINGS['selection']['select_nearest_item'])


def select_nearest_npc():
    hotkey(constants.KEY_BINDINGS['selection']['select_nearest_npc'])


def select_next_item():
    hotkey(constants.KEY_BINDINGS['selection']['select_next_item'])


def select_next_npc():
    hotkey(constants.KEY_BINDINGS['selection']['select_next_npc'])


def utilize_selection():
    pydirectinput.press(constants.KEY_BINDINGS['selection']['utilize_selection'])
    print('Utilized selection')
    generate_random_delay()


# SKILLS
def guide_to_thorins_hall():
    pydirectinput.press(constants.KEY_BINDINGS['skills']['guide_to_thorins_hall'])
    time.sleep(generate_random_time(11000, 500) / 1000)


# SETUPS
def setup_buffs():
    for i in range(3):
        pydirectinput.press(constants.KEY_BINDINGS['skills']['track_crops'])
    time.sleep(generate_random_time(3500, 500))
    for i in range(3):
        pydirectinput.press(constants.KEY_BINDINGS['skills']['find_the_path'])
    time.sleep(generate_random_time(11500, 500))


def setup_thorins_hall_farm(greenhouse_station='right'):
    guide_to_thorins_hall()
    generate_random_delay(constants.DELAYS['loading_screen'])

    rotate_left(90)
    generate_random_delay()
    move_forward(5500)
    select_nearest_item()

    # UTILIZE TWICE IN CASE INTERRUPTION FROM NOT IN RANGE ERROR
    utilize_selection()
    generate_random_delay(500)
    utilize_selection()
    generate_random_delay()
    move_forward(1500)

    # GO TO THE FARMING FACILITY
    generate_random_delay(constants.DELAYS['loading_screen'])
    rotate_right(90) if greenhouse_station == 'right' else rotate_left(90)
    move_forward(3250)
    rotate_left(90) if greenhouse_station == 'right' else rotate_right(90)


# MAIN HELPERS
def travel_to_selected_vendor(selected_npc, greenhouse_station='right'):
    utilize_selection()
    if constants.CONFIG['location'] == constants.LOCATIONS['thorins_hall']:
        generate_random_delay(3000) if greenhouse_station == 'right' else generate_random_delay(6000)
    elif constants.CONFIG['location'] == constants.LOCATIONS['hobbiton']:
        if selected_npc == 'porto_brownlock' or selected_npc == 'novice_farmhand':
            generate_random_delay(3000)
            browse_the_shop()
            generate_random_delay()
    else:
        generate_random_delay(5000)


def return_to_crafting_facility(greenhouse_station='right'):
    generate_random_delay()
    if constants.CONFIG['location'] == constants.LOCATIONS['thorins_hall']:
        move_backward(3500) if greenhouse_station == 'right' else move_backward(7500)
    else:
        move_backward(4000)


def identify_selected_npc(text):
    if constants.CONFIG['location'] == constants.LOCATIONS['thorins_hall']:
        if 'expert' or 'farmhand' in text:
            return 'expert_farmhand'
        elif 'novice' or 'farmhand' in text:
            return 'novice_farmhand'
        else:
            return None
    elif constants.CONFIG['location'] == constants.LOCATIONS['hobbiton']:
        if 'porto' or 'brownlock' in text:
            return 'porto_brownlock'
        elif 'olo' or 'proudfoot' in text:
            return 'olo_proudfoot'
        else:
            return None
    else:
        return None


# MAIN CALLS
def countdown():
    click_center_of_screen()
    print('starting bot...')
    for i in range(3):
        print(f'{3 - i}...')
        time.sleep(1)


def make(total, batch_count, induction_delay):
    batches = math.floor(total / batch_count)
    leftover = total % batch_count

    # LOOP BATCHES
    for i in range(batches):
        click_make_all_button()

        # LOOP OVER BATCH
        for j in range(batch_count):
            time.sleep(induction_delay)
            print(f'Successfully completed "make" (Total: ~{j + 1}; Left: ~{batch_count - j - 1})')
        click_center_of_screen()
        click_center_of_screen()
        generate_random_delay(1150, 200)
        move_forward() if i % 2 == 0 else move_backward()
        click_repair_tab()
        click_repair_all_button()

    # LOOP OVER LEFTOVER
    for i in range(leftover):
        time.sleep(induction_delay)
        print(f'Successfully completed "make" (Total: ~{i + 1}; Left: ~{leftover - i - 1})')


def farm(total, batch_count, greenhouse_station='right'):
    leftover = total % batch_count
    batches = math.floor(total / batch_count)
    for i in range(batches):

        # SETUP CHARACTER CRAFTING TAB
        pydirectinput.press('t')
        click_farmer_tab()
        collapse_all_tiers()
        toggle_minas_ithil_tier()
        toggle_minas_ithil_vegetables()
        toggle_minas_ithil_field()

        # CRAFT BATCH
        for j in range(batch_count):
            click_make_button()
            generate_random_delay(3500)
            for k in range(random.randint(1, 2)):
                select_nearest_item()
                generate_random_delay(50, 90)
            # TODO: CONFIRM THE CORRECT SELECTION
            utilize_selection()
            generate_random_delay(8000 - constants.CONFIG['farming_tools_harvesting_deduction'])

            # Randomly open up inventory
            chance = random.randint(1, 25)
            print(f'Random chance to open up inventory: 1/25. We need 1; We got {chance}')
            if chance == 1:
                pydirectinput.press('i')
                generate_random_delay(1200, 800)
                pydirectinput.press('i')

        pydirectinput.press('t')

        # BEGIN TO TRY TO FIND A VENDOR NPC NEARBY
        selected_npc = None
        i = 0
        while selected_npc is None and i < 5:

            # SELECT AND IDENTIFY NPC
            select_next_npc()
            generate_random_delay()
            text = convert_to_text(screenshot_portraits()).strip().lower()
            print(f'Text located: {text}')
            selected_npc = identify_selected_npc(text)

            # IF SELECTED NPC IS ON OUR LIST OF KNOWN VENDORS
            if selected_npc in constants.KNOWN_VENDORS:
                print(f'Located NPC: {selected_npc}')
                break

            i += 1

        # THROW ERROR IF NPC CANNOT BE FOUND AFTER 5 ATTEMPTS
        if selected_npc is None:
            raise Exception("Cannot find NPC in the nearby area")

        # DELAY AFTER PARSING THROUGH NEARBY NPCS
        generate_random_delay()

        # REPAIR TOOLS
        travel_to_selected_vendor(selected_npc, greenhouse_station)
        click_repair_tab()
        click_repair_all_button()
        pydirectinput.press('esc')
        pydirectinput.press('esc')
        return_to_crafting_facility(greenhouse_station)

    for i in range(leftover):

        # CRAFT BATCH
        for j in range(batch_count):
            click_make_button()
            generate_random_delay(3500)
            for k in range(random.randint(1, 2)):
                select_nearest_item()
                generate_random_delay(50, 90)
            # TODO: CONFIRM THE CORRECT SELECTION
            utilize_selection()
            generate_random_delay(8000 - constants.CONFIG['farming_tools_harvesting_deduction'])

            # Randomly open up inventory
            chance = random.randint(1, 25)
            print(f'Random chance to open up inventory: 1/25. We need 1; We got {chance}')
            if chance == 1:
                pydirectinput.press('i')
                generate_random_delay(1200, 800)
                pydirectinput.press('i')


def cook(total, batch_count=200):
    pydirectinput.press('t')
    click_cook_tab()
    collapse_all_tiers()
    toggle_minas_ithil_tier()
    toggle_minas_ithil_ingredients()
    toggle_bunch_of_par_cooked_vegetables()
    generate_random_delay()

    make(total=total,
         batch_count=batch_count,
         induction_delay=constants.DELAYS['ingredient_cooking_induction']
         )


def process(total, batch_count=200):
    # SETUP CRAFTING PANEL
    pydirectinput.press('t')
    click_farmer_tab()
    collapse_all_tiers()
    toggle_minas_ithil_tier()
    toggle_minas_ithil_vegetables()
    toggle_vegetable_treble()

    make(total=total,
         batch_count=batch_count,
         induction_delay=constants.DELAYS['crop_processing_induction']
         )


countdown()
cook(180)
