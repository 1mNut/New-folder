import json
from shared import *
from entities import *
import random

def choose_door():#skapar en funktion som heter choose_door
    print(f'\nChoose a door:\ndoor 1\ndoor 2\ndoor 3')#skriver ut, dina dörralternativ
    while True:#skapar en while loop
        choice = input(f'{RED}[1]{RESET}, {RED}[2]{RESET}, {RED}[3]{RESET} -> \n')#gör input så att koden reagerar på vad man svarar
        if choice in ['1', '2', '3']:#om du skriver 1, 2 eller 3 så aktiverar du funktionen makeroom
            make_room()
            return
        else:#om du skrev något som inte var 1, 2 eller 3 så kommer det understående skrivas ut.
            print(f'{YELLOW}X: [1], [2], or [3]{RESET}')


def trap():#skapar en funktion som heter trap
    while True:#skapar en while loop så länge det understående är sant.
        damage = random.randint(0, player.strength + 1)#skada som räknas ut utifrån en slump mellan 0 och spelarens styrka, gör så att om man har väldigt mycket kan det göra ont i fällor
        print(f"\nYou entered the room...\nOh no, it's a trap!")
        if damage == 0:#om skadan är lika med 0 skriv ut det understående och sedan avsluta loopen
            print('You manage to escape the trap without harm \n')
            break
        else:#om skadan inte är 0 så tar spelaren skada och sedan skriver den ut hur mycket skada och sedan avslutas loopen
            player.take_damage(damage)
            print(f'You took {RED}{damage}{RESET} damage. \n')
            break


def item(): 
    with open('items.json', 'r') as f:#hänvisar koden til items.json och hämtar en av deverse föremål som finns i listan.
        data = json.load(f)
    random_item = random.choice(data)
    print("\nYou enter a treasure room...")
    print(f'Wow! You found a {MAGENTA}{random_item['name']}{RESET} in a chest.')#skriver ut att man hittade ett föremål
    while True:#skapar en while loop så länge förutsättningarna är sanna.
        question = input(f'Do you want to put {MAGENTA}{random_item['name']}{RESET} in your inventory?\n-> ')#frågar om du vill lägga föremålet i dit inventarium
        if question.lower() in ['yes', 'y']:#om svaret på input är y eller yes
            if len(player.inventory) == 5:#om man har 5 föremål i inventarium så är det fullt, då skriver den att den är full.
                print("You can only manage to hold 5 items in your inventory.")
                question_2 = input(f"Do you want to replace an item in your inventory?\n-> ")#frågar om man vill byta ut ett föremål.
                if question_2 == "yes" or question_2 == "y":#om svaret är ja så gör den följande:
                    try: # Testar om den kan köra det som finns under
                        choice = int(input(f"\n{YELLOW}Inventory{RESET} -> {BLACK}{player.inventory}{RESET}\nWhich item do you want to replace? [1-5]\n-> "))
                        integer = choice - 1
                        if 0 <= integer < len(player.inventory):#om man har fler änn 0 föremål i spelarens inventarium så byter man ut ett föremål.
                            item_replace = player.inventory[integer]
                            player.subtract_strength(item_replace)
                            player.inventory[integer] = random_item['name']
                            player.add_strength()
                            print(f"updated inventory: {player.inventory} \n")
                            break
                        else:
                            print(f'{YELLOW}X: [1-5]{RESET}')#om man har skrivet något som inte är ett nummer mellan 1-5 så skrivs detta it
                    except ValueError: # Om spelaren har givit en input som inte funkar med "Try" funktionen
                        print(f'{YELLOW}X: [1-5]{RESET}')
                elif question_2 == ["no", "n"]:#om svaret är nej så skrivs detta underliggand ut sedan så avslutas loopen
                    print(f"You threw the {MAGENTA}{random_item}{RESET} away. \n")
                    break
                else:#om man inte svarar ja eller nej så skrivs underliggand ut.
                    print(f"{YELLOW}X: [yes] or [no]{RESET}")
            else:
                player.inventory.append(random_item['name'])
                player.add_strength()
                break
        elif question.lower() in ['no', 'n']:#om svaret är nej så lägger man inte till föremålet och sedan så avslutar loopen   
            print(f'You threw {MAGENTA}{random_item['name']}{RESET} in the conveniently placed garbage bin! \n')
            break
        else:
            print(f'{YELLOW}X: [yes] or [no]{RESET}')#om svaret är inte ja eller nej så skrivs detta ut


