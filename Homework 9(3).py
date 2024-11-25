def reverse_string(word):
    if len(word)==0:
        return word
    else:
       return word[-1] + reverse_string(word[:-1])

result = reverse_string(input("Write your sentence: "))
print(result)
