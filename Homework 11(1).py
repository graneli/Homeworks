def lines_1000():
    with open('file1.txt', 'w') as file:
        for i in range(1, 1001):
            file.write(f"Line {i}\n")

def count_lines():
    with open('file1.txt', 'r') as file:
        lines = file.readlines()
        filled_lines = sum(1 for line in lines if line.strip())
        print(f"Total lines: {len(lines)}")
        print(f"Filled lines: {filled_lines}")

lines_1000()
count_lines()
