import random
import json

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"


class Player:
    def __init__(self, name, health, strength, level, inventory=[]):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.inventory = inventory

    def get_item_info(self, item_name):
        database = "items.json"
        data = json.loads(open(database).read())
        for item in data:
            if item['name'] == item_name:
                return item
        
    def show_stats(self):
        print(f'---------------------------------------\nName -> {CYAN}{self.name}{RESET} \n{GREEN}Health{RESET} -> {GREEN}{self.health}{RESET}\n{RED}Strength{RESET} -> {RED}{self.strength}{RESET}\n{BLUE}Level{RESET} -> {BLUE}{self.level}{RESET}\nitems -> {self.inventory}\n---------------------------------------')
        while True:
            choice = input(f'\nDo you want to inspect an item in the inventory {RED}[1]{RESET} or exit {RED}[2]{RESET}?\n-> ')
            if choice == '1':
                try:
                    while True:
                        choice_2 = int(input(f"\nInventory -> {self.inventory}\nWhich item do you want to inspect {RED}[1-5]{RESET}? {GREEN}[6]{RESET} to exit\n-> "))
                        integer = choice_2 - 1
                        if choice_2 == 6:
                            break
                        elif 0 <= integer < len(self.inventory):
                            get_item = self.get_item_info(self.inventory[integer])
                            print(f"--------------------\n{get_item['description']}\n{RED}Strength:{RESET} {get_item['strength']}\n{GREEN}Healing:{RESET} {get_item['heal']}\n--------------------")
                            if get_item['type'] in ['Healing', 'SuperHealing']:
                                choice_3 = input(f"Remove this item {RED}[1]{RESET}\nConsume it {RED}[2]{RESET}\nGo back {RED}[3]{RESET}\n->  ")
                                if choice_3 == '1':
                                    self.inventory.remove(get_item['name'])
                                elif choice_3 == '2':
                                    self.add_health(get_item['name']) #<_------------------------------------------------------------------------
                                    print(f'Your health is {GREEN}{self.health}{RESET}')
                            else:
                                choice_3 = input("Do you want to remove this item from your inventory?\n-> ")
                                if choice_3.lower() in ['yes', 'y']:
                                    self.subtract_strength(get_item['name'])
                                    self.inventory.remove(get_item['name'])
                                elif choice_3.lower() in ['no', 'n']:
                                    break
                                else:
                                    print(f"{YELLOW}X: [yes] or [no]{RESET}")
                        else:
                            print(f"{YELLOW}There is no item in that position{RESET}")
                except ValueError:
                    print(f"{YELLOW}There is no item in that position{RESET}")
            elif choice == '2':
                break
            else:
                print(f'{YELLOW}X: [1], or [2]{RESET}')
            

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, enemy):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Oh no, you missed your attack!")
        else:
            enemy.take_damage(damage)
            print(f'{CYAN}{self.name}{RESET} attacked the enemy for {RED}{damage}{RESET} health points!\n The monster has {GREEN}{enemy.health}{RESET} hp remaining.')
    
    def add_strength(self):
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] in ['Weapon', 'Potion']:
                self.strength += int(currentItem['strength'])
                break

    def add_health(self, item_name):
        if item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] == 'SuperHealing':
                if self.health >= 100:
                    print("You have max health already.")
                else:
                    self.health = int(currentItem['heal'])
                    self.inventory.remove(item_name)
            elif currentItem['type'] == 'Healing':
                if self.health >= 91:
                    print("\nThis item wouldn't be beneficial to use now, use it later.")
                else:
                    self.health += int(currentItem['heal'])
                    self.inventory.remove(item_name)

    def subtract_strength(self, item_name):
        currentItem = self.get_item_info(item_name)
        if currentItem['type'] in ['Weapon', 'Potion']:
            self.strength -= int(currentItem['strength'])

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, player):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Yes! the foe missed their attack.")
        else:
            player.take_damage(damage)
            print(f'The {YELLOW}{self.name}{RESET} attacked {CYAN}{player.name}{RESET} for {RED}{damage}{RESET} health points\n You now have {GREEN}{player.health}{RESET} hp remaining.')