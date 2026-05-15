# Flatten a Nested List (One Level Deep)


nested = [10, [20, 30], 40, [50, 60]]

flat = []

for item in nested:

    if type(item) == list:

        for value in item:
            flat.append(value)

    else:
        flat.append(item)

print(flat)

