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
        print(f'---------------------------------------\nName -> {self.name} \nHealth -> {self.health}\nStrength -> {self.strength}\nLevel -> {self.level}\nitems -> {self.inventory}\n---------------------------------------')
        while True:
            choice = input('\nDo you want to inspect an item in the inventory [1] or exit [2]?\n-> ')
            if choice == '1':
                try:
                    while True:
                        choice_2 = int(input(f"\nInventory -> {self.inventory}\nWhich item do you want to inspect [1-5]? [6] to exit\n-> "))
                        integer = choice_2 - 1
                        if choice_2 == 6:
                            break
                        elif 0 <= integer < len(self.inventory): #<----------------------------------------------
                            get_item = self.get_item_info(self.inventory[integer])
                            print(f"--------------------\n{get_item['description']}\nStrength: {get_item['strength']}\nHealing: {get_item['heal']}\n--------------------")
                            if get_item['type'] in ['Healing', 'SuperHealing']:
                                choice_3 = input(f"Remove this item [1]\nConsume it [2]\nGo back [3]\n->  ")
                                if choice_3 == '1':
                                    self.inventory.remove(get_item['name'])
                                elif choice_3 == '2':
                                    self.add_health()
                                    print(f'Your health is {self.health}')
                            else:
                                choice_3 = input("Do you want to remove this item from your inventory?\n-> ")
                                if choice_3.lower() in ['yes', 'y']:
                                    self.subtract_strength(get_item['name'])
                                    self.inventory.remove(get_item['name'])
                                elif choice_3.lower() in ['no', 'n']:
                                    break
                        else:
                            print("There is no item in that position [6] to exit\n-> ")
                except ValueError:
                    print("There is no item in that position [6] to exit\n-> ") 
            elif choice == '2':
                break
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
    
    def add_strength(self):
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] in ['Weapon', 'Potion']:
                self.strength += int(currentItem['strength'])
                break

    def add_health(self):
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] == 'SuperHealing':
                if self.health >= 100:
                    print("You have max health already.")
                    break
                else:
                    self.health = int(currentItem['heal'])
                    self.inventory.remove(item_name)
                    break
            elif currentItem['type'] == 'Healing':
                if self.health >= 91:
                    print("\nThis item wouldn't be beneficial to use now, use it later.")
                    break
                else:
                    self.health += int(currentItem['heal'])
                    self.inventory.remove(item_name)
                    break

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

    def attack(self, player):
        damage = random.randint(0, self.strength)
        if damage == 0:
            print("Yes! the foe missed their attack.")
        else:
            player.take_damage(damage)
            print(f'The {self.name} attacked {player.name} for {damage} health points')