import random
import os
from art import *
import time

Money = 0
oggetti = ["Rock", "Gem", "monete d'oro", "perle"]
e = True
cooldowntime = 3

def inputpage():
    print("-1 Farm")
    print("-2 Shop")
    print("-3 Fight")
    print("-4 Quit")
    print(f"Money: {Money}")

Art = text2art("Untitled RNG")
print(Art)


condizione = True  # Initialize the condition for the while loop

while condizione:
    inputpage()
    choice = input("What would you like to do? ")
    

    if choice == "1":
     e = True
     while e:
        print("Farming...")

        # Simulate finding different items
        randomList = random.choices(oggetti, weights=(80, 10, 5, 2), k=1)
        if randomList[0] == "Rock":
            print("You found a rock!")
            Money += 1
        elif randomList[0] == "Gem":
            print("You found a precious gem!")
            Money += 5
        elif randomList[0] == "monete d'oro":
            print("You found some gold coins!")
            Money += 10
        elif randomList[0] == "perle":
            print("You found a valuable pearl!")
            Money += 8

        print(f"Money: {Money}")
        time.sleep(cooldowntime)
        e = False
        menu = input("Write whatever to stop farming or type 'c' to continue: ")
        if menu == "c":
            e = True



        

        

         

        # Allow continuous farming until another action is chosen
        #farm_choice = input("Continue farming? (Y/N): ")
        #if farm_choice.lower() == "n" or farm_choice.lower() == "N":
         #   e = False
        #elif farm_choice.lower() == "y" or farm_choice.lower() == "Y":
         #       continue
               

    elif choice == "2":
        print("Welcome to the Shop!")
        # Add shop logic here

    elif choice == "3":
        print("Fighting...")
        # Add fight logic here

    elif choice == "4":
        print("Leaving...")
        condizione = False  # Exit the outer loop

print("Goodbye! Thanks for playing Untitled RNG.")
