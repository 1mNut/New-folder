from doors import *
from shared import player


def main():
    while True:
        if player.health <= 0:
            print('You lost :(')
            break
        elif player.level == 10:
            print('You advanced all the way to level 10! You have beaten the dungeon!')
            break
        choice = input('\nProceed Forwards (1) \nCheck Inventory (2) \n-> ')
        if choice == '1':
            choose_door()
        elif choice == '2':
            player.show_stats()
        else:
            print('X: (1) or (2)')
main() 