import os
import time
import keyboard
from termcolor import colored
from .colorant import Colorant

TOGGLE_KEY = 'F1'
FOV = 100
CENTER_X, CENTER_Y = 2560 // 2, 1440 // 2

def cheating_main():
    os.system('title Colorant')
    colorant = Colorant(CENTER_X - FOV // 2, CENTER_Y - FOV // 2, FOV)
    print(colored('''
                        
        ██╗░░░██╗░█████╗░██╗░░░░░░█████╗░██████╗░░█████╗░███╗░░██╗████████╗
        ██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝
        ╚██╗░██╔╝███████║██║░░░░░██║░░██║██████╔╝███████║██╔██╗██║░░░██║░░░
        ░╚████╔╝░██╔══██║██║░░░░░██║░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░
        ░░╚██╔╝░░██║░░██║███████╗╚█████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░
        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░   
                                              Valorant AIMBOT - v1.0 - Develop by Ant team''', 'magenta'))
    print()
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()