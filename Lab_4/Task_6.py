# Transpose a Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

transpose = []

for i in range(cols):

    new_row = []

    for j in range(rows):
        new_row.append(matrix[j][i])

    transpose.append(new_row)

for row in transpose:
    print(row)