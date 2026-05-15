# Pascal’s Triangle 


n = 5

triangle = []

for i in range(n):

    row = []

    for j in range(i + 1):

        if j == 0 or j == i:
            row.append(1)

        else:
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

    triangle.append(row)

for row in triangle:

    for value in row:
        print(value, end=" ")

    print()