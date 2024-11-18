from doors import *
from shared import *

def main():
    while True:
        Val = input("\nProceed Forwards (1) \nCheck Inventory (2) \n-> ")
        if player.Health <= 0:
            print("You lost :(")
            break
        elif Val == "1":
            choose_door()
        elif Val == "2":
            player.show_stats()
        else:
            print("X: (1) or (2)")

if __name__ == "__main__":
    main()