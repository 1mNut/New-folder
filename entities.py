import random

class Player:
    def __init__(self, name, health, strength, level, inventory=[]):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.inventory = inventory
        
    def show_stats(self):
        print(f'\nName -> {self.name}\nHealth -> {self.health}\nStrength -> {self.strength}\nLevel -> {self.level}\nitems -> {self.inventory}')

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        enemy.take_damage(damage)
        print(f'{self.name} attacked the enemy for {damage} health points!')
    
    def update_strength(self):
        for item in self.inventory:
            if item == 'Firewood':
                self.strength += 100
            elif item == 'Stonesword':
                self.strength += 100
            elif item == 'BananaRang':
                self.strength += 100
            elif item == 'Farmors Dunderhonung':
                self.strength += 100

    def update_health(self):
        for item in self.inventory:
            if item == 'ChugJug':
                self.health = 100

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, player):
        damage = random.randint(1, self.strength)
        player.take_damage(damage)
        print(f'The {self.name} attacked {player.name} for {damage} health points')