import json
from shared import player
from entities import *
import random

def choose_door():
    print(f'\nChoose a door:\ndoor 1\ndoor 2\ndoor 3')
    while True:
        choice = input('Enter your choice [1], [2], [3] -> ')
        if choice in ['1', '2', '3']:
            make_room()
            return
        else:
            print('X: [1], [2], or [3]')


def trap():
    while True:
        damage = random.randint(0, player.strength)
        print(f"\nOh no, it's a trap!")
        if damage == 0:
            print('You manage to escape the trap without harm')
            break
        else:
            player.take_damage(damage)
            print(f'You took {damage} damage.')
            break


def item(): 
    with open('items.json', 'r') as f:
        data = json.load(f)
    random_item = random.choice(data)
    print("\nYou enter a treasure room...")
    print(f'Wow! You found a {random_item['name']} in a chest.')
    while True:
        question = input(f'Do you want to put {random_item['name']} in your inventory?\n-> ')
        if question.lower() in ['yes', 'y']:
            if len(player.inventory) == 2:
                print("Your inventory is full!")
                question_2 = input(f"Do you want to replace an item in your inventory?\n-> ")
                if question_2 == "yes" or question_2 == "y":
                    try:
                        choice = int(input(f"{player.inventory}\nWhich item do you want to replace? [1-5]\n-> "))
                        integer = choice - 1
                        if 0 <= integer < len(player.inventory):
                            item_replace = player.inventory[integer]
                            player.subtract_strength(item_replace)
                            player.inventory[integer] = random_item['name']
                            player.add_strength()
                            print(f"updated inventory: {player.inventory}")
                            break
                        else:
                            print('X: [1-5]')
                    except ValueError:
                        print('X: [1-5]')
                elif question_2 == ["no", "n"]:
                    print(f"You threw the {random_item} away.")
                    break
                else:
                    print("X: [yes] or [no]")
            else:
                player.inventory.append(random_item['name'])
                player.add_strength()
                break
        elif question.lower() in ['no', 'n']:
            print(f'You threw {random_item['name']} in the conveniently placed garbage bin!')
            break
        else:
            print('X: [yes] or [no] ')


def battle(player, enemy):
    print(f"\nYou entered a room with a {enemy.name} standing infront of you")
    while player.health > 0 and enemy.health > 0:
        choice = input(f'\nfight [1]\nflight [2]\n-> ')
        if choice in ['1', 'fight', 'attack', 'battle']:
            player.attack(enemy)
            if enemy.health <= 0:
                break
            enemy.attack(player)
        elif choice in ['2', 'flight', 'flee', 'run']:
            if random.randint(1, 10) < 5:
                print('Your pathetic booty scrambled your way to the next door, shame on you!')
                choose_door()
            else:
                print("\nYou weren't able to run away from the monster")
                enemy.attack(player)
        else:
            print('X: [1], or [2]')
    if player.health > 0:
        player.level += 1
        player.strength += 2
        print(f'\n{player.name} has bested the {enemy.name} in a fight to the death!\nYou leveled up! to level {player.level}, You gained two strength\n--------------------------------------\nYou now have {player.strength} strength!\nYour remaining health is {player.health}\n--------------------------------------')
    else:
        print(f'\n{player.name} has been defeated by the {enemy.name}')

def make_room():
    Goblin = Enemy('Goblin', 10, 10)
    Zombie = Enemy('Zombie', 20, 7)
    Giant_Spider = Enemy('Giant Spider', 40, 5)

    random_room =  random.choice(['1', '2', '3'])
    if random_room == '1':
        item()
    elif random_room == '2':
        trap()
    elif random_room == '3':
        random_enemy = random.choice(['Goblin', 'Zombie', 'Giant Spider'])
        if random_enemy == 'Goblin':
            battle(player, Goblin)
        elif random_enemy == 'Zombie':
            battle(player, Zombie)
        elif random_enemy == 'Giant Spider':
            battle(player, Giant_Spider)