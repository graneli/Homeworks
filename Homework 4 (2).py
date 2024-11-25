text = input("Enter your text: ")

ascii_values = []

for char in text:
    ascii_values.append(ord(char))

print("Your ascii values:", ascii_values)