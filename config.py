import pyautogui


def rewrite_file(text_to_change, new_text):
    reader = open('constants.py', 'r')
    file = reader.read()
    if text_to_change in file:
        file = file.replace(text_to_change, new_text)
    else:
        print('Desired target text not found... Ending Process')
        return
    writer = open('constants.py', 'w')
    writer.write(file)
    writer.close()
    reader.close()


def config_screen_dimensions():
    dim = pyautogui.size()
    new_x = dim[0]
    new_y = dim[1]

    # CYCLE THROUGH EACH KNOWN DIMENSIONS AND REFACTOR.
    # TODO: TURN INTO ARRAY
    rewrite_file('SCREEN_DIMENSIONS = (1152, 864)', f'SCREEN_DIMENSIONS = ({new_x}, {new_y})')
    rewrite_file('SCREEN_DIMENSIONS = (1920, 1080)', f'SCREEN_DIMENSIONS = ({new_x}, {new_y})')


def config():
    config_screen_dimensions()


config()