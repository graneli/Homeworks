
text = input("Enter your text: ")

text2=text.lower()

if text2 == text2[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")