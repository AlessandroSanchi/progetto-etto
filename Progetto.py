import random
import time
import art
from termcolor import colored

Art= art.text2art("Welcome to untitled farming game") 
Art_c = (colored(Art,"magenta"))    
print(Art_c)


# Variables                                                                                                                                                                                                                                                                                                                       E
armor_equipped = ""
Money = 15000000
Coins = 10000000
bonus_multiplier = 1
godpass = False
X2Price = 150
swordequipped = ""
coinswordremaining = 1
excalibur = 1
legendaryS = 1
goldS = 1
GoldC = 1
CaveTicket = False
JungleTicket = False
DesertTicket = False
VoidTicket = False
player_hp = 100
player_damage = 20000000000000000
condizione = True

new_swords = {
    "Wooden Sword": {"price": 15000, "stock": coinswordremaining, "damage": 75},
    "Legendary Sword": {"price": 100000, "stock": legendaryS, "damage": 350},
    "Excalibur": {"price": 500000, "stock": excalibur, "damage": 1000}
}

power_ups = {
    "Gold Chain": {"price": 500000, "stock": GoldC, "multiplier": 5},
    "Golden Statue": {"price": 10000000, "stock": goldS, "activate_godpass": True}
}

armor = {
    "Leather Armor": {"price": 20000, "stock": 1, "hp": 2000},
    "Iron Armor": {"price": 100000, "stock": 1, "hp": 5000},
    "Dragon Scale Armor": {"price": 500000, "stock": 1, "hp": 15000}
}







# Farming items
forest_items = {
    "Rock": 1,
    "Gem": 5,
    "Silver coins": 6,
    "Gold coins": 8,
    "Pearl": 10,
    "Diamond": 20,
    "Ancient relic": 50
}

cave_items = {
    "Crystal": 7,
    "Glowing mushroom": 3,
    "Artifact": 15,
    "Rare mineral": 30,
    "Fossil": 50
}

Jungle_items = {
    "Rare Orchid": 5,
    "Dragon Fruit": 9,
    "Jaguar Leaf": 12,
    "Elephant Ivory": 15,
    "Ara Plumage": 23,
    "Ancient Tribal Mask": 35,
    "Jungle Emerald": 50
}

Desert_Items = {
    "Cactus Flower": 8,
    "Sandstone Carving": 14,
    "Mirage Crystal": 19,
    "Scarab Beetle": 24,
    "Sunset Agate": 38,
    "Nomad Turban": 57,
    "Sands of Time": 83
}

Void_items = {
    "Cosmic Dust": 75,
    "Nebula Shard": 90,
    "Black Hole Orb": 110,
    "Celestial Echo": 125,
    "Galactic Nova": 135,
    "Astral Beacon": 150,
    "Stellar Mirage": 300
}

# Dev boost
if godpass:
    bonus_multiplier = bonus_multiplier * 15394

cooldowntime = 1.5

# Worlds
cave_unlocked = False
jungle_unlocked = False
Desert_unlocked = False
Void_unlocked = False
pass_remaining = 10
coinswordremaining = 1
power_up_remaining = 1



def format_price(price)->int:
    price_c = (colored(price,"yellow"))
    if price >= 1_000_000:
        return f"${price/1_000_000:.1f}M"
    elif price >= 1_000:
        return f"${price/1_000:.1f}K"
    else:
        return f"${price}"



def inputpage():
    print(colored("-1 Farm","green"))
    print(colored("-2 Shop","cyan"))
    print(colored("-3 Fight","light_blue"))
    print(colored("-4 Quit","light_magenta"))
    money_c = (colored(Money,"light_yellow"))
    Coins_c = (colored(Coins,"yellow"))
    print(f"Money: ${money_c}")
    print(f"Coins: £{Coins_c}")


