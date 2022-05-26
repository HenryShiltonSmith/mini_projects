import random
import os
import string

def password_main():
    sPossible = ""

    dOptions = {
            "1": ("numbers", string.digits),
            "2": ("capitals", string.ascii_uppercase),
            "3": ("lower case", string.ascii_lowercase),
            "4": ("symbols", string.punctuation)
        }

    for i in dOptions:
        bValid = False

        while bValid == False:
            sChoice = input("Do you wish to use " + dOptions[i][0] + "? (Y or N) \n    -> ")
        
            if sChoice.lower() == "y":
                sPossible = "".join(dOptions[i][1])
                bValid = True
            elif sChoice.lower() != "y" or sChoice.lower() != "n":
                print("\nPlease select a valid option")
                bValid = False

    iLength = input("\nHow long should the password be? \n    -> ")

    os.system('cls||clear')
    print("Your password is...")
    input("".join(random.sample(sPossible, int(iLength))))