def battle(player, enemy):#skapar en funktion
    print(f"\nYou entered a room with a {YELLOW}{enemy.name}{RESET} standing infront of you \n------------------------------")#skriver ut vilket monster du träffar.
    while player.health > 0 and enemy.health > 0:#loopen fortsätter så länge spelaren eller monster har hälsa
        choice = input(f'\n{RED}fight [1]{RESET}\n{BLUE}flight [2]{RESET}\n-> ')#man får antingen fly eller slåss, vi får välja
        if choice in ['1', 'fight', 'attack', 'battle']:#om man väljer att slåss så skadas monsteret och spelaren skadas, och så långe man monsteret eller spelaren får 0 hälsa så kommer loopen att börja om.
            player.attack(enemy)
            if enemy.health <= 0:
                break
            enemy.attack(player)
        elif choice in ['2', 'flight', 'flee', 'run']:#om man väljer att fly så har men en chans att man lyckas fly
            if random.randint(1, 10) < 5:
                print('Your pathetic booty scrambled your way to the next door, shame on you! \n')
                choose_door()#aktiverar funktionen choose_door om man lyckas fly
            else:
                print("\nYou weren't able to run away from the monster")
                enemy.attack(player)
        else:#om man skrev fel så får man detta felmedelande utskrivet
            print(f'{YELLOW}X: [1], or [2]{RESET}')
    if player.health > 0:#om spelarens hälsa är mer änn 0 och monsterets hälsa är mindre änn 0 så vinner man och levlar up vilket ger 2 styrka
        player.level += 1
        player.strength += 2
        print(f'\n{CYAN}{player.name}{RESET} has bested the {YELLOW}{enemy.name}{RESET} in a fight to the death!\nYou leveled up! to level {BLUE}{player.level}{RESET}, You gained {RED}2{RESET} strength\n--------------------------------------\nYou now have {RED}{player.strength}{RESET} strength!\nYour remaining health is {GREEN}{player.health}{RESET}\n-------------------------------------- \n')
    else:#om spelarens hälsa är 0 så förlorar man
        print(f'\n{CYAN}{player.name}{RESET} has been defeated by the {YELLOW}{enemy.name}{RESET}')

def make_room():#skapar en funktion som genererar de olika rummen(1,2 eller 3)
    Goblin = Enemy('Goblin', 10, 10)#den första numret är hälsa och det andra är styrka
    Zombie = Enemy('Zombie', 20, 7)
    Giant_Spider = Enemy('Giant Spider', 40, 5)

    random_room =  random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])#skapaer slumpmässigt ett av tre rum, skattrum,ett fällrum och ett monsterrum.
    if random_room in ['1', '2', '3']: #olika chanser för olika typer av rum
        item()
    elif random_room in ['4', '5']:
        trap()
    elif random_room in ['6', '7', '8', '9']:
        random_enemy = random.choice(['Goblin', 'Zombie', 'Giant Spider'])#om rummet är ett monsterrum så är monsteret antingen en rumpnisse, zombie eller stor spindel.
        if random_enemy == 'Goblin':
            battle(player, Goblin)
        elif random_enemy == 'Zombie':
            battle(player, Zombie)
        elif random_enemy == 'Giant Spider':
            battle(player, Giant_Spider)


def boss_battle(): 
    game_over = f"""{RED}
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝{RESET}"""
    game_win = f"""{BLUE}

██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ███████╗ █████╗ ████████╗    ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝    ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██████╔╝█████╗  ███████║   ██║       ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██╗██╔══╝  ██╔══██║   ██║       ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝███████╗██║  ██║   ██║       ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝{RESET}"""
   
    boss = Enemy('Unknown Creature', 75, 15)
    print(f"You advanced all the way up to level {BLUE}10{RESET}!\nWait... an {RED}Unknown Creature{RESET} appeared,\nIt seems much stronger than the monsters you have met so far! \n--------------------------------------")
    #------------------------------------------------------------------------------#
# Under detta är funktionen för den enskilda "Boss Battle" är inte samma funktion som vanlig battle 
    while player.health > 0 and boss.health > 0:
        choice = input(f'\n{RED}Attack [1]{RESET}\n{BLUE}Flee [2]{RESET}\n-> ')
        if choice in ['1', 'fight', 'attack', 'battle']:
            player.attack(boss)
            if boss.health <= 0:
                break
            boss.attack(player)
        elif choice in ['2', 'flight', 'flee']:
            print(f'The foul creature would not let you leave the room, there is no other option than to {RED}fight{RESET}')
        else:
            print(f'{YELLOW}X: [1], You cant run from this final battle...{RESET}')
    if player.health > 0:
        print(f"\n{RED}The warped creature scrambles away deep into the dungeons darkness... You won?{RESET}\nbut how do you get out...")
        print(game_win)
        return
    else:
        print(f'\nThe {CYAN}warped creature{RESET} swallowed you whole! {RED}Too bad...{RESET}')
        print(game_over)
        return
        