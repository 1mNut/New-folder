import random 
from player import Player

name = input("Välj karaktärens namn -> ")
player = Player(name, 1, 1, 1)

def choose_door():
    print("Choose a door:")
    print("1. Door 1")
    print("2. Door 2")
    print("3. Door 3")
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

while True:
    Val = input("Dörr (1) eller inventory (2)")
    if Val == "1":
        choose_door()
        break
    elif Val == "2":
        player.show_stats()
        break
    else:
        print("invalid choice, choose: 1 or 2")