# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import timeit


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    loop = True
    while loop:

        print("""\nMain Menu
        1:Spell Check a Word (Linear search
        2: Spell Check a Word (Binary Search)
        3: Spell Check Alice In Wonderland (Linear Search)
        4: Spell Check Alice In Wonderland (Binary Search)
        5: Exit
        """)
        Number = int(input("Please Enter the command: "))
        if Number == 1:
            item = input("Please Enter the word you would like to search for: ")
            start = timeit.timeit()
            if item in dictionary:
                for i in range(len(dictionary)):
                    if dictionary[i] == item:
                        print(i)

            else:
                print("Sorry " + item + " was not found in the dictionary")
            end = timeit.timeit()
            print(end - start)
        elif Number == 2:
            li = 0
            hi = len(dictionary) - 1
            item = input("Please Enter the word you would like to search for: ")
            start = timeit.timeit()
            if item in dictionary:
                while li <= hi:
                    mi = (hi+li)//2
                    if item == dictionary[mi]:
                        print(mi)
                        break
                    elif item < dictionary[mi]:
                        hi = mi -1
                    elif item > dictionary[mi]:
                        li = mi + 1
            else:
                print("Sorry " + item + " was not found in dictionary")
            end = timeit.timeit()
            print(end - start)
        elif Number == 3:
            wordsNotFound = 0
            for i in range(len(aliceWords)):
                if aliceWords[i] not in dictionary:
                    wordsNotFound + 1
            print(wordsNotFound)
        elif Number ==4:
            wordsNotFound = 0

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
