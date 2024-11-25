def count_character():

    sentence = input("Enter your sentence: ")
    char = input("Enter a character to count: ")
    count = 0

    for letter in sentence:
        if letter == char:
            count += 1

    print("The character '" + char + "' appears " + str(count) + " times in your sentence.")

count_character()
