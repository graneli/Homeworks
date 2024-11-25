import random

matrix = [[random.randint(100,1000) for _ in range(4)] for _ in range(4)]

for row in matrix:
    print(row)
