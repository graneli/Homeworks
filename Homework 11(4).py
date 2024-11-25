def palind_file ():
    with open('palindrome_file.txt', 'w') as file:
        file.write("ninin\n")
        file.write("lalala\n")
        file.write("kukuk\n")


def find_palind(palindrome_file):
    def is_palind(s):
        s = s.strip()
        return s == s[::-1]

    with open(palindrome_file, 'r') as file:
        lines = file.readlines()
        palindromes = [line.strip() for line in lines if is_palind(line.strip())]
        print("Palindromes:", palindromes)

palind_file()
find_palind('palindrome_file.txt')
