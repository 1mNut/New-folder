#Installerar simple_Colors! -----------------------------
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import simple_colors
except ImportError:
    print("simple_colors inte installerat. Installerar nu...")
    install_package("simple_colors")

#--------------------------------------------------------

import simple_colors 
from doors import *
from shared import player


def main():
    while True:
        if player.health <= 0:
            print(simple_colors.red('You lost :(',["bold", "underline"]))
            break
        elif player.level == 10:
            print(simple_colors.yellow('You advanced all the way to level 10! You have beaten the dungeon!'))
            break
        choice = input('\nProceed Forwards (1) \nCheck Inventory (2) \n-> ')
        if choice == '1':
            choose_door()
        elif choice == '2':
            player.show_stats()
        else:
            print('X: (1) or (2)')
main() 