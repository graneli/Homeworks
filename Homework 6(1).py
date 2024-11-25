sentence = input("Enter your sentence: ").lower()
words = sentence.split()

countMyWords = {}

for word in words:
    if word in countMyWords:
        countMyWords[word] +=1
    else:
        countMyWords[word] = 1

print(countMyWords)