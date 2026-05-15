# Unique Elements with Frequencies (No dict)


data = [5, 3, 5, 2, 3, 8, 1, 2, 8]

unique = []
frequency = []

for item in data:

    exists = False

    for i in range(len(unique)):

        if item == unique[i]:
            frequency[i] += 1
            exists = True
            break

    if not exists:
        unique.append(item)
        frequency.append(1)

for i in range(len(unique)):
    print(unique[i], "->", frequency[i])
    
    