import random
import time

Money = 1500000
Coins = 1500000
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

if godpass:
    bonus_multiplier = bonus_multiplier * 15394

cooldowntime = 1.5
cave_unlocked = False
jungle_unlocked = False
Desert_unlocked = False
Void_unlocked = False
pass_remaining = 10
coinswordremaining = 1
power_up_remaining = 1



def format_price(price):
    if price >= 1_000_000:
        return f"${price/1_000_000:.1f}M"
    elif price >= 1_000:
        return f"${price/1_000:.1f}K"
    else:
        return f"${price}"



def inputpage():
    print("-1 Farm")
    print("-2 Shop")
    print("-3 Fight")
    print("-4 Quit")
    print(f"Money: ${Money}")
    print(f"Coins: £{Coins}")

import random
import time

def initiate_battle(enemy_name, enemy_hp):
    enemy_list = {
    "Goblin": {"min_damage": 5, "max_damage": 16},
    "Bat": {"min_damage": 150, "max_damage": 300},
    "Snake": {"min_damage": 200, "max_damage": 400},
    "Scorpion": {"min_damage": 250, "max_damage": 500},
    "Void Beast": {"min_damage": 300, "max_damage": 600},
    "Romagna": {"min_damage": 15, "max_damage": 25},
    "Golem": {"min_damage": 300, "max_damage": 600},
    "Tiger": {"min_damage": 350, "max_damage": 700},
    "Mummy": {"min_damage": 400, "max_damage": 800},
    "Shadow Entity": {"min_damage": 450, "max_damage": 900}
}
    global Coins
    player_hp = 100 
    enemy_damage = 10  
    player_damage = 500000  
    if swordequipped == "Excalibur":
        player_damage = 500
    elif swordequipped == "Legendary Sword":
        player_damage = 250
    elif swordequipped == "Coin Sword":
        player_damage = 50
    print(f"Hai incontrato un {enemy_name} con {enemy_hp} HP!")
    time.sleep(1)

    while player_hp > 0 and enemy_hp > 0:
        # Attack
        enemy_hp -= player_damage
        print(f"You attacked {enemy_name} and dealt {player_damage} damage!")
        time.sleep(1)

        if enemy_hp <= 0:
            print(f"The {enemy_name} died!")
            time.sleep(0.5)
            if enemy_name == "Goblin":
                loot = random.randint(50,200) 
            elif enemy_name == "Romagna":
                loot = random.randint(100,300) 
            Coins += loot
            print(f"Gained {loot} Coins!")
            return loot

        enemy_damage = random.randint(enemy_list[enemy_name]["min_damage"], enemy_list[enemy_name]["max_damage"])

        # Enemy
        player_hp -= enemy_damage
        print(f"The {enemy_name} attacked and dealt {enemy_damage} damage!")
        time.sleep(0.5)

        if player_hp <= 0:
            print("You Died.")
            return 0  
    return 0  





def explore_world(world):
    global Money, cave_unlocked, bonus_multiplier
    if world == "Forest":
        print("Farming in the Forest...")
        print()
        items = forest_items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Cave":
        print("Farming in the Cave...")
        print()
        items = cave_items
        weights = (30, 15, 10, 8, 6)
    elif world == "Jungle":
        print("Farming in the Jungle...")
        print()
        items = Jungle_items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Desert":
        print("Farming in the Desert...")
        print()
        items = Desert_Items
        weights = (40, 15, 10, 8, 5, 3, 2)
    elif world == "Void":
        print("Farming in the Void...")
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


condizione = True

new_swords = {
    "Coin Sword": {"price": 15000, "stock": coinswordremaining, "damage": 50},
    "Legendary Sword": {"price": 100000, "stock": legendaryS, "damage": 250},
    "Excalibur": {"price": 500000, "stock": excalibur, "damage": 500}
}

power_ups = {
    "Gold Chain": {"price": 500000, "stock": GoldC, "multiplier": 5},
    "Golden Statue": {"price": 10000000, "stock": goldS, "activate_godpass": True}
}

