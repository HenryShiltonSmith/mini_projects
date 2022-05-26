import random
import os

def dice_main():
    os.system('cls||clear')

    print("WELCOME TO THE DICE ROLLER. \n")
    iSides = input("Please input the number of sides on your dice \n  -> ")
    iNumber = input("Please input the number of dice you wish to roll \n  -> ")

    iCount = 0
    iaRolls = []

    while iCount < int(iNumber):
        iHolder = random.randint(1, int(iSides))
        iaRolls.append(iHolder)

        iCount += 1

    print("Your rolls are - ", end = "" )
    for i in iaRolls:
        print(str(i) + ", ", end = "")
    
    print("\nYour total roll is - " + str(sum(iaRolls)))
    input("Press ENTER to return to the menu.")