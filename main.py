from doors import *
from shared import *

def main(): # Här körs all kod från de olika dokumenten, runnar från detta ställe.
    while True:
        if player.health <= 0: # Om man förlorar 
            print("This one wasn't tough enough, maybe the next one...")
            print(game_over)
            break
        if player.level == 10: # Kör "Boss Battle" om man kommer till lvl 10 
            boss_battle()
            break
        choice = input(f'\nProceed Forwards {RED}[1]{RESET} \nCheck Inventory {RED}[2]{RESET} \n-> ')
        if choice == '1':
            choose_door()
        elif choice == '2':
            player.show_stats()
        else:
            print(f'{YELLOW}X: [1] or [2]{RESET}')
main() 