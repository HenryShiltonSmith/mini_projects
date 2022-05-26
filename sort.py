def sort_main():
    arr1 = [10, 1, 144, 6, 16, 32, 94, 4, 3, 8]
    arr2 = ["a", "z", "r", "h", "o", "k"]
    word = "JDOPAJO"
    
    arr1.sort()
    sortedLetters = sorted(arr2)
    sortedString = ''.join(sorted(word))
    
    print("Sorting Method #1 - " + str(arr1) + "\n")   #
    print("Sorting Method #2 - " + str(sortedLetters) + "\n")
    print("Sorted String - " + str(sortedString) + "\n")    
    input("Press ENTER to return to the menu.")