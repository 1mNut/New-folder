import random
import json
import simple_colors 

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
        print(f'\nName -> {self.name} \nHealth -> {self.health}\nStrength -> {self.strength}\nLevel -> {self.level}\nitems -> {self.inventory}')
        choice = input('\nDo you want to inspect an item in the inventory or open a door?\n[1], [2] -> ')
        if choice == '1':
            while True:
                try:
                    choice_2 = int(input("Which item do you want to inspect? press 6 to go back ->"))
                    integer = choice_2 - 1
                    if choice_2 == 6:
                        break
                    elif 0 <= integer < len(self.inventory):
                        get_item = self.get_item_info(self.inventory[integer])
                        print(f"{get_item['description']}\nStrength: {get_item['strength']}\nHealing: {get_item['heal']}")
                        choice_3 = input("Do you want to remove this item from your inventory?\n-> ")
                        if choice_3.lower() in ['yes', 'y']:
                            self.inventory.remove(get_item['name'])
                        elif choice_3.lower() in ['no', 'n']:
                            break
                    else:
                        print("There is no item in that position [6] to exit -> ")
                except ValueError:
                    print("There is no item in that position [6] to exit -> ")
                
            
        elif choice == '2':
            return
        else:
            print('X: [1], or [2]')
            

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Oh no, you missed your attack!")
        else:
            enemy.take_damage(damage)
            print(f'{self.name} attacked the enemy for {damage} health points!')
    
    def update_strength(self):
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] in ['Weapon', 'Potion']:
                self.strength += int(currentItem['strength'])
                break

    def update_health(self):
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] == 'SuperHealing':
                if self.health >= 100:
                    break
                else:
                    self.health = int(currentItem['heal'])
                    self.inventory.remove(item_name)
                    break
            elif currentItem['type'] == 'Healing':
                if self.health >= 100:
                    break
                else:
                    self.health += int(currentItem['heal'])
                    self.inventory.pop(item_name)
                    break

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, player):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Yes! the foe missed their attack.")
        else:
            player.take_damage(damage)
            print(f'The {self.name} attacked {player.name} for {damage} health points')