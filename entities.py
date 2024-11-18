import random

class Player:
    def __init__(self, name, health, strength, level, inventory=[]):
        self.name = name
        self.Health = health
        self.Strength = strength
        self.Level = level
        self.inventory = inventory
        
    def show_stats(self):
        print(f"\nName -> {self.name}\nHealth -> {self.Health}\nStrength -> {self.Strength}\nLevel -> {self.Level}\nitems -> {self.inventory}")

    def take_damage(self, damage):
        self.Health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.Strength)
        enemy.take_damage(damage)
        print(f"{self.name} attacked the enemy for {damage} health points!")

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.Health = health
        self.Strength = strength

    def take_damage(self, damage):
        self.Health -= damage

    def attack(self, player):
        damage = random.randint(1, self.Strength)
        player.take_damage(damage)
        print(f"The {self.name} attacked {player.name} for {damage} health points")