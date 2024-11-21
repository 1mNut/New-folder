import json
from shared import player
from shared import enemy
from entities import *


def choose_door():
    print("\nChoose a door:\nDoor 1\nDoor 2\nDoor 3")
    while True:
        choice = input("Enter your choice (1), (2), or (3): ")
        if choice in ['1', '2', '3']:
            make_room()
            break
        else:
            print("X: (1), (2), or (3)")
    

def trap():
    while True:
        damage = random.randint(0, 3)
        print("\nOh no, it's a trap!")
        if damage == 0:
            print("You manage to escape the trap without harm")
            break
        else:
            player.take_damage(damage)
            print(f"You took {damage} damage.")
            break


def item():
    with open('items.json', 'r') as f:
        data = json.load(f)
    random_item = random.choice(data)
    print(f"Wow! You found a {random_item["name"]} in the Treasure room.")
    while True:
        question = input(f"Do you want to put {random_item["name"]} in your inventory?")
        if question.lower() == 'yes':
            player.inventory.append(random_item["name"])
            break
        elif question.lower() == 'no':
            print(f"You threw {random_item["name"]} in the conveniently placed garbage can!")
            break
        else:
            print("Type 'yes' or 'no'")

def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)

    if player.health > 0:
        print(f"{player.name} has bested the {enemy.name} in a fight to the death!")
    else:
        print(f"{player.name} has been defeated by the {enemy.name}")

def make_room():
    random_room =  random.choice(["Monster", "Treasure", "Trap"])
    if random_room == "Monster":
        battle(player, enemy)
    elif random_room == "Treasure":
        item()
    elif random_room == "Trap":
        trap()