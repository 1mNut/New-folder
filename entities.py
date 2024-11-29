import random
import json
import simple_colors 

class Player:
    def __init__(self, name, health, strength, level, inventory=[None] * 5):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.inventory = inventory
        
    def show_stats(self):
        print('\nName -> {self.name} \nHealth -> {self.health}\nStrength -> {self.strength}\nLevel -> {self.level}\nitems -> {self.inventory}')
        choice = input('Do you want to inspect an item in the inventory?')
        if choice == ['yes', 'y']:
            choice_2 = input("which item do you want to inspect?")
            integer = choice_2 - 1
            if self.inventory == #<------------------------------------------------------------------------------

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Oh no, you missed your attack!")
        else:
            enemy.take_damage(damage)
            print(f'{self.name} attacked the enemy for {damage} health points!')

    def get_item_info(self, item_name):
        database = "items.json"
        data = json.loads(open(database).read())
        for item in data:
            if item['name'] == item_name:
                return item
    
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