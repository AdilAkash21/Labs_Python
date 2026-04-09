import random

rolls = []
for i in range(10):
    rolls.append(str(random.randint(1, 6)))

print(" ".join(rolls))