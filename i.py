import random                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
import time

Money = 104
bonus_multiplier = 1
godpass = False # non potenzialmente rotto (dev cheat)
X2Price = 150  # Prezzo iniziale del raddoppia soldi
CoinSword =  1
swordequipped = ""



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

if  godpass:
 bonus_multiplier = bonus_multiplier * 15394  #cambia il numero se vuoi tip: " 999999999999999999999999999999 "
 
cooldowntime = 1
cave_unlocked = False
jungle_unlocked = False
Desert_unlocked = False
Void_unlocked = False
pass_remaining = 10  # x2 passes stock
coinswordremaining = 1

goblin = 10 #hp 
Romagna = 50 #hp


def inputpage():
    print("-1 Farm")
    print("-2 Shop")
    print("-3 Fight")
    print("-4 Quit")
    print(f"Money: ${Money}")

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

while condizione:
    print()
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
        #Jungle
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
        #Desert
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
        #Void
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
        if coinswordremaining > 0:
         print(f"-2 Coin Sword |5dmg (Costs ${CoinSword}) - {coinswordremaining} remaining")   
        else: 
         print("-2 Coin Sword |5dmg - out of stock")
        print("-3. Leave Shop")
        shop_choice = input("What would you like to buy? ")
        if shop_choice == "1" and pass_remaining > 0:
            if Money >= X2Price:
                Money -= X2Price
                bonus_multiplier *= 2
                print("You bought the pass successfully! Item values are doubled now.")
                X2Price = int(X2Price * 2)
                pass_remaining -= 1
            else:
                print("Sorry, you don't have enough money to buy this item.")
        elif shop_choice == "1" and pass_remaining == 0:
            print("X2Pass is out of stock.")

        if shop_choice == "2" and coinswordremaining > 0:
            if Money >= CoinSword:
                Money -= CoinSword
                print("You bought the Coin Sword successfully!")
                swordequipped = CoinSword
                coinswordremaining -= 1
            else:
                print("Sorry, you don't have enough money to buy this item.")
        elif shop_choice == "2" and coinswordremaining == 0:
            print("Coin Sword is out of stock.")

            






    # Fights
    elif choice == "3":
        if not swordequipped == "":
         print("Fighting...")
        else:
            print("Non puoi combattere senza una spada, comprala al negozio")







    # Quit
    elif choice == "4":
        print("Leaving...")
        condizione = False

print("Goodbye! Thanks for playing Untitled RNG.")