def initiate_battle(enemy_name, enemy_hp,armor_equipped,player_damage):
    global Coins, player_hp  
    enemy_list = {
        "Goblin": {"min_damage": 5, "max_damage": 16},
        "Bat": {"min_damage": 150, "max_damage": 250},
        "Snake": {"min_damage": 200, "max_damage": 350},
        "Scorpion": {"min_damage": 250, "max_damage": 450},
        "Void Beast": {"min_damage": 300, "max_damage": 600},
        "Romagna": {"min_damage": 15, "max_damage": 25},
        "Golem": {"min_damage": 200, "max_damage": 350},
        "Tiger": {"min_damage": 200, "max_damage": 400},
        "Mummy": {"min_damage": 400, "max_damage": 600},
        "Shadow Entity": {"min_damage": 450, "max_damage": 900}
    }

    if armor_equipped == "Leather Armor":
        player_hp = armor["Leather Armor"]["hp"]
    elif armor_equipped == "Iron Armor":
        player_hp = armor["Iron Armor"]["hp"]
    elif armor_equipped == "Dragon Scale Armor":
        player_hp = armor["Dragon Scale Armor"]["hp"]

    else:
        player_hp = 100

    enemy_damage = 10  
    print(f"You've encountered a {enemy_name} with {enemy_hp} HP!")
    time.sleep(1)

    while player_hp > 0 and enemy_hp > 0:
        # Attack
        enemy_hp -= player_damage
        player_damage_c = colored(player_damage,"blue")
        enemy_name_c = colored(enemy_name,"light_red")
        print(f"You attacked {enemy_name_c} and dealt {player_damage_c} damage!")
        time.sleep(1)

        if enemy_hp <= 0:
            print(f"The {enemy_name} died!")
            time.sleep(0.5)
            if enemy_name == "Goblin":
                loot = random.randint(50,200) 
            elif enemy_name == "Romagna":
                loot = random.randint(100,300) 
                Coins += loot
            elif enemy_name == "Bat":
                loot = random.randint(500,1000) 
                Coins += loot
            elif enemy_name == "Snake":
                loot = random.randint(4000,4500) 
                Coins += loot
            elif enemy_name == "Scorpion":
                loot = random.randint(42000,65000) 
                Coins += loot
            elif enemy_name == "Void Beast":
                loot = random.randint(115000,150000) 
                Coins += loot
            elif enemy_name == "Golem":
                loot = random.randint(1000,1200) 
                Coins += loot
            elif enemy_name == "Tiger":
                loot = random.randint(5000,7000) 
                Coins += loot
            elif enemy_name == "Mummy":
                loot = random.randint(35000,50000) 
                Coins += loot
            elif enemy_name == "Shadow Entity":
                loot = random.randint(100000,150000) 
                Coins += loot

            print(f"Gained {loot} Coins!")
            return loot

        enemy_damage = random.randint(enemy_list[enemy_name]["min_damage"], enemy_list[enemy_name]["max_damage"])

        # Enemy
        player_hp -= enemy_damage
        enemy_damage_c = colored(enemy_damage,"red")
        print(f"The {enemy_name} attacked and dealt {enemy_damage_c} damage!")
        time.sleep(0.5)

        if player_hp <= 0:
            print("You Died.")
            return 0  
    return 0  





def explore_world(world):
    global Money, cave_unlocked, bonus_multiplier
    if world == "Forest":
        print(colored("Farming in the Forest...","green"))
        print()
        items = forest_items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Cave":
        print(colored("Farming in the Cave...","grey"))
        print()
        items = cave_items
        weights = (30, 15, 10, 8, 6)
    elif world == "Jungle":
        print(colored("Farming in the Jungle...","green"))
        print()
        items = Jungle_items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Desert":
        print(colored("Farming in the Desert...","yellow"))
        print()
        items = Desert_Items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Void":
        print(colored("Farming in the Void...","magenta"))
        print()
        items = Void_items
        weights = (40, 20, 15, 10, 6, 5, 1)

    while True:
        random_item = random.choices(list(items.keys()), weights=weights, k=1)[0]
        money_added = items.get(random_item, 0) * bonus_multiplier
        Money += money_added
        print(f"You found {random_item}! Added ${money_added} (+${money_added}) Total money: ${Money}")
        time.sleep(cooldowntime)
        menu = input("Write whatever to stop exploring or type 'c' to continue: ")
        print()
        if menu != "c":
            break



