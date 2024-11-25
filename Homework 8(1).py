def is_anagram():
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")

    word1 = word1.replace(" ","").lower()
    word2 = word2.replace(" ","").lower()

    if len(word1) != len(word2):
        print("This is not an anagram!")
        return False

    list1 = list(word1)
    list2 = list(word2)

    list1.sort()
    list2.sort()

    if list1 == list2 :
        print ("This is an anagram!")
        return True

    print("This is not an anagram!")
    return False

is_anagram()