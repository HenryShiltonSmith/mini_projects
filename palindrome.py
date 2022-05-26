def palindrome_main():
    text = input("\nPlease give me an input: ")
    if text == text[::-1]:
        underIs = "\u0332".join("IS")
        print("Your string " + underIs + " a palindrome")
        input("Press ENTER to return to the menu.")
    else:
        underNot = "\u0332".join("NOT")
        print("Your string is " + underNot + " a palindrome")
        input("Press ENTER to return to the menu.")

    return