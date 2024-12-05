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

class Player:#skapar klassen player. klasser buntar ihop data och funktioner
    def __init__(self, name, health, strength, level, inventory=[]):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.inventory = inventory

    def get_item_info(self, item_name):#skapar en funktion.
        database = "items.json"#gör så att items.json är samma som variabeln database.
        data = json.loads(open(database).read())#öppnar filen med sökvägen database sedan så läser den hela öppnade filen som en sträng. den sedan knverterar .json filen som till ett python objekt python objectet som skapas tilldelas variabeln data.
        for item in data:#om varje item i data har tilldelats variabeln item_name
            if item['name'] == item_name:
                return item#skickar tillbaka värdet från var funktionen anropades.
        
    def show_stats(self):#skapar en funktion
        print(f'---------------------------------------\n{CYAN}Name{RESET} -> {CYAN}{self.name}{RESET} \n{GREEN}Health{RESET} -> {GREEN}{self.health}{RESET}\n{RED}Strength{RESET} -> {RED}{self.strength}{RESET}\n{BLUE}Level{RESET} -> {BLUE}{self.level}{RESET}\n{YELLOW}items{RESET} -> {YELLOW}{self.inventory}{RESET}\n---------------------------------------')#printar ut spelarens olika egenskaper, vilken level dem har etc med deras respektive färger.
        while True:#skapar en while loop.
            choice = input(f'\nDo you want to inspect an item in the inventory {RED}[1]{RESET} or exit {RED}[2]{RESET}?\n-> ')#skapar en input där man får svara 1 eller 2.
            if choice == '1':
                try:
                    while True:#skapar en while loop.
                        choice_2 = int(input(f"\nInventory -> {self.inventory}\nWhich item do you want to inspect {RED}[1-5]{RESET}? {GREEN}[6]{RESET} to exit\n-> "))#frågar vilket föremål man vill granska 1-5 eller utträde från menyn
                        integer = choice_2 - 1 #ger choice_2 - 1 variabeln integer
                        if choice_2 == 6:#om choice_2 = 6 så avslutas loopen
                            break
                        elif 0 <= integer < len(self.inventory):#om den inte är lika med 6 tar man föremålets beskrivning från items.json från en av de 5 
                            get_item = self.get_item_info(self.inventory[integer])
                            print(f"--------------------\n{get_item['description']}\n{RED}Strength:{RESET} {get_item['strength']}\n{GREEN}Healing:{RESET} {get_item['heal']}\n--------------------")
                            if get_item['type'] in ['Healing', 'SuperHealing']:#om ens föremål är typen healing ellersuperhealing då man granskar det så kan man slänga det använde den och på så vis försvinner den och man kan också utträda från menyn
                                choice_3 = input(f"Remove this item {RED}[1]{RESET}\nConsume it {RED}[2]{RESET}\nGo back {RED}[3]{RESET}\n->  ")#ger variabeln choice_3 till inputen
                                if choice_3 == '1': #om man svarar 1 så förvinner föremålet.
                                    self.inventory.remove(get_item['name'])
                                elif choice_3 == '2':#om svaret är 2 så får man så mycket hälsa som föremålet ger.
                                    self.add_health(get_item['name']) #<_------------------------------------------------------------------------
                                    print(f'Your health is now {GREEN}{self.health}{RESET}')
                            else:#om föremålet inte är av typen healing eller superhealing
                                choice_3 = input("Do you want to remove this item from your inventory?\n-> ")#frågar om man vill ta bort föremålet från sit inventaruim
                                if choice_3.lower() in ['yes', 'y']:#om svaret är y eller yes så tas föremålet bort och ens attribut styrka uppdateras
                                    self.subtract_strength(get_item['name'])
                                    self.inventory.remove(get_item['name'])
                                elif choice_3.lower() in ['no', 'n']:#om man svarar no eller n så avslutas funktionen
                                    break
                                else:#om man skriver någon man inte får så skrivs detta ut
                                    print(f"{YELLOW}X: [yes] or [no]{RESET}")
                        else:#om man anger ett nummer som inte har ett föremål på sin plats så skirver den ut understående.
                            print(f"{YELLOW}There is no item in that position{RESET}")
                except ValueError:#om det inte går att utföra while loopen oåvan så skrivs detta ut.
                    print(f"{YELLOW}There is no item in that position{RESET}")
            elif choice == '2':#om man skriver 2 så avslutas loopen
                break
            else:#om man skriver fel inte 1 eller 2 så skrivs detta ut
                print(f'{YELLOW}X: [1], or [2]{RESET}')
            

    def take_damage(self, damage):#skapar funktion.
        self.health -= damage#funktionen tar bort damage(nummeret) från health(nummeret)
        if self.health < 0:
            self.health = 0

    def attack(self, enemy):#skapaer funktion 
        damage = random.randint(0, self.strength)#skada är mellan 0 och heltalet self.strength
        if damage == 0:
            print("Oh no, you missed your attack!")
        else:
            enemy.take_damage(damage)
            print(f'{CYAN}{self.name}{RESET} attacked the enemy for {RED}{damage}{RESET} health points!\n The monster has {GREEN}{enemy.health}{RESET} hp remaining.')
    
    def add_strength(self):#skapar funktion
        for item_name in self.inventory:
            currentItem = self.get_item_info(item_name)#ger variabel
            if currentItem['type'] in ['Weapon', 'Potion']:#om föremålet är av typen weapon så uppdateras  spelarens styrka
                self.strength += int(currentItem['strength'])
                break

    def add_health(self, item_name):#skapar funktion
        if item_name in self.inventory:
            currentItem = self.get_item_info(item_name)
            if currentItem['type'] == 'SuperHealing':#om föremålet är typen superhealing så blir ens hälsa 100 och sedan så tars föremålet bort
                if self.health >= 100:#om man har 100 hälsa eller mer så kommer man inte helas uch så får man utsriften under
                    print("You have max health already.")
                else:
                    self.health = int(currentItem['heal'])
                    self.inventory.remove(item_name)
            elif currentItem['type'] == 'Healing':#om föremålet är typen healing så får man 10 hälsa om man har mer än 91 hälsa så kommer den inte användas
                if self.health >= 91:
                    print("\nThis item wouldn't be beneficial to use now, use it later.")
                else:
                    self.health += int(currentItem['heal'])
                    self.inventory.remove(item_name)

    def subtract_strength(self, item_name):#skapar funktion
        currentItem = self.get_item_info(item_name)#ger variabeln currentitem till self.get_item_info(item_name)
        if currentItem['type'] in ['Weapon', 'Potion']:#om föremålet är av typen weapon eller potion så
            self.strength -= int(currentItem['strength'])#föremålets styrka tas bort från spelarens egna styrka (nummer-nummer)

class Enemy:#skapar klassen enemy
    def __init__(self, name, health, strength):#skapar funktion
        self.name = name#ger 3 olika variabler det vill säga self.name, selfhealth coh self.strength
        self.health = health
        self.strength = strength

    def take_damage(self, damage):#take_damage är nummeret self.health-damage om self.health är mindre änn 0 så återställs det till 0
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, player):#skapar funktion
        damage = random.randint(0, self.strength)#skada är en slumpmässigt heltal mellan 0 och spelarens styrka
        if damage == 0:#om skadan är 0 så printas detta understående
            print("Yes! the foe missed their attack.")
        else:#om skadan inte är 0 så tar spelaren skada och det skrivs ut att den gör det.
            player.take_damage(damage)
            print(f'The {YELLOW}{self.name}{RESET} attacked {CYAN}{player.name}{RESET} for {RED}{damage}{RESET} health points\n You now have {GREEN}{player.health}{RESET} hp remaining.')