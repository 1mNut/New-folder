import random

class Player:
    def __init__(self, name, health, strength, level, inventory=[]):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.inventory = inventory
        
    def show_stats(self):
        print(f"\nName -> {self.name}\nHealth -> {self.health}\nStrength -> {self.strength}\nLevel -> {self.level}\nitems -> {self.inventory}")

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        enemy.take_damage(damage)
        print(f"{self.name} attacked the enemy for {damage} health points!")
    
    def update_strength(self):
        self.strength = 0
        for item in self.inventory:
            if item["type"] == "Weapon" or item["type"] == "Potion" and item["strength"] is not None:
                self.strength += item["strength"]

    def healed(self):
        self.health = 0
        for item in self.inventory:
            if item["type"] == "Healing" and item["heal"] is not None:
                self.health += item["heal"]
    # def level_up(self)
        

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
        print(f"The {self.name} attacked {player.name} for {damage} health points")