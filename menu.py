from stopwatch import stopwatch_main
from palindrome import palindrome_main
from sort import sort_main
from dice import dice_main
from passwordgen import password_main
import os

menu = True

def blank():
    return
def menu():
    menu = True

    while menu == True:
        # Clear CLI
        os.system('cls||clear')
        
        # Menu Dict
        dMenu = {
            "1": ("Stopwatch", stopwatch_main),
            "2": ("Palindrome Checker", palindrome_main),
            "3": ("Sort Inputs", sort_main),
            "4": ("Dice Roll", dice_main),
            "5": ("Password Generator", password_main),
            "6": ("Exit", blank)
        }

        # Menu Output
        for i in sorted(dMenu):
            print('{}) {}'.format(i, dMenu[i][0]))

        # Menu Input
        sChoice = input("    -> ")

        # Choice Validation
        if int(sChoice) == len(dMenu):
            menu = False
        elif sChoice in dMenu and int(sChoice) != len(dMenu):
            dMenu[sChoice][1]()
        else:
            input("No such menu option")

if __name__ == "__main__":
    menu()