while condizione:
    print("---------------------")
    inputpage()
    choice = input("What would you like to do? ")

    # Farm
    if choice == "1":
        print("Select World:")
        print("1. Forest")
        if cave_unlocked:
            print("2. Cave")
        else:
            print("2. Cave (Unlock for $15K)")
        if jungle_unlocked:
            print("3. Jungle")
        else:
            print("3. Jungle (Unlock for $50K)")
        if Desert_unlocked:
            print("4. Desert")
        else:
            print("4. Desert (Unlock for $250K)")
        if Void_unlocked:
            print("5. Void")
        else:
            print("5. Void (Unlock for $1M)")
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
        if pass_remaining > 0:
            print(f"-1. X2Pass (Costs ${X2Price}) - {pass_remaining} remaining")
        else:
            print("-1. X2Pass - Out of stock")

        # Print new swords
        for index, (sword, details) in enumerate(new_swords.items(), start=2):
         stock = details["stock"]
         price = details["price"]
         damage = details["damage"]
         if stock > 0:
            print(f"-{index}. {sword} (Costs {format_price(price)}) - {stock} remaining, Damage: {damage}")
         else:
            print(f"-{index}. {sword} - Out of stock")

    # Stampare power-up
        # Stampare power-up
        for index, (power_up, details) in enumerate(power_ups.items(), start=len(new_swords) + 2):
         stock = details["stock"]
         price = details["price"]
         if stock > 0:
          if "multiplier" in details:
            multiplier = details["multiplier"]
            print(f"-{index}. {power_up} (Costs {format_price(price)}) - {stock} remaining, Multiplier: {multiplier}")
          elif "activate_godpass" in details:
            print(f"-{index}. {power_up} (Costs {format_price(price)}) - {stock} remaining, Activates Godpass")
         else:
          print(f"-{index}. {power_up} - Out of stock")


        shop_choice = input("What would you like to buy? ")

        if shop_choice == "1" and pass_remaining > 0:
         if Money >= X2Price:
          Money -= X2Price
          bonus_multiplier *= 2
          print("You bought the X2Pass successfully! Now you will get 2x for all your earnings!")
          pass_remaining -= 1
        # Aggiornare il prezzo del X2Pass
          X2Price *= 2  # Aumenta il prezzo del 80% dopo ogni acquisto
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
                    swordequipped = selected_sword
                    print(f"Equipped {selected_sword} ")
                    new_swords[selected_sword]["stock"] -= 1
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

    # Fights
    elif choice == "3":
     if not swordequipped == "":
         print("Select World:")
         print("1. Forest")
         if cave_unlocked:
            print("2. Cave")
         else:
            print("2. Cave (Unlock for £15K)")
         if jungle_unlocked:
            print("3. Jungle")
         else:
            print("3. Jungle (Unlock for £50K)")
         if Desert_unlocked:
            print("4. Desert")
         else:
            print("4. Desert (Unlock for £250K)")
         if Void_unlocked:
            print("5. Void")
         else:
            print("5. Void (Unlock for £1M)")
            world_choice = input("Enter your choice: ")
         if world_choice == "1":
           print("Entering the forest...")
           while True:
             enemy_list = ["Goblin", "Romagna"]
             random_enemy = random.choice(enemy_list)
             coins_gained = initiate_battle(random_enemy, random.randint(100, 300))
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
                    while True:
                        enemy_list = ["Bat", "Golem"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(300, 800))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                elif CaveTicket:
                    print("Entering the cave...")
                    while True:
                        enemy_list = ["Bat", "Golem"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(300, 800))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                else:
                    print("Sorry, you don't have enough coins to unlock the Cave.")

         elif world_choice == "3":
                if not JungleTicket and Coins >= 50000:
                    Coins -= 50000
                    JungleTicket = True
                    print("You bought a ticket to the Jungle and unlocked it!")
                    print("Entering the jungle...")
                    while True:
                        enemy_list = ["Snake", "Tiger"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(1000, 2100))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                elif JungleTicket:
                    print("Entering the jungle...")
                    while True:
                        enemy_list = ["Snake", "Tiger"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(1000, 2100))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                else:
                    print("Sorry, you don't have enough coins to unlock the Jungle.")

         elif world_choice == "4":
                if not DesertTicket and Coins >= 250000:
                    Coins -= 250000
                    DesertTicket = True
                    print("You bought a ticket to the Desert and unlocked it!")
                    print("Entering the desert...")
                    while True:
                        enemy_list = ["Scorpion", "Mummy"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(2500, 4000))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                elif DesertTicket:
                    print("Entering the desert...")
                    while True:
                        enemy_list = ["Scorpion", "Mummy"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(2500, 4000))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                else:
                    print("Sorry, you don't have enough coins to unlock the Desert.")

         elif world_choice == "5":
                if not VoidTicket and Coins >= 1000000:
                    Coins -= 1000000
                    VoidTicket = True
                    print("You bought a ticket to the Void and unlocked it!")
                    print("Entering the void...")
                    while True:
                        enemy_list = ["Void Beast", "Shadow Entity"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(1000, 5000))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                elif VoidTicket:
                    print("Entering the void...")
                    while True:
                        enemy_list = ["Void Beast", "Shadow Entity"]
                        random_enemy = random.choice(enemy_list)
                        coins_gained = initiate_battle(random_enemy, random.randint(1000, 5000))
                        Coins += coins_gained
                        user_input = input("Write 'E' to stop fighting: ")
                        if user_input.lower() == "e":
                            break
                else:
                    print("Sorry, you don't have enough coins to unlock the Void.")
     else:
            print("You can't fight without a sword, buy one at the shop.")




    # Quit
    elif choice == "4":
        print("Leaving...")
        time.sleep(0.5)
        condizione = False

print("Goodbye! Thanks for playing Untitled RNG.")