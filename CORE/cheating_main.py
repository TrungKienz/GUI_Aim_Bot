import os
import time
import keyboard
from termcolor import colored
from .colorant import Colorant

TOGGLE_KEY = 'F1'
FOV = 100
CENTER_X, CENTER_Y = 1920 // 2, 1080 // 2
MOUSE_SENSITIVITY = 0.2

def cheating_main(toggle_key=TOGGLE_KEY, fov=FOV, center_x=CENTER_X, center_y=CENTER_Y, mouse_sensitivity=MOUSE_SENSITIVITY, border_color='purple', hold_key=0x06):
    os.system('title Valorant ANT BOT')
    colorant = Colorant(center_x - FOV // 2, center_y - fov // 2, fov, mouse_sensitivity, border_color, hold_key)
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(toggle_key):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()