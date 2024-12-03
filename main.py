from doors import *
from shared import player

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def main():
    while True:
        if player.health <= 0:
            print("This one wasn't tough enough, maybe the next one...")
            break
        elif player.level == 10:
            print(f'You advanced all the way to level {BLUE}10{RESET}! You have beaten the dungeon!')
            break
        choice = input(f'\nProceed Forwards {RED}[1]{RESET} \nCheck Inventory {RED}[2]{RESET} \n-> ')
        if choice == '1':
            choose_door()
        elif choice == '2':
            player.show_stats()
        else:
            print('X: (1) or (2)')
main() 