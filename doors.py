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
            break
        else:
            print('X: (1), (2), or (3)')


def trap():
    while True:
        damage = random.randint(0, 1)
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
    print(f'Wow! You found a {random_item['name']} in the Treasure room.')
    while True:
        question = input(f'Do you want to put {random_item['name']} in your inventory? -> ')
        if question.lower() in ['yes', 'y']:
            player.inventory.append(random_item['name'])
            player.update_strength()
            player.update_health()
            break
        elif question.lower() in ['no', 'n']:
            print(f'You threw {random_item['name']} in the conveniently placed garbage bin!')
            break
        else:
            print('X: [yes] or [no] ')


def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        val = input(f'{player.name}, its time for flight or fight, so what shall it be?')
        if val in ['1', 'fight']:
            player.attack(enemy)
            if enemy.health <= 0:
                break
            enemy.attack(player)
        elif val in ['2', 'flight']:
            chance = player.health / enemy.health
            chance = max(0.0, min(chance, 1.0))
            if random.random() < chance:
                print('Your pathetic booty scrambled your way to the next door, shame on you!')
                choose_door() 
            else:
                enemy.attack(player)
                print('The monster did not let that attempt slide!')

        else:
            print('1 or 2, fight or flight lil bro, dont play with me boy.')



    if player.health > 0:
        print(f'{player.name} has bested the {enemy.name} in a fight to the death!')
        player.level += 1
        while True:
            choice = input(f'You leveled up! to level {player.level}, do you want strength [1] or health [2]?')
            if choice == '1':
                player.strength += 1
                print(f'You now have {player.strength} strength!')
                break
            elif choice == '2':
                player.health += 1
                print(f'You now have {player.health} health!')
                break
            else:
                print('X: [1] or [2]')


    else:
        print(f'{player.name} has been defeated by the {enemy.name}')

def make_room():
    Goblin = Enemy('Goblin', 1, 1)
    Zombie = Enemy('Zombie', 1, 1)
    Giant_Spider = Enemy('Giant Spider', 1, 1)
    random_room =  random.choice(['Monster', 'Treasure', 'Trap'])
    if random_room == 'Monster':
        random_enemy = random.choice(['Goblin', 'Zombie', 'Giant Spider'])
        if random_enemy == 'Goblin':
           battle(player, Goblin) 
        elif random_enemy == 'Zombie':
           battle(player, Zombie)
        elif random_enemy == 'Giant Spider':
            battle(player, Giant_Spider)
        # print("monster")
    elif random_room == 'Treasure':
        item()
    elif random_room == 'Trap':
        # print("trap")
        trap()