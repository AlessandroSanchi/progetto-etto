import random
import os
import art
Money = 0
def inputpage():
 print("-1 Farm")
 print("-2 Shop")
 print("-3 Fight")
 print("-4 Quit")

oggetti = ["sassi"]
from art import *
Art= text2art("Untilted rng game") # Return ASCII text (default font) and default chr_ignore=True 
print(Art)

print(f"Money:{Money}")
inputpage()

condizione = True


while condizione == True:
 input = input("che si fa? ")
match input:
      case "1":
        print("Farming...")#"banning random people", "getting these money"])
        print("hai trovato un sasso")
        Money = Money + 1
        print(Money)
        condizione == True
        

      case "2":
        print("Welcome to the Shop!")



      case "3": 
        print("Fighting...")


      case "4":
        print("Leaving...")
        condizione = False
    

