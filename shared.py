from entities import *

print("Welcome to the dungeon!")
name = input("Enter your players name -> ")
enemy_name = random.choice(["Goblin", "Zombie", "Giant Spider"])
if enemy_name == "Goblin":
    health = 130
    strength = 16
elif enemy_name == "Zombie":
    health = 150
    strength = 15
elif enemy_name == "Giant Spider":
    health = 100
    strength = 20
player = Player(name, 200, 20, 1)
enemy = Enemy(enemy_name, health, strength)