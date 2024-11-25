strings = ["natia","ana","ina","anana"]
palindrome = list(filter(lambda s: s==s[::-1], strings))

print(palindrome)