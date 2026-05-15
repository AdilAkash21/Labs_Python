# Josephus Problem


n = 7
k = 3

people = []

for i in range(1, n + 1):
    people.append(i)

index = 0

elimination_order = []

while len(people) > 1:

    index = (index + k - 1) % len(people)

    eliminated = people.pop(index)

    elimination_order.append(eliminated)

print("Elimination order:")

for person in elimination_order:
    print(person, end=" ")

print()

print("Survivor:", people[0])

