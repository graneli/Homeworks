def add_matrices(matrix1, matrix2):
    result = []

    for w in range(len(matrix1)):
        row = []
        for h in range(len(matrix1[0])):
            sum_value = matrix1[w][h] + matrix2[w][h]
            row.append(sum_value)
        result.append(row)
    return result

matrix1 = [
    [5, 1, 3],
    [9, 5, 7],
    [7, 2, 9]
]

matrix2 = [
    [0, 4, 1],
    [2, 1, 7],
    [5, 2, 5]
]

sum_matrix = add_matrices(matrix1, matrix2)

print("Sum of matrices:")
for row in sum_matrix:
    print(row)