while condizione:
    print("---------------------")
    inputpage()
    choice = input("What would you like to do? ")

    # Farm
    if choice == "1":
        print(colored("Select World:","blue"))
        print(colored("1. Forest","green"))
        if cave_unlocked:
            print(colored("2. Cave","light_cyan"))
        else:
            print(colored("2. Cave (Unlock for $15K)","light_cyan"))
        if jungle_unlocked:
            print(colored("3. Jungle","light_green"))
        else:
            print(colored("3. Jungle (Unlock for $50K)","light_green"))
        if Desert_unlocked:
            print(colored("4. Desert","yellow"))
        else:
            print(colored("4. Desert (Unlock for $250K)","yellow"))
        if Void_unlocked:
            print("5. Void")
        else:
            print(colored("5. Void (Unlock for $1M)","magenta"))
        world_choice = input("Enter your choice: ")

        # Forest Farming
        if world_choice == "1":
            explore_world("Forest")

        # Cave farming
        elif world_choice == "2":
            if not cave_unlocked and Money >= 15000:
                Money -= 15000
                cave_unlocked = True
                print("You bought a ticket to the Cave and unlocked it!")
                explore_world("Cave")
            elif cave_unlocked:
                explore_world("Cave")
            else:
                print("Sorry, you don't have enough money to unlock the Cave.")
        # Jungle
        elif world_choice == "3":
            if not jungle_unlocked and Money >= 50000:
                Money -= 50000
                jungle_unlocked = True
                print("You bought a ticket to the Jungle and unlocked it!")
                explore_world("Jungle")
            elif jungle_unlocked:
                explore_world("Jungle")
            else:
                print("Sorry, you don't have enough money to unlock the Jungle.")
        # Desert
        elif world_choice == "4":
            if not Desert_unlocked and Money >= 250000:
                Money -= 250000
                Desert_unlocked = True
                print("You bought a ticket to the Desert and unlocked it!")
                explore_world("Desert")
            elif jungle_unlocked:
                explore_world("Desert")
            else:
                print("Sorry, you don't have enough money to unlock the Desert.")
        # Void
        elif world_choice == "5":
            if not Void_unlocked and Money >= 1000000:
                Money -= 1000000
                Void_unlocked = True
                print("You bought a ticket to the Void and unlocked it!")
                explore_world("Void")
            elif Void_unlocked:
                explore_world("Void")
            else:
                print("Sorry, you don't have enough money to unlock the Void.")

    # Shop
    elif choice == "2":
        print("Welcome to the Shop!")
        
        # Display X2Pass if available
        if pass_remaining > 0:
            x2pass_c = (colored("X2Pass","light_magenta"))
            X2Price_c = (colored(X2Price,"yellow"))
            print(f"-1. {x2pass_c} (Costs ${X2Price_c}) - {pass_remaining} remaining")
        else:
            print(f"-1. {x2pass_c} - Out of stock")

        # Display new swords
        for index, (sword, details) in enumerate(new_swords.items(), start=2):
            stock = details["stock"]
            price = details["price"]
            damage = details["damage"]
            sword_c = (colored(sword,"light_cyan"))
            price_c = (colored(price,"yellow"))
            if stock > 0:
                print(f"-{index}. {sword_c} (Costs {format_price(price)}) - {stock} remaining, Damage: {damage}")
            else:
                print(f"-{index}. {sword_c} - Out of stock")

        # Display power-ups
        for index, (power_up, details) in enumerate(power_ups.items(), start=len(new_swords) + 2):
            stock = details["stock"]
            price = details["price"]
            power_up_c = (colored(power_up,"green"))
            price_c = (colored(price,"yellow"))
            if stock > 0:
                if "multiplier" in details:
                    multiplier = details["multiplier"]
                    print(f"-{index}. {power_up_c} (Costs {format_price(price)}) - {stock} remaining, Multiplier: {multiplier}")
                elif "activate_godpass" in details:
                    print(f"-{index}. {power_up_c} (Costs {format_price(price)}) - {stock} remaining, Activates Godpass")
            else:
                print(f"-{index}. {power_up} - Out of stock")

        # Display armor
        for index, (armor_name, details) in enumerate(armor.items(), start=len(new_swords) + len(power_ups) + 2):
            stock = details["stock"]
            price = details["price"]
            hp = details["hp"]
            armor_c = (colored(armor_name,"light_red"))
            if stock > 0:
                print(f"-{index}. {armor_c} (Costs {format_price(price)}) - {stock} remaining, HP: {hp}")
            else:
                print(f"-{index}. {armor_c} - Out of stock")

        shop_choice = input("What would you like to buy? ")

        # Purchase X2Pass
        if shop_choice == "1" and pass_remaining > 0:
            if Money >= X2Price:
                Money -= X2Price
                bonus_multiplier *= 2
                print("You bought the X2Pass successfully! Now you will get 2x for all your earnings!")
                pass_remaining -= 1
                X2Price *= 2  # Increase price of X2Pass after each purchase
            else:
                print("Sorry, you don't have enough money to buy this item.")
        elif shop_choice == "1" and pass_remaining == 0:
            print("X2Pass is out of stock.")

        # Purchase new swords
        elif shop_choice in [str(i) for i in range(2, 2 + len(new_swords))]:
            item_index = int(shop_choice) - 2
            sword_names = list(new_swords.keys())
            selected_sword = sword_names[item_index]
            sword_details = new_swords[selected_sword]
            stock = sword_details["stock"]
            price = sword_details["price"]

            if stock > 0:                                                                                                                       
                if Money >= price:
                    Money -= price
                    print(f"You bought {selected_sword} successfully!")                                 
                    new_swords[selected_sword]["stock"] -= 1

                    if swordequipped == "":
                     swordequipped = selected_sword
                     player_damage = new_swords[selected_sword]["damage"]
                     print(f"Equipped {selected_sword}. Player Damage increased to {player_damage}!")
                    elif player_damage > new_swords[selected_sword]["damage"]:
                     print(f"You didnt equip the {selected_sword} because you already have a stronger one")
                    else:
                        swordequipped = selected_sword
                        player_damage = new_swords[selected_sword]["damage"]
                        print(f"Equipped {selected_sword}. Player Damage increased to {player_damage}!")
                else:
                    print("Sorry, you don't have enough money to buy this item.")
            else:
                print("This sword is out of stock.")

        # Purchase power-ups
        elif shop_choice in [str(i) for i in range(2 + len(new_swords), 2 + len(new_swords) + len(power_ups))]:
            item_index = int(shop_choice) - (2 + len(new_swords))
            power_up_names = list(power_ups.keys())
            selected_power_up = power_up_names[item_index]
            power_up_details = power_ups[selected_power_up]
            stock = power_up_details["stock"]
            price = power_up_details["price"]

            if stock > 0:
                if Money >= price:
                    Money -= price
                    print(f"You bought {selected_power_up} successfully!")
                    power_ups[selected_power_up]["stock"] -= 1
                    if "multiplier" in power_up_details:
                        multiplier = power_up_details["multiplier"]
                        bonus_multiplier *= multiplier
                        print(f"Bonus multiplier increased to {bonus_multiplier}!")
                    elif "activate_godpass" in power_up_details:
                        godpass = True
                        print("Godpass activated!")
                else:
                    print("Sorry, you don't have enough money to buy this item.")
            else:
                print("This power-up is out of stock.")

        # Purchase armor
        elif shop_choice in [str(i) for i in range(2 + len(new_swords) + len(power_ups), 2 + len(new_swords) + len(power_ups) + len(armor))]:
            item_index = int(shop_choice) - (2 + len(new_swords) + len(power_ups))
            armor_names = list(armor.keys())
            selected_armor = armor_names[item_index]
            armor_details = armor[selected_armor]
            stock = armor_details["stock"]
            price = armor_details["price"]
            hp = armor_details["hp"]

            if stock > 0:
                if Money >= price:
                    Money -= price
                    print(f"You bought {selected_armor} successfully!")
                    armor[selected_armor]["stock"] -= 1
                    if armor_equipped == "":
                     armor_equipped = selected_armor
                     player_hp += hp  
                     print(f"Equipped {selected_armor}. Player HP increased by {hp}!")
                    elif armor[armor_equipped]["hp"] > armor[selected_armor]["hp"]:
                     print(f"You didnt equip the {selected_armor} because you already have a stronger one")
                    else:
                        armor_equipped = selected_armor
                        player_hp += hp 
                        print(f"Equipped {selected_armor}. Player HP increased by {hp}!")

                else:
                    print("Sorry, you don't have enough money to buy this item.")
            else:
                print("This armor is out of stock.")



    # Fights
    elif choice == "3":
        if not swordequipped == "":
            print(colored("Select World:","blue"))
            print(colored("1. Forest","green"))
            if CaveTicket:
                print(colored("2. Cave","light_cyan"))
            else:
                print(colored("2. Cave (Unlock for £15K)","light_cyan"))
            if JungleTicket:
                print(colored("3. Jungle","light_green"))
            else:
                print(colored("3. Jungle (Unlock for £50K)","light_green"))
            if DesertTicket:
                print(colored("4. Desert","yellow"))
            else:
                print(colored("4. Desert (Unlock for £250K)","yellow"))
            if VoidTicket:
                print(colored("5. Void","magenta"))
            else:
                print(colored("5. Void (Unlock for £1M)","magenta"))
            
            world_choice = input(colored("Enter your choice: ","cyan"))
            
            if world_choice == "1":
                print("Entering the forest...")
                while True:
                    enemy_list = ["Goblin", "Romagna"]
                    random_enemy = random.choice(enemy_list)
                    coins_gained = initiate_battle(random_enemy, random.randint(100, 300), armor_equipped,player_damage)
                    Coins += coins_gained
                    user_input = input("Write 'E' to stop fighting: ")
                    if user_input.lower() == "e":
                        break
                    else:
                        continue
            elif world_choice == "2":
                if not CaveTicket and Coins >= 15000:
                    Coins -= 15000
                    CaveTicket = True
                    print("You bought a ticket to the Cave and unlocked it!")
                    print("Entering the cave...")
                while CaveTicket:
                    enemy_list = ["Bat", "Golem"]
                    random_enemy = random.choice(enemy_list)
                    coins_gained = initiate_battle(random_enemy, random.randint(300, 800), armor_equipped,player_damage)
                    Coins += coins_gained
                    user_input = input("Write 'E' to stop fighting: ")
                    if user_input.lower() == "e":
                        break
                else:
                 print("you dont have enough coins")
            elif world_choice == "3":
                if not JungleTicket and Coins >= 50000:
                    Coins -= 50000
                    JungleTicket = True
                    print("You bought a ticket to the Jungle and unlocked it!")
                print("Entering the jungle...")
                while JungleTicket:
                    enemy_list = ["Snake", "Tiger"]
                    random_enemy = random.choice(enemy_list)
                    coins_gained = initiate_battle(random_enemy, random.randint(1000, 2100), armor_equipped,player_damage)
                    Coins += coins_gained
                    user_input = input("Write 'E' to stop fighting: ")
                    if user_input.lower() == "e":
                        break
            elif world_choice == "4":
                if not DesertTicket and Coins >= 250000:
                    Coins -= 250000
                    DesertTicket = True
                    print("You bought a ticket to the Desert and unlocked it!")
                print("Entering the desert...")
                while DesertTicket:
                    enemy_list = ["Scorpion", "Mummy"]
                    random_enemy = random.choice(enemy_list)
                    coins_gained = initiate_battle(random_enemy, random.randint(2500, 4000), armor_equipped,player_damage)
                    Coins += coins_gained
                    user_input = input("Write 'E' to stop fighting: ")
                    if user_input.lower() == "e":
                        break
            elif world_choice == "5":
                if not VoidTicket and Coins >= 1000000:
                    Coins -= 1000000
                    VoidTicket = True
                    print("You bought a ticket to the Void and unlocked it!")
                print("Entering the void...")
                while VoidTicket:
                    enemy_list = ["Void Beast", "Shadow Entity"]
                    random_enemy = random.choice(enemy_list)
                    coins_gained = initiate_battle(random_enemy, random.randint(1000, 5000), armor_equipped,player_damage)
                    Coins += coins_gained
                    user_input = input("Write 'E' to stop fighting: ")
                    if user_input.lower() == "e":
                        break
        else:
            print("You can't fight without a sword, buy one at the shop.")




    # Quit
    elif choice == "4":
        print(colored("Leaving...","cyan"))
        time.sleep(0.5)
        condizione = False

print(colored("Goodbye! Thanks for playing Untitled Farming Game.","blue"))
